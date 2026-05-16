from app.ai_client import client
from app.utils import clean_and_parse_json


def analyze_conversation(transcript):

    # AI Prompt
    prompt = f"""
    Analyze this customer support conversation.

    Return ONLY valid JSON.

    Required JSON format:

    {{
        "summary": "...",
        "customer_sentiment": "...",
        "empathy_score": 0,
        "professionalism_score": 0,
        "coaching_feedback": [
            "...",
            "..."
        ]
    }}

    Conversation:
    {transcript}
    """

    # Send request to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    # Extract AI response text
    ai_output = response.choices[0].message.content

    print("\n================ RAW AI RESPONSE ================\n")
    print(ai_output)

    # Convert AI JSON into Python dictionary
    analysis_data = clean_and_parse_json(ai_output)

    return analysis_data, ai_output