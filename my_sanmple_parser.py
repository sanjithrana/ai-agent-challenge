Here's the complete, runnable Python code:

```python
import fitz  # PyMuPDF
import pandas as pd

def parse(pdf_path):
    """
    Extracts relevant data from an ICICI Bank PDF statement.

    Args:
        pdf_path (str): Path to the ICICI Bank PDF statement.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the extracted data.
    """
    data = []
    doc = fitz.open(pdf_path)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        lines = text.split('\n')
        lines = [line.strip() for line in lines]
        
        account_number = None
        account_name = None
        transaction_date = None
        transaction_amount = None
        
        for line in lines:
            if 'Account Number:' in line:
                account_number = line.split(':')[-1].strip()
            elif 'Account Name:' in line:
                account_name = line.split(':')[-1].strip()
            elif 'Date:' in line:
                transaction_date = line.split(':')[-1].strip()
            elif 'Amount:' in line:
                transaction_amount = line.split(':')[-1].strip()
        
        if account_number and account_name and transaction_date and transaction_amount:
            data.append({
                'Account Number': account_number,
                'Account Name': account_name,
                'Transaction Date': transaction_date,
                'Transaction Amount': transaction_amount
            })
    
    doc.close()
    df = pd.DataFrame(data)
    return df

# Example usage
pdf_path = 'path/to/icici_bank_statement.pdf'
df = parse(pdf_path)
print(df)
```

To use this code, replace `'path/to/icici_bank_statement.pdf'` with the actual path to your ICICI Bank PDF statement. The function will extract the relevant data from the PDF and return a pandas DataFrame containing the extracted data.

Note that this code assumes that the PDF statement has a specific layout, with the account number, account name, transaction date, and transaction amount appearing on separate lines with specific labels. If your PDF statement has a different layout, you may need to modify the code to extract the relevant data correctly.