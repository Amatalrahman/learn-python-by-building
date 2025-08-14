print("القدس الشريف")
import pandas as pd
data= pd.read_csv("python_bootcamp\\palastine_cities\\palastine_cities.csv")
print (len(data["city"]))