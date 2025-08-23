#Runs a single prompt → LLM → response pipeline

# feature/prompt/prompt_runner.py

from pipeline.prompt_pipeline import PromptPipeline
from core.llm_manager import LLMManager


def run_prompt(prompt: str, provider:str="gemini", model_name: str = "gemini-1.5-flash"):
    """
    Run a single prompt through the pipeline.
    
    Args:
        prompt (str): The input text prompt.
        model_name (str): Which LLM to use (default: gemini-flash).
    
    Returns:
        str: LLM generated response.
    """
    # Step 1: Get the LLM from manager
    # llm = LLMManager.get_model(model_name)
    llm_manager = LLMManager(provider=provider, model=model_name)



    # # Step 2: Load pipeline with chosen LLM
    # pipeline = PromptPipeline(llm=llm_manager)

    # Step 3: Run pipeline with the prompt
    response = llm_manager.run(prompt)

    return response
