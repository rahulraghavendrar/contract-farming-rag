from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_qdrant import (
    QdrantVectorStore
)

from qdrant_client import (
    QdrantClient
)

from qdrant_client.models import (
    Distance,
    VectorParams
)

embedding_model=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

client=QdrantClient(
    ":memory:"
)

client.create_collection(
    collection_name="contracts",

    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

vectorstore=QdrantVectorStore(
    client=client,
    collection_name="contracts",
    embedding=embedding_model
)

retriever=None


def process_pdf(pdf_path):

    global retriever

    loader=PyPDFLoader(
        pdf_path
    )

    documents=loader.load()

    chunks=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    ).split_documents(
        documents
    )

    vectorstore.add_documents(
        chunks
    )

    retriever=vectorstore.as_retriever(
        search_kwargs={"k":5}
    )


def retrieve_context(question):

    results=retriever.invoke(
        question
    )

    context="\n".join(
        [
            doc.page_content
            for doc in results
        ]
    )

    return context