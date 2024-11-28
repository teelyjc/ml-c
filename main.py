import pandas

if __name__ == "__main__":
  d: pandas.DataFrame = pandas.read_csv("./california_housing_train.csv")
  print(d.head())