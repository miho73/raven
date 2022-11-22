import re
from bs4 import BeautifulSoup

import work.fio as fio


"""
Assemble HTML into single file and return for build
"""
def assembleHtmlNoCss(workDir: str):
    baseHtml = fio.readText(workDir+'/base.html')

    def replaceFunc(match):
        fname = match.group(1)
        return fio.readText(workDir+'/views/'+fname+'.html')

    return re.sub('^\s*\[!(.*)\]$', replaceFunc, baseHtml, 0, re.MULTILINE)


"""
Assemble HTML into single file and return for export
"""
def assembleHtml(workDir: str, css: str):
    baseHtml = fio.readText('raven/res/export.html')

    def replaceFunc(match):
        fname = match.group(1)
        return fio.readText(workDir+'/views/'+fname+'.html')

    html = re.sub('^\s*\[!(.*)\]$', replaceFunc, baseHtml, 0, re.MULTILINE)
    return re.sub('^\s*\{!(.*)\}$', '<style>'+css+'</style>', html, 0, re.MULTILINE)
