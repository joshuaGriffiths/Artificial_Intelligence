#JOSHUA GRIFFITHS
#Problem Set 4 Question 1
#Fall 2017
#ARTIFICIAL INTELEGENCE
#Insperation gotten from Brian Faure youtube video: Single-Layer Perceptron: Backround and Python Code

from __future__ import print_function
import sys
from matplotlib import pyplot as plt
import numpy as np
from random import randrange, uniform
import math

#Calculates Projected Output given inputs and current weights
def predict(inputs,weights):

    threshold = 0.0
    total_activation = 0.0

    for inputs, weights in zip(inputs,weights):

        total_activation += inputs*weights

    return 1.0 if total_activation >= threshold else 0.0


#calculates our prediction for each input and compares that to what our desired output was
def accuracy(matrix,weights):

    num_correct = 0.0
    preds = []
    for i in range(len(matrix)):

        pred = predict(matrix[i][:-1], weights)
        preds.append(pred)

        #compares our prediction (projected output) of each input to what the actual desired output is
        #if it is correct then we can assume that that weight is accurate
        if pred == matrix[i][-1]:

            num_correct += 1

#   print ("Predictions: ", )

    #return the percentage of predictions that are correct
    return num_correct/ float(len(matrix))

#samples = number of times we going through and training the weights
#alpha = learning rate = how much were changing the weights at each iteration
#do_plot = do we want to plot and see our data and threshold at each sample?
#stop_early = when accuracy reaches 100 percent before last sample we can exit early
#verbose = print out wieghts and
def train_weights(matrix,weights,samples=10.0,alpha=1.0,do_plot=False,stop_early=True,verbose=True):

    for sample in range(samples):

        cur_accuracy = accuracy(matrix,weights)
        #print("\nSample %d \nWeights: " %sample,weights)
        #print("Current Accuracy: ",cur_accuracy)

        if cur_accuracy == 1.0 and stop_early: break

        if do_plot: plot(matrix,weights,title="Epoch %d"%sample)

        #iterate over each training input
        for i in range(len(matrix)):

            #Projected output for each input
            prediction = predict(matrix[i][:-1],weights)

            #Desired Output - Projected output
            error = matrix[i][-1] - prediction

            #if verbose:
                #print ("More Data")
                
            
                #calculate the sum of the inputs
                #sumInput = sum((matrix[i][1:-1])*weights[1:-1])

            # iterate over each weight in perceptron and update it
            for j in range(1,len(weights)):
                
                
                sumInput = weights[j] * matrix[i][j]
                #Update each of the weights by adding the product of the overall error
                #and the prior input to that specific weight
                
                #print (sumInput)
                gin = (1/(1+(2.27**(-sumInput))))   *    (1-   (1/(1+(2.27**(-sumInput)))))
                weights[j] = weights[j] + (alpha * error * gin * matrix[i][j])
               

#   plot(matrix,weights,title="Final Sample")
    return weights


def main():

    #Training Data:
    #        D,    A,    B,    C      y(output)
    data = [[1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 1.0, 0.0],
            [1.0, 0.0, 1.0, 0.0, 0.0],
            [1.0, 1.0, 0.0, 0.0, 0.0],
            [1.0, 0.0, 1.0, 1.0, 0.0],
            [1.0, 1.0, 1.0, 0.0, 0.0],
            [1.0, 1.0, 0.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0]]



    #Starting Weights
    #            wD          weightA              weightB              weightC
    weights = [-1.0, uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)]
    #weights = [-1.0, 0.35, -0.43, -0.78]
    
    print ("Old Wieghts: ", weights)

    newWeights = train_weights(data,weights=weights,samples=250,alpha=1,do_plot=False,stop_early=False)

    print ("New Weights: ", newWeights)


