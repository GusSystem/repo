# Import des librairies requises
import os
from shutil import *
import gzip
from pydpkg import Dpkg

# Définition des variables

packageDeb = input("Glissez le deb du paquet ici : ").strip()

dp = Dpkg(packageDeb)

if hasattr(dp, 'name'):
    packageName = dp.name
else:
    packageName = dp.package
packageId = dp.package
if hasattr(dp, 'description'):
    packageDescription = dp.description
else:
    packageDescription = "No description provided for this package"
packageLongDescription = "# " + packageName + "\n\n" + packageDescription
packageVersion = dp.version
packageSection = dp.section
packagePreDependencies = ""
if hasattr(dp, 'depends'):
    packageDependencies = dp.depends
else:
    packageDependencies = ""
if hasattr(dp, 'conflicts'):
    packageConflicts = dp.conflicts
else:
    packageConflicts = ""
if hasattr(dp, 'replaces'):
    packageReplaces = dp.replaces
else:
    packageReplaces = ""

path = "Packages/" + packageName

# Création du dossier du paquet
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

# Copie du deb
try:
    copyfile(packageDeb, path + "/" + packageId + ".deb")
except OSError:
    print ("Failed to copy %s " % packageDeb)
else:
    print ("Successfully copied package deb %s " % packageDeb)

# Création du silica_data
try:
    os.mkdir(path + "/silica_data")
except OSError:
    print ("Creation of the directory %s failed" % path + "/silica_data")
else:
    print ("Successfully created the directory %s " % path + "/silica_data")
# Création et écriture de description.md
f = open(path + "/silica_data/description.md", "w")
f.write(packageLongDescription)
f.close()
# Copie du logo
try:
    copyfile("docs/CydiaIcon.png", path + "/silica_data/icon.png")
except OSError:
    print ("Failed to copy logo")
else:
    print ("Successfully copied logo")
# Création et écriture de index.json
f = open(path + "/silica_data/index.json", "w")
f.write('{"bundle_id": "' + packageId + '", "name": "' + packageName + '", "version": "' + packageVersion + '", "tagline": "' + packageDescription + '", "homepage": "https://gussystem.github.io/repo","developer": {"name": "Gus", "email": ""}, "maintainer": {"name": "Gus", "email": ""}, "social": [{"name": "Website", "url": "https://gussystem.github.io/repo"}],"section": "' + packageSection + '", "pre_dependencies": "' + packagePreDependencies + '", "dependencies": "' + packageDependencies + '", "conflicts": "' + packageConflicts + '", "replaces": "' + packageReplaces + '", "provides": "", "other_control": ["Tag: role::enduser", "SomeOtherEntryToControl: True"], "tint": "#72bcd4", "works_min": "6.0", "works_max": "12.5", "featured": "true", "source": "", "changelog": [{"version": "' + packageVersion + '", "changes": "GusSystem Repo"}]}')
f.close()
