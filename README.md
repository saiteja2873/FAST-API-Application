# FastAPI Wallet Management System

A simple **FastAPI** application to manage users, wallets, and
transactions.

## 🚀 Live API Docs

👉 [FastAPI Swagger
Docs](https://fast-api-application-1.onrender.com/docs)

------------------------------------------------------------------------

## 📌 Features

1.  **List Users API** -- Fetch all users details (name, email, phone)
    along with their wallet balance.\
2.  **Update Wallet API** -- Add or update an amount in any particular
    user's wallet.\
3.  **Fetch Transactions API** -- Fetch all wallet transactions for a
    specific user by passing their `user_id`.

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

``` bash
git clone <your-repo-link>
cd <your-repo-folder>
```

### 2️⃣ Create and activate a virtual environment

``` bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Run the server

``` bash
uvicorn main:app --reload
```

Now visit 👉 <http://127.0.0.1:8000/docs>

------------------------------------------------------------------------

## 🛠 API Endpoints

### 🔹 List Users

**GET** `/users`\
Fetch all users along with their wallet balance.

### 🔹 Update Wallet

**POST** `/wallet/update`\
Update/add balance to a user's wallet.

### 🔹 Fetch Transactions

**GET** `/transactions/{user_id}`\
Fetch all transactions of a specific user.

------------------------------------------------------------------------

## 📦 Deployment

This app is deployed on **Render**.\
You can access the live API here:\
👉 [Live Demo](https://fast-api-application-1.onrender.com/docs)

------------------------------------------------------------------------

## 👨‍💻 Author

Developed by **Sai Teja**
