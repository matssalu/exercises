def slug(name):
    delen = name.split(" ")
    firstname = delen[0]
    lastname = delen[1:]

    return '-'.join(s.lower() for s in lastname + [firstname])