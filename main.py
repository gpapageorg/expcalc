from cgitb import text
from copy import copy
import tkinter as tk
from tkinter.ttk import *
from sympy import *
#from IPython import display
mainbg = '#2B2E4A'
secbg = '#903749'
init_printing(use_unicode=True)

taylor_result = []

class Expansion():
    '''Class Expantion Manages Main GUI And Doing The Mathematical Computations'''
    def __init__(self, root):
        '''Constructor Manages Main Window'''

        self.root = root
        self.ws = self.root.winfo_screenwidth()
        self.hs = self.root.winfo_screenheight()
        #print(ws,hs)
        self.root.title('Series Expantion Calulator')
        self.root.configure(background  = mainbg)
        self.root.geometry('600x200')
        self.root.resizable(False,False)
        self.title = tk.Label(root, text = 'Series Expansion Calculator', font = 'Verdana 20 bold', background= secbg)
        self. title.pack(fill = 'x')
        self.data = tk.Text(root,height = 3,font = 'verdana 15')
        self.data.pack(anchor='w', padx = 5, pady=10, fill = 'x')
        self.f1 = tk.Frame(root, background = mainbg)
        self.f1.pack(fill = 'both')
        self.b1 = tk.Button(self.f1, text = 'Taylor', font = 'verdana 15 ', background= '#E84545', command = self.taylor)
        self.b3 = tk.Button(self.f1, text = 'Binomial', font = 'verdana 15', background= '#E84545')
        self.b1.grid(row = 1, column= 0, padx= 5, pady= 15)
        self.b3.grid(row = 1, column= 2, pady= 15, padx = 5)
        

    def taylor(self):
        
        '''Function taylor Manages Taylor expantion'''
        self.taylor_res = []
        x = symbols('x')
        init_printing(use_unicode=True)

        self.text = ''
        data = self.data.get('1.0',tk.END)
        self.fun, self.op, self.value, self.times = data.split(',')
        self.fun = self.fun.strip()
        self.op = self.op.strip()
        self.value = self.value.strip()
        self.times = self.times.strip()

        
        self.fun = sympify(self.fun)
        #print(self.fun.subs(self.op, self.value))
        self.times = int(self.times)
        # print('F(x) = ',end = '')
        for i in range(self.times):
            self.dx = diff(self.fun, self.op, i)
            self.der_val = self.dx.subs(x,self.value)
            if i == self.times - 1: add = ''
            else: add = '+'
            self.text += '((x - {})**{}*{})/(factorial({})) {} '.format(self.value,i,self.der_val,i,add)
        
        self.expr = sympify(self.text)
        
        print(self.expr)
        preview(self.expr, viewer='file', filename='taylor_{}.png'.format(self.fun), dvioptions=['-D','300'])
        taylor_result.append(TopWin('Taylor Expansion {}'.format(self.fun),'taylor_{}.png'.format(self.fun),self.fun))
        print(taylor_result, taylor_result)

class TopWin():
    '''Class Responsible For Making Toplevel Windows'''
    def __init__(self, title, image,fun):
        self.window = tk.Toplevel(root)
        self.image = image
        self.title = title 
        self.fun = fun
        self.bg = tk.PhotoImage(file = self.image)
        self.window.title(self.title)
        self.label_image = tk.Label(self.window, image = self.bg)
        self.label_image.pack(expand = True, fill = 'both')
        self.window.resizable(False,False)
        self.label = tk.Label(self.window,text = self.fun)
        self.label.pack()
        

root = tk.Tk()
main = Expansion(root)

root.mainloop()