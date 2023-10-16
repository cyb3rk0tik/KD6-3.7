import utils


def svk_alg_nin(nin):
    dict_slovakia_yy = utils.read_csv_like_dict('modules/data/cze_svk_yy.csv')
    dict_slovakia_xx = utils.read_csv_like_dict('modules/data/cze_svk_xx.csv')
    dict_slovakia_dd = utils.read_csv_like_dict('modules/data/cze_svk_dd.csv')
    # checking the length
    c = 'None (for people born before 1 January 1954)'
    length = len(nin)
    if length == 10:
        c = nin[9]
    elif length == 9:
        pass
    else:
        print('Wrong length of the Slovak National Identification Number. Please, try again')
        return()
    # checking the YY parameter
    yy = nin[0:2]
    if yy in dict_slovakia_yy['YY']:
        bd_year = dict_slovakia_yy['YYYY'][dict_slovakia_yy['YY'].index(yy)]
    else:
        print('The Slovak National Identification Number is wrong. Please, try again YY')
        return()
    # checking the XX parameter
    xx = nin[2:4]
    if xx in dict_slovakia_xx['XX']:
        bd_month = dict_slovakia_xx['Month'][dict_slovakia_xx['XX'].index(xx)]
        sex = dict_slovakia_xx['Sex'][dict_slovakia_xx['XX'].index(xx)]
    else:
        print('The Slovak National Identification Number is wrong. Please, try again XX')
        return()
    # checking the DD parameter
    dd = nin[4:6]
    if dd in dict_slovakia_dd['DD']:
        bd_day = dict_slovakia_dd['Day'][dict_slovakia_dd['DD'].index(dd)]
    else:
        print('The Slovak National Identification Number is wrong. Please, try again DD')
        return()
    # checking the XXX parameter
    sss = nin[6:9]
    print('\nHere\'s what I got from that Slovak National Identification Number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex,
          '\nSequence number of person with the same date of birth: ', int(sss), '\nChecksum symbol: ',
          c, '\n')
    return()
