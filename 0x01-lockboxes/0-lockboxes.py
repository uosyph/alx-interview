#!/usr/bin/python3


def canUnlockAll(boxes):
    visited_boxes = set()
    keys = [0]

    while keys:
        current_key = keys.pop()
        visited_boxes.add(current_key)

        for box_key in boxes[current_key]:
            if box_key not in visited_boxes and 0 <= box_key < len(boxes):
                keys.append(box_key)

    return len(visited_boxes) == len(boxes)
