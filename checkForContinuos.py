def checkForContinuous(b_field: list, shapes: list) -> bool:
    for y in range(len(b_field)):
        for x in range(len(b_field[y])):
            for shape in shapes:
                mode = True
                for x1, y1 in shape.figure:
                    if (y + y1) >= len(b_field) or (x + x1) >= len(b_field[y + y1]) or b_field[y + y1][x + x1]:
                        mode = False
                        break

                if mode:
                    return True

    return False
