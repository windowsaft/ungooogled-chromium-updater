import os
import requests
from bs4 import BeautifulSoup
from clint.textui import progress
from zipfile import ZipFile
import shutil
import pyfiglet
import pyfiglet.fonts
from readchar import readchar

PATH = os.path.abspath(".")
BASE_URL = "https://ungoogled-software.github.io/ungoogled-chromium-binaries/releases/windows/64bit/"
TMP_PATH = os.path.join(PATH, "tmp")
APP_PATH = os.path.expanduser('~') + "\\AppData\\Local\\Chromium\\Application\\"
WIDEVINECDM_PATH = os.path.join(os.path.join(PATH, "resources"), "WidevineCdm")

def getVersion():
    AppPath = os.path.expanduser('~') + "/AppData/Local/Chromium/Application/"
    files = os.listdir(AppPath)
    version = files[0]
    
    return version


def getLatestVersion():
    r = requests.get(BASE_URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    version = soup.li.text

    return version


def downloadHandler(archiveUrl):
    print("Downloading Newest Version:")

    r = requests.get(archiveUrl, stream=True)
    FileName = archiveUrl.split("/")[-1]
    FilePath = os.path.join(TMP_PATH, FileName) 

    with open(FilePath, "wb") as BrowserArchive:
        total_length = int(r.headers.get('content-length'))
        for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
            if ch:
                BrowserArchive.write(ch)

    return FileName


def downloadLatestVersion(version):
    fullUrl = BASE_URL + version

    r = requests.get(fullUrl)
    soup = BeautifulSoup(r.content, 'html.parser')
    archiveUrl = soup.find_all("a")[7]["href"]
    
    return downloadHandler(archiveUrl)


def updateFiles(Version, latestVersion, ArchiveName):
    VersionPath = os.path.join(APP_PATH, Version)
    ArchivePath = os.path.join(TMP_PATH, ArchiveName)
    ArchiveDestinationPath = os.path.join(APP_PATH, latestVersion.split("-")[0])
    WidevineCdmDestinationPath = os.path.join(ArchiveDestinationPath, "WidevineCdm")
     
    ZipArchive = ZipFile(ArchivePath)
    ZipArchive.extractall(path=TMP_PATH)

    shutil.rmtree(VersionPath) 
    os.rename(os.path.join(TMP_PATH, os.listdir(TMP_PATH)[0]), ArchiveDestinationPath)
    shutil.copytree(WIDEVINECDM_PATH, WidevineCdmDestinationPath)


f = pyfiglet.Figlet(font='slant')
print(f.renderText('Ungoogled Chromium Autoupdater'))

Version = getVersion()
latestVersion = getLatestVersion()

if Version != latestVersion[:-2]:
    os.mkdir(TMP_PATH, 0o666)
    ArchiveName = downloadLatestVersion(latestVersion)
    updateFiles(Version=Version, latestVersion=latestVersion, ArchiveName=ArchiveName)
    shutil.rmtree(TMP_PATH)
    print()
    print(f"The Latest Version ({latestVersion[:-2]}) Has Been Installed!")

else:
    print(f"The Latest Version ({Version}) Is Installed!")
    

print("Press Any Key To Exit...")
readchar()