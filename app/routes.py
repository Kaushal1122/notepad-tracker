import logging
import subprocess

from flask import Blueprint, current_app, jsonify, render_template, request

from app import file_manager, git_manager

logger = logging.getLogger(__name__)

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        autosave_delay=current_app.config["AUTOSAVE_DELAY"]
    )


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
        logger.warning("File already exists: %s", data["path"])
        return jsonify({"error": str(error)}), 409

    except (ValueError, OSError) as error:
        logger.exception("File creation failed.")
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

    except (ValueError, OSError) as error:
        logger.exception("File opening failed.")
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

        committed = git_manager.commit_file(path)

        return jsonify({
            "message": "File saved successfully.",
            "path": str(path),
            "committed": committed
        }), 200

    except (
        ValueError,
        OSError,
        RuntimeError,
        subprocess.CalledProcessError
    ) as error:
        logger.exception("File saving or Git commit failed.")

        message = getattr(error, "stderr", None) or str(error)

        return jsonify({"error": message.strip()}), 400
