from collections import defaultdict

def merge_dictionaries(*dicts, strategy='sum'):
    merged = defaultdict(int)

    for d in dicts:
        for key, value in d.items():
            if strategy == 'sum':
                merged[key] += value
            elif strategy == 'max':
                merged[key] = max(merged[key], value)
            elif strategy == 'min':
                merged[key] = min(merged[key], value) if merged[key] else value

    return dict(merged)

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 2, 'c': 3}
dict3 = {'b': 1, 'c': 2}

merged_sum = merge_dictionaries(dict1, dict2, dict3, strategy='sum')
merged_max = merge_dictionaries(dict1, dict2, dict3, strategy='mean')
merged_min = merge_dictionaries(dict1, dict2, dict3, strategy='min')

print("Merged with sum:", merged_sum)
print("Merged with max:", merged_max)
print("Merged with min:", merged_min)
