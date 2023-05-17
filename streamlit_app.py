import streamlit as st

from pytube import YouTube

st.title("YouTube Downloader")

def download_video(video_url):

    try:

        youtube_object = YouTube(video_url)

        youtube_object = youtube_object.streams.get_highest_resolution()

        youtube_object.download()

        st.success("Video downloaded successfully.")

    except Exception as e:

        st.error(f"Error: {str(e)}")

video_url = st.text_input("Enter the YouTube video URL")

st.write("This will download the highest resolution available for the video.")

if st.button("Download"):

    if video_url:

        download_video(video_url)

    else:

        st.warning("Please enter a valid YouTube video URL.")

 

