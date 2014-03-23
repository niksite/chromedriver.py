#!/usr/bin/env python
import StringIO
import requests
import os
import os.path
import re
import stat
import sys
import zipfile
import platform
import logging


VERSION_URL = 'http://chromedriver.storage.googleapis.com/LATEST_RELEASE'
DOWNLOAD_URL = 'http://chromedriver.storage.googleapis.com/{0}/' \
               'chromedriver_linux{1}.zip'
NOTES_URL = 'http://chromedriver.storage.googleapis.com/{0}/notes.txt'


try:
    dest = sys.argv[1]
except IndexError:
    logging.error('please, specify an installation path')
    exit(1)

version = requests.get(VERSION_URL).content

target_file = os.path.join(dest, 'chromedriver')

version_file = '{0}.version'.format(target_file)
if os.path.exists(version_file):
    current_version = open(version_file).readline()
    if current_version == version:
        logging.warning('current version of chromedriver is already installed')
        exit()

logging.warning('fetching new {0} version of chromedriver'.format(version))
arch = platform.architecture()[0][:2]
download_url = DOWNLOAD_URL.format(version, arch)
logging.warning('trying url %s' % download_url)
response = requests.get(download_url)
if response.status_code == 200:
    zipfile.ZipFile(
        StringIO.StringIO(
            response.content)
        ).extractall(path=dest)
    all_x = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
    os.chmod(target_file,
             os.stat(target_file).st_mode | all_x)
    open(version_file, 'w').write(version)
    logging.warning('release notes: {0}'.format(NOTES_URL.format(version)))
    release_notes = re.search(
        '(----------ChromeDriver v{0}.*?)----------Chrome'.format(version),
        requests.get(NOTES_URL.format(version)).content,
        re.DOTALL)
    if release_notes and release_notes.group(1):
        logging.warning(release_notes.group(1))
    logging.warning('done')
    exit()
else:
    logging.error('cannot fetch url {0} because of HTTP{1} error'.format(
                  download_url, response.status_code))
