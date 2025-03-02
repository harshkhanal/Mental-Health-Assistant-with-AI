from transformers import pipeline

# Load pre-trained AI model
chatbot_ai = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

# Function to generate a response using GPT-2
def chatbot_response(user_input):
    response = chatbot_ai(user_input, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']
