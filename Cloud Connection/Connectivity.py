import threading
import time
import http.client as httplib

def internet_access() -> bool:
    conn = httplib.HTTPSConnection("1.0.0.2", timeout=5)
    try:
        conn.request("HEAD", "/")
        return True
    except Exception:
        return False
    finally:
        conn.close()

def perform_processes_on_internet_available():
    print("Internet is available. Performing processes...")#

def internet_check_thread():
    global stop_signal
    while not stop_signal:
        if internet_access():
            perform_processes_on_internet_available()
            stop_internet_check_thread()
        else:
            print("No internet connection. Retrying in 10 seconds...")
            time.sleep(10)
            internet_check_thread()

def stop_internet_check_thread():
    global stop_signal
    with stop_signal_lock:
        stop_signal = True



if __name__ == "__main__":
    stop_signal = False
    stop_signal_lock = threading.Lock()

    # Start the internet check thread in the background
    internet_thread = threading.Thread(target=internet_check_thread, daemon=False)
    internet_thread.start()

    print("Main code is running.")
    time.sleep(2)
    print("Main code continues...")

    print(internet_thread.is_alive())
