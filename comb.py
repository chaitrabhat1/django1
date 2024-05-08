from itertools import permutations

def get_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Example usage:
string_to_permute = "eat"
perms = get_permutations(string_to_permute)
for perm in perms:
    print(perm)
