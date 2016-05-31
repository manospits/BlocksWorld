"""Blocks World Problem"""

from search import *

class BlocksWorld(Problem) :
    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial; self.goal = goal
        #each state corresponds to a tuple containing tuples, for example state((1,2,3),(4,5)) corresponds to
        #
        # 3
        # 2 5
        #_1_4_

    def compgoalstate1(self,s) :
        sum=0
        for j in s :
            for i in self.goal:
                if j[0] in i:
                    stack_to_comp=i
                    break
            for c1 in j:
                if (c1 in stack_to_comp):
                    if j.index(c1)==stack_to_comp.index(c1):
                        continue
                sum+=len(j)-j.index(c1) #all blcks above c1 must be moved +1 move for each
                for k in j[j.index(c1):]: #checking if any of the blocks above needs two moves
                    if j.index(k)==0:
                        continue
                    for m in self.goal:
                        state2=0
                        if (k in m) and (m.index(k)!=0):
                            for l  in j[:j.index(k)]:
                                if l in m and m.index(k)>m.index(l) :     #if there any blocks below block k both in current and goal
                                    sum+=1                                #then they must be moved in the right place then k will
                                    state2=1                              #be able to be placed in it's correct position but before that
                                    break                                 #it should be placed on the table, so k requires 2 moves!
                            if state2!=1:#here checking if the position of q cube is available or not if not +1 move
                                state2=1
                                state3=0
                                for q in s:
                                    if m[0] in q:
                                        if len(q)>m.index(k) or len(q)<m.index(k)-1:# not equal with  m.index(k)
                                            sum+=1
                                            break
                                        else:
                                            for c2 in m:
                                                for c3 in q:
                                                    if c2!=c3:
                                                        sum+=1
                                                        state3=1
                                                        break
                                                if state3==1:
                                                    break
                                    if state3==1:
                                        break
                        if state2==1:
                            break
                break
        # print s,sum
        return sum

    def compgoalstate2(self,s) :
        sum=0
        for j in s :
            for i in self.goal:
                if j[0] in i:
                    stack_to_comp=i
                    break
            for c1 in j:
                if (c1 in stack_to_comp):
                    if j.index(c1)==stack_to_comp.index(c1):
                        continue
                sum+=len(j)-j.index(c1) #all blcks above c1 must be moved +1 move for each
                for k in j[j.index(c1):]: #checking if any of the blocks above needs two moves
                    if j.index(k)==0:
                        continue
                    for m in self.goal:
                        state2=0
                        if (k in m) and (m.index(k)!=0):
                            for l  in j[:j.index(k)]:
                                if l in m and m.index(k)>m.index(l) :     #if there any blocks below block k both in current and goal
                                    sum+=1                                #then they must be moved in the right place then k will
                                    state2=1                              #be able to be placed in it's correct position but before that
                                    break                                 #it should be placed on the table, so k requires 2 moves!
                        if state2==1:
                            break
                break
        # print s,sum
        return sum

    def compgoalstate3(self,s) : #checking whether a block sits on the right place(table/block)
        sum=0
        for j in s :
            for c1 in j:
                for i in self.goal:
                    if c1 in i:
                        if (i.index(c1)==0 and j.index(c1)!=0) or(i.index(c1)!=0 and j.index(c1)==0):
                            sum+=1
                            break
                        elif i[i.index(c1)-1]!=j[j.index(c1)-1]:
                            sum+=1
                            break
        # print s,sum
        return sum

    def actions(self,state) :
        validActions=[]
        for column_i in state :
            if len(column_i) > 1 : #each action is depicted by the pair of the initial stack ,the destination
                validActions.append((state.index(column_i),'N',1))#of the cube and the length of the destination stack after the cube is placed.
            for column_j in state :                        #example (1,2,3) means take cube from stack 1 and place it on stack 3
                if column_i!=column_j :
                    validActions.append((state.index(column_i),state.index(column_j),len(column_j)+1))
        validActions.sort(key=lambda x: int(x[2]))
        return validActions
#--------------------------------------------------------------------
    def result(self, state, action) :
        temp=list(state)
        LastCubeInColumnI=temp[action[0]][-1]
        temp.remove(state[action[0]])
        if len(state[action[0]]) > 1 :
            temp.append(state[action[0]][0:-1])
        if action[1]=='N' :
            temp.append((LastCubeInColumnI,))
        else :
            temp.remove(state[action[1]])
            temp.append(state[action[1]]+(LastCubeInColumnI,))
        temp.sort(key = lambda s: len(s))
        return tuple(temp)

    def goal_test(self,state):
        for i in state:
            if i not in self.goal:
                return False
        return True
