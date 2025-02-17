# 📡 Streamlit MongoDB App - Documentation

This documentation provides a guide to set up and run a Streamlit application that interacts with a MongoDB database.

## 🎯 Purpose
The **Streamlit MongoDB App** is a simple web interface to interact with a MongoDB collection. Users can:

1. **View their local network IP** to access the app.
2. **Retrieve and display documents** from a MongoDB collection.
3. **Insert or update documents** with text and status fields.

---

## 🛠️ Installation Guide

### 1️⃣ **Clone the Repository**
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2️⃣ **Install Required Packages**
```bash
pip install streamlit pymongo python-dotenv
```

### 3️⃣ **Setup Environment Variables**
Create a `.env` file in the root directory with the following content:

```bash
MONGOURL=mongodb://your_mongo_url_here
DB_NAME=your_database_name
COLLECTION=your_collection_name
```

> **Note:** Update these variables with your MongoDB connection details.

### 4️⃣ **Folder Structure**

```
project_root/
    ├── app.py
    └── .env
```

---

## 🧠 How It Works

1. **Local IP Detection:** The app detects the local IP address for network access.
2. **MongoDB Connection:** Connects to MongoDB using environment variables.
3. **Document Management:**
    - **Retrieve:** Fetches the first document from the collection.
    - **Insert/Update:** Inserts or updates a document with a unique ID.
4. **Interactive UI:**
    - **Text Input:** Users can enter text.
    - **Status Selector:** Choose between "Text" and "Code".
    - **Code Display:** If status is "Code", displays the text with syntax highlighting.

---

## 🚀 Running the Application

To start the application, execute:

```bash
streamlit run app.py --server.address $(hostname -I | awk '{print $1}') --server.port 8501
```

> **Tip:** The app displays the network URL for easy access on devices connected to the same network.

---

## ⚠️ Troubleshooting

- **MongoDB Connection Errors:** Check your `.env` file for correct MongoDB URL.
- **Streamlit Not Found:** Run `pip install streamlit`.
- **App Not Accessible:** Make sure your firewall allows connections on port `8501`.

---

Happy coding! 😊
