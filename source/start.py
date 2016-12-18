# -*- coding: utf-8 -*-
#   ===================================
#       kasetophon sto termatiko
#   ===================================
#              start
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================
from subprocess import call
from termcolor import colored
import lang
def SetMPV():
    call(["mpsyt", "set", "player", "mpv,q"])
    call(["clear"])

def logo():
    call(["clear"])
    logo=   '                                   _                            \n'\
            '                                  | |                           \n'\
            '   _  ____  ______ ___ ___ ___   _| |_   __   __  _  _____      \n'\
            '  | |/ /  \/ /  ._) __|   ) _ \ /     \ / / _ \ \| |/ / _ \     \n'\
            '  |   < ()  < () )> _) | ( (_) | (| |) ) |_/ \_| | / ( (_) )    \n'\
            '  |_|\_\__/\_\__/ \___) \_)___/ \_   _/ \___^___/|__/ \___/     \n'\
            '                                  | |                           \n'\
            '                                  |_|                           '
    logo1=  '  ____ ___ ___    ___ ___  ___  _   _  __  _____ _  _  _____    \n'\
            ' /  ._|   ) _ \  (   ) __)/ _ \| | | |/  \/ (   ) || |/ / _ \   \n'\
            '( () ) | ( (_) )  | |> _)| |_) ) |_| ( ()  < | || ||   < (_) )  \n'\
            ' \__/   \_)___/    \_)___)  __/| ._,_|\__/\_\ \_)\_)_|\_\___/   \n'\
            '                         | |   | |                              \n'\
            '                         |_|   |_|                              '
    logo2 = '================================================================\n\n'
    print colored(logo,"magenta")
    print colored(logo1,"cyan")
    print colored(logo2,"blue")
    tmp = input('Choose language: "1" for English or "2" for Greek\n>>> ')
    return tmp
