import os
import logging
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'data', 'recipes.db')

# Try to import and initialize recipe matcher but keep server alive on failure
matcher = None
try:
    from recipe_matching import RecipeMatcher
    matcher = RecipeMatcher(db_path=DB_PATH)
    logger.info("RecipeMatcher loaded successfully.")
except Exception as e:
    logger.exception("Could not initialize RecipeMatcher: %s", e)
    # matcher stays None — endpoints will return an error message

@app.route('/')
def index():
    # make sure templates/index.html exists
    return render_template('index.html')

@app.route('/api/suggest', methods=['POST'])
def suggest():
    if matcher is None:
        return jsonify({"error": "Recipe matcher unavailable. Check server logs."}), 500
    data = request.get_json() or {}
    user_ings = [i.strip().lower() for i in data.get('ingredients', [])]
    max_results = int(data.get('max_results', 20))
    try:
        results = matcher.suggest(user_ings, max_results=max_results)
        return jsonify(results)
    except Exception as e:
        logger.exception("Error while suggesting: %s", e)
        return jsonify({"error": "internal error"}), 500

if __name__ == '__main__':
    # Nimbus / many cloud platforms provide a PORT env var — use it
    port = int(os.environ.get("PORT", 5000))
    logger.info("Starting Flask on 0.0.0.0:%s (use_reloader=False)", port)
    # disable reloader so it won't continuously restart
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)
