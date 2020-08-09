#Author Name : V K VIEKASH
#Project: GUI to view,segment and make markings on Images
#Applications: For dataset collection of ultrasound scans to determine defects in fetus
#Functions:
#Global Variables: 


from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import cv2
import numpy as np
import math as m
import pandas as pd

#DECLARATION AND OPENINGS:

#LISTS
img_list=[]
new_list=[]
lisx=[]
lisy=[]
lis=[]
seg=[]
Dict={}
mini={}
rlist=[]
rlistx=[]
rlisty=[]

#IMAGE
imgp=Image.open("BG.png")
w,h = imgp.size

#ROOT
root=Tk()
root.geometry("403x490")#widthxheight
root.title('Report')
root.iconbitmap("icon.ico")
var = DoubleVar()

#FUNCTIONS

#EXIT
def Quit():
    root.quit()
    root.destroy()
    
#Export data tO CSV
def expod():
    df = pd.DataFrame({ key:pd.Series(value) for key, value in Dict.items()})
    dft=df.transpose()
    print(dft)
    dft.to_csv('new.csv')
    
#CLICK START
def RPOINT1(event):
    global X1
    global Y1
    global X
    global Y

    rlist.clear()
    rlistx.clear()
    rlisty.clear()
    
    #updating variables
    X1=event.x
    Y1=event.y    
    X=X1
    Y=Y1

#CLICK MOTION
def RMOTION(event):
    global X
    global Y
    global w
    global h
    
    #updating list
    rlistx.append(X)
    rlisty.append(Y)
    rlist.append((X,Y))

    #updating variables and connecting points
    if(event.x>=0 and event.x<=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,event.x,event.y,fill="white",width=rval)
        X=event.x
        Y=event.y
              
    if(event.x<=0 and event.x<=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,0,event.y,fill="white",width=rval)
        X=0
        Y=event.y
    if(event.x>=0 and event.x>=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,w,event.y,fill="white",width=rval)
        X=w-1
        Y=event.y
    if(event.x>=0 and event.x<=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,event.x,0,fill="white",width=rval)
        X=event.x
        Y=0
    if(event.x>=0 and event.x<=w and event.y>=0 and event.y>=h):
        c.create_line(X,Y,event.x,h,fill="white",width=rval)
        X=event.x
        Y=h-1
    if(event.x<=0 and event.x<=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,0,0,fill="white",width=rval)
        X=0
        Y=0
    if(event.x<=0 and event.x<=w and event.y>=0 and event.y>=h):
        c.create_line(X,Y,0,h,fill="white",width=rval)
        X=0
        Y=h-1
    if(event.x>=0 and event.x>=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,w,0,fill="white",width=rval)
        X=w-1
        Y=0
    if(event.x>=0 and event.x>=w and event.y>=0 and event.y>=h):
       c.create_line(X,Y,w,h,fill="white",width=rval)
       X=w-1
       Y=h-1
       
#CLICK RELEASE
def RPOINT2(event):
    global X2
    global Y2
    global X
    global Y
    global w
    global h
    global madd
    
    #updating variables and connecting point last and first
    i=0
    j=0
    k=0
    
    X2=event.x
    Y2=event.y
    
    rlist.append((X2,Y2))

    k=2#modifyable
    p=k*rval
    listlen=len(rlist)-1
    
    for i in range(listlen):
        for j in range(-p,p):
            q=rlist[i]
            rlist.append((q[0],q[1]+j))

    imcv = cv2.cvtColor(np.asarray(img_list[num-1]), cv2.COLOR_RGB2BGR)
    mask = np.zeros((imcv.shape[0],imcv.shape[1],3), np.uint8)
    madd = np.zeros((imcv.shape[0],imcv.shape[1],3), np.uint8)
              
    for k in rlist:
             j=k[1]
             i=k[0]
             mask[j][i][0]=imcv[j][i][0]
             mask[j][i][1]=imcv[j][i][1]
             mask[j][i][2]=imcv[j][i][2]
             madd[j][i][0]=255
             madd[j][i][1]=255
             madd[j][i][2]=255
             addim[j][i][0]=0
             addim[j][i][1]=0
             addim[j][i][2]=0
             
    dst = cv2.addWeighted(mask,1,addim,1,0)
    im_pil = Image.fromarray(dst)
    
    new_list[sind-1]=im_pil.copy()
    c.img= ImageTk.PhotoImage(new_list[sind-1])
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=0,columnspan=4)
    
    c.unbind("<Button-1>")
    c.unbind("<B1-Motion>")
    c.unbind("<ButtonRelease-1>")

