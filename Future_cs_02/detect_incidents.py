import pandas as pd

def detect_suspicious():
    df = pd.read_csv('alerts.csv')
    suspicious = df[df['activity'].isin(['data_exfiltration', 'admin_login'])]
    suspicious.to_csv('suspicious.csv', index=False)
    print("Suspicious activities written to suspicious.csv")

if __name__ == "__main__":
    detect_suspicious()
