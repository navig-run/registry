# Inbox

Universal drop zone for this space. Routing rules live in `routes.yaml`; this folder
ships `routes.example.yaml`. To enable routing, copy it once:

```sh
cp .navig/inbox/routes.example.yaml .navig/inbox/routes.yaml
```

Then drop files here and run `navig wiki inbox process` (or `navig inbox process-current`).
Without a `routes.yaml` the inbox still works; files are just not auto-routed.
