def switch_case(argument):
    switcher = {
        1: "Case 1",
        2: "Case 2",
        3: "Case 3",
    }
    return switcher.get(argument, "Invalid Case")

# Contoh pemanggilan fungsi
print(switch_case(1))  # Output: Case 1
print(switch_case(4))  # Output: Invalid Case
