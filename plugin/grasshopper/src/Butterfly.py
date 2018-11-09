# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
This component downloads butterfly library from github to:
C:\Users\%USERNAME%\AppData\Roaming\McNeel\Rhinoceros\5.0\scripts\butterfly

-

    Args:
        butterflyFolder_: Optional path to load butterfly libraries instead of the
            installed version
        update_: Optional boolean to update butterfly even if you have it already installed.
    Returns:
        swooooosh: !!!
"""

ghenv.Component.Name = "Butterfly"
ghenv.Component.NickName = "BF::BF"
ghenv.Component.Message = 'VER 0.0.04\nNOV_08_2018'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

import os
import System
import sys
import zipfile
import shutil
from Grasshopper.Folders import UserObjectFolders

import System
System.Net.ServicePointManager.SecurityProtocol = System.Net.SecurityProtocolType.Tls12


def removeButterfly(folder):
    """Remove current butterfly userobjects."""
    print('Removing Butterfly UserObjects from {}'.format(folder))

    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        
        if os.path.isdir(path):
            removeButterfly(path)

        if f.startswith("Butterfly"):
            try:
                os.remove(path)    
            except:
                print('Failed to remove: {}'.format(path))


def installButterfly(update):
    
    """
    This code will download butterfly library from github to:
        C:\Users\%USERNAME%\AppData\Roaming\McNeel\Rhinoceros\5.0\scripts\butterfly
    """
    urls = ("https://github.com/ladybug-tools/butterfly/archive/master.zip",
            "https://github.com/ladybug-tools/butterfly-plus/archive/master.zip")
    folders = ('butterfly', 'butterfly-plus')
    libs = ('butterfly', 'butterfly_grasshopper')

    targetDirectory = [p for p in sys.path if p.find('scripts')!= -1][0]
    
    for f in libs:
        libFolder = os.path.join(targetDirectory, f)
        if not update and os.path.isdir(libFolder):
            return
        elif update and os.path.isdir(libFolder):
            try:
                print('Removing {}'.format(libFolder))
                shutil.rmtree(libFolder)
            except:
                print('Failed to remove {}'.format(libFolder))
                
    for count, (folder, url) in enumerate(zip(folders, urls)):
        # download the zip file
        lib = libs[count]
        print "Downloading {} repository to {}".format(folder, targetDirectory)
        zipFile = os.path.join(targetDirectory, '%s.zip' % folder)

        try:
            client = System.Net.WebClient()
            client.DownloadFile(url, zipFile)
        except Exception, e:
            msg = `e` + "\nDownload failed! Try to download and unzip the file manually form:\n" + url
            raise Exception(msg)
            
        #unzip the file
        with zipfile.ZipFile(zipFile) as zf:
            for f in zf.namelist():
                if f.endswith('/'):
                    try: os.makedirs(f)
                    except: pass
                else:
                    zf.extract(f, targetDirectory)
        zf.close()
        
        bfFolder = os.path.join(targetDirectory, r"{}-master".format(folder), lib)
        libFolder = os.path.join(targetDirectory, lib)
        print 'Copying butterfly source code from {} to {}'.format(bfFolder, libFolder)
        shutil.copytree(bfFolder, libFolder)

        if count == 1:
            # copy userobjects
            uofolder = UserObjectFolders[0]
            bfuofolder = os.path.join(uofolder, 'Butterfly')
            if not os.path.isdir(bfuofolder):
                os.mkdir(bfuofolder)

            bfUserObjectsFolder = os.path.join(targetDirectory, r"butterfly-plus-master\plugin\grasshopper\userObjects")
            print 'Copying butterfly userobjects to {}'.format(bfuofolder)
            
            # remove all the butterfly userobjects
            removeButterfly(uofolder)
                    
            for f in os.listdir(bfUserObjectsFolder):
                shutil.copyfile(os.path.join(bfUserObjectsFolder, f),
                                os.path.join(bfuofolder, f))
    
        # try to clean up
        try:
            shutil.rmtree(os.path.join(targetDirectory, r"{}-master".format(folder)))
            os.unlink(zipFile)
        except:
            pass


if not butterflyFolder_:
    installButterfly(update_)
elif update_ and not os.path.isdir(butterflyFolder_):
   installButterfly(update_)
elif os.path.isdir(butterflyFolder_) and butterflyFolder_ not in sys.path:
        sys.path.insert(0, butterflyFolder_)


try:
    import butterfly
    import butterfly_grasshopper
    from butterfly.version import Version
    print "Imported butterfly from {}\nswoosh swoosh...".format(butterfly.__file__)
    
    try:
        print "Last updated: {}".format(Version.lastUpdated)
    except:
        pass
except ImportError as e:
    raise Exception("Failed to import butterfly:\n{}".format(e))

# push butterfly component to back
ghenv.Component.OnPingDocument().SelectAll()
ghenv.Component.Attributes.Selected = False
ghenv.Component.OnPingDocument().BringSelectionToTop()
ghenv.Component.OnPingDocument().DeselectAll()