

import Package
from datetime import timedelta




#set the original values for the truck
class Truck:
    def __init__(self, packages, originalTime):
        self.packages = packages
        self.current_location = 0
        self.miles_traveled = 0
        self.originalTime = originalTime



    def add_package(self, package):
        self.packages.append(package)


#replacing the package with the values of the old one
    def deliver_package(self, package, min_package_id_index, my_hash):
        self.packages.remove(package)
        self.current_location = int(min_package_id_index)
        newPackage = Package.get_package_attributes(my_hash, package)
        #convert miles to time
        timeConversion = self.miles_traveled/18
        #timedelta is easier to make than datetime
        addTime = timedelta(hours=timeConversion) + self.originalTime
        newPackage[8] = addTime
        newPackage[7] = "Delivered"
        newPackage[9] = self.originalTime
        #replace the package with new values
        my_hash.add(package, newPackage)



    def add_time(self, startTime):
        #time = distance/speed
        theTime = self.miles_traveled/18
        return theTime


    def find_next_closest_package(self, distance_matrix, my_hash):
        #this makes it so the first value is always the min value and there will always be a min value
        min_package_id_index = float('inf')
        min_distance = float('inf')
        closest_package = None

#go through all of the packages that got inputted the truck
        for package_id in self.packages:
            #get the index from the csv
            package_id_index = Package.get_index_from_csv(my_hash, package_id, file_path='addressCSV.csv')
            #get the distance using the distance matrix at what location we are at
            package_distance = distance_matrix[self.current_location][int(package_id_index)]
            #find the min value in an array and set values so they are easier to return
            if package_distance <= min_distance:
                min_distance = package_distance
                min_package_id_index = package_id_index
                closest_package = package_id
        #add the miles to the total mileage
        self.miles_traveled += min_distance
        self.deliver_package(closest_package, min_package_id_index, my_hash)
        return closest_package
