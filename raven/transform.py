import json
import sys
import re
from bs4 import BeautifulSoup

import work.scss as scss
import work.fio as fio
import work.action as action

def export():
    configJson = fio.readText('builder-config.json')
    config = json.loads(configJson)

    workDir = config['workDir']

    scss.compileScss(mode=1)
    css = fio.readText('compile/style.css')

    html = action.assembleHtml(workDir, css)
    fio.writeText('export.html', html)

def imp(imptPath):
    configJson = fio.readText('builder-config.json')
    config = json.loads(configJson)
    importConfig = config['import']

    workDir = config['workDir']


    impt = fio.readText(imptPath)
    iHtml = BeautifulSoup(impt, 'html.parser')
    
    # 1. remove RavenRemove
    for remove in iHtml.select('RavenRemove'):
        remove.decompose()

    # 2. add tistory tag
    replaces = importConfig['cover']

    for replace in replaces:
        occur = findByRid(iHtml, replace)
        toTag = replaces[replace]
        if occur != None:
            occur.replace_with(BeautifulSoup('<'+toTag+'>\n'+str(occur)+'\n</'+toTag+'>', 'html.parser'))

    # 3. change src
    occurs = iHtml.select('img')
    for occur in occurs:
        oSrc = re.findall('"\.\/'+workDir+'\/resources\/(.*)"', str(occur))
        if(len(oSrc) != 0):
            occur['src'] = './images/'+oSrc[0]

    # 4. separate into parts
    try:
        header = findByRid(iHtml, 'header')
        homeCover = findByRid(iHtml, 'home-cover').parent
        article = findByRid(iHtml, 'article').parent
        footer = findByRid(iHtml, 'footer')
        lst = findByRid(iHtml, 'list').parent

        # 4. put into individual files
        fio.writeText(workDir+'/views/navigation.html', str(header))
        fio.writeText(workDir+'/views/main-cover.html', str(homeCover))
        fio.writeText(workDir+'/views/article.html', str(article))
        fio.writeText(workDir+'/views/footer.html', str(footer))
        fio.writeText(workDir+'/views/list.html', str(lst))
    except IOError:
        print('Cannot write html to file.', file=sys.std)
    except RuntimeError:
        print("Tag(s) specified in config file was not found", file=sys.stderr)

    # print result
    print('Successfully imported \'',imptPath,'\'.', sep='')

def findByRid(html: BeautifulSoup, rid: str):
    fnd = html.select_one('[rid=\''+rid+'\']')
    return fnd