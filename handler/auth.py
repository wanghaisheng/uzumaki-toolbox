from handler.utils import *
import os
import requests

api_key = "***REMOVED***"


def get_license(license_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    req = requests.get(
        f"https://api.hyper.co/v6/licenses/{license_key}", headers=headers
    )
    if req.status_code == 200:
        return req.json()

    return None


def auth():
    settings = load_settings()
    webhook = settings["webhook"]
    key = settings["key"]

    if not key or key == "KEY HERE":
        print_task("please set key...", RED)
        input("Press Enter to exit...")
        os._exit(1)

    license_data = get_license(key)

    if license_data:
        if license_data.get("metadata") != {}:
            print_task("License is already in use on another machine!", RED)
            input("Press Enter to exit...")
            os._exit(1)
    else:
        print_task("Invalid license key!", RED)
        input("Press Enter to exit...")
        os._exit(1)

    username = license_data.get("integrations").get("discord").get("username")

    if not webhook or webhook == "WEBHOOK HERE":
        print_task("please set webhook...", RED)
        input("Press Enter to exit...")
        os._exit(1)

    return username
