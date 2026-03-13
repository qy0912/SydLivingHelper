# RAG Demo Project

A lightweight Retrieval-Augmented Generation (RAG) demo built with **FastAPI**, **FAISS**, and **OpenAI**.

This project includes:

- Automatic environment setup (`setup.sh`)
- Custom shell commands (`startapp`, `stopapp`)
- A simple RAG pipeline
- A CLI demo client (`demo.py`)
- `.env` support for API keys

---

### 🚀 Features

- One‑command setup: `./setup.sh`
- One‑command start: `startapp`
- One‑command stop: `stopapp`
- Virtual environment isolation
- FAISS vector search
- OpenAI API integration
- FastAPI server with `/ask` endpoint

---

### 📦 Project Structure

```
.
├── main.py
├── rag.py
├── vector_store/
├── requirements.txt
├── setup.sh
├── demo.py
├── .env
└── README.md
```

---

### 🔧 Installation & Setup

#### 1. Clone the repository

```
git clone <your-repo-url>
cd <your-project-folder>
```

#### 2. Add your OpenAI API key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

> `.env` is automatically loaded by the backend.  
> Do **NOT** commit your `.env` to Git.

#### 3. Run setup script

```
./setup.sh
```

This will:

- Create a Python virtual environment  
- Install all dependencies  
- Add `startapp` and `stopapp` aliases to your `~/.zshrc`  
- Reload your shell config  

---

### ▶️ Running the App

After setup, simply run:

```
startapp
```

This will:

- Activate the virtual environment  
- Launch FastAPI with Uvicorn  
- Start the RAG backend  

Stop the server with:

```
stopapp
```

---

### 🧪 Testing with the Demo Client

Run the interactive CLI:

```
python demo.py
```

Example:

```
You: What is this project about?
Answer: ...
```

---

### 📡 API Endpoint

#### `POST /ask`

**Request Body**

```json
{
  "query": "your question here"
}
```

**Response**

```json
{
  "answer": "generated answer"
}
```

---

### 🧰 Development

#### Activate the virtual environment manually

```
source venv/bin/activate
```

#### Install new dependencies

```
pip install <package>
pip freeze > requirements.txt
```

---

### 🛑 Stopping the Server

```
stopapp
```

This kills the Uvicorn process safely.

---

### 📝 Notes

- This project uses `.env` for API keys — keep it private.  
- Aliases are added only once; rerunning setup won't duplicate them.  
- Works on macOS and Linux (zsh required).  

---

### 📄 License

MIT License (or your preferred license)

---

### 🙌 Acknowledgements

- FastAPI  
- FAISS  
- OpenAI  
- Python community  