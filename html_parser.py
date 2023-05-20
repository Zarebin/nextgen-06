from bs4 import BeautifulSoup

def main_content_finder(html_content, special_tag=False, og_tag=True):
    """This function try to find out main content using 'og' tags. (e.g. description and title) if user want to
    search for a specific tag in html documents he/she has to pass special_tag like p for <p>"""
    soup = BeautifulSoup(html_content, features="html.parser")

    if special_tag:
        matched_tags = soup.findAll(special_tag)
        return matched_tags

    if og_tag:
        title = soup.find("meta", attrs={'property': 'og:title'})
        description = soup.find("meta", attrs={'property': 'og:description'})
        if title["content"] is not None or description["content"] is not None:
            matched_tags = soup.find_all(lambda tag: not (not (len(tag.find_all()) == 0) or not (
                        str(description["content"]) in tag.text)) or len(tag.find_all()) == 0 and str(title["content"]) in tag.text)

            return matched_tags
        else:
            return None
