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


**1. Blank Map at the Start**

<img width="1583" height="998" alt="Image" src="https://github.com/user-attachments/assets/af20994c-0617-471b-bfe9-c4781262b9c1" />




Type the name of a city in the prompt.


If correct, the city name will appear on the map in the right position.


**2. After Guessing Some Cities (Score Increased)**

<img width="952" height="846" alt="Image" src="https://github.com/user-attachments/assets/c78e770c-d568-43a8-ac15-6cd56af073e4" />


If you guess all cities, a congratulations message will appear.

**3. After Guessing All Cities**

<img width="1492" height="913" alt="Image" src="https://github.com/user-attachments/assets/ec3bd73d-a9ff-4fa9-8457-4c57c301670b" />

Type Exit to end the game and create a cities_tolearn.csv file with missed cities.

## Example of cities_tolearn.csv
```
0,Haifa
1,Acre
2,Tiberias
3,Nazareth
```
## 🚧 Challenges Faced

One of the main challenges in building this game was that there was **no ready-made map of Palestine with city coordinates** available.  

To solve this:

1. I manually extracted the coordinates of each city by clicking on the map using this helper function:
```python
# Helper function to get coordinates by clicking on the map
def get_mouse_click_coor(x, y):
    print(x, y)

screen.onscreenclick(get_mouse_click_coor)
```
I collected the coordinates into a Python dictionary.

I converted that dictionary into a CSV file (palastine_cities.csv) to make it easier to load and process with pandas.
ر

## ❤️ Support & Contributions

If you like this project, give it a ⭐ on GitHub — it really helps!
Contributions are welcome! Feel free to fork this repo and submit a pull request.

## ❤️ Final word
Cities are like memories — if we don't keep naming them, they fade away. Let's keep Palestine alive in our hearts and maps. ❤️🍉
