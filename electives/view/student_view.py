from tkinter import *

class StudentWindow:
    def __init__(self, master):

        self.master = master
        self.master.title('Student')

        self.top_frame = Frame(self.master)
        self.mid_frame = Frame(self.master)
        self.bot_frame = Frame(self.master)

        self.enter_sn = Label(self.top_frame, text='Enter Student Number:')
        self.sn_entry = Entry(self.top_frame, width=20)

        self.sn_label = Label(self.top_frame, text='Student Number:')
        self.sn_label = Label(self.top_frame, text='Student Number:')

        self.enter_sn.grid(row=0, col=0, padx=30, pady=10)
        self.sn_entry.grid(row=0, col=1, padx=30, pady=10)




        self.mid_frame.grid(row=1, padx=30, pady=10)
        self.bot_frame.grid(row=2, padx=30, pady=10)


if __name__ == "__main__":
