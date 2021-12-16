from tkinter import *

class TodoApp(Tk):
    app_width = 450
    app_height = 530

    def __init__(self,):
        super().__init__()
        self.title("Todo App")
        self.geometry(
            f"{self.app_width}x{self.app_height}+{(self.winfo_screenwidth()-self.app_width)//2}+{(self.winfo_screenheight()-self.app_height)//2}")
        self.iconbitmap('./Notes.ico')
        self.todo_item = StringVar()
        # Labels
        self.heading = Label(self, text="Todos", font=("Poppins Semibold", 22))
        self.heading.pack()
        # Frames
        self.main_frame = Frame(self)
        self.main_frame.pack()
        self.top_frame = Frame(self.main_frame)
        self.top_frame.pack()
        self.mid_frame = Frame(self.main_frame)
        self.mid_frame.pack()
        self.bottom_frame = Frame(self.main_frame)
        self.bottom_frame.pack()
        # Scroll bar and TodoList
        self.todo_list = Listbox(self.mid_frame, selectmode=EXTENDED, font=(
            "Poppins", 20), width=self.app_width)
        self.todo_scroll = Scrollbar(
            self.mid_frame, command=self.todo_list.yview)
        self.todo_scroll.pack(side=RIGHT, fill=Y)
        self.todo_list.config(yscrollcommand=self.todo_scroll.set)
        self.todo_list.pack()
        self.todo_list.bind("<Double-1>", self.mark_done)
        # function calls
        self.load_todos()
        # Entry with Label
        self.todo_entry_label = Label(self.top_frame, text="Type and hit Enter: ", font=(
            "Poppins Regular", 13), wraplength=175)
        self.todo_entry_label.grid(row=0, column=0, padx=10)
        self.todo_entry = Entry(
            self.top_frame, textvariable=self.todo_item, font=("Poppins Regular", 13))
        self.todo_entry.grid(row=0, column=1)
        self.todo_entry.bind("<Return>", self.add_todo)

    @staticmethod
    def get_todos():
        with open("./todos.txt", 'r') as file:
            file_content = map(lambda x: x.split(","), file.readlines())
            return list(file_content)

    def load_todos(self):
        self.todo_list.delete(0, END)
        todos = self.get_todos()
        for index, i in enumerate(todos):
            todo, code = i[0], i[1]
            self.todo_list.insert(
                END, f"{index+1}. {todo.capitalize()}                                                          {code}")

    def mark_done(self, event):
        try:
            with open("./todos.txt", "r") as file:
                file_content = file.readlines()
                file_content1 = list(map(lambda x: x.split(","), file_content))
                for i in file_content1:
                    if i[1] == self.todo_list.get(ACTIVE).split(" ")[-1]:
                        file_content.pop(file_content1.index(i))
                with open("./todos.txt", 'w') as file2:
                    file2.writelines(file_content)
            self.load_todos()
        except:
            pass

    def add_todo(self, event):
        from random import randint
        with open("./todos.txt", 'r') as file:
            file_content = file.readlines()
            file_content.append(f"\n{self.todo_item.get()},{randint(0,1000)}")
            with open('./todos.txt', 'w') as file2:
                file2.writelines(file_content)
            self.load_todos()
            self.todo_entry.delete(0,END)


if __name__ == "__main__":
    TodoApp().mainloop()
