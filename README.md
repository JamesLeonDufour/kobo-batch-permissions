# KoboToolbox Batch Permissions Assigner

A **Streamlit web app** for managing KoboToolbox user permissions in bulk—quickly assign or update roles for multiple users on any project.

---

## 🚀 Features

- Supports [kf.kobotoolbox.org](https://kf.kobotoolbox.org) and [kobo.humanitarianresponse.info](https://kobo.humanitarianresponse.info) (or your own custom server)
- Authenticate using your KoboToolbox **API token**
- Select any project from your account
- Assign multiple permissions (add/view/edit/delete submissions, edit/delete asset, etc.) to any number of users at once
- For each user: **removes all existing permissions on the project** and applies only those selected
- See all API requests, responses, and error messages for easy troubleshooting

---

## ✅ Supported Permissions

- View asset
- Add submissions
- Edit submissions
- Validate submissions
- Delete submissions
- Edit asset
- Delete asset

> **Note:**  
> “Partial submissions”, “Transfer asset”, and “Manage asset” are intentionally excluded as they are rarely needed or supported.

---

## 🖥️ Installation

Requires **Python 3.8+**

1. Install dependencies:

   ```bash
   pip install streamlit requests
