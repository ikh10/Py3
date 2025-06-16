import random

def chatbot():
    print("Hi! I'm ChatBot. Type 'bye' to exit.")

    # Lists containing responses to user_input
    unknown = [
        "Hmm, I'm not sure what you mean.",
        "Can you rephrase that?",
        "I'm still learning. Try something else!",
        "That doesn't compute... yet.",
        "Interesting... but I don't understand."
    ]

    greetings = [
        "Hello there!",
        "Hi! How can I help you?",
        "Hey! Good to see you.",
        "Hello! What's up?",
        "Hi! How are you?"
    ]

    responses = [
        "I'm just code, but thanks for asking!",
        "I'm good! Just chatting around.",
        "Doing great in binary."
        ]

    jokes = [
        "Why don't programmers like nature? Too many bugs!",
        "Why wasn’t the cactus invited to hang out with the mushrooms? He wasn’t a fungi.",
        "I had a joke about paper today, but it was tearable.",
        "Why was the computer cold? It left its Windows open.",
        "A robot walks into a bar and says he needs to loosen up. So the bartender serves him a screwdriver."
        ]

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("ChatBot: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot:", random.choice(greetings))
        elif "how are you" in user_input:
            print("ChatBot:", random.choice(responses))
        elif "fine" in user_input or "good" in user_input:
            print("ChatBot: Glad to hear that!")
        elif "your name" in user_input:
            print("ChatBot: I'm ChatBot. But you can call me whatever you like.")
        elif "I enjoy" in user_input or " My hobbies" in user_input:
            print("ChatBot: That sounds fun! I wish I had hobbies too.")
        elif "tell me a joke" in user_input:
            print("ChatBot:", random.choice(jokes))
        else:
            print("ChatBot:", random.choice(unknown))

chatbot()
