import webbrowser

def website_opener(domain):
    try:
        url = 'https://www.' + domain
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False