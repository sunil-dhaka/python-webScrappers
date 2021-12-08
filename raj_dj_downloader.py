'''
Meta info
Website name: https://djjpswami.com/

Scrapes all songs link and then downloads them in particular directories
'''
import requests
from bs4 import BeautifulSoup as bs
import os
from tqdm import tqdm

# to supress warnings
import warnings
warnings.filterwarnings("ignore")

def downloader(url=None,name=None):
    if url is not None and name is not None:
        if not(os.path.exists(name)):
            with open(name,'wb') as f:
                pass
        resume_headers={'Range':f'bytes={os.stat(name).st_size}-'}
        r=requests.get(url,stream=True,verify=False,headers=resume_headers)
        total_size=int(r.headers.get('Content-Length'))
        # print(r.headers)
        inital_pos=0
        with open(name,'ab') as f:
            with tqdm(total=total_size,unit_scale=True,unit='B',desc=name,initial=inital_pos,ascii=True) as progress_bar:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)	
                        progress_bar.update(len(chunk))
        print(f'Completed downloading of {name}.')
    else:
        pass

def dir_check(dir_name=None):
    if os.path.isdir(os.path.join(os.getcwd(),dir_name)):
        if os.getcwd()==os.path.join(os.getcwd(),dir_name):
            pass
        else:
            os.chdir(os.path.join(os.getcwd(),dir_name))
    else:
        os.mkdir(os.path.join(os.getcwd(),dir_name))
        os.chdir(os.path.join(os.getcwd(),dir_name))

def main():
    url='https://djjpswami.com/filelist/118/rajasthani_dj_remix_songs/a2z/1.html'
    r=requests.get(url)
    soup=bs(r.text,'html.parser')
    s=soup.find('div',{'class':'pgn'})
    total_pages=s.div.text.split('/')[-1].split(')')[0]
    if total_pages.isnumeric():
        total_pages=int(total_pages)
    else:
        total_pages=1

    for page in range(total_pages):
        print(f'working on page -- {page+1}')
        page_url=f'https://djjpswami.com/filelist/118/rajasthani_dj_remix_songs/a2z/{page+1}.html'
        r=requests.get(page_url)
        soup=bs(r.text,'html.parser')
        links=soup.find('div',{'class':'catList'}).find_all('a')
        for link in links:
            # links is found manually and then generalized
            if link.img.get('title') is not None:
                title='%20'.join(link.img.get('title').strip().split(' '))+'(DjJpSwami.Com).mp3'
                # src1=link.img.get('src').split('/')[-2]
                src2=link.img.get('src').split('/')[-1].split('_')[0]
                # src='https://djjpswami.com/siteuploads/files/'+src1+'/'+src2+'/'
                name=link.get('href').split('/')[-1].split('.')[0]+'.mp3'
                # downloader(src+title)
                downloader(f'https://djjpswami.com/files/download/id/{src2}',name)
                # print(src+title)
if __name__=='__main__':
    folder=os.path.expanduser('~')+'/Music/'+'Raj_DJ'
    dir_check(folder)
    main()