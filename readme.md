#  Python Threading Example (Daemon Threads, join(), and Shared State)

This project demonstrates how Python threading works, specifically
focusing on:

-   Creating threads using the `threading` module\
-   Daemon vs non-daemon threads\
-   The use of a shared global variable\
-   Thread termination control\
-   The role of `join()` (commented for demonstration)

------------------------------------------------------------------------

##  Overview

The script runs two worker threads that continuously print counters
while a shared flag (`done`) remains `False`. The program ends when the
user presses Enter, which sets `done = True`, signaling the threads to
stop.

------------------------------------------------------------------------

##  Code Explanation

### Shared Global Variable

done = False

Acts as a shared flag between threads. When set to True, threads stop
execution.

------------------------------------------------------------------------

### Worker Function

```
def worker(text): counter = 0 while not done: time.sleep(1) counter += 1
print(f"{text}: {counter}")
```

Each thread runs this function and prints a counter every second.

------------------------------------------------------------------------

### Creating Threads
```
thread1 = threading.Thread(target=worker, daemon=True, args=("ABC",))
thread2 = threading.Thread(target=worker, daemon=True, args=("XYZ",))
```

Two daemon threads are created: - thread1 prints "ABC" - thread2 prints
"XYZ"

Daemon threads run in the background and do not block program exit.

------------------------------------------------------------------------

### Starting Threads

thread1.start() thread2.start()

Begins concurrent execution of both threads.

------------------------------------------------------------------------

### Daemon Threads Behavior

Daemon threads automatically stop when the main program exits. If only
daemon threads remain, Python will terminate the program.

------------------------------------------------------------------------

### join() (Commented Out)

thread1.join() thread2.join()

join() makes the main thread wait until the thread finishes execution.

------------------------------------------------------------------------

### User Input to Stop Threads

input("Press enter to quit") done = True

The program waits for user input. When Enter is pressed, the shared flag
is set to True, stopping both threads.

------------------------------------------------------------------------

##  Key Concepts

### Daemon vs Non-Daemon Threads

Daemon threads: Run in background and terminate when the main program
exits\
Non-daemon threads: Must complete before the program exits

------------------------------------------------------------------------

### join() Behavior

-   join() → main thread waits for thread completion\
-   Without join() → main thread continues immediately

------------------------------------------------------------------------

### Shared Variables in Threads

Threads share memory, so variables like `done` can be accessed across
threads. This example does not use locks or synchronization mechanisms.

------------------------------------------------------------------------

## ▶ How to Run

python your_script.py

Then: 1. Observe both threads printing output 2. Press Enter 3. Threads
stop and program exits

------------------------------------------------------------------------

## =====Notes=======

-   This example uses a simple boolean flag for thread control
-   In production, consider:
    -   threading.Lock
    -   threading.Event
    -   queue.Queue

------------------------------------------------------------------------

## Reviewer Section

### Strengths

-   Clear demonstration of threading basics
-   Proper use of daemon threads
-   Simple and readable structure

### Improvements

-   Consider using threading.Event instead of a boolean flag
-   No synchronization primitives used
-   join() could be demonstrated separately for clarity

Example improvement:

import threading done = threading.Event()

```
def worker(text): counter = 0 
    while not done.is_set(): 
        time.sleep(1)
        counter += 1 print(f"{text}: {counter}")

done.set()
```
