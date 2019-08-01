# -*- encoding: utf-8
# yapf: disable


checkname = 'f5_bigip_vserver'


info = [
    [u'/Common/sight-seeing.wurmhole.univ', u'1', u'1', u'The virtual server is available', u'\xd4;xK',
     u'', u'', u'', u'', u'', u'', u'', u'', u'0', u''],
    [u'/Common/www.wurmhole.univ_HTTP2HTTPS', u'4', u'1', (u"The children pool member(s) either don't"
     u" have service checking enabled, or service check results are not available yet"),
     u'\xd4;xI', u'', u'', u'', u'', u'', u'', u'', u'', u'0', u''],
    [u'/Common/sight-seeing.wurmhole.univ_HTTP2HTTPS', u'4', u'1', (u"The children pool member(s) either"
     u" don't have service checking enabled, or service check results are not available yet"),
     u'\xd4;xK', u'', u'', u'', u'', u'', u'', u'', u'', u'0', u''],
    [u'/Common/starfleet.space', u'4', u'', u"To infinity and beyond!", u'\xde\xca\xff\xed', u'', u'',
     u'', u'', u'', u'', u'', u'', u'0', u''],
]


discovery = {
    '': [
        (u'/Common/sight-seeing.wurmhole.univ', {}),
        (u'/Common/sight-seeing.wurmhole.univ_HTTP2HTTPS', {}),
        (u'/Common/www.wurmhole.univ_HTTP2HTTPS', {}),
        (u'/Common/starfleet.space', {}),
    ],
}


checks = {
    '': [
        (u'/Common/sight-seeing.wurmhole.univ_HTTP2HTTPS', {}, [
            (0, u'Virtual Server with IP 212.59.120.75 is enabled', []),
            (1, u'State availability is unknown, Detail: T', []),
            (0, 'Client connections: 0', [('connections', 0, None, None, None, None)]),
            (0, 'Rate: 0.00/sec', []),
        ]),
        (u'/Common/www.wurmhole.univ', {}, []),
        (u'/Common/www.wurmhole.univ_HTTP2HTTPS', {}, [
            (0, u'Virtual Server with IP 212.59.120.73 is enabled', []),
            (1, u'State availability is unknown, Detail: T', []),
            (0, 'Client connections: 0', [('connections', 0, None, None, None, None)]),
            (0, 'Rate: 0.00/sec', []),
        ]),
        (u'/Common/starfleet.space', {}, [
            (1, u'Virtual Server with IP 222.202.255.237 is in unknown state', []),
            (1, u'State availability is unknown, Detail: T', []),
            (0, 'Client connections: 0', [('connections', 0, None, None, None, None)]),
            (0, 'Rate: 0.00/sec', []),
        ]),
    ],
}
