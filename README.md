# 💊 Drug Dose Analyzer

A Python-based **Drug Dose Analyzer** project that calculates and analyzes sample drug doses for multiple patients based on their body weight.

> ⚠️ **Disclaimer:** This project is created for educational and programming demonstration purposes only. It is not intended for real clinical or medical dosing decisions.

---

## 📌 Project Overview

The **Drug Dose Analyzer** stores and analyzes patient information such as:

* 👤 Name
* 🎂 Age
* ⚖️ Weight

The program calculates a sample dose based on the patient's weight and a predefined dose-per-kilogram value.

It also categorizes the calculated doses into:

* 🟢 Low
* 🟡 Normal
* 🔴 High

The patient data is organized using a **Pandas DataFrame** and visualized using different graphs.

---

## 📸 Code and Visualization Preview

![Drug Dose Analyzer](images/drug_dose_analyzer.png)

This project includes:

* 📊 Drug Dose Bar Chart
* 🥧 Dose Category Pie Chart
* 📈 Weight vs Drug Dose Scatter Plot

---

## ✨ Features

* Store multiple patient records
* Display patient information
* Calculate sample dose according to patient weight
* Perform dose analysis
* Categorize doses as Low, Normal, or High
* Create a Pandas DataFrame
* Generate a Bar Chart
* Generate a Pie Chart
* Generate a Scatter Plot
* Analyze the relationship between weight and calculated dose

---

## 🧮 Dose Calculation Formula

The program uses the following formula:

```text
Dose = Weight × Drug Dose Per KG
```

### Example

```text
Patient Weight = 64 kg
Drug Dose Per KG = 10 mg/kg

Calculated Dose = 64 × 10
Calculated Dose = 640 mg
```

---

## 📊 Visualizations

### 1️⃣ Drug Dose Bar Chart

Displays the calculated dose for each patient.

### 2️⃣ Dose Category Pie Chart

Shows the distribution of patients according to dose categories:

* Low
* Normal
* High

### 3️⃣ Weight vs Drug Dose Scatter Plot

Shows the relationship between patient weight and the calculated drug dose.

---

## 🛠️ Technologies Used

This project uses the following technologies and libraries:

* 🐍 Python
* 🐼 Pandas
* 📊 Matplotlib
* 📈 Seaborn

---

## 📂 Project Structure

```text
Drug-Dose-Analyzer/
│
├── drug_dose_analyzer.py
├── requirements.txt
├── README.md
│
└── images/
    └── drug_dose_analyzer.png
```

---

## ⚙️ Installation

First, clone or download the repository.

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the Python program using:

```bash
python drug_dose_analyzer.py
```

The program will:

1. Display patient data
2. Display drug information
3. Calculate the sample dose for each patient
4. Analyze the calculated dose
5. Categorize the calculated results
6. Create a Pandas DataFrame
7. Generate a Bar Chart
8. Generate a Pie Chart
9. Generate a Scatter Plot

---

## 📋 Example Patient Data

| Name   | Age | Weight (kg) |
| ------ | --: | ----------: |
| Hadiya |  21 |          64 |
| Amna   |  24 |          72 |
| Rehman |  30 |          68 |
| Nabeel |  27 |          64 |
| Maaz   |  18 |          59 |

---

## 📊 Dose Analysis Categories

The calculated doses are grouped into the following categories:

| Dose Range       | Category |
| ---------------- | -------- |
| Below 600 mg     | Low      |
| 600–699 mg       | Normal   |
| 700 mg and above | High     |

---

## 📦 Requirements

The project requires the following Python libraries:

```text
pandas
matplotlib
seaborn
```

These libraries are also included in the `requirements.txt` file.

---

## 🎯 Learning Objectives

This project demonstrates practical use of:

* Python Lists
* Dictionaries
* Loops
* Conditional Statements
* Data Handling
* Pandas DataFrames
* Data Analysis
* Data Visualization
* Bar Charts
* Pie Charts
* Scatter Plots

---

## 🚀 Future Improvements

Possible future improvements include:

* Adding user input for patient information
* Supporting multiple sample datasets
* Adding more advanced statistical analysis
* Exporting data to CSV files
* Creating an interactive dashboard
* Adding additional visualizations

---

## 👨‍💻 Author

**Maaz Ahmad**

---

## ⭐ Project Purpose

This project was developed as a **Python Data Analysis and Visualization project** to practice working with structured patient data, calculations, Pandas, conditional logic, and graphical visualization.

If you find this project useful, consider giving the repository a ⭐!
