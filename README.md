# random-timed-video

Plays a random video using mpv at a random timestamp at a regular interval, and automatically closes the video player after a certain time. 

Consider using this in combination with the pomodoro technique, where you can play a relaxing video during your break time.

## Dependencies

1. Install MPV https://mpv.io/ and make sure you can run it from the command line using `mpv`
1. Install ffmpeg https://ffmpeg.org/download.html

## Configuration

1. Edit `play.py` to configure
   ```python
   WORK_SECONDS = 3 * 60  #  time between breaks
   PLAY_SECONDS = 1 * 60  #  how long each break is

   root_dir = r"path/to/videos"  #  recursively find all videos in this folder and its subfolders
   ```
   
2. Run `python play.py` to start
