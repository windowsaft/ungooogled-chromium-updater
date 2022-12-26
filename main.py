import os
import requests
from bs4 import BeautifulSoup
from clint.textui import progress

def getVersion():
    AppPath = os.path.expanduser('~') + "/AppData/Local/Chromium/Application/"
    files = os.listdir(AppPath)
    version = files[0]
    
    return version


def getLatestVersion():
    url = "https://ungoogled-software.github.io/ungoogled-chromium-binaries/releases/windows/64bit/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    version = soup.li.text

    return version


def downloadLatestVersion(version):
    baseUrl = "https://ungoogled-software.github.io/ungoogled-chromium-binaries/releases/windows/64bit/"
    fullUrl = baseUrl + version

    r = requests.get(fullUrl)
    soup = BeautifulSoup(r.content, 'html.parser')
    installerUrl = soup.find_all("a")[6]["href"]
    
    r = requests.get(installerUrl, stream=True)
    FileName = installerUrl.split("/")[-1]
    print(FileName)
    with open(FileName, "wb") as Installer:
        total_length = int(r.headers.get('content-length'))
        for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
            if ch:
                Installer.write(ch)


    return FileName



Version = getVersion()
latestVersion = getLatestVersion()

if Version != latestVersion[:-2]:
    InstallerFile = downloadLatestVersion(latestVersion)
    os.system(f".\{InstallerFile}")