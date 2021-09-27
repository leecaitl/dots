import dots
import relationships
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, bg="white", height=900, width=1700)
canvas.pack()

if __name__ == '__main__':
    dot1 = dots.Dot(canvas, 500, 500)
    dot1.draw_dot()

    dot2 = dots.Dot(canvas, 800, 800)
    dot2.draw_dot()

    angle = relationships.angle_between(dot1, dot2)
    print(angle)

    dot1.rotate_sight(angle[0])
    dot2.rotate_sight(angle[1])

    root.mainloop()
