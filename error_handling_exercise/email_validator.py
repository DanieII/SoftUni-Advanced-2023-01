import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


# Additional Error
class MissingDomainError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


name_pattern = r"^[\w\.]{4,}@"
domain_exists_pattern = r"@[a-zA-z]+\.[a-z]+"
domain_name_pattern = r"\.[a-z\.]+"

command = input()

while command != "End":
    email = command

    if not email.count("@"):  # 0 => False
        raise MustContainAtSymbolError("Email must contain @")
    if not re.match(name_pattern, email):
        raise NameTooShortError("Name must be more than 4 characters")
    if not re.search(domain_exists_pattern, email):
        raise MissingDomainError("Email must contain a domain")
    if re.findall(domain_name_pattern, email)[-1] not in [".com", ".bg", ".org", ".net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    command = input()
