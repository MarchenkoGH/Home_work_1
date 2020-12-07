from urllib.parse import urlsplit, parse_qs
from http.cookies import SimpleCookie


def parse_parameters(url: str) -> dict:
    query = urlsplit(url).query
    params = parse_qs(query)
    return {k: v[0] for k, v in params.items()}


def parse_cookies(query: str) -> dict:
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
    assert parse_parameters('https://timeplan.net/?cell=160&day=2020-01-01&open=false&roleIds=2%2C25%2C26'
                            '%2C28%2C6%2C42%2C43%2C10%2C39%2C15%2C34%2C137%2C17%2C50%2C44%2C233%2C16%2C234%2C52%2C232'
                            '%2C231%2C32%2C55%2C45%2C109%2C229%2C46%2C14%2C97&vesselIds=34020%2C38858%2C38401') \
           == {'cell': '160', 'day': '2020-01-01', 'open': 'false', 'roleIds': '2,25,26,28,6,42,43,10,39,15,34,137,'
                                                                               '17,50,44,233,16,234,52,232,231,32,'
                                                                               '55,45,109,229,46,14,97',
               'vesselIds': '34020,38858,38401'}
    assert parse_parameters('http://mysite.ru/?a=2&b=3') == {'a': '2', 'b': '3'}
    assert parse_parameters('www.yoursite.com?myparam1=123&myparam2=abc') == {'myparam1': '123', 'myparam2': 'abc'}


    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('name=Dima; surname=ivanov;') == {'name': 'Dima', 'surname': 'ivanov'}
    assert parse_cookies('CUSTOMER=WILE_E_COYOTE; PART_NUMBER=ROCKET_LAUNCHER_0001; SHIPPING=FEDEX') \
           == {'CUSTOMER': 'WILE_E_COYOTE', 'PART_NUMBER': 'ROCKET_LAUNCHER_0001', 'SHIPPING': 'FEDEX'}
    assert parse_cookies('usernamefield=username, passwordfield=password, otherfield=othervalue')\
           == {'usernamefield': 'username,', 'passwordfield': 'password,', 'otherfield': 'othervalue'}
    assert parse_cookies('baz=42; Domain=example.com; Expires=Thu, 12-Jan-2017 13:55:08 GMT; Path=/, dir=75')\
           == {'baz': '42', 'dir': '75'}
    assert parse_cookies('ckpf_ppid_safari=a271b829cc244d5c94faae14f73f34df; '
                         'ckpf_ppid_safari=21ebcecf7ab7400483c654469c6b24fb; ecos.dt=1600401456420; '
                         'ecos.dt=1600401456208; _em_vt=99882dac-6513-43f6-877f-4f53766e67e5-1749f19f996-5ca2782f; '
                         '__gads=ID=a42c30d38b4350e3-227e540a95c3001b:T=1600399634:RT=1600399634:S'
                         '=ALNI_MZ1UNYRqcXwTpGQPoMqq9sATyF6wg; _cb=Z6cFZqJKjWDvIPNE; '
                         '_chartbeat2=.1600397040609.1600399633336.1.Bym-CVCpzqLyBCabklBCyznkC-mw7l.1; '
                         'atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22b8d29b9f-6075-4bb9-983a'
                         '-36e64c3904d2%22%2C%22options%22%3A%7B%22end%22%3A%222021-10-20T03%3A27%3A12.114Z%22%2C'
                         '%22path%22%3A%22%2F%22%7D%7D; atuserid={'
                         '%22val%22:%22b8d29b9f-6075-4bb9-983a-36e64c3904d2%22}; _cc_dc=2; '
                         '_cc_id=b58f5f5f6411e8ab29f7d1086bd0409a; ckns_sa_labels_persist={}; '
                         'ckpf_ppid=7b5b127c65d24d939298eb61b7b9a08f; ckns_orb_fig_cache={'
                         '%22ad%22:1%2C%22ap%22:0%2C%22ck%22:0%2C%22eu%22:0%2C%22uk%22:0}; ckns_explicit=1; '
                         'ckns_policy=111; ckns_policy_exp=1631933129982; '
                         'ckns_sscid=4430f388-f05f-48ff-9aba-b4837297d7a1; _cb_ls=1; ckns_privacy=july2019 ')\
           == {'ckpf_ppid_safari': '21ebcecf7ab7400483c654469c6b24fb', 'ecos.dt': '1600401456208',
               '_em_vt': '99882dac-6513-43f6-877f-4f53766e67e5-1749f19f996-5ca2782f',
               '__gads': 'ID=a42c30d38b4350e3-227e540a95c3001b:T=1600399634:RT=1600399634:S'
                         '=ALNI_MZ1UNYRqcXwTpGQPoMqq9sATyF6wg',
               '_cb': 'Z6cFZqJKjWDvIPNE',
               '_chartbeat2': '.1600397040609.1600399633336.1.Bym-CVCpzqLyBCabklBCyznkC-mw7l.1',
               'atuserid': '{%22val%22:%22b8d29b9f-6075-4bb9-983a-36e64c3904d2%22}', '_cc_dc': '2',
               '_cc_id': 'b58f5f5f6411e8ab29f7d1086bd0409a', 'ckns_sa_labels_persist': '{}',
               'ckpf_ppid': '7b5b127c65d24d939298eb61b7b9a08f',
               'ckns_orb_fig_cache': '{%22ad%22:1%2C%22ap%22:0%2C%22ck%22:0%2C%22eu%22:0%2C%22uk%22:0}',
               'ckns_explicit': '1', 'ckns_policy': '111', 'ckns_policy_exp': '1631933129982',
               'ckns_sscid': '4430f388-f05f-48ff-9aba-b4837297d7a1', '_cb_ls': '1', 'ckns_privacy': 'july2019'}


