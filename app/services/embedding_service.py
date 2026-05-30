# import google.generativeai as genai

# from app.utils.config import GEMINI_API_KEY

# genai.configure(api_key=GEMINI_API_KEY)

# def generate_embedding(text: str):

#     result = genai.embed_content(
#         model="models/gemini-embedding-2-preview",
#         content=text
#     )

#     return result["embedding"]


import google.generativeai as genai

from app.utils.config import GEMINI_API_KEY

from app.utils.cache import (
    get_cached_embedding,
    set_cached_embedding
)

genai.configure(api_key=GEMINI_API_KEY)


def generate_embedding(text: str):

    cached_embedding = get_cached_embedding(text)

    if cached_embedding:

        print("Using cached embedding")

        return cached_embedding

    print("Generating new embedding")

    result = genai.embed_content(
        model="models/gemini-embedding-2-preview",
        content=text
    )

    embedding = result["embedding"]

    set_cached_embedding(
        text,
        embedding
    )

    return embedding