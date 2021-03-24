import datetime


def dateStrValidate(date: str) -> bool:
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def idValidate(id: str) -> bool:
    if id is None:
        return False
    return id.isdigit()