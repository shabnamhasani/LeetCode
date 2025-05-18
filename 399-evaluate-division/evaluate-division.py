class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        # Step 1: Build the graph
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        # Step 2: DFS function
        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if dst in graph[src]:
                return graph[src][dst]
            visited.add(src)
            for neighbor, weight in graph[src].items():
                if neighbor not in visited:
                    result = dfs(neighbor, dst, visited)
                    if result != -1.0:
                        return result * weight
            return -1.0

        # Step 3: Process each query
        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))
        return results