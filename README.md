# Travail Pratique #2: Password Manager
## Auteurs
- POTL15100200, Potvin, Ludovic
## Compatibilité
Python – 3.12
## Utilisation
> [!NOTE] General information
> Le projet utilise UV pour manage les dependances. Il est plus facile de
> l'installer en utilisant UV.

> generate_env.sh creer un env file. Il va marcher avec les valeurs par default
> mais peut etre modifier.

> Pour mettre la DB a l'endroit demande (/db/database.db), il faut aller mettre
> le path dans le .env apres l'avoir genere.

## Installation
#### Avec UV
- Rouler `./generate_env.sh`
- Faire la commande `uv sync`.
- Utiliser le programme  ex. `uv run passmanager <arguments>`

### Sans UV
- Rouler `./generate_env.sh`
- Rouler `python -m venv venv` pour creer l'environment virtuel
- Activer l'environment virtuel `source venv/bin/activate`
- Installer passmanager `pip install .` # Doit etre au directory du `pyproject.toml`
- Utiliser le programme: ex. `passmanager -r test`
