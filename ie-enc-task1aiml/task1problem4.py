def calculate_avg(num_list):
    if len(num_list) == 0:
        return "Error"
    return sum(num_list)/len(num_list)

numbers = [4, 7, 9, 2, 5]
avg = calculate_avg(numbers)
print("average:", avg)
