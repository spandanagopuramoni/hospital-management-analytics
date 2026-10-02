import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Hospital Management Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.dashboard-title {
    font-size: 42px;
    font-weight: 800;
    color: #172033;
    margin-bottom: 5px;
}

.dashboard-subtitle {
    color: #667085;
    font-size: 17px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 25px;
    font-weight: 700;
    color: #172033;
    margin-top: 15px;
    margin-bottom: 15px;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #e6eaf0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.small-text {
    color: #667085;
    font-size: 14px;
}

.big-number {
    font-size: 30px;
    font-weight: 750;
    color: #172033;
}

.sidebar-title {
    font-size: 22px;
    font-weight: 800;
}

.insight-box {
    background: white;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #2563eb;
    margin-bottom: 12px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_data():
    data = pd.read_csv("hospital_management_cleaned.csv")

    date_columns = [
        "appointment_date",
        "date_of_birth",
        "treatment_date",
        "bill_date",
        "registration_date"
    ]

    for col in date_columns:
        if col in data.columns:
            data[col] = pd.to_datetime(data[col], errors="coerce")

    if "appointment_time" in data.columns:
        data["appointment_time"] = data["appointment_time"].astype(str)

    return data


df = load_data()


# ============================================================
# BASIC PREPARATION
# ============================================================

if "Patient_Name" not in df.columns:
    if "first_name" in df.columns and "last_name" in df.columns:
        df["Patient_Name"] = (
            df["first_name"].fillna("") + " " +
            df["last_name"].fillna("")
        ).str.strip()

if "Doctor_Name" not in df.columns:
    if "first_name_doctor" in df.columns and "last_name_doctor" in df.columns:
        df["Doctor_Name"] = (
            df["first_name_doctor"].fillna("") + " " +
            df["last_name_doctor"].fillna("")
        ).str.strip()

if "Age" not in df.columns:
    if "appointment_date" in df.columns and "date_of_birth" in df.columns:
        df["Age"] = (
            (df["appointment_date"] - df["date_of_birth"]).dt.days / 365.25
        ).round(0)

if "Appointment_Month_Name" not in df.columns:
    if "appointment_date" in df.columns:
        df["Appointment_Month_Name"] = df["appointment_date"].dt.month_name()

if "Appointment_Month" not in df.columns:
    if "appointment_date" in df.columns:
        df["Appointment_Month"] = df["appointment_date"].dt.month

if "Billing_Month_Name" not in df.columns:
    if "bill_date" in df.columns:
        df["Billing_Month_Name"] = df["bill_date"].dt.month_name()

if "Billing_Month" not in df.columns:
    if "bill_date" in df.columns:
        df["Billing_Month"] = df["bill_date"].dt.month

if "Treatment_Month_Name" not in df.columns:
    if "treatment_date" in df.columns:
        df["Treatment_Month_Name"] = df["treatment_date"].dt.month_name()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🏥 Hospital Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Overview",
            "👥 Patient Analysis",
            "👨‍⚕️ Doctor Analysis",
            "📅 Appointment Analysis",
            "💊 Treatment Analysis",
            "💰 Billing & Payments",
            "📈 Monthly Trends",
            "🔗 Hospital Relationships",
            "🧠 DSA Concepts",
            "💡 Insights",
            "📊 Dataset Information"
        ]
    )

    st.markdown("---")

    st.caption("Hospital Management Analytics")
    st.caption("B.Tech Data Science Project")


# ============================================================
# COMMON TITLE
# ============================================================

