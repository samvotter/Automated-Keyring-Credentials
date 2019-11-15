from typing import Tuple
from getpass import getpass
from keyring import set_password, get_password


def check_credentials(
        manual: bool,
        update: bool,
        service: str
) -> Tuple[str, str]:
    service: str = service
    if manual:
        print(f"Manually enter your {service} credentials:")
        basic_auth: Tuple[str, str] = manual_credentials()
    elif update:
        print(f"Update Encrypted Credentials for {service} . . .")
        set_auto_credentials(service)
        basic_auth: Tuple[str, str] = get_auto_credentials(service)
    else:
        print(f"Attempting to get login details for {service} . . .")
        basic_auth: Tuple[str, str] = get_auto_credentials(service)

    while basic_auth[0] is None or basic_auth[1] is None:
        print("Username or Password were empty.")
        basic_auth: Tuple[str, str] = manual_credentials()
    return basic_auth


def manual_credentials(
) -> Tuple[str, str]:
    username: str = str(input("\tEnter Username:"))
    password: str = str(getpass("\tEnter Password:"))
    basic_auth: Tuple[str, str] = (username, password)
    return basic_auth


def set_auto_credentials(
        service: str
) -> None:
    username = input(f"Enter a username/server for auto-login to {service}: ")
    password = getpass(f"Enter a password for the auto-login to {service}: ")
    set_password(f"{service}", f"{service} Name", username)
    set_password(f"{service}", f"{service} Password", password)


def get_auto_credentials(
        service: str
) -> Tuple[str, str]:
    username: str = get_password(f"{service}", f"{service} Name")
    password: str = get_password(f"{service}", f"{service} Password")
    basic_auth: Tuple[str, str] = (username, password)
    return basic_auth
