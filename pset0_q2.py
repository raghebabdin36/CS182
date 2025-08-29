from itertools import permutations

def check_constraints(arrangement):
    # Find the index positions of each employee for convenience
    aaron_idx = arrangement.index("Aaron")
    bella_idx = arrangement.index("Bella")
    chris_idx = arrangement.index("Chris")
    diana_idx = arrangement.index("Diana")
    ethan_idx = arrangement.index("Ethan")
    farah_idx = arrangement.index("Farah")
    george_idx = arrangement.index("George")
    hazel_idx = arrangement.index("Hazel")
    
    # Constraint 1: Aaron and Bella want at most one workstation between them
    if abs(aaron_idx - bella_idx) > 1:
        return False

    # Constraint 2: Chris and Diana prefer exactly one workstation separating them
    if abs(chris_idx - diana_idx) != 2:
        return False

    # Constraint 3: Ethan and Farah want at least three workstations apart
    if abs(ethan_idx - farah_idx) < 3:
        return False

    # Constraint 4: George and Hazel should not be adjacent
    if abs(george_idx - hazel_idx) == 1:
        return False

    return True

def find_valid_arrangements(employees):
    valid_arrangements = []
    
    for arrangement in permutations(employees):

        if check_constraints(arrangement):
            valid_arrangements.append(arrangement)
    
    return valid_arrangements

employees = ["Aaron", "Bella", "Chris", "Diana", "Ethan", "Farah", "George", "Hazel"]

valid_arrangements = find_valid_arrangements(employees)

print("Valid workstation arrangements:")
for arrangement in valid_arrangements:
    print(arrangement)
print("Total arrangements:", len(valid_arrangements))
