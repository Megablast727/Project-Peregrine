import numpy as np
import time
from tqdm import tqdm

def monte_carlo_pi_chunk(iterations):
    x = np.random.uniform(-1, 1, iterations)
    y = np.random.uniform(-1, 1, iterations)
    inside_circle = np.sum(x**2 + y**2 <= 1)
    return inside_circle

def monte_carlo_pi(total_iterations, chunk_size):
    total_inside_circle = 0
    chunks = total_iterations // chunk_size

    for _ in tqdm(range(chunks), desc="Progress"):
        total_inside_circle += monte_carlo_pi_chunk(chunk_size)

    pi_estimate = (total_inside_circle / total_iterations) * 4
    return pi_estimate

# Parameters
total_iterations = 10**8
chunk_size = 10**6  # Adjust the chunk size as needed

start_time = time.time()
pi_estimate = monte_carlo_pi(total_iterations, chunk_size)
end_time = time.time()

total_time = end_time - start_time

print(f"Estimated value of π: {pi_estimate}")
print(f"Time taken: {total_time:.2f} seconds")
