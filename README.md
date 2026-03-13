# AI Email Automation Agent

A small **Agentic AI workflow system** that automatically processes operational emails, extracts structured information using an LLM, and triggers automation workflows.

This project demonstrates a **multi-agent architecture for business automation**, similar to systems used in AI-driven operations platforms.

---

## Architecture

The system consists of three AI agents:

1. **Email Classifier Agent**
   - Determines the type of email (shipment delay, complaint, new order, etc.)

2. **Information Extraction Agent**
   - Extracts structured data from unstructured email text

3. **Workflow Execution Agent**
   - Triggers automated business actions based on the extracted information

Workflow pipeline:


Incoming Email
↓
Agent 1: Email Classification
↓
Agent 2: Structured Data Extraction
↓
Agent 3: Automation Workflow
↓
Processed Email Archived


---

## Project Structure


ai-email-agent
│
├── agent.py
├── .env
│
├── emails
│ └── email2.txt
│
├── README.md
│
└── processed
  └── email1.txt


**emails/** – incoming email files waiting to be processed  
**processed/** – archive for emails that have already been processed

---

## Example Input (email2.txt)


Subject: Shipment Delay

Hello team,

Order #8473 will be delayed by 7 days due to stock availability issues.
Please notify the customer.

Thanks


---

## Example Output


Processing: email2.txt

Agent 1 (Classifier): shipment_delay

Agent Raw Output:
{
"category": "shipment delay",
"order_id": "8473",
"delay_days": "7",
"action_required": "notify customer"
}

⚠️ Triggering logistics notification

Email processed and moved to archive


After processing, the file moves automatically:


emails/email2.txt
↓
processed/email2.txt


---

## Tech Stack

- Python
- Groq API
- Llama 3.1 model
- dotenv
- JSON automation pipeline

---

## Setup

### Install dependencies


pip install openai python-dotenv


### Create `.env`


GROQ_API_KEY=your_api_key_here


### Add email files

Place `.txt` email files inside the `emails` folder.

### Run the automation agent


python agent.py


---

## Key Concepts Demonstrated

- Agentic AI workflow design
- LLM-powered information extraction
- AI-driven email classification
- Automation pipelines
- Event-driven processing
- Structured JSON outputs from LLMs

---

## Future Improvements

- Gmail / Outlook inbox integration
- Database storage for extracted data
- Workflow dashboards
- Continuous background processing
- Slack / notification integrations

---

## Author: Asmit


Built as an exploration of **Agentic AI systems and workflow automation**.
