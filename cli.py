from modules import albania, bosnia_herzegovina, belgium, bulgaria, denmark, \
france, estonia, finland, czech_republic, slovakia
from argparse import ArgumentParser
import utils


def main():
    parser = ArgumentParser()
    
    parser.add_argument("-c", "--country", dest="country", 
                        type=str, choices=['alb', 'fin', 'fra', 'svk', 'cze', 'bgr', 'dnk', 'est', 'bih', 'bel'],
                        help="Input country.")
    
    parser.add_argument("--nin", dest="nin", 
                        type=str, help="National Identification Number.")   
                        
    parser.add_argument("--icn", dest="icn", 
                        type=str, help="Identity Card Number.")  
                        
    parser.add_argument("--ssn", dest="ssn", 
                        type=str, help="Social Security Number.")

    parser.add_argument("-a", "--auto", dest="auto", 
                        type=str, help="Autodetection.")  

    args = parser.parse_args()  

    if args.auto:
        check = utils.check_string_type(args.auto)
            
        if len(args.auto) == 13:
            if 'a' in check and 'd' in check: 
                france.fra_alg_nin(args.auto)
            elif 'd' in check: 
                bosnia_herzegovina.bih_alg_nin(args.auto)
                
        elif len(args.auto) == 12:
            if 'd' in check: 
                belgium.bel_alg_icn(args.auto)
                
        elif len(args.auto) == 11:
            if 'a' in check and 'd' in check: 
                finland.fin_alg_nin(args.auto)
            elif 'd' in check:
                belgium.bel_alg_nin(args.auto)
                estonia.est_alg_nin(args.auto)
                
        elif len(args.auto) == 10:
            if 'a' in check and 'd' in check: 
                albania.alb_alg_nin(args.auto) 
            elif 'd' in check:
                belgium.bel_alg_icn(args.auto) 
                bulgaria.bgr_alg_nin(args.auto)
                czech_republic.cze_alg_nin(args.auto)
                denmark.dnk_alg_nin(args.auto)
                slovakia.svk_alg_nin(args.auto)
                
        elif len(args.auto) == 9:
            if 'd' in check:
                belgium.bel_alg_icn(args.auto)
                czech_republic.cze_alg_nin(args.auto)
                slovakia.svk_alg_nin(args.auto)
        
    else:
        if args.country == 'alb' and args.nin:
            albania.alb_alg_nin(args.nin) 
        
        elif args.country == 'bel':
            if args.nin:
                belgium.bel_alg_nin(args.nin)
            elif args.icn:
                belgium.bel_alg_icn(args.icn)
            
        elif args.country == 'bih' and args.nin:
            bosnia_herzegovina.bih_alg_nin(args.nin)
    
        elif args.country == 'bgr' and args.nin:
            bulgaria.bgr_alg_nin(args.nin)
        
        elif args.country == 'cze' and args.nin:    
            czech_republic.cze_alg_nin(args.nin)
        
        elif args.country == 'dnk' and args.nin:         
            denmark.dnk_alg_nin(args.nin)  
        
        elif args.country == 'est' and args.nin: 
            estonia.est_alg_nin(args.nin)

        elif args.country == 'fin' and args.nin:  
            finland.fin_alg_nin(args.nin)
        
        elif args.country == 'fra' and args.ssn:  
            france.fra_alg_nin(args.ssn)
        
        elif args.country == 'svk' and args.nin:  
            slovakia.svk_alg_nin(args.nin)
        
if __name__ == "__main__":
    main()