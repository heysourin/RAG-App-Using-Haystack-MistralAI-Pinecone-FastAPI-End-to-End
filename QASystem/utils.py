# pycone db
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
HF_TOKEN = os.environ.get('HF_TOKEN')

os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['HF_TOKEN'] = HF_TOKEN

print("API Key inported successfully!")


def pinecone_config():
    document_store = PineconeDocumentStore(
        # environment="gcp-starter",
        api_key=PINECONE_API_KEY,
        index="default",
        namespace="default",
        dimension=768
    )
    return document_store
