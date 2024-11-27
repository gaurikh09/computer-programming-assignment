# display according to thier frequency
def group_by_frequency(tpl):
    freq = defaultdict(list)
    for item in set(tpl):
        freq[tpl.count(item)].append(item)
    return dict(freq)

# Example
print(group_by_frequency((1, 2, 2, 3, 4, 4, 4)))  # Output: {1: [1, 3], 2: [2], 3: [4]}
