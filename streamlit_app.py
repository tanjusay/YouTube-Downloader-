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

        video_streams = yt.streams.filter(file_extension="mp4", only_video=True, progressive=True).order_by('resolution').desc().all()

        

        stream = video_streams[0]

        format_resolution = f"{stream.resolution} ({stream.mime_type})"

        st.write(format_resolution)

        download_button = st.button("Download", key=stream.itag)

        if download_button:

            with st.spinner("Downloading..."):

                download_path = f"{yt.title}.{stream.subtype}"

                stream.download(filename=download_path)

            st.success("Video downloaded successfully!")

            st.markdown(f"**Download Link:** [Click here to download]({download_path})")

    except Exception as e:

        st.error(f"Error: {str(e)}")












