import pyxel


class App:
    def __init__(self):
        pyxel.init(256,256)

        pyxel.run(self.update(),self.draw())

    def update():
        pass

    def draw():
        pass

App()