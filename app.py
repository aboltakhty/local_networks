import streamlit as st
import socket

def get_local_ip():
    try:
        # Get the hostname of the machine
        hostname = socket.gethostname()
        # Get the local IP address
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        return f"Error getting local IP: {e}"

# Get the local IP address
local_ip = get_local_ip()

# Streamlit app
st.title("Streamlit on Local Network")
st.write(f"Access this app on your local network using: `http://{local_ip}:8501`")

st.write("### Example Content")
st.text("This is a simple Streamlit app running on your local network!")

if __name__ == "__main__":
    st.write("Run the following command in your terminal to start Streamlit:")
    st.code(f"streamlit run app.py --server.address {local_ip} --server.port 8501")
