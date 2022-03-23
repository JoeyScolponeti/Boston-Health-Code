# -*- coding: utf-8 -*-
"""
Food
"""
import csv
import matplotlib.pyplot as plt

def max_citations(citations, header, data):
    max_location = ""
    max_citation = -1
    for key, value in citations.items():
        if value > max_citation:
            max_location = key
            max_citation = value
    
    i_add = header.index("address")
    i_city = header.index("city")
    
    for i in range(len(data)):
        if data[i][0] == max_location:
            i_worst = i
            break
        else:
            pass
    
    max_add = data[i_worst][i_add]
    max_city = data[i_worst][i_city]
    
    return max_location, max_citation, max_add, max_city

def main():
    
    with open("healthcsv.csv", "r") as infile:
        
        data = []
        csvfile = csv.reader(infile, delimiter = ",")
        for row in csvfile:
            data.append(row)
    
    header = data[0]
    
    citations = {}

    for i in range(len(data)):
        if data[i][0] in citations:
            citations[data[i][0]] += 1
        else:
            citations[data[i][0]] = 1
        
    worst, w_number, w_add, w_city = max_citations(citations, header, data)
    print(worst, w_number, w_add, w_city)
    
        
    
main()
