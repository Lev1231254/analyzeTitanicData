import pandas as pd

def turn_to_numeric(args):
    if args['sex'] == 'male': args['sex'] = 0
    else: args['sex'] = 1
    return args