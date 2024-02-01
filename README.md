Explanation of the assignment :

**How to get the html content ?**\n
To get the HTML content, I have defined a function "get_content" which makes http request to the host website and decodes the recieved response.
For this purpose I have used urllib.request library. If there's any error while making http request the function raises an exception error as e.

**How to extract stories?**\n
My function "extract_stories" takes the received data(html content) and store it in a list(lines in my case).
After storing the content in list It looks for the line with "partial latest-stories" which is the div for the latest stories division, which I came to know after inspecting the page.
Once it finds the "partial latest-stories" division it start putting the next lines in a list until the closing </div> tag is found.
After which it looks for line with "latest-stories__item-headline" in the new list to extract title and 'href="' to extract link.

**API : **
For API I have used flask.

