#makes an iterator that aggregated elements from each of the iterables. returns an iterator of tuples, where the ith tuple contains the ith element from each of the argument sequences or iterables. iterator stops when the shortest input iterable is exhausted


first_zip = zip([1,2,3], [4,5,6])
#print(list(first_zip))
print(dict(first_zip))

five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
print(list(zip(*five_by_two)))

# the * as above works to help unpack items

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# final_grades = {'dan': 98, 'ang': 91, 'kate': 78}

combined = list(zip(midterms, finals))
max_scores = [max(x) for x in combined]
final_grades = {students[x]: max_scores[x] for x in range(len(students))}
print(final_grades)

#or
final_grades = {pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}
print(final_grades)

#or
final_grades = zip(
    students,
    map(
    lambda pair: max(pair),
    zip(midterms, finals)
    )
)
print(dict(final_grades))
#can also add the dict() above