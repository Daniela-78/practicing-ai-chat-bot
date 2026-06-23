# practicing-ai-chat-bot
A chat bot i built practicing my python skills = it's rule based
# Python Chatbot Project Setup

Welcome! This guide will help you set up everything you need before we start building our Python chatbot.

No prior Python experience is required.

---

# 1. Install Python

Python is the programming language we'll use for this project.

### Download Python

👉 https://www.python.org/downloads/

### Windows Users

When installing Python, **make sure you check the box that says:**

```text
☑ Add Python to PATH
```

before clicking **Install Now**.

### Verify Python Installation

Open a terminal or command prompt and run:

```bash
python --version
```

You should see something similar to:

```bash
Python 3.13.5
```

If you see a version number, Python is installed correctly.

---

# 2. Install Visual Studio Code (VS Code)

VS Code is the code editor we'll use to write our chatbot.

### Download VS Code

👉 https://code.visualstudio.com/

Install it using the default settings.

After installation, open VS Code.

---

# 3. Install VS Code Extensions

In VS Code:

1. Click the **Extensions** icon on the left sidebar.
2. Search for and install the following extensions:

### Required

- **Python** (Microsoft)
- **Pylance** (Microsoft)

### Recommended

- **Ruff**
  - Helps find errors and improve code quality.

- **GitLens**
  - Makes Git easier to understand and use.

---

# 4. Install Git

Git helps us track changes in our project and work with GitHub.

### Download Git

👉 https://git-scm.com/downloads

Install Git using the default settings.

### Verify Git Installation

Open a terminal and run:

```bash
git --version
```

You should see something similar to:

```bash
git version 2.x.x
```

---

# 5. Create a Project Folder

Create a folder anywhere on your computer.

Example:

```text
python-chatbot
```

Open VS Code and select:

```text
File → Open Folder
```

Then open your new project folder.

---

# 6. Install Project Dependencies

Open the VS Code terminal:

```text
Terminal → New Terminal
```

If a `requirements.txt` file is provided, run:

```bash
pip install -r requirements.txt
```

You may also need:

```bash
pip install python-dotenv
```

---

# 7. Verify Everything Works

Run the following commands:

```bash
python --version
git --version
pip --version
```

If all three commands return version numbers, you're ready to start coding.

---

# ✅ Required Software Checklist

- [ ] Python installed
- [ ] VS Code installed
- [ ] Git installed
- [ ] Python extension installed
- [ ] Pylance extension installed
- [ ] Project dependencies installed

---

# You're Ready!
Everyone's README has been updated

Once you've completed all the steps above, your development environment is set up and you're ready to start building your Python chatbot.

# ChatBot Greeting Logic

`# writing the logics for chatbot greeting
""" Chatbot meant to greet, would need
- Name
- Time of the day
"""

# step 1 --> Hey there, what's the name?
print("Hey there, what's the name?")

# step 2 --> accepts user's name
name = input("name: ")
print(name)

# step 3 --> Tell python to say "Hi" with your name
print("Hi " + name)

# step 4 --> Get the time of the 
time_of_the_day = input("What time of the day is it?: ")

# step 5 --> Greet with all data provided 
print(f"Yeah! Hey {name}, Good {time_of_the_day}. It's nice to have you in here.")
`
