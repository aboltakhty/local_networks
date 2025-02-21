from pymongo import MongoClient
import streamlit as st
import socket
import uuid
import os
from flask import Flask, send_from_directory
import threading

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return f"Error getting local IP: {e}"

def get_mongo_collection():
    client = MongoClient(os.getenv("MONGOURL"))
    db = client[os.getenv("DB_NAME")]
    return db[os.getenv("COLLECTION")]

def get_document(collection):
    try:
        return collection.find_one({}) or {}
    except Exception as e:
        st.error(f"Error retrieving document: {e}")
        return {}

def upsert_document(collection, doc_id, text, status):
    try:
        collection.replace_one(
            {"_id": doc_id},
            {"_id": doc_id, "text": text, "status": status},
            upsert=True
        )
        st.success("Document saved successfully.")
    except Exception as e:
        st.error(f"Failed to save document: {e}")

def save_file_locally(file):
    try:
        save_path = os.path.join("uploads", file.name)
        os.makedirs("uploads", exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(file.read())
        st.success(f"File '{file.name}' saved successfully at {save_path}.")
    except Exception as e:
        st.error(f"Failed to save file: {e}")

def list_files():
    files = os.listdir("uploads") if os.path.exists("uploads") else []
    return files

# Get the local IP address
local_ip = get_local_ip()

# Flask app to serve files
app = Flask(__name__)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory("uploads", filename, as_attachment=True)

def run_flask():
    app.run(host="0.0.0.0", port=8502, threaded=True)

# Start Flask server in a separate thread
threading.Thread(target=run_flask, daemon=True).start()

# Streamlit app
st.title("Local Network")
st.write(f"Access this app on your local network using: `http://{local_ip}:8501`")

collection = get_mongo_collection()
document = get_document(collection)

# Initialize fields
doc_id = document.get("_id", str(uuid.uuid4()))
description = document.get("text", "")
status = document.get("status", "Text")

st.write("---")

# Document Input and Retrieval
with st.expander("Document Management"):
    description_input = st.text_area("Text", value=description, height=100, key="input_text")
    status_input = st.selectbox("Status", ["Text", "Code"], index=["Text", "Code"].index(status), key="input_status")
    if st.button("Submit"):
        upsert_document(collection, doc_id, description_input, status_input)
    
    if st.button("Retrieve"):
        document = get_document(collection)
        if document:
            doc_id = document.get("_id")
            description = document.get("text")
            status = document.get("status")

            st.code(description, language="python", line_numbers=True)

st.write("---")

# File Upload and Download Section
with st.expander("File Management"):
    uploaded_file = st.file_uploader("Choose a file", type=None)
    if uploaded_file is not None:
        if st.button("Save Locally"):
            save_file_locally(uploaded_file)
    
    st.subheader("Available Files")
    files = list_files()
    if files:
        for file in files:
            st.markdown(f"[Download {file}](http://{local_ip}:8502/uploads/{file})")
    else:
        st.write("No files available.")

st.write("---")

# Run Instructions
st.write("Run the following command in your terminal to start Streamlit:")
st.code(f"streamlit run app.py --server.address {local_ip} --server.port 8501")
