import pandas as pd 
import streamlit as st

# Streamlit app title and instructions
st.title("Process 'InvNo' Column in Multiple Files")
st.write("""
Upload one or more files (CSV or Excel), and we'll process the 'InvNo' column to remove the 'i' character. 
The output will be saved as CSV files where Excel won't alter large numbers.
""")

# File uploader (multiple files)
uploaded_files = st.file_uploader("Upload your files", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    processed_files = []  # To store processed file details

    for uploaded_file in uploaded_files:
        try:
            # Skip already processed files
            if uploaded_file.name.startswith("processed_"):
                st.write(f"{uploaded_file.name} is already processed. No modifications made.")
                processed_files.append({
                    "file_name": uploaded_file.name,
                    "file_data": uploaded_file.read()
                })
                continue

            # Load each uploaded file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file, dtype=str)  # Treat all columns as strings
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file, dtype=str)  # Treat all columns as strings
            else:
                st.error(f"Unsupported file format: {uploaded_file.name}. Please upload a CSV or Excel file.")
                continue

            # Check if the 'InvNo' column exists
            if 'InvNo' in df.columns:
                # Process the 'InvNo' column to remove the 'i' character
                df['InvNo'] = df['InvNo'].str.replace('i', '', regex=False)

                # Convert 'InvNo' to the Excel-safe text format
                df['InvNo'] = df['InvNo'].apply(lambda x: f'="{x}"')

                # Save the processed data as a CSV file
                processed_file_name = f"processed_{uploaded_file.name}"
                df.to_csv(processed_file_name, index=False, quoting=1, quotechar='"', sep=',', encoding="utf-8")

                # Add the file to the download list
                with open(processed_file_name, "rb") as file:
                    processed_files.append({
                        "file_name": processed_file_name,
                        "file_data": file.read(),
                    })

                st.success(f"Processed {uploaded_file.name} successfully!")
            else:
                st.error(f"The file {uploaded_file.name} does not contain an 'InvNo' column.")

        except Exception as e:
            st.error(f"An error occurred while processing the file {uploaded_file.name}: {e}")

    # Provide download buttons for all processed files
    if processed_files:
        st.write("Download Processed Files:")
        for file in processed_files:
            st.download_button(
                label=f"Download {file['file_name']}",
                data=file["file_data"],
                file_name=file["file_name"],
                mime="text/csv"
            )
