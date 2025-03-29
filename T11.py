import time

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
start_time = time.time()
sorted_data = sorted(data, reverse=True)
print(sorted_data)
print(f"Time taken: {time.time() - start_time} seconds")