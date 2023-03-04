from handler.utils import *
from handler.ups import ups
from handler.brt import brt
from handler.sda import sda
from handler.nike import nike
import time
import os
import csv
import threading


def companyHandler(fileName, tracking_number, email):
    company_mapping = {
        "ups.csv": ups,
        "brt.csv": brt,
        "sda.csv": sda,
    }

    nike_mapping = {
        "nike.csv": nike,
    }

    try:
        company_mapping[fileName](tracking_number)
    except KeyError:
        try:
            nike_mapping[fileName](tracking_number, email)
        except KeyError:
            print_task("invalid company", RED)
            time.sleep(3)
            return


def tracker(username):
    """Displays a list of tracking files and prompts the user to select one.
    For each row in the selected file, launches a new thread to handle the tracking
    for the given company."""

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(f"{RED}{BANNER}{RESET}")

        print(
            f"{Fore.WHITE}WELCOME BACK: {Fore.RED}{username.upper()}{Style.RESET_ALL}\n"
        )

        os.chdir(os.path.join("Uzumaki", "tracker"))
        files = os.listdir()
        os.chdir(os.path.join("..", ".."))

        files_dict = {}

        for index, file in enumerate(files):
            print_file(f"{index}. {file}")

            files_dict[str(index)] = file

        print("\n")
        option = input(f"{TAB}> choose: ")

        try:
            file = files_dict[option]
            break
        except KeyError:
            print_task("invalid option", RED)
            time.sleep(2)

    with open(os.path.join("Uzumaki", "tracker", file), "r") as f:
        reader = csv.reader(f)

        try:
            next(reader)
        except StopIteration:
            print_task("file is empty", RED)
            time.sleep(2)
            return

        try:
            row = next(reader)
        except StopIteration:
            print_task(f"please fill {file}", RED)
            time.sleep(3)
            return

        f.seek(0)
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            try:
                tracking_number = row[0].strip()
                if not tracking_number:
                    print_task("invalid tracking number", RED)
                    time.sleep(3)
                    return
            except IndexError:
                print_task("invalid file", RED)
                time.sleep(3)
                return
            try:
                email = row[1].strip()
            except IndexError:
                email = ""

            threading.Thread(
                target=companyHandler, args=(file, tracking_number, email)
            ).start()
