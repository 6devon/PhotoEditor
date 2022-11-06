#packages

from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog
import cv2

def save_images():
    img = ImageTk.getimage(panelA.image).convert('RGB')
    img.save("zdj1.jpg")

    img = ImageTk.getimage(panelB.image).convert('RGB')
    img.save("zdj2.jpg")


def select_image():
    global panelA, panelB #reference to image panels

    path = tkinter.filedialog.askopenfilename() #open a file chooser dialog and allow user to select input image

    #ensurance that path was selected
    if len(path) > 0:
        #loading the image from disc, cover it to greyscale, detect edges in it

        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)
        #swap channels from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #convert images to pil format
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)

        #convert ro imagetk format
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)
        #iff panels are none inicialize them
        if panelA is None or panelB is None:
            #the firt panel stores the original pic
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side = "right", padx = 10, pady = 10)

            #second panel stores edge map
            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side = "right", padx = 10, pady = 10)
        
        #otherwise update the panels
        else:
            panelA.configure(image = image)
            panelB.configure(image = edged)
            panelA.image = image
            panelB.image = edged

#inicialize the window toolkit

root = Tk()
root.title("Photo editor")
panelA = None
panelB = None

menu = Menu(root)
submenu = Menu(menu,tearoff = 0)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label = "Save files", command = save_images)

root.config(menu = menu, width=50,height=30)


#creating a button, when pressed triggers file chooser dialog and allow the user to select an image
btn = Button(root, text = "Select an image", command = select_image)
btn.pack(side = "bottom", fill = "both", expand = "Yes", padx = "10", pady = "10")

#kick off the gui

root.mainloop()
