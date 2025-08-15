# 🍅  Pomodoro Timer – Productivity Adventure ⚡

A fun and practical **Pomodoro** app built with **Python + Tkinter** that helps you take control of your time and get more done… while enjoying the process!
Here, work isn’t just a timer… it’s a race against yourself 💪🔥

---

## 🎥 Watch the Adventure (Demo)
[![watch the video ](https://img.youtube.com/vi/pPJfpVvRzWc/maxresdefault.jpg)](https://youtu.be/pPJfpVvRzWc)


---

## 💡 The Concept

The Pomodoro technique breaks your work into intervals, usually 25 minutes, separated by short breaks. This app automates that process:

* **Work session** → focus on your task.
* **Short break** → refresh.
* **Long break** after 4 work sessions → recharge fully.

---

## ✨ Features

* Built with Python’s **Tkinter** GUI library.
* **Canvas** displays a tomato image and countdown timer.
* Buttons: **START** (begin sessions) and **RESET** (reset timer and progress).
* ✔️ marks show completed work sessions.
* Fully customizable work and break durations.

---

## How It Works (Code Overview)

[<img width="666" height="375" alt="Image" src="https://github.com/user-attachments/assets/17ee30a5-bc58-4057-92b2-118bc94973da" />](https://youtu.be/pPJfpVvRzWc)

1. **`start_mechanism()`** – Starts a work/break session based on repetition count (`reps`).
2. **`count_down(count)`** – Updates the timer every second using `window.after()` and triggers the next session when the count reaches 0.
3. **`timer_reset()`** – Cancels any scheduled countdown, resets `reps`, and clears ✔️ marks.
4. **UI Setup** – Created using Tkinter’s `Canvas`, `Label`, and `Button` widgets.

**Main logic:**

```python
if reps % 8 == 0:
    # Long break
elif reps % 2 == 0:
    # Short break
else:
    # Work session
```

---

## ⚙️ Settings

Change these values in the code to adjust durations:

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
```

For quick testing, you can use smaller numbers like:

```python
WORK_MIN = 0.25  # 15 seconds
```

---

## How to Run

1. Save the code as `pomodoro.py`.
2. Place `tomato.png` in the correct folder and update its path in the code.
3. Run:

```bash
python pomodoro.py
```

4. Click **START** to begin your first session.

---

## 🛠️ Future Ideas

* Add sound notifications when a session ends.
* Show session statistics (total work time, breaks taken).
* Theme customization.

---

## 🙌 Final Note

This app is your personal productivity coach. Every ✔️ is proof of your progress toward your goals 🎯.

> Ready? Hit START and make every second count 💥

