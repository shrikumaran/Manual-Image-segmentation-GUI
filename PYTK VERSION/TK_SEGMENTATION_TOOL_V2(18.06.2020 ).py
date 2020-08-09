# AUTHOR: V.K.VIEKASH
# LAST UPDATED ON: 18/06/2020 

##################################### packages ###############################################################################################################
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from PIL import ImageTk,Image
import cv2
import numpy as np
import os

###################################### Variable initialisation ###########################################################################################################

num_class=6
State = {0: 'disabled', 1: "normal"}
thickness=3# default thickness of the brush
w=800#width of canvas
h=450#height of canvas
time=0
u_ptr=0

####################################### LISTS #####################################################################################################################
lisx=[]
lisy=[]
lis=[]
col_arr=[]
u_stack=[]

##################################ROOT PARAMETERS##########################################################################################################
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

W=1090
H=620

root.geometry(str(W)+"x"+str(H)+"+"+str(R)+"+"+str(D))#("window width x window height + position right + position down")
#root.resizable(width=False,height=False)#TO NOT ALLOW SCREEN RESIZING
root.title('TK_SEGMENTATION_TOOL_V2')
root.iconbitmap("icon.ico")


#--------------------------------------------------------------FUNCTIONS-------------------------------------------------------------------------------

####################################CHECKBOX UPDATION FUNCTIONS###########################################################################################

# A SERIES OF FUNCTIONS THAT WILL SET THE SEHMENTATION AND LOCK CHECK BOXES AS WE CHANGE IMAGES
def update_check_set_var_2(value):
    seg_mat[0]=value
    
def L_update_check_set_var_2(value):
   lock_mat[0]=value

def update_check_set_var_3(value):
    seg_mat[1]=value
    
def L_update_check_set_var_3(value):
   lock_mat[1]=value

def update_check_set_var_4(value):
    seg_mat[2]=value
    
def L_update_check_set_var_4(value):
   lock_mat[2]=value

def update_check_set_var_5(value):
    seg_mat[3]=value
    
def L_update_check_set_var_5(value):
   lock_mat[3]=value

def update_check_set_var_6(value):
    seg_mat[4]=value
    
def L_update_check_set_var_6(value):
   lock_mat[4]=value

def update_check_set_var_7(value):
    seg_mat[5]=value
    
def L_update_check_set_var_7(value):
   lock_mat[5]=value

def update_check_set_var_8(value):
    seg_mat[6]=value
    
def L_update_check_set_var_8(value):
   lock_mat[6]=value

def update_check_set_var_9(value):
    seg_mat[7]=value
    
def L_update_check_set_var_9(value):
   lock_mat[7]=value

def update_check_set_var_10(value):
    seg_mat[8]=value
    
def L_update_check_set_var_10(value):
   lock_mat[8]=value

def update_check_set_var_11(value):
    seg_mat[9]=value
    
def L_update_check_set_var_11(value):
   lock_mat[9]=value

def update_check_set_var_12(value):
    seg_mat[10]=value
    
def L_update_check_set_var_12(value):
   lock_mat[10]=value

def update_check_set_var_13(value):
    seg_mat[11]=value
    
def L_update_check_set_var_13(value):
   lock_mat[11]=value

def update_check_set_var_14(value):
    seg_mat[12]=value
    
def L_update_check_set_var_14(value):
   lock_mat[12]=value

def update_check_set_var_15(value):
    seg_mat[13]=value
    
