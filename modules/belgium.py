import utils


def bel_alg_nin(nin):
    dict_belgium_yy = utils.read_csv_like_dict('modules/data/belgium_yy.csv')
    dict_belgium_mm = utils.read_csv_like_dict('modules/data/belgium_mm.csv')
    dict_belgium_dd = utils.read_csv_like_dict('modules/data/belgium_dd.csv')
    # checking the length
    length = len(nin)
    if length != 11:
        print('Wrong length of the Belgium National Identification Number . Please, try again')
        return()
    # checking the YY parameter
    yy = nin[0:2]
    if yy in dict_belgium_yy['YY']:
        bd_year = dict_belgium_yy['YYYY'][dict_belgium_yy['YY'].index(yy)]
    else:
        print('The Belgium National Identification Number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = nin[2:4]
    if mm in dict_belgium_mm['MM']:
        bd_month = dict_belgium_mm['Month'][dict_belgium_mm['MM'].index(mm)]
    else:
        print('The Belgium National Identification Number is wrong. Please, try again')
        return()
    # checking the DD parameter
    dd = nin[4:6]
    if dd in dict_belgium_dd['DD']:
        bd_day = dict_belgium_dd['Day'][dict_belgium_dd['DD'].index(dd)]
    else:
        print('The Belgium National Identification Number is wrong. Please, try again')
        return()
    # checking the XXX parameter
    xxx = nin[6:9]
    if xxx.isnumeric():
        if int(xxx) % 2 == 0:
            sex = 'Female'
        else:
            sex = 'Male'
    else:
        print('The Belgium National Identification Number is wrong. Please, try again')
        return()
    cd = nin[9:11]
    print('\nHere\'s what I got from that Belgium National Identification Number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex, '\nChecksum number: ', cd)
    return()


def bel_alg_icn(icn):
    if len(icn) == 12:
        print('\nHere\'s what I got from that Belguim Identity Card Number:\nThe card owner is a Belgium citizen\n')
        return()
    elif len(icn) == 9:
        print('\nHere\'s what I got from that Belguim Identity Card Number:\nThe card owner is a third country citizen\n')
        return()
    elif len(icn) == 10:
        print('\nHere\'s what I got from that Belguim Identity Card Number:\nThe card owner is a EU/EEA/Swiss citizen\n')
        return()
    else:
        print('The ID number is wrong. Please, try again')
        return()
