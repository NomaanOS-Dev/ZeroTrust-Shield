import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

def analyze_traffic_logs(api_key, log_data):
    if not api_key:
        return "Error: OpenAI API Key is missing."
    
    os.environ["OPENAI_API_KEY"] = api_key
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    
    prompt = PromptTemplate(
        input_variables=["logs"],
        template="""
You are an expert Zero-Trust Network Architect and Cloud Security Engineer.
Analyze the following network connection/traffic logs for anomalous patterns, unauthorized lateral movements, or policy violations:

NETWORK LOGS:
{logs}

Provide a structured Zero-Trust Security Report containing:
1. **Executive Summary & Risk Score (1-10)**
2. **Identified Anomalies & Suspicious Flows**
3. **Recommended Microsegmentation Rules (iptables / NetworkPolicy format)**
4. **Actionable Remediation Steps**
        """
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(logs=log_data)
    return response
