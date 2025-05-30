
# multithreading.py
import threading
import time
from PIL import Image, ImageFilter

def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)
        time.sleep(1)  # Имитация долгой операции записи

def process_image(path):
    img = Image.open(path)
    img = img.filter(ImageFilter.GaussianBlur(10))
    img.save(f"processed_{path}")
    print(f"processed_{path}")

# Синхронная запись
start = time.time()
for i in range(5):
    write_file(f"sync_file_{i}.jpg", "Hello")
sync_time = time.time() - start
print(f"Синхронная запись: {sync_time:.2f} сек")

# Многопоточная запись
start = time.time()
threads = []
for i in range(5):
    t = threading.Thread(target=write_file, args=(f"thread_file_{i}.jpg", "Hello"))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
thread_time = time.time() - start
print(f"Многопоточная запись: {thread_time:.2f} сек")