def L_update_check_set_var_15(value):
   lock_mat[13]=value


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
   
    check_2=Checkbutton(root,text='',variable=var_2,state=State[ind_mat[0]],command=lambda: update_check_set_var_2(var_2.get()))

    if(seg_mat[0]==0):
        check_2.deselect()
    if(seg_mat[0]==1):
        check_2.select()
        
    check_2.grid(row=3,column=2)

    #LOCK_2(CHECKBOXES) 
   
    LOCK_2=Checkbutton(root,text='',variable=Lvar_2,state=State[ind_mat[0]],command=lambda: L_update_check_set_var_2(Lvar_2.get()))
    LOCK_2.grid(row=3,column=3)

    if(lock_mat[0]==0):
        LOCK_2.deselect()
    if(lock_mat[0]==1):
        LOCK_2.select()


    #CHECK_3(CHECKBOXES) 
    
    check_3=Checkbutton(root,text='',variable=var_3,state=State[ind_mat[1]],command=lambda: update_check_set_var_3(var_3.get()))
    check_3.grid(row=4,column=2)

    if(seg_mat[1]==0):
        check_3.deselect()
    if(seg_mat[1]==1):
        check_3.select()

    #LOCK_3(CHECKBOXES) 
   
    LOCK_3=Checkbutton(root,text='',variable=Lvar_3,state=State[ind_mat[1]],command=lambda: L_update_check_set_var_3(Lvar_3.get()))
    LOCK_3.grid(row=4,column=3)

    if(lock_mat[1]==0):
        LOCK_3.deselect()
    if(lock_mat[1]==1):
        LOCK_3.select()


    #CHECK_4(CHECKBOXES) 
    
    check_4=Checkbutton(root,text='',variable=var_4,state=State[ind_mat[2]],command=lambda: update_check_set_var_4(var_4.get()))
    check_4.grid(row=5,column=2)

    if(seg_mat[2]==0):
        check_4.deselect()
    if(seg_mat[2]==1):
        check_4.select()

    #LOCK_4(CHECKBOXES) 
    
    LOCK_4=Checkbutton(root,text='',variable=Lvar_4,state=State[ind_mat[2]],command=lambda: L_update_check_set_var_4(Lvar_4.get()))
    LOCK_4.grid(row=5,column=3)

    if(lock_mat[2]==0):
        LOCK_4.deselect()
    if(lock_mat[2]==1):
        LOCK_4.select()


    #CHECK_5(CHECKBOXES) 
    
    check_5=Checkbutton(root,text='',variable=var_5,state=State[ind_mat[3]],command=lambda: update_check_set_var_5(var_5.get()))
    check_5.grid(row=6,column=2)

    if(seg_mat[3]==0):
        check_5.deselect()
    if(seg_mat[3]==1):
        check_5.select()

    #LOCK_5(CHECKBOXES) 
    
    LOCK_5=Checkbutton(root,text='',variable=Lvar_5,state=State[ind_mat[3]],command=lambda: L_update_check_set_var_5(Lvar_5.get()))
    LOCK_5.grid(row=6,column=3)

    if(lock_mat[3]==0):
        LOCK_5.deselect()
    if(lock_mat[3]==1):
        LOCK_5.select()


    #CHECK_6(CHECKBOXES) 
    
    check_6=Checkbutton(root,text='',variable=var_6,state=State[ind_mat[4]],command=lambda: update_check_set_var_6(var_6.get()))
    check_6.grid(row=7,column=2)

    if(seg_mat[4]==0):
        check_6.deselect()
    if(seg_mat[4]==1):
        check_6.select()

    #LOCK_6(CHECKBOXES) 
    
    LOCK_6=Checkbutton(root,text='',variable=Lvar_6,state=State[ind_mat[4]],command=lambda: L_update_check_set_var_6(Lvar_6.get()))
    LOCK_6.grid(row=7,column=3)

    if(lock_mat[4]==0):
        LOCK_6.deselect()
    if(lock_mat[4]==1):
        LOCK_6.select()

    #CHECK_7(CHECKBOXES) 
   
    check_7=Checkbutton(root,text='',variable=var_7,state=State[ind_mat[5]],command=lambda: update_check_set_var_7(var_7.get()))
    check_7.grid(row=8,column=2)

    if(seg_mat[5]==0):
        check_7.deselect()
    if(seg_mat[5]==1):
        check_7.select()

    #LOCK_7(CHECKBOXES) 
  
    LOCK_7=Checkbutton(root,text='',variable=Lvar_7,state=State[ind_mat[5]],command=lambda: L_update_check_set_var_7(Lvar_7.get()))
    LOCK_7.grid(row=8,column=3)

    if(lock_mat[5]==0):
        LOCK_7.deselect()
    if(lock_mat[5]==1):
        LOCK_7.select()

