from openai import OpenAI

class AnswerGenerator:
    def __init__(self, api_key: str, model="gpt-4o-mini"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate(self, query: str, context_chunks: list):
        context = "\n\n".join(context_chunks)

        prompt = f"""
You are a Sydney housing assistant. Use ONLY the context below to answer the question.

Context:
{context}

Question: {query}

Answer in a clear and helpful way.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
