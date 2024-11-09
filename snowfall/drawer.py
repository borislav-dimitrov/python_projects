import tkinter
from tkinter import Canvas


class Drawer:
    snowflake_img = 'snowflake.png'

    @staticmethod
    def draw_snowflake(canvas: Canvas, x, y) -> tuple[int, tkinter.PhotoImage]:
        image = tkinter.PhotoImage(file=Drawer.snowflake_img)
        image = image.subsample(2, 2)
        snowflake_id = canvas.create_image(x, y, image=image)
        return snowflake_id, image
