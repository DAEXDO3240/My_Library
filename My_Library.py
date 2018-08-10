from tkinter import *
import time
import math

#file-rwc

def rwc_copy(file, copyFile): 
  f1 = open(Originale, "r") 
  f2 = open(Copia, "w") 
  while 1: 
    Testo = f1.read(50) 
    if Testo == "": 
      break 
    f2.write(Testo) 
  f1.close() 
  f2.close() 
  return

def rwc_open(file):
  try:
    f=open(file,"r")
    text=f.read()
    f.close()
  except:
    print('=> Il file "'+str(fI)+'" non esiste\n')

def rwc_create(file):
  f=open(file,"w")
  f.close()

#mat

def add(a,b):
  ad=a+b
  print("=> Il risultato è:",ad)

def sot(a,b):
  so=a-b
  print("=> Il risultato è:",so)

def mol(a,b):
  mo=a*b
  print("=> Il risultato è:",mo)

def div(a,b):
  di=a/b
  print("=> Il risultato è:",di)

def pot(a,b):
  a1=a
  for i in range(b,1,-1):
    a=a*a1
  print("=> Il risultato è:",int(a))

def rad(a):
  ra=math.sqrt(a)
  print("=> Il risultato è:",ra)

def add3(a,b,c):
  ad=a+b+c
  print("=> Il risultato è:",ad)

def sot3(a,b,c):
  so=a-b-c
  print("=> Il risultato è:",so)

def mol3(a,b,c):
  mo=a*b*c
  print("=> Il risultato è:",mo)
  
def div3(a,b,c):
  di=a/b/c
  print("=> Il risultato è:",di)
  
def equa2(a,b,c):
  r=0
  de=(b*b)-4*a*c
  if(de<0):
    print("=> L'equazione di secondo grado è impossibile perché delta è 0.")
    print("")
  else:
    e=((b*-1)+math.sqrt(de))
    q=(2*a)
    e1=e
    q1=q
    if(e<q):
      r=q
      q=e
      e=r
    while(q!=0):
      r=e%q
      e=q
      q=r
    mcd=e
    e=int(e1/mcd)
    q=int(q1/mcd)
    if(q<0):
      q=q*-1
      e=e*-1
    if(q==1):
      print("=> x1=",e)
    elif(q!=1):
      print("=> x1=",e,"/",q)
    r=0
    e2=((b*-1)-math.sqrt(de))
    q2=(2*a)
    e3=e2
    q3=q2
    if(e2<q2):
      r=q2
      q2=e2
      e2=r
    while(q2!=0):
      r=e2%q2
      e2=q2
      q2=r
    mcd2=e2
    e2=int(e3/mcd2)
    q2=int(q3/mcd2)
    if(q2<0):
      q2=q2*-1
      e2=e2*-1
    if(q==1):
      print("=> x2=",e2)
    elif(q!=1):
      print("=> x2=",e2,"/",q2)

#sistema
def sis(a,b,c,a1,b1,c1):
  D=a*b1-a1*b
  Dx=c*b1-c1*b
  Dy=a*c1-a1*c
  Dx1=Dx
  D1=D
  r=0
  if(Dx<D):
    r=D
    D=Dx
    Dx=r
  while(D!=0):
    r=Dx%D
    Dx=D
    D=r
  mcd=Dx
  Dx=int(Dx1/mcd)
  D=int(D1/mcd)
  if(D<0):
    D=D*-1
    Dx=Dx*-1
  if(D==1):
    print("=> X=",Dx)
  elif(D!=1):
    print("=> X=",Dx,"/",D)
  print("")
  Dy1=Dy
  D1=D
  r=0
  if(Dy<D):
    r=D
    D=Dy
    Dy=r
  while(D!=0):
    r=Dy%D
    Dy=D
    D=r
  mcd=Dy
  Dy=int(Dy1/mcd)
  D=int(D1/mcd)
  if(D<0):
    D=D*-1
    Dy=Dy*-1
  if(D==1):
    print("=> Y=",Dy)
  elif(D!=1):
    print("=> Y=",Dy,"/",D)

#My_Window

def add_text(text, teext):
    texxt=""
    t=text.get(1.0,END)
    texxt += str(teext)
    text.insert(END, texxt)
    
def delete(text):
    text.delete(0.0, END)

def prt(prtx):
    print(prtx)

def exit_prog(root):
    root.destroy()
    exit()

def backup(nameBackup, nameProg, text): 
    backup=open(nameBackup+".dat","w")  
    prog=open(nameProg+".py","r")
    PG=prog.read()
    backup.write(PG)
    backup.close()
    prog.close()
    texxt=""
    text.delete(0.0, END)
    texxt += "=> Il backup è stato eseguito con successo...\n"
    text.insert(0.0, texxt)
    
def entry_open(entry, text):
    fI=entry.get()
    try:
        f=open(fI,"r")
        texxt=str(f.read())+"\n"
        text.insert(0.0, texxt)
        f.close()
    except:
        text.delete(0.0, END)
        texxt='=> Il file "'+str(fI)+'" non esiste\n'
        text.insert(0.0, texxt)

def entry_save(entry, text):
    texxt=""
    fI=entry.get()
    try:
        f=open(fI,"r")
        f.close()
        f=open(fI,"w")
        f.write(text.get(1.0,END))
        f.close()
    except:
        text.delete(0.0, END)
        texxt='=> Il file "'+str(fI)+'" non esiste\n'
        text.insert(0.0, texxt)
        
def entry_create(entry):
    fI=entry.get()
    f=open(fI,"w")
    f.close()

def root(nameRoot, nameWindow, dimX, dimY):
  nameRoot = Tk()
  nameRoot.title(nameWindow)
  dimX=str(dimX)
  dimY=str(dimY)
  nameRoot.geometry(dimX+"x"+dimY)

def loop(nameRoot):
  name.mainloop()
