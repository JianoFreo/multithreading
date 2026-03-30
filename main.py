import threading
import time

done = False

def worker(text):
    # global done
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(f"{text}: {counter}")
        # if counter == 10:
        #     done = True
        
thread1 = threading.Thread(target=worker, daemon=True, args=("ABC",))
thread2 = threading.Thread(target=worker, daemon=True, args=("XYZ",))

thread1.start()
thread2.start()

# A program will automatically terminate when only daemon threads are left running.
# In contrast, non-daemon (user) threads must finish before the program exits.
# daemon only runs as a background of main threads

input("Press enter to quit")
done = True



