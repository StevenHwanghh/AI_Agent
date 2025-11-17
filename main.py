from langchain.tools import tool

def main():
    print("Hello from langchain-course!")
    print(get_text_length("Hello, world!"))

@tool
def get_text_length(text: str) -> int:
    """Returns the length of the given text by characters."""
    return len(text)

if __name__ == "__main__":
    main()
