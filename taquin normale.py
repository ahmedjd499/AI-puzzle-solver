import random
from re import X
from pile import pile

def get_pos(p,etat) :
    
    for i in range(3):
        if p in etat[i] :
           pos=(i,etat[i].index(p))
           break
    return pos
  
def etatin() :
    etat_in=[[0,0,0],[0,0,0],[0,0,0]]
    
    for i in range(0,3) :
         for j in range(0,3) :
             while True :
                 x=random.randint(1,9)
                 if x not in etat_in[0] and  x not in etat_in[1] and x not in  etat_in[2] :
                     break
             etat_in[i][j]=x
    etat_in[get_pos(9,etat_in)[0]][get_pos(9,etat_in)[1]]=None
    return etat_in

def succ(etat) :
    succ=[]
    
    etatposs=[[0,0,0],[0,0,0],[0,0,0]]
    etatposs2=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,3) :
         for j in range(0,3) :
              etatposs[i][j]=etat[i][j]
              etatposs2[i][j]=etat[i][j]



    for i in range(3):
        if None in etat[i] :
           pos=(i,etat[i].index(None))
           break
    
    if pos[1]==0 :
        x=action(etatposs,pos,(pos[0],pos[1]+1))
        succ.append(x)
       
    elif pos[1]==1 :
        x=action(etatposs,pos,(pos[0],pos[1]+1))
        succ.append(x)
        
        x=action(etatposs,pos,(pos[0],pos[1]-1))
        succ.append(x)
        
    elif pos[1]==2:
        x=action(etatposs,pos,(pos[0],pos[1]-1))
        succ.append(x)
       


    if pos[0]==0 :
        x=action(etatposs2,pos,(pos[0]+1,pos[1]))
        succ.append(x)
        
    elif pos[0]==1 :
        x=action(etatposs2,pos,(pos[0]+1,pos[1]))
        succ.append(x)
        
        x=action(etatposs2,pos,(pos[0]-1,pos[1]))
        succ.append(x)
    elif pos[0]==2 :
        x=action(etatposs2,pos,(pos[0]-1,pos[1]))
        succ.append(x)
    return succ

def action(etat1,pos1,pos2):
    etat=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,3) :
         for j in range(0,3) :
              etat[i][j]=etat1[i][j]
    aux=etat[pos1[0]][pos1[1]]
    etat[pos1[0]][pos1[1]]=etat[pos2[0]][pos2[1]]
    etat[pos2[0]][pos2[1]]=aux
    return etat

def show(etat):
    print(etat[0])
    print(etat[1])
    print(etat[2])
    print('-----------')

def getpos(etat,x):
    for i in range(3):
        if x in etat[i] :
           return(i,etat[i].index(x))

def hn(etat):  # miss playced nodes
    c=0
    fi=[[1,2,3],[4,5,6],[7,8,None]]
    for i in range(0,3) :
         for j in range(0,3) :
             if etat[i][j] !=fi[i][j] :
                 c+=1
    return c

  
def fn(etat):  # manhuten
    c=0
    fi=[[1,2,3],[4,5,6],[7,8,None]]
    for i in range(0,3) :
         for j in range(0,3) :
             if etat[i][j] !=fi[i][j] :
                 c+=abs(i-get_pos(etat[i][j],fi)[0]) + abs(j-get_pos(etat[i][j],fi)[1])

    return c
   
def sorted_succ(x) :
    l=[]
    ss=[]
    for i in succ(x) :
         l.append(hn(i)+fn(i))
    l.sort(reverse=True)
    for g in l :
        for  i in succ(x) :
            if g== hn(i)+fn(i) and i not in ss :
                ss.append(i)
                break

    return ss 

etattest=[[None,1,2],[5,6,7],[4,3,8]]

def A_star(inp) :
    
    
    fi=[[1,2,3],[4,5,6],[7,8,None]]
    list_explore=[]
    pl=pile()
    pl.empiler(inp)
    
    while pl.p!=[]  :
       
        x=pl.dernier()
        list_explore.append(x)

        show(x)

        if  fi in list_explore :
            break
          
        

        pl.depiler()
        
        for i in sorted_succ(x) :
            if i not in list_explore :
              pl.empiler(i)
        print(len(pl.p))
       
    show(list_explore[-1])
    print(inp)


def getInvCount(arr):
    inv_count = 0
    empty_value =None
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count
 
     
# This function returns true
# if given 8 puzzle is solvable.
def is_solvable(puzzle) :
 
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])
 
    # return true if inversion count is even.
    return (inv_count % 2 == 0)
     
    



#   [[6, 3, 7], [4, 5, 1], [None, 8, 2]]  ,   [[6, 1, 7], [5, 8, 2], [None, 4, 3]] ,[[3, 4, 1], [7, 6, None], [5, 2, 8]],[[6, 4, 5], [None, 8, 1], [2, 7, 3]]

while True :
    x=etatin()
    if is_solvable(x) :
        break

A_star(x)
