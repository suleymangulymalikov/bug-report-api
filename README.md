## 🐛 Bug Report API

A simple RESTful API built with **Python Flask** that allows users to submit, view, and delete bug reports. This project is part of a learning journey to become a junior backend developer.

---

## 🚀 Features

- Submit a bug report with:
  - `user_name`
  - `bug_title`
  - `bug_description`
  - `bug_severity` (must be `low`, `medium`, or `high`)
- View all bug reports
- View a bug report by user ID
- Delete a bug report by user ID

---

## 📦 Technologies Used

- Python 3
- Flask
- UUID for unique user IDs
- Postman (for testing)
- datetime for timestamps

---

## 📂 Project Structure

```

bug-report-api/
├── app.py             # Main Flask app
├── db.py              # In-memory list of bug reports
├── requirements.txt   # Required Python packages
└── .gitignore

````

---

## 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/suleymangulymalikov/bug-report-api.git
   cd bug-report-api


2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate     # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**

   ```bash
   python app.py
   ```

---

## 🧪 API Endpoints

### ✅ `GET /`

Welcome message.

### ✅ `GET /bug-reports`

Returns a list of all submitted bug reports.

### ✅ `POST /bug-report`

Submit a new bug report.
**Required JSON body:**

```json
{
  "user_name": "Ali",
  "bug_title": "Login not working",
  "bug_description": "Users cannot log in with correct credentials.",
  "bug_severity": "high"
}
```

### ✅ `GET /bug-report/<user_id>`

Returns a specific bug report by user ID.

### ✅ `DELETE /bug-report/<user_id>`

Deletes a specific bug report by user ID.

---

## 📌 Notes

* Data is **stored in memory** using Python lists — restarting the server resets the data.
* No database or user authentication yet — this is an educational prototype.

---

## 📜 License

This project is open source and free to use for learning purposes.

---

## 🙌 Author

Developed by Suleymanguly Malikov.
