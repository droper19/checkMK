# -*- encoding: utf-8
# yapf: disable

checkname = 'graylog_cluster_traffic'

info = [[
    u'{"to": "2019-10-01T12:00:00.000Z", "output": {"2019-10-01T06:00:00.000Z": 0, "2019-10-01T12:00:00.000Z": 892382, "2019-10-01T04:00:00.000Z": 0, "2019-09-30T13:00:00.000Z": 0, "2019-10-01T10:00:00.000Z": 0, "2019-09-30T15:00:00.000Z": 0, "2019-10-01T09:00:00.000Z": 0, "2019-10-01T07:00:00.000Z": 0, "2019-10-01T08:00:00.000Z": 0, "2019-10-01T05:00:00.000Z": 0, "2019-09-30T17:00:00.000Z": 0, "2019-09-30T18:00:00.000Z": 0, "2019-09-30T14:00:00.000Z": 0, "2019-10-01T11:00:00.000Z": 0}, "from": "2019-09-30T12:00:00.000Z", "decoded": {"2019-10-01T06:00:00.000Z": 0, "2019-10-01T12:00:00.000Z": 922424, "2019-10-01T04:00:00.000Z": 0, "2019-09-30T13:00:00.000Z": 0, "2019-10-01T10:00:00.000Z": 0, "2019-09-30T15:00:00.000Z": 0, "2019-10-01T09:00:00.000Z": 0, "2019-10-01T07:00:00.000Z": 0, "2019-10-01T08:00:00.000Z": 0, "2019-10-01T05:00:00.000Z": 0, "2019-09-30T17:00:00.000Z": 0, "2019-09-30T18:00:00.000Z": 0, "2019-09-30T14:00:00.000Z": 0, "2019-10-01T11:00:00.000Z": 0}, "input": {"2019-10-01T06:00:00.000Z": 0, "2019-10-01T12:00:00.000Z": 435345, "2019-10-01T04:00:00.000Z": 0, "2019-09-30T13:00:00.000Z": 0, "2019-10-01T10:00:00.000Z": 0, "2019-09-30T15:00:00.000Z": 0, "2019-10-01T09:00:00.000Z": 0, "2019-10-01T07:00:00.000Z": 0, "2019-10-01T08:00:00.000Z": 0, "2019-10-01T05:00:00.000Z": 0, "2019-09-30T17:00:00.000Z": 0, "2019-09-30T18:00:00.000Z": 0, "2019-09-30T14:00:00.000Z": 0, "2019-10-01T11:00:00.000Z": 0}}'
]]

discovery = {'': [(None, {})]}

checks = {
    '': [(None, {}, [(0, 'Input: 425.14 kB', [('graylog_input', 435345, None,
                                               None, None, None)]),
                     (0, 'Output: 871.47 kB', [('graylog_output', 892382, None,
                                                None, None, None)]),
                     (0, 'Decoded: 900.80 kB', [('graylog_decoded', 922424,
                                                 None, None, None, None)]),
                     (0, 'Last updated: 2019-10-01 14:00:00', [])])]
}
