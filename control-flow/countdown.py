import time
def countdown_while(n):
    while n >= 0:
        print(n)
        time.sleep(1)  # Wait for 1 second
        n -= 1
    print("Countdown finished!")

def countdown_for(n):
    for i in reversed(range(n + 1)):
        print(i)
        time.sleep(1)  # Wait for 1 second
    print("Countdown finished!")   

if __name__ == "__main__":
    countdown_while(5)
    print("-----")
    countdown_for(5)
    