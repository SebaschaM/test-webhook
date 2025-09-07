import discordbot
import asyncio
#1
def handle_issues(data):
    action = data.get("action")
    if action == "opened":
        issue = data["issue"]
        title = issue["title"]
        url = issue["html_url"]
        asyncio.run_coroutine_threadsafe(
            discordbot.notify_issue(title, url), discordbot.bot.loop
        )
