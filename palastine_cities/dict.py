import pandas as pd

dict={

"city": [
  "Safad",
  "Haifa",
  "Acre",
  "Tiberias",
  "Nazareth",
  "Baysan",
  "Jenin",
  "Nablus",
  "Tulkarm",
  "Ramallah",
  "Lod",
  "Jaffa",
  "Ramla",
  "Jerusalem",
  "Hebron",
  "Gaza",
  "Beersheba",
  "Dead Sea"
],
    "x":[63.0,3.0,28.0,56.0,38.0,59.0,32.0,48.0,-3.0,29.0,1.0,-17.0,-19.0,39.0,7.0,-41.0,-18.0,60.0],
    "y":[238.0,194.0,230.0,205.0,194.0,175.0,167.0,126.0,145.0,100.0,99.0,116.0,88.0,72.0,41.0,57.0,-42.0,38.0]
}

data=pd.DataFrame(dict)
data.to_csv("python_bootcamp\\palastine_cities\\palastine_cities.csv")  # Save the DataFrame to a CSV file with UTF-8 encoding

data_city = pd.read_csv("python_bootcamp\\palastine_cities\\palastine_cities.csv")
print (data_city["city"])

