# Building Web App Using FastAPI & Vue 3

We will build a CRUD app using Vue for the frontend and FastAPI for the backend, showing how these frameworks integrate to create a smooth and efficient full-stack application.


## Frontend
We use Vue + Vite for setup frontend.

### Setup

```bash
$ npm create vite@latest frontend -- --template vue
$ cd frontend
$ npm install
$ npm install vue-router@4 axios
```

### Run
```bash
$ npm run dev
```

Go to http://localhost:5173/

## Backend
We use FastAPI for develop backend.

### Setup

```bash
$ cd backend/
$ venv\Script\activate
$ pip install -r requirements.txt
```


### Run
```bash
$ cd backend/
$ uvicorn app.main:app
```

Go to http://localhost:8000/docs