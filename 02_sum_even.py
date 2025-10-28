# Calculate the sum of all even numbers between 1 to 100 using loop

sum_of_evens = 0 # Initialize the sum

# Start from 2, go up to 101 (exclusive), step by 2
for number in range(2, 101, 2):
    sum_of_evens += number # Add each even number to the sum

print(f"The sum of even numbers from 1 to 100 is: {sum_of_evens}")
