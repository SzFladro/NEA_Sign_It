import time
import random
import string

def wikisort(arr):
    def insertion_sort(arr, start, end):
        for i in range(start + 1, end + 1):
            j = i
            while j > start and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def merge(arr, start, mid, end, buffer):
        buffer_size = end - start + 1
        i, j, k = start, mid + 1, 0

        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                buffer[k] = arr[i]
                i += 1
            else:
                buffer[k] = arr[j]
                j += 1
            k += 1

        while i <= mid:
            buffer[k] = arr[i]
            i += 1
            k += 1

        while j <= end:
            buffer[k] = arr[j]
            j += 1
            k += 1

        for i in range(k):
            arr[start + i] = buffer[i]

    def wikisort_internal(arr, start, end, buffer):
        if end - start < 12:
            insertion_sort(arr, start, end)
            return

        # Adaptive block size
        block_size = int(pow(end - start + 1, 0.33))
        buffer_start = end - block_size + 1

        while buffer_start >= start:
            insertion_sort(arr, buffer_start, end)
            mid = buffer_start + block_size - 1
            reverse(arr, buffer_start, mid)
            merge(arr, start, mid, end, buffer)
            buffer_start -= block_size

        wikisort_internal(arr, start, start + block_size - 1, buffer)

        i = start
        while i <= end:
            j = i
            while j + block_size <= end and arr[j] > arr[j + block_size]:
                arr[j], arr[j + block_size] = arr[j + block_size], arr[j]
                j += 1

            i += 1

        i = end
        while i >= start + block_size:
            wikisort_internal(arr, i - block_size + 1, i, buffer)
            merge(arr, i - block_size + 1, i, i, buffer)
            i -= block_size

    def recursive_sort(arr, buffer):
        wikisort_internal(arr, 0, len(arr) - 1, buffer)

    n = len(arr)
    buffer_size = n
    buffer = [0] * buffer_size

    # Best case: Already sorted array
    best_case_arr = arr.copy()
    start_time_best = time.time()
    recursive_sort(best_case_arr, buffer)
    end_time_best = time.time()
    time_best = end_time_best - start_time_best

    # Worst case: Reversed array
    worst_case_arr = arr[::-1]
    start_time_worst = time.time()
    recursive_sort(worst_case_arr, buffer)
    end_time_worst = time.time()
    time_worst = end_time_worst - start_time_worst

    # Average case: Randomized array
    random_case_arr = arr.copy()
    random.shuffle(random_case_arr)
    start_time_avg = time.time()
    recursive_sort(random_case_arr, buffer)
    end_time_avg = time.time()
    time_avg = end_time_avg - start_time_avg

    print(f"Best Case Time: {time_best:.30f} seconds")
    print(f"Worst Case Time: {time_worst:.30f} seconds")
    print(f"Average Case Time: {time_avg:.30f} seconds")
    print(best_case_arr)
    print(f"Space Complexity: {buffer_size * 8 / (1024 * 1024):.2f} MB") 

string_arr_size = 2000
max_string_length = 20
random_string_array = [''.join(random.choices(string.ascii_lowercase, k=random.randint(1, max_string_length))) for _ in range(string_arr_size)]
wikisort_string_array = random_string_array.copy()
wikisort(wikisort_string_array)
