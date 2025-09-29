 FlavorGraph

An intelligent recipe suggestion web app built with Python Flask + SQLite + HTML/CSS/JS, that helps users discover dishes based on the ingredients they have.

It leverages graph theory, backtracking, and greedy algorithms to efficiently match recipes, analyze ingredient gaps, and even suggest substitutions for missing ingredients.

 How to Run

Create a virtual environment :

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Run the app:

python seed_db.py
python app.py


Open 👉 http://localhost:5000
 in your browser.

📦 What’s Included

app.py — Flask app

recipe_matching.py — core matching logic

substitution.py — substitution lookup

templates/index.html — simple frontend

static/styles.css — basic styling

data/recipes.db — seeded SQLite DB

✨ Features

 Suggest recipes based on available ingredients
 Supports regional cuisines: Telugu, Gujarati, Marathi (extendable to more)
 Ingredient gap analysis — see what’s missing
 Smart substitution engine (direct, category, fuzzy matches)
 Photos for recipes (local or URL-based)
 Modern frontend with chip-based ingredient entry and results UI
 Shopping list aggregation from suggested recipes
 Fully extensible database (seed_db.py makes it easy to add new recipes)

🛠️ Tech Stack

Backend: Python 3, Flask

Database: SQLite3

Frontend: HTML5, CSS3, Vanilla JS

Algorithms: Graph theory, Backtracking, Greedy search

Deployment: Flask (local), optional Dockerfile

📂 Project Structure
recipe_suggester/
├── app.py                # Flask app (routes, API)
├── seed_db.py            # Script to create/seed SQLite DB
├── data/
│   └── recipes.db        # SQLite DB (auto-created)
├── recipe_matching.py    # Core matching algorithms
├── substitution.py       # Substitution engine
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   ├── styles.css        # CSS for frontend
│   └── images/           # Food images (local)
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
