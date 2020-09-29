import Functions.DataFunctions as df
import Functions.WebhookFunctions as wf
import Functions.Statistics as stats

recentMatches = df.getRecentMatches(False)
for match in recentMatches:
    print(match["match_id"], match["version"])
print(len(recentMatches))

# df.parseRecentMatches(recentMatches)

stats.calculateWinRateAgainst(recentMatches)