#
# # Prompt templates & formatting logic

from .llm_manager import LLMManager

class PromptManager:
    def __init__(self, llm_manager: LLMManager):
        self.llm_manager = llm_manager

    def ask(self, user_input: str) -> str:
        """
        Handle prompt creation and response retrieval.
        For now, it just forwards the input directly.
        Later: add templates, context, validation, etc.
        """
        # Step 1: (optional) build/format the prompt
        prompt = f"User asked: {user_input}"

        # Step 2: send to LLMManager
        response = self.llm_manager.send_message(prompt)

        # Step 3: return structured output (currently plain text)
        return response
