# Palestine Cities Quiz 🍉

**Game Description**  
When you start the game, a **blank map of Palestine** 🗺 will appear.  
Your task is to type the names of Palestinian cities one by one so they appear in their correct locations on the map.  

- ✅ If you guess **all the cities**, a **congratulations message** will be displayed 🎉.  
- ❌ If you don't guess some cities, at the end of the game a **`cities_tolearn.csv`** file will be created with the names of the cities you missed, so you can learn them later.  

**Important Note**:  
To play the game correctly, you must also have:
1. The **`palastine_cities.csv`** file containing the cities and their coordinates.
2. The map image **`map.gif`**.

---

## Features
- 🗺 Shows a blank map of Palestine at the start.
-    Adds guessed cities to their correct positions on the map.
-    Displays your score in real-time.
-    Creates a file of cities you didn’t guess.

---

## 📂 Project Structure
```
palestine_cities_quiz/
│
├── palastine_cities.py # Main game script
├── score.py # Score handling class
├── palastine_cities.csv # Cities with coordinates
├── cities_tolearn.csv # Generated file for missed cities
├── map.gif # Map image
└── README.md # Project documentation
```

---

## ⚙️ How to Run
1. Install the required library:
```bash
pip install pandas
```

Make sure you have:

palastine_cities.csv (cities + coordinates).

map.gif (map image).

2. Run the game:
```
python palastine_cities.py
```
## 🎮 How to Play

When the game starts, a blank map of Palestine will appear.

Type the name of a city in the prompt.

If correct, the city name will appear on the map in the right position.

Type Exit to end the game and create a cities_tolearn.csv file with missed cities.

If you guess all cities, a congratulations message will appear.


##Example of cities_tolearn.csv
```
0,Haifa
1,Acre
2,Tiberias
3,Nazareth
...
