from langchain_core.prompts import load_prompt
prompt = load_prompt("assets/prompt.json", encoding="utf-8")
print(prompt.format(name="machine learning"))


prompt = load_prompt("assets/prompt.yaml", encoding="utf-8")
print(prompt.format(name="machine learning"))