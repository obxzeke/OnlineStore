# Online Store

## Description

This repository stands as a vibrant Flask-based mock e-commerce platform crafted with Python, showcasing the collaborative efforts of a dynamic team from the Software Engineering class (ITSC 3155) at UNCC. Elevating our project, we incorporated an SQL database for refined data management and seamlessly integrated a hashing system to fortify the authentication process for secure logins.

## Demo Video
https://www.loom.com/share/6072dd8757254b4e8c86ff653144dfb6?sid=79b32f5a-caa1-459b-8704-09ac5c051056

## How to Use

To run this project, you simply need to have Python 3.10 installed on your machine. You can download Python 3.10 from the [official website](<https://www.python.org/downloads/release/python-3108>). To complete each project milestone, OS-specific dependencies (such as `Graphviz` for generating UML diagrams) may need to be installed. These dependencies are listed in the project instructions.

### Setup and Installation

All module dependencies are listed in the `requirements.txt` file. To install these dependencies, run the following command from the root of the repository:

```bash
pip3 install -r requirements.txt
# Note: depending on your system, you may need to use `pip` or `python3.10 -m pip1 instead of `pip3`
```

### Database Setup

The project uses a SQLite database, which is stored in the `database` directory. To create or reset the database, navigate to the `database` directory and run the following command:

```bash
python3 reset_database.py
# Note: depending on your system, you may need to use `python3.10` or `py` instead of `python3`
```

### Running the Server

Once all installation steps are complete, the `app.py` script can be run to start the server. Follow the local server URL that is printed to the console to view the website.

### Admin Privlages 
Use login username: admin password: admin for admin privileges.

## Documentation Style

Across all files, classes and functions are documented using docstrings, which are formatted according to the [Google Python Style Guide](<https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>).

Additionally, detailed documents for the project code folders (`authentication`, `core`, `database`, `static` `templates`, and `tests`) have been provided in the `docs/directories` folder. These documents describe the purpose of each file in the folder and how they interact with each other.

## Testing

The unit tests are kept across various files in the `testing` directory. From the root of the repository, you can run the `test.py` script to check all unit tests, which will generate a report in the `testing/reports` directory.
