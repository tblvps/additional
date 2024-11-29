import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse

# GitHub API base URL and headers
BASE_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {settings.GITHUB_ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


# List repositories
def list_repos(request):
    try:
        url = f"{BASE_URL}/user/repos"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        repos = response.json()
        return render(request, "github/list.html", {"repos": repos})
    except requests.exceptions.RequestException as e:
        messages.error(request, f"Error fetching repositories: {e}")
        return render(request, "github/list.html", {"repos": []})


# Create a repository
def create_repo(request):
    if request.method == "POST":
        repo_name = request.POST.get("name")
        private = request.POST.get("private") == "on"
        url = f"{BASE_URL}/user/repos"
        payload = {"name": repo_name, "private": private}
        try:
            response = requests.post(url, json=payload, headers=HEADERS)
            response.raise_for_status()
            messages.success(request, f"Repository '{repo_name}' created successfully.")
            return redirect("list_repos")
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Error creating repository: {e}")
            return redirect("create_repo")
    return render(request, "github/create.html")


# Delete a repository
def delete_repo(request):
    if request.method == "POST":
        owner = request.POST.get("owner")
        repo_name = request.POST.get("repo")
        url = f"{BASE_URL}/repos/{owner}/{repo_name}"
        try:
            response = requests.delete(url, headers=HEADERS)
            if response.status_code == 204:
                messages.success(request, f"Repository '{repo_name}' deleted successfully.")
            else:
                messages.error(request, f"Failed to delete repository: {response.status_code}")
            return redirect("list_repos")
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Error deleting repository: {e}")
            return redirect("list_repos")
    return render(request, "github/delete.html")
