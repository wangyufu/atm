#!/usr/bin/env python
import time
from core1 import db_handler


def acc_auth2(account, password):
    '''
    优化版认证接口
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None

    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)
    if data['password'] == password:
        return data
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")


def acc_login(log_obj):
    retry_count = 0
    while retry_count < 3:
        user = input("\033[32;1muser:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth2(user, password)
        if auth:  # not None means passed the authentication
            return auth
        retry_count += 1
    else:
        log_obj.error("account [%s] too many login attempts" % user)
        exit()
