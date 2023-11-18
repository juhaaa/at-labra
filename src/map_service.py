def binary_map_to_matrix(map):
    """Funktio muuttaa Photoimage- olion binäärimatriisiksi

    Args:
        map (PhotoImage): png - kartta PhotoImage- oliona

    Returns:
        list: binäärimatriisi
    """
    
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

    return binary_grid
