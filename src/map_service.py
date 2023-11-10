def binary_map_to_matrix(map):
    
    binary_grid = []
    img = map.convert("L") 
    for y in range(img.height):
        row = []
        for x in range(img.width):
            coordinate = img.getpixel((x,y))
            if coordinate > 128:
                row.append(0)
            else:
                row.append(1)
        binary_grid.append(row)

    print(len(binary_grid[0]))
    print(len(binary_grid))

    return binary_grid
