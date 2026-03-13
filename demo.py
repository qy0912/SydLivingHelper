import requests

API_URL = "http://127.0.0.1:8000/ask"

def ask(question: str):
    payload = {"query": question}
    response = requests.post(API_URL, json=payload)

    if response.status_code != 200:
        print("Error:", response.text)
        return

    data = response.json()
    print("\n=== Question ===")
    print(question)
    print("\n=== Answer ===")
    print(data.get("answer", "No answer returned"))
    print("\n")


if __name__ == "__main__":
    print("RAG Demo Client")
    print("Type your question below. Type 'exit' to quit.\n")

    while True:
        q = input("You: ").strip()
        if q.lower() in ["exit", "quit"]:
            break
        ask(q)
