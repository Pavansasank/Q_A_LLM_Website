from db import search_documents
from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_rag(question):

    results = search_documents(
        question
    )

    chunks = results["documents"][0]
    print("\nRETRIEVED CHUNKS:\n")

    for i, chunk in enumerate(chunks):
        print(f"\n--- CHUNK {i+1} ---")
        print(chunk[:500])

    context = "\n\n".join(chunks)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content":
                """
                Answer ONLY from the context.

                If the answer is not found,
                say:

                'I could not find that information
                in the website.'
                """
            },
            {
                "role": "user",
                "content":
                f"""
                Context:

                {context}

                Question:

                {question}
                """
            }
        ]
    )

    return response.choices[0].message.content