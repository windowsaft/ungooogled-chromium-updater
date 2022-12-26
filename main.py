import os
import requests
from bs4 import BeautifulSoup
from clint.textui import progress
from zipfile import ZipFile
import shutil

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

    print(fullUrl)

    r = requests.get(fullUrl)
    soup = BeautifulSoup(r.content, 'html.parser')
    archiveUrl = soup.find_all("a")[7]["href"]
    

    r = requests.get(archiveUrl, stream=True)
    FileName = archiveUrl.split("/")[-1]
    print(FileName)
    FilePath = os.getcwd() + "/tmp/" + FileName
    
    
    with open(FilePath, "wb") as BrowserArchive:
        total_length = int(r.headers.get('content-length'))
        for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
            if ch:
                BrowserArchive.write(ch)


    return FileName


def updateFiles(Version, latestVersion, ArchiveName):
    AppPath = os.path.expanduser('~') + "/AppData/Local/Chromium/Application/"
    AppDir = os.path.join(AppPath, Version)
    #os.rmdir(AppDir)

    ZipArchiveDestinationDirectory = os.path.join(AppPath, latestVersion.split("-")[0])
    ZipArchive = ZipFile(os.path.join(os.path.join(os.getcwd(), "tmp"), ArchiveName))
    ZipArchive.extractall(path=os.path.join(os.getcwd(), "tmp"))

    

    os.rename(os.path.join(os.path.join(os.getcwd(), "tmp"), os.listdir(os.path.join(os.getcwd(), "tmp"))[0]), ZipArchiveDestinationDirectory)

    WidevineCdmPath = os.getcwd() + "/resources/WidevineCdm"
    WidevineCdmDestinationPath = os.path.join(ZipArchiveDestinationDirectory, "WidevineCdm")
    shutil.copytree(WidevineCdmPath, WidevineCdmDestinationPath)




os.mkdir(os.path.join(os.getcwd(), "tmp"), 0o666)
Version = getVersion()
latestVersion = getLatestVersion()

if Version != latestVersion[:-2]:
    ArchiveName = downloadLatestVersion(latestVersion)
    updateFiles(Version=Version, latestVersion=latestVersion, ArchiveName=ArchiveName)

else:
    print(f"The latest version ({Version}) is installed!")

shutil.rmtree(os.path.join(os.getcwd(), "tmp"))