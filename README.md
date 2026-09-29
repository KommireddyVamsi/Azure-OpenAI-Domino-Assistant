# Azure OpenAI Domino Assistant

## Overview

This project demonstrates how to connect an Azure OpenAI model with a Python application to create a simple AI-powered assistant.

The application sends a user's question to Azure OpenAI GPT-4.1 and displays the generated response in the console. It serves as a beginner-friendly example for understanding how Large Language Models (LLMs) can be integrated into enterprise environments such as HCL Domino.

Although the sample question asks about a Domino server, the current implementation does not directly connect to a Domino server. Instead, it shows how user requests can be sent to Azure OpenAI and how AI-generated responses can be received and displayed.

---

## How It Works

### Step 1: Configure Azure OpenAI

The application connects to Azure OpenAI using:

* API Key
* Azure OpenAI Endpoint
* GPT-4.1 Deployment Name

```python
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)
```

### Step 2: Send User Request

A user question is sent to the GPT-4.1 model.

Example:

```python
"What is the current status of my Domino server?"
```

### Step 3: Azure OpenAI Processes the Request

The GPT model analyzes the question and generates a natural language response based on its knowledge and instructions.

### Step 4: Display Response

The generated answer is returned and printed to the console.

```python
print(response.choices[0].message.content)
```

---

## Technology Stack

* Python
* Azure OpenAI
* GPT-4.1
* OpenAI Python SDK

---

## Project Flow

```text
User Question
      │
      ▼
Python Application
      │
      ▼
Azure OpenAI GPT-4.1
      │
      ▼
AI Generated Response
      │
      ▼
Console Output
```

---

## Learning Objectives

This project helps beginners understand:

* Azure OpenAI integration
* GPT-4.1 API usage
* Chat Completion API
* Sending prompts to an LLM
* Receiving AI-generated responses
* Building AI assistants using Python

---

## Current Limitation

The application does not actually check a live Domino server.

When asked:

```text
What is the current status of my Domino server?
```

the model generates a response based only on the prompt it receives.

To obtain real server information, the application would need integration with:

* HCL Domino APIs
* Domino REST Services
* Monitoring Tools
* SQL Databases
* ServiceNow
* Splunk
* Custom Server Health Check Scripts

---

## Future Enhancements

* Real Domino Server Monitoring
* Tool Calling Support
* Agentic AI Workflow
* Server Health Checks
* Mail Queue Monitoring
* Backup Status Monitoring
* Domino Statistics Collection
* Dashboard Integration
* Automated Incident Analysis

---

## Use Case

This project is ideal for developers and Domino administrators who want to learn how Azure OpenAI can be integrated into enterprise applications and later extended with real-time server monitoring capabilities.