################################################################# MATERIAL ADD AND DELETE FUNCTION ###########################################################3
    
# WHEN NEW BUTTON IS PRESSED  
def add_class():
    global ind_mat
    global num_mat
    global col_arr

    # SETTINGS

    #SET COLOR
    my_color=colorchooser.askcolor()
    col_arr.append(my_color[0])
    
    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=9,column=1,rowspan=1,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=10,column=1,rowspan=1,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=9,column=3,columnspan=1)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=10,column=3,columnspan=1)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=50, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=12,column=6,rowspan=1,columnspan=1)

    #Fix slider(BUTTON)
    fix_scale=Button(root,text=" Fix Scale",state=DISABLED)
    fix_scale.grid(row=12,column=0,rowspan=1,columnspan=3)

    #UPDATIONS
    ind_mat[num_mat]=1
    num_mat+=1
    update_check_set()

    #NEW(BUTTON)
    if(not ind_mat[num_class-1]):
        new=Button(root,text="New", command=add_class)
        new.grid(row=0,column=0,columnspan=2)
    else:
        new=Button(root,text="New",state=DISABLED)
        new.grid(row=0,column=0,columnspan=2)

    #DELETE(BUTTON)
    if(ind_mat[0]):
        delete=Button(root,text="Delete",command=delete_class)
        delete.grid(row=0,column=2,columnspan=2)
    else:
        delete=Button(root,text="Delete",state=DISABLED)
        delete.grid(row=0,column=2,columnspan=2)

    
    
# WHEN DELETE BUTTON IS PRESSED  
def delete_class():
    global ind_mat
    global num_mat
    global encoded_mask
    global col_arr
    
    #SETTINGS
    
    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=9,column=1,rowspan=1,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=10,column=1,rowspan=1,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=9,column=3,columnspan=1)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=10,column=3,columnspan=1)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=50, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=12,column=6,rowspan=1,columnspan=1)

    #Fix slider(BUTTON)
    fix_scale=Button(root,text=" Fix Scale",state=DISABLED)
    fix_scale.grid(row=12,column=0,rowspan=1,columnspan=3)

    #UPDATIONS
    num_mat-=1
    ind_mat[num_mat]=0

    seg_mat[num_mat]=0
    lock_mat[num_mat]=1

    #pop the last element of the color array:
    col_arr.pop(num_mat)
    
    find=np.where(encoded_mask==num_mat+1)
    X=list(find[1])
    Y=list(find[0])
    for k in range(len(X)):
            encoded_mask[Y[k]][X[k]]=0

    update_mask()
    update_check_set()
    
    c.delete("all")
    c.img= ImageTk.PhotoImage(Image.fromarray(npfile))
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    
    
    #NEW(BUTTON)
    if(not ind_mat[num_class-1]):
        new=Button(root,text="New", command=add_class)
        new.grid(row=0,column=0,columnspan=2)
    else:
        new=Button(root,text="New",state=DISABLED)
        new.grid(row=0,column=0,columnspan=2)

    #DELETE(BUTTON)
    if(ind_mat[0]):
        delete=Button(root,text="Delete",command=delete_class)
        delete.grid(row=0,column=2,columnspan=2)
    else:
        delete=Button(root,text="Delete",state=DISABLED)
        delete.grid(row=0,column=2,columnspan=2)


