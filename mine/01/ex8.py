"""set a timer"""

import time

while True:
    try:
        second=int(input("Enter the time :"))
        if second < 1:
            print("Please enter a number greater than 0")     
            continue
        break
    except ValueError:
        print("Invalid input,please enter a whole number")
        

print("--Timer started--")
for remaining in range(second,-1,-1):
    mins,secs=divmod(remaining,60)
    time_format=f"{mins:02}:{secs:02}"
    print(f"time left : {time_format}",end="\r")
    time.sleep(1)

print("Time's up ! take a break ")
print("\a")

    