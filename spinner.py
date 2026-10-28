# spinner.py
import sys
import time
import threading

class Spinner:
    def __init__(self, message="GiggleByte is typing"):
        self.message = message
        self.is_running = False
        self.thread = None
        self.lock = threading.Lock()  # Prevents thread collisions

    def _spin(self):
        dots = [".  ", ".. ", "..."]
        i = 0
        while self.is_running:
            with self.lock:
                sys.stdout.write(f"\r{self.message}{dots[i]}")
                sys.stdout.flush()
            time.sleep(0.4)
            i = (i + 1) % len(dots)

    def start(self):
        self.is_running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()

    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join()  # Wait safely for thread to finish
        
        # Clear line safely using the lock
        with self.lock:
            sys.stdout.write("\r\033[K")
            sys.stdout.flush()