def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "👋 Hi there! How can I help you?"
    elif "how are you" in user_input:
        return "😊 I'm doing great! Thanks for asking."
    elif "your name" in user_input:
        return "🤖 I'm CodeAlphaBot, your Python chatbot."
    elif "bye" in user_input:
        return "👋 Goodbye! Have a great day!"
    else:
        return "❓ I'm not sure how to respond to that."
print("🤖 CodeAlpha Chatbot is now online!")
print("💬 Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot:", response)
    if "bye" in user_input.lower():
        break
