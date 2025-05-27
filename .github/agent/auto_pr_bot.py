import os

from datetime import datetime

import requests

from github import Github


GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
REPO_NAME = os.environ["GITHUB_REPO"]
PROMPT_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
)

# GitHub setup
gh = Github(os.environ["GITHUB_TOKEN"])
repo = gh.get_repo(REPO_NAME)

# Get latest issue
issues = repo.get_issues(state="open", sort="created", direction="desc")
issue = next(iter(issues), None)

if not issue:
    print("No open issues found.")
    exit(0)

print(f"Found issue #{issue.number}: {issue.title}")

# Build prompt
prompt = f"""
You are a Python code assistant. Suggest a Python code fix for the following GitHub issue.

Title: {issue.title}
Description: {issue.body}

The repository is structured as a Python library, with a `src/` directory and `tests/`.

Only return code — either new functions, modifications, or class definitions.
Include minimal comments. Do not include explanations, just the code.
"""

# Call Gemini API
headers = {"Content-Type": "application/json"}
params = {"key": GEMINI_API_KEY}
body = {"contents": [{"parts": [{"text": prompt}]}]}

response = requests.post(PROMPT_URL, headers=headers, params=params, json=body)
resp_json = response.json()
if "candidates" not in resp_json:
    print("Gemini API error:", resp_json)
    exit(1)
generated = resp_json["candidates"][0]["content"]["parts"][0]["text"]

print("Generated code:\n", generated)

# Create branch
base_branch = repo.get_branch("main")
branch_name = f"gemini-fix-{issue.number}-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_branch.commit.sha)

# Save suggestion to a markdown file
file_path = f"auto_solutions/issue_{issue.number}_gemini.md"
repo.create_file(file_path, generated, generated, branch=branch_name)

# Create PR
pr_title = f"[Gemini Bot] Fix for Issue #{issue.number}: {issue.title}"
pr_body = f"Auto-generated suggestion using Gemini:\n\n```python\n{generated}\n```"

repo.create_pull(title=pr_title, body=pr_body, head=branch_name, base="main")

print("Pull request created.")
