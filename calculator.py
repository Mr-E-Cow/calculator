import statistics
import random
import time
numbers = []
dash = "-" * 40
snr = "\nSequence not recognised\nPress enter to continue"
pec = "\nPress enter to continue"
rtm = "Returning to main menu, press enter to continue\n"
empty_lst = "Cannot remove numbers as the list contains no numbers"
exit_choice = ["e", "exit"]
num_one = "The only number in the list is: "
num_more = "The numbers in the list are: "


def main_menu():
    while True:
        print(f"{dash}\n{' ' * 15}Main menu\n{dash}\n")
        choice = input("Add number to list? (a)\nRemove numbers form list? (r)\nView number list? (v)" 
                       "\nClear number list (c)\nPerform functions (f)\nExit (e)\n\nwhat would you like do do?: ").casefold()
        if choice == "v":
            values()
        if choice == "a":
            adding_numbers()
        if choice == "r":
            removing_numbers()
        if choice == "f":
            if len(numbers) < 1:
                print("\n*** You need to input at least 2 numbers before you can perform a function ***\n")
            else:
                functions()
        if choice == "c":
            reset()
        if choice in exit_choice:
            print("\nThank you for using this program\n")
            for sec in range(0, 5):
                if int(sec) == 4:
                    print(f"The program will close in {5-int(sec)} seconds")
                else:
                    print(f"The program will close in {5-int(sec)} seconds")
                time.sleep(1)
            exit()


def adding_numbers():
    print(f"\n{dash}\n{' ' * 14}Add numbers\n{dash}")
    while True:
        if len(numbers) > 0:
            print(f"\nNumbers in the list: {', '.join(str(i) for i in numbers)}")
        imp = input("\nPlease enter a number, alternatively type 'rand' for random numbers or 'back' to go back: ")
        if imp.casefold() == "back":
            print("")
            main_menu()
        elif imp.casefold() == "rand":
            while True:
                rand_num = input("\nPlease enter how many random numbers you would like to be added or type 'back' to go back: ")
                if rand_num.casefold() == "back":
                    break
                elif rand_num.isnumeric():
                    adding_random = [int(100*random.random()) for x in range(1, int(rand_num)+1)]
                    numbers.extend(adding_random)
                    if int(rand_num) == 1:
                        print(f"\n{adding_random} has been added to number list\n")
                        if len(numbers) == 1:
                            print(f"*** The list now contains the number {', '.join(str(i) for i in numbers)} ***")
                        else:
                            print(f"*** The list now contains numbers: {', '.join(str(i) for i in numbers)} ***")
                    else:
                        print(f"\n{adding_random} have been added to number list\n\n"
                              f"*** list now contains numbers: {', '.join(str(i) for i in numbers)} ***")
                    input(pec)
                    break
                else:
                    input(snr)
        elif imp.isnumeric():
            numbers.append(int(imp))
            print(f"\n{imp} has been added to number list\n\n*** list now contains numbers: {', '.join(str(i) for i in numbers)} ***\n")
            while True:
                another = input("Add another number? y/n: ").casefold()
                if another == "y":
                    break
                elif another == "n":
                    print("")
                    main_menu()
                else:
                    input(snr)
        else:
            input(snr)


def removing_numbers():
    print(f"\n{dash}\n{' ' * 12}Remove numbers\n{dash}")
    while True:
        if len(numbers) == 0:
            print(f"\n{empty_lst}")
            input(rtm)
            main_menu()
        elif len(numbers) == 1:
            print(f"\n{num_one}{', '.join(str(i) for i in numbers)}")
        elif len(numbers) > 1:
            print(f"\n{num_more}{', '.join(str(i) for i in numbers)}")
        remove_num = input("Please enter the number you wish to remove or type 'back' to go back: ")
        if remove_num.casefold() == "back":
            print("")
            main_menu()
        elif remove_num.isnumeric():
            if int(remove_num) in numbers:
                pos = numbers.index(int(remove_num))
                numbers.pop(pos)
                print(f"\n{remove_num} has been removed from the list")
                if len(numbers) == 1:
                    print(f"{num_one}{', '.join(str(i) for i in numbers)}")
                elif len(numbers) > 1:
                    print(f"{num_more}{', '.join(str(i) for i in numbers)}")
                else:
                    print("The number list is now empty")
        else:
            input(snr)


