import random
import time
from tqdm import tqdm

def monte_carlo_pi(total_iterations):
    inside_circle = 0

    for _ in tqdm(range(total_iterations), desc="Progress"):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / total_iterations) * 4
    return pi_estimate

# Parameters
total_iterations = 10**8

start_time = time.time()
pi_estimate = monte_carlo_pi(total_iterations)
end_time = time.time()

total_time = end_time - start_time

print(f"Estimated value of π: {pi_estimate}")
print(f"Time taken: {total_time} seconds")
