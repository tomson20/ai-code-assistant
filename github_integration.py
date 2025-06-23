from github import Github

def create_github_pr(repo_name, base_branch, new_branch, title, body, file_path, file_content):
    g = Github("YOUR_GITHUB_TOKEN")  # შენ უნდა დაამატო რეპოზიტორიის სახელი და ტოკენი
    repo = g.get_repo(repo_name)

    try:
        # Create new branch
        base_sha = repo.get_branch(base_branch).commit.sha
        repo.create_git_ref(ref=f"refs/heads/{new_branch}", sha=base_sha)

        # Create or update file
        try:
            contents = repo.get_contents(file_path, ref=base_branch)
            repo.update_file(contents.path, "Update via AI Agent", file_content, contents.sha, branch=new_branch)
        except:
            repo.create_file(file_path, "Initial commit via AI Agent", file_content, branch=new_branch)

        # Open Pull Request
        pr = repo.create_pull(
            title=title,
            body=body,
            head=new_branch,
            base=base_branch
        )
        return f"✅ PR created: {pr.html_url}"

    except Exception as e:
        return f"❌ Error creating PR: {e}"