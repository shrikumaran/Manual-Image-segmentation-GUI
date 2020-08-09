from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import cv2
import numpy as np
import math as m
import pandas as pd
from tempfile import TemporaryFile
from cryptography.fernet import Fernet
import os
import glob


#initialisation
path="C:\\Users\\V K VIEKASH\\Desktop\\INTERN 2020 SUMMER\\Origin Health\\2. Image enhancement\\DATASET\\better images\\*.png"
flag=0
count=0
num_class=14
State = {0: 'disabled', 1: "normal"}
thickness=3# default thickness of the brush


#LISTS
lisx=[]
lisy=[]
lis=[]


#ROOT PARAMETERS
root=Tk()
#VALUES SET BY TRAIL AND ERROR TO COVER MAX SPACE IN WINDOW ASWELL AS TO BE POSITIONED APPROXIMATELY AT THE CENTER
X=107#factor of size for x axis of layout
Y=43.3#factor of size for y axis of layout
W=int(14*X)#width of window
H=int(18*Y)#height of window
hs = root.winfo_screenheight() # getting screen's height in pixels 
ws = root.winfo_screenwidth() # getting screen's width in pixels\
G=12# a correction factor considering the bottom task bar of windows 10,based on trail and error
R=int(((ws-W)/2)-G)#right position from screen top left
F=35# a correction factor considering the bottom task bar of windows 10,based on trail and error
D=int(((hs-H)/2)-F)#down position from screen top left
root.geometry(str(W)+"x"+str(H)+"+"+str(R)+"+"+str(D))#("window width x window height + position right + position down")
root.resizable(width=False,height=False)#TO NOT ALLOW SCREEN RESIZING
root.title('TK_SEGMENTATION_TOOL_V2')
root.iconbitmap("icon.ico")


#--------------------------------------------------------------FUNCTIONS-------------------------------------------------------------------------------

# A SERIES OF FUNCTIONS THAT WILL SET THE SEHMENTATION AND LOCK CHECK BOXES AS WE CHANGE IMAGES
def update_check_set_var_2(value):
    seg_mat[index][0]=value
    
def L_update_check_set_var_2(value):
   lock_mat[index][0]=value

def update_check_set_var_3(value):
    seg_mat[index][1]=value
    
def L_update_check_set_var_3(value):
   lock_mat[index][1]=value

def update_check_set_var_4(value):
    seg_mat[index][2]=value
    
def L_update_check_set_var_4(value):
   lock_mat[index][2]=value

def update_check_set_var_5(value):
    seg_mat[index][3]=value
    
def L_update_check_set_var_5(value):
   lock_mat[index][3]=value

def update_check_set_var_6(value):
    seg_mat[index][4]=value
    
def L_update_check_set_var_6(value):
   lock_mat[index][4]=value

def update_check_set_var_7(value):
    seg_mat[index][5]=value
    
def L_update_check_set_var_7(value):
   lock_mat[index][5]=value

def update_check_set_var_8(value):
    seg_mat[index][6]=value
    
def L_update_check_set_var_8(value):
   lock_mat[index][6]=value

def update_check_set_var_9(value):
    seg_mat[index][7]=value
    
def L_update_check_set_var_9(value):
   lock_mat[index][7]=value

def update_check_set_var_10(value):
    seg_mat[index][8]=value
    
def L_update_check_set_var_10(value):
   lock_mat[index][8]=value

def update_check_set_var_11(value):
    seg_mat[index][9]=value
    
def L_update_check_set_var_11(value):
   lock_mat[index][9]=value

def update_check_set_var_12(value):
    seg_mat[index][10]=value
    
def L_update_check_set_var_12(value):
   lock_mat[index][10]=value

def update_check_set_var_13(value):
    seg_mat[index][11]=value
    
def L_update_check_set_var_13(value):
   lock_mat[index][11]=value

def update_check_set_var_14(value):
    seg_mat[index][12]=value
    
def L_update_check_set_var_14(value):
   lock_mat[index][12]=value

def update_check_set_var_15(value):
    seg_mat[index][13]=value
    
def L_update_check_set_var_15(value):
   lock_mat[index][13]=value


