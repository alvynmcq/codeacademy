import math
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(grades, average):
	for grade in grades:
		variance = 0
		avg = average - grade
		avgsq = avg ** 2
		variance += avgsq
		return variance/len(grades)
		
def grades_std_deviation(variance):
	deviation = math.sqrt(variance)
	return deviation

total = grades_sum(grades)
average = grades_average(grades)
variance = grades_variance(grades, average)
deviation = grades_std_deviation(variance)

print_grades(grades)
print total 
print average
print variance