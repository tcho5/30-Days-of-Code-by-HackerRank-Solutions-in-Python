#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    validNamesList = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if emailID.find("@gmail.com") != -1: #gmail email found
            validNamesList.append(firstName)
    for i in sorted(validNamesList):
        print(i)
    
            
        
        
        
        
