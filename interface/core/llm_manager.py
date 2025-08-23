# # Low-level LLM initialization (Gemini, OpenAI, etc.)


# core/llm_manager.py

from langchain_core.language_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI  # Example: Gemini
# Later we can extend: from langchain_openai import ChatOpenAI, etc.
from core.config import DEFAULT_LLM_API_KEY

class LLMManager:
    """
    A manager for handling different LLM providers.
    Acts as a wrapper so the rest of the app does not depend on vendor-specific details.
    """

    def __init__(self, provider: str = "gemini", model: str = "gemini-flash-1.5",api_key:str=DEFAULT_LLM_API_KEY, temperature: float = 0.7):
        self.provider = provider
        self.model = model
        self.temperature = temperature
        self.api_key = api_key or DEFAULT_LLM_API_KEY
        self.llm = self._initialize_llm()

    def _initialize_llm(self) -> BaseChatModel:
        """Initialize the correct LLM client depending on provider."""
        if self.provider == "gemini":
            return ChatGoogleGenerativeAI(
                model=self.model,
                temperature=self.temperature,
                google_api_key=self.api_key
            )
        # elif self.provider == "openai":
        #     return ChatOpenAI(model=self.model, temperature=self.temperature)
        # elif self.provider == "anthropic":
        #     return ChatAnthropic(model=self.model, temperature=self.temperature)
        else:
            raise ValueError(f"Unsupported LLM provider: {self.provider}")

    def run(self, messages: list[dict]) -> str:
        """
        Run a request against the LLM.
        `messages` should follow LangChain format: [{"role": "user", "content": "Hello"}]
        """
        response = self.llm.invoke(messages)
        return response.content
