import Truck
#this part is just used as a kind of loop to deliver all of the packages
def mainProgram(truck, distanceList, my_hash):
    truckPath = []
    while len(truck.packages) > 0:
        truckPath.append(Truck.Truck.find_next_closest_package(truck, distanceList, my_hash))

    