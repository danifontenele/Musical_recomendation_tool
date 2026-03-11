*This is a personal project to simulate a simple music recommendation engine by Carlos Alvares.
# music_recommendation_tool

## Description
This project implements a simple content-based music recommendation engine.
The system analyzes user-selected reference tracks and preferred genres to identify similar songs based on artist, genre and decade similarity.

The goal is to simulate a simplified recommendation pipeline similar to those used in music streaming platforms.

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
top N recomendações
```
### Flow explained:
![ProgramDesign](images/programDesign.png)

## The algorithm
For each track in the dataset:

1. Initialize score = 0
2. If track genre matches the user's preferred genre → add points
3. If track artist matches one of the reference artists → add points
4. If track decade matches one of the reference decades → add points

Tracks are then ranked by score and the top N recommendations are returned.

## Example run
```
User input
Genre: Pop
Reference tracks:
- Blinding Lights
- One dance

Recommendations:
1. Save your tears
2. Levitating
3. Get Lucky