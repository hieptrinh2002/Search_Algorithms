from Space import *
from Constants import *
import math

def draw_path(g:Graph , father: list , sc:pygame.Surface):
    temp = g.goal;
    while True:
        if temp == g.start:
            return; 
        pygame.draw.line(sc, green, [temp.x, temp.y],[(father[temp.value]).x, (father[temp.value]).y], 3);
        temp = father[temp.value];
        if temp != g.start:
            temp.set_color(grey);
        g.draw(sc); 

#stack
def DFS(g:Graph, sc:pygame.Surface):
    open_set = [g.start] # list Node
    closed_set = []      # list Node
    father = [-1]*g.get_len()

    while len(open_set):
        current = open_set.pop();
        current.set_color(yellow);
        g.draw(sc)
        #sleep(1)
        closed_set.append(current);
        current.set_color(blue);
        
        if(g.is_goal(current)):
            g.start.set_color(orange)
            current.set_color(purple)
            draw_path(g,father,sc);
            return;
        
        for neighbor in g.get_neighbors(current):
            if neighbor not in closed_set:
                father[neighbor.value] = current
                open_set.append(neighbor)
                neighbor.set_color(red)
        g.draw(sc)
    raise NotImplementedError('Not implemented')              

def BFS(g:Graph, sc:pygame.Surface):
    
    print('Implement BFS algorithm')
    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len(); # init father 
    start = g.start;
    if(g.is_goal(g.start)):
        return;
       
    for current in open_set:
        current.set_color(yellow);
        closed_set.append(current);
        if g.is_goal(current): # check là đích đến hay chưa
            current.set_color(purple);  start.set_color(orange);
            g.draw(sc);
            draw_path(g,father,sc);
            return;            
        # duyệt và tô màu đỏ cho các node meighbors màu đỏ
        for neighbor in g.get_neighbors(current):
            if neighbor not in closed_set and neighbor not in open_set:
                father[neighbor.value] = current;
                open_set.append(neighbor);
                neighbor.set_color(red);
                g.draw(sc);
                
        current.set_color(blue);      
    raise NotImplementedError('Not implemented')              


def priority_pop(dict:dict):
    key, min = next(iter(dict.items()))
    for k , pval in dict.items():
        if pval < min:
            min = pval
            key = k

    dict.pop(key)
    return (key, min)

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = [g.start.value]
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()    
    cost[g.start.value] = 0
    
    while open_set:
        key,_ = priority_pop(open_set);
        currNode = g.grid_cells[key];
        if(g.is_goal(currNode)):
            currNode.set_color(purple);  g.start.set_color(orange);
            draw_path(g,father,sc);
            return;
        currNode.set_color(yellow);
        g.draw(sc);
        for neighbor in g.get_neighbors(currNode):
            total_cost = cost[key] + 1
            if neighbor.value not in closed_set and neighbor.value not in list(open_set.keys()):
                father[neighbor.value] = currNode;
                closed_set.append(neighbor.value);
                neighbor.set_color(red);
                g.draw(sc);
                if total_cost < cost[neighbor.value]:
                    cost[neighbor.value] = total_cost;
                    open_set[neighbor.value] = total_cost; 
        currNode.set_color(blue);
        g.draw(sc);
    raise NotImplementedError('Not implemented')              
    

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = [g.start.value]
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()    
    cost[g.start.value] = 0
    
    while open_set:
        key,_ = priority_pop(open_set);
        currNode = g.grid_cells[key];
        if(g.is_goal(currNode)):
            currNode.set_color(purple);  g.start.set_color(orange);
            draw_path(g,father,sc);
            return;
        currNode.set_color(yellow);
        g.draw(sc);
        for neighbor in g.get_neighbors(currNode):
            total_cost = cost[key] + 1
            if neighbor.value not in closed_set:
                father[neighbor.value] = currNode;
                closed_set.append(neighbor.value);
                neighbor.set_color(red);
                g.draw(sc);
                if total_cost < cost[neighbor.value]:
                    cost[neighbor.value] = total_cost;
                    open_set[neighbor.value] = total_cost + int(math.sqrt((neighbor.x - g.goal.x)**2 + (neighbor.y - g.goal.y)**2)); # h()
        currNode.set_color(blue);
        g.draw(sc);
    raise NotImplementedError('Not implemented')              
    
    