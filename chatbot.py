import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses
patterns_responses = [
    
    # Greeting
    [r'Hi|hi|Hello|hello|Hey|hey', ['Hello! Welcome to Domino\'s. How can I help you with your pizza order today?']],
    
    # Menu Inquiries
    [r'What is on the menu|Show me the menu|Menu', ['We have a variety of pizzas, sides, and drinks. Do you want to see our pizzas, sides, or drinks?']],
    
    # Pizza Options
    [r'What pizzas do you have|List of pizzas|Pizzas', ['We offer a range of pizzas including Margherita, Pepperoni, BBQ Chicken, Veggie Supreme, and more. Which one would you like to order?']],
    
    # Customization
    [r'I want a (.*) pizza', ['Great choice! What size would you like? We offer Small, Medium, and Large.']],
    [r'I would like a (.*) size', ['Got it! Do you want any extra toppings or modifications?']],
    [r'(.*) extra toppings|Add (.*) toppings', ['Sure! What extra toppings would you like to add?']],
    
    # Sides and Drinks
    [r'What sides do you have|List of sides|Sides', ['We have Garlic Bread, Chicken Wings, and Breadsticks. Would you like to add any of these to your order?']],
    [r'What drinks do you have|List of drinks|Drinks', ['We offer Coke, Sprite, and Fanta. What would you like to drink with your meal?']],
    
    # Order Confirmation
    [r'Yes|Confirm|Place order', ['Your order has been placed! We will deliver it to you as soon as possible. Thank you for choosing Domino\'s.']],
    
    # Cancel Order
    [r'Cancel my order|I want to cancel', ['I\'m sorry to hear that. I can help you cancel your order. Is there anything else you need help with?']],
    
    # Help and Support
    [r'I need help|Help me', ['I am here to assist you. What do you need help with?']],
    
    # Goodbye
    [r'Bye|Goodbye|See you', ['Goodbye! Have a great day and enjoy your pizza!']]
]



# Create a Chat object
chatbot = Chat(patterns_responses, reflections)

# Function to interact with the chatbot
def chat_with_bot():
    print("Hello! I am your chatbot. Type 'Bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if response in ('Goodbye! Have a great day!', 'Bye'):
            break

# Run the chatbot
if __name__ == "__main__":
    chat_with_bot()
