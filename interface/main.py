from features.prompt_runner import run_prompt

if __name__ == "__main__":
    takes_user_input = input("Write or Ask:")
    result = run_prompt(f"{takes_user_input}", provider="gemini", model_name="gemini-1.5-flash")
    print(result)
