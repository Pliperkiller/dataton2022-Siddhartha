def bs_semana(soup):
    return soup.find('article',class_='paywall').get_text(strip=True,separator=' ')

def bs_larepublica(soup):
    return soup.find('div',class_="html-content").get_text(strip=True,separator=' ')

def bs_espectador(soup):
    return soup.find('section',class_='false').get_text(strip=True,separator=' ')
    
def bs_portafolio(soup):
    return soup.find('div',class_='article-content').get_text(strip=True,separator=' ')
    
