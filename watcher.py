import yaml
import os
import sys
import subprocess
import datetime
import time

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

BASEDIR = os.path.abspath(os.path.dirname(__file__))
PATTERNS = [
        '*.css',
        '*.py',
        '*.html',
        '*.json',
        '*.js',
        '*.txt',
        ]
IGNORE_PATTERNS = [
        '*watcher.py',
        ]
BUILDCOMMANDS = [
        ['docker-compose', 'stop', 'web'], 
        ['docker-compose', 'build', 'web'], 
        ['docker-compose', 'up', 'web'],
        ]

def parse_gitignore():
    with open('.gitignore', 'r') as gitignore:
        print '[*] Parsing gitignore'
        for line in gitignore.readlines():
            IGNORE_PATTERNS.append(line.strip())

def parse_dockeryml():
    with open('docker-compose.yml', 'r') as dockeryml:
        yml = yaml.load(dockeryml.read())
        print "[*] Launching web server http://localhost:{}".format(yml['web']['environment']['PORT'])

def get_now():
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def build_docker():
    print "[+] Building docker container @{}".format(get_now())
    NULL = open(os.devnull, 'w')
    for cmd in BUILDCOMMANDS:
        subprocess.Popen(cmd, stdout=NULL)
        time.sleep(1) # give time for docker commands to complete
    return 

class ChangeHandler(PatternMatchingEventHandler):
    patterns = PATTERNS
    ignore_patterns = IGNORE_PATTERNS

    def __init__(self):
        super(ChangeHandler, self).__init__()
        self.last_ran = time.time()
    
    def on_any_event(self, event):
        print "[*] {} {}".format(event.src_path, event.event_type)
        if time.time() - self.last_ran > 1:
            build_docker()
            self.last_ran = time.time()
            print self.last_ran

def main():
    os.chdir(BASEDIR)
    parse_gitignore()
    parse_dockeryml()
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
