import numpy as np
import csv
import matplotlib.pyplot as plt

with open('../data/train.csv', 'r') as csvfile:
    for data in csv.reader(csvfile):
        label = data[0]
        pixels = data[1:]
        pixels = np.array(pixels, dtype='uint8')
        pixels = pixels.reshape((28,28))
        plt.title('Label is {label}'.format(label=label))
        plt.imshow(pixels, cmap='gray')
        plt.show()
        break
