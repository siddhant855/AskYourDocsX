from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(file):  
    splitter =  RecursiveCharacterTextSplitter(
        
            chunk_size = 500,
            chunk_overlap = 100
    )
    chunk = splitter.split_documents(file)
    return chunk
