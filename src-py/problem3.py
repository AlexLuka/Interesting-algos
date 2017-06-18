# This is not a problem )))
# It is more like algorithm for generation of a rough surface
import time
import numpy as np
from PIL import Image, ImageTk
from Tkinter import Frame, Tk, BOTH, X, Y, RIGHT, LEFT
from ttk import Button, Entry, Label, Combobox
from matplotlib import cm


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
        self.state = 0
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

        # set a colormap
        c_map = cm.get_cmap('bwr')

        # width and height of the image
        w_ = self.img_frame.winfo_width()-self.pad_l
        h_ = self.img_frame.winfo_height()-self.pad_l

        # generate random noise
        random_map = np.random.random((h_, w_))

        # generate a meshgrid for the filter
        xv, yv = np.meshgrid(np.linspace(-int(w_ / 2.), int(w_ / 2.), w_),
                             np.linspace(-int(h_ / 2.), int(h_ / 2.), h_))

        # define correlation length and width
        clx = 100
        cly = 50

        # this is a gauss filter
        filter_gauss = np.exp(-np.power(xv, 2) / clx - np.power(yv, 2) / cly)

        # this is a resulting map
        random_map = np.fft.ifft2(np.multiply(np.fft.fft2(random_map), np.fft.fft2(filter_gauss)))
        random_map = np.real(random_map)

        # normalize to [0, 1]
        random_map -= np.min(random_map)
        random_map /= np.max(random_map)

        # create PhotoImage object to add on the panel
        img = ImageTk.PhotoImage(
            Image.fromarray(
                # image really likes unsigned ints))
                np.uint8(
                    # convert to colormap you like
                    c_map(
                        # give a random image to color map with values between 0 and 1
                        # np.random.random(
                        #     (self.img_frame.winfo_height()-self.pad_l, self.img_frame.winfo_width()-self.pad_l)
                        # )
                        random_map
                    )*255
                )
            )
        )

        # Gray colormap
        # img = ImageTk.PhotoImage(
        #     Image.fromarray(np.random.random_integers(0, 255,
        #                                   (self.img_frame.winfo_height()-self.pad_l,
        #                                    self.img_frame.winfo_width()-self.pad_l)).astype(np.int8)
        #                     ).convert('L')
        # )

        keys = self.img_frame.children.keys()
        for key in keys:
            self.img_frame.children[key].configure(image=img)
            self.img_frame.children[key].image = img

    def button_action(self):
        """
        """
        self.init_random_image()


#
def init_gui():
    root = Tk()
    app = MainFrame(root)
    root.mainloop()


if __name__ == '__main__':
    init_gui()
