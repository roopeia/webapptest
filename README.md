# Flask starter

## Project structure

```text
flask_starter/
├── backend/
│   └── app.py
├── frontend/
│   ├── index.html
│   └── api.js
└── requirements.txt
```

## Run it

From the `flask_starter` project directory:

### 1. Create and activate a virtual environment (recommended)

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Flask

```bash
python -m pip install -r requirements.txt
```

### 3. Start the server

```bash
python backend/app.py
```

Open http://127.0.0.1:5000 in your browser. The page includes a button that tests the `/api/hello` endpoint.
