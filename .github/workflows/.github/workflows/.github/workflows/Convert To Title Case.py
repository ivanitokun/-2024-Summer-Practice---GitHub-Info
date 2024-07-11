def to_title_case(sentence: str) -> str:
    if not sentence:
        return ""

    words = sentence.split()
    title_case_words = [word.capitalize() for word in words]
    return " ".join(title_case_words)

# Test cases
print(to_title_case("hello world"))  
print(to_title_case("openai gpt-4")) 
print(to_title_case("this is a title")) 
print(to_title_case("THE QUICK BROWN FOX")) 
print(to_title_case("JUMPs ovER a LAZy dog")) 
print(to_title_case("typescript is great")) 
print(to_title_case("the answer is 42"))  
print(to_title_case("to be or not to be"))  
print(to_title_case("that is the question"))  
print(to_title_case(""))  
