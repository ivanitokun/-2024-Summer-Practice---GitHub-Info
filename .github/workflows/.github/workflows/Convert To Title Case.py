def to_title_case(sentence: str) -> str:
    if not sentence:
        return ""

    words = sentence.split()
    title_case_words = [word.capitalize() for word in words]
    return " ".join(title_case_words)

# Test cases
print(to_title_case("hello world"))  # Output: "Hello World"
print(to_title_case("openai gpt-4"))  # Output: "Openai Gpt-4"
print(to_title_case("this is a title"))  # Output: "This Is A Title"
print(to_title_case("THE QUICK BROWN FOX"))  # Output: "The Quick Brown Fox"
print(to_title_case("JUMPs ovER a LAZy dog"))  # Output: "Jumps Over A Lazy Dog"
print(to_title_case("typescript is great"))  # Output: "Typescript Is Great"
print(to_title_case("the answer is 42"))  # Output: "The Answer Is 42"
print(to_title_case("to be or not to be"))  # Output: "To Be Or Not To Be"
print(to_title_case("that is the question"))  # Output: "That Is The Question"
print(to_title_case(""))  # Output: ""
