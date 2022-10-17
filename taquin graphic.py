import random
from cmath import rect

import pygame as p
import tkinter as t
from file import file 
from pile import pile 
import time

r=t.Tk()

p.init()

win=p.display.set_mode((330,330))
p.display.set_caption('PUZZLE BY AJ')
global p1,p2,p3,p4,p5,p6,p7,p8,p9

p1=(10,10)
p2=(115,10)
p3=(220,10)

p4=(10,115)
p5=(115,115)
p6=(220,115)

p7=(10,220)
p8=(115,220)
p9=(220,220)

class taq :
    def __init__(self,num,pos,pic) :
        self.pos=pos
        self.pic=p.image.load(pic)
        self.num=num


r1=taq(1,p1,'r1.png')
r2=taq(2,p2,'r2.png')
r3=taq(3,p3,'r3.png')

r4=taq(4,p4,'r4.png')
r5=taq(5,p5,'r5.png')
r6=taq(6,p6,'r6.png')

r7=taq(7,p7,'r7.png')
r8=taq(8,p8,'r8.png')
#rn=taq(None,p9,'r9.png')


def show_g() :

  win.blit(p.image.load('b14.jpg'),(0,0))
  for r in [r1,r2,r3,r4,r5,r6,r7,r8] :
      win.blit(r.pic,r.pos)
  p.display.update()
      


def move(curr,goal) :
    etat_g(curr)
    ps1=get_pos(None,curr)
    ps2=get_pos(None,goal)
    cl=120
    if ps1[0]>ps2[0] :
        
        for r in [r1,r2,r3,r4,r5,r6,r7,r8] :
            if r.num==curr[ps2[0]][ps2[1]] :
                x=0
                while x<=100:
                    
                    x+=10
                    show_g()
                    p.time.Clock().tick(cl)
                    r.pos=(r.pos[0],r.pos[1]+10)
                   
                break
    elif ps1[0]<ps2[0] :
        for r in [r1,r2,r3,r4,r5,r6,r7,r8] :
            if r.num==curr[ps2[0]][ps2[1]] :
                x=0
                while x<=105 :
                    r.pos=(r.pos[0],r.pos[1]-10)
                    x+=10
                    
                    p.time.Clock().tick(cl)
                    show_g()
                    
                    
                break
    elif  ps1[1]<ps2[1] :
        for r in [r1,r2,r3,r4,r5,r6,r7,r8] :
            if r.num==curr[ps2[0]][ps2[1]] :
                x=0
                while x<=105 :
                    r.pos=(r.pos[0]-10,r.pos[1])
                    x+=10
                    p.time.Clock().tick(cl)
                    show_g()
                    
                    
                break
    elif  ps1[1]>ps2[1] :
        for r in [r1,r2,r3,r4,r5,r6,r7,r8] :
            if r.num==curr[ps2[0]][ps2[1]] :
                x=0
                while x<=105 :
                    r.pos=(r.pos[0]+10,r.pos[1])
                    x+=10
                    p.time.Clock().tick(cl)
                    show_g()
                    
                break
def etat_g(etat) :
   for i in range(3):
       if i==0 :
            
            for r in [r1,r2,r3,r4,r5,r6,r7,r8] :
                    if r.num==etat[0][0] :
                        r.pos=p1
                    if r.num==etat[0][1] :
                        r.pos=p2
                    if r.num==etat[0][2] :
                        r.pos=p3
        
       elif i==1 :
    
               for r in [r1,r2,r3,r4,r5,r6,r7,r8] :
                 if r.num==etat[1][0] :
                     r.pos=p4
                 if r.num==etat[1][1] :
                     r.pos=p5

                 if r.num==etat[1][2] :
                     r.pos=p6

               
       elif i==2 :
               for r in [r1,r2,r3,r4,r5,r6,r7,r8] :
                 if r.num==etat[2][0] :
                     r.pos=p7

                 if r.num==etat[2][1] :
                     r.pos=p8

                 if r.num==etat[2][2] :
                     r.pos=p9

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


def A_star(inp) :
    
    print(inp)
    fi=[[1,2,3],[4,5,6],[7,8,None]]
    list_explore=[]
    pl=pile()
    pl.empiler(inp)
    etat_g(inp)
    show_g()
    time.sleep(3)
    while pl.p!=[]  :
       
        x=pl.dernier()
        
        if len(list_explore)>=2 :
            move(list_explore[-1],x)
         
        list_explore.append(x)
        if  fi in list_explore :
            time.sleep(5)
            break
          
        

        pl.depiler()
        
        for i in sorted_succ(x) :
            if i not in list_explore :
              pl.empiler(i)
        p.display.set_caption(str(len(list_explore))+' : moves .........BY AJ')
    p.quit()
       
    





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
     
    


while True :
    x=etatin()
    if is_solvable(x) :
        break

A_star(x)

       
