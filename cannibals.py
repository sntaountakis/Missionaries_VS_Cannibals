#Initial state. 
#{(Missionaries), (Cannibals), (Boat on side)}
import copy 
moveNumber = 0
class State():
    def __init__(self, riverLeft, riverRight):
       self.riverLeft = riverLeft
       self.riverRight = riverRight          
       self.parentNode = None
       self.visited = False

    def goal_reached(self): 
        if(self.riverRight[0] == self.riverRight[1]==3):
            return True
        else:
            return False

    def is_legal(self):
        if (self.riverLeft[0] >= 0 and self.riverLeft[1] >= 0 
        and self.riverRight[0] >= 0 and self.riverRight[1] >= 0 
        and (self.riverLeft[0] >= self.riverLeft[1] or self.riverLeft[0] == 0)  
        and (self.riverRight[0] >= self.riverRight[1] or self.riverRight[0] == 0)):
            return True 
        else: 
            return False

    def is_visited(self):
        self.visited = True

    def print_state(self):
        print("Left Side :\n    - Missionaries : "+str(self.riverLeft[0])+"\n    - Cannibals : "+str(self.riverLeft[1]))
        print("Right Side :\n    - Missionaries : "+str(self.riverRight[0])+"\n    - Cannibals : "+str(self.riverRight[1]))
        

def successor_states(currentState):
    childNodes = []
    
    if (currentState.riverLeft[2] == 1):
        #Pass two Cannibals
        newState = State(currentState.riverLeft.copy(), currentState.riverRight.copy())
        newState.riverLeft[1] -=2
        newState.riverLeft[2] -=1 
        newState.riverRight[1] +=2
        newState.riverRight[2] +=1     
        if newState.is_legal():
            newState.parentNode = currentState
            childNodes.append(newState)
        
        #Pass two Missionaries
        newState = State(currentState.riverLeft.copy(), currentState.riverRight.copy())
        newState.riverLeft[0] -=2
        newState.riverLeft[2] -=1 
        newState.riverRight[0] +=2
        newState.riverRight[2] +=1     
        if newState.is_legal():
            newState.parentNode = currentState
            childNodes.append(newState)

        #Pass one Cannibal
        newState = State(currentState.riverLeft.copy(), currentState.riverRight.copy())
        newState.riverLeft[1] -=1
        newState.riverLeft[2] -=1 
        newState.riverRight[1] +=1
        newState.riverRight[2] +=1     
        if newState.is_legal():
            newState.parentNode = currentState
            childNodes.append(newState)
        
        #Pass one Missionare
        newState = State(currentState.riverLeft.copy(), currentState.riverRight.copy())
        newState.riverLeft[0] -=1
        newState.riverLeft[2] -=1 
        newState.riverRight[0] +=1
        newState.riverRight[2] +=1     
        if newState.is_legal():
            newState.parentNode = currentState
            childNodes.append(newState)

        #Pass one Missionarie and one Cannibal
        newState = State(currentState.riverLeft.copy(), currentState.riverRight.copy())
        newState.riverLeft[0] -=1
        newState.riverLeft[1] -=1
        newState.riverLeft[2] -=1 
        newState.riverRight[0] +=1
        newState.riverRight[1] +=1
        newState.riverRight[2] +=1     
        if newState.is_legal():
            newState.parentNode = currentState
            childNodes.append(newState)
    

    if (currentState.riverRight[2] == 1):
        #Pass two Cannibals
        newState = State(currentState.riverLeft.copy(), currentState.riverRight.copy())
        newState.riverLeft[1] +=2
        newState.riverLeft[2] +=1 
        newState.riverRight[1] -=2
        newState.riverRight[2] -=1     
        if newState.is_legal():
            newState.parentNode = currentState
            childNodes.append(newState)
        
        #Pass two Missionaries
        newState = State(currentState.riverLeft.copy(), currentState.riverRight.copy())
        newState.riverLeft[0] +=2
        newState.riverLeft[2] +=1 
        newState.riverRight[0] -=2
        newState.riverRight[2] -=1     
        if newState.is_legal():
            newState.parentNode = currentState
            childNodes.append(newState)

        #Pass one Cannibal
        newState = State(currentState.riverLeft.copy(), currentState.riverRight.copy())
        newState.riverLeft[1] +=1
        newState.riverLeft[2] +=1 
        newState.riverRight[1] -=1
        newState.riverRight[2] -=1     
        if newState.is_legal():
            newState.parentNode = currentState
            childNodes.append(newState)
        
        #Pass one Missionare
        newState = State(currentState.riverLeft.copy(), currentState.riverRight.copy())
        newState.riverLeft[0] +=1
        newState.riverLeft[2] +=1 
        newState.riverRight[0] -=1
        newState.riverRight[2] -=1     
        if newState.is_legal():
            newState.parentNode = currentState
            childNodes.append(newState)

        #Pass one Missionarie and one Cannibal
        newState = State(currentState.riverLeft.copy(), currentState.riverRight.copy())
        newState.riverLeft[0] +=1
        newState.riverLeft[1] +=1
        newState.riverLeft[2] +=1 
        newState.riverRight[0] -=1
        newState.riverRight[1] -=1
        newState.riverRight[2] -=1     
        if newState.is_legal():
            newState.parentNode = currentState
            childNodes.append(newState)
        
    return childNodes

def breadth_first_search():
    riverLeft = [3, 3, 1]
    riverRight = [0, 0, 0]
    initialState = State(riverLeft, riverRight)
    visitedStates = [[3, 3, 1, 0, 0, 0]]    
    stack = list()
    stack.append(initialState)

    while stack:
        state = stack.pop()
        
        children = successor_states(state)
        
        if state.goal_reached():
            return state

        for child in children:
            if not visited_states(child, visitedStates):
                stack.append(child)
        
    return None     


def print_goal(goal):
    global moveNumber
    if goal is not None:
        print_goal(goal.parentNode)
        moveNumber+=1
        print("-----------State #"+str(moveNumber)+"--------------")
        goal.print_state()
        
def visited_states(state, visitedStates):
    
    for i in range(len(visitedStates)):
        if (str(state.riverLeft) == str(visitedStates[i][:3])) and (str(state.riverRight) == str(visitedStates[i][-3:])):
            return True
    visitedStates.append(state.riverLeft+state.riverRight)
    return False 

def main():
    goal = breadth_first_search()
    if goal is not None:
        print_goal(goal)
        print("Goal reached")

if __name__ == "__main__":
    main() 

