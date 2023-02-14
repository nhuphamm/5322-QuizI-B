"""
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
"""

import csv


# open the file
filename = "employee_data.csv"
employee_dict = {}

with open(filename, "r") as file:
    csv_reader = csv.DictReader(file, delimiter=",")

    # create an empty dictionary
    # emp_sal = {}
    sal_increase = 0
    total = 0
    # use a loop to iterate through the csv file
    for emp in csv_reader:
        # check if the employee fits the search criteria
        if emp["Clearance"] == "TS":
            name = emp["First Name"] + " " + emp["Last Name"]
            old_salary = int(emp["Salary"])
            new_salary = int(old_salary * 1.1)
            employee_dict[name] = new_salary
            print(f"Employee Name: {name} Current Salary: ${old_salary:.2f}")
            print(f"Employee Name: {name} New Salary: ${new_salary:.2f}")


total_difference = sum(
    [new_salary - int(emp["Salary"]) for name, new_salary in employee_dict.items()]
)


print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per image
# for key, values in employee_dict.items:
#     print(f"")

print()
print("=========================================")
print()

# print out the total difference between the old salary and the new salary as per image.
print(f"Total difference in salary: ${total_difference:.2f}")
