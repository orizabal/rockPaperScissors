# import random module
import random

hands = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
}

# print instructions
print(
    'Welcome to Rock, Paper, Scissors! The rules of the game are as follows: \n' +
    'Rock beats scissors \n' +
    'Scissors beats paper \n' +
    'Paper beats rock \n'
)

while True:
    print(
        'What hand will you play? \n' +
        '1 = Rock \n' +
        '2 = Paper \n' +
        '3 = Scissors \n'
    )

    hand = int(input('Your hand: '))

    # make sure user's input is valid
    while hand > 3 or hand < 1:
        hand = int(input('Please enter valid input: '))

    # when user enters valid input
    print(
        'You\'ve played ' + hands[hand] + '\n' +
        'The computer will play... '
    )

    # generate computer's hand
    comp_hand = random.randint(1, 3)

    print(hands[comp_hand] + '! \n')

    # compare hands
    if (comp_hand == hand):
        print('It\'s a tie!')
        result = comp_hand
    elif ((comp_hand == 1 and hand == 2) or (comp_hand == 2 and hand == 1)):
        print(
            hands[hand] + ' vs. ' + hands[comp_hand] + '\n' +
            'Paper beats rock! \n'
        )
        result = 2
    elif ((comp_hand == 1 and hand == 3) or (comp_hand == 3 and hand == 3)):
        print(
            hands[hand] + ' vs. ' + hands[comp_hand] + '\n' +
            'Rock beats scissors! \n'
        )
        result = 1
    else:
        print(
            hands[hand] + ' vs. ' + hands[comp_hand] + '\n' +
            'Scissors beats rock! \n'
        )
        result = 3

    # print result
    if (comp_hand == result and hand == result):
        print('\n')
    elif(comp_hand == result):
        print('Computer wins! \n')
    elif(hand == result):
        print('You win! \n')

    # ask to play again
    ans = input('Would you like to play again? (Y/N): ')

    while (ans != 'n' and ans != 'N' and ans != 'y' and ans != 'Y'):
        ans = input('Please enter valid input (Y/N): ')
    
    if (ans == 'n' or ans == 'N'):
        break

print('Thank you for playing! \n')
    
