# Import pandas library
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("netflix_titles.csv")

# Check first 5 rows
print(df.head())

# Check dataset info
print(df.info())

# Count Movies vs TV Shows
type_count = df['type'].value_counts()
print(type_count)

# Bar chart
plt.figure(1)
type_count.plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.savefig("figure_1_movies_vs_tvshows.png")
plt.show()


# Year-wise content count
year_count = df['release_year'].value_counts().sort_index()

# Line graph
plt.figure(2)
plt.plot(year_count.index, year_count.values)
plt.title("Year-wise Netflix Content Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.savefig("figure_2_yearwise_trend.png")
plt.show()


# Split genres (listed_in) and count them
genres = df['listed_in'].str.split(', ')
all_genres = genres.explode()

# Top 10 genres
top_genres = all_genres.value_counts().head(10)
print(top_genres)

# Bar chart for top genres
plt.figure(3)
top_genres.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.savefig("figure_3_top_genres.png")
plt.show()

# Rating distribution
rating_count = df['rating'].value_counts()
print(rating_count)

# Bar char
plt.figure(4)
rating_count.plot(kind='bar')
plt.title("Netflix Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.savefig("figure_4_rating_distribution.png")
plt.show()

# India vs Other Countries analysis
india_count = df[df['country'].str.contains('India', na=False)].shape[0]
other_count = df.shape[0] - india_count

# Data for plot
country_data = {
    'India': india_count,
    'Other Countries': other_count
}

# Pie chart
plt.figure(5)
plt.pie(
    country_data.values(),
    labels=country_data.keys(),
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Netflix Content: India vs Other Countries")
plt.savefig("figure_5_india_vs_others.png")
plt.show()



