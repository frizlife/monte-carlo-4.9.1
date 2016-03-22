'''This script demonstrates simulations of coin flipping'''
import random
import matplotlib.pyplot as plt

# let's create a fair coin object that can be flipped:

class Coin(object):
    '''this is a simple fair coin, can be pseudorandomly flipped'''
    sides = ('one', 'two', 'three', 'four', 'five', 'six')
    last_result = None

    def flip(self):
        '''call coin.flip() to flip the coin and record it as the last result'''
        self.last_result = result = random.choice(self.sides)
        return result

# let's create some auxilliary functions to manipulate the coins:

def create_coins(number):
    '''create a list of a number of coin objects'''
    return [Coin() for _ in xrange(number)]

def flip_coins(coins):
    '''side effect function, modifies object in place, returns None'''
    for coin in coins:
        coin.flip()

def count_one(flipped_coins):
    return sum(coin.last_result == 'one' for coin in flipped_coins)

def count_two(flipped_coins):
    return sum(coin.last_result == 'two' for coin in flipped_coins)
    
def count_three(flipped_coins):
    return sum(coin.last_result == 'three' for coin in flipped_coins)

def count_four(flipped_coins):
    return sum(coin.last_result == 'four' for coin in flipped_coins)
    
def count_five(flipped_coins):
    return sum(coin.last_result == 'five' for coin in flipped_coins)

def count_six(flipped_coins):
    return sum(coin.last_result == 'six' for coin in flipped_coins)

cnt_min = []
cnt_max = []
def main():
    coins = create_coins(1000)
    for i in xrange(100):
        flip_coins(coins)
        print("Number of ones: " + str(count_one(coins)))
        print("Number of two: " + str(count_two(coins)))
        print("Number of three: " + str(count_three(coins)))
        print("Number of four: " + str(count_four(coins)))
        print("Number of five: " + str(count_five(coins)))
        print("Number of six: " + str(count_six(coins)))
        
        cnt_min.append(min(count_one(coins), count_two(coins), count_three(coins), count_four(coins), count_five(coins), count_six(coins)))
        cnt_max.append(max(count_one(coins), count_two(coins), count_three(coins), count_four(coins), count_five(coins), count_six(coins)))

if __name__ == '__main__':
    main()
    print cnt_min
    plt.hist(cnt_min)
    plt.show()
    plt.clf()
    print cnt_max
    plt.hist(cnt_max)
    plt.show()