from flask import Blueprint, jsonify, render_template, request

from app import file_manager

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main.route("/api/files", methods=["POST"])
def create_file():
    data = request.get_json()

    if not data or not data.get("path"):
        return jsonify({"error": "File path is required."}), 400

    try:
        path = file_manager.create_file(data["path"])

        return jsonify({
            "message": "File created successfully.",
            "path": str(path)
        }), 201

    except FileExistsError as error:
        return jsonify({"error": str(error)}), 409

    except (ValueError, OSError) as error:
        return jsonify({"error": str(error)}), 400


@main.route("/api/files", methods=["GET"])
def open_file():
    file_path = request.args.get("path")

    if not file_path:
        return jsonify({"error": "File path is required."}), 400

    try:
        content = file_manager.read_file(file_path)

        return jsonify({
            "path": file_path,
            "content": content
        }), 200

    except (ValueError, FileNotFoundError, OSError) as error:
        return jsonify({"error": str(error)}), 400


@main.route("/api/files", methods=["PUT"])
def save_file():
    data = request.get_json()

    if not data or not data.get("path"):
        return jsonify({"error": "File path is required."}), 400

    if "content" not in data:
        return jsonify({"error": "File content is required."}), 400

    if not isinstance(data["content"], str):
        return jsonify({"error": "File content must be text."}), 400

    try:
        path = file_manager.save_file(
            data["path"],
            data["content"]
        )

        return jsonify({
            "message": "File saved successfully.",
            "path": str(path)
        }), 200

    except (ValueError, FileNotFoundError, OSError) as error:
        return jsonify({"error": str(error)}), 400
