import tensorflow as tf
import numpy as np
import pickle
import itertools


def fact(n):
    if n == 1:
        return 1
    result = n * fact(n - 1)
    return result

def signalMatrix(label, rank, length, num_label):

    # flabel = open(r"D:\Workspace\Experiments\Dataset\sinainformation\1220\label.txt", "rb")  # label 0 1 0 0 1 1
    # fvotes = open(r"D:\Workspace\Experiments\Dataset\sinainformation\1220\votes.txt", "rb")
    # fnorm = open(r"D:\Workspace\Experiments\Dataset\sinainformation\1220\normedlabel.txt", "rb")
    # flength = open(r"D:\Workspace\Experiments\Dataset\sinainformation\1220\length.txt", "rb")
    # frank = open(r"D:\Workspace\Experiments\Dataset\sinainformation\1220\rank.txt", "rb")
    # fheadline = open(r"D:\Workspace\Experiments\Dataset\sinainformation\1220\headline.txt", "rb")
    # ftext = open(r"D:\Workspace\Experiments\Dataset\sinainformation\1220\text.txt", "rb")
    # print(pickle.load(fheadline))
    # # print(pickle.load(ftext))
    # print(pickle.load(flabel))
    # print(pickle.load(fvotes))
    # print(pickle.load(fnorm))
    # print(pickle.load(flength))
    # print(pickle.load(frank))

    # label = pickle.load(flabel)
    # rank = pickle.load(frank)
    # length = pickle.load(flength)
    label = np.array(label)
    rank = np.array(rank)
    length = np.array(length)

    labelT = label.reshape(-1,1,num_label)
    rankingsignal = np.transpose(labelT,[0,2,1])-labelT


    listrelevant = []
    for i in range(len(length)):
        mat = np.zeros((num_label, num_label))
        listcombine = list(itertools.permutations(rank[i,0:length[i]], 2))
        for j in range(len(listcombine)):
            if j in range(fact(length[i]-1)):
                mat[listcombine[j][0]][listcombine[j][1]] = 1
            else:
                mat[listcombine[j][0]][listcombine[j][1]] = -1
        listrelevant.append(mat)
    listrelevant = np.array(listrelevant)

    prolosssignal = rankingsignal + listrelevant

    return rankingsignal, prolosssignal

# print(label[3, :], labelT[3, :, :], rankingsignal[3, :, :], rank[3, :], prolosssignal[3, :, :])
