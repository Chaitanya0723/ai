print("ChatBot: Hi! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == 'hello':
        print("ChatBot: Hello there!")
    elif user == 'how are you':
        print("ChatBot: I'm just code, but I'm doing fine!")
    elif 'name ' in user:
        print("ChatBot: I'm a simple chatbot.")
    elif user == 'bye':
        print("ChatBot: Goodbye!")
        break
    else:
        print("ChatBot: Sorry, I didn't understand that.")
