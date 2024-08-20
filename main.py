grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_score = {}

for ind, val in enumerate(students):
    average_mark = sum(grades[ind]) / len(grades[ind])
    average_score.update({val: average_mark})
print(average_score)
