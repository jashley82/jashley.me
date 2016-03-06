import os
import sys
import subprocess
import datetime
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler

BASEDIR = os.path.abspath(os.path.dirname(__file__))
PATTERNS = [
        '*.py',
        ]
IGNORE_PATTERNS = [
        '*src*',
        'watcher.py',
        ]
BUILDCOMMANDS = [
        ['docker-compose', 'build'], 
        ['docker-compose', 'up'],
        ]

def get_now():
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def build_docker():
    print >> sys.stderr, "Building docker container at {}".format(get_now())
    os.chdir(BASEDIR)
    NULL = open(os.devnull, 'w')
    for cmd in BUILDCOMMANDS:
        subprocess.call(cmd, stdout=NULL)

# def run_tests():
    # print >> sys.stderr, "Running unit tests at %s" % get_now()
    # os.chdir(BASEDIR)
    # subprocess.call(r'python -m unittest discover -b')


class ChangeHandler(PatternMatchingEventHandler):
    patterns = PATTERNS
    ignore_patterns = IGNORE_PATTERNS

    def on_any_event(self, event):
        if event.is_directory:
            return
        print event.src_path, event.event_type
        build_docker()
        # run_tests()
        

def main():
    build_docker()
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, BASEDIR, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == '__main__':
    main()
