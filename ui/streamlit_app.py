import streamlit as st
import requests

st.title("🧠 Multi-Agent Access Auditor")

query = st.text_input("Enter your query:")

if st.button("Analyze"):
    response = requests.get(
        "http://localhost:8000/query",
        params={"q": query}
    )

    if response.status_code == 200:
        try:
            data = response.json()
            #st.write("FULL RESPONSE:", data)   # 👈 ADD THIS

            st.write(data.get("response", "No response"))
        except:
            st.error("❌ Invalid JSON response")
            st.write(response.text)

