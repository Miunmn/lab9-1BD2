import csv
from utils import *

k_values = [2, 4, 8, 16, 32]

def knnSearch(register_list, query, k_val):
    query_item = register_list[query]
    result = []
    for register in register_list:
        if register != query:
            distance = euclidian_distance(query_item, register)
            pair = (register, distance)
            result.append(pair)    
    result.sort(key = lambda tup: tup[1])
    return result[1:k_val]

def solve(query_list, register_list):
    for elem in query_list:
        for k_val in k_values:
            print(elem, k_val)
            knnresult = knnSearch(register_list, elem, k_val)
            print(knnresult[len(knnresult)-1])
            #for Ci, dist in knnresult:
            #    print(Ci,dist)
            print("\n")

def start(filename, query_list):
    with open(filename, newline='') as file:
        csvfile = csv.reader(file)
        register_list = []
        for row in csvfile:
            register_list.append(row)
    
    solve(query_list, register_list)


if __name__ == "__main__":
    start("iris.data", [15, 82, 121])