def values():
    print(f"\n{dash}\n{' ' * 17}Values\n{dash}\n")
    if len(numbers) == 1:
        print(f"{num_one}{', '.join(str(i) for i in numbers)}\n")
    elif len(numbers) > 1:
        print(f"{num_more}{', '.join(str(i) for i in numbers)}\n")
    else:
        print("No values have been entered\n")
    input(rtm)
    main_menu()


def functions():
    sort_num = sorted(numbers)

    print(f"\n{dash}\n{' ' * 15}Functions\n{dash}")
    while True:
        print(f"\nthe numbers in the list are: {', '.join(str(i) for i in numbers)}")
        option = input("\nsum?:\t(sum)\t| median?:\t(med)\n"
                       "min?:\t(min)\t| mean?:\t(mean)\n"
                       "max?:\t(max)\t| mode?:\t(mode)\n"
                       "range?:\t(range)\t| exit?:\t(exit)\n\n"
                       "What function would you like to perform?: ").casefold()
        if option == "sum":
            total = sum(numbers)
            print(f"\nThe sum of all entered numbers is: {total}")
            input(pec)
            continue
        if option == "min":
            print(f"\nThe smallest number is: {min(numbers)}")
            input(pec)
            continue
        if option == "max":
            print(f"\nThe largest number is: {max(numbers)}")
            input(pec)
            continue
        if option == "range":
            print(f"\nThe highest number is {sort_num[-1]}\n" +
                  f"The lowest number is {sort_num[0]}\n" +
                  f"The range is {int(sort_num[-1]) - int(sort_num[0])}")
            input(pec)
            continue
        if option == "median" or option == "med":
            med_odd = sort_num[len(sort_num)//2]
            med_even = (sort_num[len(sort_num)//2-1]+med_odd)/2
            if med_even % 1 == 0:
                med_even = int(med_even)
            if len(sort_num) % 2 == 0:
                print(f"\nThere are {len(sort_num)} numbers in the list: {sort_num}")
                print(f"The median is located between positions {len(sort_num)//2} and {len(sort_num)//2+1}"
                      f"\nThe median is: {med_even}")
            else:
                print(f"\nThere are {len(sort_num)} numbers in the list: {sort_num}")
                print(f"The median at position {len(sort_num)//2+1} is: {med_odd}")
            input(pec)
            continue
        if option == "mean":
            avg = sum(numbers) / len(numbers)
            if avg % 1 == 0:
                print(f"\nThe average value is: {round(avg)}")
            else:
                print(f"\nThe average value is: {round(avg,2)}")
            input(pec)
            continue
        if option == "mode":
            if len(numbers) == len(set(numbers)):
                print("\nThe mode function can not be performed as there is no single number that occurs more than other")
            else:
                print(f"\nThe number that occurs more that an other is: {statistics.mode(numbers)}")
            input(pec)
            continue
        if option in exit_choice:
            print("")
            main_menu()
        else:
            input(snr)
        while True:
            another = input("\nChoose another function? y/n: ").casefold()
            if another == "y":
                print("")
                break
            elif another == "n":
                print("")
                main_menu()
            else:
                input(snr)


def reset():
    print(f"\n{dash}\n{' ' * 11}Reset number list\n{dash}")
    if len(numbers) == 0:
        print(empty_lst)
        input(rtm)
        main_menu()
    while True:
        clear = input("\nAre you sure you want to clear all the numbers form the list? y/n: ")
        if clear == "y":
            numbers.clear()
            input(f"\nAll numbers now reset\n{rtm}")
            main_menu()
        if clear == "n":
            input(f"\nNo numbers have been changed\n{rtm}")
            main_menu()
        else:
            input(snr)


main_menu()
