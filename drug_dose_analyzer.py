import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print("."*30)
print("DRUG DOSE ANALYZER")
print("."*30)

patients=[
    {"Name":"Hadiya","Age":"21y","Weight":64},
    {"Name":"Amna","Age":"24y","Weight":72},
    {"Name":"Rehman","Age":"30y","Weight":68},
    {"Name":"Nabeel","Age":"27y","Weight":64},
    {"Name":"Maaz","Age":"18y","Weight":59},

 ]

print("\n","."*10,"PATIENT DATA","."*10)

for patient in patients:
    print(
        f"Name: {patient['Name'] } | ",
        f"Age: {patient['Age']  } | ",
        f"Weight:{patient['Weight']}","kg"
    )


print("\n","."*10,"DRUG INFORMATION","."*10)

Drug_name="Paracetamol"
Drug_per_kg=10

print("Drug:", Drug_name)
print("Effected person can take dose according to his weight:")
print( "---->"," Drug Per Kg:",Drug_per_kg,"mg")


print("\n","."*10,"DOSE CALCULATION","."*10)

for patient in patients:
    
    weight=patient["Weight"]
    dose=weight*Drug_per_kg
    patient["Dose"]=dose

    print(
        patient["Name"],
        "----->",
        dose,
        "mg"
    )


print("\n","."*10,"PATIENTS DOSE DETAILS","."*10)

print(f"{'Name':<10} {'dose(mg)':<10} {'Weight(kg)':<10}")

for patient in patients:

    print(
        f"{patient['Name']: <10}"
        f"{patient['Dose']: <10} "
        f"{patient['Weight']: <10}"
    )


print("\n","."*10,"DOSE ANALYSIS","."*10)

for patient in patients:

    dose=patient["Dose"]

    if dose <600:
        category ="low"

    elif dose <700:
        category ="normal"

    else:
        category="high"

    patient["Category"] = category

    print(
        f"{patient['Name']:<10}"
        f"{dose:<10}"
        f"{category}"
    )


print("\n","."*10,"CREATE PATIENT SHEET USING DATAFRAME IN PANDAS","."*10)

df=pd.DataFrame({
    "Names":["Hadiya","Amna","Rehman","Nabeel","Maaz"],
    "Age":["21y","24y","30y","27y","18y"],
    "Weight":[64,72,68,64,59],
    "Dose":[640,720,680,640,590],
})

print(df)


# ==========================================
# VISUALIZATION 1 - BAR CHART
# ==========================================

plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x="Names",
    y="Dose"
)

plt.title("Drug Dose for Each Patient")
plt.xlabel("Patient Name")
plt.ylabel("Dose (mg)")

plt.tight_layout()
plt.show()


# ==========================================
# VISUALIZATION 2 - PIE CHART
# ==========================================

category_counts = pd.Series(
    [patient["Category"] for patient in patients]
).value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    category_counts.values,
    labels=category_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Dose Category Distribution")

plt.tight_layout()
plt.show()


# ==========================================
# VISUALIZATION 3 - SCATTER PLOT
# ==========================================

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="Weight",
    y="Dose",
    s=100
)

plt.title("Weight vs Drug Dose")
plt.xlabel("Weight (kg)")
plt.ylabel("Dose (mg)")

plt.tight_layout()
plt.show()


# ==========================================
# PROJECT COMPLETED
# ==========================================

print("\n","."*10,"PROJECT COMPLETED","."*10)
