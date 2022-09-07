from tkinter import *

value = 0

def check_win():
    pass

def restart():
    pass

def insert_value(row, column):
    global value
    if value > 0 and value < 10 and button_values[row][column] == 0:
        buttons[row][column].config(text=str(value))
        button_values[row][column] = value
        button_values_y[column][row] = value
        #calculation of block values
        if row<3:
            block_row = 0
        elif row>5:
            block_row = 2
        else:
            block_row = 1
        if column<3:
            block_column = 0
        elif column>5:
            block_column = 2
        else:
            block_column = 1
        # from 3 base to 10 base convert
        block_number = int((str(block_row)+str(block_column)), 3)
        print(block_number)
        in_block_row = row%3
        in_block_column = column%3
        in_block_number = int((str(in_block_row)+str(in_block_column)), 3)
        print(in_block_number)
        button_values_block[block_number][in_block_number] = value
    else:
        print("invalid number")

def value_giving(num):
    global value
    value = num+1

def check_errors():
    for i in range (9):
        all_recurring_x = []
        all_recurring_y = []
        all_recurring_blocks = []
        for num in range(9):
            recurring_idx = (find_duplicates(button_values[i], (num+1)))
            if recurring_idx != []:
                all_recurring_x.extend(recurring_idx)

            recurring_idy = (find_duplicates(button_values_y[i], (num+1)))
            if recurring_idy != []:
                all_recurring_y.extend(recurring_idy)

            recurring_id_block = (find_duplicates(button_values_block[i], (num+1)))
            if recurring_id_block != []:
                all_recurring_blocks.extend(recurring_id_block)

            highlight_errors(all_recurring_x, all_recurring_y, i, all_recurring_blocks)

def highlight_errors(x,y,i, block):
    [buttons[i][step].config(bg="#ff7290") for step in range(9) if x != [] and buttons[i][step]['bg'] != "#ff4658"]
    [buttons[step][i].config(bg="#ff7290") for step in range(9) if y != [] and buttons[step][i]['bg'] !="#ff4658"]
    for pizda in range (3):
        for mocha in range(3):
            if block!= [] and buttons[pizda][mocha]['bg'] !="#ff4658":
                thing = i//3
                buttons[pizda+thing*3][mocha+((i-(thing*3))*3)].config(bg="#ff7290")
    [buttons[i][idx].config(bg="#ff4658") for idx in x]
    [buttons[idx][i].config(bg="#ff4658") for idx in y]
    print(x)

def find_duplicates(lst, item):
    placeholder = [i for i, x in enumerate(lst) if x == item]
    if len(placeholder) > 1:
        return placeholder
    else:
        return []

button_values = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

button_values_y = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

button_values_block = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]
window = Tk()
window.title("sudoku")
# container for grids
babushka = Frame(window, bg="#148869")
babushka.pack(expand=True, fill=BOTH)
# grid of values to choose
lol = Frame(babushka)
lol.grid(row=0, column=0)
available_numbers = [Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()]
for num in range(9):
    available_numbers[num] = Button(lol, text=str(num+1), width=5, height=4, bg="#d83999", command=lambda num=num: value_giving(num))
    available_numbers[num].grid(in_=lol, row=0, column=num)

buttons = [[Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()],
            [Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()],
            [Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()],
            [Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()],
            [Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()],
            [Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()],
            [Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()],
            [Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()],
            [Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()]]
# grid of main buttons
frame = Frame(babushka)
frame.grid(row=1, column=0)
for row in range(9):
    for column in range(9):
        buttons[row][column] = Button(frame, text="", width=5, height=4, bg="gray", command= lambda row=row, column=column: insert_value(row, column))
        buttons[row][column].grid(row=row, column=column)
# check button, obviously
check_button = Button(babushka, text="check\nerrors",height=50, bg="#ffdbff", command= check_errors)
check_button.grid(row=0, column=1, rowspan=2, sticky=E)


window.mainloop()
