## Project Setup

### Create a virtual environment
```bash
python3 -m venv venv
```

### Activate the virtual environment
- On Windows
```bash
venv\Scripts\activate
```
- On MacOS and Linux
```bash
source venv/bin/activate
```

### Install the dependencies
```bash
pip install -r requirements.txt
```

### Run the server

```bash
uvicorn app.main:app --reload
```

### API Documentation

```bash
http://127.0.0.1:8000/docs
```
