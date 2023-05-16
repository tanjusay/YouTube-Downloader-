import streamlit as st

from pytube import YouTube

from pytube.helpers import validate_url

st.title("YouTube Downloader")

st.write("Welcome to the YouTube Downloader app! With this app, you can easily download videos from YouTube and save them to your local device for offline viewing.")

st.write("Please note that the downloaded videos are intended for personal use only and should not be shared or distributed without the copyright owner's permission.")

video_url = st.text_input("Enter the YouTube video URL:")

if st.button("Download") and video_url:

    try:

        # Validate the URL

        if not validate_url(video_url):

            st.error("Invalid YouTube video URL. Please enter a valid URL.")

        else:

            yt = YouTube(video_url)

            st.subheader("Video Details")

            st.write(f"Title: {yt.title}")

            st.write(f"Duration: {yt.length} seconds")

            st.write(f"Views: {yt.views}")

            st.image(yt.thumbnail_url)

            video_streams = yt.streams.filter(file_extension="mp4", only_video=True, progressive=True).order_by('resolution').desc().all()

            if len(video_streams) == 0:

                st.warning("No download options available for this video.")

            else:

                stream = video_streams[0]

                format_resolution = f"{stream.resolution} ({stream.mime_type})"

                st.write(format_resolution)

                download_path = f"{yt.title}.{stream.subtype}"

                if st.button("Download", key=stream.itag):

                    with st.spinner("Downloading..."):

                        stream.download(filename=download_path)

                    st.success(f"Video downloaded successfully. Saved as '{download_path}'")

    except Exception as e:

        st.error(f"An error occurred: {str(e)}")



 
