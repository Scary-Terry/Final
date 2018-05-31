import tkinter as tk

walls_top = [[0, 0, 76.25, 15], [76.25, 0, 152.5, 15], [152.5, 0, 228.75, 15],
             [305, 0, 381.25, 15], [381.25, 0, 457.5, 15], [457.5, 0, 533.75, 15],
             [533.75, 0, 610, 15]]
walls_bottom = [[0, 385, 76.25, 400], [76.25, 385, 152.5, 400], [152.5, 385, 228.75, 400],
                [305, 385, 381.25, 400], [381.25, 385, 457.5, 400], [457.5, 385, 533.75, 400],
                [533.75, 385, 610, 400]]
walls_right = [[595, 15, 610, 89], [595, 89, 610, 163], [595, 163, 610, 237],
               [595, 237, 610, 311], [595, 311, 610, 385]]
walls_left = [[0, 15, 15, 89], [0, 89, 15, 163], [0, 163, 15, 237],
              [0, 237, 15, 311], [0, 311, 15, 385]]
walls_inner = [[76.25, 15, 91.25, 89], [76.25, 89, 152.5, 104], [152.5, 89, 228.75, 104],
               [228.75, 89, 243.75, 163], [228.75, 163, 305, 178], [305, 163, 381.25, 178],
               [305, 89, 320, 163], [381.25, 15, 396.25, 89], [381.25, 89, 457.5, 104],
               [533.75, 89, 595, 104], [381.25, 163, 457.5, 178], [457.5, 163, 533.75, 178],
               [457.5, 163, 472.5, 237], [457.5, 237, 533.75, 252], [381.25, 237, 457.5, 252],
               [228.75, 237, 305, 252], [228.75, 237, 243.75, 311], [228.75, 311, 305, 326],
               [305, 311, 381.25, 326], [381.25, 311, 457.5, 326], [457.5, 311, 533.75, 326],
               [457.5, 311, 472.5, 385], [152.5, 237, 228.75, 252], [76.25, 237, 152.5, 252],
               [152.5, 163, 167.5, 237], [76.25, 163, 152.5, 178], [76.25, 237, 152.5, 252],
               [76.25, 311, 91.25, 385], [76.25, 311, 152.5, 326]]
class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)


                
class avatar(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 6
        item = canvas.create_oval(x-self.radius, y-self.radius,
                                  x+self.radius, y+self.radius,
                                  fill = 'white')
        super(avatar, self).__init__(canvas, item)
        
    def set_ball(self, ball):
        self.ball = ball

    def move(self, x_offset, y_offset):  
        coords = self.get_position()
        super(avatar, self).move(x_offset, y_offset)        


class Brick(GameObject):

    def __init__(self, canvas, x, y, xmax, ymax):
        item = canvas.create_rectangle(x, y, xmax, ymax, fill = 'red', tags= 'brick')
        super(Brick, self).__init__(canvas, item)

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.width = 1920
        self.height = 1080
        self.canvas = tk.Canvas(self, bg='blue',
                                width = self.width,
                                height=self.height,)
        self.canvas.pack()
        self.pack()
        self.items = {}
        self.ball = None
        self.avatar = avatar(self.canvas, 266.875, 392.5)
        self.items[self.avatar.item] = self.avatar
        ########################
        for values in walls_top:
            x, y, xmax, ymax = values
            self.add_brick(x, y, xmax, ymax)
        for values in walls_bottom:
            x, y, xmax, ymax = values
            self.add_brick(x, y, xmax, ymax)
        for values in walls_right:
            x, y, xmax, ymax = values
            self.add_brick(x, y, xmax, ymax)
        for values in walls_left:
            x, y, xmax, ymax = values
            self.add_brick(x, y, xmax, ymax)
        for values in walls_inner:
            x, y, xmax, ymax = values
            self.add_brick(x, y, xmax, ymax)
        ########################
        self.hud = None
        self.canvas.focus_set()

        self.canvas.bind('<Left>', lambda _: self.avatar.move(-7.5, 0))
        self.canvas.bind('<Right>', lambda _: self.avatar.move(7.5, 0))
        self.canvas.bind('<Up>', lambda _: self.avatar.move(0, -7.5))
        self.canvas.bind('<Down>', lambda _: self.avatar.move(0, 7.5))

        for values in walls_top:
            x, y, xmax, ymax = values
            ball_coords = self.avatar.get_position()
            if x <= ball_coords <= xmax:
                self.canvas.bind('<Left>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Right>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Up>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Down>', lambda _: self.avatar.move(0, 0))
            if y <= ball_coords <= ymax:
                self.canvas.bind('<Left>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Right>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Up>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Down>', lambda _: self.avatar.move(0, 0))
        for values in walls_left:
            x, y, xmax, ymax = values
            ball_coords = self.avatar.get_position()
            print(ball_coords)
            if x <= ball_coords <= xmax:
                self.canvas.bind('<Left>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Right>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Up>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Down>', lambda _: self.avatar.move(0, 0))
            if y <= ball_coords <= ymax:
                self.canvas.bind('<Left>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Right>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Up>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Down>', lambda _: self.avatar.move(0, 0))
        for values in walls_right:
            x, y, xmax, ymax = values
            ball_coords = self.avatar.get_position()
            if x <= ball_coords <= xmax:
                self.canvas.bind('<Left>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Right>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Up>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Down>', lambda _: self.avatar.move(0, 0))
            if y <= ball_coords <= ymax:
                self.canvas.bind('<Left>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Right>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Up>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Down>', lambda _: self.avatar.move(0, 0))
        for values in walls_bottom:
            x, y, xmax, ymax = values
            ball_coords = self.avatar.get_position()
            if x <= ball_coords <= xmax:
                self.canvas.bind('<Left>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Right>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Up>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Down>', lambda _: self.avatar.move(0, 0))
            if y <= ball_coords <= ymax:
                self.canvas.bind('<Left>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Right>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Up>', lambda _: self.avatar.move(0, 0))
                self.canvas.bind('<Down>', lambda _: self.avatar.move(0, 0))
    def add_brick(self, x, y, xmax, ymax):
        brick = Brick(self.canvas, x, y, xmax, ymax)
        self.items[brick.item] = brick
    
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Maze!')
    game = Game(root)
    game.mainloop()
