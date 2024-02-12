'''
853. Car Fleet
Solved
Medium
Topics
Companies
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.

'''
class Solution:
    def carFleet(self, target, position, speed):
        # we are zipping as we have two separate arrays, as pairs
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
        # time to reach destination is target/speed
            stack.append((target - p) / s)
            # check if stack has atleast 2 items to compare
            # time of top of stack reached before ahead car, so they collide
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # beacuse they collide we pop as to keep the ahead one
                stack.pop()
        return len(stack)

def main():
    solutionObj = Solution()
    print(solutionObj.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))

if __name__ == '__main__':
    main()