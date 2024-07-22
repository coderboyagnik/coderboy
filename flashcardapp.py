flashcards = {
    "Python": "A high-level programming language.",
    "HTML": "The standard markup language for creating web pages.",
    "CSS": "A stylesheet language used for describing the presentation of a document written in HTML or XML."
}

def run_flashcards():
    while True:
        for term, definition in flashcards.items():
            print(f"\nTerm: {term}")
            input("Press Enter to see the definition...")
            print(f"Definition: {definition}")
        if input("\nDo you want to go through the flashcards again? (yes/no) ").lower() != 'yes':
            break

if __name__ == "__main__":
    run_flashcards()