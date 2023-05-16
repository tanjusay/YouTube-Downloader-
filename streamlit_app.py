import streamlit as st

import subprocess

st.title("YouTube Downloader")

st.write("Welcome to the YouTube Downloader app! With this app, you can easily download videos from YouTube and save them to your local device for offline viewing.")

video_url = st.text_input("Enter the YouTube video URL:")

if st.button("Download"):

    try:

        command = f"youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best {video_url}"

        subprocess.call(command, shell=True)

        st.success("Video downloaded successfully!")

    except Exception as e:

        st.error(f"An error occurred: {str(e)}")


