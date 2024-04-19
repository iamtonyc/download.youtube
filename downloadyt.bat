@echo off
REM python -m pip install python-dotenv
REM python -m pip install typer
REM python -m pip install pytube

rem python main.py --input-file "path_or_url_to_input" --output-file "output_file_path.mp4" --voice "voice_option"
rem python main.py --input-file "https://www.youtube.com/watch?v=WI4nPQau0WU" --output-file "output_file_path.mp4"
python main.py

explorer .\downloaded.file