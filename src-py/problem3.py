# This is not a problem )))
# It is more like algorithm for generation of a rough surface
import time
import numpy as np
from PIL import Image, ImageTk
from Tkinter import Frame, Tk, BOTH, X, Y, RIGHT, LEFT, Text, INSERT
from ttk import Button, Entry, Label, Combobox
from matplotlib import cm


class MainFrame(Frame):

    TOP_FRAME_BACKGROUND_COLOR = 'gray75'

    w_ = 500
    h_ = 400

    a_ = 5.
    b_ = 5.

    pad_l = 10

    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')

        self.parent_ = parent

        # this is the main frame we are working on
        self.img_frame = Frame(self, background='navy')
        self.entry1 = None
        self.entry2 = None
        self.cb = None

        #
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
        frame_top = Frame(self, background=self.TOP_FRAME_BACKGROUND_COLOR)
        frame_top.pack(fill=X)

        self.cb = Combobox(frame_top, values=('Gaussian', 'Laplace'))
        self.cb.current(0)
        self.cb.pack(side=LEFT, padx=5, expand=True)

        l1 = Label(frame_top, text=r'Cx', background=self.TOP_FRAME_BACKGROUND_COLOR, width=4)
        l1.pack(side=LEFT, padx=5, expand=True)

        self.entry1 = Entry(frame_top,
                            validate='key',
                            validatecommand=(self.register(self.on_validate),
                                             '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'),
                            width=10)
        self.entry1.pack(side=LEFT, padx=5, expand=True)
        self.entry1.insert(0, str(self.a_))

        l1 = Label(frame_top, text=r'Cy', width=4, background=self.TOP_FRAME_BACKGROUND_COLOR)
        l1.pack(side=LEFT, padx=5)

        self.entry2 = Entry(frame_top,
                            validate='key',
                            validatecommand=(self.register(self.on_validate),
                                             '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'),
                            width=10)
        self.entry2.pack(side=LEFT, padx=5, expand=True)
        self.entry2.insert(0, str(self.b_))

        but1 = Button(frame_top, text='RUN', command=self.button_action)
        but1.pack(side=RIGHT, padx=5, pady=5)

        # central panel. It will have a label with an image. Image may have a random noise state, or
        # transformed image state
        self.img_frame.pack(fill=BOTH, expand=True)
        img_label = Label(self.img_frame, background=None)
        img_label.pack(expand=True, fill=BOTH, padx=5, pady=5)

    def on_validate(self, d, i, P, s, S, v, V, W):
        """
        :param d: type of action: 1 - insert, 0 - delete, -1 - other
        :param i: index of char string to be inserted/deleted, or -1
        :param P: value of the entry if the edit is allowed
        :param s: value of entry prior to editing
        :param S: the text string being inserted or deleted, if any
        :param v: the type of validation that is currently set
        :param V: the type of validation that triggered the callback
                    (key, focusin, focusout, forced)
        :param W: the tk name of the widget
        :return: True/False -> Valid / Invalid

        Found it here:
            https://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter
        Very good answer!
        """

        if d == '1':
            if W == str(self.entry1):
                try:
                    float(s + S)
                    return True
                except ValueError:
                    self.entry1.delete(0, 'end')
                    self.entry1.insert(0, s)

                    print("Not a number, entry 1")
                    return False
            if W == str(self.entry2):
                try:
                    float(s + S)
                    return True
                except ValueError:
                    self.entry2.delete(0, 'end')
                    self.entry2.insert(0, s)

                    print("Not a number, entry 2")
                    return False
        return True

    def init_random_image(self):
        """
            Create a rough surface image from a random noise
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
        if len(self.entry1.get()) > 0:
            clx = float(self.entry1.get())
        else:
            return

        if len(self.entry2.get()) > 0:
            cly = float(self.entry2.get())
        else:
            return

        #
        if self.cb.get().startswith('G'):
            # Gaussian filter
            filter_ = np.exp(-np.power(xv, 2) / clx - np.power(yv, 2) / cly)
        else:
            # Laplace filter
            filter_ = np.exp(-np.abs(xv) / clx - np.abs(yv) / cly)

        # this is a resulting map
        random_map = np.fft.ifft2(np.multiply(np.fft.fft2(random_map), np.fft.fft2(filter_)))
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
