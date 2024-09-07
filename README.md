# uifolks-recsys

## 1. Install virtual environment
```bash
pip install venv
python3 -m venv .venv
```

## 2. Activate virtual environment
```bash
# Mac/Linux
source .venv/bin/activate

# Windows
.venv/Scripts/activate
```

## 3. Install requirements
```bash
pip install -r requirements.txt
```

## 4. Seed the database
```bash
py scripts/create_tables.py
py scripts/populate_db.py
```

## 5. Start the backend
```bash
uvicorn main:app --reload
```