import os
import typer

from dotenv import load_dotenv, find_dotenv
from pytube import YouTube

load_dotenv(find_dotenv())

app = typer.Typer()

DOWNLOADED_VIDEO_FILENAME = "downloaded.file/downloaded_video.mp4"

def download_youtube_video(url, output_path):
    typer.echo(f"Downloading YouTube video from {url}")
    yt = YouTube(url)
    stream = (
        yt.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
    )
    stream.download(output_path=output_path, filename=DOWNLOADED_VIDEO_FILENAME)
    typer.echo("Download completed.")



@app.command()
def main(

    input_file: str = input("URL of Youtube Video:"),
    output_file: str= DOWNLOADED_VIDEO_FILENAME,
    # input_file: str = typer.Option(
    #     ..., "--input-file", "-i", help="Input file path or YouTube URL"
    # ),
    # output_file: str = typer.Option(
    #     "video.mp4", "--output-file", "-o", help="Output file path"
    # ),
):

    # Check if input is a URL
    if input_file.startswith("http://") or input_file.startswith("https://"):
        typer.echo("Input is a URL, proceeding to download the video.")
        download_youtube_video(input_file, os.getcwd())
        video_path = os.path.join(os.getcwd(), DOWNLOADED_VIDEO_FILENAME)
    else:
        video_path = input_file

    new_video_path = output_file

    typer.echo("Process completed successfully.")

if __name__ == "__main__":
    app()