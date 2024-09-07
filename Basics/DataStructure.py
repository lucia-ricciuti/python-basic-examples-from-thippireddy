students={"John": ["Python", "Django", "DRF"], "Bob": ["Java", "Spring"], "Jim": ["Js", "Node", "React"]}

print(type(students))
studentNames = students.keys()
for name in studentNames:
    print("Courses taken by", name, "are: ")
    for course in students[name]:
        print(course)