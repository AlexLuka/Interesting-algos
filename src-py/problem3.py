# This is not a problem )))
# It is more like algorithm for generation of a rough surface
import time
import numpy as np
from PIL import Image, ImageTk
from Tkinter import Frame, Tk, BOTH, X, Y, RIGHT, LEFT
from ttk import Button, Entry, Label, Combobox


class MainFrame(Frame):

    w_ = 500
    h_ = 400

    pad_l = 10

    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')

        self.parent_ = parent

        # this is the main frame we are working on
        self.img_frame = Frame(self, background='navy')
        self.init_ui()
        self.centering()

        # broken TV app))
        # while True:
        self.init_random_image()
        # time.sleep(0.05)

    def centering(self):
        pos_x = (self.parent_.winfo_screenwidth() - self.w_) / 2
        pos_y = (self.parent_.winfo_screenheight() - self.h_) / 2

        self.parent_.geometry('{}x{}+{}+{}'.format(self.w_, self.h_, pos_x, pos_y))

    def init_ui(self):
        self.parent_.title('Rough surface generator')
        self.pack(fill=BOTH, expand=True)

        # top panel with controls
        frame_top = Frame(self, background='gray75')
        frame_top.pack(fill=X)

        cb = Combobox(frame_top, values=('Gaussian', 'Laplace'))
        cb.current(0)
        cb.pack(side=LEFT, padx=5, expand=True)

        entry1 = Entry(frame_top)
        entry1.pack(side=LEFT, padx=5, expand=True)

        entry2 = Entry(frame_top)
        entry2.pack(side=LEFT, padx=5, expand=True)

        but1 = Button(frame_top, text='RUN', command=self.button_action)
        but1.pack(side=RIGHT, padx=5, pady=5)

        # central panel. It will have a label with an image. Image may have a random noise state, or
        # transformed image state
        self.img_frame.pack(fill=BOTH, expand=True)

        img_label = Label(self.img_frame, background=None)
        img_label.pack(expand=True, fill=BOTH, padx=5, pady=5)

    def init_random_image(self):
        """
            Init white noise image on the main panel
        """
        self.update()

        img = ImageTk.PhotoImage(
            Image.fromarray(
                np.random.random_integers(0, 255,
                                          (self.img_frame.winfo_height()-self.pad_l,
                                           self.img_frame.winfo_width()-self.pad_l)).astype(np.int32)
            ).convert('I')
        )

        keys = self.img_frame.children.keys()
        for key in keys:
            self.img_frame.children[key].configure(image=img)
            self.img_frame.children[key].image = img

    def button_action(self):
        """
            Update the main panel: if it contains white noise -> transform it
                                   if it contains transformed image -> remove it and create white noise
        """
        self.init_random_image()


#
def init_gui():
    root = Tk()
    app = MainFrame(root)
    root.mainloop()


if __name__ == '__main__':
    init_gui()
