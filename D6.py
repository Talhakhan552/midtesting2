# CHATGPT TIME GREETING 

import datetime

print(datetime)

# Get the current time
current_time = datetime.datetime.now()
hour = current_time.hour

# Define greetings based on the time of day
if 5 <= hour < 12:
    greeting = "Good morning!"
elif 12 <= hour < 17:
    greeting = "Good afternoon!"
elif 17 <= hour < 20:
    greeting = "Good evening!"
else:
    greeting = "Good night!"

# Display the greeting
print(greeting)



# -----------------QUESTION NO.1------------
# Time greeting program

import time

time_1 = time.strftime("%H:%M:%S")
print(time_1)

if(time_1>'07:00:00'):
    print("GOOD MORNING")
elif(time_1>'12:00:00'):
    print("GOOD AFTERNOON")
elif(time_1>'19:00:00'):
    print("GOOD NIGHT")
else:
    print("NICE")
    

# -------------QUESTION NO.2----------------
# Number identification

num = int(input("Enter a number : "))

if(num>0):
    print("It is positive")
elif(num<0):
    print("It is negative")
else:
    print("It is zero")
    
    



