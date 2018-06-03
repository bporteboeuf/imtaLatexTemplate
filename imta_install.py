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
#                   shutil
#                   subprocess
#                   sys
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
# 1.0        BP       31.05.2018    Some bugs fixed with MikTeX support
####################################################################

import os
import platform
import shutil
import subprocess
import sys


def f_chdir(my_dir):
    """f_chdir(my_dir) forces to change directory by creating it if needed
    (only 1 level can be created at a time)
    """
    if not os.path.isdir(my_dir):
        os.mkdir(my_dir)
    os.chdir(my_dir)

    
def copy_source_files(or_dir,template_dir):
    """copy_source_files(or_dir,template_dir) copies the source files from or_dir
    to template_dir
    """    
    def copy_sc(file,fpA,fpB):
        fpA = os.path.join(fpA,file)
        if os.path.isfile(fpA):
            shutil.copy(fpA,fpB)
        else:
            raise Exception("Error: File '{}' is missing".format(file))
        return
    
    copy_sc('imta_core.sty',or_dir,template_dir)
    copy_sc('imta_extra.sty',or_dir,template_dir)
    copy_sc('imta_logo.pdf',or_dir,template_dir)
    copy_sc('imta_documentation.tex',or_dir,template_dir)
    print('Template files copied at {}'.format(template_dir))
    
    
def _input(msg):
    """_input(msg) prints the given message and returns the user input
    supports both python 2 and 3
    """
    if sys.version_info.major >= 3:
        ans = input(msg)
    elif sys.version_info.major == 2:
        ans = raw_input(msg)
    else:
        raise Exception("Unsupported python version. Please upgrade to python 2 or higher.")

    return ans
    
    
def texlive_install():
    """texlive_install() is the complete template installation scheme for TeX Live on both
    Windows and Linux
    """
    orDir = os.getcwd()
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
    copy_source_files(orDir,templatePath)

    
    output = subprocess.check_output("tlmgr conf auxtrees add {}".format(texmf_dir), 
                                     shell=True).decode('utf-8')
   
    print('Configuration file updated')
    
    
def miktex_install():
    """miktex_install is the complete template installation scheme for MikTeX on Windows
    """
    orDir = os.getcwd()
    output = subprocess.check_output("initexmf --report", shell=True).decode('utf-8')
    for l in output.split('\n'):
        if 'CommonInstall' in l:
            r = l.split('CommonInstall: ')
            base_dir = r[1]
            base_dir = base_dir.split('\r')
            base_dir = base_dir[0]
            break
    
    texmfSuccess = True
    texmf_dir = os.path.join(base_dir,'texmf-local')
    try:
        f_chdir(texmf_dir)
    except Exception as e:
        print(e)
        default_dir = os.path.join(orDir,'texmf-local')
        ans = _input('Continuing with default folder <{}>? (y/n)'.format(default_dir))
        if ans == 'y':
            f_chdir(default_dir)
        else:
            print('Aborting procedure...')
            texmfSuccess = False
            
    if texmfSuccess:
        new_dir = 'tex'
        f_chdir(new_dir)
        new_dir = 'latex'
        f_chdir(new_dir)
        templatePath = os.getcwd()

        copy_source_files(orDir,templatePath)

        output = subprocess.check_output("initexmf --register-root={}".format(texmf_dir), 
                                         shell=True).decode('utf-8')
        output = subprocess.check_output("initexmf --update-fndb", shell=True).decode('utf-8')
        
        print('Configuration file updated.')



# Actual main function
if __name__ == '__main__':
    output = subprocess.check_output("pdflatex --version", shell=True).decode('utf-8')
        
    if 'TeX Live' in output:
        print('A TeX Live distribution has been found.')
        texlive_install()
        print('Done.')

    elif 'MiKTeX' in output:
        print('A MikTeX distribution has been found.') 
        miktex_install()
        print('Done.')

    else:
        print('Error: Unsupported distribution or setup.')
        raise Exception



########## END ########## 
##########################