# BASED ON THE ABOVE VALUE SETTINGS THE CHECK BOXES ARE UPDATED
def update_check_set():
    global seg_mat
    global lock_mat

    global var_2
    global Lvar_2
    global var_3
    global Lvar_3
    global var_4
    global Lvar_4
    global var_5
    global Lvar_5
    global var_6
    global Lvar_6
    global var_7
    global Lvar_7
    global var_8
    global Lvar_8
    global var_9
    global Lvar_9
    global var_10
    global Lvar_10
    global var_11
    global Lvar_11
    global var_12
    global Lvar_12
    global var_13
    global Lvar_13
    global var_14
    global Lvar_14
    global var_15
    global Lvar_15

    
    #CHECK_2(CHECKBOXES) 
   
    check_2=Checkbutton(root,text='',variable=var_2,state=State[ind_mat[index][0]],command=lambda: update_check_set_var_2(var_2.get()))

    if(seg_mat[index][0]==0):
        check_2.deselect()
    if(seg_mat[index][0]==1):
        check_2.select()
        
    check_2.grid(row=3,column=2)

    #LOCK_2(CHECKBOXES) 
   
    LOCK_2=Checkbutton(root,text='',variable=Lvar_2,state=State[ind_mat[index][0]],command=lambda: L_update_check_set_var_2(Lvar_2.get()))
    LOCK_2.grid(row=3,column=3)

    if(lock_mat[index][0]==0):
        LOCK_2.deselect()
    if(lock_mat[index][0]==1):
        LOCK_2.select()


    #CHECK_3(CHECKBOXES) 
    
    check_3=Checkbutton(root,text='',variable=var_3,state=State[ind_mat[index][1]],command=lambda: update_check_set_var_3(var_3.get()))
    check_3.grid(row=4,column=2)

    if(seg_mat[index][1]==0):
        check_3.deselect()
    if(seg_mat[index][1]==1):
        check_3.select()

    #LOCK_3(CHECKBOXES) 
   
    LOCK_3=Checkbutton(root,text='',variable=Lvar_3,state=State[ind_mat[index][1]],command=lambda: L_update_check_set_var_3(Lvar_3.get()))
    LOCK_3.grid(row=4,column=3)

    if(lock_mat[index][1]==0):
        LOCK_3.deselect()
    if(lock_mat[index][1]==1):
        LOCK_3.select()


    #CHECK_4(CHECKBOXES) 
    
    check_4=Checkbutton(root,text='',variable=var_4,state=State[ind_mat[index][2]],command=lambda: update_check_set_var_4(var_4.get()))
    check_4.grid(row=5,column=2)

    if(seg_mat[index][2]==0):
        check_4.deselect()
    if(seg_mat[index][2]==1):
        check_4.select()

    #LOCK_4(CHECKBOXES) 
    
    LOCK_4=Checkbutton(root,text='',variable=Lvar_4,state=State[ind_mat[index][2]],command=lambda: L_update_check_set_var_4(Lvar_4.get()))
    LOCK_4.grid(row=5,column=3)

    if(lock_mat[index][2]==0):
        LOCK_4.deselect()
    if(lock_mat[index][2]==1):
        LOCK_4.select()


    #CHECK_5(CHECKBOXES) 
    
    check_5=Checkbutton(root,text='',variable=var_5,state=State[ind_mat[index][3]],command=lambda: update_check_set_var_5(var_5.get()))
    check_5.grid(row=6,column=2)

    if(seg_mat[index][3]==0):
        check_5.deselect()
    if(seg_mat[index][3]==1):
        check_5.select()

    #LOCK_5(CHECKBOXES) 
    
    LOCK_5=Checkbutton(root,text='',variable=Lvar_5,state=State[ind_mat[index][3]],command=lambda: L_update_check_set_var_5(Lvar_5.get()))
    LOCK_5.grid(row=6,column=3)

    if(lock_mat[index][3]==0):
        LOCK_5.deselect()
    if(lock_mat[index][3]==1):
        LOCK_5.select()


    #CHECK_6(CHECKBOXES) 
    
    check_6=Checkbutton(root,text='',variable=var_6,state=State[ind_mat[index][4]],command=lambda: update_check_set_var_6(var_6.get()))
    check_6.grid(row=7,column=2)

    if(seg_mat[index][4]==0):
        check_6.deselect()
    if(seg_mat[index][4]==1):
        check_6.select()

    #LOCK_6(CHECKBOXES) 
    
    LOCK_6=Checkbutton(root,text='',variable=Lvar_6,state=State[ind_mat[index][4]],command=lambda: L_update_check_set_var_6(Lvar_6.get()))
    LOCK_6.grid(row=7,column=3)

    if(lock_mat[index][4]==0):
        LOCK_6.deselect()
    if(lock_mat[index][4]==1):
        LOCK_6.select()

    #CHECK_7(CHECKBOXES) 
   
    check_7=Checkbutton(root,text='',variable=var_7,state=State[ind_mat[index][5]],command=lambda: update_check_set_var_7(var_7.get()))
    check_7.grid(row=8,column=2)

    if(seg_mat[index][5]==0):
        check_7.deselect()
    if(seg_mat[index][5]==1):
        check_7.select()

    #LOCK_7(CHECKBOXES) 
  
    LOCK_7=Checkbutton(root,text='',variable=Lvar_7,state=State[ind_mat[index][5]],command=lambda: L_update_check_set_var_7(Lvar_7.get()))
    LOCK_7.grid(row=8,column=3)

    if(lock_mat[index][5]==0):
        LOCK_7.deselect()
    if(lock_mat[index][5]==1):
        LOCK_7.select()
    

    #CHECK_8(CHECKBOXES) 
   
    check_8=Checkbutton(root,text='',variable=var_8,state=State[ind_mat[index][6]],command=lambda: update_check_set_var_8(var_8.get()))
    check_8.grid(row=9,column=2)

    if(seg_mat[index][6]==0):
        check_8.deselect()
    if(seg_mat[index][6]==1):
        check_8.select()

    #LOCK_8(CHECKBOXES) 
  
    LOCK_8=Checkbutton(root,text='',variable=Lvar_8,state=State[ind_mat[index][6]],command=lambda: L_update_check_set_var_8(Lvar_8.get()))
    LOCK_8.grid(row=9,column=3)

    if(lock_mat[index][6]==0):
        LOCK_8.deselect()
    if(lock_mat[index][6]==1):
        LOCK_8.select()


    #CHECK_9(CHECKBOXES) 
   
    check_9=Checkbutton(root,text='',variable=var_9,state=State[ind_mat[index][7]],command=lambda: update_check_set_var_9(var_9.get()))
    check_9.grid(row=10,column=2)

    if(seg_mat[index][7]==0):
        check_9.deselect()
    if(seg_mat[index][7]==1):
        check_9.select()

    #LOCK_9(CHECKBOXES) 
  
    LOCK_9=Checkbutton(root,text='',variable=Lvar_9,state=State[ind_mat[index][7]],command=lambda: L_update_check_set_var_9(Lvar_9.get()))
    LOCK_9.grid(row=10,column=3)

    if(lock_mat[index][7]==0):
        LOCK_9.deselect()
    if(lock_mat[index][7]==1):
        LOCK_9.select()
    

    #CHECK_10(CHECKBOXES) 
   
    check_10=Checkbutton(root,text='',variable=var_10,state=State[ind_mat[index][8]],command=lambda: update_check_set_var_10(var_10.get()))
    check_10.grid(row=11,column=2)

    if(seg_mat[index][8]==0):
        check_10.deselect()
    if(seg_mat[index][8]==1):
        check_10.select()

    
    #LOCK_10(CHECKBOXES) 
  
    LOCK_10=Checkbutton(root,text='',variable=Lvar_10,state=State[ind_mat[index][8]],command=lambda: L_update_check_set_var_10(Lvar_10.get()))
    LOCK_10.grid(row=11,column=3)

    if(lock_mat[index][8]==0):
        LOCK_10.deselect()
    if(lock_mat[index][8]==1):
        LOCK_10.select()

    
    #CHECK_11(CHECKBOXES) 
  
    check_11=Checkbutton(root,text='',variable=var_11,state=State[ind_mat[index][9]],command=lambda: update_check_set_var_11(var_11.get()))
    check_11.grid(row=12,column=2)

    if(seg_mat[index][9]==0):
        check_11.deselect()
    if(seg_mat[index][9]==1):
        check_11.select()

    
    #LOCK_11(CHECKBOXES) 
  
    LOCK_11=Checkbutton(root,text='',variable=Lvar_11,state=State[ind_mat[index][9]],command=lambda: L_update_check_set_var_11(Lvar_11.get()))
    LOCK_11.grid(row=12,column=3)

    if(lock_mat[index][9]==0):
        LOCK_11.deselect()
    if(lock_mat[index][9]==1):
        LOCK_11.select()


    #CHECK_12(CHECKBOXES) 
   
    check_12=Checkbutton(root,text='',variable=var_12,state=State[ind_mat[index][10]],command=lambda: update_check_set_var_12(var_12.get()))
    check_12.grid(row=13,column=2)

    if(seg_mat[index][10]==0):
        check_12.deselect()
    if(seg_mat[index][10]==1):
        check_12.select()

    #LOCK_12(CHECKBOXES) 
  
    LOCK_12=Checkbutton(root,text='',variable=Lvar_12,state=State[ind_mat[index][10]],command=lambda: L_update_check_set_var_12(Lvar_12.get()))
    LOCK_12.grid(row=13,column=3)

    if(lock_mat[index][10]==0):
        LOCK_12.deselect()
    if(lock_mat[index][10]==1):
        LOCK_12.select()


    #CHECK_13(CHECKBOXES) 
  
    check_13=Checkbutton(root,text='',variable=var_13,state=State[ind_mat[index][11]],command=lambda: update_check_set_var_13(var_13.get()))
    check_13.grid(row=14,column=2)

    if(seg_mat[index][11]==0):
        check_13.deselect()
    if(seg_mat[index][11]==1):
        check_13.select()

    #LOCK_13(CHECKBOXES) 
 
    LOCK_13=Checkbutton(root,text='',variable=Lvar_13,state=State[ind_mat[index][11]],command=lambda: L_update_check_set_var_13(Lvar_13.get()))
    LOCK_13.grid(row=14,column=3)

    if(lock_mat[index][11]==0):
        LOCK_13.deselect()
    if(lock_mat[index][11]==1):
        LOCK_13.select()
    

    #CHECK_14(CHECKBOXES) 
  
    check_14=Checkbutton(root,text='',variable=var_14,state=State[ind_mat[index][12]],command=lambda: update_check_set_var_14(var_14.get()))
    check_14.grid(row=15,column=2)

    if(seg_mat[index][12]==0):
        check_14.deselect()
    if(seg_mat[index][12]==1):
        check_14.select()

    #LOCK_14(CHECKBOXES) 
   
    LOCK_14=Checkbutton(root,text='',variable=Lvar_14,state=State[ind_mat[index][12]],command=lambda: L_update_check_set_var_14(Lvar_14.get()))
    LOCK_14.grid(row=15,column=3)

    if(lock_mat[index][12]==0):
        LOCK_14.deselect()
    if(lock_mat[index][12]==1):
        LOCK_14.select()
    

    #CHECK_15(CHECKBOXES) 
   
    check_15=Checkbutton(root,text='',variable=var_15,state=State[ind_mat[index][13]],command=lambda: update_check_set_var_15(var_15.get()))
    check_15.grid(row=16,column=2)

    if(seg_mat[index][13]==0):
        check_15.deselect()
    if(seg_mat[index][13]==1):
        check_15.select()

    #LOCK_15(CHECKBOXES) 
  
    LOCK_15=Checkbutton(root,text='',variable=Lvar_15,state=State[ind_mat[index][13]],command=lambda: L_update_check_set_var_15(Lvar_15.get()))
    LOCK_15.grid(row=16,column=3)

    if(lock_mat[index][13]==0):
        LOCK_15.deselect()
    if(lock_mat[index][13]==1):
        LOCK_15.select()


    
