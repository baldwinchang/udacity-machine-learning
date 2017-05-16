from scipy.spatial.distance import euclidean, cityblock
import heapq

# Data points from the quiz, [(x1, x2), y]
data_points = [
    [(1, 6), 7],
    [(2, 4), 8],
    [(3, 7), 16],
    [(6, 8), 44],
    [(7, 1), 50],
    [(8, 4), 68]
]

# The data point we would like to get a prediction from
q = (4, 2)

# K-NN Heaps
euclidean_heap = []
manhattan_heap = []

for dp in data_points:
    point = dp[0]

    # Add to the heap
    heapq.heappush(euclidean_heap, (euclidean(point, q), dp))
    heapq.heappush(manhattan_heap, (cityblock(point, q), dp))


def knn_average(k, heap):
    k_found = 0
    total_sum = 0.
    last_distance = None
    for item in heap:
        distance, dp = item
        x, y = dp

        # If the last distance is the same as this point's distance,
        # we shall entertain it. We also take into consideration all
        # points under our k threshold.
        if last_distance == distance or k_found < k:
            total_sum += y
            k_found += 1
            last_distance = distance
        else:
            break

    return total_sum / k_found

euclidean_heap = heapq.nsmallest(len(euclidean_heap), euclidean_heap)
print("Euclidean K-NN:")
print("1-NN: {}".format(knn_average(1, euclidean_heap)))
print("3-NN: {}".format(knn_average(3, euclidean_heap)))


manhattan_heap = heapq.nsmallest(len(manhattan_heap), manhattan_heap)
print("Manhattan K-NN:")
print("1-NN: {}".format(knn_average(1, manhattan_heap)))
print("3-NN: {}".format(knn_average(3, manhattan_heap)))
