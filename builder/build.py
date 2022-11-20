import shutil
import subprocess
import json
import re

import fio

#### Load Config ####
configJson = fio.readText('builder-config.json')
config = json.loads(configJson)

workDir = config['workDir']
outDir  = config['outDir']
cssConfig = config['css']


#### Compile SCSS ####
baseCss = fio.readText(workDir+'/scss/'+cssConfig['baseCss']+'.scss')
cssIncudeList = cssConfig['priority']

for css in cssIncudeList:
    baseCss += fio.readText(workDir+'/scss/'+css+'.scss')

fio.writeText('compile/style.scss', baseCss)


#### Assesmble HTML ####
baseHtml = fio.readText(workDir+'/base.html')

def replaceFunc(match):
    fname = match.group(1)
    return fio.readText(workDir+'/views/'+fname+'.html')

replHtml = re.sub('^\s*\[!(.*)\]$', replaceFunc, baseHtml, 0, re.MULTILINE)
fio.writeText(outDir+'/skin.html', replHtml)


#### Copy files ####
shutil.copy2(workDir+'/etc/index.xml', outDir)