#Saving Segmentation mask
def segment():

    
    #converting the collected list to numpy array contour format
    arr = np.asarray(lis)
    lc=[arr]

    #Preparing mask for segmentation
    imcv = cv2.cvtColor(np.asarray(img_list[num-1]), cv2.COLOR_RGB2BGR)
    mask = np.ones((imcv.shape[0],imcv.shape[1],3), np.uint8)
    mask*=255

    #Finding the internals of the drawn contour
    miny=min(lisy)
    maxy=max(lisy)
    minx=min(lisx)
    maxx=max(lisx)
    
    for i in range(minx,maxx):
        for j in range(miny,maxy):       
          if((cv2.pointPolygonTest(lc[0],(i,j),False))>0):
              mask[j][i][0]=imcv[j][i][0]
              mask[j][i][1]=imcv[j][i][1]
              mask[j][i][2]=imcv[j][i][2]

    dst = cv2.addWeighted(mask,1,madd,1,0)
    
    #Saving using a popup message       
    response= messagebox.askyesno("Question","Do u want to save the segmentation")
    if(response):
        seg[sind-1]+=1#updating segmentation count
        #Saving"in" the numpy mask segmentation
        cv2.imwrite( "image "+str(sind)+" segmentation "+str(seg[sind-1])+".jpg", dst)

#SCALE VALUE SELECTION
def sel():
   global rval
   selection = var.get()
   rval=int(selection)*2
   
#Erase
def rub():
    c.unbind("<Button-1>")
    c.unbind("<B1-Motion>")
    c.unbind("<ButtonRelease-1>")

    #ERASER SIZE OPTIONS(SLIDER)
    slider=Scale(root,from_=1, to=3, variable = var, orient=HORIZONTAL)
    slider.grid(row=6,column=0,columnspan=2)

    c.bind("<Button-1>",RPOINT1)
    c.bind("<B1-Motion>",RMOTION)
    c.bind("<ButtonRelease-1>",RPOINT2)
    
    
#CLICK START
def POINT1(event):
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
def MOTION(event):
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
        c.create_line(X,Y,event.x,event.y,fill="white")
        X=event.x
        Y=event.y
              
    if(event.x<=0 and event.x<=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,0,event.y,fill="white")
        X=0
        Y=event.y
    if(event.x>=0 and event.x>=w and event.y>=0 and event.y<=h):
        c.create_line(X,Y,w,event.y,fill="white")
        X=w-1
        Y=event.y
    if(event.x>=0 and event.x<=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,event.x,0,fill="white")
        X=event.x
        Y=0
    if(event.x>=0 and event.x<=w and event.y>=0 and event.y>=h):
        c.create_line(X,Y,event.x,h,fill="white")
        X=event.x
        Y=h-1
    if(event.x<=0 and event.x<=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,0,0,fill="white")
        X=0
        Y=0
    if(event.x<=0 and event.x<=w and event.y>=0 and event.y>=h):
        c.create_line(X,Y,0,h,fill="white")
        X=0
        Y=h-1
    if(event.x>=0 and event.x>=w and event.y<=0 and event.y<=h):
        c.create_line(X,Y,w,0,fill="white")
        X=w-1
        Y=0
    if(event.x>=0 and event.x>=w and event.y>=0 and event.y>=h):
       c.create_line(X,Y,w,h,fill="white")
       X=w-1
       Y=h-1
       
#CLICK RELEASE
def POINT2(event):
    global X2
    global Y2
    global X
    global Y
    global w
    global h
    global addim
    
    #updating variables and connecting point last and first
    i=0
    j=0
    a=0
    b=0
    X2=event.x
    Y2=event.y
    c.create_line(X1,Y1,X2,Y2,fill="white")

    addim = cv2.cvtColor(np.asarray(img_list[num-1]), cv2.COLOR_RGB2BGR)
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
              addim[j][i][0]=0
              addim[j][i][1]=0
              addim[j][i][2]=0

    im_pil = Image.fromarray(addim)
    new_list[sind-1]=im_pil.copy()
    c.img= ImageTk.PhotoImage(new_list[sind-1])
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=0,columnspan=4)
    
    #SAVE SEGMENTATION(BUTTON) *
    saveseg=Button(root,text="Create Segmentation mask",command=segment)
    saveseg.grid(row=5,column=2,columnspan=2)

    #ERASER(BUTTON) *
    erase=Button(root,text="Erase",command=rub)
    erase.grid(row=3,column=1)
    
    c.unbind("<Button-1>")
    c.unbind("<ButtonRelease-1>")
    
