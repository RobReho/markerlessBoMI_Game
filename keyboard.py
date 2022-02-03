from tkinter import *
import tkinter.scrolledtext as scrolledtext    
         
class Keyboard():             
    """
    class that initialize a virtual keyboard that can be controlled by the real mouse cursor
    """
    def __init__(self):

        root = Tk()
        root.title("keyboard")
        root.resizable(0,0)
        print('init virtual keyboard')
        #text window
        text=scrolledtext.ScrolledText(root,width=120,height=5,wrap=WORD,padx=10,pady=10,borderwidth=5,relief=RIDGE)
        text.grid(row=1,columnspan=16)

        buttons=['q','w','e','r','t','y','u','i','o','p','<-','7','8','9','-',
                'a','s','d','f','g','h','j','k','l','[',']','4','5','6','+',
                'z','x','c','v','b','n','m',',','.','Tab','0','1','2','3','/',
                'Space']

        varrow=2
        varcolumn=0

        for button in buttons:
            command = lambda x=button: self.select(x,text)
            
            if button != 'Space':
                Button(root,text=button,width=8,bg='black',fg='white',activebackground="white",activeforeground="black",
                relief=RIDGE,padx=12,pady=15,bd=5,command=command).grid(row=varrow,column=varcolumn)
            if button == 'Space':
                Button(root,text=button,width=5,bg='black',fg='white',activebackground="white",activeforeground="black",
                relief=RIDGE,padx=180,pady=15,bd=5,command=command).grid(row=6,columnspan=16)
                
            varcolumn+=1
            if varcolumn >14 and varrow ==2:
                varcolumn=0
                varrow+=1
            if varcolumn > 14 and varrow ==3:
                varcolumn=0
                varrow+=1
                
        root.mainloop()

    # Function that handles the selected characters
    def select(self, value,text):
        if value =="<-":
            txt=text.get(1.0,END)
            val=len(txt)
            text.delete(1.0,END)
            text.insert(1.0,txt[:val-2])
        
        elif value =="Space":
            text.insert(END," ")
        elif value =="Space":
            text.insert(END,"    ")
        else:
            text.insert(END,value)   
    
