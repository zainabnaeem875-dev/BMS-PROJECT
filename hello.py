import streamlit as st
from app import Bank


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SmartBank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f4f7fb;
}

/* Main content */
.main .block-container {
    max-width: 1250px;
    padding-top: 40px;
    padding-left: 45px;
    padding-right: 45px;
    padding-bottom: 50px;
}


/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background-color: #111d35 !important;
    min-width: 290px !important;
    max-width: 290px !important;
}

section[data-testid="stSidebar"] > div {
    width: 290px !important;
}


/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white !important;
}


/* Sidebar title */
.sidebar-title {
    font-size: 30px;
    font-weight: 800;
    text-align: center;
    color: white;
}


/* Sidebar subtitle */
.sidebar-subtitle {
    text-align: center;
    color: #aebbd0;
    font-size: 13px;
    margin-top: 5px;
}


/* Sidebar menu */
section[data-testid="stSidebar"] label {
    font-size: 16px !important;
    font-weight: 600 !important;
}


/* ================= HEADINGS ================= */

h1 {
    color: #10213f !important;
    font-size: 38px !important;
    font-weight: 800 !important;
}

h2 {
    color: #10213f !important;
}

h3 {
    color: #1e293b !important;
}


/* ================= NORMAL TEXT ================= */

p {
    color: #53657d;
    font-size: 16px;
}


/* ================= INPUTS ================= */

.stTextInput input,
.stNumberInput input {
    background-color: white !important;
    color: #172033 !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 8px !important;
    min-height: 45px !important;
    font-size: 15px !important;
}

.stTextInput input:focus,
.stNumberInput input:focus {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 2px rgba(37,99,235,0.12) !important;
}


