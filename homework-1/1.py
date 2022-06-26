def domain_name(url: str) -> str:
    url_split = url.split('//')[-1].split('.')
    if url_split[0] == 'www':
        return url_split[1]
    return url_split[0]


if __name__ == '__main__':
    domain_name(input("Input url: "))
