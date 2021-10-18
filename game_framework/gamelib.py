import tkinter as tk
import tkinter.ttk as ttk

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500
TIMER_DELAY = 33


class GameCanvasElement():
    """Base class for an element on the game canvas, with attributes:
    x = x-coordinate of object's image
    y = y-coordinate of object's image
    canvas = reference to the game canvas
    canvas_object_id = id of the object, used to manipulate it using canvas
    is_visible = boolean flag if element is visible.
    By default the (x,y) coordinate are at the center of the image,
    but this can be changed by subclasses or calls to canvas.itemconfigure().
    """

    def __init__(self, game_app, x=0, y=0):
        self.x = x
        self.y = y
        self.canvas = game_app.canvas

        self.is_visible = True

        self.init_canvas_object()
        self.init_element()

    def show(self):
        self.is_visible = True
        self.canvas.itemconfigure(self.canvas_object_id, state="normal")

    def hide(self):
        self.is_visible = False
        self.canvas.itemconfigure(self.canvas_object_id, state="hidden")

    def render(self):
        if self.is_visible:
            self.canvas.coords(self.canvas_object_id, self.x, self.y)

    def init_canvas_object(self):
        """A method that a subclass can override to init it self after
        it has been added to the canvas
        """
        pass

    def init_element(self):
        pass

    def update(self):
        """Update the object to emulate animation.
        """
        pass


class Text(GameCanvasElement):
    def __init__(self, game_app, text, x=0, y=0):
        self.text = text
        super().__init__(game_app, x, y)

    def init_canvas_object(self):
        self.canvas_object_id = self.canvas.create_text(
            self.x,
            self.y,
            text=self.text)

    def set_text(self, text):
        self.text = text
        self.canvas.itemconfigure(self.canvas_object_id, text=text)


class Sprite(GameCanvasElement):
    def __init__(self, game_app, image_filename, x=0, y=0):
        self.image_filename = image_filename
        super().__init__(game_app, x, y)

    def init_canvas_object(self):
        self.photo_image = tk.PhotoImage(file=self.image_filename)
        self.canvas_object_id = self.canvas.create_image(
            self.x,
            self.y,
            image=self.photo_image)


class GameApp(ttk.Frame):
    """Base class for a game.  This class creates a canvas, manages
    a collection of game elements, and controls animation.
    It provides several call-back methods for initializing elements
    on the canvas, start/stop animation, and running the animation loop.
    """

    def __init__(self, parent,
                 canvas_width=CANVAS_WIDTH,
                 canvas_height=CANVAS_HEIGHT,
                 update_delay=TIMER_DELAY):
        super().__init__(parent)
        self.parent = parent

        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.update_delay = update_delay

        self.grid(sticky=tk.NSEW)
        self.canvas = self.create_canvas(canvas_width, canvas_height)

        self._elements = []
        self.init_game()

        self.parent.bind('<KeyPress>', self.on_key_pressed)
        self.parent.bind('<KeyRelease>', self.on_key_released)

    def create_canvas(self, width, height):
        canvas = tk.Canvas(self, borderwidth=0,
                           width=width, height=height,
                           highlightthickness=0)
        canvas.grid(sticky=tk.NSEW)
        return canvas

    def animate(self):
        self.pre_update()

        for element in self._elements:
            element.update()
            element.render()

        self.post_update()

        self.after(self.update_delay, self.animate)

    def add_element(self, element: GameCanvasElement):
        """Add an element to the Game.
        Args:
            element (GameCanvasElement): The element you want to add.
        """
        self._elements.append(element)

    def remove_element(self, element: GameCanvasElement):
        """Remove the element from the Game
        Args:
            element (GameCanvasElement): [description]
        """
        if element in self._elements:
            self._elements.remove(element)
            self.canvas.delete(element.canvas_object_id)

    def start(self):
        self.after(0, self.animate)

    def init_game(self):
        pass

    def pre_update(self):
        pass

    def post_update(self):
        pass

    def on_key_pressed(self, event):
        pass

    def on_key_released(self, event):
        pass