def largest_number(list_input):
    largest_number = list_input[0]

    for list_element in list_input:
        if list_element > largest_number:
            largest_number = list_element

    return largest_number
    
list_input = []
list_size = int(input("Please enter list size = "))
print("Please enter list elements")

for i in range(0,list_size):
    input_element = int(input(f"Please enter list element {i}: "))
    list_input.append(input_element)

print("Largest number = ",largest_number(list_input))
