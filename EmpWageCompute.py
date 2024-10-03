""" 

    @Author: Likhitha S
    @Date: 03-10-2024 12:20
    @Last Modified by: Likhitha S
    @Last Modified time: 03-10-2024 12:20
    @Title: Write a Python program to Check Employee is Present or Absent - Use ((RANDOM)) for Attendance Check

"""

import random

def check_attendance(attended):
    """
        
        Description: 
           This function is used to check attendance of an employees.
        Parameters:
           attended is a parameter that used to check the condition
        Return:
            It prints the output according to the calculation . 
        
    """
    
    if attended==1:
        print("Employee is present!!!")
    else:
        print("Employee is absent!!!")
    
    
def main():

    attended=random.randint(0,1)
    check_attendance(attended)
    
if __name__=="__main__":
    main()