import os

students = []
courses = []

opt_str = """
Options:
1. Add student
2. Add course
3. Add marks
4. Print information
5. Clear screen
0. Exit
"""

def print_func():
	print("Student information")
	for st in students:
		print(f"Student name: {st['st_name']}")
		print(f"Student ID: {st['st_id']}")

	print("Courses information:")
	for c in courses:
		print(f"Course name: {c['c_name']}")
		print(f"Course ID: {c['c_id']}")
		if "students" in c:
			print("Mark:")
			for st_id, mark in c["students"].items():
				print(f"Student ID: {st_id}, Mark: {mark}")

if __name__ == "__main__":
	opt = 0
	while True:
		opt = int(input(opt_str))
		if opt not in [0, 1, 2, 3, 4, 5]:
			print("Wrong option")
			continue

		if opt == 0:
			print("Exit")
			break
		elif opt == 1:
			st = {}
			st["st_name"] = input("Enter student name: ")
			st["st_id"] = input("Enter student ID: ")
			students.append(st)
		elif opt == 2:
			c = {}
			c["c_name"] = input("Enter course name: ")
			c["c_id"] = input("Enter course ID: ")
			courses.append(c)
		elif opt == 3:
			c_id = input("Enter course ID: ")

			for course in courses:
				if course["c_id"] == c_id:
					st_id = input("Enter student ID: ")
					mark = input("Enter mark: ")
					if "students" not in course:
						course["students"] = {}
					course["students"][st_id] = mark
					print("Mark added!")
					break
			else:
				print("Course not found!")
		elif opt == 4:
			print_func()
		elif opt == 5:
			os.system("clear")
		else:
			print("Invalid option!") 
