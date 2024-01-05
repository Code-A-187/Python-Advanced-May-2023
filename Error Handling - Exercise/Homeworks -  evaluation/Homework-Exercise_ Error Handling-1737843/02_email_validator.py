from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


USERNAME_MIN_LENGTH = 4
VALID_DOMAINS = ["com", "bg", "org", "net"]

username_pattern = r"[a-z0-9_]+"

email_to_check = input()

while email_to_check != "End":

    if "@" not in email_to_check:
        raise MoreThanOneAtSymbolError("The email must contain only one @ symbol!")

    if email_to_check.count("@") > 1:
        raise MustContainAtSymbolError("The email must contain @ symbol!")

    username = email_to_check.split("@")[0]
    domain = email_to_check.split(".")[-1]

    if findall(username_pattern, username)[0] != username:
        raise InvalidNameError("The username must contain only lowercase letters, digits and underscore!")

    if len(username) < USERNAME_MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email_to_check = input()
