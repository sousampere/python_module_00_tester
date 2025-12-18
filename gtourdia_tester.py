
import os
import subprocess
import time

RED = "\033[0;31m"
GREEN = "\033[0;32m"
WHITE = '\033[0;37m'
YELLOW = "\033[1;33m"

def display_result(exercise_name: str, success: bool, trace: str = None):
    time.sleep(0.05)
    if (success):
        print(f"{exercise_name} ->  {GREEN}✅ Success !{WHITE}")
    else:
        print(f"{exercise_name} ->  {RED}❌ Fail :({WHITE}")
    if (trace is not None):
        print(f"\tTrace : {RED}{trace}{WHITE}")

def display_summary(success : list, fails : list):
    print(f"{YELLOW}--- [SUMMARY] ---")
    for item in success:
        print(f"{GREEN}OK:{item} ", end=f"{WHITE}")
    print("")
    for item in fails:
        print(f"{RED}KO : {item}", end=f"{WHITE}")

if __name__ == "__main__":
    print()
    print(YELLOW, "  /$$$$$$    /$$                                         /$$ /$$                \    /\\")
    print(YELLOW, " /$$__  $$  | $$                                        | $$|__/                 )  ( ')")
    print(YELLOW, "| $$  \__/ /$$$$$$    /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$$ /$$  /$$$$$$       (  /  )")
    print(YELLOW, "| $$ /$$$$|_  $$_/   /$$__  $$| $$  | $$ /$$__  $$ /$$__  $$| $$ |____  $$       \(__)|")
    print(YELLOW, "| $$|_  $$  | $$    | $$  \ $$| $$  | $$| $$  \__/| $$  | $$| $$  /$$$$$$$")
    print(YELLOW, "| $$  \ $$  | $$ /$$| $$  | $$| $$  | $$| $$      | $$  | $$| $$ /$$__  $$")
    print(YELLOW, "|  $$$$$$/  |  $$$$/|  $$$$$$/|  $$$$$$/| $$      |  $$$$$$$| $$|  $$$$$$$")
    print(YELLOW, " \______/    \___/   \______/  \______/ |__/       \_______/|__/ \_______/")
    print(WHITE)

    success = list()
    fails = list()

    os.system("python3 -m flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6 ex7")
    try:
        subprocess.check_output("python3 -m flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6 ex7", shell=True)
        print(f"{GREEN}Flake8 NORM OK{WHITE}")
    except Exception:
        print(f"{RED}Please install falke8 to check the norm : pip3 install flake8{WHITE}")

    # ex0
    exercise = "test_ex0"
    expected = b'Hello, Garden Community!\n'
    test = subprocess.check_output(f"python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE}")

    # ex1
    exercise = "test_ex1"
    expected = b'Enter length: Enter width: Plot area: 15\n'
    test = subprocess.check_output(f"echo \"5\n3\n\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (length = 5, width = 3)")

    # ex2
    exercise = "test_ex2"
    expected = b'Day 1 harvest: Day 2 harvest: Day 3 harvest: Total harvest: 16\n'
    test = subprocess.check_output(f"echo \"5\n8\n3\n\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Values: 1 = 5, 2 = 8, 3 = 3)")

    # ex3
    exercise = "test_ex3"
    expected = b'Enter plant age in days: Plant needs more time to grow.\n'
    test = subprocess.check_output(f"echo \"42\n\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Values: 45)")
    expected = b'Enter plant age in days: Plant is ready to harvest!\n'
    test = subprocess.check_output(f"echo \"420\n\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Values: 420)")

    # ex4
    exercise = "test_ex4"
    expected = b'Days since last watering: Water the plants!\n'
    test = subprocess.check_output(f"echo \"42\n\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Value: 6)")
    expected = b'Days since last watering: Plants are fine\n'
    test = subprocess.check_output(f"echo \"2\n\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Values: 2)")

    # ex5 iterative
    exercise = "test_ex5_iter"
    expected = b'Days until harvest: Day 1\nDay 2\nDay 3\nHarvest time!\n'
    test = subprocess.check_output(f"echo \"3\n\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Value: 6)")
    exercise = "test_ex5_recurs"
    expected = b'Days until harvest: Day 1\nDay 2\nDay 3\nHarvest time!\n'
    test = subprocess.check_output(f"echo \"3\n\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Values: 2)")

    # ex6
    exercise = "test_ex6"
    expected = b'Enter garden name: Enter number of plants: Garden: Gtourdia garden\nPlants: 1664\nStatus: Growing well!\n'
    test = subprocess.check_output(f"echo \"Gtourdia garden\n1664\n\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Values: Gtourdia garden, 1664)")

    # ex7
    exercise = "test_ex7_area"
    expected = b'Magical seeds: covers 42 square meters\n'
    test = subprocess.check_output(f"echo \"magical\n42\narea\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Values: magical, 42, area)")
    exercise = "test_ex7_grams"
    expected = b'Apple seeds: 500 grams total\n'
    test = subprocess.check_output(f"echo \"apple\n500\ngrams\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Values: apple, 500, grams)")
    exercise = "test_ex7_packets"
    expected = b'Kiwi seeds: 20 packets available\n'
    test = subprocess.check_output(f"echo \"kiwi\n20\npackets\" | python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Values: kiwi, 20, packets)")
    exercise = "test_ex7_unknown"
    expected = b'Unknown unit type\n'
    test = subprocess.check_output(f"python3 {exercise}.py", shell=True)
    if (test == expected):
        display_result(exercise, True, None)
        success.append(exercise)
    else:
        display_result(exercise, False, test)
        fails.append(exercise)
        print(f"\tExpect: {YELLOW}{expected}{WHITE} (Values: altarian coin, 42, kilo)")
    display_summary(success, fails)