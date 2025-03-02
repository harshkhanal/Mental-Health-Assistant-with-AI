# Mental-Health-Assistant-with-AI

## Overview
This is an AI-powered mental health chatbot built using Streamlit and a pre-trained GPT model. The chatbot provides responses to user inputs, offering a conversational experience for mental health support.

## Features
- Simple and intuitive interface powered by Streamlit
- Uses a pre-trained language model (`EleutherAI/gpt-neo-125M`) for generating responses
- Provides AI-generated replies to user queries about mental health

## Installation

### Prerequisites
Ensure you have Python installed (>=3.8) and install the required dependencies:

```sh
pip install streamlit transformers torch
```

## Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/ai-mental-health-chatbot.git
   cd ai-mental-health-chatbot
   ```
2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
3. Open the provided local URL in your browser and start chatting with the AI.

## Project Structure
```
.
├── app.py          # Streamlit application script
├── chatbot.py      # AI response generation using GPT model
├── requirements.txt # Dependencies (if applicable)
└── README.md       # Project documentation
```

## How It Works
- The `app.py` file initializes the Streamlit UI and takes user input.
- The input is processed using the `chatbot_response` function from `chatbot.py`.
- The chatbot generates a response using the `EleutherAI/gpt-neo-125M` model.
- The response is then displayed in the Streamlit app.

## Limitations & Disclaimer
- This chatbot is not a replacement for professional mental health services.
- AI-generated responses may not always be accurate or appropriate.
- Always consult a licensed therapist or professional for serious mental health concerns.

## Contributing
Feel free to fork the repository, open issues, or submit pull requests.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

Enjoy using the AI Mental Health Chatbot! 😊
