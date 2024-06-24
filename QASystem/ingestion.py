from haystack import Pipeline  # similar to chain in langchain
from haystack.components.writers import DocumentWriter  # writing into the DB
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore  # starage
from haystack.components.converters import PyPDFToDocument
from pathlib import Path
import os
from dotenv import load_dotenv
from QASystem.utils import pinecone_config

# Data ingestion pipeline


def ingest(document_store):
    indexing = Pipeline()

    indexing.add_component("converter", PyPDFToDocument())
    indexing.add_component("splitter", DocumentSplitter(
        split_by="sentence", split_length=2))
    indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
    indexing.add_component("writer", DocumentWriter(document_store))

    indexing.connect("converter", "splitter")
    indexing.connect("splitter", "embedder")
    indexing.connect("embedder", "writer")

    path = "/home/ryle/Desktop/gen-ai/data/Retrieval-Augmented-Generation-for-NLP.pdf"
    indexing.run({"converter": {"sources": [Path(path)]}})


if __name__ == '__main__':
    document_store = pinecone_config()
    ingest(document_store)
