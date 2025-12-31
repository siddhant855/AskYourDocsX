def retrieve_docs(vectorstore, question, k=3):
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )
    docs = retriever.invoke(question)
    return [doc.page_content for doc in docs]
