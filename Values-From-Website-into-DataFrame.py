import re
from bs4 import BeautifulSoup
from bs4.element import Comment

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


request = Request(
    'https://www.gfsc.gg/news',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})

html = urlopen(request).read()

text = (text_from_html(html))

pattern = re.compile(r'(£\d\d,?\d,?\d\d?\d)')

matches = pattern.findall(text)

results = []


for match in matches:
    print(match)
    results.append(match)
    
df = pd.DataFrame(results)
df.columns = ['Values']
df = df['Values'].str.replace('£', '').str.replace(',', '').to_frame()
df['12.5%'] = df['Values'].astype(int) * 0.125
print('\n')
print(df)