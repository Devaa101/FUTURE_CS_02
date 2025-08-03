import pandas as pd

def classify():
    df = pd.read_csv('suspicious.csv')
    df['incident_type'] = df['activity'].apply(lambda x: 'Credential Abuse' if x == 'admin_login' else 'Data Leak')
    df.to_csv('classified_incidents.csv', index=False)
    print("Incidents classified and saved.")

if __name__ == "__main__":
    classify()
