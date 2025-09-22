import pandas as pd
import os

# Create "Data" folder if it doesn't exist
os.makedirs("Data", exist_ok=True)

# Data for 10 people
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "cell" : [1234567890, 2345678901, 3456789012, 4567890123, 5678901234, 6789012345, 7890123456, 8901234567, 9012345678, 1123456789],
    "Name": [
        "Ali Khan", "Sara Ahmed", "Bilal Hussain", "Ayesha Malik", "Hamza Ali",
        "Fatima Noor", "Usman Tariq", "Zainab Iqbal", "Ahmad Raza", "Hira Sheikh"
    ],
    "Age": [25, 22, 28, 30, 27, 24, 29, 26, 31, 23],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "City": [
        "Lahore", "Karachi", "Islamabad", "Faisalabad", "Rawalpindi",
        "Multan", "Peshawar", "Quetta", "Sialkot", "Hyderabad"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save inside "Data" folder
df.to_csv("Data/people.csv", index=False, encoding="utf-8")

print("✅ people.csv saved inside 'Data' folder successfully!")
