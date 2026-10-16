# Inbox

Drop zone for this space. Channel routing (which agent owns which `#channel`) lives in
`routes.yaml`; this folder ships `routes.example.yaml`. Copy it once to enable routing:

```sh
cp .navig/inbox/routes.example.yaml .navig/inbox/routes.yaml
```

Then drop files here and run `navig wiki inbox process` (or `navig inbox process-current`).
Edit `routes.yaml` to match how you work in `clips-space`.
