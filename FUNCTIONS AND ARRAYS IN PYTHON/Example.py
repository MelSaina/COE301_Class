# Example of thee addition function
import math
import numpy as  np
def main():
    def add():
        x = int(input("Enter yor value of x: "))
        y = int(input("Enter yor value of y: "))
        sum = x + y
        print ("Your sum for ", + x ,"and ", + y , "is: ", sum)
        
    def user_defined():
        list = [1,2,3,3,3,5,5,76,34,56]
        minimum =np.min(list)
        print(minimum)
    add()
    user_defined()

main()