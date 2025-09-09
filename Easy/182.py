import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_counts = person.groupby('email').size().reset_index(name='count')
    duplicated_emails = email_counts[email_counts['count'] > 1]
    return pd.DataFrame({'Email': duplicated_emails['email']})