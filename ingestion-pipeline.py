import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

def load_documents(docs_path="docs"):
    """Load all the text documents from the docs directory"""
    print(f"Loading documents from {docs_path}...")

    # Check if the docs directory exists
    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"The directory {docs_path} does not exist. Please create it and add your files.")
    
    # Load all txt files
    loader = DirectoryLoader(
        path=docs_path,
        glob="*.txt",
        loader_cls=TextLoader
    )

    documents = loader.load()

    if len(documents) == 0:
        raise FileNotFoundError(f"No .txt files found in {docs_path}. Please add your files.")
    
    for i, doc in enumerate(documents[:2]):
        print(f"\nDocument {i+1}:")
        print(f"\n  Source:             {doc.metadata['source']}")
        print(f"\n  Content Lenght:     {len(doc.page_content)} Characters")
        print(f"\n  Content Preview:    {doc.page_content[:100]}...")
        print(f"\n  Metadata:           {doc.metadata}")

    return documents

def main():
    print("Main Function")

    #1. Loading the files
    documents = load_documents(docs_path="docs")

    #2. Chunking the files
    #3. Embedding and Storing in Vector DB

if __name__ == "__main__":
    main()