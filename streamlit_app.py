



import streamlit as st
from pytube import YouTube

# Set Streamlit app title
st.title("YouTube Downloader")

# Get user input for YouTube video URL
video_url = st.text_input("Enter the YouTube video URL:")

# Check if the user has entered a valid URL
if video_url:
    try:
        # Create YouTube object from the video URL
        yt = YouTube(video_url)

        # Display video details
        st.subheader("Video Details")
        st.write(f"Title: {yt.title}")
        st.write(f"Duration: {yt.length} seconds")
        st.write(f"Views: {yt.views}")
        st.image(yt.thumbnail_url)

        # Provide download options
        st.subheader("Download Options")
        st.write("Select the highest resolution available for download (excluding YouTube subscription streams):")

        # Get available video streams (excluding YouTube subscription streams)
        video_streams = yt.streams.filter(file_extension="mp4", only_video=True, progressive=True).order_by('resolution').desc().all()

        # Display download button for the highest resolution stream
        stream = video_streams[0]
        format_resolution = f"{stream.resolution} ({stream.mime_type})"
        st.write(format_resolution)
        download_button = st.button("Download", key=stream.itag)

        # Check if download button is clicked
        if download_button:
            # Set download path
            download_path = f"{yt.title}.{stream.subtype}"

            # Download the video
            stream.download(filename=download_path)

            # Display success message
            st.success(f"Video downloaded successfully. Saved as '{download_path}'")

    except Exception as e:
        # Display error message
        st.error(f"Error: {str(e)}")
