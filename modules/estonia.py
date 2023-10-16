import utils


def est_alg_nin(nin):
    dict_estonia_yy = utils.read_csv_like_dict('modules/data/estonia_yy.csv')
    dict_estonia_mm = utils.read_csv_like_dict('modules/data/estonia_mm.csv')
    dict_estonia_dd = utils.read_csv_like_dict('modules/data/estonia_dd.csv')
    # checking the length
    length = len(nin)
    if length != 11:
        print('Wrong length of the Estonian National Identification Number. Please, try again')
        return()
    # checking the G parameter
    g = nin[0]
    if int(g) % 2 == 0:
        sex = 'Female'
    else:
        sex = 'Male'
    # checking the YY parameter
    yy = nin[1:3]
    if yy in dict_estonia_yy['YY']: 
        if 1 <= int(g) <= 2:
            bd_year = dict_estonia_yy['YYYY_1-2'][dict_estonia_yy['YY'].index(yy)]
        elif 3 <= int(g) <= 4:
            bd_year = dict_estonia_yy['YYYY_3-4'][dict_estonia_yy['YY'].index(yy)]
        elif 5 <= int(g) <= 6:
            bd_year = dict_estonia_yy['YYYY_5-6'][dict_estonia_yy['YY'].index(yy)]
    else:
        print('The Estonian National Identification Number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = nin[3:5]
    if mm in dict_estonia_mm['MM']:
        bd_month = dict_estonia_mm['Month'][dict_estonia_mm['MM'].index(mm)]
    else:
        print('The Estonian National Identification Number is wrong. Please, try again')
        return()
    # checking the DD parameter
    dd = nin[5:7]
    if dd in dict_estonia_dd['DD']:
        bd_day = dict_estonia_dd['Day'][dict_estonia_dd['DD'].index(dd)]
    else:
        print('The Estonian National Identification Number is wrong. Please, try again')
        return()
    # checking the SSS parameter
    sss = nin[7:10]
    c = nin[10]
    msg = f'\nPersonal mail for contacting government agencies: {nin}@eesti.ee'
    print('\nHere\'s what I got from that Estonian National Identification Number:\nDay of birth: ', bd_day, '\nMonth of birth: ', bd_month,
          '\nYear of birth: ', bd_year, '\nSex: ', sex,
          '\nSequence number of person with the same date of birth: ', int(sss), '\nChecksum symbol: ', c,
          msg, '\n')
    return()
