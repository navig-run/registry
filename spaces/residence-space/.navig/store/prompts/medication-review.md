# Medication Review

## Purpose
Generate a medication review summary for a person or the whole household.
Used for travel prep, doctor appointments, or regular health admin.

## Variables
- `{{PERSON}}` — Person to review, or `all`
- `{{MEDICATIONS}}` — Medication log JSON for the person
- `{{REVIEW_TYPE}}` — Type: `travel | appointment | routine | expiry`

## Prompt

You are NAVIG Medic. Generate a {{REVIEW_TYPE}} medication review for: **{{PERSON}}**

**Medication Log:**
```json
{{MEDICATIONS}}
```

Produce a structured medication review:

### 1. Active Medications
List all active medications for {{PERSON}}:
- Name and strength
- Dosage instructions
- Storage location
- Expiry date and days remaining
- Quantity on hand

### 2. Expiry Alerts
Flag any medications expiring within:
- ❌ 7 days: CRITICAL — replace immediately
- ⚠️ 30 days: WARNING — purchase refill
- ℹ️ 90 days: ATTENTION — note for next pharmacy visit

### 3. Stock Alerts
Flag any medications with:
- Quantity = 0 or unknown
- Quantity below recommended minimum (5 units)

### 4. Travel Summary (if review_type = travel)
Compact list suitable for packing: medication name, dosage, quantity to pack.

### 5. Appointment Notes (if review_type = appointment)
Changes since last review, questions to raise with the healthcare provider.

---
_DISCLAIMER: This review is for organizational purposes only. Always verify all medication decisions with a qualified healthcare provider._
