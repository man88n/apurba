import tkinter as tk
from tkinter import messagebox
import random
class BusinessManagementGame:
    def __init__(self,master):
        self.master=master
        self.master.title("BusinessmanagmentGame")
        self.balance=1000
        self.expenses=500
        self.income=0
        self.create_widgets()

    def create_widgets(self):
        self.balance_label=tk.Label(self.master,text=f"Balance:${self.balance}")
        self.balance_label.pack()
        self.expenses_label=tk.Label(self.master,text=f"Expenses:${self.expenses}")
        self.expenses_label.pack()
        self.income_label=tk.Label(self.master,text=f"Income:${self.income}")
        self.income_label.pack()
        self.investment_button=tk.Button(self.master,text="Invest",command=self.invest
                                         )
        self.investment_button.pack()
        self.work_button=tk.Button(self.master,text="Work",command=self.work)
        self.work_button.pack()
    
    def invest(self):
                investment=random.randint(100,500)
                self.balance-=investment
                self.expenses+=investment
                self.update_display()
    def work(self):
          income=random.randint(200,800)
          self.balance+=income
          self.income+=income
          self.update_display()
          if self.income>=self.expenses:
                messagebox.showinfo("congradulation","you've earned enough to cover your expenses")
          
    def update_display(self):
          self.balance_label.config(text=f"Balance:${self.balance}")
          self.expenses_label.config(text=f"Expenses:${self.expenses}")
          self.income_label.config(text=f"Income:${self.income}")
          
if __name__== "__main__":
    root=tk.Tk()    
    app=BusinessManagementGame(root)
    root.mainloop()                            