# base.py responsibilities
# 1. load_prompt_template(name) 
# 2. get_gemini_llm() via llm.py
# 3. build_llm_chain(prompt_name)
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')  # Downloads model if needed
sentence = "This is a test sentence."
embedding = model.encode(sentence)

print("Embedding shape:", embedding.shape)