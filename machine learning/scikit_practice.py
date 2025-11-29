import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

matches = pd.read_csv("matches.csv", index_col=0)

matches["target"] = (matches["Result"]).astype("category").cat.codes
matches["Date"] = pd.to_datetime(matches["Date"], format="%d/%m/%Y")
matches["Venue_code"] = matches["Venue"].astype("category").cat.codes
matches["Opp_code"] = matches["Opponent"].astype("category").cat.codes
matches = matches.dropna(subset=["Time"])
matches["hour"] = matches["Time"].str.replace(":.+", "", regex=True).astype(int)
matches["day_code"] = matches["Date"].dt.dayofweek

rf = RandomForestClassifier(n_estimators=100, min_samples_split=10, random_state=1)
train = matches[matches["Date"] < '2023-01-02']
test = matches[matches["Date"] > '2023-01-01']
predictors = ["Venue_code", "Opp_code", "hour", "day_code", "GF", "GA"]
rf.fit(train[predictors], train["target"])

preds = rf.predict(test[predictors])
accuracy = accuracy_score(test["target"], preds)

grouped_matches = matches.groupby("Team")
group = grouped_matches.get_group("Manchester City").sort_values("Date")

def rolling_averages(group, cols, new_cols):
    group = group.sort_values("Date")
    rolling_stats = group[cols].rolling(3, closed='left').mean()
    group[new_cols] = rolling_stats
    group = group.dropna(subset=new_cols)


cols = ["GF", "GA", "Sh", "SoT", "FK", "PK", "PKatt"]
new_cols = [f"{c}_rolling" for c in cols]

matches_rolling = matches.groupby("Team").apply(lambda x: rolling_averages(x, cols, new_cols))
matches_rolling = matches_rolling.reset_index(drop=True)  # Simple flat index
matches_rolling.index = range(matches_rolling.shape[0])


def make_predictions(data, predictors):
    train = data[data["Date"] < '2023-01-02']
    test = data[data["Date"] > '2023-01-01']
    rf.fit(train[predictors], train["target"])
    preds = rf.predict(test[predictors])
    combined = pd.DataFrame(dict(actual=test["target"], predicted=preds), index=test.index)
    accuracy = accuracy_score(test["target"], preds)
    return combined, accuracy

combined, accuracy = make_predictions(matches_rolling, predictors + new_cols)

combined = combined.merge(matches_rolling[["Date", "Team", "Opponent", "Result"]], left_index=True, right_index=True)

class MissingDict(dict):
    __missing__ = lambda self, key: key

map_values = {"Brighton and Hove Albion": "Brighton",
              "Manchester United": "Manchester Utd",
              "Newcastle United": "Newcastle Utd",
              "Tottenham Hotspur": "Tottenham",
              "West Ham United": "West Ham",
              "Wolverhampton Wanderers": "Wolves"
              }
mapping = MissingDict(**map_values)

combined["Team"] = combined["Team"].map(mapping)
combined["Opponent"] = combined["Opponent"].map(mapping)

