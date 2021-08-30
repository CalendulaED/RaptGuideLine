import json
import re

from rapt.rapt import Rapt

def change_to_sql():

    #Q1
    str = "\project_{BranName}(\s_{State='Indiana' } (LibraryBranch) );"


    with open('config.json') as config_file:
        config = json.load(config_file)
    r = Rapt(**config)
    f = open('schema.json')
    schema = json.load(f)

    return r.to_sql(str, schema)


if __name__ == '__main__':
    sql_list = change_to_sql()

    print('SQL: Queries')

    for q in sql_list:
        print(q)

    print()