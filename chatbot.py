# Simple Rule-Based Chatbot
# This chatbot responds to user input with predefined replies

def get_chatbot_response(user_input):
    """
    Function to get chatbot response based on user input
    Takes user input and returns appropriate response
    """
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Predefined responses for different inputs
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "what is your name":
        return "I'm a simple chatbot!"
    elif user_input == "help":
        return "You can say: hello, how are you, bye, what is your name, or help"
    else:
        return "I don't understand that. Try saying 'help' to see what I can do."

def main():
    """
    Main function to run the chatbot program
    Handles the conversation loop
    """
    print("Welcome to the Simple Chatbot!")
    print("Type 'bye' to exit the chat")
    print("Type 'help' to see available commands")
    print("-" * 40)
    
    # Main conversation loop
    while True:
        # Get user input
        user_message = input("You: ")
        
        # Check if user wants to exit
        if user_message.lower() == "bye":
            print("Bot: Goodbye!")
            break
        
        # Get and display bot response
        bot_response = get_chatbot_response(user_message)
        print("Bot:", bot_response)

# Run the chatbot when this file is executed directly
if __name__ == "__main__":
    main()
