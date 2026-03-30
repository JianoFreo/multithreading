import threading
import time

done = False

def worker():
    # global done
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)
        # if counter == 10:
        #     done = True
        
threading.Thread(target=worker, deamon=True).start()

# A program will automatically terminate when only daemon threads are left running.
# In contrast, non-daemon (user) threads must finish before the program exits.
# daemon only runs as a background of main threads

input("Press enter to quit")
done = True



