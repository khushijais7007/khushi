import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("hospital_data.csv")

# First 5 Rows
print("\nFIRST 5 ROWS\n")
print(df.head())

# Dataset Info
print("\nDATASET INFO\n")
print(df.info())

# Statistical Summary
print("\nSTATISTICAL SUMMARY\n")
print(df.describe())

# Missing Values
print("\nMISSING VALUES\n")
print(df.isnull().sum())

# Disease Count
print("\nDISEASE COUNT\n")
print(df["Disease"].value_counts())

# Gender Distribution
print("\nGENDER DISTRIBUTION\n")
print(df["Gender"].value_counts())

# Average Fees
print("\nAVERAGE FEES\n")
print(df["Fees"].mean())

# Highest Fees
print("\nHIGHEST FEES\n")
print(df["Fees"].max())

# Graph 1
df["Disease"].value_counts().plot(kind="bar")

plt.title("Disease Count")
plt.xlabel("Disease")
plt.ylabel("Patients")

plt.show()

# Graph 2
df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")
plt.ylabel("")

plt.show()
