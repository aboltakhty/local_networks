
### 📡 **StreamNet: Mongo & File Share**  
This documentation provides a guide to set up and run a Streamlit application that interacts with a MongoDB database.


## 📝 **Purpose**  
The **StreamNet** is a simple web-based tool that enables users to:  

1. **View their local network IP** for easy access on multiple devices.  
2. **Retrieve and manage documents** stored in a MongoDB collection.  
3. **Insert or update documents** with text and status fields.  
4. **Upload and share files** over the local network.  
5. **Download available files** from any device connected to the same network.  

---

## 🛠️ **Installation Guide**  

### 1️⃣ **Clone the Repository**  
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2️⃣ **Install Required Packages**  
```bash
pip install streamlit pymongo python-dotenv flask
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
    ├── .env
    ├── uploads/  (stores uploaded files)
```

---

## 🚀 **How It Works**  

1. **Local IP Detection**  
   - The app detects the local IP address, so other devices can access it.  

2. **MongoDB Connection**  
   - Uses the environment variables to connect and interact with MongoDB.  

3. **Document Management**  
   - **Retrieve:** Fetches the first document from the collection.  
   - **Insert/Update:** Allows users to store and update text-based documents.  

4. **File Sharing**  
   - **Upload Files:** Users can upload files, which are stored locally.  
   - **List Files:** Displays all uploaded files with download links.  
   - **Download Files:** Files are accessible via browser using:  
     ```
     http://<LOCAL_IP>:8502/uploads/<filename>
     ```

---

## ▶️ **Running the Application**  

Run the following command in your terminal to start the app:  
```bash
streamlit run app.py --server.address $(hostname -I | awk '{print $1}') --server.port 8501
```
> **Tip:** The app displays the network URL so other devices can access it easily.  

---

## ⚠️ **Troubleshooting**  

- **MongoDB Connection Errors?**  
  - Ensure the `.env` file is correctly configured.  

- **Streamlit Not Found?**  
  - Run `pip install streamlit`.  

- **Cannot Access the App from Other Devices?**  
  - Ensure your firewall allows connections on ports `8501` (Streamlit) and `8502` (Flask file server).  

---

Enjoy using **StreamNet**! 😊