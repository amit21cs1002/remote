from sketchpy import canvas
import turtle
obj = canvas.sketch_from_image("D:\WhatsApp Image 2022-12-25 at 00.30.51.jpg")       # Change the path to your image           
obj.draw(threshold = 127)
turtle.done()