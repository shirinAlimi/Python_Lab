candidates = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

valid_votes = 0
rejected_votes = 0

while True:
    vote = input("Enter candidate name or DONE to finish: ")

    if vote.upper() == "DONE":
        break

    found = False

    for candidate in candidates:
        if candidate.lower() == vote.lower():
            candidates[candidate] += 1
            valid_votes += 1
            found = True
            break

    if not found:
        rejected_votes += 1
        print("Rejected vote.")

print("\nElection Results")

for candidate, votes in candidates.items():
    print(candidate + ":", votes)

print("Total valid votes:", valid_votes)
print("Rejected votes:", rejected_votes)

if valid_votes == 0:
    print("No valid votes were submitted.")
else:
    print("\nVote percentages:")

    for candidate, votes in candidates.items():
        percentage = (votes / valid_votes) * 100
        print(candidate + ":", percentage, "%")

    highest_votes = None

    for candidate, votes in candidates.items():
        if highest_votes is None or votes > highest_votes:
            highest_votes = votes

    winners = []

    for candidate, votes in candidates.items():
        if votes == highest_votes:
            winners.append(candidate)

    if len(winners) == 1:
        print("Winner:", winners[0])
    else:
        print("Tie between:")

        for winner in winners:
            print(winner)