# This is not a problem )))
# It is more like algorithm for generation of a rough surface
from Tkinter import Frame, Tk, BOTH, X, RIGHT, LEFT
from ttk import Button, Entry, Label, Combobox


class MainFrame(Frame):

    w_ = 500
    h_ = 400

    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')

        self.parent_ = parent

        self.init_ui()

        self.centering()

    def centering(self):
        pos_x = (self.parent_.winfo_screenwidth() - self.w_) / 2
        pos_y = (self.parent_.winfo_screenheight() - self.h_) / 2

        self.parent_.geometry('{}x{}+{}+{}'.format(self.w_, self.h_, pos_x, pos_y))

    def init_ui(self):
        self.parent_.title('Rough surface generator')
        self.pack(fill=BOTH, expand=True)

        # top panel
        frame_top = Frame(self, background='gray75')
        frame_top.pack(fill=X)

        cb = Combobox(frame_top, values=('Gaussian', 'Laplace'))
        cb.current(0)
        cb.pack(side=LEFT, padx=5, expand=True)

        entry1 = Entry(frame_top)
        entry1.pack(side=LEFT, padx=5, expand=True)

        entry2 = Entry(frame_top)
        entry2.pack(side=LEFT, padx=5, expand=True)

        but1 = Button(frame_top, text='RUN')
        but1.pack(side=RIGHT, padx=5, pady=5)

        # central panel
        frame_top = Frame(self, background='white')
        frame_top.pack(fill=BOTH, expand=True)


#
def init_gui():
    root = Tk()
    app = MainFrame(root)
    root.mainloop()


if __name__ == '__main__':
    init_gui()
