# KoboToolbox Batch Permissions Assigner

A **Streamlit web app** to quickly assign and update user permissions for any KoboToolbox project, in bulk.

---

## 🚀 Features

- Supports [kf.kobotoolbox.org](https://kf.kobotoolbox.org), [kobo.humanitarianresponse.info](https://kobo.humanitarianresponse.info), or a custom Kobo server
- Login with your **API token**
- Select any project from your account
- Paste multiple usernames at once (one per line)
- Select any combination of the most-used permissions to assign
- For each user, **removes all existing permissions for the project** and applies only the permissions you select
- Transparent logs: see exactly which API calls are made and the result for each user/permission

---

## ✅ Supported Permissions

You can assign any of these roles (tick one or more):

- View asset
- Add submissions
- Edit submissions
- Validate submissions
- Delete submissions
- Edit asset
- Delete asset

*Not included: “Partial submissions”, “Transfer asset”, or “Manage asset” (these are rarely used or not supported in all Kobo setups).*

---

## 🖥️ Installation

Requires: **Python 3.8+**

1. Open a terminal and install dependencies:

    ```bash
    pip install streamlit requests
    ```

2. Save the script (e.g., as `kobo_batch_permissions.py`) in a folder.

---

## 🏁 Usage

1. Launch the app:

    ```bash
    streamlit run kobo_batch_permissions.py
    ```

2. Your browser will open to `http://localhost:8501` (if not, open it manually).

3. **Follow these steps:**
    - **Select your KoboToolbox server** (or enter a custom URL)
    - **Paste your API token** (find it in your KoboToolbox profile/settings)
    - Click **Fetch Projects** and pick the project you want to manage
    - **Paste usernames** (one per line; case-sensitive, not email unless that is their Kobo username)
    - **Tick the permissions** you want to assign
    - Click **Assign/Update Permissions**
    - Check the logs for each action, including errors and success messages

**How it works:**  
The app deletes all existing permissions for each user on the chosen project, then sets only the permissions you selected.

---

## 🛠️ Troubleshooting

- **Usernames must match exactly** (as registered in KoboToolbox).
- You must have permission to manage project permissions (usually you are the project owner or an admin).
- All API requests and responses are logged in the app for transparency.
- If you get errors (user not found, forbidden, etc), double-check the username and your access rights.

---

## 🔒 Security

- Your API token is only used locally for calls between your computer and your KoboToolbox server.
- This app does **not** send data anywhere else.

---

## 📜 License

MIT License (or your preferred license)

---

_Made with [Streamlit](https://streamlit.io/) and ChatGPT 🤖_
