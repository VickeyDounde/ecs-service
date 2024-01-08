import psutil

# Get a list of all running processes
processes = psutil.process_iter()
for process in processes:
    print(process)

# Get information about a specific process by its process ID (PID)
pid = 1100
process = psutil.Process(pid)
print(f"Process Name: {process.name()}")
print(f"CPU Usage: {process.cpu_percent(interval=1)}%")
print(f"Memory Usage: {process.memory_info().rss / (1024 * 1024):.2f} MB")
