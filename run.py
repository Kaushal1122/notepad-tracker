import logging

from app import create_app


def main():
    app = create_app()
    logging.basicConfig(
        level=getattr(logging, app.config["LOG_LEVEL"], logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=app.config["DEBUG"]
    )


if __name__ == "__main__":
    main()
