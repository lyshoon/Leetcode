""" There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array."""

from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        g = defaultdict(list)

        for a, b in prerequisites:
            g[b].append(a)
        states = [0] * numCourses 
            
        def dfs(i):
            if states[i] == -1: 
                return False
            if states[i] == 1:  
                return True
            states[i] = -1

            for nei in g[i]:
                if not dfs(nei):
                    return False
            states[i] = 1
            order.append(i)
            return True

        for i in range(numCourses):
            if states[i] == 0: 
                if not dfs(i):
                    return [] 
        return order[::-1]
