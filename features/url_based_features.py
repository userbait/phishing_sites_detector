from urllib.parse import urlparse


def is_shortened_url(url):
    """
    url 단축 서비스가 사용되었는지 확인
    :param url: String
    :return: boolean
    """

    domain = urlparse(url).netloc  # domain name with subdomain if exists

    # references : https://wiki.archiveteam.org/index.php?title=URLTeam#URL_shorteners
    url_shorteners = [
        'goo.gl', 'ff.im', '4url.cc', 'litturl.com', 'xs.md', 'url.0daymeme.com',
        'tr.im', 'visibli', 'visibli', 'zapd.co', 'bre.ad', 'arseh.at', 'bit.ly',
        'is.gd', 'kl.am', 'links.sharedby.co', 'ow.ly', 'surl.ws', 'tny.im', 'snipurl.com',
        'tinyurl.com', 'tr.im', 'ur1.ca', 'vbly.us', 'xym.kr', 'twitter-unrolled-urls-spritzer-stream',
    ]

    is_shortened = False
    for url_shortener in url_shorteners:
        if domain == url_shortener:
            is_shortened = True
            break

    return is_shortened


def use_https(url):
    """
    https 프로토콜이 적용되었는지 확인
    :param url: String
    :return: boolean
    """

    protocol = url[:5]
    use_https_ = False
    if protocol == 'https':
        use_https_ = True

    return use_https_


if __name__ == '__main__':
    print(is_shortened_url('https://tinyurl.com/asdlas'))
    print(use_https('https://www.naver.com'))