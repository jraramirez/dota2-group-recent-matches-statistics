from flask import Flask, request
from flask_restful import Resource, Api

import Functions.DataFunctions as df
import Functions.WebhookFunctions as wf
import Functions.Statistics as stats

app = Flask(__name__)

@app.route('/chat-win-rate', methods=['GET'])
def chatWinRate():
    recentMatches = df.getRecentMatches(parsedOnly=False)
    winRate = stats.calculateMatchesWinRate(recentMatches)
    wf.chatWinRate(winRate)
    return {}
    
@app.route('/chat-meme-hammer-stats', methods=['GET'])
def chatmeteorHammerStats():
    recentMatches = df.getRecentMatches(parsedOnly=True)
    meteorHammerStats = stats.calculateMeteorHammerPurchases(recentMatches)
    # print(meteorHammerStats)
    wf.chatmeteorHammerStats(meteorHammerStats)
    return {}

@app.route('/parse-recent-matches', methods=['GET'])
def parseRecentMatches():
    recentMatches = df.getRecentMatches(parsedOnly=False)
    df.parseRecentMatches(recentMatches)
    return {}
    
@app.route('/chat-g', methods=['GET'])
def chatG():
    wf.chatG()
    return {}
    

if __name__ == '__main__':
     app.run(debug=True, port='5003', host='0.0.0.0')