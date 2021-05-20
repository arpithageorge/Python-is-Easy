def create_board(rows, columns):
    totalcol = 100
    totalrow = 10
    rows = int(rows)
    columns = int(columns)
    if columns <= totalcol and rows <= totalrow:
        for row in range(rows):
            if row % 2 == 0:
                for col in range(1, columns):
                    if col % 2 == 1:
                        if col != columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        
        return True
    else:
        
        reason = ""
        if columns > totalcol and rows > totalrow:
            reason = "columns and rows"
        elif columns > totalcol:
            reason += "columns"
        elif rows > totalrow:
            reason += "rows"
        print("Cannot create the board , too many {0:s}.".format(reason))
        return False


create_board(10, 100)