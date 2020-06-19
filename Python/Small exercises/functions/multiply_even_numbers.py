
def multiply_even_numbers(test_list):
    even_list = []
    final_product = 1
    [[even_list.append(x)] for x in test_list if x % 2 == 0]
    for x in even_list:
        final_product *= x
    print(final_product)

multiply_even_numbers([2, 3, 4, 5, 6])


