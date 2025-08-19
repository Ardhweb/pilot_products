from langchain.prompts import PromptTemplate

cover_letter_template = """Based on the information provided, your task is to write a well-crafted and professional cover letter. The letter should be persuasive, highlighting the applicant's skills and why they are a good fit for the job.

Here are the details:

Please generate a concise and professional cover letter for this job application.
"""

def query_prompt(query, *args, **kwargs):
    """
    This function takes input variables for the cover letter and generates a result.
    If there is an error in the prompt generation or LLM execution, it raises an error.
    """
    query = query
    try:
        # Attempt to create the PromptTemplate with the given inputs
        cover_letter_prompt = PromptTemplate(
            input_variables=["query"],
            template=cover_letter_template,
        )

        # Generate the prompt text
        prompt = cover_letter_prompt.format(**kwargs)

        # Initialize the LLM (OpenAI, Gemini, etc.)
        llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Generate the cover letter using the LLM
        result = llm(prompt)

        return result

    except Exception as e:
        # If there is any error in creating the PromptTemplate or executing the LLM
        raise RuntimeError(f"Error generating cover letter: {str(e)}")