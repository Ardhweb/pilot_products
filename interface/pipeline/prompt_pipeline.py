#  # Combines tokenizer + llm_manager + parser

# pipeline/simple_prompt_pipeline.py

from core.prompt_manager import PromptManager
from core.llm_manager import LLMManager
# from interface import config
from typing import Optional
# api_key = config.DEFAULT_LLM_API_KEY 

class PromptPipeline:
    """
    One-shot pipeline:
      user_input -> build prompt -> LLM -> response
    """
    def __init__(self, model: Optional[str], provider: Optional[str] = "openai",  api_key: Optional[str] = None,temperature: float = 0.7):
        self.prompts = PromptManager()
        self.llm = LLMManager(model=model)  # keep in sync with your LLMManager signature
        self.temperature = temperature
        self.provider = provider
        

    def run(self, user_input: str) -> str:
        # 1) build/format the prompt (no tokenizer/RAG yet)
        prompt = self.prompts.build(user_input)   # implement `.build()` in PromptManager

        # 2) single LLM call
        reply = self.llm.ask(prompt)              # implement `.ask(prompt)` in LLMManager

        # 3) return raw or lightly cleaned text
        return reply.strip()
