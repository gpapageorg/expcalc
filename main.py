import tkinter as tk
from sympy import *
from IPython import display
mainbg = '#2B2E4A'
secbg = '#903749'
init_printing(use_unicode=True)
class Expansion():
    '''Class Expantion Manages Main GUI And Doing The Mathematical Computations'''
    def __init__(self, root):
        '''Constructor Manages Main Window'''

        self.root = root
        self.root.title('Series Expantion Calulator')
        self.root.configure(background  = mainbg)
        self.root.geometry('600x200')
        self.root.resizable(False,False)
        self.title = tk.Label(root, text = 'Series Expansion Calculator', font = 'Verdana 20 bold', background= secbg)
        self.title.pack(fill = 'x')
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
        x = symbols('x')
        init_printing(use_unicode=True)
        #display(Integral(x*2,x))

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
            if int(self.value) == 0: self.text += 'x^{} * {}/{}! {} '.format(self.value,i,self.der_val,i,add)
            else: self.text += '((x - {})**{}*{})/(factorial({})) {} '.format(self.value,i,self.der_val,i,add)
        
        expr = sympify(self.text)
        
        print(expr)
        preview(expr, viewer='file', filename='taylor.png',dvioptions=['-D','300'],order = 'grevlex')
        
        self.taylor_res = TopWin('Taylor Expansion','taylor.png')
        

class TopWin():
    '''Class Responsible For Making Toplevel Windows'''
    def __init__(self, title, image):
        self.window = tk.Toplevel()
        self.image = image
        self.title = title
        self.bg = tk.PhotoImage(file = self.image)
        self.window.title(self.title)
        self.label_image = tk.Label(self.window, image = self.bg)
        self.label_image.pack(expand = True, fill = 'both')
        self.window.resizable(False,False)

root = tk.Tk()
main = Expansion(root)

root.mainloop()