import random
from math import *
import csv
from pprint import pprint

def read_cities(file_name):
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        l = list(map(tuple, reader))
        return l

def print_cities(road_map):
    for i in range(len(road_map)):
        f1 = float("{0:.2f}".format(float(road_map[i][2])))
        f2 = float("{0:.2f}".format(float(road_map[i][3])))
        print("City ",i+1," is ", road_map[i][1], " which has latitude",f1, " and longitude ", f2)

def print_map(road_map):
    newtaglist = [road_map[i % len(road_map)] for i in range(len(road_map))]
    temp2=0
    print("BEST PATH IS")
    for i in range(len(road_map)):
        if i!=len(road_map)-1:
            print(newtaglist[i][0],"->", end=" ")
        else:
            print(newtaglist[i][0],"->",newtaglist[0][0])
    print("PATH FOLLOWED BY SALESMAN IS")
    for i in range(len(road_map)):
        if i!= len(road_map)-1:
            x=compute_total_distance(road_map[i:((i+1)%len(road_map)+1)])/2
        else:
            x=compute_total_distance([road_map[-1],road_map[0]])/2
        temp2=temp2+x
        print("Salesman going from", newtaglist[i][0], " to", newtaglist[(i + 1) % len(road_map)][0], "travelling a distance of ", x)
    print("FINAL DISTANCE IS=",temp2)

def compute_total_distance(road_map):
    newtaglist = [road_map[i % len(road_map)] for i in range(len(road_map))]
    temp=0
    for i in range(len(road_map)):
        x=distance(float(newtaglist[i][2]),float(newtaglist[i][3]),float(newtaglist[(i + 1) % len(road_map)][2]),float(newtaglist[(i + 1) % len(road_map)][3]))
        temp=temp+x
    return temp

def swap_adjacent_cities(road_map, index):
    new_road_map=road_map
    if index!=len(new_road_map)-1:
        temp=new_road_map[index]
        new_road_map[index]=new_road_map[index+1]
        new_road_map[index+1]=temp
    else:
        temp = new_road_map[index]
        new_road_map[index] = new_road_map[0]
        new_road_map[0] = temp
    new_distance=compute_total_distance(new_road_map)
    return (new_road_map,new_distance)

def swap_cities(road_map, index1, index2):
    new_road_map = road_map
    if index1!= index2:
        temp = new_road_map[index1]
        new_road_map[index1] = new_road_map[index2]
        new_road_map[index2] = temp
    new_distance = compute_total_distance(new_road_map)
    return (new_road_map, new_distance)

def find_best_cycle(first_road_map):
    best_distance=9999999
    road_map1 = first_road_map.copy()
    road_map2 = first_road_map.copy()
    road_map3 = first_road_map.copy()
    for i in range(10000):
        number1 = int(50 * random.random())
        number2=int(50 * random.random())
        temp1=swap_adjacent_cities(road_map1,number1)
        temp2=swap_adjacent_cities(road_map2,number2)
        temp3=swap_cities(road_map3,number1,number2)
        d1=temp1[1]
        d2=temp2[1]
        d3 = temp3[1]
        temp=min(d1,d2,d3)
        if best_distance>temp and temp==d1:
            best_distance=d1
            best_city=temp1[0].copy()
        elif best_distance>temp and temp==d2:
            best_distance=d2
            best_city=temp2[0].copy()
        elif best_distance>temp and temp==d3:
            best_distance=d3
            best_city=temp3[0].copy()
    print_map(best_city)

def distance(lat1degrees, long1degrees, lat2degrees, long2degrees):
    earth_radius = 3956  # miles
    lat1 = radians(lat1degrees)
    long1 = radians(long1degrees)
    lat2 = radians(lat2degrees)
    long2 = radians(long2degrees)
    lat_difference = lat2 - lat1
    long_difference = long2 - long1
    sin_half_lat = sin(lat_difference / 2)
    sin_half_long = sin(long_difference / 2)
    a = sin_half_lat ** 2 + cos(lat1) * cos(lat2) * sin_half_long ** 2
    c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
    return earth_radius * c

def main():
        file_name="C:/Users/mohit/Desktop/ts.csv"
        x=read_cities(file_name)
        find_best_cycle(x)

main()
