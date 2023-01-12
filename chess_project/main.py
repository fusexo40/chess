from voice import record_volume, get_coords
from table import generate_table, print_table

table = generate_table()
print_table(table)
while (1):
    coords = get_coords()
    from_coord = coords[0]
    to_coord = coords[1]
    print(table[from_coord[0]][from_coord[1]], table[to_coord[0]][to_coord[1]], sep="\n")
    table[from_coord], table[to_coord] == table[to_coord], table[from_coord]
    print_table(table)

