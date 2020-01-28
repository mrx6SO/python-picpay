# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_payment 1'] = {
    'expiresAt': '2022-05-01T16:00:00-03:00',
    'paymentUrl': 'https://app.picpay.com/checkout/NWFmMGRjNmViZDc0Y2EwMDMwNzZlYzEw',
    'qrcode': {
        'base64': 'data:image/png;base64,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',
        'content': 'https://app.picpay.com/checkout/NWNlYzMxOTM1MDg1NGEwMDIwMzUxODcy'
    },
    'referenceId': '4878711'
}