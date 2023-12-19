import random


elements = ['A', 'B', 'C', 'D']
weights = [0.1, 0.3, 0.5, 0.1]  


random_element = random.choices(elements, weights=weights, k=1)[0]

# Display the randomly selected element
print("Randomly selected element based on weighted probabilities:", random_element)
