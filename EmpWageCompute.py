""" 

    @Author: Likhitha S
    @Date: 03-10-2024 12:20
    @Last Modified by: Likhitha S
    @Last Modified time: 03-10-2024 12:20
    @Title: Write a Python program to Check Employee is Present or Absent - Use ((RANDOM)) for Attendance Check

"""


def Emp_Daily_Wage(wage_per_hour, no_of_hour):
    """
        
        Description: 
           This function is used to check attendance of an employees.
        Parameters:
           attended is a parameter that used to check the condition
        Return:
            It prints the output according to the calculation . 
        
    """
    
    total_earning=wage_per_hour*no_of_hour
    print(f"daily wage that an employee will earn: {total_earning} rupees")
    
def main():

    wage_per_hour=20
    no_of_hour=8
    Emp_Daily_Wage(wage_per_hour, no_of_hour)
    
if __name__=="__main__":
    main()