################################################################ DRAWING FUCTION #######################################################################

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
    global A_encoded_mask
    global E_encoded_mask
    
    #updating variables and connecting point last and first
    i=0
    j=0
    
    X2=event.x
    Y2=event.y
    c.create_line(X1,Y1,X2,Y2,fill="red",width=thickness)
    
    result = np.where(seg_mat == 1)#serch for the index where 1 is found

    #arbitrary masks
    A_encoded_mask=np.copy(encoded_mask)  
    E_encoded_mask=np.copy(encoded_mask)  
    
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
                    if(encoded_mask[j][i]==0 or check_open(encoded_mask[j][i])):
                        A_encoded_mask[j][i]=result[0][0]+1
                        E_encoded_mask[j][i]=0

    
    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",command=add_seg)
    plus.grid(row=9,column=3,columnspan=1)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",command=sub_seg)
    minus.grid(row=10,column=3,columnspan=1)

    deactivate()




#CLICK RELEASE
def BPOINT2(event):
    global X2
    global Y2
    global X
    global Y
    global w
    global h
    global trace
    global A_encoded_mask
    global E_encoded_mask
    
    
    #updating variables and connecting point last and first
    i=0
    j=0

    result = np.where(seg_mat == 1)#serch for the index where 1 is found

    #arbitrary masks
    A_encoded_mask=np.copy(encoded_mask)  
    E_encoded_mask=np.copy(encoded_mask)
    
    gray = cv2.cvtColor(trace, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #converted to list to find the max and min
    try:
        for k in range(len(contours[0])):#putting contours in the list format
            lisx.append(contours[0][k][0][0])
            lisy.append(contours[0][k][0][1])
            lis.append((contours[0][k][0][0],contours[0][i][0][1]))
            
    except:#this happens if 0 contours returned
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
                    if(encoded_mask[j][i]==0 or check_open(encoded_mask[j][i])):
                        A_encoded_mask[j][i]=result[0][0]+1
                        E_encoded_mask[j][i]=0

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",command=add_seg)
    plus.grid(row=9,column=3,columnspan=1)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",command=sub_seg)
    minus.grid(row=10,column=3,columnspan=1)
    
    deactivate()
    
def check_open(ind):#the functionality of locks are displayed in this, overriding of tissues is avoided
    if(lock_mat[ind-1]==0):
        return 1
    else:
        return 0
    
def update_mask():
    global npfile
    
 
    
    colornpfile=np.copy(copynpfile)
    

    for en in range(0,14):
        find=np.where(encoded_mask==en+1)
        X=list(find[1])
        Y=list(find[0])
        color_mask = np.zeros((npfile.shape[0],npfile.shape[1],npfile.shape[2]), np.uint8)#coloured mask
        
        for k in range(len(X)):       
                color_mask[Y[k]][X[k]][0]=col_arr[en][0]
                color_mask[Y[k]][X[k]][1]=col_arr[en][1]
                color_mask[Y[k]][X[k]][2]=col_arr[en][2]
        
        colornpfile=cv2.addWeighted(colornpfile,1,color_mask,0.4,0)
        
    npfile=np.copy(colornpfile)
    
##    for i in range(u_ptr,len(u_stack)):
##        print("the i val is:",i)
        
    

    #shortcut to save segmentation
    root.bind('<Control-z>',undo)
    #shortcut to save segmentation
    root.bind('<Control-r>',redo)
    
            
def add_seg():
    global encoded_mask
    global u_ptr
    global u_stack
    
    result = np.where(seg_mat == 1)#serch for the index where 1 is found
    
    if(lock_mat[result[0][0]]==0):
        encoded_mask=np.copy(A_encoded_mask)
        update_mask()

    while(u_ptr!=len(u_stack)):
        u_stack.pop()
        

    u_stack.append(encoded_mask)
    u_ptr+=1

    c.delete("all")
    c.img= ImageTk.PhotoImage(Image.fromarray(npfile))
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=9,column=1,rowspan=1,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=10,column=1,rowspan=1,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=9,column=3,columnspan=1)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=10,column=3,columnspan=1)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=50, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=12,column=6,rowspan=1,columnspan=1)

    
def sub_seg():
    global encoded_mask
    global u_ptr
    global u_stack
    
    result = np.where(seg_mat == 1)#serch for the index where 1 is found
    if(lock_mat[result[0][0]]==0):
        encoded_mask=np.copy(E_encoded_mask)
        update_mask()

    while(u_ptr!=len(u_stack)):
        u_stack.pop()
        
    u_stack.append(encoded_mask)
    u_ptr+=1
 
    c.delete("all")
    c.img= ImageTk.PhotoImage(Image.fromarray(npfile))
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=9,column=1,rowspan=1,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=10,column=1,rowspan=1,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=9,column=3,columnspan=1)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=10,column=3,columnspan=1)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=50, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=12,column=6,rowspan=1,columnspan=1)



