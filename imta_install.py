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
# 1.0        BP       29.05.2018   	First Draft with support for TeX Live only
####################################################################

import os,platform,subprocess,shutil


# First, we need to know if the user is running TeX Live or MikTeX
bashCommand = "pdflatex --version"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

orDir = os.getcwd()

if error:
    print(error)
    
if 'TeX Live' in str(output):
    print('A TeX Live distribution has been found.')
    system = platform.system()
    if system is 'Windows':
        print('A Windows system has been detected.')
    elif system is 'Linux':
        print('A Windows system has been detected.')
    else:
        print("Error: System '{}' not supported".format(system))

    print('Looking for configuration file...')
    # If available, the default root path is used
    if os.path.isdir('/texlive/'):
        os.chdir('/texlive/')
    else:
        os.chdir('/')
    # Then we look for the config file
    for root, dirs, files in os.walk(os.getcwd()):
        if 'texmf.cnf' in files:
            filePath = os.path.join(root,'texmf.cnf')
            print('Configuration file found at {}'.format(filePath))
            break
    
    # And now for the actual local texmf folder, which is created if not already there
    os.chdir(os.path.join(root,'..'))
    texmf_dir = os.path.join(os.getcwd(),'texmf-local')
    if not os.path.isdir(texmf_dir):
        os.mkdir(texmf_dir)
    os.chdir(texmf_dir)
    new_dir = 'tex'
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    os.chdir(new_dir)
    new_dir = 'latex'
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    os.chdir(new_dir)

    # template files are copied
    new_dir = 'imta'
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    os.chdir(new_dir)
    templatePath = os.getcwd()
    shutil.copy(os.path.join(orDir, 'imta_core.sty'),templatePath)
    shutil.copy(os.path.join(orDir, 'imta_extra.sty'),templatePath)
    shutil.copy(os.path.join(orDir, 'imta_documentation.tex'),templatePath)
    shutil.copy(os.path.join(orDir, 'imta_logo.pdf'),templatePath)
    print('Copying files at {}'.format(templatePath))
    
    # File is opened and is content is read
    f = open(filePath,'r')
    fc = f.read()
    f.close()

    # We look for the definition of the TEXMFHOME variable
    # if it is not there, we simply append it
    if 'TEXMFHOME' not in fc:
        fc += '\nTEXMFHOME = {}'.format(texmf_dir)
    # otherwise, we just need to add the correct directory
    else:
        # regex should be used here
        lines = fc.split('\n')
        i = 0
        for l in lines:
            if 'TEXMFHOME' in l:
                break
            i += 1
        
        if not texmf_dir in l:
            l = l.split('=')
            r = l[1]; l = l[0]
            rl = r.split('{') 
            if len(rl) == 1:
                r = ' {'+texmf_dir+','+rl[0]+'}'
            else:
                r = rl[0]+texmf_dir+','+rl[1]
            l = '='.join([l,r])
            lines[i] = l
            fc = '\n'.join(lines)

    # File is overwritten
    f = open(filePath,'w')
    f.write(fc)
    f.close()

    print('Configuration file updated')
    print('Done.')


elif 'MikTeX' in str(output):
    print('A MikTeX distribution has been found.') 

    print('No setup scheme has been provided for now.')

else:
    print('Error: Unsupported distribution or setup.')



########## END ########## 
##########################
