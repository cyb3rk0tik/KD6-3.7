import utils


def fra_alg_nin(ssn):
    dict_france_yy = utils.read_csv_like_dict('modules/data/france_yy.csv')
    dict_france_mm = utils.read_csv_like_dict('modules/data/france_mm.csv')
    dict_france_com = utils.read_csv_like_dict('modules/data/france_com.csv')
    dict_france_com_comer = utils.read_csv_like_dict('modules/data/france_com_comer.csv')
    dict_france_pays = utils.read_csv_like_dict('modules/data/france_pays.csv')
    # checking the length
    length = len(ssn)
    if length != 13:
        print('Wrong length of the French Social Security Number. Please, try again')
        return()
    # checking the S parameter
    s = ssn[0]
    temp = [3, 4, 7, 8]
    if int(s) == 1:
        sex = 'Male'
    elif int(s) == 2:
        sex = 'Female'
    elif int(s) in temp:
        sex = 'Unknown (the number has been assigned to the person on a temporary basis)'
    else:
        print('Wrong length of the French Social Security Number. Please, try again')
        return()
    # checking the YY parameter
    yy = ssn[1:3]
    if yy in dict_france_yy['YY']:
        bd_year =  dict_france_yy['YYYY'][dict_france_yy['YY'].index(yy)]
    else:
        print('The French Social Security Number is wrong. Please, try again')
        return()
    # checking the MM parameter
    mm = ssn[3:5]
    if mm in dict_france_mm['MM']: 
        bd_month = dict_france_mm['Month'][dict_france_mm['MM'].index(mm)]
    elif 20 <= int(mm) <= 30:
        bd_month = 'Unknown (the person was registered on the basis of a civil status document not specifying the ' \
                   'month of birth)'
    elif 50 <= int(mm) <= 99:
        bd_month = 'Unknown (the person was registered on the basis of a civil status document not specifying the ' \
                   'month of birth)'
    else:
        print('The French Social Security Number is wrong. Please, try again')
        return()
    # checking the LLOOO parameter
    llooo = ssn.upper()[5:10]
    if llooo in dict_france_com['COG']: 
        reg = dict_france_com['REG'][dict_france_com['COG'].index(llooo)]
        ncc_reg = dict_france_com['NCC_REG'][dict_france_com['COG'].index(llooo)]
        nccenr_reg = dict_france_com['NCCENR_REG'][dict_france_com['COG'].index(llooo)]
        libelle_reg = dict_france_com['LIBELLE_REG'][dict_france_com['COG'].index(llooo)]
        dep = dict_france_com['DEP'][dict_france_com['COG'].index(llooo)]
        ncc_dep = dict_france_com['NCC_DEP'][dict_france_com['COG'].index(llooo)]
        nccenr_dep = dict_france_com['NCCENR_DEP'][dict_france_com['COG'].index(llooo)]
        libelle_dep = dict_france_com['LIBELLE_DEP'][dict_france_com['COG'].index(llooo)]
        ncc_com = dict_france_com['NCC_COM'][dict_france_com['COG'].index(llooo)]
        nccenr_com = dict_france_com['NCCENR_COM'][dict_france_com['COG'].index(llooo)]
        libelle_com = dict_france_com['LIBELLE_COM'][dict_france_com['COG'].index(llooo)]
    elif llooo in dict_france_com_comer['COG']:
        ncc_com_comer = dict_france_com_comer['NCC_COM_COMER'][dict_france_com_comer['COG'].index(llooo)]
        nccenr_com_comer = dict_france_com_comer['NCCENR_COM_COMER'][dict_france_com_comer['COG'].index(llooo)]
        libelle_com_comer = dict_france_com_comer['LIBELLE_COM_COMER'][dict_france_com_comer['COG'].index(llooo)]
        comer = dict_france_com_comer['COMER'][dict_france_com_comer['COG'].index(llooo)]
        ncc_comer = dict_france_com_comer['NCC_COMER'][dict_france_com_comer['COG'].index(llooo)]
        nccenr_comer = dict_france_com_comer['NCCENR_COMER'][dict_france_com_comer['COG'].index(llooo)]
        libelle_comer = dict_france_com_comer['LIBELLE_COMER'][dict_france_com_comer['COG'].index(llooo)]
    elif llooo in dict_france_pays['COG']: 
        libcog = dict_france_pays['LIBCOG'][dict_france_pays['COG'].index(llooo)]
        libenr = dict_france_pays['LIBENR'][dict_france_pays['COG'].index(llooo)] 
        codeiso2 = dict_france_pays['CODEISO2'][dict_france_pays['COG'].index(llooo)]
        codeiso3 = dict_france_pays['CODEISO3'][dict_france_pays['COG'].index(llooo)]
    else:
        print('The French Social Security Number is wrong. Please, try again')
        return()
    # checking the KKK parameter
    kkk = ssn[10:12]
    mm_comment_2 = 'The person was registered on the basis of an incomplete civil status document'
    print('\nHere\'s what I got from that French Social Security Number:\nMonth of birth: ', bd_month, '\nYear of birth: ',
          bd_year, '\nSex: ', sex)
    if llooo in dict_france_com['COG']:
        print('The region of origin: ', ncc_reg, '/', nccenr_reg, '/', libelle_reg, ' (', reg,
              ')\nThe department of origin: ', ncc_dep, '/', nccenr_dep, '/', libelle_dep, ' (', dep,
              ')\nThe commune of origin: ', ncc_com, '/', nccenr_com, '/', libelle_com)
    elif llooo in dict_france_com_comer['COG']:
        print('The territory of origin: ', ncc_com_comer, '/', nccenr_com_comer, '/',
              libelle_com_comer, '\nThe commune of origin: ', ncc_comer, '/', nccenr_comer, '/',
              libelle_comer, ' (', comer, ')')
    elif llooo in dict_france_pays['COG']:
        print('The country of origin: ', libcog, '/', libenr, ' (', codeiso2, '/', codeiso3, ')')
    print('Sequence number of person with the same date of birth: ', int(kkk), '\n')
    return()
