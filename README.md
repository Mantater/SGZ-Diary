# Project Title: SGZ Diary 

## Description:
A personal digital diary that stores your entries on your computer using SQLite database, secured with hashing function.

## Installation:
1. Clone repo
```sh
git clone https://github.com/Mantater/SGZ-Diary.git
```
2. Install dependencies
```sh
pip install -r requirements.txt
```
3. Run project (**not** for ver0)
```sh
python Main.py
```

or

- Download `.exe` file then run it


## Usage:
1. Login (default password is empty)
2. Use the Menu to:
    - Write a new diary entry
    - View previous entries
    - Reset your password

## Features:
- Simple and intuitive interface: Login → Menu → Write/View entries → Reset password
- Default password is blank ("") — just press Login
- Automatically creates a new database if one doesn’t exist
- All entries are stored securely in a local SQLite database

## License:
This project uses the MIT License.
- The code in this repo is open-source and free to use.

## Notes:
- Don't forget your password cause I don't know how to get it back :')
- You can still view the notes from the database if you have SQLite 
- Feel free to download 'old versions' to view the progression

## Versions / Changelog:
- ver0 – Initial build: created the project from scratch and got the basic diary functionality working.
- ver1 – Added entry storage and password protection. Password reset feature was missing.
- ver2 – Current version: fully functional, compiled into a .exe for easy use.
