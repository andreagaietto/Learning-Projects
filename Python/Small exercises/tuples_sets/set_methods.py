s = set({1, 2, 3, 4})
print(s)
s.add(5)
print(s)
s.remove(5)
print(s)
#discard will not give an error if the value doesnt exist
s.discard(5)
print(s)
duplicate = s.copy()
print(duplicate)


math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_student = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

print(math_students | biology_student)

print(math_students & biology_student)