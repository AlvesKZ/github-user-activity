import requests
import sys


def main(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        events = response.json()

        if not events:
            print(f"No recent events found for user: {username}")
            return

        print(f"\n=== Recent Activity for {username} ===\n")

        for event in events:
            event_type = event["type"]
            repo_name = event["repo"]["name"]
            created_at = event["created_at"]

            if event_type == "PushEvent":
                payload = event["payload"]
                commit_count = len(payload.get("commits", []))
                ref = payload.get("ref", "").replace("refs/heads/", "")
                print(f"- Pushed {commit_count} commit(s) to {repo_name} ({ref})")

            elif event_type == "CreateEvent":
                payload = event["payload"]
                ref_type = payload.get("ref_type")
                ref = payload.get("ref", "")
                print(f"- Created {ref_type}: {ref} in {repo_name}")

            elif event_type == "DeleteEvent":
                payload = event["payload"]
                ref_type = payload.get("ref_type")
                ref = payload.get("ref", "")
                print(f"- Deleted {ref_type}: {ref} in {repo_name}")

            elif event_type == "WatchEvent":
                print(f"- Starred {repo_name}")

            elif event_type == "ForkEvent":
                print(f"- Forked {repo_name}")

            elif event_type == "IssuesEvent":
                payload = event["payload"]
                action = payload.get("action")
                issue_number = payload.get("issue", {}).get("number")
                print(f"- {action.capitalize()} issue #{issue_number} in {repo_name}")

            elif event_type == "IssueCommentEvent":
                payload = event["payload"]
                issue_number = payload.get("issue", {}).get("number")
                print(f"- Commented on issue #{issue_number} in {repo_name}")

            elif event_type == "PullRequestEvent":
                payload = event["payload"]
                action = payload.get("action")
                pr_number = payload.get("number")
                print(f"- {action.capitalize()} pull request #{pr_number} in {repo_name}")

            elif event_type == "PullRequestReviewEvent":
                payload = event["payload"]
                pr_number = payload.get("pull_request", {}).get("number")
                print(f"- Reviewed pull request #{pr_number} in {repo_name}")

            elif event_type == "PullRequestReviewCommentEvent":
                payload = event["payload"]
                pr_number = payload.get("pull_request", {}).get("number")
                print(f"- Commented on pull request #{pr_number} in {repo_name}")

            elif event_type == "ReleaseEvent":
                payload = event["payload"]
                tag_name = payload.get("release", {}).get("tag_name", "")
                print(f"- Published release {tag_name} in {repo_name}")

            elif event_type == "MemberEvent":
                payload = event["payload"]
                member = payload.get("member", {}).get("login", "")
                print(f"- Added {member} as collaborator to {repo_name}")

            elif event_type == "PublicEvent":
                print(f"- Made {repo_name} public")

            elif event_type == "GollumEvent":
                payload = event["payload"]
                pages_count = len(payload.get("pages", []))
                print(f"- Updated {pages_count} wiki page(s) in {repo_name}")

            else:
                print(f"- {event_type} in {repo_name}")

        print(f"\n=== Total events: {len(events)} ===\n")

    elif response.status_code == 404:
        print(f"User '{username}' not found.")
    elif response.status_code == 403:
        print("Rate limit exceeded. Please try again later.")
    else:
        print(f"Error fetching events for {username}: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python script.py <github_username>")
        print("Example: python script.py octocat")