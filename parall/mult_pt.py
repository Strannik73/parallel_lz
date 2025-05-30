
import threading
import time
from PIL import Image, ImageFilter
class m_pt:
    def write_file(file_name, data):
        with open(file_name, 'w') as f:
            f.write(data)
            time.sleep(1)  # Имитация долгой операции записи

    def process_image(path):
        img = Image.open(path)
        img = img.filter(ImageFilter.GaussianBlur(10))
        img.save(f"processed_{path}")
        print(f"processed_{path}")
        
    def __del__(self):
        print('удаление')  
          
def main():
    # Синхронная запись
    start = time.time()
    for i in range(5):
        m_pt.write_file(f"sync_file_{i}.jpg", "Hello")
    sync_time = time.time() - start
    print(f"Синхронная запись: {sync_time:.2f} сек")

    # Многопоточная запись
    start = time.time()
    threads = []
    for i in range(10):
        t = threading.Thread(target=m_pt.write_file, args=(f"thread_file_{i}.jpg", "Hello"))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    thread_time = time.time() - start
    print(f"Многопоточная запись: {thread_time:.2f} сек")

    if __name__ == "__main__":
        main()