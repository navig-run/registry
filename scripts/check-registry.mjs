#!/usr/bin/env node
/**
 * check-registry — the publish gate for github.com/navig-run/registry.
 *
 * Fails (exit 1) on anything that must never reach the public registry:
 *   privacy   machine-specific absolute paths, personal identifiers, real emails
 *   secrets   API keys, tokens, private keys
 *   state     seeded user state (.navig/memory|inbox|state) other than examples
 *   json      a .json file that does not parse
 *   catalog   spaces/registry.json entries whose folder is missing, duplicate ids
 *   license   a space without a LICENSE, or one not held by "NAVIG contributors"
 *   identity  author/owner/maintainer fields other than "navig-run"
 *
 * Paths listed in registry/.publish-exclude are not published and not checked.
 *
 *   node scripts/check-registry.mjs            # human report
 *   node scripts/check-registry.mjs --json     # machine-readable
 *   node scripts/check-registry.mjs --only privacy,secrets
 */
import { execFileSync } from 'node:child_process';
import { readFileSync, readdirSync, statSync, lstatSync, existsSync } from 'node:fs';
import { join, relative, sep, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const asJson = args.includes('--json');
const onlyArg = args.find((a) => a.startsWith('--only'));
const only = onlyArg ? new Set((onlyArg.split('=')[1] ?? args[args.indexOf(onlyArg) + 1] ?? '').split(',')) : null;
const enabled = (rule) => !only || only.has(rule);

// ── exclude list ────────────────────────────────────────────────────────────
function globToRegExp(glob) {
  let re = '';
  for (let i = 0; i < glob.length; i++) {
    const c = glob[i];
    if (c === '*' && glob[i + 1] === '*') {
      re += '.*';
      i++;
      if (glob[i + 1] === '/') i++;
    } else if (c === '*') re += '[^/]*';
    else if (c === '?') re += '[^/]';
    else re += c.replace(/[.+^${}()|[\]\\]/g, '\\$&');
  }
  return new RegExp(`^${re}$`);
}
export function loadExcludes(root = ROOT) {
  const f = join(root, '.publish-exclude');
  if (!existsSync(f)) return [];
  return readFileSync(f, 'utf8')
    .split(/\r?\n/)
    .map((l) => l.trim())
    .filter((l) => l && !l.startsWith('#'))
    .map(globToRegExp);
}
export function isExcluded(rel, excludes) {
  return excludes.some((re) => re.test(rel) || re.test(`${rel}/`));
}

// ── walk (never follows links) ──────────────────────────────────────────────
// Only files git TRACKS are published: a plain disk walk shipped untracked local junk
// (`__pycache__/*.pyc` from a test run, which embeds absolute machine paths). Outside a
// git checkout (a fresh export) every file on disk counts.
function trackedFiles(root) {
  try {
    const out = execFileSync('git', ['-C', root, 'ls-files', '-z', '--', '.'], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
    const set = new Set(out.split('\0').filter(Boolean));
    return set.size ? set : null;
  } catch {
    return null;
  }
}
export function publishedFiles(root = ROOT) {
  const excludes = loadExcludes(root);
  const tracked = trackedFiles(root);
  const out = [];
  const walk = (dir) => {
    for (const name of readdirSync(dir)) {
      if (name === '.git') continue;
      const abs = join(dir, name);
      const rel = relative(root, abs).split(sep).join('/');
      if (isExcluded(rel, excludes)) continue;
      const st = lstatSync(abs);
      if (st.isSymbolicLink()) continue; // links are never published
      if (st.isDirectory()) walk(abs);
      else if (!tracked || tracked.has(rel)) out.push(rel);
    }
  };
  walk(root);
  return out.sort();
}

// ── rules ───────────────────────────────────────────────────────────────────
const TEXT_EXT = /\.(md|mdx|txt|json|jsonl|ya?ml|toml|ini|cfg|conf|ps1|psm1|sh|bash|zsh|py|js|mjs|cjs|ts|tsx|html|css|reg|bat|cmd|xml|csv|env|example|gitignore)$/i;
const isText = (rel) => TEXT_EXT.test(rel) || !/\.[^/]+$/.test(rel.split('/').pop());

// A drive-letter path that names a real folder. `C:\path\to\...`, `C:\Users\<you>` and
// `%USERPROFILE%`-style placeholders are allowed: they teach, they do not leak.
// Standard install locations (`C:\Program Files`, `C:\Windows`) are generic, not personal.
const DRIVE_PATH = /\b([A-Za-z]):[\\/]{1,2}(?!<|\{|\$|%|path[\\/]to|your|example|\.\.\.|Program Files|Program\b|Windows\b)([A-Za-z0-9_][^\s"'`<>|,;(){}$%]*)/g;
const UNIX_HOME = /(?:^|[\s"'`(=])\/(?:home|Users)\/(?!<|\{|\$|user\b|you\b|username\b|example\b|me\b|developer\b|navig\b|ubuntu\b|runner\b)([a-z][a-z0-9_.-]*)/g;
// A drive path whose next segment is a placeholder (`C:\Users\<you>`, `D:\{root}`) teaches.
const PLACEHOLDER_TAIL = /^[\\/]?(?:<|\{|\$|%|\.\.\.)/;
const AUTHOR_PLACEHOLDER = /^(your name|\{\{\s*\w+\s*\}\}|<[^>]+>)$/i;
// Personal identifiers come from `.publish-identifiers`, a private list that is never
// published (a public gate must not itself name the people it protects).
function loadIdentity(root) {
  const f = join(root, '.publish-identifiers');
  if (!existsSync(f)) return null;
  const pats = readFileSync(f, 'utf8').split(/\r?\n/).map((l) => l.trim()).filter((l) => l && !l.startsWith('#'));
  return pats.length ? new RegExp(pats.map((p) => `(?:${p})`).join('|'), 'gi') : null;
}
const EMAIL = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b/g;
const EMAIL_OK = /@(?:[a-z0-9-]+\.)*(example|yourserver|your-?domain|your-?company|email|domain|company|acme|test|localhost|navig)\.[a-z]{2,}$|@users\.noreply\.github\.com$|^(you|your|user|me|name|jane\.doe|john\.doe|noreply|no-reply)@/i;
const SECRETS = [
  [/\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{20,}/g, 'API key (sk-…)'],
  [/\bgh[pousr]_[A-Za-z0-9]{30,}/g, 'GitHub token'],
  [/\bAKIA[0-9A-Z]{16}\b/g, 'AWS access key'],
  [/\bxox[abpr]-[A-Za-z0-9-]{10,}/g, 'Slack token'],
  [/-----BEGIN [A-Z ]*PRIVATE KEY-----/g, 'private key'],
  [/\b\d{8,10}:[A-Za-z0-9_-]{35}\b/g, 'Telegram bot token'],
];
const STATE_DIR = /^spaces\/(?:[^/]+\/)*\.navig\/(memory|inbox|state)\/(.+)$/;
const STATE_OK = /(^|\/)(README\.md|\.gitkeep|[^/]+\.example\.[a-z0-9]+)$/i;
const OFFICIAL = 'navig-run';
const LICENSE_HOLDER = /Copyright \(c\) \d{4}(?:-\d{4})? NAVIG contributors/;

export function check(root = ROOT) {
  const findings = [];
  const add = (rule, file, line, message) => findings.push({ rule, file, line, message });
  const files = publishedFiles(root);
  const IDENTITY = loadIdentity(root);
  if (files.length < 50) add('catalog', '.', 0, `only ${files.length} files would be published — refusing a near-empty scan`);

  for (const rel of files) {
    const st = enabled('state') && STATE_DIR.exec(rel);
    if (st && !STATE_OK.test(rel)) add('state', rel, 0, `seeded ${st[1]}/ file — ship ${st[1]}/*.example.* instead`);
    if (!isText(rel)) continue;
    let text;
    try {
      text = readFileSync(join(root, rel), 'utf8');
    } catch (e) {
      add('json', rel, 0, `unreadable: ${e.message}`);
      continue;
    }
    if (enabled('json') && rel.endsWith('.json')) {
      try {
        JSON.parse(text.replace(/^\uFEFF/, ''));
      } catch (e) {
        add('json', rel, 0, `invalid JSON: ${e.message}`);
      }
    }
    const lines = text.split(/\r?\n/);
    lines.forEach((ln, i) => {
      const n = i + 1;
      if (enabled('privacy')) {
        for (const m of ln.matchAll(DRIVE_PATH)) {
          const tail = ln.slice(m.index + m[0].length);
          if (PLACEHOLDER_TAIL.test(tail) && /[\\/]$/.test(m[0])) continue;
          add('privacy', rel, n, `absolute path ${m[0].slice(0, 60)}`);
        }
        for (const m of ln.matchAll(UNIX_HOME)) add('privacy', rel, n, `home path /…/${m[1]}`);
        if (IDENTITY) for (const m of ln.matchAll(IDENTITY)) add('privacy', rel, n, `personal identifier "${m[0]}"`);
        for (const m of ln.matchAll(EMAIL)) if (!EMAIL_OK.test(m[0])) add('privacy', rel, n, `email ${m[0]}`);
      }
      if (enabled('secrets')) for (const [re, what] of SECRETS) for (const _ of ln.matchAll(re)) add('secrets', rel, n, what);
    });
    if (enabled('identity') && rel.endsWith('.json')) {
      try {
        const data = JSON.parse(text.replace(/^\uFEFF/, ''));
        const walk = (o, path) => {
          if (!o || typeof o !== 'object') return;
          for (const [k, v] of Object.entries(o)) {
            if (['author', 'owner', 'maintainer'].includes(k)) {
              const val = typeof v === 'string' ? v : v && typeof v === 'object' ? (v.name ?? v.github ?? '') : '';
              if (val && val !== OFFICIAL && !AUTHOR_PLACEHOLDER.test(val)) add('identity', rel, 0, `${path}${k} = "${val}" (must be "${OFFICIAL}")`);
            } else walk(v, `${path}${k}.`);
          }
        };
        walk(data, '');
      } catch {
        /* reported by the json rule */
      }
    }
  }

  // catalog + license, per published space
  const regPath = join(root, 'spaces', 'registry.json');
  if (enabled('catalog') && existsSync(regPath)) {
    const excludes = loadExcludes(root);
    const reg = JSON.parse(readFileSync(regPath, 'utf8').replace(/^\uFEFF/, ''));
    const entries = Array.isArray(reg.spaces) ? reg.spaces : [];
    const ids = new Map();
    for (const e of entries) {
      const folder = e.path ?? e.id;
      if (ids.has(e.id)) add('catalog', 'spaces/registry.json', 0, `duplicate id ${e.id}`);
      ids.set(e.id, folder);
      if (isExcluded(`spaces/${folder}`, excludes)) add('catalog', 'spaces/registry.json', 0, `${e.id} is listed but its folder is not published`);
      else if (!existsSync(join(root, 'spaces', folder))) add('catalog', 'spaces/registry.json', 0, `${e.id}: folder spaces/${folder} does not exist`);
      // A differing folder must be declared with an explicit `path` (kept only where a
      // paid grant `item:<id>` predates the folder name — changing the id breaks buyers).
      if (e.id !== folder && !e.path) add('catalog', 'spaces/registry.json', 0, `${e.id}: id differs from its folder "${folder}"`);
    }
    if (typeof reg.total === 'number' && reg.total !== entries.length) add('catalog', 'spaces/registry.json', 0, `total says ${reg.total}, ${entries.length} entries`);
    for (const name of readdirSync(join(root, 'spaces'))) {
      const abs = join(root, 'spaces', name);
      if (!statSync(abs).isDirectory() || isExcluded(`spaces/${name}`, excludes)) continue;
      if (!entries.some((e) => (e.path ?? e.id) === name)) add('catalog', `spaces/${name}`, 0, 'folder is not listed in spaces/registry.json');
      if (enabled('license')) {
        const lic = join(abs, 'LICENSE');
        if (!existsSync(lic)) add('license', `spaces/${name}`, 0, 'no LICENSE');
        else if (!LICENSE_HOLDER.test(readFileSync(lic, 'utf8'))) add('license', `spaces/${name}/LICENSE`, 0, 'holder is not "NAVIG contributors"');
      }
    }
  }
  return { files: files.length, findings };
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const { files, findings } = check();
  if (asJson) {
    process.stdout.write(JSON.stringify({ files, findings }, null, 2) + '\n');
  } else {
    const byRule = {};
    for (const f of findings) (byRule[f.rule] ??= []).push(f);
    console.log(`check-registry: ${files} files would be published`);
    for (const [rule, list] of Object.entries(byRule)) {
      console.log(`\n✗ ${rule} — ${list.length}`);
      for (const f of list.slice(0, 400)) console.log(`  ${f.file}${f.line ? `:${f.line}` : ''}  ${f.message}`);
      if (list.length > 400) console.log(`  … ${list.length - 400} more`);
    }
    console.log(findings.length ? `\n✗ ${findings.length} finding(s) — not publishable` : '\n✓ publishable');
  }
  process.exit(findings.length ? 1 : 0);
}
