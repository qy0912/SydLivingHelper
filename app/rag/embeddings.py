from openai import OpenAI

class EmbeddingGenerator:
    def __init__(self, api_key: str, model="text-embedding-3-small"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def embed(self, text_list):
        response = self.client.embeddings.create(
            model=self.model,
            input=text_list
        )
        return [item.embedding for item in response.data]
