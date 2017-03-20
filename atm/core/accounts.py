from core import db_handler


def load_current_balance(account_id):
    '''
    return account balance and other basic info
    :param account_id:
    :return:
    '''
    # db_path = db_handler.db_handler(settings.DATABASE)
    # account_file = "%s/%s.json" %(db_path,account_id)
    #
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account_id)

    return data


def dump_account(account_data):
    '''
    after updated transaction or account data , dump it back to file db
    :param account_data:
    :return:
    '''
    db_api = db_handler.db_handler()
    data = db_api("update accounts where account=%s" % account_data['id'], account_data=account_data)

    # db_path = db_handler.db_handler(settings.DATABASE)
    # account_file = "%s/%s.json" %(db_path,account_data['id'])
    # with open(account_file, 'w') as f:
    #     acc_data = json.dump(account_data,f)
    return True


def dump_account_id_record(account_new_data, file):
    '''
    Create account id record
    :param account_new_data:
    :return:
    '''
    db_api = db_handler.db_handler()
    data = db_api("create table %s" % account_new_data, data=file)
    return True


def dump_create_account(account_new_data):
    '''
    Create a new account
    :param account_new_data:
    :return:
    '''
    db_api = db_handler.db_handler()
    data = db_api("create table %s" % account_new_data['id'], data=account_new_data)
    if data:
        print('\033[34;1mSuccessfully created %d\033[0m' % account_new_data['id'])
    return True