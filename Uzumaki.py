from handler.utils import *
from handler.redirect import redirect
from handler.geocode import geocode
from handler.tracker import tracker
from handler.auth import auth, update
from handler.jigger import jigger
from handler.scraperOrder import scraperOrder
from handler.presence import reachPresence
from handler.restock import restockPayout
from handler.unsubscriber import unsubscriber


import colorama


OPTIONS = {
    "01": redirect,
    "02": tracker,
    "03": geocode,
    "04": jigger,
    "05": scraperOrder,
    "06": restockPayout,
    "07": unsubscriber,
    "00": bye,
}


def handler_option(option):
    try:
        OPTIONS[option]()
    except KeyError:
        print_task("invalid option", RED)
        input("press enter to exit...")
        return


def main():
    colorama.init(wrap=True)

    update()
    checking()
    username = auth()
    reachPresence(username)

    option = banner(username)
    handler_option(option)


if __name__ == "__main__":
    main()


# Email Unsubscriber
# ups redirect => opt bot
