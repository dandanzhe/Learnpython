import itertools as it

def rolldice_sum_prob(sum_, dice_amount):
    return len( [ combination for combination in list( it.product( range(1,7) , repeat = dice_amount) ) if sum(combination) == sum_] ) / (6.0**dice_amount)
