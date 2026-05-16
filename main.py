import os
import json

from app.analyzer import analyze_conversation

# Folder paths
DATA_FOLDER = "data"
REPORTS_FOLDER = "reports"

# Create reports folder if not exists
os.makedirs(REPORTS_FOLDER, exist_ok=True)

# Get all transcript files
transcript_files = [
    file for file in os.listdir(DATA_FOLDER)
    if file.endswith(".txt")
]

# Process each transcript
for file_name in transcript_files:

    file_path = os.path.join(DATA_FOLDER, file_name)

    # Read transcript
    with open(file_path, "r", encoding="utf-8") as file:
        transcript = file.read()

    print(f"\nProcessing: {file_name}")

    # AI Analysis
    analysis_data, raw_response = analyze_conversation(transcript)

    # Print result
    print("\nSummary:")
    print(analysis_data["summary"])

    print("\nCustomer Sentiment:")
    print(analysis_data["customer_sentiment"])

    print("\nEmpathy Score:")
    print(analysis_data["empathy_score"])

    print("\nProfessionalism Score:")
    print(analysis_data["professionalism_score"])

    # Generate report file name
    report_name = file_name.replace(".txt", "_report.json")

    report_path = os.path.join(REPORTS_FOLDER, report_name)

    # Save report
    with open(report_path, "w", encoding="utf-8") as report_file:
        json.dump(analysis_data, report_file, indent=4)

    print(f"\nReport saved: {report_name}")