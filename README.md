
# CSVanalyzer

CSVanalyzer is a Django-based web application that allows users to upload CSV files for detailed analysis. This tool provides summary statistics, handles missing values, and generates visualizations, making it ideal for data analysis tasks. The application is designed to be user-friendly and provides immediate insights into the structure and content of uploaded datasets.
## Technologies Used
#### Django: 
- A high-level Python web framework that encourages rapid development and clean, pragmatic design.
#### Pandas:
 - A powerful Python library for data manipulation and analysis.
#### Matplotlib & Seaborn: 
- Python libraries for creating static, animated, and interactive visualizations.
#### HTML/CSS: 
- For the structure and styling of web pages.

## Installation and Setup
#### Prerequisites
- Python 3.x installed on your system
- Git installed on your system
#### 1. Clone the Repository:

Open your terminal and run the following command to clone the repository:\
- git clone https://github.com/yourusername/CSVanalyzer.git 
- cd CSVanalyzer 
#### 2. Create and Activate a Virtual Environment:

It's recommended to use a virtual environment to manage dependencies.Run the following commands in your terminal:

- python3 -m venv venv 
- venv\Scripts\activate 
#### 3. Install the required Python packages using pip:

- pip install -r requirements.txt 
#### 4. Apply Migrations:

Set up your database by applying migrations:

- python manage.py migrate

#### 5. Run the Development Server:

Start the Django development server:

- python manage.py runserver 

#### 6. Access the Application:

Open your web browser and navigate to http://127.0.0.1:8000/ to start using the application.



## Features

#### CSV File Upload:

- Users can upload CSV files through an intuitive web interface.

#### Data Preview: 
- Displays the first five rows of the dataset to give an overview of its structure.

#### Summary Statistics:
- Automatically calculates mean, median, and standard deviation for numerical columns.

#### Missing Values Handling:
- Identifies and highlights missing values within the dataset.

#### Data Visualization:
- Generates histograms for numerical columns to visualize data distributions.

#### Displays box plots to show the spread and outliers in the data.
- Pairwise scatter plots to explore relationships between numerical variables.

#### User-Friendly Interface:
- The web interface is designed with simplicity and usability in mind, allowing users to perform complex analysis with minimal effort.
##  Usage

#### Upload CSV File:
• Navigate to the home page and upload your CSV file.
#### View Data Preview:
• The first five rows of your dataset are displayed for a quick overview.
#### Perform Data Analysis:
• View summary statistics, identify missing values, and generate   visualizations to understand your data better.

## Project Structure

Here's an overview of the key directories and files in the project:

 #### CSVanalyzer/:
The main project directory.

#### dataapp/: 
Contains the Django app where all data processing and analysis logic is implemented.

- views.py: Contains the logic for handling user requests and rendering templates.

- models.py: Defines any database models (not used in this project).
- forms.py: Handles forms for uploading CSV files.

- templates/dataapp/: Contains HTML templates for rendering web pages.

- static/dataapp/: Contains static files like CSS and JavaScript for the app.

#### requirements.txt: 
Lists all the dependencies required to run the project.

#### manage.py: 
A command-line utility that lets you interact with this Django project.
## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute code, feel free to fork the repository and submit a pull request.

####  How to Contribute
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes.
- Push to your branch.
- Submit a pull request.


## License
This project is licensed under the MIT License. See the LICENSE file for more details.
[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

 - Thanks to the Django and Python communities for their extensive documentation and support.
 - Special recognition to the creators of Pandas, Matplotlib, and Seaborn for their powerful data analysis and visualization libraries.
 

