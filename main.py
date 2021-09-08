def find_closest_spoons(addrs):
    import locationservices
    avg = locationservices.average_locations(addrs)
    if avg is not None:
        return locationservices.get_nearby(avg)
    else:
        return None


def __gen_buck_palace():
    from locationservices.averager import Addr
    a = Addr()
    a.house = 'Buckingham Palace'
    a.line2 = 'London'
    a.postcode = 'SW1A 1AA'


if __name__ == '__main__':
    addrs = [__gen_buck_palace()]
    pub = find_closest_spoons(addrs)
    if pub is None:
        print('error - no closest pub')
    else:
        print('success')
