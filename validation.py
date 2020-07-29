import argparse


def check_if_positive(number):
    num = number.isdigit()
    if not num:
        raise argparse.ArgumentTypeError(f'[-] You must enter a valid and positive number.'
                                         f'\n[*] Type "-h/--help" for more info.')
    #elif int(num) <= 0:
        #raise argparse.ArgumentTypeError(f'[-] You must enter positive number.'
                                        #f'\nType "-h/--help" for more info"')
    return number
