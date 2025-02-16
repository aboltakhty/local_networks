from pymongo import MongoClient
import streamlit as st
import socket
import uuid
import os


def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
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


# Get the local IP address
local_ip = get_local_ip()

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

# Input fields
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
        if status == "Code":
            st.code(description, language="python", line_numbers=True)
        else:
            lines = description.count('\n') + (len(description) // 50) + 1
            height = min(500, 25 * lines)  # Max height of 500px

            st.text_area("Text", value=description, height=height, key="retrieved_text")


st.write("---")

st.write("Run the following command in your terminal to start Streamlit:")
st.code(f"streamlit run app.py --server.address {local_ip} --server.port 8501")