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
    except urllib2.URLError as e:
        if hasattr(e, "reason"):
            print e.reason
            return 0
        elif hasattr(e, "code"):
            print e.code
            return 0
    else:
        print 'No exception raise.\n'
    print "The code : %s" % response.getcode()
    rawdata = response.read()
    print rawdata
    return rawdata

