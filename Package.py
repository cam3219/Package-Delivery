from datetime import datetime

import csv

import makeHashMap


class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, delivery_status, time_delivered):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.delivery_status = delivery_status
        self.time_delivered = time_delivered
        self.leftHub = None



    # Customize string output to avoid returning the object reference
    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (self.package_id, self.address, self.city, self.state, self.zipcode, self.deadline,
                                                  self.weight, self.delivery_status, self.time_delivered, self.leftHub)

    def getDistance(self):
        return self.distance








# Function to read package data from a CSV file and return it in a hash table
def create_package_hash():
        # Create a hash table object

    my_hash = makeHashMap.HashMap()

        # Read CSV file
    with open('packageCSV.csv', encoding='utf-8-sig') as packages:
        package_data = csv.reader(packages, delimiter=',')
        for item in package_data:
            package_id = int(item[0])
            address = item[1]
            city = item[2]
            state = item[3]
            zipcode = item[4]
            deadline = item[5]
            weight = item[6]
            delivery_status = 'At the hub'
            time_delivered = None
                # Create a package object

            package = Package(package_id, address, city, state, zipcode, deadline, weight, delivery_status, time_delivered)

                # Add package to hash table
            my_hash.add(package_id, package)

    return my_hash



#easy way to get the package in a formatted way if necessary
def get_package_address(package_hash_table, package_id):
    package_object = format(package_hash_table.get(package_id)).split(',')
    return package_object[1]

def get_package_attributes(package_hash_table, package_id):
    package_attributes = format(package_hash_table.get(package_id)).split(',')
    return package_attributes
#how we get the index is go through and if the address matches return the package id

def get_index_from_csv(my_hash, packageId, file_path='addressCSV.csv'):
    with open(file_path, encoding='utf-8-sig') as addresses:
        csv_reader = csv.reader(addresses)

        for row in csv_reader:
            if row[2] == get_package_address(my_hash, packageId):
                return row[0]
        return None


