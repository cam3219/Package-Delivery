# Cameron Davis Student ID: 010438694
from random import shuffle

import Truck
import Time

from datetime import datetime


import csv
import Package
#create a time that the trucks will leave the hub at

time1 = datetime(year = 2023, month=3, day=27, hour = 8)

time2 = datetime(year = 2023, month=3, day=27, hour = 9, minute=10)

time3= datetime(year = 2023, month=3, day=27, hour=10)

#go through the distance csv and make a 2d list of the distances

with open('WGUPSDistanceCSV.csv', 'r', encoding='utf-8-sig') as csvfile:
    csv_reader = csv.reader(csvfile)
    distanceList = []

    for row in csv_reader:
        converted_row = [float(val) for val in row]
        distanceList.append(converted_row)


#call function to make hashmap and place all of the package objects inside of it

my_hash = Package.create_package_hash()






#initialize the truck objects with packages and a time that they leave the hub at


t1 = Truck.Truck([29, 13, 37, 21, 16, 40, 30, 19, 34, 1, 8, 14, 31, 20, 15], time1)
t2 = Truck.Truck([35, 3, 18, 11, 6, 33, 7, 2, 36, 26, 17, 28, 27, 38, 25, 39], time2)


t3 = Truck.Truck([9, 4, 32, 10, 22, 12, 23, 5, 24], time3)

#run the main program to deliver the packages

Time.mainProgram(t1, distanceList, my_hash)

Time.mainProgram(t2, distanceList, my_hash)

Time.mainProgram(t3, distanceList, my_hash)


#loop for user interface

exit = False

while exit == False:

#lets user choose an option
    userInputChoice = input("Choose from the following options:\n"
        "1) Check on the statuses of all of the packages at a given time\n"
        "2) Display the total mileage traveled by all trucks\n"
        "3) Check on a single package status at a given time\n"
        "4) Exit program\n")



    if int(userInputChoice) == 1 or int(userInputChoice) == 3:
        #get the input as a time and format it so we can create a datetime object to compare it to other times
        timeInput = input("Enter a time in the format HH:MM as 24-hour time:\n").split(":")

        if int(userInputChoice) == 3:
            packageInputChoice = input("What is the ID of the package you would like to check?\n")

        timeInput[0] = int(timeInput[0])
        timeInput[1] = int(timeInput[1])

        timeInputDatetime = datetime(year=2023, month = 3, day= 27, minute = timeInput[1], hour=timeInput[0])

        print("The time you entered:",timeInputDatetime.strftime('%H:%M'))

    #go through all of the package id's and print

        for i in range(1, 41):
            packageAtTime = my_hash.get(i)
            if int(packageAtTime[0]) == 9 and timeInputDatetime > datetime(2023, 3, 27, 10, 20):
                packageAtTime[1] = '410 S State St'
                packageAtTime[2] = 'Salt Lake City'
                packageAtTime[4] = '84111'
            if packageAtTime[8] > timeInputDatetime:
                packageAtTime[7] = "En route"
            if packageAtTime[9] > timeInputDatetime:
                packageAtTime[7] = "At the hub"
            #format time


            calculateMiles = 18 * (timeInputDatetime - packageAtTime[9])
            packageAtTime[8] = packageAtTime[8].strftime('%H:%M:%S')
            packageAtTime[8] = "Calculated Delivery Time: " + packageAtTime[8]
            packageAtTime[9] = packageAtTime[9].strftime('%H:%M:%S')
            packageAtTime[9] = "Calculated time to leave hub: "+ packageAtTime[9]
            my_hash.add(i, packageAtTime)
            if int(userInputChoice) == 1:
                print(my_hash.get(i))
        if int(userInputChoice) == 3:
            print(my_hash.get(int(packageInputChoice)))
        exit = True

    if int(userInputChoice) == 2:
        print("Truck 1 traveled a total of " + str(t1.miles_traveled)+ " miles")
        print("Truck 2 traveled a total of: " + str(t2.miles_traveled)+ " miles")
        print("Truck 3 traveled a total of: " + str(t3.miles_traveled)+ " miles")
        print("The total that mileage traveled by all trucks: " + str(t1.miles_traveled + t2.miles_traveled + t3.miles_traveled))
        exit = True












    if int(userInputChoice) == 4:
        exit = True



