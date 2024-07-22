def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you": "I'm just a computer program, but I'm doing fine!",
        "bye": "Goodbye! Have a nice day!",
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

def main():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        print(f"Chatbot: {chatbot_response(user_input)}")

if __name__ == "__main__":
    main()