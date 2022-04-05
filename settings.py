# settings of window
width, height = 17, 17

# Coordinates of field on window
x, y = 1, 1

# Size of field
f_width, f_height = width - 2 * x, 9

# size unit
block = 40

# Size of block
tall = 39

# Panel Size
p_width, p_height = 5, height - 6

# Size of mini block
smalltall = (tall + 1) // 2

# Shape surface size and poses of surfaces
shapeSurfaceWidth = 7
shapeSurfaceHeight = 7

collision = int(((width - 2 * x) // 3 * block - shapeSurfaceWidth * smalltall) / 2)

shapeSurfaceOneX = block * x
shapeSurfaceTwoX = block * (1 * (width - 2 * x) // 3 + x) + collision
shapeSurfaceThreeX = block * (2 * (width - 2 * x) // 3 + x) + 2 * collision

shapeSurfaceY = int((height - 5.5) * block)

# Pictures
bPictures = ["blue", "green", "pink", "purple", "red", "sky", "white", "yellow"]

# loss
OVER, CONTINUE, JUMP, MENU = 0, 1, 2, 3

# Colours
window = (30, 30, 30)
panelColour = (22, 22, 22)
shapeColour = (255, 0, 0)
borderFieldColour = (80, 80, 80)
borderSurfaceColour = (0, 0, 0)
fieldColour = (185, 185, 185)
shadowBlock = (200, 100, 100)
surfaceColour = (40, 40, 40)
textColour = (255, 255, 255)

# Various of shapes
figures = {
    (((0, 0), (0, 1), (0, 2), (0, 3)), (1, 4)),
    (((0, 0), (0, 1), (0, 2)), (1, 3)),
    (((0, 0), (1, 0), (2, 0)), (3, 1)),
    (((0, 0), (1, 0), (2, 0), (3, 0)), (4, 1)),
    (((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)), (3, 3)),
    (((0, 0), (1, 0), (1, 1)), (2, 2)),
    (((0, 0), (0, 1), (1, 1)), (2, 2)),
    (((0, 1), (0, 0), (1, 0)), (2, 2)),
    (((0, 1), (1, 1), (1, 0)), (2, 2)),
    (((0, 0), ), (1, 1)),
    (((0, 0), (0, 1)), (1, 2)),
    (((0, 0), (1, 0)), (2, 1)),
    (((0, 2), (1, 2), (1, 1), (1, 0)), (2, 3)),
    (((0, 0), (1, 0), (1, 1), (2, 1)), (3, 2)),
    (((0, 1), (1, 1), (1, 0), (2, 0)), (3, 2)),
    (((0, 0), (0, 1), (1, 1), (2, 1), (2, 0)), (3, 2)),
    (((0, 1), (0, 0), (1, 0), (2, 0), (2, 1)), (3, 2)),
    (((0, 0), (0, 1), (0, 2), (0, 3), (1, 3)), (2, 4)),
    (((0, 1), (1, 1), (1, 0), (1, 2), (2, 1)), (3, 3)),
    (((0, 0), (0, 1), (1, 1), (1, 0)), (2, 2))
}
