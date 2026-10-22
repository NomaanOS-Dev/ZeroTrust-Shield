# ZeroTrust-Shield

An AI-assisted Zero-Trust Network Security application engineered to analyze network telemetry, identify suspicious lateral movement, and recommend defensive firewall policies.

Developed by NomaanOS-Dev.

## 🚀 Key Features

- **Network Telemetry Analysis:** Review connection logs and identify suspicious traffic patterns.
- **Threat Assessment:** Generate risk assessments and defensive recommendations using OpenAI.
- **Zero-Trust Guidance:** Identify potentially unauthorized connections and recommend least-privilege controls.
- **PDF Audit Reports:** Export security assessment reports for documentation and review.
- **Interactive Dashboard:** Streamlit-based interface for security log analysis.

## 🛠️ Tech Stack

Python 3.x | Streamlit | OpenAI API | Pandas | ReportLab

## 📦 Installation

```bash
git clone https://github.com/NomaanOS-Dev/ZeroTrust-Shield.git
cd ZeroTrust-Shield
pip install -r requirements.txt
streamlit run app.py

Configure your OpenAI API key in the application sidebar.
🛡️ Security Notice
Use only on networks and telemetry you are authorized to analyze. AI-generated findings require human verification.
