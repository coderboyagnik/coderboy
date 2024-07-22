def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    text = input("Enter text: ")
    print(f"Number of words: {count_words(text)}")
