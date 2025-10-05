import PyPDF2
import pypdf
import pandas as pd
import re

def parse(pdf_path: str) -> pd.DataFrame:
    with open(pdf_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()

    text = re.sub(r'\n+', '\n', text)
    lines = text.split('\n')

    headers = ['Date', 'Description', 'Debit Amt', 'Credit Amt', 'Balance']
    data = []

    for line in lines:
        if line and not line.startswith(('Date', ' ', 'Description', 'Debit Amt', 'Credit Amt', 'Balance')):
            match = re.match(r'(\d{2}-\d{2}-\d{4})\s(.*)\s(\d{0,10}(?:\.\d{1,2})?)\s(\d{0,10}(?:\.\d{1,2})?)\s(\d{0,10}(?:\.\d{1,2})?)', line)
            if match:
                date, description, debit, credit, balance = match.groups()

                if re.match(r'^-?\d+(\.\d+)?$|^\d+(\.\d+)$', debit):
                    try:
                        debit = float(debit)
                    except ValueError:
                        debit = None
                if re.match(r'^-?\d+(\.\d+)?$|^\d+(\.\d+)$', credit):
                    try:
                        credit = float(credit)
                    except ValueError:
                        credit = None
                if re.match(r'^-?\d+(\.\d+)?$|^\d+(\.\d+)$', balance):
                    try:
                        balance = float(balance)
                    except ValueError:
                        balance = None

                data.append([date, description, debit, credit, balance])

    df = pd.DataFrame(data, columns=headers)
    return df