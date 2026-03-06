# EXP2 — Django Project

A small Django project (EXP2) containing a sample app and project configuration used for development and learning.

## Contents

- `manage.py` — Django management script
- `db.sqlite3` — SQLite database (local development)
- `root/` — Django app containing models, views, templates
- `url_sort/` — Django project settings and URL configuration

## Prerequisites

- Python 3.8+ (3.10 recommended)
- pip
- (optional) virtual environment support: `venv` or `virtualenv`

## Setup

1. Create and activate a virtual environment (Windows PowerShell):

   `python -m venv .venv`

   `.\.venv\Scripts\Activate.ps1`

2. Install dependencies:

   - If a `requirements.txt` file exists: `pip install -r requirements.txt`
   - Otherwise install Django directly: `pip install django`

3. Apply database migrations:

   `python manage.py migrate`

4. (Optional) Create an admin user:

   `python manage.py createsuperuser`

5. Run the development server:

   `python manage.py runserver`

Open http://127.0.0.1:8000/ in your browser to view the site.

## Running tests

`python manage.py test`

## Project notes

- Templates live in the `templates/` directory; the main template is `index.html`.
- The local database file `db.sqlite3` is included for convenience during development.

## Next steps

- Add a `requirements.txt` listing project dependencies.
- Add a license and update this README with project-specific details.

---
Generated for the EXP2 workspace.
