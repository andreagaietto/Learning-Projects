def triple_and_filter(number_list):
    return [x*3 for x in number_list if x%4 == 0]


triple_and_filter([6, 8, 10, 12])