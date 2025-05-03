import openai

# Set your OpenAI API key here
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Define a function to interact with the AI assistant
def chat_with_jarvis(prompt):
    response = openai.Completion.create(
        engine="davinci",  # You can experiment with different engines
        prompt=prompt,
        max_tokens=150,   # You can adjust the response length
        n=1,
        stop=None
    )
    
    return response.choices[0].text.strip()

# Main loop for chatting with the assistant
print("Hello! I'm your AI assistant. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    response = chat_with_jarvis(user_input)
    print("Jarvis:", response)
