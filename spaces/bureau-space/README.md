# Bureau

Espace administratif français — gestion des documents officiels, impôts, logement, sécurité sociale, état civil, et correspondances avec les organismes publics et privés.

Langue par défaut : **français** (`default_locale: fr`). Un document peut exister en version locale (`<nom>.fr.md`) ou bilingue (`<nom>.fr.md` + `<nom>.en.md`) selon le besoin.

---

## Structure

```
bureau-space/
  README.md               ← ce fichier
  logement.md             ← domaine « logement »
  LICENSE                 ← MIT
  space.manifest.json     ← identité de l'espace (format historique)
  .navig/
    space.json            ← manifeste canonique
    state/                ← contexte runtime
    plans/                ← phases administratives en cours
    memory/               ← contexte long-terme pour l'IA (*.example.json à copier)
    inbox/                ← routes.example.yaml (à copier en routes.yaml)
    paperwork/            ← état de `navig paperwork` (créé à l'usage, ignoré par git)
  docs/                   ← documents de référence par domaine
  ops/                    ← runbooks et checklists administratives
  inbox/                  ← zone de dépôt : courriers à traiter (ignoré par git)
  out/                    ← documents envoyés, archivés, clôturés (créé au besoin)
```

---

## Espaces documentaires (domaines)

| Fichier | Domaine |
|---------|---------|
| [logement.md](logement.md) | Bail, charges, aides logement (APL), énergie, déménagements |

> Ajouter un domaine = créer un fichier `.md` dans ce dossier + une entrée dans ce tableau.

---

## Convention de nommage des fichiers

| Type | Convention | Exemple |
|------|-----------|---------|
| Document monolingue | `<nom>.<locale>.md` | `reclamation.fr.md` |
| Traduction | `<nom>.<locale>.md` | `reclamation.en.md` |
| Document sans locale spécifique | `<nom>.md` | `logement.md` (domaine entier) |

---

## Inbox — protocole de tri

1. Déposer tout courrier entrant (PDF, scan, email converti) dans `inbox/`
2. `navig paperwork scan inbox --space bureau-space --profile personal`, puis
   `navig paperwork apply --yes --space bureau-space` — classement par organisme, échéances détectées
3. Pièces d'identité et documents de santé : `navig paperwork handoff --yes --space bureau-space`
   les chiffre dans le coffre (`navig cabinet`) — jamais en clair dans cet espace
4. Documents envoyés ou archivés → `out/`
5. Relances en attente → noter dans `.navig/plans/` ; échéances : `navig paperwork echeances --space bureau-space`

---

## Liens rapides

- Runbooks : `ops/README.md`
- Plans en cours : `.navig/plans/`
- Contexte IA : `.navig/memory/`

---

## Statut

Espace **planifié** : la documentation, les runbooks et la configuration sont prêts, et le
classement du courrier fonctionne dès aujourd'hui via `navig paperwork` et `navig cabinet`.
Les agents décrits dans `.navig/wiki/agent-guide.md` ne sont pas encore livrés.
