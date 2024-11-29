# JPEG vs JPEG 2000 Comparison

## Introduction
This project by Gustavo Fonseca and Hunter Baisden and aims to compare the loading times and display qualities of JPEG and JPEG 2000 images. It includes a Flask web application that allows users to view different image formats.

## Features
- Display Baseline JPEG images.
- Show Progressive JPEG images.
- Simulate Hierarchical loading of JPEG images.
- Compare JPEG with JPEG 2000 counterparts.

## Installation
To run this project, you need to have Python and Flask installed. Follow these steps:

1. Clone the repository:
```
git clone https://github.com/gvfonseca/my-projects.git
cd my-projects/
```

2. Set up a virtual environment (optional but recommended):
```
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Run the Flask application:
```
python app.py
```

## Usage
Once the application is running, navigate to `http://localhost:5000` in your web browser. You will see a home page with links to different image formats.

## Project Structure
- `app.py`: The Flask application's main file with route definitions.
- `templates/`: Contains the HTML templates for the web application.
- `static/`: Stores the images used in the web application.


