import streamlit as st
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from analyzer import analyze_traffic_logs

st.set_page_config(page_title="ZeroTrust-Shield | AI Microsegmentation", page_icon="🛡️", layout="wide")

st.title("🛡️ ZeroTrust-Shield")
st.markdown("### AI Microsegmentation & Network Policy Engine")
st.markdown("Analyze network flow telemetry, detect unauthorized lateral movement, and generate zero-trust firewall rules instantly.")

# Sidebar Configuration
st.sidebar.header("🔐 Configuration")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Sample Network Logs")
sample_logs = """[2026-06-06 12:01:10] SRC=192.168.1.50 DST=10.0.0.5 DPT=22 PROTO=TCP STATE=ESTABLISHED (SSH Lateral Scan)
[2026-06-06 12:02:15] SRC=192.168.1.105 DST=10.0.0.22 DPT=3389 PROTO=TCP (RDP Brute-force attempt)
[2026-06-06 12:05:00] SRC=10.0.0.15 DST=8.8.8.8 DPT=53 PROTO=UDP (DNS Query - Normal)
[2026-06-06 12:06:40] SRC=192.168.1.200 DST=10.0.0.99 DPT=443 PROTO=TCP (Unencrypted Database Exfiltration attempt)"""

if st.sidebar.button("Load Sample Telemetry"):
    st.session_state["log_input"] = sample_logs

# Main Input Section
log_input = st.text_area("Paste Network Flow / Connection Telemetry Logs:", value=st.session_state.get("log_input", ""), height=200)

if st.button("🚀 Analyze & Generate Zero-Trust Policy", type="primary"):
    if not api_key:
        st.error("Please provide your OpenAI API Key in the sidebar.")
    elif not log_input.strip():
        st.error("Please provide network logs to analyze.")
    else:
        with st.spinner("Analyzing network vectors and formulating zero-trust rules..."):
            result = analyze_traffic_logs(api_key, log_input)
            st.session_state["audit_result"] = result

if "audit_result" in st.session_state:
    st.markdown("---")
    st.subheader("📋 ZeroTrust-Shield Audit & Policy Report")
    st.markdown(st.session_state["audit_result"])
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    # Export Markdown
    with col1:
        st.download_button(
            label="📥 Download Markdown Report",
            data=st.session_state["audit_result"],
            file_name="ZeroTrust_Shield_Report.md",
            mime="text/markdown"
        )
        
    # Export PDF Logic
    with col2:
        def create_pdf(text):
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter
            p.drawString(50, height - 50, "ZeroTrust-Shield Security Audit Report")
            
            textobject = p.beginText(50, height - 80)
            textobject.setFont("Helvetica", 10)
            
            for line in text.split("\n"):
                if textobject.getY() < 50:
                    p.drawText(textobject)
                    p.showPage()
                    textobject = p.beginText(50, height - 50)
                    textobject.setFont("Helvetica", 10)
                textobject.textLine(line[:90])
                
            p.drawText(textobject)
            p.save()
            buffer.seek(0)
            return buffer.getvalue()

        pdf_data = create_pdf(st.session_state["audit_result"])
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_data,
            file_name="ZeroTrust_Shield_Report.pdf",
            mime="application/pdf"
        )
