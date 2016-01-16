# encoding=utf8

# standard libs
import urllib2


def read_page(url):
    headers = {
        'User-Agent': 'fake-client',
    }

    req = urllib2.Request(
        url=url,
        headers=headers
    )
    # req.add_header('User-Agent','fake-client')
    try:
        response = urllib2.urlopen(req)
        raw_html_data = response.read()
        return raw_html_data
    except urllib2.HTTPError:
        return None
    except urllib2.URLError as e:
        if hasattr(e, "reason"):
            print e.reason
            return None
        elif hasattr(e, "code"):
            print e.code
            return None
    except Exception:
        return None



