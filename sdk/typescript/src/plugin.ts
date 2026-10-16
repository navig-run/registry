import * as readline from "readline";

/**
 * Build a JSON-RPC response object.
 */
function reply(
  id: unknown,
  payload: { result?: unknown; error?: string }
): object {
  return { id, ...payload };
}

/**
 * NAVIG Plugin SDK — TypeScript / Node.js
 *
 * Implements a JSON-RPC stdio transport so plugins can be written in any
 * Node.js-compatible language and driven by the NAVIG CLI.
 *
 * @example
 * ```ts
 * import { NavigPlugin } from "navig-sdk";
 *
 * const plugin = new NavigPlugin("my-plugin", "1.0.0");
 *
 * plugin.command("greet", async ({ name = "world" }: { name?: string }) => {
 *   return `Hello, ${name}!`;
 * });
 *
 * plugin.run();
 * ```
 */
export class NavigPlugin {
  private readonly _commands = new Map<string, (params: unknown) => unknown>();

  constructor(
    public readonly name: string,
    public readonly version: string = "0.1.0"
  ) {}

  /**
   * Register a command handler.
   *
   * @param name     - JSON-RPC method name.
   * @param handler  - Async or sync function that receives the `params`
   *                   value from the JSON-RPC request and returns the result.
   */
  command(name: string, handler: (params: unknown) => unknown): this {
    this._commands.set(name, handler);
    return this;
  }

  /** Return plugin metadata. */
  meta(): { name: string; version: string; commands: string[] } {
    return {
      name: this.name,
      version: this.version,
      commands: [...this._commands.keys()],
    };
  }

  /**
   * Start the JSON-RPC stdio event loop.
   * Reads newline-delimited JSON from stdin and writes replies to stdout.
   */
  run(): void {
    const rl = readline.createInterface({
      input: process.stdin,
      terminal: false,
    });

    rl.on("line", async (raw) => {
      const line = raw.trim();
      if (!line) return;

      let message: Record<string, unknown>;

      try {
        message = JSON.parse(line) as Record<string, unknown>;
      } catch (err) {
        process.stdout.write(
          JSON.stringify({ error: `JSON parse error: ${err}` }) + "\n"
        );
        return;
      }

      const id = message["id"] ?? null;
      const method = typeof message["method"] === "string" ? message["method"] : "";
      const params = message["params"] ?? {};

      if (!method || !this._commands.has(method)) {
        process.stdout.write(
          JSON.stringify(reply(id, { error: `Unknown method: ${method}` })) + "\n"
        );
        return;
      }

      try {
        const result = await this._commands.get(method)!(params);
        process.stdout.write(JSON.stringify(reply(id, { result })) + "\n");
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err);
        process.stdout.write(
          JSON.stringify(reply(id, { error: msg })) + "\n"
        );
      }
    });
  }
}

/** @deprecated Use {@link NavigPlugin} directly. */
export const NavigStdioPlugin = NavigPlugin;