# WHEN NEW BUTTON IS PRESSED  
def add_class():
    global ind_mat
    global num_mat

    # SETTINGS
    
    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=14,column=9,rowspan=2,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=14,column=11,rowspan=2,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=14,column=13,columnspan=3)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=15,column=13,columnspan=3)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=10, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=16,column=6,rowspan=2,columnspan=5)

    #Fix slider(BUTTON)
    fix_scale=Button(root,text=" Fix Scale",state=DISABLED)
    fix_scale.grid(row=16,column=11,rowspan=2,columnspan=5)

    #UPDATIONS
    ind_mat[index][num_mat[index]]=1
    num_mat[index]+=1
    update_check_set()

    #NEW(BUTTON)
    if(not ind_mat[index][num_class-1]):
        new=Button(root,text="New", command=add_class)
        new.grid(row=0,column=0,columnspan=2)
    else:
        new=Button(root,text="New",state=DISABLED)
        new.grid(row=0,column=0,columnspan=2)

    #DELETE(BUTTON)
    if(ind_mat[index][0]):
        delete=Button(root,text="Delete",command=delete_class)
        delete.grid(row=0,column=2,columnspan=2)
    else:
        delete=Button(root,text="Delete",state=DISABLED)
        delete.grid(row=0,column=2,columnspan=2)

    
    

def delete_class():
    global ind_mat
    global num_mat

    #SETTINGS
    
    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=14,column=9,rowspan=2,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=14,column=11,rowspan=2,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=14,column=13,columnspan=3)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=15,column=13,columnspan=3)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=10, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=16,column=6,rowspan=2,columnspan=5)

    #Fix slider(BUTTON)
    fix_scale=Button(root,text=" Fix Scale",state=DISABLED)
    fix_scale.grid(row=16,column=11,rowspan=2,columnspan=5)

    #UPDATIONS
    num_mat[index]-=1
    ind_mat[index][num_mat[index]]=0
    update_check_set()
    
    color_mask[index][num_mat[index]]=np.copy(np.zeros((npfile.shape[1],npfile.shape[2],npfile.shape[3]), np.uint8))                        
    class_mask[index][num_mat[index]]=np.copy(np.zeros((npfile.shape[1],npfile.shape[2]), np.uint8))
    npfile[index]=np.copy(copyfile[index])
    for i in range(num_mat[index]):
        npfile[index]=cv2.addWeighted(npfile[index],1,color_mask[index][i],0.4,0)
        
    c.delete("all")
    c.img= ImageTk.PhotoImage(Image.fromarray(npfile[index]))
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    
    
    #NEW(BUTTON)
    if(not ind_mat[index][num_class-1]):
        new=Button(root,text="New", command=add_class)
        new.grid(row=0,column=0,columnspan=2)
    else:
        new=Button(root,text="New",state=DISABLED)
        new.grid(row=0,column=0,columnspan=2)

    #DELETE(BUTTON)
    if(ind_mat[index][0]):
        delete=Button(root,text="Delete",command=delete_class)
        delete.grid(row=0,column=2,columnspan=2)
    else:
        delete=Button(root,text="Delete",state=DISABLED)
        delete.grid(row=0,column=2,columnspan=2)



#CLICK START
def LPOINT1(event):
    global X1
    global Y1
    global X
    global Y

    #clearing lists for new segmentation          
    lisx.clear()
    lisy.clear()
    lis.clear()
    
    #updating variables
    X1=event.x
    Y1=event.y    
    X=X1
    Y=Y1

def BPOINT1(event):
    global X1
    global Y1
    global X
    global Y
   
    #clearing lists for new segmentation          
    lisx.clear()
    lisy.clear()
    lis.clear()
    
    #updating variables
    X1=event.x
    Y1=event.y    
    X=X1
    Y=Y1

#CLICK MOTION
def LMOTION(event):
    global X
    global Y
    global w
    global h

    global trace

    #updating list
    lisx.append(X)
    lisy.append(Y)
    lis.append((X,Y))
    
    #updating variables and connecting points
    if(event.x>=0 and event.x<=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,event.x,event.y,fill="red",width=thickness)
        X=event.x
        Y=event.y
       
              
    if(event.x<=0 and event.x<=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,0,event.y,fill="red",width=thickness)
        X=0
        Y=event.y
        
    if(event.x>=0 and event.x>=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,w,event.y,fill="red",width=thickness)
        X=w-1
        Y=event.y
        
    if(event.x>=0 and event.x<=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,event.x,0,fill="red",width=thickness)
        X=event.x
        Y=0
       
    if(event.x>=0 and event.x<=w and event.y>=0 and event.y>=h):
        c.create_line(X,Y,event.x,h,fill="red",width=thickness)
        X=event.x
        Y=h-1
       
    if(event.x<=0 and event.x<=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,0,0,fill="red",width=thickness)
        X=0
        Y=0
        
    if(event.x<=0 and event.x<=w and event.y>=0 and event.y>=h):
        c.create_line(X,Y,0,h,fill="red",width=thickness)
        X=0
        Y=h-1
        
    if(event.x>=0 and event.x>=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,w,0,fill="red",width=thickness)
        X=w-1
        Y=0
        
    if(event.x>=0 and event.x>=w and event.y>=0 and event.y>=h):
       c.create_line(X,Y,w,h,fill="red",width=thickness)
       X=w-1
       Y=h-1


#CLICK MOTION
def BMOTION(event):
    global X
    global Y
    global w
    global h

    global trace
    global imcopy
    

    
    #updating variables and connecting points
    if(event.x>=0 and event.x<=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,event.x,event.y,fill="red",width=thickness)
        trace = cv2.line(trace,(X,Y),(event.x,event.y), (255, 0, 0), thickness)
        X=event.x
        Y=event.y
       
              
    if(event.x<=0 and event.x<=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,0,event.y,fill="red",width=thickness)
        trace = cv2.line(trace,(X,Y),(0,event.y), (255, 0, 0), thickness)
        X=0
        Y=event.y
        
    if(event.x>=0 and event.x>=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,w,event.y,fill="red",width=thickness)
        trace = cv2.line(trace,(X,Y),(w,event.y), (255, 0, 0), thickness)
        X=w-1
        Y=event.y
        
    if(event.x>=0 and event.x<=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,event.x,0,fill="red",width=thickness)
        trace = cv2.line(trace,(X,Y),(event.x,0), (255, 0, 0), thickness)
        X=event.x
        Y=0
       
    if(event.x>=0 and event.x<=w and event.y>=0 and event.y>=h):
        c.create_line(X,Y,event.x,h,fill="red",width=thickness)
        trace = cv2.line(trace,(X,Y),(event.x,h), (255, 0, 0), thickness)
        X=event.x
        Y=h-1
       
    if(event.x<=0 and event.x<=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,0,0,fill="red",width=thickness)
        trace = cv2.line(trace,(X,Y),(0,0), (255, 0, 0), 2)
        X=0
        Y=0
        
    if(event.x<=0 and event.x<=w and event.y>=0 and event.y>=h):
        c.create_line(X,Y,0,h,fill="red",width=thickness)
        trace = cv2.line(trace,(X,Y),(0,h), (255, 0, 0), thickness)
        X=0
        Y=h-1
        
    if(event.x>=0 and event.x>=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,w,0,fill="red",width=thickness)
        trace = cv2.line(trace,(X,Y),(w,0), (255, 0, 0), thickness)
        X=w-1
        Y=0
        
    if(event.x>=0 and event.x>=w and event.y>=0 and event.y>=h):
       c.create_line(X,Y,w,h,fill="red",width=thickness)
       trace = cv2.line(trace,(X,Y),(w,h), (255, 0, 0), thickness)
       X=w-1
       Y=h-1

              
