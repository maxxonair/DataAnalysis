 #!/usr/bin/python

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyPersonalWatchdog(FileSystemEventHandler):
    patterns = ["*.pdf", "*.xml"]
    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print event.src_path, event.event_type  # print now only for degug

    def on_modified(self, event):
         print("file change detected.",event)
         for filename in os.listdir(folderToTrack):
             if(".pdf" in filename):
                 print("File detected")
                 src = folderToTrack + "/" + filename
                 newDestination = destiantionFolder+"/"+"BounceBack.pdf"
                 os.rename(src, newDestination)


if __name__ == "__main__":
    folderToTrack="."
    destiantionFolder="./testfolder2"
    observer = Observer()
    observer.schedule(MyPersonalWatchdog(), folderToTrack, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
