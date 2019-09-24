# Travelling Salesman

Suppose there are a number of "cities". The distance between any two cities is the standard Euclidean distance, that is, √((x1-x2)2+(y1-y2)2). A traveling salesman wishes to visit every city exactly once, then return to his starting point. (It doesn't matter what city is the starting point.) Such a path is called a circuit. However, the salesman also wishes to minimize the total distance that must be traveled.

The travelling salesman problem (TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?" It is an NP-hard problem in combinatorial optimization, important in operations research and theoretical computer science.

The problem has been solved using "hill climbing" approach, where you start with "any" solution, and try to progressively improve it until you can't improve it any more.

## Function Definitions 

def read_cities(file_name): </br>
Read in the cities from the given file_name, and return them as a list of four-tuples: [(state, city, latitude, longitude), ...] Use this as your initial road_map, that is, the cycle Alabama → Alaska → Arizona → ... → Wyoming → Alabama.

def print_cities(road_map): </br>
Prints a list of cities, along with their locations. Print only one or two digits after the decimal point.

def compute_total_distance(road_map): </br>
Returns, as a floating point number, the sum of the distances of all the connections in the road_map. Remember that it's a cycle, so that (for example) in the initial road_map, Wyoming connects to Alabama.

def swap_adjacent_cities(road_map, index): </br>
Take the city at location index in the road_map, and the city at location index+1 (or at 0, if index refers to the last element in the list), swap their positions in the road_map, compute the new total distance, and return the tuple (new_road_map, new_total_distance).

def swap_cities(road_map, index1, index2): </br>
Take the city at location index in the road_map, and the city at location index2, swap their positions in the road_map, compute the new total distance, and return the tuple (new_road_map, new_total_distance). Allow the possibility that index1=index2, and handle this case correctly.

def find_best_cycle(road_map): </br>
Using a combination of swap_cities and swap_adjacent_cities, try 10000 swaps, and each time keep the best cycle found so far. After 10000 swaps, return the best cycle found so far.

def print_map(road_map): </br>
Prints, in an easily understandable format, the cities and their connections, along with the cost for each connection and the total cost.

def main() </br>
Reads in and prints out the city data, then creates the "best" cycle and prints it out.
