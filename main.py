def parse_parameters(url: str) -> dict:
    from urllib.parse import urlsplit, parse_qs
    query = urlsplit(url).query
    params = parse_qs(query)
    return {k: v[0] for k, v in params.items()}


def parse_cookies(query: str) -> dict:
    from http.cookies import SimpleCookie
    cookie = SimpleCookie()
    cookie.load(query)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret',
                                                                                             'color': 'purple'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
