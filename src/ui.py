from tkinter import IntVar, Frame, Button, Radiobutton, Label, Toplevel
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
from algo_service import start_route_search
from map_service import binary_map_to_matrix
from config import map_dir_path

class UI:
    """Luokka joka vastaa graafisesta käyttöliittymästä
    """
    def __init__(self, master):
        self.master = master
        self.image = None
        self.binary_grid = None
        self.start_coords = None
        self.finish_coords = None
        self.result = None
        self.visited = None
        self.is_selecting_start = True
        self.algorithm = IntVar()
        self.initialize_gui()

    def initialize_gui(self):
        """Metodi rakentaa käyttöliittymän
        """
        self.master.title("Reitinhaku")
        self.master.minsize(500, 500)
        self.master.config(bg="goldenrod")
        self.algorithm.set(-1)
        self.toolbar_init()
        self.map_init()

    def toolbar_init(self):
        """Metodi rakentaa valikon
        """
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
            text="A*",
            variable=self.algorithm,
            value=2, bg="lemonchiffon2",
            highlightthickness = 0,
            bd=0,
            width=30,
            activebackground="lemonchiffon3")
        self.radio3 = Radiobutton(
            self.toolbar,
            text="JPS",
            variable=self.algorithm,
            value=3, bg="lemonchiffon2",
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
        self.start_entry = Label(self.toolbar,
                                 width=30,
                                 bg="goldenrod",
                                 fg="green",
                                 font="HELVETICA")
        self.finish_entry = Label(self.toolbar,
                                  width=30,
                                  bg="goldenrod",
                                  fg="red",
                                  font="HELVETICA")
        self.coordinates_label = Label(self.toolbar,
                                       text="Koordinaatit: (0, 0)",
                                       width= 30,
                                       bg="goldenrod")
        self.toolbar.pack(side="left", fill="x", expand=True, padx=10, pady=5)
        self.start_button.pack(ipady= 10, ipadx=2, padx=10, pady=5)
        self.radio1.pack(ipady= 13, padx=10, pady=5)
        self.radio2.pack(ipady= 13, padx=10, pady=5)
        self.radio3.pack(ipady= 13, padx=10, pady=5)
        self.map_button.pack(ipady= 10, ipadx=2, padx=10, pady=5)
        self.start_entry.pack(ipady= 10, ipadx=2, padx=10, pady=0)
        self.finish_entry.pack(ipady= 10, ipadx=2, padx=10, pady=0)
        self.coordinates_label.pack(ipady= 10, ipadx=2, padx=10, pady=5)

    def map_init(self):
        """Metodi rakentaa karttaikkunan"""
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
        """Metodi kuvatiedoston avaamiseksi
        """
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
        """Metodi alku- ja loppukoordinaattien rekisteröintiin

        Args:
            event (tuple): (int, int)
        """
        x, y = event.x, event.y
        if self.is_selecting_start:
            self.start_coords = (x, y)
            print(f"Alku: ({x}, {y})")
            self.is_selecting_start = False
            self.start_entry.config(text=f"Alku: ({x}, {y})")
        else:
            self.finish_coords = (x, y)
            print(f"Loppu: ({x}, {y})")
            self.draw_coordinates()
            self.is_selecting_start = True
            self.finish_entry.config(text=f"Loppu: ({x}, {y})")

    def show_hovered_coordinates(self, event):
        """Metodi osoittimen sijainnin näyttämiseksi

        Args:
            event (tuple): (int, int)
        """
        x, y = event.x, event.y
        coordinates_text = f"Koordinaatit: ({x}, {y})"
        self.coordinates_label.config(text=coordinates_text)

    def clear_hovered_coordinates(self, event):
        """Metodi osoittaa käyttäjälle kun osoitin ei ole alueella
        """
        self.coordinates_label.config(text="Ei alueella")

    def draw_coordinates(self, with_path=False, draw=None):
        """Metodi piirtää aloitus- ja lopetuspisteet kartalle
        Jos operaatiota ei suoriteta samanaikaisesti polun piirtämisen kanssa, luodaan
        uusi Imagedraw- objekti ja käytetään sitä.

        Args:
            with_path (bool, optional): Default = False.
            draw (PIL.ImageDraw.ImageDraw, optional): Default = None.
        """
        if not with_path:
            img_with_coords = self.img.copy()
            draw = ImageDraw.Draw(img_with_coords)
        draw.rectangle([self.start_coords[0]-5,
                        self.start_coords[1]-5,
                        self.start_coords[0]+5,
                        self.start_coords[1]+5],
                        outline="green",
                        fill="green")
        draw.rectangle([self.finish_coords[0]-5,
                        self.finish_coords[1]-5,
                        self.finish_coords[0]+5,
                        self.finish_coords[1]+5],
                        outline="red",
                        fill="red")
        if not with_path:
            self.photo_img = ImageTk.PhotoImage(img_with_coords)
            self.image.config(image=self.photo_img)

    def draw_visited(self, visited, draw):
        """Metodi piirtää vierallut solmut kartalle

        Args:
            visited (List): Vieraillut solmut (True/False)
            draw (PIL.Imagedraw.ImageDraw): Imagedraw objekti joka toimii alustana
        """
        rows = len(visited)
        cols = len(visited[0])
        for row in range(rows):
            for col in range(cols):
                if visited[row][col]:
                    draw.rectangle([col, row, col, row], fill="rgb(102,255,153)")

    def draw_path(self, path, result, visited):
        """Metodi piirtää haun tuloksen käytetylle kuvatiedostolle ja
        kutsuu avukseen draw_visited ja draw_coordinates metodeja.
        Jos ratkaisua ei ole kirjoitetaan kuvan päälle ei ratkaisua.

        Args:
            path (_type_): _description_
            result (_type_): _description_
            visited (_type_): _description_
        """
        img_with_path = self.img.copy()
        draw = ImageDraw.Draw(img_with_path)
        if result == float("inf"):
            xc, yc = img_with_path.size
            xc = xc/2-20
            yc= yc/2
            self.draw_visited(visited, draw)
            draw.text(xy=(xc,yc), text="Ei ratkaisua", fill="red", anchor="ms")
        else:
            self.draw_visited(visited, draw)
            draw.line(path, fill="blue", width=5)
            self.draw_coordinates(True, draw)
        self.photo_img = ImageTk.PhotoImage(img_with_path)
        self.image.config(image=self.photo_img)
        
    def start_program(self):
        """Metodi käynnistää reitinhaun
        """
        self.result, path, self.visited= start_route_search(self.algorithm.get(),
                                                       self.start_coords,
                                                       self.finish_coords,
                                                       self.binary_grid)
        self.draw_path(path, self.result, self.visited)
