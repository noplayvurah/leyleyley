# Ley Question Game

A small Flask app built for Ley. The site asks a series of yes/no questions and follows the conversation based on your answers.

## Setup

1. Install Python 3.11+ or 3.12+.
2. Create a virtual environment (optional but recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Run

```powershell
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## How it works

- The app starts with the question: `Do you love me?`
- If you answer `yes`, it asks `Are you sure?`
- If you answer `no`, it asks `Why not?`
- The conversation continues with follow-up questions until it reaches a friendly ending.
