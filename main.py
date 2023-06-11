# Простое
# Нарисовать квадратик со звездочек(пользователь вводит диагональ)

def right_diagonal(s):
    for i in range(s):
        for j in range(s):
            if i == j or i == 0 or j == 0 or i == s - 1 or j == s - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def left_diagonal(s):
    for i in range(s):
        for j in range(s):
            if i == s - j - 1 or i == 0 or j == 0 or i == s - 1 or j == s - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def l_r_diagonals(s):
    for i in range(s):
        for j in range(s):
            if i == j or i == s - j - 1 or i == 0 or j == 0 or i == s - 1 or j == s - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")


arr = [right_diagonal, left_diagonal, l_r_diagonals]

while True:
    choice = abs(int(input(
        "Enter number from 0 ... to 3: \n1 -> show right diagonal in square, 2 -> show left diagonal in square, 3 -> show right and left diagonals in square, 0 -> Exit\n")))

    if choice == 0:
        print("Exit")
        break
    elif choice >= 1 and choice <= 3:
        s = abs(int(input("Enter number from 5 ... to 100 for drawing diagonal in a square: \n\n")))
        val = arr[choice - 1 ]
        val(s)
    else:
        print("Enter correct value -> ")


# Среднее
# Нарисовать ромб со звездочек(пользователь вводит диагональ)

def hv_diamond(s):
    print("Your vertical diagonal is -> " + str(s * 2) + " and your horizontal diagonal is -> " + str(s))
    if s % 2 != 0:
        s1 = int(( s / 1) / 2)
        s2 = int(3 * s / 2 - 1)
        for i in range(0, s):
            for j in range(0, s):
                if i + j == s1 or i - j == s1 or j - i == s1 or i + j == s2 or i == s1 or j == s1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
        print("Please enter correct number (it should be odd) -> ")


def h_diamond(s):
    print("Your horizontal diagonal is: " + str(s))
    if s % 2 != 0:
        s1 = int((s / 1) / 2)
        s2 = int(3 * s / 2 - 1)
        for i in range(0, s):
            for j in range(0, s):
                if i + j == s1 or i - j == s1 or j - i == s1 or i + j == s2 or i == s1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
        print("Please enter correct number (it should be odd) -> ")

def v_diamond(s):
    print("Your vertical diagonal is: " + str(s*2))
    if s % 2 != 0:
        u1 = int((s/1)/2)
        u2 = int(3*s/2-1)
        for i in range(0, s):
            for j in range(0, s):
                if i+j == u1 or i-j == u1 or j-i == u1 or i+j == u2 or j == u1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
        print("Please enter correct number (it should be odd) -> ")


d_diamond = [hv_diamond, h_diamond, v_diamond]

while True:
    choice = abs(int(input("Choose an action with a diamond, 1 - show vertical and horizontal diagonals, 2 - show only horizontal diagonal of diamond, 3 - show only vertical diagonal of diamond, 0 - exit ->\t")))

    if choice == 0:
        print("Exit")
        break
    elif choice >= 1 and choice <= 3:
        s = abs(int(input("Enter the number: ")))
        val = d_diamond[choice - 1]
        val(s)
    else:
        print("Enter correct number from 0 to 3")


# Сложное
# Нарисовать не заполненный квадрат с заполненными диагоналями внутри. Все с использованием только цикла for

def main_diagonal(s):
    for i in range(s):
        for j in range(s):
            if i == j or i == 0 or j == 0 or i == s - 1 or j == s - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def side_diagonal(s):
    for i in range(s):
        for j in range(s):
            if i == s - j - 1 or i == 0 or i == s - 1 or j == 0 or j == s - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def all_diagonals(s):
    for i in range(s):
        for j in range(s):
            if i == j or i == s - j - 1 or i == 0 or i == s - 1 or j == 0 or j == s - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")


def right_diagonal(s):
    for i in range(s):
        for j in range(s):
            if i == j or i == 0 or j == 0 or i == s - 1 or j == s - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def left_diagonal(s):
    for i in range(s):
        for j in range(s):
            if i == s - j - 1 or i == 0 or j == 0 or i == s - 1 or j == s - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

def l_r_diagonals(s):
    for i in range(s):
        for j in range(s):
            if i == j or i == s - j - 1 or i == 0 or j == 0 or i == s - 1 or j == s - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")


arr = [right_diagonal, left_diagonal, l_r_diagonals, main_diagonal, side_diagonal, all_diagonals]

while True:
    choice = abs(int(input(
        "Enter a number from 0 to 6:\n1 -> show right diagonal in square\n2 -> show left diagonal in square\n3 -> show right and left diagonals in square\n4 -> show main diagonal in square\n5 -> show side diagonal in square\n6 -> show all diagonals in square\n0 -> Exit\n")))

    if choice == 0:
        print("Exit")
        break
    elif choice >= 1 and choice <= 6:
        s = abs(int(input("Enter a number from 5 to 100 for drawing the diagonal in a square: \n")))
        val = arr[choice - 1]
        val(s)
    else:
        print("Enter a correct value.")

