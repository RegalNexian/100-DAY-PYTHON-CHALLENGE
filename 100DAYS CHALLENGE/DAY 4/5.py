# Sample nested list
nested_list = [1, [2, 3], [4, [5, 6, [7, 8]]], 9, [10]]

# Flatten the nested list without using a predefined function
flat_list = []

# Iterate through the nested list elements
for element in nested_list:
    if isinstance(element, list):
        # Extend the flat_list with elements from the sublist
        for sub_element in element:
            if isinstance(sub_element, list):
                # Flatten further if the sub_element is a list within the sublist
                for sub_sub_element in sub_element:
                    flat_list.append(sub_sub_element)
            else:
                flat_list.append(sub_element)
    else:
        flat_list.append(element)

# Display the flattened list
print("Original Nested List:", nested_list)
print("Flattened List:", flat_list)
