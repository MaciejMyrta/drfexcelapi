from rest_framework import serializers
import pandas as pd
from .models import ExcelFile


class ExcelFileCreateSerializer(serializers.ModelSerializer):
    '''ExcelFile creation serializer is dedicated to 'create' action for the instance of ExcelFile model.
        Class Meta restricts the response output only to FileField and summary field, which is created by
        the serializer specifically for the project's task purpose.'''

    summary = serializers.SerializerMethodField()

    class Meta:
        model = ExcelFile
        fields = ('file', 'columns', 'summary')

        extra_kwargs = {
            'columns': {'write_only': True}
        }

    def validate(self, data):
        '''Object level validation which supports the validators of FileField inside the model which is
            the content of this serializer. Model validators disallow other extension than '.xlsx' but it's obvious
            that it's only naming convention restriction. This validator tries to open the file in Pandas functionality
            with use of Openpyxl engine. If this not succeed, the file is not sufficient to scrape the data about columns
            which the user tries to find in the purpose of this project.'''

        try:
            df = pd.read_excel(data['file'], engine='openpyxl')
        except:
            error = 'The file processing did not succeed. Please check your file and try once again.'
            raise serializers.ValidationError(error)
        return data

    def get_summary(self, object) -> list:
        '''The ExcelFile creation serializer proceed with the task of analysis for input data, which the function
            tries to find inside the file's header row. With use of Pandas functionality, the script retrieves the
            string values to be find inside the sheet's header row and standarizes the dataframe column names by
            making it lower string and stripping it from spaces at both ends.

            For the purpose of this project, we assume that script searches for the column names in first row of
            dataframe which is supposed to be header. If the function matches the input with any column, it processes
            to get rid of non-numeric values, collects the list of correct ones and calculates sum and average of it.

            The result of this function is a list of dictionaries with names, sums and averages of found columns.
            If the column does not contain sufficient data, there is error handling message provided as a string.
            The same if no string value from the input matches any column name in the header row.'''

        path = object.file.path
        df = pd.read_excel(path, engine='openpyxl')
        summary_columns = [x for x in df.columns if str(x).strip().lower() in
                           [x.strip() for x in object.columns.lower().split(', ')]]

        if summary_columns:

            summary_result = []

            for col in summary_columns:

                df[col] = df[col].fillna('')
                calc = [x for x in df[col].to_list() if isinstance(x, int) or isinstance(x, float)]

                if calc:
                    col_sum = round(sum(calc), 2)
                    col_avg = round(sum(calc) / len(calc), 2)

                else:
                    col_sum = col_avg = 'No sufficient data'

                summary_result.append({"column": col, "sum": col_sum, "avg": col_avg})

        else:
            summary_result = 'None of provided columns found in the header row. ' \
                             'Please check if the input corresponds to the header row of your file and try once again.'

        return summary_result


class ExcelFileDetailedSerializer(ExcelFileCreateSerializer):
    '''This serializer inherits from ExcelFile creation serializer in purpose to provide different output inside the
        response of 'list', 'retrieve' and 'destroy' actions. The response is more detailed, especially with 'id'
        primary key of each particular instance which is an address to specific instance url, where the logged in user
        with admin rights can delete instance as well.'''

    class Meta:
        model = ExcelFile
        fields = ('id', 'file', 'summary', 'columns')