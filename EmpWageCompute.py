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
       This function checks the attendance of an employee.
    Parameters:
       attended: A parameter that indicates if the employee is present (1) or absent (0).
    Returns:
        Prints whether the employee is present or absent.
    """
    
    if attended == 1:
        print("Employee is present!!!")
    else:
        print("Employee is absent!!!")

def Emp_Daily_Wage(wage_per_hour, no_of_hour):
    """
    Description:
       This function calculates the daily wage of an employee.
    Parameters:
       wage_per_hour: The wage rate per hour.
       no_of_hour: The number of hours worked.
    Returns:
        Prints the total earnings of the employee.
    """
    
    total_earning = wage_per_hour * no_of_hour
    print(f"Daily wage that an employee will earn: {total_earning} rupees")

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
    # Check attendance
    attended = random.randint(0, 1)
    check_attendance(attended)

    # Calculate daily wage
    wage_per_hour = 20
    no_of_hour = 8
    Emp_Daily_Wage(wage_per_hour, no_of_hour)

    # Calculate parttime wage
    no_of_hours = 4
    per_hour_wage = 18
    parttime_emp_wage(no_of_hours, per_hour_wage )
    
if __name__ == "__main__":
    main()
