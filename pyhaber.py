from GoogleNews import GoogleNews

#
googlenews = GoogleNews()
googlenews = GoogleNews(lang='tr', period='7d')
googlenews.search('Türkiye')
haber = googlenews.result()

for i in haber:
    print("")
    print("Başlık: ",i['title'])
    print("Açıklama: ",i['desc'])
    print("Zaman: ",i['date'])
    print("Haberin Linki: ",i['link']) 
