import pandas as pd
from datetime import datetime
import random

def generate_alerts():
    alerts = []
    users = ['alice', 'bob', 'charlie']
    activities = ['login_failure', 'data_exfiltration', 'usb_inserted', 'admin_login']

    for _ in range(10):
        alert = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'user': random.choice(users),
            'activity': random.choice(activities),
            'severity': random.choice(['Low', 'Medium', 'High'])
        }
        alerts.append(alert)

    df = pd.DataFrame(alerts)
    df.to_csv('alerts.csv', index=False)
    print("Simulated alerts written to alerts.csv")

if __name__ == "__main__":
    generate_alerts()
