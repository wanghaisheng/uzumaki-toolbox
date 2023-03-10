from handler.utils import *
import requests
import json

UPS_LOGO = "https://media.discordapp.net/attachments/819084339992068110/1078449797121445920/ups-social-share-logo-removebg-preview.png"


def redirect_webhook_brt(
    company, tracking_number, name, phone, address, city, state, zip, url, email
):
    settings = load_settings()
    webhook = settings["webhook"]

    url_ = url

    data = {
        "username": "Uzumaki™",
        "avatar_url": LOGO,
        "content": " ",
        "embeds": [
            {
                "title": tracking_number,
                "url": url_,
                "color": 12298642,
                "description": "> Successfully redirect your parcel!",
                "footer": {"text": "by Uzumaki Tools", "icon_url": LOGO},
                "fields": [
                    {"name": "Company", "value": company.upper(), "inline": True},
                    {
                        "name": "Tracking Number",
                        "value": tracking_number,
                        "inline": False,
                    },
                    {"name": "Name", "value": "||" + name + "||", "inline": True},
                    {"name": "Phone", "value": "||" + phone + "||", "inline": True},
                    {"name": "Address", "value": "||" + address + "||", "inline": True},
                    {"name": "City", "value": "||" + city + "||", "inline": True},
                    {"name": "State", "value": "||" + state + "||", "inline": True},
                    {"name": "Zip", "value": "||" + zip + "||", "inline": True},
                    {"name": "Email", "value": "||" + email + "||", "inline": False},
                ],
            }
        ],
    }

    result = requests.post(
        webhook, data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    try:
        result.raise_for_status()
        print_task(f"[brt {tracking_number}] successfully sent webhook", YELLOW)
    except requests.exceptions.HTTPError as err:
        print(err)


def checker_brt_discord(
    tracking,
    brt_tracking_response,
    redictable,
    zip_code,
    order_number,
):
    settings = load_settings()
    webhook = settings["webhook"]

    description = "> You can't redirect your parcel, pleease wait."

    if redictable == "Yes":
        description = "> You can redirect your parcel!"

    data = {
        "username": "Uzumaki™",
        "avatar_url": LOGO,
        "content": " ",
        "embeds": [
            {
                "title": order_number,
                "url": brt_tracking_response,
                "color": 12298642,
                "description": description,
                "footer": {"text": "by Uzumaki Tools", "icon_url": LOGO},
                "fields": [
                    {"name": "Company", "value": "BRT", "inline": True},
                    {
                        "name": "Tracking Number",
                        "value": "||" + tracking + "||",
                        "inline": False,
                    },
                    {
                        "name": "Zip Code",
                        "value": "||" + zip_code + "||",
                        "inline": True,
                    },
                    {"name": "Redirectable", "value": redictable, "inline": False},
                ],
            }
        ],
    }

    result = requests.post(
        webhook, data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    try:
        result.raise_for_status()
        print_task(f"[brt {order_number}] successfully sent webhook", YELLOW)
    except requests.exceptions.HTTPError as err:
        print(err)


def send_webhook_sda(tracking_number, date, city, status):
    settings = load_settings()
    webhook = settings["webhook"]

    url: str = ""

    url = (
        "https://www.sda.it/wps/portal/Servizi_online/dettaglio-spedizione?locale=it&tracing.letteraVettura="
        + tracking_number
    )

    data = {
        "username": "Uzumaki™",
        "avatar_url": LOGO,
        "content": " ",
        "embeds": [
            {
                "title": "Tracking Number",
                "url": url,
                "color": 12298642,
                "footer": {"text": "Powered by Uzumaki Tools", "icon_url": LOGO},
                "fields": [
                    {"name": "Company", "value": "SDA", "inline": True},
                    {"name": "Date", "value": date, "inline": True},
                    {"name": "City", "value": city, "inline": False},
                    {"name": "Status", "value": status, "inline": True},
                ],
            }
        ],
    }

    result = requests.post(
        webhook, data=json.dumps(data), headers={"Content-Type": "application/json"}
    )

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)


def send_webhook_brt(company, tracking_number, date, time, location, status):
    settings = load_settings()
    webhook = settings["webhook"]

    url: str = ""

    if company == "brt":
        url = (
            "https://www.mybrt.it/it/mybrt/my-parcels/search?lang=en&parcelNumber="
            + tracking_number
        )

    data = {
        "username": "Uzumaki™",
        "avatar_url": LOGO,
        "content": " ",
        "embeds": [
            {
                "title": "Tracking Number",
                "url": url,
                "color": 12298642,
                "footer": {"text": "Powered by Uzumaki Tools", "icon_url": LOGO},
                "fields": [
                    {"name": "Company", "value": "BRT", "inline": True},
                    {"name": "Status", "value": status, "inline": True},
                    {"name": "Date", "value": date, "inline": True},
                    {"name": "Time", "value": time, "inline": True},
                    {"name": "Branch", "value": location, "inline": True},
                ],
            }
        ],
    }

    result = requests.post(
        webhook, data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)


def send_webhook(dataInfo):

    settings = load_settings()
    webhook = settings["webhook"]
    
    url = (
        "https://www.ups.com/track?loc=en_IT&tracknum="
        + dataInfo["tracking_number"]
        + "&requester=ST/trackdetails"
    )

    data = {
        "username": "Uzumaki™",
        "avatar_url": LOGO,
        "content": " ",
        "embeds": [
            {
                "title": "Tracking Number",
                "url": url,
                "color": 12298642,
                "footer": {"text": "Powered by Uzumaki Tools", "icon_url": LOGO},
                "thumbnail": {"url": UPS_LOGO},
                "fields": [
                    {"name": "Company", "value": "UPS", "inline": True},
                    {
                        "name": "Tracking Number",
                        "value": dataInfo["tracking_number"],
                        "inline": True,
                    },
                    {
                        "name": "Status",
                        "value": dataInfo["package_status"],
                        "inline": True,
                    },
                    {
                        "name": "Date",
                        "value": dataInfo["delivered_date"],
                        "inline": True,
                    },
                    {
                        "name": "Time",
                        "value": dataInfo["time_stamp"],
                        "inline": True,
                    },
                    {
                        "name": "Branch",
                        "value": dataInfo["location"],
                        "inline": True,
                    },

                ],
            }
        ],
    }
    result = requests.post(
        webhook, data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    try:
        result.raise_for_status()
        print_task(f"[ups {dataInfo['tracking_number']}] successfully sent webhook", GREEN)
    except requests.exceptions.HTTPError as err:
        print_task(f"[ups {dataInfo['tracking_number']}] error sending webhook", RED)


def webhook_nike(
    price: str,
    name: str,
    url_image: str,
    size: str,
    lineItemStatus: str,
    address: str,
    city: str,
    country: str,
    zip: str,
    tracklink: str,
    tracking_number: str,
):
    settings = load_settings()
    webhook = settings["webhook"]

    data = {
        "username": "Uzumaki™",
        "avatar_url": LOGO,
        "content": " ",
        "embeds": [
            {
                "title": "Tracking Number",
                "url": tracklink,
                "color": 12298642,
                "footer": {"text": "Powered by Uzumaki Tools", "icon_url": LOGO},
                "thumbnail": {"url": url_image},
                "fields": [
                    {"name": "Status", "value": lineItemStatus, "inline": False},
                    {"name": "Price", "value": price + "€", "inline": True},
                    {"name": "Name", "value": name, "inline": True},
                    {"name": "Size", "value": size, "inline": True},
                    {"name": "Address", "value": address, "inline": True},
                    {"name": "City", "value": city, "inline": True},
                    {"name": "Country", "value": country, "inline": True},
                    {"name": "Zip", "value": zip, "inline": True},
                    {
                        "name": "Order Number",
                        "value": tracking_number,
                        "inline": True,
                    },
                ],
            }
        ],
    }
    result = requests.post(
        webhook, data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)


def webhook_newBalance(
    orderNumber,
    date,
    style,
    price,
    image,
    title,
    email,
    firstName,
    secondName,
    addy,
    zipCode,
    status,
    trackingLink,
):
    settings = load_settings()
    webhook = settings["webhook"]
    status_final = "[" + status + "]" + "(" + trackingLink + ")"
    orderNumber = "||" + orderNumber + "||"

    data = {
        "username": "Uzumaki™",
        "avatar_url": LOGO,
        "content": " ",
        "embeds": [
            {
                "title": title,
                "color": 12298642,
                "footer": {"text": "Powered by Uzumaki Tools", "icon_url": LOGO},
                "thumbnail": {"url": image},
                "fields": [
                    {"name": "Status", "value": status_final, "inline": False},
                    {"name": "Order Number", "value": orderNumber, "inline": True},
                    {"name": "Date", "value": date, "inline": True},
                    {"name": "Price", "value": price, "inline": True},
                    {"name": "Email", "value": email, "inline": False},
                    {"name": "First Name", "value": firstName, "inline": True},
                    {"name": "Second Name", "value": secondName, "inline": True},
                    {"name": "Address", "value": addy, "inline": True},
                    {"name": "Zip Code", "value": zipCode, "inline": True},
                ],
            }
        ],
    }
    result = requests.post(
        webhook, data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)


def webhook_courir(orderNumber, image, status, title, email, zipCode, trackingLink):
    settings = load_settings()
    webhook = settings["webhook"]
    if trackingLink != None:
        status = "[" + status + "]" + "(" + trackingLink + ")"

    data = {
        "username": "Uzumaki™",
        "avatar_url": LOGO,
        "content": " ",
        "embeds": [
            {
                "title": title,
                "color": 12298642,
                "footer": {"text": "Powered by Uzumaki Tools", "icon_url": LOGO},
                "thumbnail": {"url": image},
                "fields": [
                    {"name": "Status", "value": status, "inline": False},
                    {"name": "Order Number", "value": orderNumber, "inline": True},
                    {"name": "Email", "value": email, "inline": False},
                    {"name": "Zip Code", "value": zipCode, "inline": True},
                ],
            }
        ],
    }
    result = requests.post(
        webhook, data=json.dumps(data), headers={"Content-Type": "application/json"}
    )
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