#CLICK RELEASE
def LPOINT2(event):
    global X2
    global Y2
    global X
    global Y
    global w
    global h
    global addim
    
    global class_mask
    global copyfile
    global greyfile
    global color_mask
    global A_class_mask
    global A_color_mask
    global A_erase_mask
    global blackcv
    global cocmcv
    global clcmcv
    
    #updating variables and connecting point last and first
    i=0
    j=0
    
    X2=event.x
    Y2=event.y
    c.create_line(X1,Y1,X2,Y2,fill="red",width=thickness)
    
    imcv=np.copy(greyfile[index])# a copy of the image from which the segmentation points are chosen and added to
    erasecv=np.copy(copyfile[index])#for eraser original imgae is required
    blackcv=np.copy(npfile[index])#black erased region
    result = np.where(seg_mat[index] == 1)#serch for the index where 1 is found
    
    #arbitrary masks
    A_class_mask=np.copy(np.zeros((npfile.shape[1],npfile.shape[2]), np.uint8))
    A_color_mask=np.copy(np.zeros((npfile.shape[1],npfile.shape[2],npfile.shape[3]), np.uint8))
    A_erase_mask=np.copy(np.zeros((npfile.shape[1],npfile.shape[2],npfile.shape[3]), np.uint8))
    cocmcv=np.copy(color_mask[index][result[0][0]])
    clcmcv=np.copy(class_mask[index][result[0][0]])
    
    
    #converting the collected list to numpy array contour format
    arr = np.asarray(lis)
    lc=[arr]
    
    #Finding the internals of the drawn contour
    miny=min(lisy)
    maxy=max(lisy)
    minx=min(lisx)
    maxx=max(lisx)

    
    for i in range(minx,maxx):
        for j in range(miny,maxy):       
              if((cv2.pointPolygonTest(lc[0],(i,j),False))>0):
                  c.create_oval(i,j,i,j,fill="white")
                          
                  A_color_mask[j][i][0]=col_arr[result[0][0]][0]
                  A_color_mask[j][i][1]=col_arr[result[0][0]][1]
                  A_color_mask[j][i][2]=col_arr[result[0][0]][2]
                  
                  A_class_mask[j][i]=imcv[j][i]

                  A_erase_mask[j][i][0]=erasecv[j][i][0]
                  A_erase_mask[j][i][1]=erasecv[j][i][1]
                  A_erase_mask[j][i][2]=erasecv[j][i][2]
                  
                  blackcv[j][i][0]=0
                  blackcv[j][i][1]=0
                  blackcv[j][i][2]=0

                  cocmcv[j][i][0]=0
                  cocmcv[j][i][1]=0
                  cocmcv[j][i][2]=0

                  clcmcv[j][i]=0
    
    
    c.delete("all")
    imp=Image.fromarray(cv2.addWeighted(npfile[index],1,A_color_mask,0.4,0))
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",command=add_seg)
    plus.grid(row=14,column=13,columnspan=3)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",command=sub_seg)
    minus.grid(row=15,column=13,columnspan=3)

    deactivate()

##    #SAVE SEGMENTATION(BUTTON) *
##    saveseg=Button(root,text="Create Segmentation mask",command=segment)
##    saveseg.grid(row=5,column=2,columnspan=2)


#CLICK RELEASE
def BPOINT2(event):
    global X2
    global Y2
    global X
    global Y
    global w
    global h
    global addim
    
    global class_mask
    global copyfile
    global greyfile
    global color_mask
    global trace
    global A_class_mask
    global A_color_mask
    global A_erase_mask
    global blackcv
    global cocmcv
    global clcmcv
    
    
    
    #updating variables and connecting point last and first
    i=0
    j=0

    gray = cv2.cvtColor(trace, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    imcv=np.copy(greyfile[index])# a copy of the image from which the segmentation points are chosen and added 
    erasecv=np.copy(copyfile[index])#for eraser original imgae is required
    blackcv=np.copy(npfile[index])#black erased region

    result = np.where(seg_mat[index] == 1)#serch for the index where 1 is found

    #arbitrary masks
    A_class_mask=np.copy(np.zeros((npfile.shape[1],npfile.shape[2]), np.uint8))
    A_color_mask=np.copy(np.zeros((npfile.shape[1],npfile.shape[2],npfile.shape[3]), np.uint8))
    A_erase_mask=np.copy(np.zeros((npfile.shape[1],npfile.shape[2],npfile.shape[3]), np.uint8))
    cocmcv=np.copy(color_mask[index][result[0][0]])
    clcmcv=np.copy(class_mask[index][result[0][0]])

    #converted to list to find the max and min
    try:
        for k in range(len(contours[0])):#putting contours in the list format
            lisx.append(contours[0][k][0][0])
            lisy.append(contours[0][k][0][1])
            lis.append((contours[0][k][0][0],contours[0][i][0][1]))
    except:
        return
    
    
    #converting the collected list to numpy array contour format
    arr = np.asarray(lis)
    lc=[arr]

    
    #Finding the internals of the drawn contour
    try:
        miny=min(lisy)
        maxy=max(lisy)
        minx=min(lisx)
        maxx=max(lisx)
    except:
        miny=0
        maxy=0
        minx=0
        maxx=0
        
    
    for i in range(minx,maxx):
        for j in range(miny,maxy):
              if((cv2.pointPolygonTest(contours[0],(i,j),False))>0):
                  
                  A_color_mask[j][i][0]=col_arr[result[0][0]][0]
                  A_color_mask[j][i][1]=col_arr[result[0][0]][1]
                  A_color_mask[j][i][2]=col_arr[result[0][0]][2]
                  
                  A_class_mask[j][i]=imcv[j][i]

                  A_erase_mask[j][i][0]=erasecv[j][i][0]
                  A_erase_mask[j][i][1]=erasecv[j][i][1]
                  A_erase_mask[j][i][2]=erasecv[j][i][2]
                  
                  blackcv[j][i][0]=0
                  blackcv[j][i][1]=0
                  blackcv[j][i][2]=0

                  cocmcv[j][i][0]=0
                  cocmcv[j][i][1]=0
                  cocmcv[j][i][2]=0

                  clcmcv[j][i]=0
                  


    c.delete("all")
    imp=Image.fromarray(cv2.addWeighted(npfile[index],1,A_color_mask,0.4,0))
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",command=add_seg)
    plus.grid(row=14,column=13,columnspan=3)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",command=sub_seg)
    minus.grid(row=15,column=13,columnspan=3)
    
    deactivate()



def add_seg():
    result = np.where(seg_mat[index] == 1)#serch for the index where 1 is found
    if(lock_mat[index][result[0][0]]==0):
        color_mask[index][result[0][0]]=cv2.addWeighted(A_color_mask,1,color_mask[index][result[0][0]],1,0)                      
        class_mask[index][result[0][0]]=cv2.addWeighted(A_class_mask,1,class_mask[index][result[0][0]],1,0)
        npfile[index]=cv2.addWeighted(npfile[index],1,color_mask[index][result[0][0]],0.4,0)
        
    c.delete("all")
    c.img= ImageTk.PhotoImage(Image.fromarray(npfile[index]))
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=14,column=9,rowspan=2,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=14,column=11,rowspan=2,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=14,column=13,columnspan=3)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=15,column=13,columnspan=3)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=10, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=16,column=6,rowspan=2,columnspan=5)

    #Fix slider(BUTTON)
    fix_scale=Button(root,text=" Fix Scale",state=DISABLED)
    fix_scale.grid(row=16,column=11,rowspan=2,columnspan=5)
    
