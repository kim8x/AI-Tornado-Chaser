# Guide de Contribution

## Comment Contribuer

1. **Fork du projet**
   - Visitez la page GitHub du projet
   - Cliquez sur le bouton "Fork"

2. **Cloner votre fork**
   ```bash
   git clone https://github.com/votre-nom/Tropical-Cyclone-chasers.git
   cd Tropical-Cyclone-chasers
   ```

3. **Créer une branche**
   ```bash
   git checkout -b nom-de-votre-fonctionnalite
   ```

4. **Faire vos modifications**
   - Écrivez votre code
   - Ajoutez des tests si nécessaire
   - Mettez à jour la documentation

5. **Tester vos modifications**
   ```bash
   python -m pytest tests/
   ```

6. **Commit et Push**
   ```bash
   git add .
   git commit -m "Description claire des modifications"
   git push origin nom-de-votre-fonctionnalite
   ```

7. **Créer une Pull Request**
   - Visitez votre fork sur GitHub
   - Cliquez sur "Compare & pull request"
   - Remplissez la description avec les détails de vos modifications

## Standards de Code

### Style de Code
- Suivez PEP 8
- Utilisez des noms descriptifs en français
- Commentez votre code en français
- Limitez les lignes à 79 caractères

### Documentation
- Documentez toutes les fonctions avec des docstrings
- Incluez des exemples d'utilisation
- Mettez à jour le README.md si nécessaire

### Tests
- Écrivez des tests pour toute nouvelle fonctionnalité
- Maintenez une couverture de test > 80%
- Utilisez pytest pour les tests

## Structure du Projet

```
Tropical-Cyclone-chasers/
│
├── data/
│   ├── raw/          # Données brutes
│   └── processed/    # Données traitées
│
├── docs/             # Documentation
│   ├── api.md
│   ├── installation.md
│   └── ...
│
├── notebooks/        # Notebooks Jupyter
│   └── ...
│
├── scripts/          # Scripts Python
│   ├── __init__.py
│   ├── extract_to_csv.py
│   └── ...
│
├── tests/           # Tests unitaires
│   ├── __init__.py
│   └── ...
│
├── requirements.txt  # Dépendances
└── README.md        # Documentation principale
```

## Signalement de Bugs

Pour signaler un bug:

1. Vérifiez qu'il n'existe pas déjà dans les Issues
2. Créez une nouvelle Issue avec:
   - Description détaillée du bug
   - Étapes pour reproduire
   - Comportement attendu vs observé
   - Environnement (OS, Python version, etc.)

## Questions et Support

- Utilisez les Issues GitHub pour les questions
- Consultez la documentation existante
- Rejoignez notre canal de discussion [lien]
