import random
random.seed()
num_test_cases = 1000
print(num_test_cases)
for test_case_idx in range(num_test_cases):
    list_length = random.randint(10, 100)
    test_case_list = []
    for list_elem_idx in range(list_length):
        test_case_list.append(random.randint(10, 100))
    test_case_list = sorted(test_case_list)
    for list_elem_idx in range(list_length):
        print(test_case_list[list_elem_idx], end=' ')
    item_to_search = random.randint(10, 100)
    edge_case = random.randint(0, 10)
    if (edge_case == 0):
        item_to_search = 5
    elif edge_case == 1:
        item_to_search = 105
    else:
        pass
    print('')
    print(item_to_search)