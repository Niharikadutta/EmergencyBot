__author__ = "Abhimanyu Dogra and Niharika Dutta"

#! /usr/bin/env python

from app import App

GRID_SIZE = 5

class BOT:
    def __init__(self, grid, source, destination, current_direction):
        self.direction = current_direction
        self.GRID = grid
        self.current_position = source
        self.destination = destination
        self.app = App(grid, source, destination)
    
    def main(self):
        #app = App(self.GRID)
        #self.printGrid(GRID_SIZE)
        while(self.current_position != self.destination):
            next_x,next_y = self.app.next_step(self.current_position[0],self.current_position[1])
            if(self.is_safe(next_x,next_y)):
                print "Next x = %d, Next y = %d is safe" %(next_x,next_y)
                self.move_straight(next_x,next_y)
            else:
                print "Encountered obstacle at Next x = %d, Next y = %d" %(next_x,next_y)
                self.app.mark_obstacle(next_x,next_y)
                #self.app.update_grid(self.current_position[0],self.current_position[1])
				#import ipdb; ipdb.set_trace()
                
    def printGrid(self,n):    
        for i in range(n):
            for j in range(n):
                print self.GRID[i][j],
            print
        print self.current_position
        print self.destination
        
    def is_safe(self,next_x,next_y):
        print "current direction %s" %self.direction
        if(self.current_position[0] < next_x):
            self.turn_north()
        elif(self.current_position[0] > next_x):
            self.turn_south()
        elif(self.current_position[1] < next_y):
            self.turn_west()
        else:
			self.turn_east()
        if(next_x == 2 and next_y == 1):
            return False
        if(self.GRID[next_x][next_y] == "obstacle"):
            return False
        else:
		    return True
        		 
    def turn_south(self):
        print "Moving south now"
        if(self.direction == "north"):
            self.turn_180_deg()
        elif(self.direction == "east"):
            self.turn_90_deg_clock_wise()
        elif(self.direction == "west"):
            self.turn_90_deg_anti_clock_wise()
        else:    
            pass
        self.direction = "south"
            
    def turn_north(self):
        print "Moving north now"
        if(self.direction == "south"):
            self.turn_180_deg()
        elif(self.direction == "west"):
            self.turn_90_deg_clock_wise()
        elif(self.direction == "east"):
            self.turn_90_deg_anti_clock_wise()
        else:
            pass
        self.direction = "north"
        
    def turn_east(self):
        print "Moving east now"
        if(self.direction == "west"):
            self.turn_180_deg()
        elif(self.direction == "south"):
            self.turn_90_deg_anti_clock_wise()
        elif(self.direction == "north"):
            self.turn_90_deg_clock_wise()
        else:
            pass
        self.direction = "east"
        
    def turn_west(self):
        print "Moving west now"
        if(self.direction == "east"):
            self.turn_180_deg()
        elif(self.direction == "north"):
            self.turn_90_deg_anti_clock_wise()
        elif(self.direction == "south"):
            self.turn_90_deg_clock_wise()
        else:
            pass
        self.direction = "west"
    
    def turn_180_deg(self):
        print "Turning 180 degree"
        self.turn_90_deg_clock_wise()
        self.turn_90_deg_clock_wise()
        
    def turn_90_deg_clock_wise(self):
        print "Turning 90 degree clockwise"
    
    def turn_90_deg_anti_clock_wise(self):
        print "Turning 90 degree anticlockwise"    
    
    def move_straight(self,next_x,next_y):
        print "Moving straight now"
        
        self.app.moved(next_x, next_y)   
        self.current_position = (next_x, next_y)
        
def make_grid(n):            
    grid = [["free"]*n for __ in xrange(n)]    
    blocked = [(0, 3), (1, 3), (2, 2), (2, 3)]    
    preferred = [(0, 1), (0, 2), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]  #(0, 0),  removed
    for b in blocked:
        grid[b[0]][b[1]] = "obstacle"    
    for p in preferred:
        grid[p[0]][p[1]] = "preferred"
    return grid

if __name__ == '__main__':
    n = input()
    input_grid = [ [int(x) for x in raw_input().split()] for __ in xrange(n) ]  
    grid_values = ['obstacle', 'free', 'preferred']
    grid = [ [grid_values[i] for i in row] for row in input_grid]
    source = tuple(map(int, raw_input().split()))
    destination = tuple(map(int, raw_input().split()))
    grid[source[0]][source[1]] = 'free'
    cur_dir = raw_input()
    bot = BOT(grid, source, destination, cur_dir)
    bot.printGrid(n)
    bot.main()
