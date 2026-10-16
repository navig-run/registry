#!/usr/bin/env node
/**
 * export-registry — write the exact tree published to github.com/navig-run/registry.
 *
 *   node scripts/export-registry.mjs <out-dir>
 *
 * Copies every file check-registry.mjs would publish (registry/.publish-exclude applied,
 * links never followed) into <out-dir>, which must be empty or absent. Refuses to export
 * while the publish gate has findings, so a dirty tree can never be pushed by mistake.
 */
import { copyFileSync, existsSync, mkdirSync, readdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { check, publishedFiles } from './check-registry.mjs';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const out = process.argv[2] ? resolve(process.argv[2]) : null;
if (!out) {
  console.error('usage: node scripts/export-registry.mjs <out-dir>');
  process.exit(2);
}
if (existsSync(out) && readdirSync(out).length) {
  console.error(`refusing: ${out} is not empty`);
  process.exit(2);
}
const { findings } = check(ROOT);
if (findings.length) {
  console.error(`refusing: the publish gate has ${findings.length} finding(s) — run node scripts/check-registry.mjs`);
  process.exit(1);
}
const files = publishedFiles(ROOT);
for (const rel of files) {
  const dest = join(out, rel);
  mkdirSync(dirname(dest), { recursive: true });
  copyFileSync(join(ROOT, rel), dest);
}
console.log(`exported ${files.length} files to ${out}`);
