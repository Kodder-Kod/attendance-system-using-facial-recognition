my_rectangle = self.round_rectangle1(root, 50, 50, 700, 200, radius=30, p=100, q=100, fill="navy")


# das=Label(pop, text='').place(x=100,y=100)

def round_rectangle1(self, root, x1, y1, x2, y2, radius, p, q, **kwargs):
    canvas = Canvas(root)
    canvas.place(x=p, y=q)
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


