from collections import defaultdict, deque
import heapq
from typing import List

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        totalEdges = len(edges)
        for i in range(totalEdges):
            u, v, w = edges[i]
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [float('inf')] * n
        dist[0] = 0
        min_heap = [(0, 0)] 
        while min_heap:
            d, node = heapq.heappop(min_heap)
            if d > dist[node]:
                continue
            for v, w in adj[node]:
                if dist[v] > dist[node] + w:
                    dist[v] = dist[node] + w
                    heapq.heappush(min_heap, (dist[v], v))

        if dist[n - 1] == float('inf'):
            return [False] * totalEdges
        
        ans = [False] * totalEdges
        q = deque([(n - 1, dist[n - 1])])
        visited = set()
        shortest_path_edges = set()

        while q:
            node, d = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            for v, w in adj[node]:

                if d - w == dist[v]:
                    shortest_path_edges.add((min(node, v), max(node, v)))
                    q.append((v, dist[v]))

        for i in range(totalEdges):
            u, v, _ = edges[i]
            if (min(u, v), max(u, v)) in shortest_path_edges:
                ans[i] = True

        return ans