def draw():
    #SOLID/LASSO (RADIO BUTTON)
    global c
    
    if(np.count_nonzero(seg_mat)==0):
       messagebox.showerror("ERROR","You have chosen 0 tissue classes for segmentation")
       return
    
    if(np.count_nonzero(seg_mat)!=1):
       messagebox.showerror("ERROR","You have chosen more than 1 tissue class for segmentation")
       return

    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    imp=Image.fromarray(npfile)
    c.delete("all")
    c= Canvas(root,height=h,width=w,bg="white")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)

    #SIZE(SLIDER)
    size=Scale(root,from_=1, to=50, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,command=fix)
    size.grid(row=12,column=6,rowspan=1,columnspan=1)

    solid()
##    rad1=Radiobutton(root,text="Solid",value=1,command=solid)
##    rad1.grid(row=9,column=1,rowspan=1,columnspan=2)
    #rad2=Radiobutton(root,text="Lasso",value=2,command=lasso)
    #rad2.grid(row=10,column=1,rowspan=1,columnspan=2)
       
    
    
def lasso():
    global thickness
    global c
    
    deactivate()
    thickness=3

    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    imp=Image.fromarray(npfile)
    c.delete("all")
    c= Canvas(root,height=h,width=w,bg="white")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)


    c.bind("<Button-1>",LPOINT1)
    c.bind("<B1-Motion>",LMOTION)
    c.bind("<ButtonRelease-1>",LPOINT2)

def fix(arg=""):
    global thickness
    thickness=int(1.5*var.get())

    
