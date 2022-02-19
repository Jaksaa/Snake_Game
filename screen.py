from turtle import Screen

class Screen_Settings:
    def __init__(self):
        self.screen = Screen()
    def settings(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Sneko")