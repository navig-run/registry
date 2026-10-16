# Genesis — why the System space exists

This space was not designed in the abstract. It was **extracted from real bulk filesystem
work**: multi-terabyte drive migrations, large media-library reorganizations and space
reclamation — done without losing a file.

Along the way the filesystem fought back, and every wound became a rule:

- A `Move-Item` that slow-copied a junction for an hour → **same-volume = `[IO.Directory]::Move`, instant.**
- A web-hosting backup nested past 350 chars that `rm` and Explorer couldn't touch →
  **`\\?\` + `[IO.Directory]::Delete` / `robocopy /MIR`.**
- A Linux `dhclient.leases` with hostile ACLs blocking a purge → **`robocopy /B` backup mode.**
- A folder that wouldn't move ("Access denied") because a stray `find.exe` held a handle →
  **kill the lock, then rename.**
- Keyword scans that nearly filed songs titled "Hypnotize" or "Mantra" as non-music →
  **classify by purpose AND size, guard the false-positives.**
- A `.trash` declared "safe to empty" while a few orphans lived only there →
  **verify by count, never by folder-exists; never hard-delete.**

The System space is the memory of those lessons, made operational. It exists so the next
operation starts where the last one ended — knowing the traps before stepping in them.
