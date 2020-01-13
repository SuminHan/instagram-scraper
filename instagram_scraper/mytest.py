#%%
from app import InstagramScraper

#%%
v = InstagramScraper()

#v.login_user = 'suminkaist@gmail.com'
#v.login_pass = '!summer221b'
#v.authenticate_with_login()

#%%
#json_data = v._InstagramScraper__search('오늘은쉼표;카페')


# %%
#for v in json_data['places']:
#    w = v['place']['location']
#    if 'lat' in w and 'lng' in w:
#        display(w['name'], w['external_source'], w['lat'], w['lng'])

# %%
   

#v.usernames = ['217847758965661']
v.usernames = ['22642832']

a = v.my_scrape_location()

# %%
