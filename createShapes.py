from shape import Shape
from settings import figures, shapeSurfaceOneX, shapeSurfaceTwoX, shapeSurfaceThreeX
from random import choice


def createShapes(shapes: list, destroy: list, b_field: list):
    shapeSurfacesX = [shapeSurfaceOneX, shapeSurfaceTwoX, shapeSurfaceThreeX]
    for i in range(3):
        figure = choice(list(figures))

        shapes.append(Shape(figure, shapeSurfacesX[i], destroy, b_field))

        shapes[-1].init_images()
        shapes[-1].init_shape()
