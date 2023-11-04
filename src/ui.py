from tkinter import IntVar, Frame, Button, Radiobutton, Label
from tkinter import filedialog, Tk
from PIL import ImageTk, Image, ImageDraw
from main_service import start_route_search

class UI:

    def __init__(self, master):
        self.master = master
        self.start_coords = None
        self.finish_coords = None
        self.is_selecting_start = True
        self.algorithm = IntVar()
        self.initialize_gui()
      
    def initialize_gui(self):
        self.master.title("Reitinhaku")
        self.master.minsize(1100, 900)
        self.master.config(bg="goldenrod")
        self.toolbar_init()
        self.map_init()
        self.algorithm.set(-1)
        self.toolbar.pack(side="left", fill="x", expand=True, padx=10, pady=5)
        self.map.pack(side="right", padx=10, pady=10)
        self.start_button.pack(ipady= 10, ipadx=2, padx=10, pady=5)
        self.radio1.pack(ipady= 13, padx=10, pady=5)
        self.radio2.pack(ipady= 13, padx=10, pady=5)
        self.map_button.pack(ipady= 10, ipadx=2, padx=10, pady=5)
        self.image.pack()
        
    def toolbar_init(self):
        self.toolbar = Frame(self.master, bg="goldenrod")
        self.start_button = Button(
            self.toolbar,
            text="Start",
            bg="palegreen4",
            borderwidth=0,
            command=self.start_program,
            highlightthickness = 0, bd=0,
            width=30,
            activebackground="seagreen3")
        self.radio1 = Radiobutton(
            self.toolbar,
            text="DIJKSTRA",
            variable=self.algorithm,
            value=1,
            bg="lemonchiffon2",
            highlightthickness = 0,
            bd=0,
            width=30,
            activebackground="lemonchiffon3")
        self.radio2 = Radiobutton(
            self.toolbar,
            text="JPS",
            variable=self.algorithm,
            value=2, bg="lemonchiffon2",
            highlightthickness = 0,
            bd=0,
            width=30,
            activebackground="lemonchiffon3")
        self.map_button = Button(
            self.toolbar,
            text="MAP",
            command=self.choose_image,
            bg="lemonchiffon2",
            highlightthickness = 0,
            bd = 0,
            width = 30,
            activebackground="lemonchiffon3")
        
    def map_init(self):
        self.map = Frame(self.master, bg="goldenrod")
        self.image = Label(self.map, bg="goldenrod")
        self.image.bind("<Button-1>", self.coordinates_click)

    def choose_image(self):
        file_path = filedialog.askopenfilename(initialdir="map",filetypes=[("Png", "*.png")])
        if file_path:
            self.img = Image.open(file_path)
            self.photo_img = ImageTk.PhotoImage(self.img)
            self.image.config(image=self.photo_img)
        
    def coordinates_click(self, event):
        x, y = event.x, event.y
        if self.is_selecting_start:
            self.start_coords = (x, y)
            print(f"Alku: ({x}, {y})")
            self.is_selecting_start = False    
        else:
            self.finish_coords = (x, y)
            print(f"Loppu: ({x}, {y})")
            self.draw_coordinates(self.start_coords, "green", self.finish_coords, "red")
            self.is_selecting_start = True
    
    def insert_coordinates():
        #koordinaatit käsin syötettynä
        pass

    def draw_coordinates(self, coords, color, coords2, color2):
        img_with_coords = self.img.copy()
        draw = ImageDraw.Draw(img_with_coords)
        draw.rectangle([coords[0]-5, coords[1]-5, coords[0]+5, coords[1]+5], outline=color, fill=color)
        draw.rectangle([coords2[0]-5, coords2[1]-5, coords2[0]+5, coords2[1]+5], outline=color2, fill=color2)
        self.photo_img = ImageTk.PhotoImage(img_with_coords)
        self.image.config(image=self.photo_img)

    def start_program(self):
        print(self.start_coords, self.finish_coords)
        print(self.algorithm.get())
        start_route_search(self.algorithm, self.start_coords, self.finish_coords)

if __name__ == "__main__":
    root = Tk()
    ui = UI(root)
    root.mainloop()