#Method Taken from Brian Faure
#Graphically Plots Data and Seperation
def plot(matrix, weights=None, title="Prediction Matrix"):
    if len(matrix[0]) == 3:  # if 1D inputs, excluding bias and ys
        fig, ax = plt.subplots()
        ax.set_title(title)
        ax.set_xlabel("i1")
        ax.set_ylabel("Classifications")

        if weights != None:
            y_min = -0.1
            y_max = 1.1
            x_min = 0.0
            x_max = 1.1
            y_res = 0.001
            x_res = 0.001
            ys = np.arange(y_min, y_max, y_res)
            xs = np.arange(x_min, x_max, x_res)
            zs = []
            for cur_y in np.arange(y_min, y_max, y_res):
                for cur_x in np.arange(x_min, x_max, x_res):
                    zs.append(predict([1.0, cur_x], weights))
            xs, ys = np.meshgrid(xs, ys)
            zs = np.array(zs)
            zs = zs.reshape(xs.shape)
            cp = plt.contourf(xs, ys, zs, levels=[-1, -0.0001, 0, 1], colors=('b', 'r'), alpha=0.1)

        c1_data = [[], []]
        c0_data = [[], []]

        for i in range(len(matrix)):
            cur_i1 = matrix[i][1]
            cur_y = matrix[i][-1]

            if cur_y == 1:
                c1_data[0].append(cur_i1)
                c1_data[1].append(1.0)
            else:
                c0_data[0].append(cur_i1)
                c0_data[1].append(0.0)

        plt.xticks(np.arange(x_min, x_max, 0.1))
        plt.yticks(np.arange(y_min, y_max, 0.1))
        plt.xlim(0, 1.05)
        plt.ylim(-0.05, 1.05)

        c0s = plt.scatter(c0_data[0], c0_data[1], s=40.0, c='r', label='Class -1')
        c1s = plt.scatter(c1_data[0], c1_data[1], s=40.0, c='b', label='Class 1')

        plt.legend(fontsize=10, loc=1)
        plt.show()
        return

    if len(matrix[0]) == 5:  # if 2D inputs, excluding bias and ys
        fig, ax = plt.subplots()
        ax.set_title(title)
        ax.set_xlabel("i1")
        ax.set_ylabel("i2")

        if weights != None:
            map_min = 0.0
            map_max = 1.1
            y_res = 0.001
            x_res = 0.001
            ys = np.arange(map_min, map_max, y_res)
            xs = np.arange(map_min, map_max, x_res)
            zs = []
            for cur_y in np.arange(map_min, map_max, y_res):
                for cur_x in np.arange(map_min, map_max, x_res):
                    zs.append(predict([1.0, cur_x, cur_y], weights))
            xs, ys = np.meshgrid(xs, ys)
            zs = np.array(zs)
            zs = zs.reshape(xs.shape)
            cp = plt.contourf(xs, ys, zs, levels=[-1, -0.0001, 0, 1], colors=('b', 'r'), alpha=0.1)

        c1_data = [[], [],[]]
        c0_data = [[], [],[]]
        for i in range(len(matrix)):
            cur_i1 = matrix[i][1]
            cur_i2 = matrix[i][2]
            cur_i3 = matrix[i][3]
            cur_y = matrix[i][-1]
            if cur_y == 1:
                c1_data[0].append(cur_i1)
                c1_data[1].append(cur_i2)
                c1_data[2].append(cur_i3)
            else:
                c0_data[0].append(cur_i1)
                c0_data[1].append(cur_i2)
                c0_data[2].append(cur_i3)

        plt.xticks(np.arange(0.0, 1.1, 0.1))
        plt.yticks(np.arange(0.0, 1.1, 0.1))
        plt.xlim(0, 1.05)
        plt.ylim(0, 1.05)

        c0s = plt.scatter(c0_data[0], c0_data[1], s=40.0, c='r', label='Class -1')
        #c1s = plt.scatter(c1_data[0], c1_data[1], s=40.0, c='b', label='Class 1')
        c2s = plt.scatter(c1_data[0], c1_data[2], s=40.0, c='b', label='Class 1')
        plt.legend(fontsize=10, loc=1)
        plt.show()
        return

    print("Matrix dimensions not covered.")


if __name__ == '__main__':
	main()
