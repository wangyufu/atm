#!/usr/bin/env python
from core1 import auth
from core1 import logger
from core1 import db_handler
from atm.core import consume

# transaction logger
trans_logger = logger.logger('transaction')
# access logger
access_logger = logger.logger('access')


def settlement(data, goods, shopping_cart):
    '''
    Call the consume of ATM interface
    :param data:
    :param goods: goods
    :param shopping_cart: shopping_cart list
    :return:
    '''
    total_price = 0
    for i in shopping_cart:
        total_price += goods[i]
    account = {'id': input("\033[33;1mPlease enter the credit card account:\033[0m")}
    if consume.consume(account, total_price):
        print('\n\033[33;1mTo complete the payment!\033[0m')
        trans_logger.info("user:%s   goods:%s   total_price:%s   account:%s   status:%s" %
                          (data['user'], ','.join(shopping_cart), total_price, account['id'], 0))


def interactive(data):
    '''
    interact with user
    :return:
    '''
    db_api = db_handler.db_handler()
    goods = db_api("select * from accounts where account=goods")
    row = max([len(x) for x in goods])
    shopping_cart = []
    while True:
        for k, v in goods.items():
            print('\033[34;1m%s : %s\033[0m' % (k.ljust(row), v))
        print("'b'settlement，'q'exit")
        choose_goods = input("\033[33;1mInput to buy goods:\033[0m").strip()
        if choose_goods == 'b' and len(shopping_cart):
            settlement(data, goods, shopping_cart)
            shopping_cart = []
        elif choose_goods == 'q':
            exit('Out of a shopping cart')
        elif len(choose_goods) > 0 and choose_goods in goods:
            shopping_cart.append(choose_goods)
            print("\033[33;1mAdd a shopping cart\033[0m")
        else:
            print('\033[31;1m[%s] is not a valid goods!\033[0m' % choose_goods)


def run():
    '''
    User name password judgment
    :return:
    '''
    data = auth.acc_login(access_logger)
    interactive(data)
