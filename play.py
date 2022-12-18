import os
import traceback
import time
import subprocess as sub
import threading
import random

WORK_SECONDS = 3 * 60
PLAY_SECONDS = 1 * 60

root_dir = r"/path/to/videos/"

# if installed using a package manager
FFPROBE_EXEC = "ffprobe"
MPV_EXEC = "mpv" 

# otherwise specify absolute path to the executables
# FFPROBE_EXEC = r"C:\Program Files\ffmpeg\bin\ffprobe.exe"
# MPV_EXEC = r"C:\Program Files\mpv\mpv.exe" 

# recursively walk through file system starting at root_dir
# and add absolute paths to all video files to `filenames` list
filenames = []
for root, dirs, files in os.walk(os.path.abspath(root_dir)):
    for file in files:
        if any(file.endswith(ext) for ext in {".mp4", ".mkv", ".webm", ".mov"}):
            filename = os.path.join(root, file)
            filenames.append(filename)
            print(filename)


class RunCommand(threading.Thread):
    """Run command and terminate after timeout seconds"""

    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        self.p = sub.Popen(self.cmd)
        self.p.wait()

    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            self.p.terminate()  # use self.p.kill() if process needs a kill -9
            self.join()


def get_length(filename):
    """get length of video in seconds"""
    result = sub.run([FFPROBE_EXEC, "-v", "error", "-show_entries",
                      "format=duration", "-of",
                      "default=noprint_wrappers=1:nokey=1", filename],
                     stdout=sub.PIPE,
                     stderr=sub.STDOUT)
    return float(result.stdout)


while True:
    try:
        # choose random file
        filename = filenames[random.randint(0, len(filenames) - 1)]
        # choose random start time, set to 0 if start at beginning
        start = random.randint(10, int(get_length(filename)))
        # run mpv in fullscreen mode for PLAY_SECONDS
        args = [MPV_EXEC, "--loop-file=inf", "--fullscreen",
                f"--start={start // 60}:{start - (start // 60) * 60}", filename]
        RunCommand(args, PLAY_SECONDS).Run()
    except Exception as e:
        traceback.print_exc()
    time.sleep(WORK_SECONDS)
