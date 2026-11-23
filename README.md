
# Notepad Tracker

A simple Flask-based text editor that automatically saves changes and tracks file revisions using Git.

## Features

- Create, open, and edit text files.
- Save files in any directory on the local machine.
- Automatically save changes when typing stops.
- Track file changes using Git commits.
- Configure application settings using environment variables.
- Application logging and exception handling.

## Prerequisites

- Python 3.13 or later
- Git

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Kaushal1122/notepad-tracker.git
   cd notepad-tracker
   ```

2. Create and activate a virtual environment:

   **Windows:**

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **Linux/macOS:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create your environment file:

   **Windows:**

   ```powershell
   Copy-Item .env.example .env
   ```

   **Linux/macOS:**

   ```bash
   cp .env.example .env
   ```

5. Configure the environment variables in `.env`:

   | Variable | Description | Default |
   |---|---|---|
   | `SECRET_KEY` | Flask secret key | `development-key` |
   | `DEBUG` | Enables Flask debug mode | `False` |
   | `AUTOSAVE_DELAY` | Autosave delay in milliseconds | `2000` |
   | `LOG_LEVEL` | Application logging level | `INFO` |

6. Run the application:

   ```bash
   python run.py
   ```


# Notepad Tracker

A simple Flask-based text editor that automatically saves changes and tracks file revisions using Git.

## Features

- Create, open, and edit text files.
- Save files in any directory on the local machine.
- Automatically save changes when typing stops.
- Track file changes using Git commits.
- Configure application settings using environment variables.
- Application logging and exception handling.

## Prerequisites

- Python 3.13 or later
- Git

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Kaushal1122/notepad-tracker.git
   cd notepad-tracker
   ```

2. Create and activate a virtual environment:

   **Windows:**

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **Linux/macOS:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create the environment file:

   **Windows:**

   ```powershell
   Copy-Item .env.example .env
   ```

   **Linux/macOS:**

   ```bash
   cp .env.example .env
   ```

5. Configure the environment variables in `.env`:

   | Variable | Description | Default |
   |---|---|---|
   | `SECRET_KEY` | Flask secret key | `development-key` |
   | `DEBUG` | Enables Flask debug mode | `False` |
   | `AUTOSAVE_DELAY` | Autosave delay in milliseconds | `2000` |
   | `LOG_LEVEL` | Application logging level | `INFO` |

6. Run the application:

   ```bash
   python run.py
   ```

7. Open the application:

   ```text
   http://127.0.0.1:5000
   ```

## Testing

Run unit tests:

```bash
python -m pytest
```

Run tests with coverage:

```bash
python -m pytest --cov=app --cov-report=term-missing
```

Generate an HTML coverage report:

```bash
python -m pytest --cov=app --cov-report=html
```

Open the report:

```bash
start htmlcov/index.html
```

## Code Quality

Run Ruff:

```bash
ruff check .
```