def sub_seg():
    result = np.where(seg_mat[index] == 1)#serch for the index where 1 is found
    if(lock_mat[index][result[0][0]]==0):
        color_mask[index][result[0][0]]=cv2.addWeighted(cocmcv,1,color_mask[index][result[0][0]],1,0)                          
        class_mask[index][result[0][0]]=cv2.addWeighted(clcmcv,1,class_mask[index][result[0][0]],1,0)
        npfile[index]=cv2.addWeighted(A_erase_mask,1,blackcv,1,0)
 
    c.delete("all")
    c.img= ImageTk.PhotoImage(Image.fromarray(npfile[index]))
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=14,column=9,rowspan=2,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=14,column=11,rowspan=2,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=14,column=13,columnspan=3)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=15,column=13,columnspan=3)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=10, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=16,column=6,rowspan=2,columnspan=5)

    #Fix slider(BUTTON)
    fix_scale=Button(root,text=" Fix Scale",state=DISABLED)
    fix_scale.grid(row=16,column=11,rowspan=2,columnspan=5)
    

def draw():
    #SOLID/LASSO (RADIO BUTTON)
    global c
    
    if(np.count_nonzero(seg_mat[index])==0):
       messagebox.showerror("ERROR","You have chosen 0 tissue classes for segmentation")
       return
    
    if(np.count_nonzero(seg_mat[index])!=1):
       messagebox.showerror("ERROR","You have chosen more than 1 tissue class for segmentation")
       return

    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    imp=Image.fromarray(npfile[index])
    c.delete("all")
    c= Canvas(root,height=590,width=1260,bg="white")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #Fix slider(BUTTON)
    fix_scale=Button(root,text=" Fix Scale",command=fix)
    fix_scale.grid(row=16,column=11,rowspan=2,columnspan=5)
    
    #SIZE(SLIDER)
    size=Scale(root,from_=1, to=10, variable = var,sliderlength=40,length=600, orient=HORIZONTAL)
    size.grid(row=16,column=6,rowspan=2,columnspan=5)

    
    rad1=Radiobutton(root,text="Solid",value=1,command=solid)
    rad1.grid(row=14,column=9,rowspan=2,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",value=2,command=lasso)
    rad2.grid(row=14,column=11,rowspan=2,columnspan=2)
       
    
    
def lasso():
    global thickness
    global c
    
    deactivate()
    thickness=3

    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    imp=Image.fromarray(npfile[index])
    c.delete("all")
    c= Canvas(root,height=590,width=1260,bg="white")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)


    c.bind("<Button-1>",LPOINT1)
    c.bind("<B1-Motion>",LMOTION)
    c.bind("<ButtonRelease-1>",LPOINT2)

def fix():
    global thickness
    thickness=int(1.5*var.get())

    
def solid():
    deactivate()
    global trace
    global imcopy
    global c

    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    imp=Image.fromarray(npfile[index])
    c.delete("all")
    c= Canvas(root,height=590,width=1260,bg="white")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)
    
    #create mask where the motion is traced
    trace=np.zeros((npfile.shape[1],npfile.shape[2],3), np.uint8)
    
    c.bind("<Button-1>",BPOINT1)
    c.bind("<B1-Motion>",BMOTION)
    c.bind("<ButtonRelease-1>",BPOINT2)


    

#-----------------------------------------------------NAVIGATION---------------------------------------------------------------------------------------------

#OPEN FILE
def openf():
    global back
    global front
    global status
    global c
    global brush
    global erase
    global mark
    global w
    global h
    global num
    global sind
    global new_file
    
    global count
    global class_mask
    global color_mask
    global npfile
    global flag
    global imp
    global data_size
    global index
    global ind_mat
    global seg_mat
    global lock_mat
    global num_mat
    global copyfile
    global greyfile


    if(flag==0):
        cdata = []
        data=[]
        files = glob.glob (path)
        for myFile in files:
            cimage = cv2.imread (myFile)#considering 3 channel image
            cdata.append (cv2.resize(cimage, (800,540), interpolation = cv2.INTER_AREA))
            
            image = cv2.imread (myFile,0)#considering greyscale image
            data.append (cv2.resize(image, (800,540), interpolation = cv2.INTER_AREA))
        
        npfile =np.array(cdata) #the transperent region of segmented mask is made in this and the colour mask is added over this
        copyfile =np.copy(npfile) #the actual set of images
        greyfile=np.array(data)#greyscale image lst for mask making 
        flag+=1
        data_size=len(data)
        #stores the 15 classes of tissue segmentations on one file
        class_mask = np.zeros((npfile.shape[0],num_class,npfile.shape[1],npfile.shape[2]), np.uint8)#actual Image mask
        color_mask = np.zeros((npfile.shape[0],num_class,npfile.shape[1],npfile.shape[2],npfile.shape[3]), np.uint8)#coloured mask
        # all the below three functions have 15 0s or 1s for each index of images
        # 0 corresponds to disabled/unchecked segmentation/locked
        # 1 corresponds to normal/checked/unlocked
        ind_mat = np.zeros((npfile.shape[0],num_class), np.uint8)
        seg_mat = np.zeros((npfile.shape[0],num_class), np.uint8)
        lock_mat = np.ones((npfile.shape[0],num_class), np.uint8)
        #The below will have the count for number of added materials in each image
        num_mat= np.zeros((npfile.shape[0]), np.uint8)
        
    
    
    count+=1#total number of added images
    index=count-1#index of current image
    imp=Image.fromarray(npfile[index])#Load image and convert image to PIL
    h,w,cha = npfile[index].shape


    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    c.delete("all")
    c= Canvas(root,height=590,width=1260,bg="white")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #BACKWARD(BUTTON)
    back=Button(root,text="<<", state=DISABLED)
    back.grid(row=12,column=6,columnspan=2)

    #ADD TO STACK PARAMETERSS(BUTTON) *
    if(count<data_size):
            op=Button(root,text="Add Image", command= openf)
    if(count>=data_size):
            op=Button(root,text="Add Image",state=DISABLED)
    op.grid(row=12,column=8,columnspan=3)

    #DISPLAY(BUTTON) *
    if(index+1>1):
        display=Button(root,text="display",command=lambda: forward(index+1))
        display.grid(row=12,column=11,columnspan=3)

    #FORWARD(BUTTON)
    front=Button(root,text=">>", state=DISABLED)
    front.grid(row=12,column=14,columnspan=4)

    #STATUS PARAMETERS(LABEL) *
    status=Label(root,text="image "+str(index+1)+" of "+str(count),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=13,column=6,columnspan=10)

    #SAVE SEGMENTATION(BUTTON)
    save_seg=Button(root,text="Save Segmentation",state=DISABLED)
    save_seg.grid(row=17,column=0,columnspan=2)

    #CHECKPOINT(BUTTON)
    checkpoint=Button(root,text="Checkpoint",command=save_check)
    checkpoint.grid(row=17,column=2,rowspan=2,columnspan=2)



    #NEW(BUTTON)
    if(not ind_mat[index][num_class-1]):
        new=Button(root,text="New", command=add_class)
        new.grid(row=0,column=0,columnspan=2)
    else:
        new=Button(root,text="New",state=DISABLED)
        new.grid(row=0,column=0,columnspan=2)

    #DELETE(BUTTON)
    if(ind_mat[index][0]):
        delete=Button(root,text="Delete",command=delete_class)
        delete.grid(row=0,column=2,columnspan=2)
    else:
        delete=Button(root,text="Delete",state=DISABLED)
        delete.grid(row=0,column=2,columnspan=2)

    #BRUSH(BUTTON)
    brush=Button(root,text="Brush",command=draw)
    brush.grid(row=14,column=6,rowspan=2,columnspan=3)

    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=14,column=9,rowspan=2,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=14,column=11,rowspan=2,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=14,column=13,columnspan=3)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=15,column=13,columnspan=3)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=10, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=16,column=6,rowspan=2,columnspan=5)

    #Fix slider(BUTTON)
    fix_scale=Button(root,text=" Fix Scale",state=DISABLED)
    fix_scale.grid(row=16,column=11,rowspan=2,columnspan=5)

    #Set the checkboxes of segmentations and locks
    update_check_set()
    
    #Keep the mouse keys unbinded
    deactivate()

    #print("index:",index," seg: ",seg_mat[index]," lock: ",lock_mat[index])

    

    
