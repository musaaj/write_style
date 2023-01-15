#!/usr/bin/python3
"""Change writing style of a text using openai"""
from docx import Document
import openai
import os
import sys


def main():
    """main entry"""
    for arg in sys.argv[1:]:
        try:
            edit(arg)
        except Exception:
            print('error reading file {}'.format(arg))


def edit(filename):
    """edit file and save it in a seperate folder"""
    edited = change_style(filename)
    with open('edited/_edit_' + filename, 'w') as fp:
        write(edited)


def change_style(filename=''):
    """change writing style of a text

    Args:
        filename: string, must be name of an existing docx file
    
    Return: string, text of @filename rewritten
    """
    if not isinstance(filename, str):
        raise TypeError('filename must be astring')
    doc = Document(filename)
    result = ''
    for para in doc.paragraphs:
        content = para.text
        results = openai.Completion.create(
                model="text-davinci-002",
                prompt="in a suspensful and mysterious style rewrite text below\n"
                + content +"",
                temperature=0,
                max_tokens=2355,
                top_p=1,
                frequency_penalty=0.2,
                presence_penalty=0
            )
        response = dict(results)
        openai_response = response['choices']
        result += (openai_response)
    return result

if __name__ == '__main__':
    main()
