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

def total_comment_number(open_issues,closed_issues):
    comment_no = 0
    open_total_comments = 0
    closed_total_comments = 0
    total = 0
    for issue in open_issues:
        comment_no = issue.comments
        open_total_comments += comment_no
    total += comment_no
    comment_no = 0
    for issue in closed_issues:
        comment_no= issue.comments
        closed_total_comments += comment_no 
    total += comment_no
    return closed_total_comments,open_total_comments,total

def total_labels(open_issues,closed_issues):
    total_issues = []
    label_no = 0
    for issue in open_issues:
        total_issues.append(issue)
    for issue in closed_issues:
        total_issues.append(issue)
    for issue in total_issues:
        labels = issue.get_labels()
        for label in labels:
            label_no += 1
    return label_no  

def total_issues(open_issues, closed_issues):

    total_open_issues = 0
    for issue in open_issues:
        total_open_issues += 1
    total_closed_issues = 0
    for issue in closed_issues:
        total_closed_issues += 1

    total_issue_number = total_open_issues + total_closed_issues

    return total_open_issues, total_closed_issues, total_issue_number

@app.route('/')
def main():
    repo_name = "DIP-Group/GithubTracker"
    repo = get_repo(repo_name)
    open_issues = take_issues(repo,'open')
    closed_issues = take_issues(repo,'closed')
    total_open_issues, total_closed_issues, total_issue_number = total_issues(open_issues,closed_issues)
    closed_comment,open_comment,total_comment = total_comment_number(open_issues, closed_issues)
    label_no = total_labels(open_issues, closed_issues)
    result = {
        "Repository name": repo_name,
        "Open issue number": total_open_issues,
        "Closed issue number": total_closed_issues,
        "Total issue number": total_issue_number,
        "Closed comment number": closed_comment,
        "Open comment number": open_comment,
        "Total comment number": total_comment,
        "Total label number": label_no
    }
    return result