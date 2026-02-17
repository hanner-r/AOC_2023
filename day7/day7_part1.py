from collections import Counter

with open('day7_input.txt', 'r') as input_file:
    hand_info = input_file.readlines()
    hand_info = [line.replace('\n', '') for line in hand_info]

hands_list = []
for hand in hand_info:
    hands_list.append((hand[:5], int(hand[6:])))

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []


def determine_hand_type(given_hand):
    hand_pattern = sorted(Counter(given_hand[0]).values(), reverse=True)
    if hand_pattern == [5]:
        five_of_a_kind.append(given_hand)
    elif hand_pattern == [4, 1]:
        four_of_a_kind.append(given_hand)
    elif hand_pattern == [3, 2]:
        full_house.append(given_hand)
    elif hand_pattern == [3, 1, 1]:
        three_of_a_kind.append(given_hand)
    elif hand_pattern == [2, 2, 1]:
        two_pair.append(given_hand)
    elif hand_pattern == [2, 1, 1, 1]:
        one_pair.append(given_hand)
    else:
        high_card.append(given_hand)


for hand in hands_list:
    determine_hand_type(hand)

# I have sorted the hands into lists based on the type of hand that they are.
# Next I need to sort within these lists based on the first card, second card, so on.
# Can use sort with key=function to give sort criteria as a function.
# What would that function need to do to sort correctly?
