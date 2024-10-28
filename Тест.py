

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    result = 0
    result1 = 0
    for arg in args:
        # print(arg)
        if type(arg) == int:
            result += arg
        elif type(arg) == str:
            result1 += len(arg)
        elif type(arg) == list or type(arg) == tuple or type(arg) == set:
            calculate_structure_sum(*arg)
        elif type(arg) == dict:

            calculate_structure_sum(*arg)
        print(arg)
    return result + result1





print(calculate_structure_sum(data_structure))
