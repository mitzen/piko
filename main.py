import sys
import time
import logging
from watchdog.observers import Observer
from filesysevent import FileEvent

if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO)
    logging.info("starting up application")
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(path)
    event_handler = FileEvent()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            logging.info(f"Watching {path} for file system event")
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
