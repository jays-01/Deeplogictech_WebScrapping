from flask import Flask
import urllib.request
import json

app = Flask(__name__)

# Function to make an HTTP request and get the HTML content
def get_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
        return html_content
    except Exception as e:
        print("Error fetching HTML:", e)
        return None

# Function to extract the latest stories
def extract_stories(html):
    latest_stories = []
    current_title = ""
    current_link = ""
    latest_stories_div =[]

    lines = html.split("\n")

    for line in range(len(lines)):
        if "partial latest-stories" in lines[line]:
            line+=1
            while("</div>" not in lines[line]):
                latest_stories_div.append(lines[line])
                line+=1

    for line in latest_stories_div:
        if 'href="' in line:
            href_index = line.find('href="') + 6
            link_end_index = line.find('"',href_index)
            current_link = line[href_index:link_end_index]

        if "latest-stories__item-headline" in line:
            title_start_index = line.find('>') + 1
            title_end_index = line.find('<',title_start_index)
            current_title += line[title_start_index:title_end_index]
            latest_stories.append({'title': current_title,'link': 'https://time.com'+current_link})
            current_title = ""
            current_link = ""

    return latest_stories[:6]

# Main function to fetch latest stories from Time.com
def fetch_latest_stories():
    latest_stories = []
    url = 'https://time.com/'
    html = get_content(url)
    if html:
        latest_stories = extract_stories(html)
        return latest_stories
    else:
        return []
    


@app.route('/getTimeStories')
def get_time_stories():
    latest_stories = fetch_latest_stories()
    return json.dumps(latest_stories)

if __name__ == '__main__':
    app.run(debug=False)