import time
from core import db_handler


def login_required(func):
    "验证用户是否登录"

    def wrapper(*args, **kwargs):
        # print('--wrapper--->',args,kwargs)
        db_api = db_handler.db_handler()
        data = db_api("select * from accounts where account=%s" % args[0]['id'])
        if data is not None:
            return func(*args, **kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper


def acc_auth2(account, password):
    '''
    优化版认证接口
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None

    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)
    if data is not None:
        if data['password'] == password:
            exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
            if time.time() > exp_time_stamp:
                print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
            elif data['status'] != 0:
                exit('User to freeze')
            else:  # passed the authentication
                return data
        else:
            print("\033[31;1mAccount ID or password is incorrect!\033[0m")
    else:
        exit()


def acc_login(user_data, log_obj):
    '''
    Account password interaction, password will correct account information saved in the user_data
    :param user_data: user_data
    :param log_obj: access_logger
    :return: Account information
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth2(account, password)
        if auth:  # not None means passed the authentication
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()
