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
def chatMeteorHammerStats():
    recentMatches = df.getRecentMatches(parsedOnly=True)
    meteorHammerStats = stats.calculateMeteorHammerPurchases(recentMatches)
    wf.chatMeteorHammerStats(meteorHammerStats)
    return {}

@app.route('/chat-win-rate-against', methods=['GET'])
def chatWinRateAgainst():
    recentMatches = df.getRecentMatches(parsedOnly=True)
    winRateAgainstStats = stats.calculateWinRateAgainst(recentMatches)
    wf.chatWinRateAgainst(winRateAgainstStats)
    return {}

@app.route('/chat-hero-win-rates', methods=['GET'])
def chatHeroWinRates():
    recentMatches = df.getRecentMatches(parsedOnly=True)
    heroWinRates = stats.calculateHeroWinRates(recentMatches)
    wf.chatHeroWinRates(heroWinRates)
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