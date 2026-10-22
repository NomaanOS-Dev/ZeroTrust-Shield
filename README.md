# ZeroTrust-Shield

AI-powered microsegmentation and network policy engine for analyzing telemetry, identifying suspicious lateral movement, and recommending zero-trust firewall controls.

Developed by NomaanOS-Dev.

## Overview

ZeroTrust-Shield helps security teams review connection telemetry, detect abnormal behavior, and generate actionable network policy guidance. The application ingests log lines, sends them to OpenAI for analysis, and produces a human-readable security assessment with risk scoring, mitigation recommendations, and downloadable reports.

## Key Features

- Network telemetry analysis for suspicious connection patterns
- Threat assessment and risk scoring
- Recommended defensive firewall and segmentation controls
- PDF and Markdown report export
- Streamlit-based interactive dashboard
- AI-assisted detection of lateral movement and privilege escalation indicators

## Tech Stack

- Python 3.x
- Streamlit
- OpenAI API
- Pandas
- ReportLab

## Project Structure

```text
ZeroTrust-Shield/
├── app.py            # Streamlit frontend and report export logic
├── analyzer.py       # OpenAI-based traffic log analysis
├── requirements.txt  # Python dependencies
├── README.md        # Project documentation
└── .gitignore       # Repository ignore rules (if present)
```

## Installation

```bash
git clone https://github.com/NomaanOS-Dev/ZeroTrust-Shield.git
cd ZeroTrust-Shield
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Usage

1. Launch the app with `streamlit run app.py`.
2. Provide your OpenAI API key in the sidebar.
3. Paste network flow or connection telemetry into the input box.
4. Click the analysis button to generate a zero-trust policy assessment.
5. Review the generated findings, then export the report as Markdown or PDF.

### Sample Telemetry

The app includes a sample telemetry block for testing. You can load it from the sidebar and analyze it immediately.

## Configuration

Set the OpenAI API key from the sidebar before running analysis. The tool uses the `gpt-4o-mini` model via the official OpenAI Python SDK.

## Security Notice

This project is intended for authorized use only. Analyze only networks and telemetry you are permitted to inspect. AI-generated findings should always be reviewed by a qualified security professional before enforcement.

## License

This repository currently does not include a license file. If you intend to distribute or reuse this project publicly, consider adding an appropriate open-source license.

## Notes

This tool is designed as a security assistive workflow and is not a substitute for formal security engineering, detection engineering, or operational review.
