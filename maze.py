import tkinter as tk

walls_top = [[683, 0, 751.3, 15], [751.3, 0, 819.6, 15], [819.6, 0, 887.9, 15],
             [887.9, 0, 956.2, 15], [956.2, 0, 1024.5, 15], [1024.5, 0, 1092.8, 15],
             [1092.8, 0, 1161.1, 15], [1161.1, 0, 1229.4, 15], [1229.4, 0, 1297.7, 15],
             [1297.7, 0, 1366, 15]]
walls_bottom = [[683, 685, 751.3, 700], [751.3, 685, 819.6, 700], [819.6, 685, 887.9, 700],
                [887.9, 685, 956.2, 700], [956.2, 685, 1024.5, 700], [1024.5, 685, 1092.8, 700],
                [1092.8, 685, 1161.1, 700], [1161.1, 685, 1229.4, 700], [1229.4, 685, 1297.7, 700],
                [1297.7, 685, 1366, 700]]
walls_right = [[1351, 15, 1366, 82], [1351, 82, 1366, 149], [1351, 149, 1366, 216],
              [1351, 216, 1366, 283], [1351, 283, 1366, 350], [1351, 350, 1366, 417],
              [1351, 417, 1366, 484], [1351, 484, 1366, 551],[1351, 551, 1366, 618],
              [1351, 618, 1366, 685]]
walls_left = [[683, 15, 698, 82], [683, 82, 698, 149], [683, 149, 698, 216],
              [683, 216, 698, 283], [683, 350, 698, 417], [683, 417, 698, 484], [683, 484, 698, 551],
              [683, 551, 698, 618], [683, 618, 698, 685]]
walls_inner = [[698, 283, 751.3, 268], [751.3, 216, 766.3, 283], [751.3, 149, 766.3, 216],
               [751.3, 82, 819.6, 97],[819.6, 82, 887.9, 97], [887.9, 82, 956.2, 97],
               [956.2, 82, 1024.5, 97],[1024.5, 82, 1092.8, 97],[1077.8, 15, 1092.8, 82],
               [1092.8, 82, 1161.1, 97],[1161.1, 82, 1229.4, 97],[1297, 82, 1351, 97],
               [819.6,149,887.9,164],[887.9,149,956.2,164],[941.2,164,956.2,216],
               [956.2,201,1024.5,216],[1024.5,201,1092.8,216],[1092.8,201,1161.1,216],
               [1009.5,97,1024.5,164],[1024.5,149,1092.8,164],[1146.1,97,1161.1,201],
               [1146.1,216,1161.1,283],[1161.1, 268, 1229.4, 283],[1229.4,268,1297.7,283],
               [1282.7, 216, 1297.7,268],[1297.7,149,1351,164],[1229.4,149,1297.7,164],
               [1229.4,164,1244.4,216],

               [698,350,751.3,365],[751.3,350,766,417]
               ]
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
        self.width = 1366
        self.height = 700
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

    def add_brick(self, x, y, xmax, ymax):
        brick = Brick(self.canvas, x, y, xmax, ymax)
        self.items[brick.item] = brick
    
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Maze!')
    game = Game(root)
    game.mainloop()
