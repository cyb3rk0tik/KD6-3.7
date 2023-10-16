import utils


def alb_alg_nin(nin):
    dict_albania_yy = utils.read_csv_like_dict('modules/data/albania_yy.csv')
    dict_albania_mm = utils.read_csv_like_dict('modules/data/albania_mm.csv')
    dict_albania_dd = utils.read_csv_like_dict('modules/data/albania_dd.csv')
    # checking the length
    length = len(nin)
    if length != 10:
        print('Wrong length of the Albanian National Identification Number. Please, try again')
        return()
    # checking the YY parameter
    yy = nin.upper()[0:2]
    if yy in dict_albania_yy['YY']: 
        bd_year = dict_albania_yy['YYYY'][dict_albania_yy['YY'].index(yy)]
    else:
        print('The Albanian National Identification Number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = nin.upper()[2:4]
    if mm in dict_albania_mm['MM']:
        bd_month = dict_albania_mm['Month'][dict_albania_mm['MM'].index(mm)] 
        sex = dict_albania_mm['Sex'][dict_albania_mm['MM'].index(mm)] 
    else:
        print('The Albanian National Identification Number is wrong. Please, try again')
        return()
    # checking the dd parameter
    dd = nin.upper()[4:6]
    if dd in dict_albania_dd['DD']:
        bd_day = dict_albania_dd['Day'][dict_albania_dd['DD'].index(dd)] 
    else:
        print('The Albanian National Identification Number is wrong. Please, try again')
        return()
    sss = nin.upper()[6:9]
    c = nin.upper()[9]
    print('\nHere\'s what I got from that Albanian National Identification Number:\nDay of birth: ', bd_day, '\nMonth of birth: ',
          bd_month, '\nYear of birth: ', bd_year, '\nSex: ', sex,
          '\nSequence number of person with the same date of birth: ', int(sss), '\nChecksum symbol: ', c, '\n')
    return()
