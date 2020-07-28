import csv


DUMP_PATH = r'C:\Users\15314\source\repos\LAFG\LAFG\lafg_site\data_tools\data_dump'


def export_db(django_model, response):
    """Export the entire django model table to a csv file saved in the data dump folder"""

    all_data = convert_django_model_to_lists(django_model)

    # File name is just the same name as the model. So Book model will be 'Book.csv' 
    write_to_response(all_data, response)


def convert_django_model_to_lists(django_model):
    """Takes a django model and returns a list of lists with each inner list containing one row of data associated with the database
    included the column names as the first row."""

    model_fields = [field.name for field in django_model._meta.fields]
    model_data = django_model.objects.all()

    all_data = []
    all_data.append(model_fields) # Column headers

    for row in model_data:
        this_row_data = []
        for field in model_fields:
            field_value = getattr(row, field)
            this_row_data.append(field_value)
        all_data.append(this_row_data)

    return all_data


def write_to_response(data, response):
    """Takes an interable of iterables like a list of lists and writes it to the response object as a csv?"""

    writer = csv.writer(response)
    writer.writerows(data)

 


