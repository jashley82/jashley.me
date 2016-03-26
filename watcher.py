import os
import sys
import subprocess
import datetime
import time

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

BASEDIR = os.path.abspath(os.path.dirname(__file__))
PATTERNS = [
        '*.py',
        '*.html',
        ]
IGNORE_PATTERNS = [
        '*src/*',
        '*watcher.py',
        ]
BUILDCOMMANDS = [
        ['docker-compose', 'build'], 
        ['docker-compose', 'up'],
        ]

def get_now():
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def build_docker():
    print "[+] Building docker container @{}".format(get_now())
    NULL = open(os.devnull, 'w')
    for cmd in BUILDCOMMANDS:
        subprocess.Popen(cmd, stdout=NULL)
    return

class ChangeHandler(PatternMatchingEventHandler):
    patterns = PATTERNS
    ignore_patterns = IGNORE_PATTERNS
    
    def on_any_event(self, event):
        print "[*] {} {}".format(event.src_path, event.event_type)
        build_docker()

def main():
    os.chdir(BASEDIR)
    print "[*] Starting watchdog in {} @{}".format(BASEDIR, get_now())
    build_docker()
    observer = Observer()
    observer.schedule(ChangeHandler(), BASEDIR, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    main()
