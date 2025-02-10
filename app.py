import os
import streamlit as st
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables
load_dotenv()
api_key = os.getenv('MISTRAL_OPENAI_KEY')

if not api_key:
    st.error('❌ Missing OpenAI API key. Please set the MISTRAL_OPENAI_KEY environment variable.')
    st.stop()

# Initialize Mistral client
client = Mistral(api_key=api_key)
model = 'mistral-small-2501'

# Streamlit UI with improved styling
st.set_page_config(page_title="🤖 Mistral AI Chatbot", layout="centered")

st.markdown(
    """
    <style>
        body {background-color: #f5f5f5;}
        .stTextArea textarea {background-color: #000000; color: white; border: 2px solid brown; border-radius: 10px; padding: 10px;}
        .stButton button {background-color: #4CAF50; color: white; border-radius: 8px; font-size: 16px; padding: 10px 20px;}
        .stMarkdown h1 {color: #4CAF50;}
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("ℹ️ About Mistral-Small-2501")
st.sidebar.write("1️⃣ Lightweight model optimized for efficiency.")
st.sidebar.write("2️⃣ Suitable for quick and cost-effective inference.")
st.sidebar.write("3️⃣ Balances accuracy with computational performance.")
st.sidebar.write("4️⃣ Can be integrated into various applications.")
st.sidebar.write("5️⃣ Supports multiple languages and complex queries.")

st.title("🤖 Mistral AI Chatbot")
st.write("💬 Enter your query below:")

query = st.text_area("✍️ Your input:")

if st.button("🚀 Submit"):
    if query.strip():
        with st.spinner("⏳ Generating response..."):
            chat_response = client.chat.complete(
                model=model,
                messages=[{'role': 'user', 'content': query}]
            )
            response = chat_response.choices[0].message.content
            st.subheader("📝 Response:")
            st.success(response)
    else:
        st.warning("⚠️ Please enter a valid query.")