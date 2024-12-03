import requests
from bs4 import BeautifulSoup

usr = "NishaantKrSingh"
url = f"https://github.com/users/{usr}/contributions?from=2024-01-01&to=2024-12-31"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract data from ContributionCalendar-day and tool-tip
contributions = []

for td in soup.find_all("td", {"class": "ContributionCalendar-day"}):
    date = td.get("data-date")
    tooltip_id = td.get("id")
    tooltip = soup.find("tool-tip", {"for": tooltip_id})
    if date and tooltip:
        # Parse contribution count from tooltip text
        text = tooltip.text.strip()
        if "No contributions" in text:
            count = 0
        else:
            count = int(text.split()[0])  # Extract the number from the text
        contributions.append({"date": date, "contributions": count})

# print(contributions)

for i in contributions:
    if i["contributions"] != 0:
        print(i["date"], ":", i["contributions"])