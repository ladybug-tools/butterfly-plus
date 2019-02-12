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
        butterfly_folder_: Optional path to load butterfly libraries instead of the
            installed version
        update_: Optional boolean to update butterfly even if you have it already installed.
    Returns:
        swooooosh: !!!
"""

ghenv.Component.Name = "Butterfly"
ghenv.Component.NickName = "BF::BF"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
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


def remove_butterfly(folder):
    """Remove current butterfly userobjects."""
    print('Removing Butterfly UserObjects from {}'.format(folder))

    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        
        if os.path.isdir(path):
            remove_butterfly(path)

        if f.startswith("Butterfly"):
            try:
                os.remove(path)    
            except:
                print('Failed to remove: {}'.format(path))


def install_butterfly(update):
    
    """
    This code will download butterfly library from github to:
        C:\Users\%USERNAME%\AppData\Roaming\McNeel\Rhinoceros\5.0\scripts\butterfly
    """
    urls = ("https://github.com/ladybug-tools/butterfly/archive/master.zip",
            "https://github.com/ladybug-tools/butterfly-plus/archive/master.zip")
    folders = ('butterfly', 'butterfly-plus')
    libs = ('butterfly', 'butterfly_grasshopper')

    target_directory = [p for p in sys.path if p.find('scripts')!= -1][0]
    
    for f in libs:
        lib_folder = os.path.join(target_directory, f)
        if not update and os.path.isdir(lib_folder):
            return
        elif update and os.path.isdir(lib_folder):
            try:
                print('Removing {}'.format(lib_folder))
                shutil.rmtree(lib_folder)
            except:
                print('Failed to remove {}'.format(lib_folder))
                
    for count, (folder, url) in enumerate(zip(folders, urls)):
        # download the zip file
        lib = libs[count]
        print "Downloading {} repository to {}".format(folder, target_directory)
        zip_file = os.path.join(target_directory, '%s.zip' % folder)

        try:
            client = System.Net.WebClient()
            client.DownloadFile(url, zip_file)
        except Exception, e:
            msg = `e` + "\nDownload failed! Try to download and unzip the file manually form:\n" + url
            raise Exception(msg)
            
        #unzip the file
        with zipfile.ZipFile(zip_file) as zf:
            for f in zf.namelist():
                if f.endswith('/'):
                    try: os.makedirs(f)
                    except: pass
                else:
                    zf.extract(f, target_directory)
        zf.close()
        
        bf_folder = os.path.join(target_directory, r"{}-master".format(folder), lib)
        lib_folder = os.path.join(target_directory, lib)
        print 'Copying butterfly source code from {} to {}'.format(bf_folder, lib_folder)
        shutil.copytree(bf_folder, lib_folder)

        if count == 1:
            # copy userobjects
            uofolder = UserObjectFolders[0]
            bfuofolder = os.path.join(uofolder, 'Butterfly')
            if not os.path.isdir(bfuofolder):
                os.mkdir(bfuofolder)

            bf_user_objects_folder = os.path.join(target_directory, r"butterfly-plus-master\plugin\grasshopper\userObjects")
            print 'Copying butterfly userobjects to {}'.format(bfuofolder)
            
            # remove all the butterfly userobjects
            remove_butterfly(uofolder)
                    
            for f in os.listdir(bf_user_objects_folder):
                shutil.copyfile(os.path.join(bf_user_objects_folder, f),
                                os.path.join(bfuofolder, f))
    
        # try to clean up
        try:
            shutil.rmtree(os.path.join(target_directory, r"{}-master".format(folder)))
            os.unlink(zip_file)
        except:
            pass


if not butterfly_folder_:
    install_butterfly(update_)
elif update_ and not os.path.isdir(butterfly_folder_):
   install_butterfly(update_)
elif os.path.isdir(butterfly_folder_) and butterfly_folder_ not in sys.path:
        sys.path.insert(0, butterfly_folder_)


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