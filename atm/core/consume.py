#!/usr/bin/env python
import sys, os

base_dir = os.path.normcase(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         os.path.pardir))
sys.path.insert(0, base_dir)

from core.auth import login_required
from core import transaction
from core import logger
from core import db_handler

trans_logger = logger.logger('transaction')


@login_required
def consume(account, total_price):
    '''
    print current balance and let user repay the bill
    :return:
    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account['id'])

    new_balance = transaction.make_transaction(trans_logger, data, 'consume', total_price, type='consume')
    if new_balance:
        return True


