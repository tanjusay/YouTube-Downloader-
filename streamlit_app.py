import streamlit as st
from pytube import YouTube

st.title("YouTube Downloader")

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
        st.write("Select the desired format and resolution:")

        video_streams = yt.streams.filter(file_extension="mp4").all()

        for stream in video_streams:
            format_resolution = f"{stream.resolution} ({stream.mime_type})"
            st.write(format_resolution)

            download_button = st.button("Download", key=stream.itag)

            if download_button:
                download_path = f"{yt.title}.{stream.extension}"

                stream.download(filename=download_path)

                st.success(f"Video downloaded successfully. Saved as '{download_path}'")

    except Exception as e:
        st.error(f"Error: {str(e)}")