#FORWARD KEY
def forward(num):
    global back
    global front
    global status
    global display
    global brush
    global c
    global erase
    global mark
    global w
    global h
    global sind

    global count
    global class_mask
    global color_mask
    global npfile
    global flag
    global imp
    global data_size
    global index
    global ind_mat
    global seg_mat
    global lock_mat
    global num_mat
    global copyfile
    global greyfile

    index=num-1#updation of index
    
    imp=Image.fromarray(npfile[num-1])
    h,w,cha= npfile[index].shape
    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    c.delete("all")
    c= Canvas(root,height=590,width=1260,bg="white")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #BACKWARD(BUTTON)
    back=Button(root,text="<<", command=lambda: backward(num-1))
    back.grid(row=12,column=6,columnspan=2)

    #ADD TO STACK PARAMETERSS(BUTTON) *
    if(count<data_size):
            op=Button(root,text="Add Image", command= openf)
    if(count>=data_size):
            op=Button(root,text="Add Image",state=DISABLED)
    op.grid(row=12,column=8,columnspan=3)

    #DISPLAY(BUTTON)
    display=Button(root,text="display",state=DISABLED)
    display.grid(row=12,column=11,columnspan=3)

    #FORWARD(BUTTON)
    front=Button(root,text=">>",command=lambda: forward(num+1))
    if num==count:
        front=Button(root,text=">>",state=DISABLED)
    front.grid(row=12,column=14,columnspan=4)

    #STATUS PARAMETERS(LABEL) *
    status=Label(root,text="image "+str(num)+" of "+str(count),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=13,column=6,columnspan=10)




    #NEW(BUTTON)
    if(not ind_mat[index][num_class-1]):
        new=Button(root,text="New", command=add_class)
        new.grid(row=0,column=0,columnspan=2)
    else:
        new=Button(root,text="New",state=DISABLED)
        new.grid(row=0,column=0,columnspan=2)

    #DELETE(BUTTON)
    if(ind_mat[index][0]):
        delete=Button(root,text="Delete",command=delete_class)
        delete.grid(row=0,column=2,columnspan=2)
    else:
        delete=Button(root,text="Delete",state=DISABLED)
        delete.grid(row=0,column=2,columnspan=2)

        
    #SAVE SEGMENTATION(BUTTON)
    save_seg=Button(root,text="Save Segmentation",state=DISABLED)
    save_seg.grid(row=17,column=0,columnspan=2)

    #CHECKPOINT(BUTTON)
    checkpoint=Button(root,text="Checkpoint",command=save_check)
    checkpoint.grid(row=17,column=2,rowspan=2,columnspan=2)



    #BRUSH(BUTTON)
    brush=Button(root,text="Brush",command=draw)
    brush.grid(row=14,column=6,rowspan=2,columnspan=3)

    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=14,column=9,rowspan=2,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=14,column=11,rowspan=2,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=14,column=13,columnspan=3)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=15,column=13,columnspan=3)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=10, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=16,column=6,rowspan=2,columnspan=5)

    #Fix slider(BUTTON)
    fix_scale=Button(root,text=" Fix Scale",state=DISABLED)
    fix_scale.grid(row=16,column=11,rowspan=2,columnspan=5)

    #Set the checkboxes of segmentations and locks
    update_check_set()
    
    #Keep the mouse keys unbinded
    deactivate()
    #print("index:",index," seg: ",seg_mat[index]," lock: ",lock_mat[index])
   


#BACKWARD KEY
def backward(num):
    global back
    global front
    global status
    global display
    global brush
    global c
    global erase
    global mark
    global ind
    global w
    global h
    global sind

    global count
    global class_mask
    global color_mask
    global npfile
    global flag
    global imp
    global data_size
    global index
    global ind_mat
    global seg_mat
    global lock_mat
    global num_mat
    global copyfile
    global greyfile
    
    index=num-1#updation of index
    
    imp=Image.fromarray(npfile[num-1])
    h,w,cha= npfile[index].shape
    
    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    c.delete("all")
    c= Canvas(root,height=590,width=1260,bg="white")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #BACKWARD(BUTTON)
    back=Button(root,text="<<", command=lambda: backward(num-1))
    if num==1:
        back=Button(root,text="<<",state=DISABLED)
    back.grid(row=12,column=6,columnspan=2)

    #ADD TO STACK PARAMETERSS(BUTTON) *
    if(count<data_size):
            op=Button(root,text="Add Image", command= openf)
    if(count>=data_size):
            op=Button(root,text="Add Image",state=DISABLED)
    op.grid(row=12,column=8,columnspan=3)

    #DISPLAY(BUTTON)
    display=Button(root,text="display",state=DISABLED)
    display.grid(row=12,column=11,columnspan=3)

    #FORWARD(BUTTON)
    front=Button(root,text=">>",command=lambda: forward(num+1))
    if num==count:
        front=Button(root,text=">>",state=DISABLED)
    front.grid(row=12,column=14,columnspan=4)

    #STATUS PARAMETERS(LABEL) *                           
    status=Label(root,text="image "+str(num)+" of "+str(count),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=13,column=6,columnspan=10)



    #NEW(BUTTON)
    if(not ind_mat[index][num_class-1]):
        new=Button(root,text="New", command=add_class)
        new.grid(row=0,column=0,columnspan=2)
    else:
        new=Button(root,text="New",state=DISABLED)
        new.grid(row=0,column=0,columnspan=2)

    #DELETE(BUTTON)
    if(ind_mat[index][0]):
        delete=Button(root,text="Delete",command=delete_class)
        delete.grid(row=0,column=2,columnspan=2)
    else:
        delete=Button(root,text="Delete",state=DISABLED)
        delete.grid(row=0,column=2,columnspan=2)
        

    #SAVE SEGMENTATION(BUTTON)
    save_seg=Button(root,text="Save Segmentation",state=DISABLED)
    save_seg.grid(row=17,column=0,columnspan=2)

    #CHECKPOINT(BUTTON)
    checkpoint=Button(root,text="Checkpoint",command=save_check)
    checkpoint.grid(row=17,column=2,rowspan=2,columnspan=2)





    #BRUSH(BUTTON)
    brush=Button(root,text="Brush",command=draw)
    brush.grid(row=14,column=6,rowspan=2,columnspan=3)

    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=14,column=9,rowspan=2,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=14,column=11,rowspan=2,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=14,column=13,columnspan=3)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=15,column=13,columnspan=3)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=10, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=16,column=6,rowspan=2,columnspan=5)

    #Fix slider(BUTTON)
    fix_scale=Button(root,text=" Fix Scale",state=DISABLED)
    fix_scale.grid(row=16,column=11,rowspan=2,columnspan=5)

    #Set the checkboxes of segmentations and locks
    update_check_set()

    #Keep the mouse keys unbinded
    deactivate()
    #print("index:",index," seg: ",seg_mat[index]," lock: ",lock_mat[index])
    