/* Input labels */
[data-testid="stWidgetLabel"] p {
    color: #1e293b !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}


/* ================= BUTTONS ================= */

.stButton > button,
.stFormSubmitButton > button {
    background-color: #2563eb !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    min-height: 46px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

.stButton > button p,
.stFormSubmitButton > button p {
    color: white !important;
    font-weight: 700 !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #1d4ed8 !important;
}


/* ================= METRICS ================= */

[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 15px rgba(15,23,42,0.06);
}

[data-testid="stMetricLabel"] {
    color: #64748b !important;
}

[data-testid="stMetricValue"] {
    color: #10213f !important;
    font-weight: 800 !important;
}


/* ================= CHECKBOX ================= */

[data-testid="stCheckbox"] label p {
    color: #1e293b !important;
    font-weight: 600 !important;
}


/* ================= FOOTER ================= */

.footer {
    margin-top: 50px;
    padding-top: 25px;
    border-top: 1px solid #dbe2ea;
    text-align: center;
    color: #64748b;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# BANK OBJECT
# =========================================================

bank = Bank()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    '<div style="text-align:center;font-size:50px;">🏦</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="sidebar-title">SmartBank</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="sidebar-subtitle">Banking Management System</div>',
    unsafe_allow_html=True
)

st.sidebar.divider()

st.sidebar.markdown("### 📋 BANKING MENU")

page = st.sidebar.radio(
    "",
    [
        "🏠 Dashboard",
        "📝 Create Account",
        "💰 Deposit Money",
        "💸 Withdraw Money",
        "👤 Account Details",
        "✏️ Update Details",
        "🗑️ Delete Account"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### 🔐 Secure Banking")

st.sidebar.caption(
    "Safe • Simple • Reliable"
)

st.sidebar.caption(
    "Python + OOP + JSON + Streamlit"
)


# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.title("🏦 Welcome to SmartBank")

    st.write(
        "A simple, secure and reliable Banking Management System."
    )

    st.write("")

    # Statistics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👥 Total Accounts",
            bank.total_accounts()
        )

    with col2:
        st.metric(
            "💰 Total Balance",
            f"Rs. {bank.total_balance():,}"
        )

    with col3:
        st.metric(
            "🟢 System Status",
            "Active"
        )

    st.write("")
    st.divider()

    st.subheader("✨ Banking Services")

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            """
            ### 📝 Create Account

            Create a new SmartBank account
            with your personal information.
            """
        )

    with col2:
        st.success(
            """
            ### 💰 Deposit Money

            Add money to your bank account
            quickly and securely.
            """
        )

    with col3:
        st.warning(
            """
            ### 💸 Withdraw Money

            Withdraw money from your
            available account balance.
            """
        )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            """
            ### 👤 Account Details

            View your account information
            and current balance.
            """
        )

    with col2:
        st.info(
            """
            ### ✏️ Update Details

            Update your name, email
            or account PIN.
            """
        )

    with col3:
        st.error(
            """
            ### 🗑️ Delete Account

            Permanently remove your
            SmartBank account.
            """
        )


# =========================================================
# CREATE ACCOUNT
# =========================================================

elif page == "📝 Create Account":

    st.title("📝 Create New Account")

    st.write(
        "Fill in the information below to create your SmartBank account."
    )

    st.write("")

    with st.form("create_account_form"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Full Name",
                placeholder="Enter your full name"
            )

            age = st.number_input(
                "Age",
                min_value=1,
                max_value=100,
                value=18
            )

        with col2:

            email = st.text_input(
                "Email Address",
                placeholder="example@gmail.com"
            )

            pin = st.text_input(
                "4 Digit PIN",
                type="password",
                max_chars=4,
                placeholder="Enter your 4 digit PIN"
            )

        st.write("")

        submit = st.form_submit_button(
            "📝 Create Account",
            use_container_width=True
        )

    if submit:

        success, result = bank.create_account(
            name,
            age,
            email,
            pin
        )

        if success:

            st.success(
                "🎉 Account created successfully!"
            )

            st.write("")

            st.info(
                f"🏦 Your Account Number: **{result['accountNo']}**"
            )

            st.warning(
                "🔐 Please save your account number for future transactions."
            )

        else:

            st.error(
                f"❌ {result}"
            )


# =========================================================
# DEPOSIT MONEY
# =========================================================

elif page == "💰 Deposit Money":

    st.title("💰 Deposit Money")

    st.write(
        "Add money to your SmartBank account."
    )

    st.write("")

    with st.form("deposit_form"):

        account = st.text_input(
            "Account Number",
            placeholder="Enter your account number"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
            placeholder="Enter your 4 digit PIN"
        )

        amount = st.number_input(
            "Amount",
            min_value=1,
            max_value=10000,
            value=100,
            step=100
        )

        st.caption(
            "Maximum deposit amount: Rs. 10,000"
        )

        submit = st.form_submit_button(
            "💰 Deposit Money",
            use_container_width=True
        )

    if submit:

        success, result = bank.deposit_money(
            account,
            pin,
            amount
        )

        if success:

            st.success(
                "✅ Money deposited successfully!"
            )

            st.metric(
                "Updated Balance",
                f"Rs. {result:,}"
            )

        else:

            st.error(
                f"❌ {result}"
            )


# =========================================================
# WITHDRAW MONEY
# =========================================================

elif page == "💸 Withdraw Money":

    st.title("💸 Withdraw Money")

    st.write(
        "Withdraw money from your SmartBank account."
    )

    st.write("")

    with st.form("withdraw_form"):

        account = st.text_input(
            "Account Number",
            placeholder="Enter your account number"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
            placeholder="Enter your 4 digit PIN"
        )

        amount = st.number_input(
            "Amount",
            min_value=1,
            value=100,
            step=100
        )

        submit = st.form_submit_button(
            "💸 Withdraw Money",
            use_container_width=True
        )

    if submit:

        success, result = bank.withdraw_money(
            account,
            pin,
            amount
        )

        if success:

            st.success(
                "✅ Money withdrawn successfully!"
            )

            st.metric(
                "Remaining Balance",
                f"Rs. {result:,}"
            )

        else:

            st.error(
                f"❌ {result}"
            )


# =========================================================
# ACCOUNT DETAILS
# =========================================================

elif page == "👤 Account Details":

    st.title("👤 Account Details")

    st.write(
        "Enter your account number and PIN to view your details."
    )

    st.write("")

    with st.form("account_details_form"):

        account = st.text_input(
            "Account Number",
            placeholder="Enter your account number"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
            placeholder="Enter your 4 digit PIN"
        )

        submit = st.form_submit_button(
            "👤 View Account",
            use_container_width=True
        )

    if submit:

        success, user = bank.account_details(
            account,
            pin
        )

        if success:

            st.success(
                "✅ Account found!"
            )

            st.write("")

            col1, col2 = st.columns(2)

            with col1:

                st.info(
                    f"**👤 Name**\n\n{user['name']}"
                )

                st.info(
                    f"**🎂 Age**\n\n{user['age']}"
                )

                st.info(
                    f"**📧 Email**\n\n{user['email']}"
                )

            with col2:

                st.info(
                    f"**🏦 Account Number**\n\n{user['accountNo']}"
                )

                st.metric(
                    "💰 Current Balance",
                    f"Rs. {user['balance']:,}"
                )

        else:

            st.error(
                f"❌ {user}"
            )


# =========================================================
# UPDATE DETAILS
# =========================================================

elif page == "✏️ Update Details":

    st.title("✏️ Update Account")

    st.write(
        "Update your name, email or PIN."
    )

    st.info(
        "ℹ️ Account number, age and balance cannot be changed."
    )

    st.write("")

    with st.form("update_form"):

        account = st.text_input(
            "Account Number",
            placeholder="Enter your account number"
        )

        pin = st.text_input(
            "Current PIN",
            type="password",
            max_chars=4,
            placeholder="Enter your current PIN"
        )

        st.write("### New Information")

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "New Name",
                placeholder="Leave empty if no change"
            )

            email = st.text_input(
                "New Email",
                placeholder="Leave empty if no change"
            )

        with col2:

            new_pin = st.text_input(
                "New PIN",
                type="password",
                max_chars=4,
                placeholder="Leave empty if no change"
            )

        st.write("")

        submit = st.form_submit_button(
            "✏️ Update Details",
            use_container_width=True
        )

    if submit:

        success, message = bank.update_details(
            account,
            pin,
            name,
            email,
            new_pin
        )

        if success:

            st.success(
                "✅ Details updated successfully!"
            )

        else:

            st.error(
                f"❌ {message}"
            )


