import json


def load_data() -> dict:
    with open("data_set.json", "r") as f:
        dataset = json.load(f)
    return dataset


def compute_scores(dataset: dict, profile) -> list:
    tracks_and_scores_list = []
    for track in dataset.values():
        score = 0
        if track in profile["reference_tracks"]:
            continue
        if track["artist"] in profile["artists"]:
            score += 4
        if track["genre"] == profile["genre"]:
            score += 3
        if ((track["year"] // 10) * 10) in profile["decades"]:
            score += 2
        # Bonus as a tiebreaker criterion
        bonus = (track["year"]) / 10000
        score += bonus
        tracks_with_scores = (track, score)
        tracks_and_scores_list.append(tracks_with_scores)
    return tracks_and_scores_list


# The algorithm that will give points to genre, decade and
# artist matches and return top N recommendations.
def engine(profile: dict):
    # load the dataset
    dataset = load_data()
    # Compute the scores by gender and artist matches
    tracks_and_scores_list = compute_scores(dataset, profile)
    # Descending sorting
    tracks_and_scores_list.sort(key=lambda track: track[1], reverse=True)
    # Return N recommendations:
    N = 5
    top_tracks = tracks_and_scores_list[:N]
    return top_tracks
