class NameTooShortError(Exception):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(Exception):
    """Email must contain @"""


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""


line = input('Enter e-mail:')

while line != "End":
    if "@" in line:
        if line.index('@') <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        elif not (line.endswith('.com') or line.endswith('.bg') or line.endswith('.net') or line.endswith('.org')):
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        else:
            print("Email is valid")
    else:
        raise MustContainAtSymbolError("Email must contain @")
    line = input('Enter "End" or e-mail:')
