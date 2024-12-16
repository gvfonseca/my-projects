# Comparing JPEG vs JPEG2000

## Introduction
This project by Gustavo Fonseca and Hunter Baisden aims to compare the loading times and display qualities of JPEG and JPEG 2000 images. It includes a Flask web application that allows users to view different image formats. This was our final project for ECE418-"Image Processing" at the University of Illinois.

The final report can be found [here](./JPEG_Comparison_Final_Report.pdf).

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
cd my-projects/JPEG_Comparison
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


## Skills and Technologies Used

- **Tools**: WebPageTest.org for performance testing.
- **Skills**: Image processing and analysis with standardized testing.
- **Frameworks**: Evaluation hosted on a dedicated website for controlled experiments.

## Methodology

The analysis used a controlled environment for consistent and repeatable results:
- **Test Platform**: [WebPageTest.org](https://www.webpagetest.org).
- **Image Formats Tested**: Baseline JPEG, Progressive JPEG, Hierarchical JPEG, and their JPEG2000 counterparts.
- **Metrics Collected**:
  - Load Time
  - Start Render
  - Speed Index
  - Visual Progress
  - Cumulative Layout Shift (CLS)

Performance tests were conducted under typical web browsing conditions:
- Connection type: Cable (5 Mbps download, 1 Mbps upload).
- Browser: Safari on a Mac Mini.
- Location: New York City.

## Results Summary

- **Best Performer**: Baseline JPEG emerged as the most efficient format for quick page rendering.
- **Worst Performer**: Progressive JPEG2000 showed slower load times despite its advanced compression capabilities.
- **Insights**:
  - Progressive JPEG improves user experience by showing low-quality images quickly.
  - JPEG2000 provides high-quality compression but may not be suited for real-time web applications due to higher processing overhead.

