
markdown
Copy
Edit
# KoboToolbox Batch Permissions Assigner

This Streamlit web app lets you **assign or update permissions** for multiple users on any KoboToolbox project, in bulk, with just a few clicks.

## Features

- Select your KoboToolbox server and authenticate with your API token
- Choose your project (asset) from a dropdown
- Paste a list of usernames (one per line)
- Select one or more permissions to assign (e.g., "Add submissions", "Edit submissions", etc.)
- For each user, **removes all existing permissions for the project**, then assigns your selected ones
- Prints all payloads and API responses for troubleshooting

## Permissions You Can Assign

- View asset
- Add submissions
- Edit submissions
- Validate submissions
- Delete submissions
- Edit asset
- Delete asset

_(“Manage asset”, “Transfer asset”, and “Partial submissions” are intentionally excluded)_

## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/) and [requests](https://docs.python-requests.org/en/latest/)

Install requirements:

```bash
pip install streamlit requests
Usage
Clone or copy this script (e.g., kobo_batch_permissions.py) to your computer.

Open a terminal and run:

bash
Copy
Edit
streamlit run kobo_batch_permissions.py
The app will open in your browser (usually at http://localhost:8501).

How to use the app:

Select your KoboToolbox server or enter a custom URL

Paste your API token (find it in your user profile on KoboToolbox)

Click "Fetch Projects" and select the target project

Paste usernames (one per line, case-sensitive, as in KoboToolbox)

Tick the permissions you want each user to have

Click "Assign/Update Permissions"

Review the log for results, API calls, and any errors

What happens under the hood?

For each username, all their current project permissions are removed

The checked permissions are (re)assigned exactly as you select

Troubleshooting
Usernames must be exact (as shown in KoboToolbox, usually not emails unless that is their username)

If you get errors about permissions or assignments, check the Streamlit log for the payload and response

You need to be a project owner or have admin privileges to assign permissions

Security
Never share your API token.

This tool runs locally and does not send data anywhere except your KoboToolbox server.

License
MIT License (or as you choose)
