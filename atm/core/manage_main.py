#!/usr/bin/env python
import time
from core import accounts


def create_account(account_new_passwd):
    '''
    Create a new account
    :param account_new_passwd: character
    '''
    account_id_record = accounts.load_current_balance('account_id_record')
    account_new_id = account_id_record['id'] + 1
    account_new_data = {
        'id': account_new_id,
        'password': account_new_passwd,
        'credit': 15000,
        'balance': 15000,
        'enroll_date': time.strftime('%F', time.localtime()),
        'expire_date': '%d-%d-%d' % (time.localtime()[0] + 5, time.localtime()[1], time.localtime()[2]),
        'pay_day': 22,
        'status': 0  # 0 = normal, 1 = locked, 2 = disabled
    }
    success_created = accounts.dump_create_account(account_new_data)
    if success_created:
        account_id_record['id'] = account_new_id
        accounts.dump_account_id_record('account_id_record', account_id_record)


def frozen_account(account):
    pass


def user_quota(account):
    pass


def logout():
    exit('logout')


def interactive():
    '''
    interact with manage
    '''
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- Manage ---------
    \033[32;1m1.  创建账户
    2.  冻结账户(未实现)
    3.  用户额度(未实现)
    4.  退出
    \033[0m'''
    menu_dic = {
        '1': create_account,
        '2': frozen_account,
        '3': user_quota,
        '4': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            if user_option == '1':
                option = input('\033[32;1mPlease enter a new user password>>:\033[0m').strip()
            elif user_option == '4':
                menu_dic[user_option]()
            else:
                option = input('\033[32;1mPlease enter the bank account>>:\033[0m').strip()
            menu_dic[user_option](option)
        else:
            print("\033[31;1mOption does not exist!\033[0m")
