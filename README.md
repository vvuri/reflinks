# reflinks
Reference links - python prototype project



## Steps
- x $ python -m venv venv
- x $ venv\Scripts\activate.bat
- Ctrl + Alt + S -> Python Interpreter ->  Add New Interpreter - Python 3.12 + venv
- $ pip install poetry
- $ poetry --version           
  Poetry (version 1.8.4)
- $ poetry init
- $ poetry add fastapi uvicorn 
- $ mkdir app
- add app.py in app
- $ uvicorn app.app:app --host 0.0.0.0 --port 8080
- $ mkdir ml
- file ml/iris/model.py
- $ poetry add pandas joblib scikit-learn
- Run server: $ uvicorn app.app:app --host 0.0.0.0 --port 8080
- Swagger: http://127.0.0.1:8080/docs
- Run tests: $ python .\test\test_ml_iris.py 
