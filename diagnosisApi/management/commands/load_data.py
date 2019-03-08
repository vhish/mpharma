from django.core.management.base import BaseCommand, CommandError
from diagnosisApi.models import Category, Diagnosis
import os.path
import csv
from django.core.management.color import no_style
from django.db import connection

class Command(BaseCommand) :
    help= 'This command load test data'


    def handle(self, *args, **options):

        sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Category, Diagnosis])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)

        Category.objects.all().delete()
        Diagnosis.objects.all().delete()
        current = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(current, "../../data/categories.csv")
        with open( path , 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            i  = 1
            for row in csv_reader:
                obj, created = Category.objects.get_or_create(category_code=row[0] ,
                defaults = {'category_title': row[1] } )
                i += 1

        print("Total Number of test data pushed in Category database --> " ,  i )
        path = os.path.join(current, "../../data/codes.csv")

        with open( path , 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            c  = 0
            for row in csv_reader:
                c += 1
                try:

                    cat  =  Category.objects.get(category_code=row[0])

                except Category.DoesNotExist :
                    cat  =  None

                if cat :
                    obj, created = Diagnosis.objects.get_or_create( category=cat ,
                    defaults = {'diagnosis_code': row[1] , 'abbreviated_description' : row[3]  ,  'full_description' : row[4]   })
                    #print("Diagnosis_code : " ,  row[1] , " Abbreviated_description: " , row[3] , "Full_description: " , row[4],
                    #"Category: " , cat.category_code )
        print("Total Number of test data pushed in Diagnosis database --> ",  c )