st.markdown(
    '<div class="dashboard-title">🏥 Hospital Management Analytics</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Interactive analytics dashboard for patients, doctors, appointments, '
    'treatments and billing records.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PAGE 1 — OVERVIEW
# ============================================================

if page == "🏠 Overview":

    st.markdown('<div class="section-title">Hospital Overview</div>',
                unsafe_allow_html=True)

    total_records = len(df)

    total_patients = (
        df["patient_id"].nunique()
        if "patient_id" in df.columns else 0
    )

    total_doctors = (
        df["doctor_id"].nunique()
        if "doctor_id" in df.columns else 0
    )

    total_appointments = (
        df["appointment_id"].nunique()
        if "appointment_id" in df.columns else 0
    )

    total_revenue = (
        df["amount"].sum()
        if "amount" in df.columns else 0
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("📋 Records", f"{total_records:,}")
    c2.metric("👥 Patients", f"{total_patients:,}")
    c3.metric("👨‍⚕️ Doctors", f"{total_doctors:,}")
    c4.metric("📅 Appointments", f"{total_appointments:,}")
    c5.metric("💰 Billing Amount", f"{total_revenue:,.0f}")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Appointment Status")

        if "status" in df.columns:

            status_data = df["status"].value_counts().reset_index()
            status_data.columns = ["Status", "Count"]

            fig = px.bar(
                status_data,
                x="Status",
                y="Count",
                text="Count",
                title="Appointments by Status"
            )

            fig.update_layout(
                showlegend=False,
                height=400
            )

            st.plotly_chart(fig, width="stretch")

    with col2:

        st.subheader("Payment Status")

        if "payment_status" in df.columns:

            payment_data = df["payment_status"].value_counts().reset_index()
            payment_data.columns = ["Payment Status", "Count"]

            fig = px.pie(
                payment_data,
                names="Payment Status",
                values="Count",
                hole=0.45,
                title="Payment Status Distribution"
            )

            fig.update_layout(height=400)

            st.plotly_chart(fig, width="stretch")


# ============================================================
# PAGE 2 — PATIENT ANALYSIS
# ============================================================

elif page == "👥 Patient Analysis":

    st.markdown('<div class="section-title">Patient Analysis</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        if "gender" in df.columns:

            gender_data = df["gender"].value_counts().reset_index()
            gender_data.columns = ["Gender", "Count"]

            fig = px.pie(
                gender_data,
                names="Gender",
                values="Count",
                hole=0.45,
                title="Patient Gender Distribution"
            )

            st.plotly_chart(fig, width="stretch")

    with col2:

        if "Age" in df.columns:

            age_data = df.copy()

            age_data["Age_Group"] = pd.cut(
                age_data["Age"],
                bins=[0, 18, 30, 45, 60, 120],
                labels=[
                    "0-18",
                    "19-30",
                    "31-45",
                    "46-60",
                    "61+"
                ],
                include_lowest=True
            )

            age_groups = (
                age_data["Age_Group"]
                .value_counts()
                .sort_index()
                .reset_index()
            )

            age_groups.columns = ["Age Group", "Count"]

            fig = px.bar(
                age_groups,
                x="Age Group",
                y="Count",
                text="Count",
                title="Patient Age Groups"
            )

            st.plotly_chart(fig, width="stretch")

    st.subheader("Patient Records")

    patient_columns = [
        col for col in [
            "patient_id",
            "Patient_Name",
            "gender",
            "date_of_birth",
            "Age",
            "contact_number",
            "registration_date"
        ]
        if col in df.columns
    ]

    if patient_columns:
        st.dataframe(
            df[patient_columns].drop_duplicates("patient_id"),
            width="stretch",
            height=400
        )


# ============================================================
# PAGE 3 — DOCTOR ANALYSIS
# ============================================================

elif page == "👨‍⚕️ Doctor Analysis":

    st.markdown('<div class="section-title">Doctor Analysis</div>',
                unsafe_allow_html=True)

    doctor_counts = (
        df.groupby("Doctor_Name")
        .size()
        .reset_index(name="Appointments")
        .sort_values("Appointments", ascending=False)
    )

    fig = px.bar(
        doctor_counts,
        x="Doctor_Name",
        y="Appointments",
        text="Appointments",
        title="Appointments by Doctor"
    )

    fig.update_layout(
        xaxis_tickangle=-45,
        height=500
    )

    st.plotly_chart(fig, width="stretch")

    if "specialization" in df.columns:

        specialization = (
            df.groupby("specialization")
            .size()
            .reset_index(name="Appointments")
            .sort_values("Appointments", ascending=False)
        )

        fig = px.bar(
            specialization,
            x="specialization",
            y="Appointments",
            text="Appointments",
            title="Appointments by Specialization"
        )

        st.plotly_chart(fig, width="stretch")

    st.subheader("Doctor Summary")

    doctor_columns = [
        col for col in [
            "doctor_id",
            "Doctor_Name",
            "specialization",
            "department",
            "experience_years"
        ]
        if col in df.columns
    ]

    if doctor_columns:

        doctor_summary = df[doctor_columns].drop_duplicates("doctor_id")

        st.dataframe(
            doctor_summary,
            width="stretch",
            height=350
        )


# ============================================================
# PAGE 4 — APPOINTMENT ANALYSIS
# ============================================================

elif page == "📅 Appointment Analysis":

    st.markdown('<div class="section-title">Appointment Analysis</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        status_data = df["status"].value_counts().reset_index()
        status_data.columns = ["Status", "Count"]

        fig = px.bar(
            status_data,
            x="Status",
            y="Count",
            text="Count",
            title="Appointment Status"
        )

        st.plotly_chart(fig, width="stretch")

    with col2:

        reason_data = df["reason_for_visit"].value_counts().reset_index()
        reason_data.columns = ["Reason", "Count"]

        fig = px.bar(
            reason_data,
            x="Count",
            y="Reason",
            orientation="h",
            text="Count",
            title="Reasons for Visit"
        )

        st.plotly_chart(fig, width="stretch")

    st.subheader("Appointment Details")

    appointment_columns = [
        col for col in [
            "appointment_id",
            "patient_id",
            "Doctor_Name",
            "appointment_date",
            "appointment_time",
            "reason_for_visit",
            "status"
        ]
        if col in df.columns
    ]

    st.dataframe(
        df[appointment_columns].sort_values(
            "appointment_date",
            ascending=False
        ),
        width="stretch",
        height=450
    )


# ============================================================
# PAGE 5 — TREATMENT ANALYSIS
# ============================================================

elif page == "💊 Treatment Analysis":

    st.markdown('<div class="section-title">Treatment Analysis</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        treatment_counts = (
            df["treatment_type"]
            .value_counts()
            .reset_index()
        )

        treatment_counts.columns = [
            "Treatment Type",
            "Count"
        ]

        fig = px.bar(
            treatment_counts,
            x="Treatment Type",
            y="Count",
            text="Count",
            title="Treatment Types"
        )

        fig.update_layout(xaxis_tickangle=-30)

        st.plotly_chart(fig, width="stretch")

    with col2:

        treatment_cost = (
            df.groupby("treatment_type")["cost"]
            .sum()
            .reset_index()
            .sort_values("cost", ascending=False)
        )

        fig = px.bar(
            treatment_cost,
            x="treatment_type",
            y="cost",
            text="cost",
            title="Treatment Cost by Type"
        )

        fig.update_layout(xaxis_tickangle=-30)

        st.plotly_chart(fig, width="stretch")

    st.subheader("Treatment Records")

    treatment_columns = [
        col for col in [
            "treatment_id",
            "appointment_id",
            "treatment_type",
            "description",
            "cost",
            "treatment_date"
        ]
        if col in df.columns
    ]

    st.dataframe(
        df[treatment_columns],
        width="stretch",
        height=400
    )


# ============================================================
# PAGE 6 — BILLING & PAYMENTS
# ============================================================

elif page == "💰 Billing & Payments":

    st.markdown('<div class="section-title">Billing & Payments</div>',
                unsafe_allow_html=True)

    total_billing = df["amount"].sum()
    average_bill = df["amount"].mean()

    paid_amount = df.loc[
        df["payment_status"] == "Paid",
        "amount"
    ].sum()

    pending_amount = df.loc[
        df["payment_status"] == "Pending",
        "amount"
    ].sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Billing", f"{total_billing:,.0f}")
    c2.metric("Average Bill", f"{average_bill:,.0f}")
    c3.metric("Paid Amount", f"{paid_amount:,.0f}")
    c4.metric("Pending Amount", f"{pending_amount:,.0f}")

    col1, col2 = st.columns(2)

    with col1:

        payment_method = (
            df["payment_method"]
            .value_counts()
            .reset_index()
        )

        payment_method.columns = [
            "Payment Method",
            "Count"
        ]

        fig = px.pie(
            payment_method,
            names="Payment Method",
            values="Count",
            hole=0.45,
            title="Payment Methods"
        )

        st.plotly_chart(fig, width="stretch")

    with col2:

        payment_status = (
            df["payment_status"]
            .value_counts()
            .reset_index()
        )

        payment_status.columns = [
            "Payment Status",
            "Count"
        ]

        fig = px.bar(
            payment_status,
            x="Payment Status",
            y="Count",
            text="Count",
            title="Payment Status"
        )

        st.plotly_chart(fig, width="stretch")

    st.subheader("Billing Records")

    billing_columns = [
        col for col in [
            "bill_id",
            "treatment_id",
            "bill_date",
            "amount",
            "payment_method",
            "payment_status"
        ]
        if col in df.columns
    ]

    st.dataframe(
        df[billing_columns],
        width="stretch",
        height=400
    )


# ============================================================
# PAGE 7 — MONTHLY TRENDS
# ============================================================

elif page == "📈 Monthly Trends":

    st.markdown('<div class="section-title">Monthly Trends</div>',
                unsafe_allow_html=True)

    if "appointment_date" in df.columns:

        monthly = (
            df.groupby(
                df["appointment_date"].dt.month
            )
            .size()
            .reset_index(name="Appointments")
        )

        monthly["Month"] = pd.to_datetime(
            monthly["appointment_date"],
            format="%m"
        ).dt.month_name()

        monthly = monthly.sort_values("appointment_date")

        fig = px.line(
            monthly,
            x="Month",
            y="Appointments",
            markers=True,
            text="Appointments",
            title="Monthly Appointment Trend"
        )

        st.plotly_chart(fig, width="stretch")

    if "bill_date" in df.columns:

        revenue = (
            df.groupby(
                df["bill_date"].dt.month
            )["amount"]
            .sum()
            .reset_index()
        )

        revenue["Month"] = pd.to_datetime(
            revenue["bill_date"],
            format="%m"
        ).dt.month_name()

        revenue = revenue.sort_values("bill_date")

        fig = px.line(
            revenue,
            x="Month",
            y="amount",
            markers=True,
            text="amount",
            title="Monthly Revenue Trend"
        )

        st.plotly_chart(fig, width="stretch")


# ============================================================
# PAGE 8 — HOSPITAL RELATIONSHIPS
# ============================================================

elif page == "🔗 Hospital Relationships":

    st.markdown(
        '<div class="section-title">Hospital Relationship Analysis</div>',
        unsafe_allow_html=True
    )

    st.info(
        "This section demonstrates how patient, doctor, appointment, "
        "treatment and billing tables are connected through IDs."
    )

    relationship_data = pd.DataFrame({
        "Relationship": [
            "Patient → Appointment",
            "Doctor → Appointment",
            "Appointment → Treatment",
            "Treatment → Billing"
        ],
        "Key": [
            "patient_id",
            "doctor_id",
            "appointment_id",
            "treatment_id"
        ]
    })

    st.dataframe(
        relationship_data,
        width="stretch"
    )

    st.subheader("Appointment → Treatment Analysis")

    treatment_by_reason = (
        df.groupby("reason_for_visit")["cost"]
        .mean()
        .reset_index()
        .sort_values("cost", ascending=False)
    )

    fig = px.bar(
        treatment_by_reason,
        x="reason_for_visit",
        y="cost",
        text="cost",
        title="Average Treatment Cost by Visit Reason"
    )

    st.plotly_chart(fig, width="stretch")

    st.subheader("Age vs Treatment Cost")

    if "Age" in df.columns:

        fig = px.scatter(
            df,
            x="Age",
            y="cost",
            color="treatment_type",
            hover_data=[
                "Patient_Name",
                "Doctor_Name"
            ],
            title="Patient Age vs Treatment Cost"
        )

        st.plotly_chart(fig, width="stretch")


# ============================================================
# PAGE 9 — DSA CONCEPTS
# ============================================================

elif page == "🧠 DSA Concepts":

    st.markdown(
        '<div class="section-title">Data Structures & Algorithms Demonstration</div>',
        unsafe_allow_html=True
    )

    st.info(
        "The following operations demonstrate how common DSA concepts "
        "can be applied to hospital analytics."
    )

    # Dictionary / Hash Map
    st.subheader("1️⃣ Dictionary / Hash Map")

    doctor_lookup = (
        df[["doctor_id", "Doctor_Name"]]
        .drop_duplicates()
        .set_index("doctor_id")["Doctor_Name"]
        .to_dict()
    )

    selected_doctor = st.selectbox(
        "Search Doctor ID",
        list(doctor_lookup.keys())
    )

    st.success(
        f"Doctor ID {selected_doctor} → "
        f"{doctor_lookup[selected_doctor]}"
    )

    # Searching
    st.subheader("2️⃣ Searching")

    search_name = st.text_input(
        "Search patient name"
    )

    if search_name:

        results = df[
            df["Patient_Name"]
            .str.contains(
                search_name,
                case=False,
                na=False
            )
        ]

        st.write(
            f"Search results: {len(results)}"
        )

        st.dataframe(
            results,
            width="stretch"
        )

    # Sorting
    st.subheader("3️⃣ Sorting")

    sort_column = st.selectbox(
        "Sort by",
        [
            "Age",
            "cost",
            "amount"
        ]
    )

    sorted_data = df.sort_values(
        sort_column,
        ascending=False
    )

    st.dataframe(
        sorted_data.head(10),
        width="stretch"
    )

    # Top-K
    st.subheader("4️⃣ Top-K Analysis")

    top_k = st.slider(
        "Select K",
        min_value=3,
        max_value=10,
        value=5
    )

    top_doctors = (
        df.groupby("Doctor_Name")
        .size()
        .reset_index(name="Appointments")
        .sort_values(
            "Appointments",
            ascending=False
        )
        .head(top_k)
    )

    st.dataframe(
        top_doctors,
        width="stretch"
    )

    # Frequency counting
    st.subheader("5️⃣ Frequency Counting")

    frequency = (
        df["reason_for_visit"]
        .value_counts()
        .reset_index()
    )

    frequency.columns = [
        "Reason",
        "Frequency"
    ]

    st.dataframe(
        frequency,
        width="stretch"
    )

    # Filtering
    st.subheader("6️⃣ Filtering")

    filter_status = st.selectbox(
        "Appointment Status",
        sorted(df["status"].dropna().unique())
    )

    filtered = df[
        df["status"] == filter_status
    ]

    st.write(
        f"Records with status '{filter_status}': "
        f"{len(filtered)}"
    )

    st.dataframe(
        filtered.head(20),
        width="stretch"
    )


# ============================================================
# PAGE 10 — INSIGHTS
# ============================================================

elif page == "💡 Insights":

    st.markdown(
        '<div class="section-title">Key Data Insights</div>',
        unsafe_allow_html=True
    )

    # Appointment insight
    most_common_status = (
        df["status"].value_counts().idxmax()
    )

    status_count = (
        df["status"].value_counts().max()
    )

    st.markdown(
        f"""
        <div class="insight-box">
        <b>📅 Appointment Status:</b><br>
        The most frequent appointment status in the dataset is
        <b>{most_common_status}</b>, with <b>{status_count}</b> records.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Visit reason
    common_reason = (
        df["reason_for_visit"]
        .value_counts()
        .idxmax()
    )

    reason_count = (
        df["reason_for_visit"]
        .value_counts()
        .max()
    )

    st.markdown(
        f"""
        <div class="insight-box">
        <b>🩺 Common Visit Reason:</b><br>
        <b>{common_reason}</b> is the most frequently recorded
        reason for a hospital visit, with <b>{reason_count}</b> records.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Treatment
    common_treatment = (
        df["treatment_type"]
        .value_counts()
        .idxmax()
    )

    treatment_count = (
        df["treatment_type"]
        .value_counts()
        .max()
    )

    st.markdown(
        f"""
        <div class="insight-box">
        <b>💊 Treatment Pattern:</b><br>
        <b>{common_treatment}</b> is the most frequently recorded
        treatment type, appearing <b>{treatment_count}</b> times.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Doctor
    top_doctor = (
        df["Doctor_Name"]
        .value_counts()
        .idxmax()
    )

    top_doctor_count = (
        df["Doctor_Name"]
        .value_counts()
        .max()
    )

    st.markdown(
        f"""
        <div class="insight-box">
        <b>👨‍⚕️ Doctor Workload:</b><br>
        <b>{top_doctor}</b> has the highest number of recorded
        appointments with <b>{top_doctor_count}</b> appointments.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Payment
    common_payment = (
        df["payment_method"]
        .value_counts()
        .idxmax()
    )

    st.markdown(
        f"""
        <div class="insight-box">
        <b>💳 Payment Method:</b><br>
        <b>{common_payment}</b> is the most frequently used
        payment method in the dataset.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Correlation
    st.subheader("Correlation Analysis")

    numeric_columns = [
        col for col in [
            "Age",
            "cost",
            "amount"
        ]
        if col in df.columns
    ]

    if len(numeric_columns) >= 2:

        corr = df[numeric_columns].corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            title="Numeric Feature Correlation"
        )

        st.plotly_chart(fig, width="stretch")


# ============================================================
# PAGE 11 — DATASET INFORMATION
# ============================================================

elif page == "📊 Dataset Information":

    st.markdown(
        '<div class="section-title">Dataset Information</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Rows",
        f"{df.shape[0]:,}"
    )

    c2.metric(
        "Columns",
        f"{df.shape[1]:,}"
    )

    c3.metric(
        "Missing Values",
        f"{df.isna().sum().sum():,}"
    )

    st.subheader("Dataset Structure")

    info_data = pd.DataFrame({
        "Column": df.columns,
        "Data Type": [
            str(dtype)
            for dtype in df.dtypes
        ],
        "Missing Values": [
            int(df[col].isna().sum())
            for col in df.columns
        ],
        "Unique Values": [
            int(df[col].nunique())
            for col in df.columns
        ]
    })

    st.dataframe(
        info_data,
        width="stretch",
        height=500
    )

    st.subheader("Processed Dataset Preview")

    st.dataframe(
        df.head(20),
        width="stretch",
        height=500
    )

    st.success(
        "The dataset was cleaned, date-formatted, feature-engineered "
        "and exported from the Google Colab preprocessing workflow."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Hospital Management Analytics Dashboard | "
    "Python • Pandas • Plotly • Streamlit"
)