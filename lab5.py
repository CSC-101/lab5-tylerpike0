import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
from data import Time, Point


# takes to times and returns the combined time
# input: Time
# input: Time
# output: Time
def time_add(time1: Time, time2: Time) -> Time:
    seconds = time1.second + time2.second
    minutes = time1.minute + time2.minute + seconds // 60
    seconds %= 60
    hours = time1.hour + time2.hour + minutes // 60
    minutes %= 60
    new_time = Time(hours, minutes, seconds)
    return  new_time


# Part 4

# takes in a list and returns whether each element in the list is less than the previous
# input: list[float]
# output: bool
def is_descending(nums: list[float]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i+1]:
            return False

    return True

# Part 5
from typing import Optional

# Takes in a list of ints and two indices, and returns the index of largest int within those indices
# input: list[int]
# input: int
# input: int
# output: int

def largest_between(nums: list[int], index_1: int, index_2: int) -> Optional[int]:
    if len(nums) == 0:
        return None
    index_1 = max(index_1, 0)
    index_2 = min(index_2, len(nums) - 1)

    if index_1 > index_2:
        return None

    best_index = index_1
    current_largest = nums[index_1]
    for i in range(index_1 + 1, index_2 + 1):
        if nums[i] > current_largest:
            best_index = i
            current_largest = nums[i]

    return best_index


# Part 6
import math

# Takes in a list of points and returns the index of the point that is the farthest from the origin (0,0)
# input: list[Point]
# Output: int
def furthest_from_origin(points: list[Point]) -> Optional[int]:
    if len(points) == 0:
        return None

    best_index = 0
    current_farthest = 0
    for i in range(0, len(points)):
        point = points[i]
        distance = distance_between_points(Point(0,0), point)
        if distance > current_farthest:
            best_index = i
            current_farthest = distance

    return best_index

# Takes in two points and returns the distance between them
# input: Point
# input: Point
# output: float
def distance_between_points(point1: Point, point2: Point) -> float:
    delta_x = point1.x - point2.x
    delta_y = point1.y - point2.y
    return math.hypot(delta_x, delta_y)