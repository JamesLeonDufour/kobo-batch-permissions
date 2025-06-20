import streamlit as st
import requests

st.set_page_config(page_title="KoboToolbox Batch Permissions Assigner", layout="centered")
st.title("KoboToolbox Batch Permissions Assigner (with Update)")

SERVER_OPTIONS = [
    'https://kf.kobotoolbox.org',
    'https://eu.kobotoolbox.org',
    'Custom'
]

server = st.selectbox("Select Kobo server", SERVER_OPTIONS)
if server == "Custom":
    server = st.text_input("Custom Kobo server URL (with https://)", "https://")
server = server.rstrip("/")

token = st.text_input("API Token", type="password")

# Fetch projects
fetch = st.button("Fetch Projects")
if fetch:
    if not token or not server:
        st.warning("Please enter server and API token")
    else:
        headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
        url = f"{server}/api/v2/assets.json"
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            st.error(f"Failed to fetch projects. Response:\n\n{resp.text}")
        else:
            try:
                assets = resp.json().get('results', [])
                if not assets:
                    st.error("No projects found.")
                else:
                    st.session_state['assets'] = assets
                    st.success(f"Found {len(assets)} projects.")
            except Exception as e:
                st.error(f"Error decoding JSON: {e}\nResponse:\n{resp.text[:400]}")

assets = st.session_state.get('assets', [])
project_uid = None
if assets:
    project_options = [f"{a['name']} ({a['uid']})" for a in assets]
    project_choice = st.selectbox("Select project", project_options)
    idx = project_options.index(project_choice)
    project_uid = assets[idx]['uid']

usernames = st.text_area("Usernames to add (one per line):", height=180)

# Static list of permissions (excluding transfer_asset, manage_asset, partial_submissions)
static_permissions = [
    {"codename": "view_asset", "name": "View asset"},
    {"codename": "add_submissions", "name": "Add submissions"},
    {"codename": "change_submissions", "name": "Edit submissions"},
    {"codename": "validate_submissions", "name": "Validate submissions"},
    {"codename": "delete_submissions", "name": "Delete submissions"},
    {"codename": "change_asset", "name": "Edit asset"},
    {"codename": "delete_asset", "name": "Delete asset"}
]

for perm in static_permissions:
    perm["url"] = f"{server}/api/v2/permissions/{perm['codename']}/"

st.markdown("### Select permissions to assign:")
selected_permissions = []
for perm in static_permissions:
    checked = st.checkbox(f"{perm['name']} ({perm['codename']})", value=(perm['codename']=="add_submissions"), key=perm['codename'])
    if checked:
        selected_permissions.append(perm)

def get_existing_assignments(server, token, project_uid):
    headers = {"Authorization": f"Token {token}"}
    url = f"{server}/api/v2/assets/{project_uid}/permission-assignments/"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        if isinstance(data, dict) and "results" in data:
            return data["results"]
        elif isinstance(data, list):
            return data
        else:
            return []
    return []

if st.button("Assign/Update Permissions"):
    if not (token and server and project_uid):
        st.warning("Please fetch projects and select a project first.")
    elif not selected_permissions:
        st.warning("Please select at least one permission.")
    else:
        ids = [u.strip() for u in usernames.splitlines() if u.strip()]
        if not ids:
            st.warning("Please enter at least one username.")
        else:
            headers = {"Authorization": f"Token {token}", "Content-Type": "application/json"}
            existing = get_existing_assignments(server, token, project_uid)
            # Build quick lookup of assignments for each user
            assignments_by_user = {}
            for a in existing:
                user = a["user"]
                assignments_by_user.setdefault(user, []).append(a)

            added = []
            for ident in ids:
                user_url = f"{server}/api/v2/users/{ident}/"
                st.write(f"User: {ident}")
                st.write(f"User URL: {user_url}")
                # Delete ALL assignments for this user on this asset
                if user_url in assignments_by_user:
                    for assignment in assignments_by_user[user_url]:
                        del_url = assignment["url"]
                        st.write(f"Deleting old permission assignment: {del_url}")
                        try:
                            r = requests.delete(del_url, headers=headers)
                            st.write(f"DELETE response: {r.status_code}, {r.text}")
                        except Exception as e:
                            st.error(f"Error deleting assignment for {ident}: {e}")

                # POST the new permissions selected
                for perm in selected_permissions:
                    payload = {
                        "user": user_url,
                        "permission": perm["url"]
                    }
                    assign_url = f"{server}/api/v2/assets/{project_uid}/permission-assignments/"
                    st.write(f"POSTing {assign_url} with {payload}")
                    try:
                        r = requests.post(assign_url, headers=headers, json=payload)
                        st.write(f"POST response: {r.status_code}, {r.text}")
                        if r.status_code in (200, 201):
                            added.append(f"{ident} ({perm['codename']})")
                        else:
                            st.error(f"Failed to assign {perm['codename']} for {ident}: {r.text}")
                    except Exception as e:
                        st.error(f"Request error for {ident}, {perm['codename']}: {e}")
            if added:
                st.success(f"Permissions assigned: {', '.join(added)}")

st.markdown("---")
