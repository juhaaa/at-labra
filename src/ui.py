from tkinter import IntVar, Frame, Button, Radiobutton, Label, Toplevel
from tkinter import filedialog, Tk
from PIL import ImageTk, Image, ImageDraw
from main_service import start_route_search
from map_service import binary_map_to_matrix
from config import map_dir_path

class UI:
    def __init__(self, master):
        self.master = master
        self.image = None
        self.binary_grid = None
        self.start_coords = None
        self.finish_coords = None
        self.is_selecting_start = True
        self.algorithm = IntVar()
        self.initialize_gui()
      
    def initialize_gui(self):
        self.master.title("Reitinhaku")
        self.master.minsize(500, 500)
        self.master.config(bg="goldenrod")
        self.algorithm.set(-1)
        self.toolbar_init()
        self.map_init()
        
        
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
            text="KARTTA",
            command=self.choose_image,
            bg="lemonchiffon2",
            highlightthickness = 0,
            bd = 0,
            width = 30,
            activebackground="lemonchiffon3")
        self.start_entry = Label(self.toolbar, width=30, bg="goldenrod", fg="green", font="HELVETICA")
        self.finish_entry = Label(self.toolbar, width=30, bg="goldenrod", fg="red", font="HELVETICA")
        self.coordinates_label = Label(self.toolbar, text="Koordinaatit: (0, 0)", width= 30, bg="goldenrod")
        self.toolbar.pack(side="left", fill="x", expand=True, padx=10, pady=5)
        self.start_button.pack(ipady= 10, ipadx=2, padx=10, pady=5)
        self.radio1.pack(ipady= 13, padx=10, pady=5)
        self.radio2.pack(ipady= 13, padx=10, pady=5)
        self.map_button.pack(ipady= 10, ipadx=2, padx=10, pady=5)
        self.start_entry.pack(ipady= 10, ipadx=2, padx=10, pady=0)
        self.finish_entry.pack(ipady= 10, ipadx=2, padx=10, pady=0)
        self.coordinates_label.pack(ipady= 10, ipadx=2, padx=10, pady=5)
        
    def map_init(self):
        self.toplevel = Toplevel(self.master)
        self.toplevel.config(bg="goldenrod")
        self.map = Frame(self.toplevel, bg="goldenrod")
        self.image = Label(self.map, bg="goldenrod")
        self.image.bind("<Button-1>", self.coordinates_click)
        self.image.bind("<Motion>", self.show_hovered_coordinates)
        self.image.bind("<Leave>", self.clear_hovered_coordinates)
        self.map.pack(side="right", padx=10, pady=10)
        self.image.pack()

    def choose_image(self):
        file_path = filedialog.askopenfilename(initialdir=map_dir_path,filetypes=[("Png", "*.png")])
        if file_path:
            self.img = Image.open(file_path)
            self.photo_img = ImageTk.PhotoImage(self.img)
            if self.toplevel.winfo_exists():
                self.image.config(image=self.photo_img)
            else:
                self.map_init()
                self.image.config(image=self.photo_img)
            self.binary_grid = binary_map_to_matrix(self.img)
        
    def coordinates_click(self, event):
        x, y = event.x, event.y
        if self.is_selecting_start:
            self.start_coords = (x, y)
            print(f"Alku: ({x}, {y})")
            self.is_selecting_start = False
            self.start_entry.config(text=f"Alku: ({x}, {y})") 
        else:
            self.finish_coords = (x, y)
            print(f"Loppu: ({x}, {y})")
            self.draw_coordinates(self.start_coords, "green", self.finish_coords, "red")
            self.is_selecting_start = True
            self.finish_entry.config(text=f"Loppu: ({x}, {y})")
    
    def show_hovered_coordinates(self, event):
        x, y = event.x, event.y
        coordinates_text = f"Koordinaatit: ({x}, {y})"
        self.coordinates_label.config(text=coordinates_text)
    
    def clear_hovered_coordinates(self, event):
        self.coordinates_label.config(text="Ei alueella")

    
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

    def draw_path(self, path, result):
        path_xy = [(col, row) for row, col in path]
        img_with_path = self.img.copy()
        draw = ImageDraw.Draw(img_with_path)
        if result == float("inf"):
            x, y = img_with_path.size
            x = x/2-20
            y= y/2
            draw.text(xy=(x,y), text="Ei ratkaisua", fill="red", anchor="ms")
        else:
            draw.line(path_xy, fill="blue", width=5, joint="curve")
        self.photo_img = ImageTk.PhotoImage(img_with_path)
        self.image.config(image=self.photo_img)
        
    def start_program(self):
        print(self.start_coords, self.finish_coords)
        self.result, path, visited= start_route_search(self.algorithm.get(), self.start_coords, self.finish_coords, self.binary_grid)
        self.draw_path(path, self.result)
