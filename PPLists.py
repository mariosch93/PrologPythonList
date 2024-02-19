from swiplserver import PrologMQI

lst = []
while True:
    try:
        lst_number = int(input("how many numbers you want in the list? :"))
        for i in range(lst_number):
            input_number = float(
                input(f"choose the {i+1} number you wish to add: "))
            lst.append(input_number)
        break
    except Exception as e:
        print(f"Invalid input: {e}")

print(f"\nYour list is: {lst}\n")

with PrologMQI() as mqi:
    with mqi.create_thread() as prolog_thread:
        prolog_thread.query('consult("PPLists.pl").')
        while True:
            print("1. Addition of all the list elements.")
            print("2. Delete an element from the list.")
            print("3. Random select items from the list.")
            print("4. Delete all unique elements.")
            print("5. Find the length of the list.")
            print("6. Find the average value.")
            print("7. Find max.")
            print("8. Reverse all the elements of the list.")
            print("9. Increment list by one.")
            print("10. Sort list.")
            print("11. Add element.")
            print("12. Add the nth element from fibonacci sequence.")
            print("---> Press 0 to exit. <---")
            choice = (input("\nChoose from the above: \n"))
            if choice == "1":
                result = prolog_thread.query(f"sumlist({lst},X)")
                if result[0]["X"] == 0:
                    print(
                        "\n---> The list is currently empty,choose 10 to add some values <---\n")
                else:
                    print(
                        f'\n---> The total sum of the list elements is: {result[0]["X"]}\n')
            elif choice == "2":
                remove_el = float(
                    input("\n---> Which number do you wish to remove from your list?\n"))
                result = prolog_thread.query(f"delete_el({remove_el},{lst},X)")
                print(
                    f'\n---> The new list without: {remove_el} is: {result[0]["X"]}\n')
                lst = result[0]["X"]
            elif choice == "3":
                rand_el = int(
                    input("\n---> How many numbers do you wish to keep: \n"))
                if lst == []:
                    print(
                        "\n---> The list is currently empty,choose 10 to add some values <---\n")
                    continue
                elif rand_el > len(lst):
                    print(
                        "---> The list doesn't have that many numbers, choose again! <---\n")
                    rand_el = int(
                        input("\n---> How many numbers do you wish to keep: \n"))
                result = prolog_thread.query(f"rnd_select({lst},{rand_el},X)")
                print(
                    f'\n---> The new list is: {result[0]["X"]}\n')
                lst = result[0]["X"]
            elif choice == "4":
                result = prolog_thread.query(
                    f"delete_unique({lst},X)")
                print(
                    f'\n---> The new list only contains duplicates: {result[0]["X"]}\n')
                lst = result[0]["X"]
            elif choice == "5":
                result = prolog_thread.query(f"list_length({lst},X)")
                if result[0]["X"] == 0:
                    print(
                        "\n---> The list is currently empty,choose 10 to add some values <---\n")
                else:
                    print(
                        f'\n---> The length of the list is: {result[0]["X"]}\n')
            elif choice == "6":
                result = prolog_thread.query(f"average({lst},X)")
                print(
                    f'\n---> The average value is: {result[0]["X"]}\n')
            elif choice == "7":
                result = prolog_thread.query(f"max({lst},X)")
                if result and len(result) > 0:
                    print(
                        f'\n---> Max is: {result[0]["X"]}\n')
                else:
                    print(
                        "\n---> The list is currently empty,choose 10 to add some values <---\n")
            elif choice == "8":
                result = prolog_thread.query(f"reverse_list({lst},X)")
                print(
                    f'\n---> The list is now reversed: {result[0]["X"]}\n')
                lst = result[0]["X"]
            elif choice == "9":
                result = prolog_thread.query(f"increment({lst},X)")
                print(
                    f'\n---> The new list is: {result[0]["X"]}\n')
                lst = result[0]["X"]
            elif choice == "10":
                result = prolog_thread.query(f"quick({lst},X)")
                print(
                    f'\n---> The list is now sorted: {result[0]["X"]}\n')
                lst = result[0]["X"]
            elif choice == "11":
                add_el = float(
                    input("\n---> Which number do you wish to add: \n"))
                result = prolog_thread.query(f"insertinto({add_el},{lst},X)")
                print(
                    f'\n---> The new list is: {result[0]["X"]}\n')
                lst = result[0]["X"]
            elif choice == "12":
                prolog_thread.query(
                    "set_prolog_flag(stack_limit, 50_000_000_000)")
                add_fibo = int(
                    input("\n---> choose the ending value of the fibonacci sequence(max:30): \n"))
                for j in range(1, add_fibo+1):
                    result = prolog_thread.query(f"fib({j},X)")
                    for i in range(len(result)):
                        lst.append(result[i]["X"])
                print(f'---> the new list is: {lst}\n')
            elif choice == "0":
                print(f'\n---> Your final list contains: {lst} <---\n')
                print("---> Thank you for creating this awesome list, Goodbye! <---\n")
                break
            else:
                print("\n---> Choice not available try again!<---\n")
