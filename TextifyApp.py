import streamlit as st
import os
from helper import split_audio, transcribe_audio
from tempfile import NamedTemporaryFile

# Streamlit app
def main():
    st.title("Upload and Read M4A File")

    # Dropdown menu for selecting an action
    option = st.selectbox("Select an option", ["Upload a voice file", "Other options"])

    if option == "Upload a voice file":
        # File uploader widget for .m4a files
        uploaded_file = st.file_uploader("Choose a voice file", type=["m4a"])

        if uploaded_file is not None:
            # Read the uploaded file in binary mode
            file_content = uploaded_file.read()

            # Save the uploaded file temporarily
            with NamedTemporaryFile(delete=False, suffix=".m4a") as temp_file:
                temp_file.write(file_content)
                temp_file_path = temp_file.name

            st.write(f"Temporary file saved at: {temp_file_path}")

            audio_data = open(temp_file_path, "rb")
            transcript = transcribe_audio(audio_data)
            # Display the transcript
            st.subheader("Transcript")
            st.write(transcript)

if __name__ == '__main__':
    main()

    # st.title("Voice File Transcription App")
    #
    # st.write("Upload a voice file and get the transcript.")
    #
    # uploaded_file = st.file_uploader("Choose a voice file", type=["wav", "mp3", "m4a"])
    #
    # if uploaded_file is not None:
    #     # Save the uploaded file temporarily
    #     with NamedTemporaryFile(delete=False) as temp_file:
    #         temp_file.write(uploaded_file.read())
    #         temp_file_path = temp_file.name
    #
    #         st.write(temp_file_path)
    #
    #     # Transcribe the audio file
    #     st.write('entering into translation loop')
    #     audio_file = open(temp_file_path, "rb")
    #     transcript = transcribe_audio(audio_file)
    #
    #     # Display the transcript
    #     st.subheader("Transcript")
    #     st.write(transcript)
    #
    #     # Optionally, you can delete the temporary file after use
    #     os.remove(temp_file_path)



