import random

# Function to compute f(x)
def f(x):
    return -(x ** 2) + 10

# Hill Climbing algorithm
def hill_climbing():
    # Initialize current state randomly within the range [-10, 10]
    current_state = random.uniform(-10, 10)
    max_value = f(current_state)
    
    # Set step size for perturbation
    step_size = 0.1
    
    # Number of iterations
    iterations = 1000
    
    for _ in range(iterations):
        # Generate a neighbor by perturbing the current state
        neighbor = current_state + random.uniform(-step_size, step_size)
        
        # If the neighbor is within the valid range [-10, 10], compute the value of f(x)
        if -10 <= neighbor <= 10:
            neighbor_value = f(neighbor)
            
            # If the value of f(x) at the neighbor is greater than the current maximum, update the maximum
            if neighbor_value > max_value:
                max_value = neighbor_value
                current_state = neighbor
    
    return max_value

# Main function
if __name__ == "__main__":
    max_value = hill_climbing()
    print("Maximum value of f(x) found using Hill Climbing method:", max_value)
