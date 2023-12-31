def compare(a, b, c):
    if a == b == c:
        return "All three values equal"
    elif a == b or b == c or a == c:
        return "Two values equal"
    else:
        return "All three values different"

v1 = 9
v2 = 4
v3 = 9

comparison_result = compare(v1, v2, v3)
print(f"Comparison result: {comparison_result}")
