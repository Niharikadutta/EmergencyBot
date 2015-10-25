__author__ = "Abhimanyu Dogra and Niharika Dutta"

#! /usr/bin/env python

class App:
    def __init__(self, grid, source, destination):
        self.grid = grid
        self.source = source
        self.destination = destination
        self.current = self.source
        self.n = len(grid[0])  # length of the grid which is a square
        
    def _update_grid(self, x, y, state):
        self.grid[x][y] = state

    def _bfs(self, source): #Assumes source is not an obstacle
        Q = []
        Q.append(source)
        visited = [[False]*self.n for __ in xrange(self.n)]
        parent = [[(-1, -1)]*self.n for __ in xrange(self.n)]
        visited[source[0]][source[1]] = True
        while len(Q) != 0:
            current = Q.pop(0)
            #print 'current = ', current
            if self.grid[current[0]][current[1]] == "preferred":
                break
            adj = self._adj(current, self.destination)
            for node in adj:
                if not visited[node[0]][node[1]]:
                    Q.append(node)
                    visited[node[0]][node[1]] = True
                    parent[node[0]][node[1]] = current
        current = parent[current[0]][current[1]]
        while current != source:
            #print '>'*3, current, 
            self.grid[current[0]][current[1]] = "preferred"
            current = parent[current[0]][current[1]]
        
    def next_step(self, cur_x, cur_y):
        adj = self._adj((cur_x,cur_y), self.destination)
        found_preferred_cell = False
        for x, y in adj:
            if self.grid[x][y] == "preferred":
                found_preferred_cell = True
                result = (x, y)
                break
        if not found_preferred_cell:
            self.grid[cur_x][cur_y] = "free"
            self._bfs((cur_x, cur_y))
            result = self.next_step(cur_x, cur_y)
            #found_free_cell = False
            #for x, y in adj:
            #    if self.grid[x][y] == "free":
            #        found_free_cell = True
            #        result = (x, y)
            #        self._bfs((x, y))
            #        break
            #if not found_free_cell:
            #    result = (-1, -1)
        return result
            
    def moved(self, x, y):
        self.grid[x][y] = "free"
        
    def mark_obstacle(self, x, y):
        self.grid[x][y] = "obstacle"
        
    def _adj(self, current, destination):
        #print 'In _adj()'
        #neighbours = ((current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]+1), (current[0], current[1]-1))
        #neighbours = ((current[0], current[1]+1), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0]-1, current[1]))
        neighbours = [None] * 4
        west, north, east, south = (current[0], current[1]+1), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0]-1, current[1])
        if destination[0] > current[0]:
            neighbours[0] = north
            neighbours[1] = south
        else:
            neighbours[0] = south
            neighbours[1] = north
        if destination[1] > current[1]:
            neighbours[2] = west
            neighbours[3] = east
        else:
            neighbours[2] = east
            neighbours[3] = west
        adj = [(x, y) for x, y in neighbours if x >= 0 and x < self.n and y >=0 and y < self.n and self.grid[x][y] != "obstacle"]
        return adj
        
