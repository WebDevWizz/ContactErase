# ContactErase - A Terminal-Based Phonebook Application

**ContactEase** is a Python command-line application that allows users to manage their phone contacts easily and intuitively. Developed as a final course project, it leverages Object-Oriented Programming (OOP) principles to provide a clean, scalable, and user-friendly structure.

## 🧠 Purpose

The goal is to simplify the organization and retrieval of personal contact information through an interactive text-based interface. The app allows users to add, edit, delete, search, view, save, and load contacts in JSON format.

## 📁 Project Structure

- `Contact.py`: Defines the `Contact` class, representing a single contact entry.
- `Phonebook.py`: Handles the phonebook logic, including storage and contact manipulation.
- `UserInterface.py`: Manages user interaction via terminal menus.
- `main.py`: Entry point of the application.

## 🚀 Requirements

- Python 3.8+
- Python virtual environment (optional but recommended)

## 🛠️ Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/contactease.git
cd contactease
```

### 2. Create and activate the virtual environment:
python3 -m venv my_venv
source my_venv/bin/activate (On Windows: my_venv\Scripts\activate) 


## Usage
Launch the app from the terminal: 
python main.py

## Data Peristence 
Contacts are stored in a contacts.json file, which is automatically loaded the next time the app is run.
