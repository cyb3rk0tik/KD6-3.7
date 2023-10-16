import utils


def fin_alg_nin(nin):
    dict_finland_yy = utils.read_csv_like_dict('modules/data/finland_yy.csv')
    dict_finland_mm = utils.read_csv_like_dict('modules/data/finland_mm.csv')
    dict_finland_dd = utils.read_csv_like_dict('modules/data/finland_dd.csv')

    # checking the length
    length = len(nin)
    if length != 11:
        print('Wrong length of the Finnish National Identification Number. Please, try again')
        return()
    # checking the DD parameter
    dd = nin[0:2]
    if dd in dict_finland_dd['DD']: 
        bd_day = dict_finland_dd['Day'][dict_finland_dd['DD'].index(dd)]
    else:
        print('The Finnish National Identification Number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = nin[2:4]
    if mm in dict_finland_mm['MM']:
        bd_month = dict_finland_mm['Month'][dict_finland_mm['MM'].index(mm)]
    else:
        print('The Finnish National Identification Number is wrong. Please, try again')
        return()
    # checking the YY parameter
    yy = nin[4:6]
    if yy in dict_finland_yy['YY']:
        pass
    else:
        print('The Finnish National Identification Number is wrong. Please, try again')
        return()
    # checking the C parameter
    c = nin.upper()[6]
    xixcent = ['+']
    xxcent = ['-', 'U', 'V', 'W', 'X', 'Y']
    xxicent = ['A', 'B', 'C', 'D', 'E', 'F']
    if c in xixcent:
        bd_year = dict_finland_yy['YYYY_19'][dict_finland_yy['YY'].index(yy)]
    elif c in xxcent:
        bd_year = dict_finland_yy['YYYY_20'][dict_finland_yy['YY'].index(yy)]
    elif c in xxicent:
        bd_year = dict_finland_yy['YYYY_21'][dict_finland_yy['YY'].index(yy)]
    else:
        print('The Finnish National Identification Number is wrong. Please, try again')
        return()
    # checking the ZZZ parameter
    zzz = nin[7:10]
    if int(zzz) % 2 == 0:
        sex = 'Female'
    else:
        sex = 'Male'
    q = nin.upper()[10]
    print('\nHere\'s what I got from that Finnish National Identification Number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex,
          '\nSequence number of person with the same date of birth: ', int(zzz), '\nChecksum symbol: ',
          q, '\n')
    return()