#MOUSE ACTIVATION
def tool():
    c.unbind("<Button-1>")
    c.unbind("<B1-Motion>")
    c.unbind("<ButtonRelease-1>")

    c.bind("<Button-1>",POINT1)
    c.bind("<B1-Motion>",MOTION)
    c.bind("<ButtonRelease-1>",POINT2)


#ALL MOUSE DEACTIVATION
def deactivate():    
    c.unbind("<Button-1>")
    c.unbind("<B1-Motion>")
    c.unbind("<ButtonRelease-1>")

#START CLICK OF MARK
def marking1(event):
    global x1
    global y1
    x1=event.x
    y1=event.y
    c.create_oval(x1-4,y1-4,x1+4,y1+4,fill="Yellow")
    
#END CLICK OF MARK
def marking2(event):
    global status
    
    x2=event.x
    y2=event.y
    c.create_oval(x2-4,y2-4,x2+4,y2+4,fill="Yellow")
    c.create_line(x1,y1,x2,y2,fill="pink",dash=(4, 2),width=3)
    d=m.sqrt(((x2-x1)**2)+((y2-y1)**2))
    key=str(sind)
    dlis=[d]
    tup=[(key,dlis)]
    mini=dict(tup)
    
    try:#to update an existing key
        Dict[key].append(d)
    except:#to add a new key itself
        Dict.update(mini)
        
    mini.clear()
    
    #LENGTH(LABELS) *
    length=Label(root,text="length of line drawn between the two points in pixels is: "+str(d),bd=1,relief=SUNKEN,anchor=W)
    length.grid(row=4,column=0,columnspan=4,sticky=E+W)

    c.unbind("<Button-1>")
    c.unbind("<ButtonRelease-1>")

#mark
def marker():
    length=Label(root,text="Press at the innitial point and release at the final point over the image" ,bd=1,relief=SUNKEN,anchor=W)
    length.grid(row=4,column=0,columnspan=4,sticky=E+W)
    c.unbind("<Button-1>")
    c.unbind("<B1-Motion>")
    c.unbind("<ButtonRelease-1>")

    c.bind("<Button-1>",marking1)
    c.bind("<ButtonRelease-1>",marking2)

