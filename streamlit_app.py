import streamlit as st

from pytube import YouTube

st.title("YouTube Downloader")

st.write("Welcome to the YouTube Downloader app! With this app, you can easily download videos from YouTube and save them to your local device for offline viewing.")

video_url = st.text_input("Enter the YouTube video URL:")

if video_url:

    try:

        yt = YouTube(video_url)

        st.subheader("Video Details")

        st.write(f"Title: {yt.title}")

        st.write(f"Duration: {yt.length} seconds")

        st.write(f"Views: {yt.views}")

        st.image(yt.thumbnail_url)

        st.subheader("Download Options")

        st.write("Select the highest resolution available for download (excluding YouTube subscription streams):")

        download_options = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

        for option in download_options:

            st.write(f"{option.resolution} ({option.mime_type})")

            download_button = st.button("Download", key=option.itag)

            if download_button:

                download_path = f"{yt.title}.{option.subtype}"

                option.download(filename=download_path)

                st.success(f"Video downloaded successfully. Saved as '{download_path}'")

                break  # Stop looping after the first successful download

    except Exception as e:

        st.error(f"Error: {str(e)}")







 
