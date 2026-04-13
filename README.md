# 🎓 Faculty Evaluation Automation Bot (Playwright)

Automate your university faculty evaluation process using Python + Playwright.
This bot logs in, navigates to pending evaluations, fills responses, and submits them automatically.

---

## 🚀 Features

* 🔐 Automatic login (Student portal)
* 📋 Detects pending evaluations (skips completed ones)
* 🧠 Fills all dropdowns automatically
* 🔀 Randomized answers (more human-like behavior)
* 🧾 Handles popups (e.g., "Perform Mandatory Evaluation")
* 🧭 Supports multiple evaluations in one run
* 🗂️ Handles new tabs automatically
* ⚡ Fast and efficient

---

## 🛠️ Tech Stack

* Python 3.10+
* Playwright (Browser Automation)

---

## 📦 Installation

### 1. Clone the repository

```bash
https://github.com/Abpattar/Feedback_Automation.git
cd faculty-evaluation-bot
```

### 2. Install dependencies

```bash
pip install playwright
```

OR (recommended for Windows users):

```bash
python -m pip install playwright
```

### 3. Install browsers

```bash
python -m playwright install
```

---

## ⚙️ Configuration

Open `bot2.py` and replace:

```python
USERNAME = "YOUR_ID"
PASSWORD = "YOUR_PASSWORD"
```

⚠️ **Important:**

* Do NOT share your credentials publicly
* Consider using environment variables for security

---

## ▶️ Usage

Run the script:

```bash
python bot2.py
```

---

## 🧠 How It Works

1. Opens the university portal
2. Logs in as a student
3. Navigates to evaluation dashboard
4. Handles popup automatically
5. Detects pending evaluations
6. Opens evaluation (new tab)
7. Fills all dropdowns
8. Submits the form
9. Repeats until all evaluations are completed

---

## ⚠️ Disclaimer

* This project is for **educational purposes only**
* Use responsibly and at your own risk
* Some platforms may detect automation behavior
* Do not misuse or violate institutional policies

---

## 🐞 Troubleshooting

### ❌ Login not working

* Check username/password
* Website UI may have changed → update selectors

### ❌ Dropdowns not filling

* Inspect dropdown structure
* Update selector in code

### ❌ Popup not handled

* Increase timeout in `handle_popup()`

---

## 💡 Future Improvements

* 🔐 Environment variable support for credentials
* 🤖 Human-like mouse movement
* 📊 Logging and reporting
* 🌐 Support for other portals

---

## 🤝 Contributing

Pull requests are welcome!
If you find a bug or want to improve something, feel free to contribute.

---

## ⭐ Support

If this helped you, consider giving a ⭐ on GitHub!

---

## 👨‍💻 Author

Made with 💻 by [Your Name]

---
