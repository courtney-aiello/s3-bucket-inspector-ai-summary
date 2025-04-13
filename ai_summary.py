import json
import openai
import os
from dotenv import load_dotenv


load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_report(path='s3_bucket_report_.json'):
    with open(path,'r') as f:
        return json.load(f)

def format_prompt(report_data):
    return(
        "Here is a list of S3 buckets with their settings:\n\n"
        + json.dumps(report_data, indent=2)
        + "\n\nPlease summarize the security posture of these buckets. "
          "Highlight and risks and suggest improvements in plain language."

    )


def get_ai_summary(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7,
    )
    return response.choices[0].message.content

def main():
    report = load_report() # loads the scanned report from the dictionary version of the original s3 bucket inspector scan
    prompt = format_prompt(report) # takes the report and formats it into a natural language prompt
    summary = get_ai_summary(prompt) # gets the prompt from above and sends to chatGPT gets a summarizes response

if __name__ == "__main__":
    main()
