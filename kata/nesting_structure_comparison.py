"""Complete the function/method (depending on the language) to return true/True
when its argument is an array that has the same nesting structures a
nd same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )"""

def same_structure_as(original: list, other: list) -> bool:
    if not isinstance(original, list) and not isinstance(other, list):
        return original == other
    if len(original) != len(other):
        return False
    for orig_item, other_item in zip(original, other):
        if isinstance(orig_item, list) and isinstance(other_item, list):
            if not same_structure_as(orig_item, other_item):
                return False
        elif not isinstance(orig_item, list) and not isinstance(other_item, list):
            continue
        else:
            return False
    return True