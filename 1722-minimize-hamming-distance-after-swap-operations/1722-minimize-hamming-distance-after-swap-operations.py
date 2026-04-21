from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        """
        Calculate the minimum Hamming distance between source and target arrays
        after performing allowed swaps.
      
        Args:
            source: The source array
            target: The target array to match
            allowedSwaps: List of index pairs that can be swapped
          
        Returns:
            The minimum Hamming distance achievable
        """
      
        def find_root(index: int) -> int:
            """
            Find the root parent of an index using path compression.
          
            Args:
                index: The index to find the root for
              
            Returns:
                The root parent index
            """
            if parent[index] != index:
                # Path compression: directly connect to root
                parent[index] = find_root(parent[index])
            return parent[index]
      
        # Initialize Union-Find structure
        array_length = len(source)
        parent = list(range(array_length))  # Each element is initially its own parent
      
        # Union operation: Connect all swappable indices into groups
        for index_a, index_b in allowedSwaps:
            # Connect the two indices by making them share the same root
            parent[find_root(index_a)] = find_root(index_b)
      
        # Count frequency of values in each connected component for source array
        component_value_counts = defaultdict(Counter)
        for index, value in enumerate(source):
            root = find_root(index)
            component_value_counts[root][value] += 1
      
        # Calculate minimum Hamming distance
        hamming_distance = 0
        for index, value in enumerate(target):
            root = find_root(index)
            # Decrement the count of this value in its component
            component_value_counts[root][value] -= 1
            # If count goes negative, this position contributes to Hamming distance
            if component_value_counts[root][value] < 0:
                hamming_distance += 1
      
        return hamming_distance