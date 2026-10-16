# Bureau Space — Runbooks

## File a New Document

1. Drop it in `inbox/`
2. `navig paperwork scan inbox --space bureau-space --profile personal` — reads the letter,
   names it, finds the organism, the reference and any deadline
3. `navig paperwork review --needs-review` for anything it would not guess
4. `navig paperwork apply --yes --space bureau-space`
5. ID / santé documents: `navig paperwork handoff --yes --space bureau-space` encrypts them into
   the cabinet (`navig cabinet list --tag paperwork` to check)

## Open a New Dossier

1. Post to `#dossiers`:
   - Name of the procedure
   - Category (impôts / logement / santé / etc.)
   - Required documents list
   - Key deadline
2. dossier-tracker creates dossier record
3. Update status as each step completes
4. Close dossier when officially resolved

## Annual Tax Workflow

**Timing:** April–May

1. Gather: tous les bulletins de salaire, avis d'imposition précédent
2. Log onto impots.gouv.fr
3. Review pre-filled declaration
4. Complete: revenus complémentaires, charges déductibles
5. Submit before deadline
6. Download and file: confirmation de declaration + avis d'imposition

## Emergency: Lost Document

1. Search the cabinet for the last known copy: `navig cabinet search <nom ou numéro>`,
   then `navig cabinet export <id> -o <dossier>` (or `navig cabinet open <id>`)
2. Search correspondence log for reference numbers
3. Request replacement from issuing authority
4. Log correspondence to `#courrier`
