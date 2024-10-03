
""" 

    @Author: Likhitha S
    @Date: 03-10-2024 15:20
    @Last Modified by: Likhitha S
    @Last Modified time: 03-10-2024 15:20
    @Title: Write a Python program to Add Part time Employee & Wage - Assume Part time Hour is 8.
    
"""

import random

def wages_of_an_hour(no_of_hours, per_hour_wage ):
    """
        
        Description: 
           This function is used to calculate the wages based on hours of an employees.
        Parameters:
           no_of_hours, per_hour_wage is a parameter that used to check the condition
        Return:
            It prints the output according to the calculation . 
        
    """
    
    total_wages=no_of_hours*per_hour_wage
    print(f"parttime wage do employee get for his/her work will be: {total_wages} rupees")
    
def wages_of_days(no_of_days,wage_per_day):
    """
        
        Description: 
           This function is used to calculate the wages based on dayspof an employees.
        Parameters:
           no_of_days,wage_per_day is a parameter that used to check the condition
        Return:
            It prints the output according to the calculation . 
        
    """
    
    total_wages=no_of_days*wage_per_day
    print(f"parttime wage do employee get for his/her work will be: {total_wages} rupees")
    
def main():

    no_of_hours = 100
    per_hour_wage = 20
    no_of_days=20
    wage_per_day=160
    
    wages_of_an_hour(no_of_hours, per_hour_wage )
    wages_of_days(no_of_days,wage_per_day)
    
if __name__=="__main__":
    main()