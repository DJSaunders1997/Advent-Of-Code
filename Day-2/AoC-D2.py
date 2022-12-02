# Advent Of Code Day 2 - https://adventofcode.com/2022/day/2
## Part 1

data = open('input.txt', 'r').read().split('\n')

# print(data)

their_response_dict = {"A": "Rock", "B": "Paper", "C": "Scissors"}
my_response_dict = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
response_score_dict = {"Rock":1, "Paper":2, "Scissors":3}
outcome_score_dict = {"Lose":0, "Draw":3, "Win":6}
game = {
    # Left is Rock
    ("Rock", "Rock"): "Draw",
    ("Rock", "Paper"): "Win",
    ("Rock", "Scissors"): "Lose",
    # Left is Paper
    ("Paper", "Paper"): "Draw",
    ("Paper", "Rock"): "Lose",
    ("Paper", "Scissors"): "Win",
    # Left is Scissors
    ("Scissors", "Scissors"): "Draw",
    ("Scissors", "Rock"): "Win",
    ("Scissors", "Paper"): "Lose",
}

def score_round(their_response_encoded, my_response_encoded):

    my_response = my_response_dict[my_response_encoded]
    their_response = their_response_dict[their_response_encoded]

    outcome = game[(their_response, my_response)]
    
    score = outcome_score_dict[outcome] + response_score_dict[my_response]

    return score

print(score_round("A", "Y"))
print(score_round("B", "X"))
print(score_round("C", "Z"))

def score_all(data):

    total_score = 0

    for round in data:
        responses = round.split(" ")
        their_response_encoded = responses[0]
        my_response_encoded = responses[1]

        round_score = score_round(their_response_encoded, my_response_encoded)

        total_score += round_score

    return total_score


print(score_all(data))
print()

## Part 2

required_outcome_dict = {"X":"Lose", "Y":"Draw", "Z":"Win"}

def score_round_match_outcome(their_response_encoded, required_outcome_encoded):

    required_outcome = required_outcome_dict[required_outcome_encoded]
    their_response = their_response_dict[their_response_encoded]
    # print(their_response)
    # print(required_outcome)

    # List possible states that could lead to required outcome
    possible_states = [states for states,outcome in game.items() if outcome == required_outcome]
    # print(possible_states)

    # Get the response from the tuple that matches their state
    my_response = [mine for theirs,mine in possible_states if theirs == their_response][0]
    # print(my_response)

    score = outcome_score_dict[required_outcome] + response_score_dict[my_response]

    return score

print(score_round_match_outcome("A", "Y"))
print(score_round_match_outcome("B", "X"))
print(score_round_match_outcome("C", "Z"))

def score_all_match_outcome(data):

    total_score = 0

    for round in data:
        responses = round.split(" ")
        their_response_encoded = responses[0]
        required_outcome_encoded = responses[1]

        round_score = score_round_match_outcome(their_response_encoded, required_outcome_encoded)

        total_score += round_score

    return total_score


print(score_all_match_outcome(data))