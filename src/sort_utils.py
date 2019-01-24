"""

 sort_utils.py  (author: Anson Wong / github: ankonzoid)

"""
import numpy as np

"""
 Finds the first unique k elements (based on lowest distance) of lists 'indices' and 'distances'
"""
def find_topk_unique(indices, distances, k):

    # Sort by ascending distance
    i_sort_1 = np.argsort(distances)
    distances_sorted = distances[i_sort_1]
    indices_sorted = indices[i_sort_1]

    window = np.array(indices_sorted[:k], dtype=int)  # collect first k elements for window intialization
    window_unique, j_window_unique = np.unique(window, return_index=True)  # find unique window values and indices
    j = k  # track add index when there are not enough unique values in the window
    # Run while loop until window_unique has k elements
    while len(window_unique) != k:
        # Append new index and value to the window
        j_window_unique = np.append(j_window_unique, [j])  # append new index
        window = np.append(window_unique, [indices_sorted[j]])  # append new value
        # Update the new unique window
        window_unique, j_window_unique_temp = np.unique(window, return_index=True)
        j_window_unique = j_window_unique[j_window_unique_temp]
        # Update add index
        j += 1

    # Sort the j_window_unique (not sorted) by distances and get corresponding
    # top-k unique indices and distances (based on smallest distances)
    distances_sorted_window = distances_sorted[j_window_unique]
    indices_sorted_window = indices_sorted[j_window_unique]
    u_sort = np.argsort(distances_sorted_window)  # sort

    distances_top_k_unique = distances_sorted_window[u_sort].reshape((1, -1))
    indices_top_k_unique = indices_sorted_window[u_sort].reshape((1, -1))

    return indices_top_k_unique, distances_top_k_unique

"""
 Checks if a list has unique elements
"""
def is_unique(vec):
    n_vec = len(vec)
    n_vec_unique = len(np.unique(vec))
    return (n_vec == n_vec_unique)


# Main driver
if __name__ == "main":
    main()