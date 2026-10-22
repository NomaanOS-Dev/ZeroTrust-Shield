from openai import OpenAI


def analyze_traffic_logs(api_key, log_data):
    if not api_key:
        return "Please provide your OpenAI API key in the app settings."

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a defensive cybersecurity analyst. "
                        "Assess threats, assign a 0-100 risk score, "
                        "map relevant MITRE ATT&CK techniques, "
                        "and recommend defensive mitigations."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Analyze these security logs:\n{log_data}",
                },
            ],
            temperature=0.2,
            max_tokens=1200,
        )
        return response.choices[0].message.content or "No analysis returned."
    except Exception as e:
        return f"AI analysis error: {e}"
