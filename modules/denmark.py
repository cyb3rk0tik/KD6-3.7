import utils


def dnk_alg_nin(nin):
    dict_denmark_yys = utils.read_csv_like_dict('modules/data/denmark_yys.csv')
    dict_denmark_mm = utils.read_csv_like_dict('modules/data/denmark_mm.csv')
    dict_denmark_dd = utils.read_csv_like_dict('modules/data/denmark_dd.csv')
    # checking the length
    length = len(nin)
    if length != 10:
        print('Wrong length of the Danish National Identification Number. Please, try again')
        return ()
    # checking the DD parameter
    dd = nin[0:2]
    if dd in dict_denmark_dd['DD']: 
        bd_day = dict_denmark_dd['Day'][dict_denmark_dd['DD'].index(dd)]
    else:
        print('The Danish National Identification Number is wrong. Please, try again DD')
        return()
    # checking the MM parameter
    mm = nin[2:4]
    if mm in dict_denmark_mm['MM']:
        bd_month = dict_denmark_mm['Month'][dict_denmark_mm['MM'].index(mm)]
    else:
        print('The Danish National Identification Number is wrong. Please, try again XX')
        return()
    # checking the YY parameter
    yy = nin[4:6]
    if yy in dict_denmark_yys['YY']:
        if 0 <= int(nin[6]) <= 3:
            bd_year = dict_denmark_yys['YYYY_0-3'][dict_denmark_yys['YY'].index(yy)]
        elif int(nin[6]) == 4:
            bd_year = dict_denmark_yys['YYYY_4'][dict_denmark_yys['YY'].index(yy)]
        elif 5 <= int(nin[6]) <= 8:
            bd_year = dict_denmark_yys['YYYY_5-8'][dict_denmark_yys['YY'].index(yy)]
        elif int(nin[6]) == 9:
            bd_year = dict_denmark_yys['YYYY_9'][dict_denmark_yys['YY'].index(yy)]
    else:
        print('The Danish National Identification Number is wrong. Please, try again YY')
        return()
    # checking the SSSS parameter
    ssss = nin[9]
    if int(ssss) % 2 == 0:
        sex = 'Female'
    else:
        sex = 'Male'
    print('\nHere\'s what I got from that Danish National Identification Number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex, '\n')
    return()
