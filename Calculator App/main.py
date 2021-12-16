from tkinter import *

class CalcApp(Tk):
    app_width=450
    app_height=500
    def __init__(self):
        super().__init__()
        self.pos_x=(self.winfo_screenwidth()-self.app_width)//2
        self.pos_y=(self.winfo_screenheight()-self.app_height)//2
        self.title("Calculator")
        self.iconbitmap("./calculator.ico")
        self.geometry(f"{self.app_width}x{self.app_height}+{self.pos_x}+{self.pos_y}")

if __name__=="__main__":
    CalcApp().mainloop()