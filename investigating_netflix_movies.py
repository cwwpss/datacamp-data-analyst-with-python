# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
netflix_df = pd.read_csv("netflix_data.csv")

# Remove TV shows from netflix_df
netflix_subset = netflix_df[netflix_df["type"] != "TV Show"]

# Sub-set data only title, country, genre, release_year and duration column
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# filter duration of moive that shorter than 60
short_movies = netflix_moives[netflix_moives["duration"] < 60]

# Create colors list for build chart
colors = []
for i, n in netflix_movies.iterrows():
    if n["genre"] == "Children":
        colors.append("green")
    elif n["genre"] == "Documentaries":
        colors.append("blue")
    elif n["genre"] == "Stand-Up":
        colors.append("yellow")
    else:
        colors.append("red")

# Create chart for analysis trend of movies
fig = plt.figure()
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c = colors)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')
plt.show()

answer = "no" 
