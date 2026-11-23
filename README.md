# Notepad Tracker

A simple Flask-based text editor that automatically saves changes and tracks file revisions using Git.

## Features

- Create and edit text files.
- Save files in any directory on the machine.
- Automatically save changes when typing stops.
- Track changes using Git commits.

## Prerequisites

- Python 3.13 or later
- Git

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Run the application:

   `python run.py`

## Testing

Run tests with coverage:

`python -m pytest --cov=app --cov-report=term-missing`