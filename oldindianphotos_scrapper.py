'''
this script shows category names and based on category 
input downloades all images from that category from 
https://www.oldindianphotos.in/ website
'''
import requests
from bs4 import BeautifulSoup as bs
import os
from tqdm import tqdm

def downloader(url):
    name=url.split('/')[-1]

    if not(os.path.exists(name)):
        with open(name,'wb') as f:
            pass
    resume_headers={'Range':f'bytes={os.stat(name).st_size}-'}
    r=requests.get(url,stream=True,verify=False,headers=resume_headers)
    total_size=int(r.headers.get('Content-Length'))
    print(r.headers)
    inital_pos=0
    with open(name,'ab') as f:
        with tqdm(total=total_size,unit_scale=True,unit='B',desc=name,initial=inital_pos,ascii=True) as progress_bar:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)	
                    progress_bar.update(len(chunk))		
    
    print(f'Completed downloading of {name}.')

url='https://www.oldindianphotos.in'

def make_dir(dir_name):
    if os.path.exists(dir_name) and os.path.isdir(dir_name):
        os.chdir(dir_name)
    else:
        os.makedirs(dir_name)
        os.chdir(dir_name)

try:
    r=requests.get(url)
    soup=bs(r.text,'html.parser')
    cat_data=soup.find(id='main-sidebar').ul.find_all('li')
    cat_link=[s.a.get('href') for s in cat_data]
    cat_names=[s.a.text.strip() for s in cat_data]

    for i,cat in enumerate(cat_names):
        make_dir(cat)

        # get all links of images
        images_links=[]
        response=requests.get(cat_link[i])
        image_soup=bs(response.text,'html.parser')
        curr_pager=True
        while(image_soup.find(id='Blog1_blog-pager-older-link') is not None):
            for link in image_soup.find(id='main-wrapper').find(id='Blog1').find_all('img'):         
                images_links.append(link.get('src'))

            curr_link=image_soup.find(id='Blog1_blog-pager-older-link').get('href')
            response=requests.get(curr_link)
            image_soup=bs(response.text,'html.parser')
        
        # download links
        already_there_images=os.listdir()

        for link in images_links:
            if link.split('/')[-1] not in already_there_images:
                downloader(link)
        os.chdir('..')
        print(''.center(50,'='))
        print(f'completed > {cat}')
        print(''.center(50,'='))
except Exception as e:
    print(f'Error: {e}')