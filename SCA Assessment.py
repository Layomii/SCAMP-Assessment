books_data = pd.read_csv("/kaggle/input/amazon-top-50-bestselling-books-2009-2019/bestsellers with categories.csv")
name_data = books_data["Name"]
author_data = books_data["Author"]
user_rating_data = books_data["User Rating"]
year_data = books_data["Year"]
plt.plot(price_data, year_data)
plt.xlabel("price_data")
plt.ylabel("year_data")
plt.title("Trends over the Years")
plt.show()