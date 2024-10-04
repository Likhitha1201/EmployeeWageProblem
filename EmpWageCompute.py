
""" 

    @Author: Likhitha S
    @Date: 03-10-2024 17:20
    @Last Modified by: Likhitha S
    @Last Modified time: 04-10-2024 13:10
    @Title: Write a Python program to Add Part time Employee & Wage - Assume Part time Hour is 8.
    
"""

import random

class Employee:
    # static variables -> per_day_hour and amt_perhour
    per_day_hour=8
    part_time=4
    amt_perhour=40
    total_hour=50
    total_parttime_hour=28
    
    def welcome(self):
        """
        
        Description: 
           This function is used welcome the user.
        Return:
            It prints the welcome message. 
        
        """
        
        print("Welcome to Employee Wage Program...!!")
        
    def attendance(self):
        """
        
        Description: 
           This function is used to check attendance of all employees.
        Parameters:
           attend is container used to strore the random values.
        Return:
            It returns wheather employees present or not. 
        
        """
        
        attend=random.randint(0,2)
        return attend
        

    def compute_daily_wage(self):
        """
        
        Description: 
           This function is used to calculate the dialy wages of an employee.
        Parameters:
           amt_per_day is container used to strore the daily wages of an employee.
        Return:
            It returns the daily wages of an employees. 
        
        """
        
        amt_per_day=self.per_day_hour*self.amt_perhour
        return amt_per_day
  
  
    def compute_part_time(self):
        """
        
        Description: 
           This function is used to calculate the parttime wages of an employee.
        Parameters:
           amt_per_day is container used to strore the parttime wages of an employee.
        Return:
            It returns the parttime wages of an employees. 
        
        """
        
        amt_parttime=self.part_time*self.amt_perhour
        return amt_parttime
    
    def compute_monthly_wages(self):
        """
        
        Description: 
           This function is used to calculate the monthly wages along with the attendance datails of all employee.
        Parameters:
           attend_list, wages, attend, total_wage is container used to strore the attendance details and monthly wages in a two different list's, attend is storing the called method, and total wages is used to strore overall salary of all the employees.
        Return:
            It prints the attend_list and wages of all employees, and returns returns the overall wages of all employees. 
        
        """
        
        
        attend_list=[]
        wages=[]
        attend =self.attendance()
        total_wage=0
        
        for i in range(0,30):
            
            if attend==0:
                attend_list.append('Abs')
                wages.append(000)
                
            elif attend==1:
                daily_wage=self.compute_daily_wage()
                monthly_sal= self.total_hour*daily_wage
                total_wage=total_wage+monthly_sal
                attend_list.append('Pres')
                wages.append(monthly_sal)
                
            else:
                parttime_wage=self.compute_daily_wage()
                monthly_sal= self.total_parttime_hour*parttime_wage
                total_wage=total_wage+monthly_sal
                attend_list.append('PartTime')
                wages.append(monthly_sal)
        print(f"Attendance list of the month(for 30 days): {attend_list}")
        print(f"Monthly wages of all employees: {wages}")
        return total_wage
    

def main():
    e1=Employee()
    e1.welcome()
                
    total_sal=e1.compute_monthly_wages()
    print(f"total salary of all employee's will be: {total_sal}")
        
if __name__=="__main__":
    main()