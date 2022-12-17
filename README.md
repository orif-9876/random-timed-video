# random-timed-video

Plays a random video using mpv at a random timestamp at a regular interval, and automatically closes the video player after a certain time. 

Consider using this in combination with the pomodoro technique, where you can play a relaxing video during your break time.

## Dependencies

1. Install MPV https://mpv.io/ and make sure you can run it from the command line using `mpv`
1. Install ffmpeg https://ffmpeg.org/download.html

## Configuration

1. Edit `play.py` to configure
   ```python
   WORK_SECONDS = 3 * 60
   PLAY_SECONDS = 1 * 60

   filenames = [
       "/path/to/your/video1.mp4",
       "/path/to/another/video.mp4",
   ]
   ```
2. Run `python play.py` to start
