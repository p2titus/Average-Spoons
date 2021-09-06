def find_closest_spoons(addr):
    import locationservices
    avg = locationservices.average_locations(addr)
    pub = locationservices.get_nearby(avg)
    print(pub)


if __name__ == '__main__':
    addrs = None
    find_closest_spoons(addrs)
