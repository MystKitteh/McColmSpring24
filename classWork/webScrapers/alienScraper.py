import bs4
import requests
import os

archive_url = "http://www.textfiles.com/ufo/"

def get_tales():
    r = requests.get(archive_url)

    soup = bs4.BeautifulSoup(r.content, 'html.parser')

    # find all links on web-page
    for item in soup.findAll('li'):
        link = item.find('a')
        href = archive_url + link['href']
        download_links(href)
    print("All stories downloaded!")

def download_links(href):

    file_name = href.split('/')[-1]
    print("Downloading file: " + file_name)


    r = requests.get(href, stream = True)

    workingDir = os.getcwd()
    print("current working directory: " + workingDir)
    fileDeposit = os.path.join(workingDir, 'wearenotAlone', file_name)
    print(fileDeposit)



    with open(fileDeposit, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024*1024):
            if chunk:
                f.write(chunk)
                print("Downloaded " + file_name)

    return

if __name__ == "__main__":

    get_tales = get_tales()