#---------------------------------------OTHER FUNCTION-----------------------------------------------------------------------------------------------------------
#ALL MOUSE DEACTIVATION
def deactivate():
    c.unbind("<Button-1>")
    c.unbind("<B1-Motion>")
    c.unbind("<ButtonRelease-1>")

#CHECKPOINT
def save_check():
    return
    

#------------------------END OF FUNCTIONS-------------------------------------------------------------------------------------------------------------------------


#WIDGETS
#*-Activated, else DISABLED

#NEW(BUTTON)
new=Button(root,text="New", state=DISABLED)
new.grid(row=0,column=0,columnspan=2)

#DELETE(BUTTON)
delete=Button(root,text="Delete",state=DISABLED)
delete.grid(row=0,column=2,columnspan=2)

#SAVE SEGMENTATION(BUTTON)
save_seg=Button(root,text="Save Segmentation",state=DISABLED)
save_seg.grid(row=17,column=0,columnspan=2,rowspan=2)

#CHECKPOINT(BUTTON)
checkpoint=Button(root,text="Checkpoint",state=DISABLED)
checkpoint.grid(row=17,column=2,columnspan=2,rowspan=2)





#BRUSH(BUTTON)
brush=Button(root,text="Brush",state=DISABLED)
brush.grid(row=14,column=6,rowspan=2,columnspan=3)

#SOLID/LASSO (RADIO BUTTON)
r=IntVar()
rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
rad1.grid(row=14,column=9,rowspan=2,columnspan=2)
rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
rad2.grid(row=14,column=11,rowspan=2,columnspan=2)
       
#ADD SEGMENTATION(BUTTON)
plus=Button(root,text="     +++   ",state=DISABLED)
plus.grid(row=14,column=13,columnspan=3)

#ERASE SEGMENTATION(BUTTON)
minus=Button(root,text="      ---      ",state=DISABLED)
minus.grid(row=15,column=13,columnspan=3)