def solid():
    deactivate()
    global trace
    global c
    global thickness

    thickness=int(1.5*var.get())
    
    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    imp=Image.fromarray(npfile)
    c.delete("all")
    c= Canvas(root,height=h,width=w,bg="white")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)
    
    #create mask where the motion is traced
    trace=np.zeros((npfile.shape[0],npfile.shape[1],npfile.shape[2]), np.uint8)
    
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

    global w
    global h

    global class_mask
    global color_mask
    global npfile

    global imp


    global index
    global ind_mat
    global seg_mat
    global lock_mat
    global num_mat
    global copyfile
    global copynpfile
    global encoded_mask
    global tail_path
    global head_path
    global time

    global col_arr

    global u_ptr
    global u_stack
    global uc_ptr
    global uc_stack
       

    try:
        if(time==0):
            root.filename= filedialog.askopenfilename(initialdir="Desktop",title="Select file",filetypes=(("png files","*.png"),("all files","*.*")))
            time+=1
        else:
            root.filename= filedialog.askopenfilename(initialdir=head_path,title="Select file",filetypes=(("png files","*.png"),("all files","*.*")))
            
        tail_path = os.path.split(root.filename)[1] #split path for saving purposes
        head_path = os.path.split(root.filename)[0]
        
        imp=Image.open(root.filename)                                                                                                       
        npfile=cv2.imread(root.filename)
        copynpfile =np.copy(npfile) #the copy of actual set of images                                                                                                                                   
        encoded_mask=np.zeros((npfile.shape[0],npfile.shape[1]), np.uint8)#the mask which will be saved later
        # all the below three functions have 15 0s or 1s for each index of images
        # 0 corresponds to disabled/unchecked segmentation/locked
        # 1 corresponds to normal/checked/unlocked
        ind_mat = np.zeros((num_class), np.uint8)
        seg_mat = np.zeros((num_class), np.uint8)
        lock_mat = np.ones((num_class), np.uint8)
        #The below will have the count for number of added materials in each image
        num_mat=0
        rev_count=0#set to 0 when ever a new image is loaded
        h,w,cha = npfile.shape
    except:
        return

    u_stack=[]
    u_ptr=1
    
    u_stack.append(encoded_mask)

    col_arr=[]


    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    c.delete("all")
    c= Canvas(root,height=h,width=w,bg="white")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)


    #NEW(BUTTON)
    new=Button(root,text="New", command=add_class)
    new.grid(row=0,column=0,columnspan=2)

    #DELETE(BUTTON)
    delete=Button(root,text="Delete",command=delete_class)
    delete.grid(row=0,column=2,columnspan=2)

    #BRUSH(BUTTON)
    brush=Button(root,text="Brush",command=draw)
    brush.grid(row=9,column=0,rowspan=2,columnspan=1)

    #SOLID/LASSO (RADIO BUTTON)
    r=IntVar()
    rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
    rad1.grid(row=9,column=1,rowspan=1,columnspan=2)
    rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
    rad2.grid(row=9,column=1,rowspan=1,columnspan=2)

    #ADD SEGMENTATION(BUTTON)
    plus=Button(root,text="     +++   ",state=DISABLED)
    plus.grid(row=9,column=3,columnspan=1)

    #ERASE SEGMENTATION(BUTTON)
    minus=Button(root,text="      ---      ",state=DISABLED)
    minus.grid(row=10,column=3,columnspan=1)

    #SIZE(SLIDER)
    var = DoubleVar()
    size=Scale(root,from_=1, to=50, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
    size.grid(row=12,column=6,rowspan=1,columnspan=1)

    #REVIEW(BUTTON)
    review=Button(root,text="Review",command=rev)
    review.grid(row=13,column=1,columnspan=4)

    #shortcut to save segmentation
    root.bind('<Control-s>',save_mask)

    #shortcut to save segmentation
    root.unbind('<Control-z>')
    #shortcut to save segmentation
    root.unbind('<Control-r>')
    
    #Set the checkboxes of segmentations and locks
    update_check_set()
    
    #Keep the mouse keys unbinded
    deactivate()
    

    

#---------------------------------------OTHER UTILITY FUNCTION-----------------------------------------------------------------------------------------------------------
#ALL MOUSE DEACTIVATION
def deactivate():
    c.unbind("<Button-1>")
    c.unbind("<B1-Motion>")
    c.unbind("<ButtonRelease-1>")

def undo(event=""):
    global u_ptr
    global u_stack
    global encoded_mask
    
    if(u_ptr>0):
        if(u_ptr>1):
            encoded_mask=np.copy(u_stack[u_ptr-2])
        if(u_ptr==1):
            encoded_mask=np.copy(u_stack[u_ptr-1])
        u_ptr-=1
        update_mask()
        c.delete("all")
        c.img= ImageTk.PhotoImage(Image.fromarray(npfile))
        c.create_image(0,0,image=c.img,anchor='nw')
        c.grid(row=0,column=6,rowspan=12,columnspan=10)


  
    

def redo(event=""):
    global u_ptr
    global u_stack
    global encoded_mask
        
    if(u_ptr<len(u_stack)):
        encoded_mask=np.copy(u_stack[u_ptr])
        u_ptr+=1
        update_mask()
        c.delete("all")
        c.img= ImageTk.PhotoImage(Image.fromarray(npfile))
        c.create_image(0,0,image=c.img,anchor='nw')
        c.grid(row=0,column=6,rowspan=12,columnspan=10)
    
    


#CHECKPOINT
def save_mask(event=""):
    folder_selected = filedialog.askdirectory()
    path=folder_selected+"/"+tail_path.split('.')[0]+"_Annotation.png"
    enh_encoded_mask=encoded_mask
    cv2.imwrite(path,enh_encoded_mask)

def rev():
    global encoded_mask
    root.filename= filedialog.askopenfilename(initialdir="C://Users",title="Select file",filetypes=(("png files","*.png"),("all files","*.*")))
    seg_mask=Image.open(root.filename)
    encoded_mask=np.copy(seg_mask)
    update_mask()
    c.delete("all")
    c.img= ImageTk.PhotoImage(Image.fromarray(npfile))
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=6,rowspan=12,columnspan=10)
    
    
#------------------------END OF FUNCTIONS-------------------------------------------------------------------------------------------------------------------------


