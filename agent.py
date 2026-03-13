import os
import json
import shutil
from openai import OpenAI
from dotenv import load_dotenv
print("Current working directory:", os.getcwd())

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# Agent 1: Email Classifier


def classify_email(email):

    prompt = f"""
Classify the type of this email.

Categories:
shipment_delay
customer_complaint
new_order
general

Return ONLY the category name.

Email:
{email}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You only output the category name."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


# Agent 2: Data Extractor


def extract_data(email):

    prompt = f"""
Extract structured information from this email.

Return ONLY valid JSON.

JSON format:
{{
 "category": "",
 "order_id": "",
 "delay_days": "",
 "action_required": ""
}}

Email:
{email}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You only output valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    output = response.choices[0].message.content.strip()

    print("\nAgent Raw Output:", output)

    return json.loads(output)


# Agent 3: Workflow Executor


def run_workflow(data):

    category = data["category"]

    if category == "shipment delay":
        print("⚠️ Triggering logistics notification")

    elif category == "customer complaint":
        print("📩 Opening support ticket")

    elif category == "new order":
        print("📦 Updating order database")

    else:
        print("No workflow triggered")


# Read Emails From Folder


def read_emails(folder):

    emails = []

    for file in os.listdir(folder):

        if file.endswith(".txt"):

            path = os.path.join(folder, file)

            with open(path, "r") as f:
                content = f.read()

            emails.append((file, content))

    return emails


# Move Processed Emails


def move_processed(file_name):

    source = os.path.join("emails", file_name)
    destination = os.path.join("processed", file_name)

    shutil.move(source, destination)


# Agent System Execution


print("Watching for new emails...\n")

emails = read_emails("emails")

for file_name, email_text in emails:

    print("Processing:", file_name)

    category = classify_email(email_text)
    print("Agent 1 (Classifier):", category)

    data = extract_data(email_text)
    print("Agent 2 (Extractor):", data)

    run_workflow(data)

    move_processed(file_name)

    print("Email processed and moved to archive\n")