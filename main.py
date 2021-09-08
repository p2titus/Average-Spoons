def find_closest_spoons(addr):
    import locationservices
    avg = locationservices.average_locations(addr)
    pub = locationservices.get_nearby(avg)
    print(pub)


def __gen_buck_palace():
    from locationservices.averager import Addr
    a = Addr()
    a.house = 'Buckingham Palace'
    a.line2 = 'London'
    a.postcode = 'SW1A 1AA'


if __name__ == '__main__':
    addrs = []
    find_closest_spoons(addrs)
