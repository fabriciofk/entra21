from datetime import datetime


current_year = datetime.now().year


def age_by_birth(birth_year: int) -> int:
    return current_year - birth_year


print(age_by_birth(1990))
