
""" 

    @Author: Likhitha S
    @Date: 03-10-2024 12:20
    @Last Modified by: Likhitha S
    @Last Modified time: 03-10-2024 12:20
    @Title: Write a Python program to Add Part time Employee & Wage - Assume Part time Hour is 8.
    
"""

import random

def parttime_emp_wage(no_of_hours, per_hour_wage ):
    """
        
        Description: 
           This function is used to calculate the part time wage of an employees.
        Parameters:
           no_of_hours, per_hour_wage is a parameter that used to check the condition
        Return:
            It prints the output according to the calculation . 
        
    """
    
    total_wages=no_of_hours*per_hour_wage
    print(f"parttime wage do employee get for his/her work will be: {total_wages} rupees")
    
    
def main():

    no_of_hours = 4
    per_hour_wage = 18
    parttime_emp_wage(no_of_hours, per_hour_wage )
    
if __name__=="__main__":
    main()
