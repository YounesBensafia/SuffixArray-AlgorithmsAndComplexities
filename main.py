import heapq
import tracking_usage as tu
import random
import string

def suffix_array_construction(text):
    suffixes = [text[i:] for i in range(len(text))]
    return suffixes

def quicksort_suffixes(suffixes):
    if len(suffixes) <= 1:
        return suffixes
    pivot = suffixes[len(suffixes) // 2]
    left = [x for x in suffixes if x < pivot]
    middle = [x for x in suffixes if x == pivot]
    right = [x for x in suffixes if x > pivot]
    return quicksort_suffixes(left) + middle + quicksort_suffixes(right)

def heapsort_suffixes(suffixes):
    heapq.heapify(suffixes)
    return [heapq.heappop(suffixes) for _ in range(len(suffixes))]

def mergesort_suffixes(suffixes):
    if len(suffixes) <= 1:
        return suffixes
    mid = len(suffixes) // 2
    left = mergesort_suffixes(suffixes[:mid])
    right = mergesort_suffixes(suffixes[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def bucketsort_suffixes(suffixes):
    max_len = max(len(suffix) for suffix, _ in suffixes)
    buckets = [[] for _ in range(256)]
    for i in range(max_len - 1, -1, -1):
        for suffix, index in suffixes:
            key = ord(suffix[i]) if i < len(suffix) else 0
            buckets[key].append((suffix, index))
        suffixes = [suffix for bucket in buckets for suffix in bucket]
        buckets = [[] for _ in range(256)]
    return suffixes

def main_sorting():
    text = "Pneumonoultramicroscopicsilicovolcanoconiosis"
    suffixes = suffix_array_construction(text)
    print("\nBucket Sort:")
    print(f"{tu.track_time(lambda: bucketsort_suffixes(suffixes.copy())):.6f}")
    
    print("\nQuick Sort:")
    print(f"{tu.track_time(lambda: quicksort_suffixes(suffixes.copy())):.6f}")
    
    print("\nHeap Sort:")
    print(f"{tu.track_time(lambda: heapsort_suffixes(suffixes.copy())):.6f}")
    
    print("\nMerge Sort:")
    print(f"{tu.track_time(lambda: mergesort_suffixes(suffixes.copy())):.6f}")

# DANS PIRE DES CAS:
# MERGE O(n*log(n))> HEAP O(n*log(n)) > BUCKET O(n2)> QUICK O(n2)


# ================================================================

def binary_search_suffix_array(suffixes, pattern):
    left, right = 0, len(suffixes) - 1
    while left <= right:
        mid = (left + right) // 2
        suffix = suffixes[mid]
        if suffix.startswith(pattern):
            return 0
        elif suffix < pattern:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main_search():
    time = 0
    with open("./complexity.csv", "w") as a:
        a.write("num,time\n")
        for i in range(1,10000):
            c = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 20)))

            patterns = [''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5))) for _ in range(10)]

            pattern = random.choice(patterns)
            suffixes = quicksort_suffixes(suffix_array_construction(c))
            time_up = time
            time = tu.track_time(lambda: binary_search_suffix_array(suffixes, pattern))
            if time > time_up:
                a.write(f"{i},{time:.6f}\n")

if __name__ == "__main__":
    main_search()