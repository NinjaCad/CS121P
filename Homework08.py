print('Reading input file "classes.txt"...')
try:
    text = open("./classes.txt", "r")
except FileNotFoundError:
    print("Error: classes.txt does not exist or it can't be opened for input.")
    print("Program exiting now...")

students = {}
with open("./classes.txt", "r") as infile:
    current_class = None
    for line in infile:
        line = line.strip()
        if not line:
            current_class = None
            continue
        if line.endswith(":"):
            current_class = line[:-1].strip()
        else:
            student = line.strip()
            if student not in students:
                students[student] = []
            students[student].append(current_class)
print("Input processed")

print('Writing output file "students.txt"...')
try:
    text = open("./students.txt", "w")
except FileNotFoundError:
    print("Error: classes.txt can't be opened for output.")
    print("Program exiting now...")

with open("./students.txt" , "w") as outfile:
    for student in sorted(students):
        classes_list = " ".join(sorted(students[student]))
        outfile.write(str(student) + ": " + classes_list + "\n")

print("Output processed.")
print("Program exiting now...")