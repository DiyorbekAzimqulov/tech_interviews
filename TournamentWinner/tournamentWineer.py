
# Complexity analysis, Time complexity->O(n), Space complexity-> O(n)
def tournamentWinner(competitions, results):
    # Write your code here.
    team_score = {}
    for i in range(len(results)): # traverse array
        if results[i] == 0:
            winner_team = competitions[i][1]
            loser_team = competitions[i][0]
        if winner_team not in team_score:
            team_score[winner_team] = 3
        else:
            team_score[winner_team] += 3
        if loser_team not in team_score:
            team_score[loser_team] = 0
        else:
            winner_team = competitions[i][0]
            loser_team = competitions[i][1]
        if winner_team not in team_score:
            team_score[winner_team] = 3
        else:
            team_score[winner_team] += 3
        if loser_team not in team_score:
            team_score[loser_team] = 0

    max_value = max(list(team_score.values()))
    for k, v in team_score.items():
        if v == max_value:
            return k

