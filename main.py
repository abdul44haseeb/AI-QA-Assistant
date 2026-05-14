from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Sample customer support transcript
transcript = """
Customer: I have been waiting for my refund for 10 days.

Agent: I understand your frustration. Let me check this for you.

Customer: This is very disappointing.

Agent: I apologize for the inconvenience. Your refund will be processed within 24 hours.
"""

# AI prompt
prompt = f"""
Analyze this customer support conversation.

Provide:
1. Conversation summary
2. Customer sentiment
3. Empathy score out of 10
4. Professionalism score out of 10
5. Coaching feedback for the agent

Conversation:
{transcript}
"""

# Send request to Groq
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.3
)

# Print AI response
print("\nAI QA ANALYSIS:\n")
print(response.choices[0].message.content)