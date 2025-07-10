from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text, chunk_size=10000, chunk_overlap=1000):
    # First split by major sections (headers in all caps)
    sections = []
    current_section = []
    
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped and stripped.isupper() and len(stripped) > 3:  # Section header
            if current_section:
                sections.append('\n'.join(current_section))
                current_section = []
        current_section.append(line)
    
    if current_section:
        sections.append('\n'.join(current_section))
    
    # Special handling for fiscal policy document structure
    if "Fiscal Policy" in text:
        # Merge small related sections
        merged_sections = []
        current_merge = []
        for section in sections:
            if any(header in section for header in ["Definition", "Importance", "Objectives"]):
                if current_merge:
                    merged_sections.append('\n'.join(current_merge))
                    current_merge = []
            current_merge.append(section)
        if current_merge:
            merged_sections.append('\n'.join(current_merge))
        sections = merged_sections
    
    # Then split large sections into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        keep_separator=True
    )
    
    chunks = []
    for section in sections:
        if len(section) > chunk_size:
            sub_chunks = text_splitter.split_text(section)
            chunks.extend(sub_chunks)
        else:
            chunks.append(section)
    
    return chunks