#NAVIGATION

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

      
    #OPEN FILE
    root.filename= filedialog.askopenfilename(initialdir="C://Users//V K VIEKASH//Desktop//codemy TKINTER",title="Select file",filetypes=(("jfif files","*.jfif"),
                                                                                                                         ("all files","*.*")))
    imp=Image.open(root.filename)
    img_list.append(imp)
    new_list.append(imp)
    w,h = imp.size
    num= len(img_list)
    seg.append(0)
    sind=num  #its the status value for each slide of the image viewer

    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    c.delete("all")
    c.img= ImageTk.PhotoImage(imp)
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=0,columnspan=4)

    #STATUS PARAMETERS(LABEL) *
    status=Label(root,text="image "+str(len(img_list))+" of "+str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=1,column=0,columnspan=4,sticky=W+E)

    #BACKWARD(BUTTON)
    back=Button(root,text="<<", state=DISABLED)
    back.grid(row=2,column=0)
    
    #FORWARD(BUTTON)
    front=Button(root,text=">>", state=DISABLED)
    front.grid(row=2,column=2)

    #DISPLAY(BUTTON) *
    if(num>1):
        display=Button(root,text="display", command=lambda: forward(num))
        display.grid(row=2,column=3)
    
    #BRUSH(BUTTON) *
    brush=Button(root,text="Brush",command=tool)
    brush.grid(row=3,column=0)

    #ERASER(BUTTON)
    erase=Button(root,text="Erase",state=DISABLED)
    erase.grid(row=3,column=1)

    #MARKINGS(BUTTON) *
    mark=Button(root,text="Mark",command=marker)
    mark.grid(row=3,column=2)

    #EXPORT DATA(BUTTON) *
    Expo=Button(root,text="Export length",command=expod)
    Expo.grid(row=3,column=3)

    #LENGTH(LABELS) *
    length=Label(root,text="press Mark to know the length between two points in that image ",bd=1,relief=SUNKEN,anchor=W)
    length.grid(row=4,column=0,columnspan=4,sticky=E+W)

    #DEACTIVATION(BUTTON) *
    off=Button(root,text="Off",command=deactivate)
    off.grid(row=5,column=0,columnspan=2)

    #SAVE SEGMENTATION(BUTTON)
    saveseg=Button(root,text="Create Segmentation mask",state=DISABLED)
    saveseg.grid(row=5,column=2,columnspan=2)

    #ERASER SIZE OPTIONS(SLIDER)
    slider=Scale(root,from_=1, to=3, variable = var, orient=HORIZONTAL,state=DISABLED)
    slider.grid(row=6,column=0,columnspan=2)

    #UPDATE SIZE(BUTTON)
    upd= Button(root,text="updadte size",command=sel)
    upd.grid(row=6,column=2,columnspan=2)

    
    #Keep the mouse keys unbinded
    c.unbind("<Button-1>")
    c.unbind("<B1-Motion>")
    c.unbind("<ButtonRelease-1>")
    

    
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

    sind=num#updation
    
    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    c.delete("all")
    c.img= ImageTk.PhotoImage(img_list[num-1])
    w,h = img_list[num-1].size
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=0,columnspan=4)

    #STATUS PARAMETERS(LABEL) *                           
    status=Label(root,text="image "+str(num)+" of "+str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=1,column=0,columnspan=4,sticky=E+W)

    #BACKWARD(BUTTON) *
    back=Button(root,text="<<", command=lambda: backward(num-1))
    back.grid(row=2,column=0)

    #ADD TO STACK PARAMETERSS(BUTTON) *
    op=Button(root,text="Add to stack", command= openf)
    op.grid(row=2,column=1)

    #FORWARD(BUTTON) *
    front=Button(root,text=">>", command=lambda: forward(num+1))
    if num==len(img_list):
        front=Button(root,text=">>",state=DISABLED)
    front.grid(row=2,column=2)

    #DISPLAY(BUTTON) *
    display=Button(root,text="display",state=DISABLED)
    display.grid(row=2,column=3)

    #BRUSH(BUTTON) *
    brush=Button(root,text="Brush",command=tool)
    brush.grid(row=3,column=0)

    #ERASER(BUTTON)
    erase=Button(root,text="Erase",state=DISABLED)
    erase.grid(row=3,column=1)

    #MARKINGS(BUTTON) *
    mark=Button(root,text="Mark",command=marker)
    mark.grid(row=3,column=2)

    #EXPORT DATA(BUTTON) *
    Expo=Button(root,text="Export length",command=expod)
    Expo.grid(row=3,column=3)

    #LENGTH(LABELS) *
    length=Label(root,text="press Mark to know the length between two points in that image ",bd=1,relief=SUNKEN,anchor=W)
    length.grid(row=4,column=0,columnspan=4,sticky=E+W)
    
    #DEACTIVATION(BUTTON) *
    off=Button(root,text="Off",command=deactivate)
    off.grid(row=5,column=0,columnspan=2)

    #SAVE SEGMENTATION(BUTTON)
    saveseg=Button(root,text="Create Segmentation mask",state=DISABLED)
    saveseg.grid(row=5,column=2,columnspan=2)

    #ERASER SIZE OPTIONS(SLIDER)
    slider=Scale(root,from_=1, to=3, variable = var, orient=HORIZONTAL,state=DISABLED)
    slider.grid(row=6,column=0,columnspan=2)

    #UPDATE SIZE(BUTTON)
    upd= Button(root,text="updadte size",command=sel)
    upd.grid(row=6,column=2,columnspan=2)

    #Keep the mouse keys unbinded
    c.unbind("<Button-1>")
    c.unbind("<B1-Motion>")
    c.unbind("<ButtonRelease-1>")
   


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

    sind=num#updation
    
    #IMAGE BACKGROUND PARAMETERS(CANVAS) *
    c.delete("all")
    c.img= ImageTk.PhotoImage(img_list[num-1])
    w,h = img_list[num-1].size
    c.create_image(0,0,image=c.img,anchor='nw')
    c.grid(row=0,column=0,columnspan=4)

    #STATUS PARAMETERS(LABEL) *                           
    status=Label(root,text="image "+str(num)+" of "+str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=1,column=0,columnspan=4,sticky=E+W)

    #BACKWARD(BUTTON) *
    back=Button(root,text="<<", command=lambda: backward(num-1))
    if num==1:
        back=Button(root,text="<<",state=DISABLED)
    back.grid(row=2,column=0)

    #ADD TO STACK PARAMETERSS(BUTTON) *
    op=Button(root,text="Add to stack", command= openf)
    op.grid(row=2,column=1)

    #FORWARD(BUTTON) *
    front=Button(root,text=">>", command=lambda: forward(num+1))
    if num==len(img_list):
        front=Button(root,text=">>",state=DISABLED)
    front.grid(row=2,column=2)

    #DISPLAY(BUTTON) *
    display=Button(root,text="display",state=DISABLED)
    display.grid(row=2,column=3)

    #BRUSH(BUTTON) *
    brush=Button(root,text="Brush",command=tool)
    brush.grid(row=3,column=0)

    #ERASER(BUTTON)
    erase=Button(root,text="Erase",state=DISABLED)
    erase.grid(row=3,column=1)

    #MARKINGS(BUTTON) *
    mark=Button(root,text="Mark",command=marker)
    mark.grid(row=3,column=2)

    #EXPORT DATA(BUTTON) *
    Expo=Button(root,text="Export length",command=expod)
    Expo.grid(row=3,column=3)

    #LENGTH(LABELS) *
    length=Label(root,text="press Mark to know the length between two points in that image ",bd=1,relief=SUNKEN,anchor=W)
    length.grid(row=4,column=0,columnspan=4,sticky=E+W)

    #DEACTIVATION(BUTTON) *
    off=Button(root,text="Off",command=deactivate)
    off.grid(row=5,column=0,columnspan=2)

    #SAVE SEGMENTATION(BUTTON)
    saveseg=Button(root,text="Create Segmentation mask",state=DISABLED)
    saveseg.grid(row=5,column=2,columnspan=2)
    
    #ERASER SIZE OPTIONS(SLIDER)
    slider=Scale(root,from_=1, to=3, variable = var, orient=HORIZONTAL,state=DISABLED)
    slider.grid(row=6,column=0,columnspan=2)

    #UPDATE SIZE(BUTTON)
    upd= Button(root,text="updadte size",command=sel)
    upd.grid(row=6,column=2,columnspan=2)



    #Keep the mouse keys unbinded
    c.unbind("<Button-1>")
    c.unbind("<B1-Motion>")
    c.unbind("<ButtonRelease-1>")

    
