# Bureau — Runbooks administratifs

Procédures et checklists pour les démarches administratives courantes.

---

## Checklist mensuelle

```
[ ] Vérifier inbox/ — traiter tout courrier en attente
[ ] Vérifier les prélèvements automatiques attendus (loyer, EDF, internet)
[ ] Déposer la quittance de loyer du mois dans docs/logement/quittances/
[ ] Vérifier les notifications CAF (mise à jour ressources, attestations)
```

---

## Déclaration d'impôts (annuelle — avril/mai)

```
[ ] Rassembler les justificatifs de revenus (bulletins de salaire, attestations de revenus, etc.)
[ ] Vérifier les informations pré-remplies sur impots.gouv.fr
[ ] Déclarer les revenus fonciers si applicable
[ ] Valider et télécharger l'avis d'imposition → out/impots/<année>/
[ ] Mettre à jour les ressources CAF après la déclaration
```

---

## Déménagement — checklist de notifications

```
[ ] Impôts (impots.gouv.fr — espace particulier)
[ ] CAF (caf.fr — mise à jour situation)
[ ] Sécurité sociale / CPAM (ameli.fr)
[ ] Banque(s)
[ ] Employeur (RH)
[ ] Caisse de retraite
[ ] Mutuelle
[ ] EDF / Engie — transfert ou ouverture de contrat
[ ] Internet / téléphone — résiliation + nouvel abonnement
[ ] La Poste — réexpédition du courrier
[ ] Médecin traitant
[ ] Assurance habitation — mise à jour ou résiliation
[ ] Mise à jour de la pièce d'identité/passeport si besoin
```

---

## Renouvellement de documents

| Document | Délai de renouvellement | Démarche |
|----------|------------------------|---------|
| Carte nationale d'identité | 10 ans (adulte) | ants.gouv.fr |
| Passeport | 10 ans (adulte) | ants.gouv.fr |
| Attestation d'assurance habitation | Annuel | Assureur |
| Attestation mutuelle | Annuel | Mutuelle |

Donnez une date d'expiration à chaque pièce dans le coffre
(`navig cabinet add passeport.pdf --category identity --expires 2031-05-01`) ;
`navig cabinet expiring --within 180` liste ce qui arrive à échéance.

---

*Ajouter des scripts d'automatisation ici en `.ps1` / `.sh` / `.py` selon le besoin.*