#SIZE(SLIDER)
var = DoubleVar()
size=Scale(root,from_=1, to=10, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
size.grid(row=16,column=6,rowspan=2,columnspan=5)

#Fix slider(BUTTON)
fix_scale=Button(root,text=" Fix Scale",state=DISABLED)
fix_scale.grid(row=16,column=11,rowspan=2,columnspan=5)




#IMAGE BACKGROUND PARAMETERS(CANVAS) *
c= Canvas(root,height=590,width=1260,bg="white")
c.grid(row=0,column=6,rowspan=12,columnspan=10)

#BACKWARD(BUTTON)
back=Button(root,text="<<", state=DISABLED)
back.grid(row=12,column=6,columnspan=2)

#ADD TO STACK PARAMETERSS(BUTTON) *
op=Button(root,text="Add Image",command= openf)
op.grid(row=12,column=8,columnspan=3)

#DISPLAY(BUTTON)
display=Button(root,text="display",state='disabled')
display.grid(row=12,column=11,columnspan=3)

#FORWARD(BUTTON)
front=Button(root,text=">>", state=DISABLED)
front.grid(row=12,column=14,columnspan=4)

#STATUS PARAMETERS(LABEL) *                           
status=Label(root,text="",bd=1,relief=SUNKEN,anchor=E)
status.grid(row=13,column=6,columnspan=10)














#COLOR(LABELS) *
color=Label(root,text="Color",bd=1,relief=SUNKEN)
color.grid(row=1,column=0)

#CLASS NAME(LABELS) *
class_name=Label(root,text="Class Name",bd=1,relief=SUNKEN)
class_name.grid(row=1,column=1)

#SEGMENTATION(LABELS) *
segmentation=Label(root,text="Segmentation",bd=1,relief=SUNKEN)
segmentation.grid(row=1,column=2)

#LOCK(LABELS) *
color=Label(root,text="Lock",bd=1,relief=SUNKEN)
color.grid(row=1,column=3)





# "#fff" is white, "#000000" is black, "#000fff000" is pure green, and "#00ffff" is pure cyan
 
#COLOR_1(LABELS) *
color_1=Label(root,text="NONE",bd=1)
color_1.grid(row=2,column=0)

#EXTERNAL TISSUE(LABELS) *
external_tissue=Label(root,text="External_Tissue",bd=1)
external_tissue.grid(row=2,column=1)

#COLOR_2(LABELS) *
color_2=Label(root,text="light green",bd=1)
color_2.grid(row=3,column=0)

#TISSUE_1(LABELS) *
tissue_1=Label(root,text="Tissue_1",bd=1)
tissue_1.grid(row=3,column=1)

#COLOR_3(LABELS) *
color_3=Label(root,text="pink",bd=1)
color_3.grid(row=4,column=0)

#TISSUE_2(LABELS) *
tissue_2=Label(root,text="Tissue_2",bd=1)
tissue_2.grid(row=4,column=1)

#COLOR_4(LABELS) *
color_4=Label(root,text="sky blue",bd=1)
color_4.grid(row=5,column=0)

#TISSUE_3(LABELS) *
tissue_3=Label(root,text="Tissue_3",bd=1)
tissue_3.grid(row=5,column=1)

#COLOR_5(LABELS) *
color_5=Label(root,text="violet",bd=1)
color_5.grid(row=6,column=0)

#TISSUE_4(LABELS) *
tissue_4=Label(root,text="Tissue_4",bd=1)
tissue_4.grid(row=6,column=1)

#COLOR_6(LABELS) *
color_6=Label(root,text="dark green",bd=1)
color_6.grid(row=7,column=0)

#TISSUE_5(LABELS) *
tissue_5=Label(root,text="Tissue_5",bd=1)
tissue_5.grid(row=7,column=1)

#COLOR_7(LABELS) *
color_7=Label(root,text="ink blue",bd=1)
color_7.grid(row=8,column=0)

#TISSUE_6(LABELS) *
tissue_6=Label(root,text="Tissue_6",bd=1)
tissue_6.grid(row=8,column=1)

#COLOR_8(LABELS) *
color_8=Label(root,text="dark blue",bd=1)
color_8.grid(row=9,column=0)

#TISSUE_7(LABELS) *
tissue_7=Label(root,text="Tissue_7",bd=1)
tissue_7.grid(row=9,column=1)

#COLOR_9(LABELS) *
color_9=Label(root,text="red",bd=1)
color_9.grid(row=10,column=0)

#TISSUE_8(LABELS) *
tissue_8=Label(root,text="Tissue_8",bd=1)
tissue_8.grid(row=10,column=1)

#COLOR_10(LABELS) *
color_10=Label(root,text="Brown",bd=1)
color_10.grid(row=11,column=0)

#TISSUE_9(LABELS) *
tissue_9=Label(root,text="Tissue_9",bd=1)
tissue_9.grid(row=11,column=1)

#COLOR_11(LABELS) *
color_11=Label(root,text="dark cyan",bd=1)
color_11.grid(row=12,column=0)

#TISSUE_10(LABELS) *
tissue_10=Label(root,text="Tissue_10",bd=1)
tissue_10.grid(row=12,column=1)

#COLOR_12(LABELS) *
color_12=Label(root,text="medium cyan",bd=1)
color_12.grid(row=13,column=0)

#TISSUE_11(LABELS) *
tissue_11=Label(root,text="Tissue_11",bd=1)
tissue_11.grid(row=13,column=1)

#COLOR_13(LABELS) *
color_13=Label(root,text="light cyan",bd=1)
color_13.grid(row=14,column=0)

#TISSUE_12(LABELS) *
tissue_12=Label(root,text="Tissue_!2",bd=1)
tissue_12.grid(row=14,column=1)

#COLOR_14(LABELS) *
color_14=Label(root,text="yellow",bd=1)
color_14.grid(row=15,column=0)

#TISSUE_13(LABELS) *
tissue_13=Label(root,text="Tissue_13",bd=1)
tissue_13.grid(row=15,column=1)

#COLOR_15(LABELS) *
color_15=Label(root,text="purple",bd=1)
color_15.grid(row=16,column=0)

#TISSUE_14(LABELS) *
tissue_14=Label(root,text="Tissue_14",bd=1)
tissue_14.grid(row=16,column=1)

#color initialization
col_arr=np.zeros((15,3), np.uint8)

#light green
col_arr[0][0]=0
col_arr[0][1]=255
col_arr[0][2]=0

#pink
col_arr[1][0]=255
col_arr[1][1]=0
col_arr[1][2]=180

#sky blue
col_arr[2][0]=120
col_arr[2][1]=200
col_arr[2][2]=255

#violet
col_arr[3][0]=127
col_arr[3][1]=0
col_arr[3][2]=255

#dark green
col_arr[4][0]=0
col_arr[4][1]=127
col_arr[4][2]=0

#
col_arr[5][0]=0
col_arr[5][1]=0
col_arr[5][2]=255

col_arr[6][0]=0
col_arr[6][1]=0
col_arr[6][2]=127

col_arr[7][0]=255
col_arr[7][1]=0
col_arr[7][2]=0

col_arr[8][0]=127
col_arr[8][1]=0
col_arr[8][2]=0

col_arr[9][0]=0
col_arr[9][1]=127
col_arr[9][2]=255

col_arr[10][0]=0
col_arr[10][1]=180
col_arr[10][2]=255

col_arr[11][0]=0
col_arr[11][1]=255
col_arr[11][2]=255

col_arr[12][0]=255
col_arr[12][1]=255
col_arr[12][2]=0

col_arr[13][0]=255
col_arr[13][1]=0
col_arr[13][2]=255


var = DoubleVar()


var_2= IntVar()
Lvar_2= IntVar()
var_3= IntVar()
Lvar_3= IntVar()
var_4= IntVar()
Lvar_4= IntVar()
var_5= IntVar()
Lvar_5= IntVar()
var_6= IntVar()
Lvar_6= IntVar()
var_7= IntVar()
Lvar_7= IntVar()
var_8= IntVar()
Lvar_8= IntVar()
var_9= IntVar()
Lvar_9= IntVar()
var_10= IntVar()
Lvar_10= IntVar()
var_11= IntVar()
Lvar_11= IntVar()
var_12= IntVar()
Lvar_12= IntVar()
var_13= IntVar()
Lvar_13= IntVar()
var_14= IntVar()
Lvar_14= IntVar()
var_15= IntVar()
Lvar_15= IntVar()



#CHECK_1(CHECKBOXES)
check_1=Checkbutton(root,text='',state=DISABLED)
check_1.select()
check_1.grid(row=2,column=2)

#CHECK_2(CHECKBOXES)
check_2=Checkbutton(root,text='',state=DISABLED)
check_2.grid(row=3,column=2)

#CHECK_3(CHECKBOXES) 
check_3=Checkbutton(root,text='',state=DISABLED)
check_3.grid(row=4,column=2)

#CHECK_4(CHECKBOXES)
check_4=Checkbutton(root,text='',state=DISABLED)
check_4.grid(row=5,column=2)

#CHECK_5(CHECKBOXES) 
check_5=Checkbutton(root,text='',state=DISABLED)
check_5.grid(row=6,column=2)

#CHECK_6(CHECKBOXES)
check_6=Checkbutton(root,text='',state=DISABLED)
check_6.grid(row=7,column=2)

#CHECK_7(CHECKBOXES)
check_7=Checkbutton(root,text='',state=DISABLED)
check_7.grid(row=8,column=2)

#CHECK_8(CHECKBOXES) 
check_8=Checkbutton(root,text='',state=DISABLED)
check_8.grid(row=9,column=2)

#CHECK_9(CHECKBOXES) 
check_=Checkbutton(root,text='',state=DISABLED)
check_.grid(row=10,column=2)

#CHECK_10(CHECKBOXES)
check_10=Checkbutton(root,text='',state=DISABLED)
check_10.grid(row=11,column=2)

#CHECK_11(CHECKBOXES)
check_11=Checkbutton(root,text='',state=DISABLED)
check_11.grid(row=12,column=2)

#CHECK_12(CHECKBOXES) 
check_12=Checkbutton(root,text='',state=DISABLED)
check_12.grid(row=13,column=2)

#CHECK_13(CHECKBOXES)
check_13=Checkbutton(root,text='',state=DISABLED)
check_13.grid(row=14,column=2)

#CHECK_14(CHECKBOXES)
check_14=Checkbutton(root,text='',state=DISABLED)
check_14.grid(row=15,column=2)

#CHECK_15(CHECKBOXES)
check_15=Checkbutton(root,text='',state=DISABLED)
check_15.grid(row=16,column=2)









#LOCK_1(CHECKBOXES)
LOCK_1=Checkbutton(root,text='',state=DISABLED)
LOCK_1.select()
LOCK_1.grid(row=2,column=3)

#LOCK_2(CHECKBOXES)
LOCK_2=Checkbutton(root,text='',state=DISABLED)
LOCK_2.select()
LOCK_2.grid(row=3,column=3)

#LOCK_3(CHECKBOXES)
LOCK_3=Checkbutton(root,text='',state=DISABLED)
LOCK_3.select()
LOCK_3.grid(row=4,column=3)

#LOCK_4(CHECKBOXES)
LOCK_4=Checkbutton(root,text='',state=DISABLED)
LOCK_4.select()
LOCK_4.grid(row=5,column=3)

#LOCK_5(CHECKBOXES)
LOCK_5=Checkbutton(root,text='',state=DISABLED)
LOCK_5.select()
LOCK_5.grid(row=6,column=3)

#LOCK_6(CHECKBOXES)
LOCK_6=Checkbutton(root,text='',state=DISABLED)
LOCK_6.select()
LOCK_6.grid(row=7,column=3)

#LOCK_7(CHECKBOXES) 
LOCK_7=Checkbutton(root,text='',state=DISABLED)
LOCK_7.select()
LOCK_7.grid(row=8,column=3)

#LOCK_8(CHECKBOXES) 
LOCK_8=Checkbutton(root,text='',state=DISABLED)
LOCK_8.select()
LOCK_8.grid(row=9,column=3)

#LOCK_9(CHECKBOXES) 
LOCK_9=Checkbutton(root,text='',state=DISABLED)
LOCK_9.select()
LOCK_9.grid(row=10,column=3)

#LOCK_10(CHECKBOXES) 
LOCK_10=Checkbutton(root,text='',state=DISABLED)
LOCK_10.select()
LOCK_10.grid(row=11,column=3)

#LOCK_11(CHECKBOXES) 
LOCK_11=Checkbutton(root,text='',state=DISABLED)
LOCK_11.select()
LOCK_11.grid(row=12,column=3)

#LOCK_12(CHECKBOXES) 
LOCK_12=Checkbutton(root,text='',state=DISABLED)
LOCK_12.select()
LOCK_12.grid(row=13,column=3)

#LOCK_13(CHECKBOXES) 
LOCK_13=Checkbutton(root,text='',state=DISABLED)
LOCK_13.select()
LOCK_13.grid(row=14,column=3)

#LOCK_14(CHECKBOXES) 
LOCK_14=Checkbutton(root,text='',state=DISABLED)
LOCK_14.select()
LOCK_14.grid(row=15,column=3)

#LOCK_15(CHECKBOXES) 
LOCK_15=Checkbutton(root,text='',state=DISABLED)
LOCK_15.select()
LOCK_15.grid(row=16,column=3)


root.mainloop()

