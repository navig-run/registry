# Inbox

Drop files and notes here; NAVIG routes them to the space's agents.

Routing rules ship as `routes.example.yaml`. Copy it to `routes.yaml` (the file NAVIG
loads) and adjust the channels to taste:

```bash
cp -n .navig/inbox/routes.example.yaml .navig/inbox/routes.yaml
```

```powershell
if (-not (Test-Path .navig/inbox/routes.yaml)) { Copy-Item .navig/inbox/routes.example.yaml .navig/inbox/routes.yaml }
```
