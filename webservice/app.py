from flask import Flask
from github import Github

app = Flask(__name__)

#get repository object from Github
def get_repo(repo):
    github = Github()
    repo = github.get_repo(repo)
    return repo

#get issue objects from each repository.
#status can be either 'open' or 'closed'
def take_issues(repo, status):
    issues = repo.get_issues(state = status)
    return issues

#calculate the number of open comments, the number of closed comments 
#and total comments.
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

#get total labels on issues.
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

#get the number of open issues, closed issues and total issues
def total_issues(open_issues, closed_issues):

    total_open_issues = 0
    for issue in open_issues:
        total_open_issues += 1
    total_closed_issues = 0
    for issue in closed_issues:
        total_closed_issues += 1

    total_issue_number = total_open_issues + total_closed_issues

    return total_open_issues, total_closed_issues, total_issue_number

#return all the data in one request.
@app.route('/calculate_metrics')
@app.route('/')
def calculate_metrics():
    repo_name = "DIP-Group/GithubTracker"
    repo = get_repo(repo_name)
    open_issues = take_issues(repo,'open')
    closed_issues = take_issues(repo,'closed')
    total_open_issues, total_closed_issues, total_issue_number = total_issues(open_issues,closed_issues)
    closed_comment,open_comment,total_comment = total_comment_number(open_issues, closed_issues)
    label_no = total_labels(open_issues, closed_issues)
    result = {
        "Repository_name": repo_name,
        "Open_issue_number": total_open_issues,
        "Closed_issue_number": total_closed_issues,
        "Total_issue_number": total_issue_number,
        "Closed_comment_number": closed_comment,
        "Open_comment_number": open_comment,
        "Total_comment_number": total_comment,
        "Total_label_number": label_no
    }
    return result
    
#return only the issue data.
@app.route('/issues')
def issues():
    repo_name = "DIP-Group/GithubTracker"
    repo = get_repo(repo_name)
    open_issues = take_issues(repo,'open')
    closed_issues = take_issues(repo,'closed')
    total_open_issues, total_closed_issues, total_issue_number = total_issues(open_issues,closed_issues)
    result = {
        "Repository_name": repo_name,
        "Open_issue_number": total_open_issues,
        "Closed_issue_number": total_closed_issues,
        "Total_issue_number": total_issue_number,
    }
    return result

#return only the comments data.
@app.route('/comments')
def comments():
    repo_name = "DIP-Group/GithubTracker"
    repo = get_repo(repo_name)
    open_issues = take_issues(repo,'open')
    closed_issues = take_issues(repo,'closed')
    closed_comment,open_comment,total_comment = total_comment_number(open_issues, closed_issues)
    result = {
        "Repository name": repo_name,
        "Closed comment number": closed_comment,
        "Open comment number": open_comment,
        "Total comment number": total_comment,
    }
    return result

#return only the labels data.
@app.route('/labels')
def labels():
    repo_name = "DIP-Group/GithubTracker"
    repo = get_repo(repo_name)
    open_issues = take_issues(repo,'open')
    closed_issues = take_issues(repo,'closed')
    label_no = total_labels(open_issues, closed_issues)
    result = {
        "Repository name": repo_name,
        "Total label number": label_no
    }
    return result