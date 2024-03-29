from AC_first import ac, acWithAddnum
import random
from ShowProcess import ShowProcess
from addnumList import getAddnumOddList, getAddnumList
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time


def count_one(n):
    sum = 0
    while(n):
        sum += 1
        n &= (n-1)
    return sum


def accuracy_test():
    n = 1023
    addnum = 1
    length, chain = acWithAddnum(n, addnum)
    print(length)
    print(chain)


def param_amount_test(n):
    # generate different bit addnum
    i = 0
    bit_max = len(bin(n)[2:]) // 2
    addnum_list = []
    length_list = []
    max_steps = 2**bit_max
    process_bar = ShowProcess(max_steps - 1, 'down')
    for addnum in range(1, max_steps):
        addnum_list.append(addnum)
        length, _ = acWithAddnum(n, addnum)
        length_list.append(length)
        i += 1
        process_bar.show_process()
    fig, ax = plt.subplots()
    sns.set()
    ax.scatter(addnum_list, length_list)
    plt.title(str(n))
    plt.savefig('img/test_param_amount/addition_chain_' + str(bin(n)) + '.png')
    # ax.legend()
    # plt.show()
    # return addnum_list, length_list


def param_amount_diffbit_test(n):
    # generate different bit addnum
    i = 0
    data = {str(i): [[], []] for i in range(1, 11)}
    addnum_list = getAddnumOddList(1024)
    process_bar = ShowProcess(len(addnum_list), 'down')
    for addnum in addnum_list:
        index = str(count_one(addnum))
        data[index][0].append(addnum)
        length, _ = acWithAddnum(n, addnum)
        data[index][1].append(length)
        i += 1
        process_bar.show_process()
    # plt.figure(figsize=(4, 4))
    fig, ax = plt.subplots(figsize=(13, 6))
    sns.set()
    for key in data:
        ax.scatter(data[key][0], data[key][1], label=key)
    ax.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)
    plt.title(str(len(bin(n)[2:])))
    plt.savefig('img/test_param_amount_diffbit/addition_chain_' + str(len(bin(n)[2:])) + '.png')
    
    return data


def ratio_param(ratio):
    # generate some data with the radio
    # bit-range(every range with 10 num)
    # 1-64
    # 64-128
    # 128-512
    # 512-1024
    # 1024-2048
    # 2048-4096
    bit_range = [64, 128, 512, 1024, 2048, 4096]
    data_list = []
    for ran in bit_range:
        num = 0
        r = int(ratio * ran)
        nonce = [random.randint(0, ran - 1) for _ in range(r)]
        for bit in nonce:
            num |= (1 << bit)
        data_list.append(num)

    addnum_list = getAddnumOddList(1024)
    max_steps = len(data_list) * len(addnum_list)
    i = 0
    process_bar = ShowProcess(max_steps, 'down')
    for data in data_list:
        data_dict = {str(i): [[], []] for i in range(1, 11)}
        for addnum in addnum_list:
            index = str(count_one(addnum))
            data_dict[index][0].append(addnum)
            length, _ = acWithAddnum(data, addnum)
            data_dict[index][1].append(length)
            i += 1
            process_bar.show_process()
        fig, ax = plt.subplots(figsize=(13, 6))
        sns.set()
        for key in data_dict:
            ax.scatter(data_dict[key][0], data_dict[key][1], label=key)
        ax.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)
        plt.title(str(len(bin(data)[2:])))
        plt.savefig('img/ratio--' + str(ratio) + '/addition_chain_' + str(len(bin(data)[2:])) + '.png')

    return data


if __name__ == "__main__":
    '''
    start = time.time()
    process_bar = ShowProcess(100, 'down')
    for i in range(100):
        length, _ = acWithAddnum(1487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482148797428148214879742814821487974281482, 1024)
        process_bar.show_process() 
    end = time.time()
    print(str(100/(end-start)) + 'cps')
    print(length)
    '''
    '''
    start = time.time()
    for i in range(6, 25):
        param_amount_test(random.randint(2**(i-1), 2**i))
    end = time.time()
    print(str(end - start) + 's')
    '''
    ratio_param(0.1)
    ratio_param(0.2)
    ratio_param(0.3)
    ratio_param(0.4)
    ratio_param(0.5)
    ratio_param(0.6)
    ratio_param(0.7)
    ratio_param(0.8)
    ratio_param(0.9)
    ratio_param(1.0)
