"""BlackJack"""
def main(num):
    """Calculate Card Score"""
    ace_count = 0
    score = 0
    card_text = ["J","K","Q"]
    for _ in range(num):
        card = input()
        if card == "A":
            score += 11
            ace_count += 1
        elif card in card_text:
            score += 10
        else:
            score += int(card)
    if score > 21 and ace_count > 0:
        while True:
            if score <= 21:
                break
            score -= 10
            ace_count -= 1
    print(score)
main(int(input()))
