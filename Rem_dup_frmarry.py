def remove_duplicates(arr):
    unique_arr = []
    for num in arr:
        if not unique_arr or num != unique_arr[-1]:
            unique_arr.append(num)
    return unique_arr


input_array = []
while True:
    try:
        num = int(input("Enter a number (or press anything other than a number to stop): "))
        input_array.append(num)
    except ValueError:
        break

output = remove_duplicates(input_array)
print("Output:", output)
