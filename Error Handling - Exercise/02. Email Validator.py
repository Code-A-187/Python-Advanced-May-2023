class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_SYMBOLS = 4
DOMAINS = [".com", ".bg", ".net", ".org"]

email = input()

while email != "END":

    if len(email.split('@')[0]) < MIN_SYMBOLS:
        raise NameTooShortError("Name must be more than 4 characters")
    if '@' not in email:
        raise MustContainAtSymbolError("E-mail must contain @")
    if not any(map(email.__contains__, DOMAINS)):
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')

    email = input()
