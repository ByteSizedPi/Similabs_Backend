import os

from analysis.analysis import get_metadata
from comparison.comparison import cosine, jaccard, levenshtein
from comparison.doc_comparison import docx_to_html, sim
from db.mongo import push_corpus
from docx import Document
from flask_cors import CORS
from werkzeug.utils import secure_filename

from flask import Flask, json, jsonify, make_response, request, send_file

app = Flask(__name__)
cors = CORS(app)
app.config["UPLOAD_FOLDER"] = "static/files"


@app.route("/docx_to_html", methods=["GET", "POST"])
def docx_html():
    return jsonify(docx_to_html(request.files["file"]))


@app.route("/heatmaps", methods=["GET", "POST"])
def get_heatmaps():
    files = request.files.getlist("files")
    heatmaps = [sim(files[0], file) for file in files[1:]]
    return jsonify(heatmaps)


@app.route("/compare", methods=["POST"])
def compare():
    try:
        text1 = request.form.get("text1")
        text2 = request.form.get("text2")
    except:
        return make_response(jsonify({"error": "Invalid request"}), 400)

    return make_response(
        jsonify(
            {
                "cosine": cosine(text1, text2),
                "jaccard": jaccard(text1, text2),
                "levenstein": levenshtein(text1, text2),
            }
        )
    )


@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files["file"]
        curDir = os.path.abspath(os.path.dirname(__file__))
        uploadDir = app.config["UPLOAD_FOLDER"]
        filename = push_corpus(file)
        Document(file).save(os.path.join(curDir, uploadDir, filename))
    except Exception as e:
        print(e)
        return make_response(jsonify({"error": "Invalid request"}), 400)

    return make_response(jsonify({"msg": "sucesfully uploaded"}))


if __name__ == "__main__":
    # get_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
