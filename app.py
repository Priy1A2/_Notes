import streamlit as st
import os
from PIL import Image
import base64

# Title and description with a GIF
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://media.giphy.com/media/J5QXLLueZ2QFNQCsCX/giphy.gif" alt="Study Materials" width="400">
    </div>
    """,
    unsafe_allow_html=True
)
st.title("Study Materials Upload")
st.write("Upload and manage your study materials easily.")

# Background image
bg_image_path = "1717831505301.jpg"
if os.path.exists(bg_image_path):
    with open(bg_image_path, "rb") as image_file:
        bg_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{bg_image}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("Background image not found.")

# File upload function
def save_uploaded_file(uploaded_file, folder):
    try:
        with open(os.path.join(folder, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return st.success(f"Saved file: {uploaded_file.name} to {folder}")
    except Exception as e:
        return st.error(f"Error saving file: {e}")

# Create folders if they don't exist
os.makedirs("notes", exist_ok=True)
os.makedirs("papers", exist_ok=True)

# Sidebar for navigation with icons
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Notes", "Previous Year/Sem Papers"],
    index=0,
    format_func=lambda x: f"📄 {x}" if x == "Notes" else f"📚 {x}"
)

# Display uploaded files function
def list_uploaded_files(folder):
    files = os.listdir(folder)
    if files:
        st.write(f"Files in {folder}:")
        for file in files:
            st.write(file)
    else:
        st.write("No files uploaded yet.")

# Notes section
if section == "Notes":
    st.header("Upload Notes")
    col1, col2 = st.columns([3, 1])
    with col1:
        uploaded_note = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"], key="note")
    with col2:
        st.image("https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif", width=100)
    if uploaded_note is not None:
        with st.spinner('Saving file...'):
            save_uploaded_file(uploaded_note, "notes")
        st.balloons()
    list_uploaded_files("notes")

# Previous Year/Sem Papers section
elif section == "Previous Year/Sem Papers":
    st.header("Upload Previous Year/Sem Papers")
    col1, col2 = st.columns([3, 1])
    with col1:
        uploaded_paper = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"], key="paper")
    with col2:
        st.image("https://media.giphy.com/media/xUPGcxkBRZFSOZciHK/giphy.gif", width=100)
    if uploaded_paper is not None:
        with st.spinner('Saving file...'):
            save_uploaded_file(uploaded_paper, "papers")
        st.balloons()
    list_uploaded_files("papers")

# Custom CSS for enhanced styling
st.markdown(
    """
    <style>
    .stApp {
        font-family: 'Arial', sans-serif;
    }
    .stFileUploader {
        background: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 10px;
    }
    .stSidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    </style>
    """,
    unsafe_allow_html=True
)
