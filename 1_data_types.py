def string_from_start_end_chars(str_input):

  if len(str_input) < 2:
    return ''

  return str_input[0:2] + str_input[-2:]

str_input = input("Please enter a string \n")
print(string_from_start_end_chars(str_input))