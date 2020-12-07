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
    assert parse_parameters('http://site.ru/page.php?name=dima&age=27') == {'name': 'dima', 'age': '27'}
    assert parse_parameters('http://httpbin.org/get?key2=value2&key1=value1&key3=value3') == {'key2': 'value2',
                                                                                              'key1': 'value1',
                                                                                              'key3': 'value3'}
    assert parse_parameters('https://www.google.com/search?q=test&oq=t&'
                            'aqs=chrome.0.69i59j69i57j69i59l2j69i60l4.5093j0j1&sourceid=chrome&ie=UTF-8') \
           == {'q': 'test', 'oq': 't', 'aqs': 'chrome.0.69i59j69i57j69i59l2j69i60l4.5093j0j1', 'sourceid': 'chrome',
               'ie': 'UTF-8'}

    assert parse_parameters('https://duckduckgo.com/?q=test&t=h&ia=web') == {'q': 'test', 't': 'h', 'ia': 'web'}

    assert parse_parameters('https://www.google.com/search?client=firefox-b-d&q=k') \
           == {'client': 'firefox-b-d', 'q': 'k'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('name=Dima; surname=ivanov;') == {'name': 'Dima', 'surname': 'ivanov'}
    assert parse_cookies('CUSTOMER=WILE_E_COYOTE; PART_NUMBER=ROCKET_LAUNCHER_0001; SHIPPING=FEDEX') \
           == {'CUSTOMER': 'WILE_E_COYOTE', 'PART_NUMBER': 'ROCKET_LAUNCHER_0001', 'SHIPPING': 'FEDEX'}

