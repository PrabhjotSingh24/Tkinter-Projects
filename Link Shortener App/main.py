import pyshorteners
from tkinter import *
from tkinter import PhotoImage, messagebox


class UrlShortApp(Tk):
    app_width = 450
    app_height = 450

    def __init__(self):
        super().__init__()
        self.title("Link Shortener")
        self.geometry(
            f"{self.app_width}x{self.app_height}+{(self.winfo_screenwidth()-self.app_width)//2}+{(self.winfo_screenheight()-self.app_height)//2}")
        self.iconbitmap("./urlshort.ico")
        self.resizable(0, 0)

        # frames
        self.main_frame = Frame(self)
        self.main_frame.pack()
        self.heading_frame = Frame(self.main_frame)
        self.heading_frame.pack()
        self.shorten_frame = Frame(self.main_frame)
        self.shorten_frame.pack()

        # Title
        self.heading = Label(
            self.heading_frame, text="Shorten your URLs!", font=("Poppins Semibold", 25))
        self.heading.pack()

        #link and api(Shorten)
        self.link_var = StringVar()
        self.api_var = StringVar()
        self.link_label = Label(
            self.shorten_frame, text="Enter your link here: ", font=("Poppins Semibold", 13))
        self.link_label.grid(row=0, column=0)
        self.api_label = Label(
            self.shorten_frame, text="Enter your API here: ", font=("Poppins Semibold", 13))
        self.api_label.grid(row=1, column=0, pady=10)

        self.link = Entry(
            self.shorten_frame, textvariable=self.link_var, font=("Poppins Regular", 13))
        self.link.grid(row=0, column=1)
        self.api = Entry(self.shorten_frame, textvariable=self.api_var, font=(
            "Poppins Regular", 13), show="*")
        self.api.grid(row=1, column=1)

        #link and api (unshorten)
        self.unshort_link_var = StringVar()
        self.heading2 = Label(
            self.main_frame, text="Unshorten your URLs!", font=("Poppins Semibold", 25))
        self.heading2.pack()
        self.unshorten_frame = Frame(self.main_frame)
        self.unshorten_frame.pack()
        self.unshorten_link_label = Label(self.unshorten_frame, text="Enter your short link here: ", font=(
            "Poppins Semibold", 13), wraplength=200, padx=10)
        self.unshorten_link_label.grid(row=0, column=0)
        self.unshorten_link = Entry(
            self.unshorten_frame, textvariable=self.unshort_link_var, font=("Poppins Regular", 13))
        self.unshorten_link.grid(row=0, column=1)

        # Universal Button
        self.link_image = PhotoImage(file="./get link.png")
        self.uni_button = Button(self.main_frame, text="Get link", font=(
            "Poppins Regular", 13), command=self.get_link, image=self.link_image, borderwidth=0)
        self.uni_button.pack()

        # All links
        self.link_box = Text(self.main_frame, font=(
            "poppins regular", 13), height=1)
        self.link_box.place(x=0, y=400)

    def get_link(self):
        try:
            if self.api_var.get() != "" and self.unshort_link_var.get() == "":
                short_link = pyshorteners.Shortener(api_key=self.api_var.get())
                link = short_link.bitly.short(self.link_var.get())
                self.link_box.insert(END, link)
            elif self.api_var.get() == "" and self.unshort_link_var.get() == "":
                short_link = pyshorteners.Shortener()
                link = short_link.tinyurl.short(self.link_var.get())
                self.link_box.insert(END, link)
            elif self.api_var.get() != "" and self.link_var.get() == "":
                unshort_link = pyshorteners.Shortener(api_key=self.api_var.get())
                link = unshort_link.bitly.expand(self.unshort_link_var.get())
                self.link_box.insert(END, link)
            elif self.api_var.get() == "" and self.link_var.get() == "":
                unshort_link = pyshorteners.Shortener()
                link = unshort_link.tinyurl.expand(self.unshort_link_var.get())
                self.link_box.insert(END, link)
        except:
            messagebox.showwarning("Alert", "Please enter a link!")


if __name__ == "__main__":
    UrlShortApp().mainloop()