#WIDGETS
#*-Activated

#IMAGE BACKGROUND PARAMETERS(CANVAS) *
c= Canvas(root,height=h,width=w,bg="white")
c.img=ImageTk.PhotoImage(imgp)
c.create_image(0,0,image=c.img,anchor='nw')
c.grid(row=0,column=0,columnspan=4)

#STATUS PARAMETERS(LABEL) *                           
status=Label(root,text="image 0 of "+str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
status.grid(row=1,column=0,columnspan=4,sticky=E+W)

#BACKWARD(BUTTON)
back=Button(root,text="<<", state=DISABLED)
back.grid(row=2,column=0)

#ADD TO STACK PARAMETERSS(BUTTON) *
op=Button(root,text="Add to stack", command= openf)
op.grid(row=2,column=1)

#FORWARD(BUTTON)
front=Button(root,text=">>", state=DISABLED)
front.grid(row=2,column=2)

#DISPLAY(BUTTON)
display=Button(root,text="display",state=DISABLED)
display.grid(row=2,column=3)

#BRUSH(BUTTON)
brush=Button(root,text="Brush",state=DISABLED)
brush.grid(row=3,column=0)

#ERASER(BUTTON)
erase=Button(root,text="Erase",state=DISABLED)
erase.grid(row=3,column=1)

#MARKINGS(BUTTON)
mark=Button(root,text="Mark",state=DISABLED)
mark.grid(row=3,column=2)

#EXPORT DATA(BUTTON)
Expo=Button(root,text="Export length",state=DISABLED)
Expo.grid(row=3,column=3)

#LENGTH(LABELS) *
length=Label(root,text="press Mark to know the length between two points in that image ",bd=1,relief=SUNKEN,anchor=W)
length.grid(row=4,column=0,columnspan=4,sticky=E+W)

#DEACTIVATION(BUTTON)
off=Button(root,text="Off",state=DISABLED)
off.grid(row=5,column=0,columnspan=2)

#SAVE SEGMENTATION(BUTTON)
saveseg=Button(root,text="Create Segmentation mask",state=DISABLED)
saveseg.grid(row=5,column=2,columnspan=2)

#ERASER SIZE OPTIONS(SLIDER)
slider=Scale(root,from_=1, to=3, variable = var, orient=HORIZONTAL,state=DISABLED)
slider.grid(row=6,column=0,columnspan=2)

#UPDATE SIZE(BUTTON)
upd= Button(root,text="updadte size",command=sel)
upd.grid(row=6,column=2,columnspan=2)

#EXIT PARAMETERS(BUTTON)
Exit= Button(root,text="exit", command=Quit)
Exit.grid(row=7,column=0,columnspan=4)

root.mainloop()
