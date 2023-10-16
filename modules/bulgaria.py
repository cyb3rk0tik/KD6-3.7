import utils


def bgr_alg_nin(nin):
    dict_bulgaria_yy = utils.read_csv_like_dict('modules/data/bulgaria_yy.csv')
    dict_bulgaria_mm = utils.read_csv_like_dict('modules/data/bulgaria_mm.csv')
    dict_bulgaria_dd = utils.read_csv_like_dict('modules/data/bulgaria_dd.csv')
    dict_bulgaria_xxs = utils.read_csv_like_dict('modules/data/bulgaria_xxs.csv')
    # checking the length
    length = len(nin)
    if length != 10:
        print('Wrong length of the Bulgarian National Identification Number. Please, try again')
        return()
    # checking the MM parameter
    mm = nin[2:4]
    if mm in dict_bulgaria_mm['MM']: 
        bd_month = dict_bulgaria_mm['Month'][dict_bulgaria_mm['MM'].index(mm)]
    else:
        print('The Bulgarian National Identification Number is wrong. Please, try again')
        return()
    # checking the YY parameter
    yy = nin[0:2]
    if yy in dict_bulgaria_yy['YY']:
        if 1 <= int(mm) <= 12:
            bd_year = dict_bulgaria_yy['YYYY_1900'][dict_bulgaria_yy['YY'].index(yy)]
        elif 21 <= int(mm) <= 32:
            bd_year = dict_bulgaria_yy['YYYY_1800'][dict_bulgaria_yy['YY'].index(yy)]
        elif 41 <= int(mm) <= 52:
            bd_year = dict_bulgaria_yy['YYYY_2000'][dict_bulgaria_yy['YY'].index(yy)]
    else:
        print('The Bulgarian National Identification Number is wrong. Please, try again')
        return()
    # checking the DD parameter
    dd = nin[4:6]
    if dd in dict_bulgaria_dd['DD']:                
        bd_day = dict_bulgaria_dd['Day'][dict_bulgaria_dd['DD'].index(dd)]
    else:
        print('The Bulgarian National Identification Number is wrong. Please, try again')
        return()
    # checking the XXX parameter
    xxs = nin[6:9]
    if dict_bulgaria_xxs['XXS'].isin([xxs]).any():
        reg = dict_bulgaria_xxs['Region'][dict_bulgaria_xxs['XXS'].index(xxs)]
    else:
        print('The Bulgarian National Identification Number is wrong. Please, try again')
        return()
    s = nin[8:9]
    if int(s) % 2 == 0:
        sex = 'Male'
    else:
        sex = 'Female'
    c = nin[9]
    print('\nHere\'s what I got from that Bulgarian National Identification Number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex, '\nPlace of birth: ', reg,
          '\nChecksum symbol: ', c, '\n')
    return()
