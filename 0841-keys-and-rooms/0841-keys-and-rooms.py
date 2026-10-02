class Solution(object):
    def canVisitAllRooms(self, rooms):
        n=len(rooms)
        visited=[False]*n
        def dfs(room):
            for key in rooms[room]:
                if  not  visited[key]:
                    visited[key]=True
                    dfs(key)          
        visited[0]=True
        dfs(0)
        return all(visited)


            
                