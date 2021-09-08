from locationservices import Addr


def find_closest_spoons(addrs):
    import locationservices
    avg = locationservices.average_locations(addrs)
    if avg is not None:
        return locationservices.get_nearby(avg)
    else:
        return None


def __input_addrs():
    xs = []
    x = ''

    while x != 'finish':
        xs.append(__get_addr())
        x = input("Input 'finish' if you wish to end address input")

    return xs


def __get_addr() -> Addr:
    house = input('\nPlease input house name:\n')
    line1 = input('\nPlease input the next line of an address:\n')
    line2 = input('\nPlease input the next line of an address:\n')
    postcode = input('\nPlease input the postcode:\n')

    a = Addr()
    a.house = house
    a.line1 = line1
    a.line2 = line2
    a.postcode = postcode

    return a


def __gen_buck_palace():
    a = Addr()
    a.house = 'Buckingham Palace'
    a.line1 = ''
    a.line2 = 'London'
    a.postcode = 'SW1A 1AA'
    return a


if __name__ == '__main__':
    addrs = __input_addrs()
    pub = find_closest_spoons(addrs)
    if pub is None:
        print('error - no closest pub')
    else:
        print('success')
