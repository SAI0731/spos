def chatbot():
    print("Welcome to ShopEasy Support Bot!")
    print("How can I assist you today?")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("Bot: Thank you for visiting. Have a great day!")
            break

        elif "order" in user_input and "track" in user_input:
            print("Bot: Please enter your order ID to track your order.")
        
        elif "return" in user_input:
            print("Bot: You can return a product within 10 days. Please visit the 'My Orders' section to initiate a return.")

        elif "refund" in user_input:
            print("Bot: Refunds are processed within 3 to 5 business days after product pickup.")

        elif "available" in user_input or "stock" in user_input:
            print("Bot: Could you please specify the product name you're looking for?")

        elif "payment" in user_input:
            print("Bot: We accept credit cards, debit cards, UPI, and net banking.")

        elif "support" in user_input or "help" in user_input:
            print("Bot: You can reach customer support at support@shopeasy.com or call 1800-123-456.")

        else:
            print("Bot: I'm sorry, I didn't understand that. Can you please rephrase your question?")

# Run the chatbot
chatbot()
