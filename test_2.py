"""
create a list to store 24 numbers (float)
capture user's input 24 times for their grades
each time we capture the user's, we append the number to the list
sort the list ascending, then splice the items before index 13
output we have 13 highest number on the list, we sum them up and divide them by13
output a message to the user
end
"""

"""
create list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

sort the list, then splice out the items before 13
print message to user
"""

grades = []

for i in range(13):
    print(i)
    grades.append(float(input("Enter the grade: ")))

grades.sort()
grades = sum(grades[0:]) / 13
# grades = sum(grades)
# results = grades / 13

print("Average Grade: {0: .0f}%".format(grades))