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
worker()

input("Press enter to quit")
done = True

