from setuptools import find_packages, setup

setup(
    name="QA RAG System using Haystack",
    version="0.0.1",
    author="Sourin",
    author_email="sourin07@gmail.com",
    packages=find_packages(),
    install_requires=["pinecone-haystack", "haystack-ai",
                      "fastapi", "uvicorn", "python-dotenv", "pathlib"],
)
