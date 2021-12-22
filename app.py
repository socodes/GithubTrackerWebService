from flask import Flask
from github import Github

app = Flask(__name__)

def get_repo(repo):
    github = Github()
    repo = github.get_repo(repo)
    return repo

#status can be either 'open' or 'closed'
def take_issues(repo, status):
    issues = repo.get_issues(state = status)
    return issues
    


@app.route('/<repo_no>')
def main(repo_no):
    repo_no = int(repo_no)-1
    repo_name = "DIP-Group/GithubTracker"
    repo = get_repo(repo_name)
    issue = take_issues(repo,'open')
    return issue[repo_no].title