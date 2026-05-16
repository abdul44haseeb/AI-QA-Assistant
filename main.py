from app.analyzer import analyze_conversation
from app.utils import read_transcript_file, save_report

# Read transcript file
transcript = read_transcript_file("data/sample_transcript.txt")

# Run AI analysis
analysis_data = analyze_conversation(transcript)

# Save report
save_report(
    analysis_data,
    "reports/qa_report.json"
)

print("\n================ EXTRACTED VALUES ================\n")

print("Summary:")
print(analysis_data["summary"])

print("\nCustomer Sentiment:")
print(analysis_data["customer_sentiment"])

print("\nEmpathy Score:")
print(analysis_data["empathy_score"])

print("\nProfessionalism Score:")
print(analysis_data["professionalism_score"])

print("\nCoaching Feedback:")

for feedback in analysis_data["coaching_feedback"]:
    print("-", feedback)

print("\nReport saved successfully in reports/qa_report.json")