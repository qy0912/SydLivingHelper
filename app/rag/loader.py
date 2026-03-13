import os

class DocumentLoader:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    def load_all_documents(self):
        documents = []
        for root, _, files in os.walk(self.data_dir):
            for file in files:
                if file.endswith(".txt"):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8") as f:
                        text = f.read()
                        documents.append({"text": text, "source": file})
        return documents
