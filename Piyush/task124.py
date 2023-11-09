original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Specify the desired length
desired_length = 5

# Calculate the resizing factor
resize_factor = len(original_list) / desired_length

# Create the resized list by rounding and selecting elements
resized_list = [original_list[int(round(i * resize_factor))] for i in range(desired_length)]

print(resized_list)
#end of task124
