
""" 

    @Author: Likhitha S
    @Date: 03-10-2024 12:20
    @Last Modified by: Likhitha S
    @Last Modified time: 03-10-2024 12:20
    @Title: Write a Python program to Add Part time Employee & Wage - Assume Part time Hour is 8.
    
"""

import random

def monthly_emp_wage(daily_wages, working_days ):
    """
        
        Description: 
           This function is used to calculate the part time wage of an employees.
        Parameters:
           no_of_hours, per_hour_wage is a parameter that used to check the condition
        Return:
            It prints the output according to the calculation . 
        
    """
    
    total_wages=daily_wages* working_days
    print(f"total wage do employee get for his/her work will be: {total_wages} rupees")
    
    
def main():

    working_days = 20
    daily_wages = 160
    monthly_emp_wage(daily_wages, working_days )
    
if __name__=="__main__":
    main()