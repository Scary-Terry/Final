import tkinter as tk

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
    def __init__(self,canvas, x, y):
        self.radius = 5
        self.ball = None
        item = canvas.create_oval(x-self.radius, y-self.radius,
                                  x+self.radius, y+self.radius,
                                  fill = 'red')
        super(avatar, self).__init__(canvas, item)

    def set_ball(self, ball):
        self.ball = ball

    def move(self, offset):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] +offset >= 0 and coords[2] + offset <=width:
            super(avatar, self).move(offset, 0)
            


class Brick(GameObject):
    COLORS = {1: '#999999', 2: '#555555', 3:'#222222'}

    def __init__(self, canvas, x, y, hits):
        self.width = 20
        self.height = 75
        self.hits = hits
        color = Brick.COLORS[hits]
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill = color, tags= 'brick')
        super(Brick, self).__init__(canvas, item)

    def hit(self):

        self.hits -=1
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item,
                                   fill = Brick.COLORS[self.hits])

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg='#aaaaff',
                                width = self.width,
                                height=self.height,)
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball = None
        self.avatar = avatar(self.canvas, self.width/2, 326)
        self.items[self.avatar.item] = self.avatar
        for x in range(5, self.width - 5, 75):
            self.add_brick(x + 37.5, 50, 2)
            self.add_brick(x + 37.5, 70, 1)
            self.add_brick(x + 37.5, 90, 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()

        self.canvas.bind('<Left>', lambda _: self.avatar.move(-10))
        self.canvas.bind('<Right>', lambda _: self.avatar.move(10))
        self.canvas.bind('<Up>', lambda _: self.avatar.move(0, 10))
        
    def setup_game(self):
        self.update_lives_text()
        self.text = self.draw_text(300, 200,
                                   'Press Space to start')
        self.canvas.bind('<space>', lambda _: self.start_game())

    def add_brick(self, x, y, hits):
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size='40'):
        font = ('Helvetica', size)
        return self.canvas.create_text(x, y, text=text, font=font)

    def update_lives_text(self):
        text = 'Lives: %s' %self.lives
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        self.canvas.unbind('<space>')
        self.canvas.delete(self.text)
        self.game_loop()

    def game_loop(self):
        self.check_collisions()
        num_bricks = len(self.canvas.find_withtag('brick'))
        if num_bricks == 0:
            self.ball.speed = None
            self.draw_text(300, 200, 'You Win!')
        elif self.ball.get_position()[3] >= self.height:
            self.ball.speed = None
            self.lives -= 1
            if self.lives < 0:
                self.draw_text(300, 200, 'Game Over')
            else:
                self.after(1000, self.setup_game)
        else:
            self.ball.update()
            self.after(50, self.game_loop)

    def check_collisions(self):
        ball_coords = self.ball.get_position()
        items = self.canvas.find_overlapping(*ball_coords)
        objects = [self.items[x] for x in items if x in self.items]
        self.ball.collide(objects)
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Maze!')
    game = Game(root)
    game.mainloop()
