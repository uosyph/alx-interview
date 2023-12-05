#!/usr/bin/python3
"""
Module: unlock_boxes

This module provides a function for determining whether it is possible
to unlock all boxes in a given list of boxes. The primary function,
'canUnlockAll', uses a depth-first search approach to explore
the connectivity between boxes, checking if all boxes can be visited
starting from the first box (index 0).

Functions:
    canUnlockAll(boxes): Determines if all boxes in the given list
    can be unlocked.

Example Usage:
    from 0-lockboxes import canUnlockAll

    boxes = [[1, 2], [3], [], [4], []]
    result = canUnlockAll(boxes)
    print(result)  # Output: True
"""


def canUnlockAll(boxes):
    """
    Determines whether it is possible to unlock
    all boxes in a given list of boxes.

    Args:
        boxes (list of lists): A list of boxes, where each box
        is represented as a list containing indices of other boxes
        that can be unlocked with keys.

    Returns:
        bool: True if it is possible to unlock all boxes, False otherwise.

    The function uses a depth-first search approach to explore
    the connectivity between boxes and checks if all boxes
    can be visited starting from the first box (index 0).
    """

    visited_boxes = set()
    keys = [0]

    while keys:
        current_key = keys.pop()
        visited_boxes.add(current_key)

        for box_key in boxes[current_key]:
            if box_key not in visited_boxes and 0 <= box_key < len(boxes):
                keys.append(box_key)

    return len(visited_boxes) == len(boxes)
