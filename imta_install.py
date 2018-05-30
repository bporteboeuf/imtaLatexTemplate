# -*- coding: utf-8 -*-

#####################################################################
# File Name:        imta_install.py
#
# Description:      Installation Python script for the IMTA LaTeX template.
#
# Note:             /
#
# Limitations:      /
#
# Errors:           None known
#
# Dependencies:     os
#                   platform
#                   subprocess
#                   shutil
#
# Author:           B. Porteboeuf - benoit.porteboeuf@telecom-bretagne.eu
# Contributor:      /
#
# University:       IMT Atlantique, Brest (France)
#
# Environment:      Python 3.6.3
####################################################################
# Revision List:
# Version    Author   Date         	Changes
# 0.1        BP       29.05.2018   	First Draft with support for TeX Live only
# 0.2        BP       30.05.2018   	First draft for MikTeX support
####################################################################

import os,platform,subprocess,shutil


def f_chdir(my_dir):
    if not os.path.isdir(my_dir):
        os.mkdir(my_dir)
    os.chdir(my_dir)
    return

def copy_files(or_dir,template_dir):
    shutil.copy(os.path.join(or_dir, 'imta_core.sty'),template_dir)
    shutil.copy(os.path.join(or_dir, 'imta_extra.sty'),template_dir)
    shutil.copy(os.path.join(or_dir, 'imta_documentation.tex'),template_dir)
    shutil.copy(os.path.join(or_dir, 'imta_logo.pdf'),template_dir)
    print('Template files copied at {}'.format(template_dir))
    return


# First, we need to know if the user is running TeX Live or MikTeX
bashCommand = "pdflatex --version"
output = subprocess.check_output(bashCommand, shell=True)

orDir = os.getcwd()

    
if 'TeX Live' in str(output):
    print('A TeX Live distribution has been found.')
    system = platform.system()
    if system is 'Windows':
        print('A Windows system has been detected.')
        default_dir = '/texlive/'
    elif system is 'Linux':
        print('A Windows system has been detected.')
        default_dir = '/usr/local/texlive'
    else:
        print("System '{}' is not known. Continuing...".format(system))
        default_dir = '/'

    print('Looking for configuration file...')
    # If available, the default root path is used
    if os.path.isdir(default_dir):
        os.chdir(default_dir)
    else:
        os.chdir('/')
    # Then we look for the config file
    for root, dirs, files in os.walk(os.getcwd()):
        if 'texmf.cnf' in files:
            filePath = os.path.join(root,'texmf.cnf')
            print('Configuration file found at {}'.format(filePath))
            break
    if filePath is None:
        print('Warning: no configuration file has been found. Continuing with default settings...')
        filePath = default_dir

    # And now for the actual local texmf folder, which is created if not already there
    os.chdir(os.path.join(root,'..'))
    texmf_dir = os.path.join(os.getcwd(),'texmf-local')
    f_chdir(texmf_dir)
    new_dir = 'tex'
    f_chdir(new_dir)
    new_dir = 'latex'
    f_chdir(new_dir)

    # template files are copied
    new_dir = 'imta'
    f_chdir(new_dir)
    templatePath = os.getcwd()
    copy_files(orDir,templatePath)

    bashCommand = "tlmgr conf auxtrees add {}".format(texmf_dir)
    output = str(subprocess.check_output(bashCommand, shell=True))
   
    print('Configuration file updated')
    print('Done.')


elif 'MikTeX' in str(output):
    print('A MikTeX distribution has been found.') 

    bashCommand = "initexmf --report"
    output = str(subprocess.check_output(bashCommand, shell=True))
    for l in output.split('\n'):
        if 'CommonData' in l:
            r = l.split(': ')
            base_dir = r[1]
            break
    
    texmf_dir = os.path.join(base_dir,'texmf-local')
    os.chdir(texmf_dir)
    new_dir = 'tex'
    f_chdir(new_dir)
    new_dir = 'latex'
    f_chdir(new_dir)
    templatePath = os.getcwd()

    copy_files(orDir,templatePath)

    bashCommand = "initexmf --register-root={}".format(texmf_dir)
    output = str(subprocess.check_output(bashCommand, shell=True))
    print(str(output))
    bashCommand = "initexmf --update-fndb"
    output = str(subprocess.check_output(bashCommand, shell=True))
    print(str(output))

    print('Done.')

else:
    print('Error: Unsupported distribution or setup.')



########## END ########## 
##########################
