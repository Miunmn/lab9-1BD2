import csv
import random
from utils import *


def random_quartile_radius(sample_list):
    random.seed(201810044)  # Pseudorandom para que sea replicable.
    distance_list = []
    answer_list = []
    for register in sample_list:
        distance_list.append(euclidian_distance(register, sample_list[random.randint(0, len(sample_list) - 1)]))
    distance_list.sort()
    answer_list.append(round(distance_list[len(distance_list)//4], 2))
    answer_list.append(round(distance_list[len(distance_list)//2], 2))
    answer_list.append(round(distance_list[(len(distance_list)*3)//4], 2))
    return answer_list

def range_search(register_list, query, radius):
    print(query)
    query_item = register_list[query]
    answer_list = []
    for register in register_list:
        if register != query:
            #print("query_item: ",query_item)
            #print("register: ",register)
            distance = euclidian_distance(query_item, register)
            if distance < radius:
                answer_list.append(register)
                # print(register)  # Descomentar para ver los registros en el rango
    hits = 0
    for register in answer_list:
        if query_item[4] == register[4]:
            hits += 1
    print("Precision: " + str(hits/len(answer_list)))
    return answer_list

def start(filename, query_list):
    with open(filename, newline='') as file:
        csvfile = csv.reader(file)
        register_list = []
        for row in csvfile:
            register_list.append(row)

    print(register_list)
    quartile_list = random_quartile_radius(register_list)

    for elem in query_list:
        for quartile in quartile_list:
            #print("Query: "+str(elem)+" Radius: "+str(quartile))
            range_search(register_list, elem, quartile)
            #print('\n')


if __name__ == "__main__":
    start("iris.data", [15, 82, 121])
