from BlocksWorld import *
import random
def h1(n) :
    return p.compgoalstate1(n.state)
def h2(n) :
    return p.compgoalstate2(n.state)
def h3(n) :
    return p.compgoalstate3(n.state)

def random_state(n):
    random.seed()
    sizeofstart=random.randint(1,n)
    start=[]
    for i in range(0,sizeofstart):
        start.append(['a',])
    for i in range(0,n):
        x=random.randint(0,sizeofstart-1)
        start[x].append(i)
        if 'a' in start[x]:
            start[x].remove('a')
    fstart=[]
    for i in start:
        if 'a' not in i:
            fstart.append(tuple(i))
    tuplestart=tuple(fstart)
    sizeofend=random.randint(1,n)
    end=[]
    for i in range(0,sizeofend):
        end.append(['a',])
    for i in range(0,n):
        x=random.randint(0,sizeofend-1)
        end[x].append(i)
        if 'a' in end[x]:
            end[x].remove('a')
    fend=[]
    for i in end:
        if 'a' not in i:
            fend.append(tuple(i))
    tupleend=tuple(fend)
    problem=(tuplestart,tupleend,)
    return problem


#-----------must make changes in search.py to run below code----------
# for i in range(2,60):
#     su=0
#     start=time.time()

#     for j in range(0,10):
#         x=random_state(i)
#         # print x
#         p = BlocksWorld(x[0],x[1])
#         s = astar_search(p,h1)
#         # print s
#         su+=int(s)
#     end=time.time()
#     print "Average nodes of :",i," blocks is :",su/i," and average time is :",(end-start)/

print"Enter number of cubes : "
num_of_cubes=raw_input()
num_of_cubes=int(num_of_cubes)
print"Enter the number of tests you want to make:"
num_of_tests=raw_input()
num_of_tests=int(num_of_tests)
print"Enter the number of the heuristic you want to use:"
num=raw_input()
num=int(num)
if num!=1 and num!=2 and num!=3:
    print"ERROR"
    assert(1)
for j in range (0,num_of_tests):
    x=random_state(num_of_cubes)
    print"Initial state :",x[0]
    print"Goal state :",x[1]
    # p=BlocksWorld(((3,2,),(5,4)),((3,4),(5,2)))
    p=BlocksWorld(x[0],x[1])
    # s = breadth_first_search(p)
    if num==1:
        s = astar_search(p,h1)
    elif num==2:
        s = astar_search(p,h2)
    else:
        s = astar_search(p,h3)
    sol = s.solution()
    path= s.path()
    print "Solution: \n+{0}+\n|Action \t|State\t\t\t\t	 \t|Path Cost |\n+{0}+".format('-'*74)
    for i in range(len(path)) :
        state = path[i].state
        cost = path[i].path_cost
        action = "(S, S) "
        if i > 0 : # The initial state has not an action that results to it
            action = sol[i-1]
            width=10
        print "|{0} \t|{1}  \t\t|{2} \t   |".format(action , state , cost)
    print "+{0}+".format('-'*74)

