# 🏥 Hospital Management Analytics

An interactive **Hospital Management Analytics Dashboard** built with **Python, Pandas, NumPy, Plotly, and Streamlit**.

The project analyzes hospital data related to **patients, doctors, appointments, treatments, billing, and payments** and presents the results through interactive charts, tables, analytics, and data-structure demonstrations.

## 🚀 Live Demo

👉 **[Open Hospital Management Analytics Dashboard](https://hospital-management-analytics-pltifwya3dxztyhsxz9jgt.streamlit.app/)**

---

## 📌 Project Overview

Hospital Management Analytics is a data analytics project designed to transform hospital records into meaningful visual insights.

The dashboard combines multiple hospital datasets and provides an interactive interface where users can explore:

- Patient demographics
- Doctor workload and specialization
- Appointment status and visit reasons
- Treatment types and treatment costs
- Billing and payment information
- Monthly appointment and revenue trends
- Relationships between hospital entities
- DSA concepts applied to hospital data
- Automatically generated analytical insights
- Dataset structure and data quality information

The project is designed as a **B.Tech Data Science project** demonstrating practical applications of data preprocessing, exploratory data analysis, visualization, and basic DSA concepts.

---

## ✨ Key Features

### 🏠 1. Hospital Overview

Provides a quick summary of the hospital dataset with key metrics such as:

- Total records
- Total patients
- Total doctors
- Total appointments
- Total billing amount
- Appointment status distribution
- Payment status distribution

---

### 👥 2. Patient Analysis

Analyzes patient-related information including:

- Gender distribution
- Patient age groups
- Patient records
- Date of birth
- Registration date
- Contact information

Interactive charts make it easier to understand the demographic structure of the dataset.

---

### 👨‍⚕️ 3. Doctor Analysis

Provides insights into doctor activity and workload:

- Appointments by doctor
- Appointments by specialization
- Doctor ID
- Doctor name
- Department
- Years of experience

A doctor summary table is also provided for detailed inspection.

---

### 📅 4. Appointment Analysis

Analyzes hospital appointments using:

- Appointment status
- Reasons for visits
- Appointment dates
- Appointment times
- Assigned doctors
- Patient IDs

The dashboard provides interactive visualizations and detailed appointment records.

---

### 💊 5. Treatment Analysis

Analyzes treatment information including:

- Treatment types
- Treatment frequency
- Treatment costs
- Treatment descriptions
- Treatment dates
- Average treatment cost patterns

This section helps identify common treatments and their associated costs.

---

### 💰 6. Billing & Payments

Provides financial analytics such as:

- Total billing amount
- Average bill amount
- Paid amount
- Pending amount
- Payment methods
- Payment status
- Billing records

Interactive charts show how payments are distributed across different methods and statuses.

---

### 📈 7. Monthly Trends

Visualizes changes over time using:

- Monthly appointment trends
- Monthly revenue trends

Line charts make it easier to identify changes in hospital activity and billing over the available dataset period.

---

### 🔗 8. Hospital Relationship Analysis

Demonstrates relationships between the major hospital entities:

```text
Patient
   │
   └── Appointment
          │
          ├── Doctor
          │
          └── Treatment
                  │
                  └── Billing
```

The project demonstrates relationships using IDs such as:

- `patient_id`
- `doctor_id`
- `appointment_id`
- `treatment_id`

Additional analysis includes:

- Average treatment cost by visit reason
- Patient age vs. treatment cost

---

### 🧠 9. DSA Concepts

This section demonstrates how basic **Data Structures and Algorithms concepts** can be applied to real-world hospital data.

Implemented concepts include:

#### Dictionary / Hash Map
Doctor IDs are mapped to doctor names for quick lookup.

#### Searching
Users can search patient records by patient name.

#### Sorting
Records can be sorted based on:

- Age
- Treatment cost
- Billing amount

#### Top-K Analysis
Users can select `K` to find doctors with the highest number of appointments.

#### Frequency Counting
The frequency of different reasons for hospital visits is calculated.

#### Filtering
Hospital records can be filtered according to appointment status.

---

### 💡 10. Automated Insights

The dashboard automatically identifies important patterns from the dataset, including:

- Most common appointment status
- Most common reason for visiting
- Most frequently recorded treatment
- Doctor with the highest number of appointments
- Most frequently used payment method
- Correlation between numerical variables

A correlation heatmap is also generated for available numerical features such as:

- Age
- Treatment cost
- Billing amount

---

### 📊 11. Dataset Information

Provides information about the processed dataset:

- Number of rows
- Number of columns
- Missing values
- Data types
- Unique values
- Dataset preview

The application also performs date conversion and feature engineering before displaying the analytics.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Interactive web dashboard |
| **Pandas** | Data loading, cleaning and analysis |
| **NumPy** | Numerical operations |
| **Plotly** | Interactive data visualization |
| **CSV** | Dataset storage |
| **Git & GitHub** | Version control and project hosting |
| **Streamlit Cloud** | Application deployment |

---

## 📂 Project Structure

```text
hospital-management-analytics/
│
├── app.py
│
├── hospital_management_cleaned.csv
│
├── patients.csv
├── doctors.csv
├── appointments.csv
├── treatments.csv
├── billing.csv
│
├── requirements.txt
│
└── README.md
```

### File Description

| File | Description |
|---|---|
| `app.py` | Main Streamlit application |
| `hospital_management_cleaned.csv` | Cleaned and processed dataset used by the dashboard |
| `patients.csv` | Patient-related data |
| `doctors.csv` | Doctor-related data |
| `appointments.csv` | Appointment records |
| `treatments.csv` | Treatment records |
| `billing.csv` | Billing and payment records |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## 🔄 Data Processing Workflow

The project follows a basic data analytics workflow:

```text
Raw Hospital Data
       ↓
Data Cleaning
       ↓
Data Preprocessing
       ↓
Date Conversion
       ↓
Feature Engineering
       ↓
Exploratory Data Analysis
       ↓
Data Visualization
       ↓
DSA-Based Analysis
       ↓
Insights
       ↓
Interactive Streamlit Dashboard
```

### Feature Engineering

The application derives additional fields such as:

- Patient name
- Doctor name
- Patient age
- Appointment month
- Appointment month name
- Billing month
- Billing month name
- Treatment month name

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the project folder

```bash
cd hospital-management-analytics
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser, normally at:

```text
http://localhost:8501
```

---

## 📦 Requirements

The project uses the following Python packages:

```text
streamlit
pandas
numpy
plotly
```

These dependencies are listed in `requirements.txt`.

---

## ☁️ Deployment

The project is deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the project to GitHub.
2. Make sure `app.py` is present in the repository.
3. Add `requirements.txt`.
4. Connect the GitHub repository to Streamlit.
5. Select `app.py` as the main application file.
6. Deploy the application.

### Live Application

**[Hospital Management Analytics](https://hospital-management-analytics-pltifwya3dxztyhsxz9jgt.streamlit.app/)**

---

## 📊 Analytics Covered

The project covers the following major data analytics areas:

- Descriptive analytics
- Exploratory data analysis
- Categorical data analysis
- Numerical data analysis
- Frequency analysis
- Aggregation
- Filtering
- Sorting
- Top-K analysis
- Correlation analysis
- Time-series trend analysis
- Interactive visualization

---

## 🎯 Project Objectives

The main objectives of this project are:

1. To analyze hospital management data using Python.
2. To clean and preprocess real-world style healthcare records.
3. To identify meaningful patterns from hospital data.
4. To visualize hospital operations using interactive charts.
5. To analyze patients, doctors, appointments, treatments, and billing.
6. To demonstrate DSA concepts using a practical dataset.
7. To build an interactive analytics dashboard using Streamlit.
8. To deploy the completed project as a web application.

---

## 🔍 Example Questions the Dashboard Can Answer

The dashboard can help answer questions such as:

- How many patients are present in the dataset?
- How many doctors are available?
- What is the most common appointment status?
- What are the most common reasons for hospital visits?
- Which doctors have the highest number of appointments?
- Which treatment types are most frequently recorded?
- Which treatments have higher costs?
- How much billing revenue is recorded?
- How much billing is paid or pending?
- Which payment method is used most frequently?
- How do appointments change month by month?
- How does revenue change over time?
- Is there a relationship between patient age and treatment cost?
- How can searching, sorting, filtering, and Top-K analysis be applied to hospital data?

---

## 🧪 DSA Concepts Demonstrated

The project connects data analytics with fundamental DSA concepts:

```text
Dictionary / Hash Map → Doctor Lookup
Searching             → Patient Search
Sorting               → Data Ordering
Top-K                 → Top Doctors
Frequency Counting    → Visit Reasons
Filtering             → Appointment Status
```

This makes the project useful not only as a visualization dashboard but also as a demonstration of applying programming and DSA concepts to a practical dataset.

---

## 🔐 Data Privacy Note

This project is intended for **educational and demonstration purposes**.

The included datasets should contain synthetic, sample, or non-sensitive data. Real patient information, personally identifiable information, or confidential medical records should not be uploaded to a public GitHub repository or public Streamlit application.

---

## 🚀 Future Enhancements

Possible improvements for future versions include:

- User authentication and role-based access
- Advanced sidebar filters
- Date-range filtering
- Doctor-specific dashboards
- Patient search with detailed profiles
- Export analytics to CSV/PDF
- More advanced KPI cards
- Predictive analytics
- Hospital resource forecasting
- Appointment cancellation prediction
- Revenue forecasting
- Database integration using MySQL/PostgreSQL
- Admin dashboard
- Real-time hospital data integration

---

## 👨‍💻 Project

**Hospital Management Analytics**

Built as a **B.Tech Data Science project** using Python and Streamlit.

### Built With

**Python • Pandas • NumPy • Plotly • Streamlit • GitHub**

---

## ⭐ If You Like This Project

If this project helped you or you found it useful, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is intended for educational purposes. You may modify and extend it for learning and academic projects.
