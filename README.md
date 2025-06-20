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
