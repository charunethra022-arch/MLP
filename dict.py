student = {
    "Name": "Surya",
    "Age": 20,
    "Course": "AIML"
}

print("Original:", student)

student["City"] = "Coimbatore"
print("After Adding:", student)

student["Age"] = 21
print("After Updating:", student)

del student["Course"]
print("After Deleting:", student)

print("Keys:", student.keys())
print("Values:", student.values())