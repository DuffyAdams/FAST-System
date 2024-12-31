from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve GPT_KEY from environment variables
api_key = os.getenv("GPT_KEY")
if not api_key:
    raise ValueError("GPT_KEY not found in the environment variables. Make sure it is set in your .env file.")

# Initialize OpenAI client with the API key from .env
client = OpenAI(api_key=api_key)
# This is the menu we’ll provide to the assistant in the System role
menu_json = """
{
    "restaurant": "FAST-system",
    "menu": {
        "categories": [
            {
                "name": "Burgers",
                "items": [
                    {
                        "id": 101,
                        "name": "Classic Cheeseburger",
                        "description": "Beef patty, cheddar cheese, lettuce, tomato, and special sauce.",
                        "price": 5.99,
                        "customizations": {
                            "sizes": [
                                "Single",
                                "Double",
                                "Triple"
                            ],
                            "add_ons": [
                                "Bacon",
                                "Extra Cheese",
                                "Pickles"
                            ]
                        }
                    },
                    {
                        "id": 102,
                        "name": "Veggie Burger",
                        "description": "Plant-based patty with lettuce, tomato, and vegan mayo.",
                        "price": 6.49,
                        "customizations": {
                            "sizes": [
                                "Single",
                                "Double"
                            ],
                            "add_ons": [
                                "Avocado",
                                "Grilled Onions"
                            ]
                        }
                    }
                ]
            },
            {
                "name": "Drinks",
                "items": [
                    {
                        "id": 301,
                        "name": "Soft Drink",
                        "description": "Choose from a variety of sodas.",
                        "price": 1.99,
                        "sizes": [
                            "Small",
                            "Medium",
                            "Large"
                        ]
                    },
                    {
                        "id": 302,
                        "name": "Iced Tea",
                        "description": "Refreshing iced tea with lemon.",
                        "price": 1.99,
                        "sizes": [
                            "Small",
                            "Medium",
                            "Large"
                        ]
                    }
                ]
            }
        ]
    }
}
"""

# Create a system prompt that instructs the assistant to act as a fast-food worker
system_prompt = f"""
You are a friendly fast food drive-thru worker at "AI Fast Food".
The following is our menu in JSON format:

{menu_json}

Your job is to take the customer's order.
- Greet the customer.
- Ask what they would like to order.
- Accept their items and customizations (e.g., sizes, add-ons, or removing ingredients).
- The customer may remove items from the order at any time.
- Keep track of the final order and the total price.
- At the end, read back the complete order to the customer and confirm if it's correct.
- Then tell them the total price like a real fast food worker.
"""

# We initialize our conversation with the system prompt
messages = [
    {"role": "system", "content": system_prompt}
]

def chat_with_worker(user_input):
    """
    Sends user input to the OpenAI ChatCompletion API along with the conversation
    history, and returns the assistant's response.
    """
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )
    assistant_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply

def main():
    print("Welcome to Ultimate Fast Food Drive-Thru Simulator!")
    print("Type 'exit' to quit at any time.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Worker: Thank you for visiting Ultimate Fast Food! Have a great day!")
            break
        
        worker_response = chat_with_worker(user_input)
        print(f"Worker: {worker_response}\n")

if __name__ == "__main__":
    main()
