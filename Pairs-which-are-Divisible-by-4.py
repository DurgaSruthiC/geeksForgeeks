#Given an array if �n� positive integers, count number of pairs of integers in the array that have the sum divisible by 4.
#Input:
#The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each test-case has two lines of the input, the first line contains an integer denoting the size of an array N and the second line of input contains N positive integers.
#Output:
#Print the number of pairs of integers in the array that have the sum divisible by 4.
#Constraints:
#1<=T<=100
#1<=N<=100
#1<=arr[]<=1000
#Example:
#Input:
#2
#5
#2 2 1 7 5
#5
#2 2 3 5 6
#Output:
#3
#4
#Explanation:

#Testcase 1: (2,2), (1,7) and(7,5) are the 3 pairs.

#Testcase 2: (2,2), (2,6), (2,6), (3,5) are the 4 pairs.

#** For More Input/Output Examples Use 'Expected Output' option **

def check_divisiblty(n):
    pair_list=[]
    for i in range(len(n)):
        for j in range(i):
            #print(n[:i],n[i+1:])
            print(n[i],n[j])
            pair_list.append(n[i]+n[j])
    print(pair_list)        
    
    
check_divisiblty([2,2,1,7,5])