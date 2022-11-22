import json
import shutil

import work.fio as fio
import work.scss as scss
import work.action as action

def build():
    configJson = fio.readText('builder-config.json')
    config = json.loads(configJson)

    workDir = config['workDir']
    outDir  = config['outDir']

    scss.compileScss(mode=0)

    replHtml = action.assembleHtmlNoCss(workDir)
    fio.writeText(outDir+'/skin.html', replHtml)

    shutil.copy2(workDir+'/etc/index.xml', outDir)
