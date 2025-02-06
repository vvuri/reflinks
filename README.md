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
- Change Poetry to UV
- install uv
- uvx migrate-to-uv
- Add linter: $ uv add --dev ruff
- Add pytest: $ uv add --dev pytest

### TypeSpec 
- playground for experiment https://typespec.io/playground/
- $  mkdir tspec | cd tspec
- $ node --version
    v20.10.0
- $ npm -v
    10.9.0
- $ npm install -g @typespec/compiler
- $ code .
  - Extension: TypeSpec for VS Code 
    https://typespec.io/docs/introduction/editor/vscode
  - Extension: vscode-openapi-viewer 
    https://marketplace.visualstudio.com/items?itemName=AndrewButson.vscode-openapi-viewer
- Create new TSP Project: $ tsp init
  - Generic REST API
  - tspec
  - Yes for .gitignore
  - openAPI3 only
- $ tsp install
- Add in package.json
  "scripts": { "start": "tsp compile . --watch" },
- TYPESCRIPT PlayGround: https://typespec.io/playground
- Edit file: main.tsp
- $ npm run start
- Open file tsp-output/openapi.yaml and copy yaml to https://editor.swagger.io/
- result -> online Swagger view with REST API 
- Result: \tspec\tsp-output\@typespec\openapi3\openapi.v0.1.yaml
- Can generate server code for Python, Go, Java, Nodejs

### Vue
- Structure
├── dist/ <- Vue-CLI output
    └── index.html
├── src/ <- Vue source files
└── app.py
- $ npm create vue@latest
- name: src
- $ cd src | npm install
- Ставим либу обертку для получения данных вместо fetch 
  $ npm i @vueuse/core
- $ npm run dev
  Open:  http://localhost:5173/
- Install Tailwind 
  $ npm install -D tailwindcss@3 postcss autoprefixer
  $ npx tailwindcss init -p
  created  tailwind.config.js + postcss.config.js + configure by https://v2.tailwindcss.com/docs/guides/vue-3-vite


- $ npm run build