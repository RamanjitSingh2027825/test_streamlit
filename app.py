import streamlit as st
import os

# Function to get the size of a folder
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

# Main function to run the Streamlit app
def main():
    st.title("Folder Size Checker and File Uploader")
    
    # Define folder path
    folder_name = "TEST ADINA"
    folder_path = os.path.join(os.getcwd(), folder_name)
    
    # Check if folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        st.info(f"The folder '{folder_name}' is created.")
    
    # Display folder size
    folder_size = get_folder_size(folder_path)
    st.write(f"The size of the folder '{folder_name}' is: {folder_size / (1024*1024):.2f} MB")
    
    # File uploader
    st.write("Upload files to the folder:")
    uploaded_files = st.file_uploader(label="Upload Files", accept_multiple_files=True)
    
    # Save uploaded files to the folder
    if uploaded_files:
        for file in uploaded_files:
            file_path = os.path.join(folder_path, file.name)
            with open(file_path, "wb") as f:
                f.write(file.getvalue())
        st.success("Files uploaded successfully!")
    
        # List files in the folder
    files = os.listdir(folder_path)
    st.sidebar.write("Files in the folder:")
    for file in files:
        file_path = os.path.join(folder_path, file)
        file_size = os.path.getsize(file_path)
        st.sidebar.write(f"- {file} ({file_size / (1024*1024):.2f} MB)")
    
main()
