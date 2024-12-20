import heapq
import tracking_usage as tu

def suffix_array_construction(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
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

def main():
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

if __name__ == "__main__":
    main()