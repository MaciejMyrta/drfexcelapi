# drfexcelapi project introduction
Exercise project about the topic of uploading and managing the Excel files inside DRF API, developed in Python 3.8.

### How to run the project:

1. Clone this repository via command: git clone https://github.com/MaciejMyrta/drfexcelapi.git

2. Set up all the packages (if needed) from requirements.txt file.

3. Open the app with use of 'python manage.py runserver' command and then navigate with use of urls mentioned in section 'Endpoints prepared...', written below.

-------------------------------------------------------

### Context ideas:

1. API allows to upload the Excel file with the manual input of the columns, which the user wants to get data about: 'sum' and 'average.

2. Input is being recognised as a string being splitted by commas. The input 'column 1, column 2, column 3' is the correct way to get the sum and average of columns: 'column 1', 'column 2', 'column 3'. The input is not upper/lowercase vulnerable, as it is standarized in the background, same as the column headers inside the Excel file.

3. Correctness of Excel file - it should be the Excel file with '.xlsx' extension, with size less than 100 mb, as the extension and size are restricted by the validators.

4. Please check if the column header is placed in the top row - only the typical first header row is being parsed in case of column header names. Sheets with non-typical placing of the table will not be parsed correctly.

-------------------------------------------------------

### Endpoints prepared for the purpose of this project:

http://127.0.0.1:8000/api/files/create - Create the instance of ExcelFile model with choosing the Excel '.xlsx' file and columns which the user wants to retrieve data about.

http://127.0.0.1:8000/api/files - List the data about all ExcelFile objects being created yet.

http://127.0.0.1:8000/api/files/:id/ - Retrieve the data about one particular instance from API with possibility to delete it, once being logged as an admin.

-------------------------------------------------------

http://127.0.0.1:8000/admin - Admin panel, once being logged in, the user is able to delete the created instances ExcelFile model, both in admin panel and in API endpoint presented above.

Admin credentials:
login: admin
password: password
