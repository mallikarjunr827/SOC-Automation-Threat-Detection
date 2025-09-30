# src/realtime.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import subprocess

class LogHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".json"):
            print(f"New log detected: {event.src_path}")
            # Run ingestion, detection, visualization, and report automatically
            subprocess.run(["python", "src/log_ingest.py"])
            subprocess.run(["python", "src/detect.py"])
            subprocess.run(["python", "src/visualize.py"])
            subprocess.run(["python", "src/report.py"])

# Watch the sample_logs folder
observer = Observer()
observer.schedule(LogHandler(), path="data/sample_logs", recursive=False)
observer.start()

print("Real-time monitoring started. Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
# Replace this line:
# subprocess.run(["python", "src/detect.py"])
# With:
subprocess.run(["python", "src/detectemail.py"])
