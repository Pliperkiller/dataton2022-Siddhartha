def bs_semana(soup):
    return soup.find('article',class_='paywall').get_text(strip=True,separator=' ')

def bs_larepublica(soup):
    return soup.find('div',class_="html-content").get_text(strip=True,separator=' ')

def bs_espectador(soup):
    return soup.find('section',class_='false').get_text(strip=True,separator=' ')
    
def bs_portafolio(soup):
    return soup.find('div',class_='article-content').get_text(strip=True,separator=' ')

def bs_elpais(soup):
    return soup.find('div',class_='a_c clearfix').get_text(strip=True,separator=' ')
    
def bs_eltiempo(soup):
    return soup.find('p',class_='contenido').get_text(strip=True,separator=' ')    

def bs_infobae(soup):
    return soup.find('div',class_='nd-body-article').get_text(strip=True,separator=' ') 

def bs_laopinion(soup):
    return soup.find('div',class_='field field--name-field-meta-article-components field--type-entity-reference-revisions field--label-hidden field__items').get_text(strip=True,separator=' ') 
    

def bs_bnamericas(soup):
    return soup.find('div',class_='card__paragraph').get_text(strip=True,separator=' ')     

def bs_redmas(soup):
    return soup.find('div',class_='text-entrada').get_text(strip=True,separator=' ')
    
def bs_bloomberglinea(soup):
    return soup.find('div',class_='col-sm-md-12 col-lg-xl-8 left-article-section ie-flex-100-percent-sm layout-section').get_text(strip=True,separator=' ')
    
def bs_elespanol(soup):
    return soup.find('div',class_='article-body__content').get_text(strip=True,separator=' ')
    
def bs_elcolombiano(soup):
    return soup.find('div',class_='portlet-boundary portlet-static-end content-viewer-portlet contenido-articulo last full-access norestricted').get_text(strip=True,separator=' ')
    
def bs_cnn(soup):
    return soup.find('div',class_='storyfull__body').get_text(strip=True,separator=' ')
    
def bs_bbc(soup):
    return soup.find('div',class_='e1j2237y4 bbc-irdbz7 ebmt73l0').get_text(strip=True,separator=' ')