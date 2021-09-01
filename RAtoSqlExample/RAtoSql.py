import json
import re

# import mysql.connector

from rapt.rapt import Rapt
from pyparsing import *

import sqlite3


def preprocess(raw):
    i = 0
    j = 0
    result = ""
    firstFind = False
    for j in range(len(raw)):
        if (i < len(raw) and raw[i] == '(' and not firstFind):
            while(raw[i+1] != ')' and i < len(raw)):
                # print("inside")
                i += 1
                # print(raw[i])
                # print(i)
            i += 2
            firstFind = True
        else:
            # print(raw[i])
            if (i < len(raw)):
                result += raw[i]
                i += 1


    # print(result)
    return result

def removeExAs(raw):
    sub = "AS"
    res = [i for i in range(len(raw)) if raw.startswith(sub, i)]

    if len(res) > 1:
        res.pop(0)
        # print(res)

        changeAmount = 0

        for index in res:
            for i in range(3):
                if len(raw) > index:
                    raw = raw[0: index - changeAmount:] + raw[index - changeAmount + 1::]
            changeAmount += 3

        # print(raw)
        return raw
    else:
        return raw


def change_to_sql():

    #Q1
    # str = "\project_{BranName}(\s_{State='Indiana' } (LibraryBranch) );"

    #Q2
    str = """LibrBran \leftarrow \s_{State='Indiana' } (LibraryBranch);
        LibrBookCopi \leftarrow  LibrBran \\theta_join_{LibrBran.BranId =BookCopies.BranId } BookCopies;
        LibrBook \leftarrow  LibrBookCopi \\theta_join_{LibrBookCopi.BookId =Book.BookId } Book;
        Result \leftarrow \project_{Title} (LibrBook);
"""

    #Q3
    # str = """
    # WithLoans \leftarrow \project_{MembId} (BookLoans);
    # AllMemb \leftarrow \project_{MembId} (Member);
    # NoLoans \leftarrow AllMemb - WithLoans;
    # Result \leftarrow \project_{MembName} (NoLoans \j Member);"""


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

