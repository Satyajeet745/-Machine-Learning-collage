
from flask import Flask, Response, abort
from pathlib import Path

app = Flask(__name__)

# Folder containing all practical codes
CODE_DIR = Path(__file__).parent / "codes"

@app.route("/")
def home():
    return "ML Practical Code Server is Running!"

@app.route("/t/<int:code_id>")
def get_code(code_id):

    file_path = CODE_DIR / f"{code_id}.py"

    if not file_path.exists():
        abort(404, description="Practical code not found")

    code = file_path.read_text(encoding="utf-8")

    return Response(code, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
