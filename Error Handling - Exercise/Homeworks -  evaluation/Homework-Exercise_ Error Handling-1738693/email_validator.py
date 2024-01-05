class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = (".com", ".bg", ".net", ".org")

while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, registration = email.split("@")
    domain = registration.split(".")[-1]

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "." + domain not in domains:
        raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .net, .org")

    print("Valid email")


