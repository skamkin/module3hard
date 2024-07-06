data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
  "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    sum_all = 0
    for item in data_structure:
        if isinstance(item, list | tuple | set):
          sum_all += calculate_structure_sum(item)
        if isinstance(item, dict):
          for i in item:
            sum_all += len(i)
          sum_all += sum(item.values())
        if isinstance(item, int):
          sum_all += item
        if isinstance(item, str):
          sum_all += len(item)

    return sum_all



result = calculate_structure_sum(data_structure)
print(result)