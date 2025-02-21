import itertools as it
from math import comb
def flipMonedas(p, event):
    q = 1 - p
    # Definimos las monedas como tuplas (tipo, p = cara, q = cruz)
    monedas = [
        ("p", p),  # p = cara
        ("p", p),  # p = cara
        ("q", q)   # q = cruz
    ]
    # Probabilidad Total
    p_cara = sum((1/3) * p for (_, p) in monedas)

    # P(A|p)
    p_AyCara = sum((1/3) * p for (tipo, p) in monedas if tipo == event)

    # P(A | cara)
    p_A_dado_cara = p_AyCara / p_cara

    print("Ejercicio 1:")
    print(f"La probabilidad de que sea moneda A dado que salió cara es: {p_A_dado_cara:.4f}")

flipMonedas(p= 1/4, event= "p")


def cardPickerIndepency():
    suits = ['C', 'D', 'H', 'S']  # 4 suits
    ranks = range(1, 14)          # 13 ranks
    # Full deck
    deck = [(rank, suit) for suit in suits for rank in ranks]
    num_cards = len(deck)  # 52
    # Sample space for 3 cards with replacement:
    total_combinations = num_cards ** 3

    def same_suit(card1, card2):
        return card1[1] == card2[1]

    # Counters
    count_e = 0
    count_f = 0
    count_g = 0
    count_ef = 0
    count_eg = 0
    count_fg = 0
    count_efg = 0

    for card1, card2, card3 in it.combinations(deck, 3):
        event_e = same_suit(card1, card2)
        event_f = same_suit(card2, card3)
        event_g = same_suit(card1, card3)

        count_e += event_e
        count_f += event_f
        count_g += event_g
        count_ef += event_e and event_f
        count_eg += event_e and event_g
        count_fg += event_f and event_g
        count_efg += event_e and event_f and event_g

    probability_e = count_e / total_combinations
    probability_f = count_f / total_combinations
    probability_g = count_g / total_combinations

    probability_ef = count_ef / total_combinations
    probability_eg = count_eg / total_combinations
    probability_fg = count_fg / total_combinations

    probability_efg = count_efg / total_combinations

    print("Exercise 3:")
    print("\n- Pairwise independence (equalities hold).")
    if (probability_ef == probability_e * probability_f and
            probability_eg == probability_e * probability_g and
            probability_fg == probability_f * probability_g):
        print("Events E with F, E with G, F with G are independent")
    else:
        print("Events E with F, E with G, F with G are not independent")

    if probability_efg == probability_e * probability_f * probability_g:
        print("Events E, F, and G are independent")
    else:
        print("Events E, F, and G are not independent")
cardPickerIndepency()



def urn():
    # Balls: 'W' = white, 'R' = red
    box1 = ['W', 'R', 'R', 'R', 'R']  # 1W, 4R
    box2 = ['W', 'W', 'R', 'R', 'R']  # 2W, 3R
    box3 = ['W', 'W', 'W', 'R', 'R']  # 3W, 2R
    # a) Probability of drawing exactly 2 red balls given box1 is not chosen
    def probability_two_reds(box):
        # Calculate P(2R) without replacement in 3 draws
        # = (# ways to choose 2R and 1W) / # ways to choose 3 out of 5
        num_reds = box.count('R')
        num_whites = box.count('W')
        ways_two_reds = comb(num_reds, 2) * comb(num_whites, 1)
        total_ways = comb(len(box), 3)
        return ways_two_reds / total_ways

    prob_two_reds_box2 = probability_two_reds(box2)
    prob_two_reds_box3 = probability_two_reds(box3)

    prob_two_reds_given_not_box1 = 0.5 * prob_two_reds_box2 + 0.5 * prob_two_reds_box3

    print("Exercise 4:")
    print("a) Probability of drawing exactly 2 red balls given box1 is not chosen:")
    print(f"   P(2R | not box1) = {prob_two_reds_given_not_box1:.4f}")

    # b) Compare P(2 reds) vs P(more whites than reds) (overall, with 1/3 probability for each box)
    def probability_of_event_in_box(box, condition):
        total_combinations = 0
        satisfying_combinations = 0
        for combo in it.combinations(box, 3):
            total_combinations += 1
            if condition(combo):
                satisfying_combinations += 1
        return satisfying_combinations / total_combinations

    def is_two_reds(triple):
        return triple.count('R') == 2

    def more_whites_than_reds(triple):
        return triple.count('W') > triple.count('R')

    # Probability of each "global" event = average of the 3 boxes (1/3 each)
    prob_two_reds_global = (probability_of_event_in_box(box1, is_two_reds) +
                            probability_of_event_in_box(box2, is_two_reds) +
                            probability_of_event_in_box(box3, is_two_reds)) / 3

    prob_more_whites_global = (probability_of_event_in_box(box1, more_whites_than_reds) +
                               probability_of_event_in_box(box2, more_whites_than_reds) +
                               probability_of_event_in_box(box3, more_whites_than_reds)) / 3

    print("\nb) Comparison of global probabilities:")
    print(f"   P(2 reds)               = {prob_two_reds_global:.4f}")
    print(f"   P(more whites than reds)= {prob_more_whites_global:.4f}")
    if prob_two_reds_global > prob_more_whites_global:
        print("  It is more probable to draw exactly 2 reds.")
    else:
        print("  It is more probable to draw more whites than reds.")

    # c) P(box3 | 2R) = [P(2R|box3)*P(box3)] / P(2R)
    # Using previously calculated values:
    prob_box3 = 1 / 3
    prob_two_reds_box3 = probability_of_event_in_box(box3, is_two_reds)
    prob_box3_given_two_reds = (prob_two_reds_box3 * prob_box3) / prob_two_reds_global

    print("\nc) Probability of having chosen box3 given that exactly 2 reds were drawn:")
    print(f"   P(box3 | 2R) = {prob_box3_given_two_reds:.4f}")

urn()


