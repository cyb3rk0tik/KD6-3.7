import utils


def bih_alg_nin(nin):
    dict_bih_yyy = utils.read_csv_like_dict('modules/data/bosnia_herzegovina_yyy.csv')
    dict_bih_mm = utils.read_csv_like_dict('modules/data/bosnia_herzegovina_mm.csv')
    dict_bih_dd = utils.read_csv_like_dict('modules/data/bosnia_herzegovina_dd.csv')
    dict_bih_rr = utils.read_csv_like_dict('modules/data/bosnia_herzegovina_rr.csv')
    # checking the length
    length = len(nin)
    if length != 13:
        print('Wrong length of the Bosnian National Identification Number. Please, try again')
        return()
    # checking the DD parameter
    dd = nin[0:2]
    if dd in dict_bih_dd['DD']: 
        bd_day = dict_bih_dd['Day'][dict_bih_dd['DD'].index(dd)]
    else:
        print('The Bosnian National Identification Number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = nin[2:4]
    if mm in dict_bih_mm['MM']:
        bd_month = dict_bih_mm['Month'][dict_bih_mm['MM'].index(mm)]
    else:
        print('The Bosnian National Identification Number is wrong. Please, try again')
        return()
    # checking the YYY parameter
    yyy = nin[4:7]
    if yyy in dict_bih_yyy['YYY']:
        bd_year = dict_bih_yyy['YYYY'][dict_bih_yyy['YYY'].index(yyy)]
    else:
        print('The Bosnian National Identification Number is wrong. Please, try again')
        return()
    # checking the RR parameter
    rr = nin[7:9]
    if rr in dict_bih_rr['RR']:
        status = dict_bih_rr['Status'][dict_bih_rr['RR'].index(rr)]
        reg = dict_bih_rr['Political region'][dict_bih_rr['RR'].index(rr)]
    else:
        print('The Bosnian National Identification Number is wrong. Please, try again')
        return()
    # checking the BBB parameter
    bbb = nin[9:12]
    if bbb.isnumeric():
        if 0 <= int(bbb) <= 499:
            sex = 'Male'
        else:
            sex = 'Female'
    else:
        print('The Bosnian National Identification Number is wrong. Please, try again')
        return()
    k = nin[12]
    print('\nHere\'s what I got from that Bosnian National Identification Number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex, '\nStatus: ', status,
          '\nPolitical region of birth (for persons born before 1976, political region where they '
          'were first registered): ', reg, '\nChecksum symbol: ', k, '\n')
    return()
