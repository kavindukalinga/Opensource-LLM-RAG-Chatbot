import argparse
import requests
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from get_embedding_function import get_embedding_function

CHROMA_PATH = '../chroma/huggingface'

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    # url = "http://8888888888888/v1/models/llama3"

    # payload = {
    #     "context": context_text,
    #     "prompt": query_text
    # }

    # headers = {
    #     "cache-control": "no-cache",
    #     "content-type": "application/json",
    #     "postman-token": "1a5b79ea-0fb3-b67d-d330-b6bb255a74f9"
    # }

    # print("Sending request to Llama...")
    try:
        # response = requests.post(url, json=payload, headers=headers)

        # response_text = response.text
        model = Ollama(model="llama3:latest")
        response_text = model.invoke(prompt)

        sources = [doc.metadata.get("id", None) for doc, _score in results]
        formatted_response = f"Response: {response_text}\nSources: {sources}"
        print(formatted_response)
        # print(response_text)
        # print("Source:\n",sources)
    except Exception as e:
        formatted_response = f"Error: {e}"
        print(formatted_response)
    return formatted_response


if __name__ == "__main__":
    main()
