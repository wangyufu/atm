import os

from core import auth
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}

# transaction logger
trans_logger = logger.logger('transaction')
# access logger
access_logger = logger.logger('access')


def account_info(acc_data, log_obj):
    '''
    Print information other than the password
    :param acc_data:
    :return:
    '''
    row = max([len(x) for x in user_data['account_data']])
    for k, v in acc_data['account_data'].items():
        if k != 'password':
            print('%s : %s' % (k.ljust(row), v))


def repay_withdraw(acc_data, log_obj, rw):
    '''
    Print and operating withdrawals and repayment
    :param acc_data: user_data
    :param log_obj: trans_logger
    :param rw: 'repay' or 'withdraw'
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        rw_amount = input("\033[33;1mInput %s amount:\033[0m" % rw).strip()
        if len(rw_amount) > 0 and rw_amount.isdigit():
            new_balance = transaction.make_transaction(log_obj, account_data, rw, rw_amount)
            if new_balance:
                print('\033[34;1mNew Balance:%s\033[0m' % (new_balance['balance']))
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % rw_amount)

        if rw_amount == 'b':
            back_flag = True


# def withdraw(acc_data, log_obj):
#     '''
#     print current balance and let user do the withdraw action
#     :param acc_data:
#     :return:
#     '''
#     account_data = accounts.load_current_balance(acc_data['account_id'])
#     current_balance = ''' --------- BALANCE INFO --------
#         Credit :    %s
#         Balance:    %s''' % (account_data['credit'], account_data['balance'])
#     print(current_balance)
#     back_flag = False
#     while not back_flag:
#         withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
#         if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
#             new_balance = transaction.make_transaction(account_data, 'withdraw', withdraw_amount)
#             if new_balance:
#                 print('\033[33;1mNew Balance:%s\033[0m' % (new_balance['balance']))
#         else:
#             print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)
#
#         if withdraw_amount == 'b':
#             back_flag = True


def transfer(acc_data, log_obj):
    '''
    Print and transfer operation
    :param acc_data: user_data
    :param log_obj: trans_logger
    '''
    my_account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (my_account_data['credit'], my_account_data['balance'])
    print(current_balance)
    transfer_account_data = None
    count = 0
    while transfer_account_data is None and count < 3:
        transfer_account = input('\033[33;1mInput transfer account:\033[0m')
        transfer_account_data = accounts.load_current_balance(transfer_account)
        if transfer_account_data is not None:
            print('\033[34;1mTransfer accounts to normal!\033[0m')
            break
        count += 1
    else:
        print('\033[31;1m Try to too many!\033[0m')
        exit()
    back_flag = False
    while not back_flag:
        transfer_amount = input("\033[33;1mInput transfer amount:\033[0m").strip()
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            my_balance = transaction.make_transaction(log_obj, my_account_data, 'transfer', transfer_amount)
            transaction.make_transaction(log_obj, transfer_account_data, 'repay', transfer_amount, type='transfer_receive')
            if my_balance:
                print('\033[34;1mNew Balance:%s\033[0m' % (my_balance['balance']))
        elif transfer_amount == 'b':
            back_flag = True
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % transfer_amount)


def pay_check(acc_data, log_obj):
    '''
    Print the account transaction log information
    :param acc_data: user_data
    :param log_obj: trans_logger
    '''
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(base_dir+'/log/transactions.log', 'r') as f:
        [print(i) for i in [line for line in f.readlines() if line.find('account:'+acc_data['account_id']) != -1]]


def logout(acc_data, log_obj):
    exit('Successfully logged off')


def interactive(acc_data):
    '''
    interact with user
    '''
    menu = u'''
    -------  Bank ---------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay_withdraw,
        '3': repay_withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    rw = (None, None, 'repay', 'withdraw')
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # acc_data['is_authenticated'] = False
            if user_option == '2' or user_option == '3':
                menu_dic[user_option](acc_data, trans_logger, rw[eval(user_option)])
            else:
                menu_dic[user_option](acc_data, trans_logger)

        else:
            print("\033[31;1mOption does not exist!\033[0m")


def run():
    '''
    User login auth
    '''
    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)

