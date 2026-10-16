# Runbooks — DevOps Space

## RB-001: Deploy a service

1. Confirm tests are green in CI: check #pipeline
2. Run pre-deploy health check:
   ```
   navig skill run health-probe --service <name> --environment staging
   ```
3. Run deploy workflow:
   ```
   navig ask "run the deploy-check workflow for service=<name> image=<tag> environment=staging"
   ```
4. If staging passes, repeat for prod
5. Monitor for 10 min post-deploy in Grafana

---

## RB-002: Respond to a critical alert

1. Check #incidents — is there already an open incident?
2. If not, open one:
   ```
   @incident-commander open --severity critical --title "<alert name>"
   ```
3. Run triage:
   ```
   navig ask "run the incident-triage workflow for alert_name=<alert> service=<name> severity=critical"
   ```
4. Assign technical lead
5. Post status update every 15 minutes until resolved
6. On resolution: write postmortem within 24h

---

## RB-003: Recover from Terraform state lock

1. Identify the lock:
   ```
   terraform force-unlock -force <LOCK_ID>
   ```
2. If DynamoDB — navigate to the lock table and delete the record manually
3. Verify state is clean:
   ```
   terraform state list
   ```
4. Re-run plan before any next apply
5. File ISS in known-issues.json if this is recurring

---

## RB-004: SSL certificate expiry alert

1. Check which domain triggered: run `cert-check` skill
2. If ≤ 14 days: renew immediately
   - Let's Encrypt: `certbot renew --cert-name <domain>`
   - ACM: request new cert in AWS Console
3. Test renewal: `openssl s_client -connect <domain>:443 | openssl x509 -noout -dates`
4. Update monitoring if auto-renewal was disabled

---

## RB-005: Run the weekly reliability review

```
navig ask "run the weekly-reliability-review workflow"
```

Review the report in #sre. Action any items with status ≠ OK before next Monday.
