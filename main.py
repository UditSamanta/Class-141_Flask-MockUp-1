import csv
from flask import Flask, jsonify, request
allMovies = []

with open('movies.csv', encoding="utf-8") as f:
    r = csv.reader(f)
    data = list(r)
    allMovies = data[1:]

likedMovies = []
nonLikedMovies = []
didNotWatch = []

app = Flask(__name__)

@app.route('/get-movie')
def getMovie():
    return jsonify({
        'data':allMovies[0],
        'status':'success'
    })

@app.route('/liked-Movie', methods = ['POST'])
def likedMovies():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    likedMovies.append(movie)
    return jsonify({
        'status' : 'success'
    }), 201

@app.route('/non-Liked-Movie', methods = ['POST'])
def nonLikedMovies():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    nonLikedMovies.append(movie)
    return jsonify({
        'status' : 'success'
    }), 201

@app.route('/didNotWatch', methods = ['POST'])
def didNotWatch():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    didNotWatch.append(movie)
    return jsonify({
        'status' : 'success'
    }), 201

if __name__ == '__main__':
    app.run()