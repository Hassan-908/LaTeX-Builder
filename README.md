# LaTeX Resume Builder (Django)

A minimal Django project that renders a **LaTeX (`.tex`) file into a PDF** and serves it directly in the browser.  
This is an MVP-style setup focused only on **LaTeX → PDF rendering**, without forms, AI, or user input yet.

---

## Features
1. Renders a `.tex` file using `pdflatex`
2. Serves the generated PDF directly in the browser
3. Uses a temporary directory for safe compilation
4. Handles LaTeX errors properly (no infinite loading)

---

## Tech Stack
- Python
- Django
- LaTeX (MiKTeX on Windows / TeX Live on Linux)
- `pdflatex` (system-level dependency)

---

## Follow the steps to run the project
1. Go to https://miktex.org/download and install the app
2. During the installation set "Install missing packages on-the-fly → Yes"
3. Keep the application running (it will be in the app tray)
4. git clone https://github.com/Hassan-908/Latex-Resume-Builder/
5. cd Resume Builder
6. python -m venv venv
7. venv\Scripts\activate
8. pip install -r requirements.txt
9. python manage.py runserver



### Working Demo

<img width="1866" height="956" alt="image" src="https://github.com/user-attachments/assets/ae2d469f-39a0-4341-a1fd-05ead04837c1" />
