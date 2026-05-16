import json

def clean_and_parse_json(ai_output):
    """
    Cleans markdown formatting and converts JSON string
    into Python dictionary.
    """

    cleaned_output = (
        ai_output
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned_output)

def read_transcript_file(file_path):
    """
    Reads transcript text file and returns content.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
    
def save_report(report_data, output_path):
    """
    Saves AI analysis report as formatted JSON file.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report_data, file, indent=4)    
