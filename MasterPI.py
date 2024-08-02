import subprocess
import time
import csv
import pandas as pd

def run_script(script_name, num_runs):
    """Run the script multiple times and return the execution times."""
    times = []
    for _ in range(num_runs):
        start_time = time.time()
        subprocess.run(['python3', script_name], check=True)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def write_results_to_file(filename, results):
    """Write the collected results to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Script', 'Run', 'Time (seconds)'])
        for script, times in results.items():
            for i, time in enumerate(times):
                writer.writerow([script, i + 1, time])

def analyze_results(filename):
    """Analyze the results from the CSV file and print statistics."""
    df = pd.read_csv(filename)
    stats = df.groupby('Script')['Time (seconds)'].agg(['mean', 'std', 'min', 'max'])
    print("Analysis Results:")
    print(stats)

def main():
    scripts = ['PI.py', 'PI2.py', 'PI_numpy.py']  # List of your scripts
    num_runs = 1000
    results = {}

    for script in scripts:
        print(f"Running {script}...")
        times = run_script(script, num_runs)
        results[script] = times

    results_filename = 'results.csv'
    write_results_to_file(results_filename, results)
    print(f"Results saved to {results_filename}")

    # Analyze the results
    analyze_results(results_filename)

if __name__ == "__main__":
    main()
