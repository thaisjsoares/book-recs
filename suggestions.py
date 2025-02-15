from google import genai
from contents import INSTRUCTIONS


class BookRecs:
    def __init__(self, key: str, prompt: str):
        self.key = key
        self.client = genai.Client(api_key=self.key)
        self.prompt = prompt

    def get_book_recs(self) -> str:
        response = self.client.models.generate_content(
             model="gemini-2.0-flash",
             contents=f"{INSTRUCTIONS}\n{self.prompt}"
        )

        return response.text

def main(key: str, prompt: str) -> str:
    book_recs = BookRecs(key, prompt)
    recs = book_recs.get_book_recs()

    return recs
