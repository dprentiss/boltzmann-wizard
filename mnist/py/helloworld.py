import csv
import matplotlib.pyplot as plt

with open('../data/test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    next(reader)[0]
    print(next(reader)[0])
