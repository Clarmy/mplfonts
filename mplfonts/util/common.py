import hashlib


def calc_md5(content):
    return hashlib.md5(content).hexdigest()


if __name__ == "__main__":
    pass
