def set_operations(set1, set2):
    # Set Union
    union_set = set1.union(set2)
    
    # Set Intersection
    intersection_set = set1.intersection(set2)
    
    # Set Difference (set1 - set2)
    difference_set1 = set1.difference(set2)
    
    # Set Difference (set2 - set1)
    difference_set2 = set2.difference(set1)
    
    return union_set, intersection_set, difference_set1, difference_set2

def main():
    # Example sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    # Perform set operations
    union_set, intersection_set, difference_set1, difference_set2 = set_operations(set1, set2)
    
    # Print results
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {union_set}")
    print(f"Intersection: {intersection_set}")
    print(f"Difference (Set 1 - Set 2): {difference_set1}")
    print(f"Difference (Set 2 - Set 1): {difference_set2}")

if __name__ == "__main__":
    main()
