🍔 FAST-System: AI-Powered Drive-Thru Worker 🚗
Welcome to FAST-System (Fully Automated Service for Takeout)! This is an AI-powered fast-food drive-thru simulation that interacts with customers, takes their orders, and calculates totals just like a friendly fast-food worker. Built with Python and OpenAI's GPT, it provides a seamless and engaging experience. 💡

🎉 Features
🥪 Dynamic Order Processing: Takes customer orders, including customizations like sizes and add-ons.
📋 JSON-Based Menu Management: Easily modify the menu with a structured JSON format.
🤖 AI-Powered Conversations: Simulates a real drive-thru worker, complete with greetings and confirmation of orders.
💰 Order Summaries: Tracks total prices and reads back the final order for confirmation.
🔒 Secure Configuration: Uses environment variables to safely manage sensitive API keys.
🚀 How It Works
🗂 Menu: The menu is defined in JSON format for easy updates and scalability.
🤝 Conversation Flow:
Greet the customer.
Take their order with customizations (e.g., size, add-ons).
Allow changes or removal of items.
Read back the final order and confirm the total price.
🌐 Environment Variables:
API keys are securely loaded via .env file using python-dotenv.
🛠 Setup Instructions
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/DuffyAdams/FAST-System.git
cd FAST-System
2️⃣ Install Dependencies
Ensure you have Python 3.7+ installed, then install the required Python libraries:

bash
Copy code
pip install openai python-dotenv
3️⃣ Configure Your .env File
Create a .env file in the project root and add your OpenAI API key:

env
Copy code
GPT_KEY=your-openai-api-key
4️⃣ Run the Application
Run the script to start the drive-thru simulation:

bash
Copy code
python main.py
🎨 Example Interaction
plaintext
Copy code
Welcome to Ultimate Fast Food Drive-Thru Simulator!
Type 'exit' to quit at any time.

You: Hi, can I get a Double Cheeseburger with extra cheese?
Worker: Sure! Would you like anything else?

You: Add a large Soft Drink and Fries.
Worker: Got it! Your order is:
1. Double Cheeseburger with extra cheese
2. Large Soft Drink
3. Fries
Your total is $12.47. Is that correct?
📂 Project Structure
bash
Copy code
FAST-System/
├── .env               # Environment variables (API key)
├── .gitignore         # Ignored files (e.g., .env)
├── main.py            # Main Python script
├── menu.json          # JSON-based menu
❤️ Contributing
Feel free to fork this repository, submit pull requests, or suggest features! 🚀

📜 License
This project is licensed under the MIT License.

🌟 Acknowledgements
🧠 Powered by OpenAI's GPT models.
🛠 Inspired by real-world fast-food experiences.
Enjoy the FAST-System experience! 🎉