# =========================================================
# DELETE ACCOUNT
# =========================================================

elif page == "🗑️ Delete Account":

    st.title("🗑️ Delete Account")

    st.write(
        "Permanently remove your SmartBank account."
    )

    st.warning(
        "⚠️ Warning: Account deletion is permanent and cannot be undone."
    )

    st.write("")

    with st.form("delete_account_form"):

        account_number = st.text_input(
            "Account Number",
            placeholder="Enter your account number"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
            placeholder="Enter your 4 digit PIN"
        )

        st.write("")

        confirm = st.checkbox(
            "I understand that my account will be permanently deleted."
        )

        st.write("")

        delete_button = st.form_submit_button(
            "🗑️ Delete Account",
            use_container_width=True
        )

    if delete_button:

        if account_number.strip() == "":

            st.error(
                "❌ Please enter your account number."
            )

        elif pin.strip() == "":

            st.error(
                "❌ Please enter your PIN."
            )

        elif not confirm:

            st.warning(
                "⚠️ Please tick the confirmation checkbox first."
            )

        else:

            success, message = bank.delete_account(
                account_number,
                pin
            )

            if success:

                st.success(
                    "✅ Account deleted successfully!"
                )

                st.info(
                    "Your account has been permanently removed from SmartBank."
                )

            else:

                st.error(
                    f"❌ {message}"
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        🏦 <b>SmartBank</b><br>
        Banking Management System<br><br>
        Secure • Simple • Reliable<br>
        Python • OOP • JSON • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)