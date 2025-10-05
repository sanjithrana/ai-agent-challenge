```python
import fitz
import pandas as pd
import os

def parse(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file {pdf_path} does not exist")

    # Open the PDF file using PyMuPDF (fitz)
    doc = fitz.open(pdf_path)
    
    # Initialize lists to collect extracted data
    date_list = []
    details_list = []
    debit_amount_list = []
    credit_amount_list = []
    
    # Iterate over pages to extract data
    for page in doc:
        # Perform text extraction using PyMuPDF
        text = page.get_text()
        
        # Split extracted text into lines
        lines = text.split('\n')
        
        # Identify transaction lines (assuming format 'Date | Details | Debit Amount | Credit Amount')
        for line in lines:
            if line:
                split_line = line.split(' | ')
                if len(split_line) >= 4:  # Check if line has at least 4 values
                    date, details, debit_amount, credit_amount = split_line[:4]
                    
                    # Append extracted data to lists
                    date_list.append(date)
                    details_list.append(details)
                    debit_amount_list.append(debit_amount)
                    credit_amount_list.append(credit_amount)

    # Close the PDF document to free up resources
    doc.close()
    
    # Define the schema for the DataFrame
    schema = {
        'Date': date_list,
        'Details': details_list,
        'Debit Amount': debit_amount_list,
        'Credit Amount': credit_amount_list
    }
    
    # Create a pandas DataFrame from the extracted data
    df = pd.DataFrame(schema)
    
    # Return the DataFrame
    return df
```