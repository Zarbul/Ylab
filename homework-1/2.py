from ipaddress import IPv4Address


def int32_to_ip(int32: int) -> str:
    ip = IPv4Address(int32)
    return str(ip)


if __name__ == '__main__':
    int32_to_ip(int(input('Input int32 number: ')))
