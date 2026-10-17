class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]

        for pair in prerequisites:
            a = pair[0]
            b = pair[1]
            graph[b].append(a)

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return True

            if course in visited:
                return False

            visiting.add(course)
            for neighbor in graph[course]:
                if dfs(neighbor):
                    return True
            visiting.remove(course)
            visited.add(course)
            return False
        for course in range(numCourses):
            if dfs(course):
                return False
        return True