#WIDGETS
#*-Activated, else DISABLED

#NEW(BUTTON)
new=Button(root,text="New", state=DISABLED)
new.grid(row=0,column=0,columnspan=2)

#DELETE(BUTTON)
delete=Button(root,text="Delete",state=DISABLED)
delete.grid(row=0,column=2,columnspan=2)

#BRUSH(BUTTON)
brush=Button(root,text="Brush",state=DISABLED)
brush.grid(row=9,column=0,rowspan=2,columnspan=1)

#SOLID/LASSO (RADIO BUTTON)
r=IntVar()
rad1=Radiobutton(root,text="Solid",variable=r,value=1,state=DISABLED)
rad1.grid(row=9,column=1,rowspan=1,columnspan=2)
rad2=Radiobutton(root,text="Lasso",variable=r,value=2,state=DISABLED)
rad2.grid(row=10,column=1,rowspan=1,columnspan=2)
       
#ADD SEGMENTATION(BUTTON)
plus=Button(root,text="     +++   ",state=DISABLED)
plus.grid(row=9,column=3,columnspan=1)

#ERASE SEGMENTATION(BUTTON)
minus=Button(root,text="      ---      ",state=DISABLED)
minus.grid(row=10,column=3,columnspan=1)

#SIZE(SLIDER)
var = DoubleVar()
size=Scale(root,from_=1, to=50, variable = var,sliderlength=40,length=600, orient=HORIZONTAL,state=DISABLED)
size.grid(row=12,column=6,rowspan=1,columnspan=1)


#IMAGE BACKGROUND PARAMETERS(CANVAS) *
c= Canvas(root,height=h,width=w,bg="white")
c.grid(row=0,column=6,rowspan=12,columnspan=10)

#ADD TO STACK PARAMETERSS(BUTTON) *
op=Button(root,text="Add Image",command= openf)
op.grid(row=12,column=8,columnspan=1)

#REVIEW(BUTTON)
review=Button(root,text="Review",state=DISABLED)
review.grid(row=13,column=1,columnspan=4)

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
 

#EXTERNAL TISSUE(LABELS) *
external_tissue=Label(root,text="External_Tissue",bd=1)
external_tissue.grid(row=2,column=1)

#TISSUE_1(LABELS) *
tissue_1=Label(root,text="Tissue_1",bd=1)
tissue_1.grid(row=3,column=1)

#TISSUE_2(LABELS) *
tissue_2=Label(root,text="Tissue_2",bd=1)
tissue_2.grid(row=4,column=1)

#TISSUE_3(LABELS) *
tissue_3=Label(root,text="Tissue_3",bd=1)
tissue_3.grid(row=5,column=1)

#TISSUE_4(LABELS) *
tissue_4=Label(root,text="Tissue_4",bd=1)
tissue_4.grid(row=6,column=1)

#TISSUE_5(LABELS) *
tissue_5=Label(root,text="Tissue_5",bd=1)
tissue_5.grid(row=7,column=1)

#TISSUE_6(LABELS) *
tissue_6=Label(root,text="Tissue_6",bd=1)
tissue_6.grid(row=8,column=1)


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

root.mainloop()

