# Assignment 2

Assignment Date: 24 September, 2022 

Maximum Marks: 4

Student Roll Number: 718019Z334

## Assignment Details

Technology: Internet of Things

Domain: Smart Solution for Railways

## Problem Statement

Build a python code assuming you get temperature and humidity values (Generated with random function) and write a condition to continuously detect alarm in case of high temperature.



## Solution

```python
import random

min_temp = 10
max_temp = 50

min_hum = 30
max_hum = 60

overflow = 20

def getRandomVal(min, max, overflow):
    return random.randrange(min - overflow, max + overflow)

outFile = open("alarm_output.txt", "w")

maxLoopCount = 100
for i in range(maxLoopCount):
    temp = getRandomVal(min_temp, max_temp, overflow)
    hum = getRandomVal(min_hum, max_hum, overflow)

    outFile.write("Temperature: " + str(temp) + "  \tHumidity: " + str(hum) + "\t-----")

    if (temp > max_temp or temp < min_temp and hum > max_hum or hum < min_hum):
        outFile.write("\tALARM: Temperature and Humidity not safe!")

    elif (temp > max_temp or temp < min_temp):
        outFile.write("\tALARM: Temp not safe!")
    
    elif (hum > max_hum or hum < min_hum):
        outFile.write("\tALARM: Humidity not safe!")
    
    else:
        outFile.write("\tNo Alarm!")

    outFile.write("\n")
```



## Output
[alarm_output.txt](https://github.com/IBM-EPBL/IBM-Project-39046-1660389861/blob/main/Assesments/Nikhil%20Dhaka/Assignment%202/alarm_output.txt)