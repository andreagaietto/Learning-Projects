l = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, l))
# evens = [2, 4]

names = ['austin', 'penny', 'anthony', 'billy']
a_names = filter(lambda n: n[0]=='a', names)


names = ['Lassie', 'Andi', 'Rusty']
list(map(lambda name: f"Your instructior is {name}", filter(lambda value: len(value) < 5, names)))
# Your instructor is andi


# can often be done using list comp



def remove_negatives(number_list):
    negatives_removed = list(filter(lambda value: value >= 0, number_list))
    return negatives_removed


remove_negatives([-1, 3, 4, -99])