def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
dataset1 = [{"geneZ":'ATG', "int":3}, {"geneHOX114":'ATGCC', "int":12}]
dataset2 = [{"geneBRCA1":'AAACCC', "int":85}]
resultnumb1 = [1, 2, 3, 4, 5]
d = [[1, dataset1, dataset2, resultnumb1, 2], [[[3]], 'home2'], 4, 5]
flattened_list = flatten(d)

print(flattened_list)
def reverse_nested_list(lst):
    reversed_list = []
    
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_list.append(reverse_nested_list(item)) 
        else:
            reversed_list.append(item)
    
    return reversed_list

dataset1 = [{"geneZ":'ATG', "int":3}, {"geneHOX114":'ATGCC', "int":12}]
dataset2 = [{"geneBRCA1":'AAACCC', "int":85}]
resultnumb1 = [1, 2, 3, 4, 5]
d = [[1, dataset1, dataset2, resultnumb1, 2], [[[3]], 'home2'], 4, 5]

reversed_d = reverse_nested_list(d)

print(reversed_d)