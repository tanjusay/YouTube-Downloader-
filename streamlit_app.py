import streamlit as st

import subprocess

st.title("YouTube Downloader")

st.write("Welcome to the YouTube Downloader app! With this app, you can easily download videos from YouTube and save them to your local device for offline viewing.")

video_url = st.text_input("Enter the YouTube video URL:")

if video_url:

    try:

        st.subheader("Download Options")

        st.write("Select the video format and quality:")

        download_options = subprocess.check_output(['youtube-dl', '-F', video_url]).decode().strip().split('\n')[1:]

        download_formats = [opt.split() for opt in download_options]

        for format_code, extension, resolution, _, _ in download_formats:

            st.write(f"Format Code: {format_code} | Extension: {extension} | Resolution: {resolution}")

        selected_format = st.selectbox("Select a format:", [f"{format_code} ({extension})" for format_code, extension, _, _, _ in download_formats])

        if st.button("Download"):

            format_code = selected_format.split()[0]

            download_path = f"{st.text_input('Enter the filename:', value='video')}.{selected_format.split()[2]}"

            subprocess.call(['youtube-dl', '-f', format_code, '-o', download_path, video_url])

            st.success(f"Video downloaded successfully. Saved as '{download_path}'")

    except Exception as e:

        st.error(f"Error: {str(e)}")





