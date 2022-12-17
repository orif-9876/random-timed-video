import time
import subprocess as sub
import threading
import random

WORK_SECONDS = 3 * 60
PLAY_SECONDS = 1 * 60

filenames = [
    "/path/to/your/video1.mp4",
    "/path/to/another/video.mp4",
]


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
    result = sub.run(["ffprobe", "-v", "error", "-show_entries",
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
        args = ["mpv", "--loop-file=inf", "--fullscreen",
                f"--start={start // 60}:{start - (start // 60) * 60}", filename]
        RunCommand(args, PLAY_SECONDS).Run()
    except sub.TimeoutExpired:
        pass
    time.sleep(PLAY_SECONDS)
