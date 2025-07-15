# 🐢 habitTurtle

> A minimalist desktop habit tracker with a streak counter and smart turtle mascot.

---

## ✨ What It Does

habitTurtle helps you build daily habits by tracking your consistency — like solving a LeetCode problem or going for a walk — and displays a cute turtle mascot that reacts to your progress.

- 🧠 Smart streak counter  
- 🐢 Turtle mascot with emotional states  
- ✅ One-click “Mark as Done” button  
- 📆 JSON-based habit logging  
- 🖥️ Lightweight PyQt5 GUI

---

## 🚀 Features

- 🔥 Tracks daily streak automatically
- 🐢 Mascot changes meme based on streak
- 📅 JSON data is auto-created and updated
- 📈 GUI updates in real-time
- ⚙️ Built using: Python 3.10+, PyQt5

---

## 🖥️ How to Run

1. Make sure you have Python 3.10+ installed
2. Install required packages:

```bash
pip install -r requirements.txt
Run the application:
```

bash
Copy
Edit
python main.py
📦 Build a Windows Executable (Optional)
To create a standalone .exe:
```bash
Copy
Edit
pyinstaller --onefile --windowed --add-data "assets;assets" main.py
🗂 Make sure the assets/ folder is in the same directory and includes all mascot images.
```
```
📁 Project Structure
css
Copy
Edit
habitTurtle/
├── main.py
├── gui.py
├── storage.py
├── habits.json
├── requirements.txt
├── assets/
│   ├── happy.png
│   ├── nervous.png
│   ├── angry.png
│   ├── sad.png
│   ├── sleeping.png
│   └── ... (more moods)
└── README.md
```
```
🐢 Mascot Moods
Mood	When it shows up
😊 Happy	You completed today's habit ✅
😰 Nervous	You're getting close to the end of day

These are probably future iterations i might do , need to find some more memes and set the logic too
😴 Sleepy	It's still early, you're safe
😡 Angry	You're very late! Don't break the streak
😢 Sad	You missed a day
🤩 Excited	Long streaks or early solves
```
🧠 Why I Built This
To learn how to structure small Python projects, use real-time GUI updates, manage state with JSON, and make habit tracking fun using mascots like a turtle. This is part of a learning journey to complete 20–30 meaningful mini-projects for mastery.

🔗 License
MIT License — free to use, modify, and share.
