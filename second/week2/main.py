
"""You successfully wrote a Python script that achieves two tasks.  
First, it reads a CSV file containing a list of the employees in the organization. 
Second, it generates a report of the number of people in each department in a plain text file.
Creating reports using Python is a very useful tool in IT support. 
You will likely complete similar tasks regularly throughout your career, so feel free to go through this lab more than once. Remember, practice makes perfect."""

import csv
def read_employees(csv_file_location):
    employe_list = []
    with open(csv_file_location) as file:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employe_file = csv.DictReader(file, dialect='empDialect')
        for data in employe_file:
            employe_list.append(data)
    return employe_list

employee_list = read_employees('employees.csv')
print(employee_list)

def process_data(employe_list):
    department_list = []
    for employee_data in employe_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)
print(dictionary)

def write_report(obj, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(obj):
            f.write(str(k)+':'+str(obj[k])+'\n')
    f.close()

write_report(dictionary, 'report.txt')
