*This project simulates a simplified recommendation pipeline
similar to those used in music streaming platforms.

Created by Carlos Alvares.
# music_recommendation_tool

## Description
This project implements a simple content-based music recommendation engine.
The system analyzes user-selected reference tracks and preferred genres to identify similar songs based on artist, genre and decade similarity.

### Goal
To output the best list of recommended songs according to the user profile which consists in chosen genres and favorite songs.

### The challenges and solutions
• Cold start problem  
Since no listening history is available in a CLI environment,
the system uses user-selected reference tracks to infer preferences.

• Feature extraction  
Artists and decades are extracted from the selected tracks and stored
in sets to allow efficient similarity checks.

• Recommendation scoring  
Tracks receive points based on three similarity signals:
artist match, genre match and decade match.

## System Design

### Full program flow:
```
CLI
↓
selected_tracks + genre
↓
input_profile()
↓
profile
↓
engine(dataset, profile)
↓
scores
↓
top N recommendations
```

## The algorithm
For each track in the dataset:

1. Initialize score = 0
2. If track genre matches the user's preferred genre → add points
3. If track artist matches one of the reference artists → add points
4. If track decade matches one of the reference decades → add points
5. Bonus points proportional to the track release year to break ties between tracks with similar scores.

Tracks are then ranked by score and the top N recommendations are returned.

## Project Structure
```
miniRT/
│
├── main.py
├── cli.py
├── engine.py
├── dataset.json
├── README.md
└── images/
    └── programDesign.png
```
## How to Run
```
Clone the repository:

https:

git clone https://github.com/danifontenele/music_recommendation_tool

or

ssh:

git clone git@github.com:danifontenele/Musical_recomendation_tool.git

Run the program:

python3 main.py
```
## Example run
```
User input
Genre: Pop
Reference tracks:
- Blinding Lights
- One dance

Recommendations:
1. Save Your Tears - The Weeknd
2. Levitating - Dua Lipa
3. Get Lucky - Daft Punk
```

## Limitations
The recommendations are based only on metadata similarity
(artist, genre and decade).

Future improvements could include:
- additional audio features
- popularity signals
- collaborative filtering
