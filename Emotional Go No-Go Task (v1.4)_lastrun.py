#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on August 18, 2025, at 18:16
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from Initialise_Eyetracker
import pylink
import os
from psychopy import gui, core
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy

# === Prompt for filename ===
while True:
    dlg = gui.Dlg("Enter EDF filename")
    dlg.addField("Filename (≤8 chars)", "TEST")
    ok_data = dlg.show()
    if not dlg.OK:
        core.quit()
    edf_fname = ok_data[0].split(".")[0]
    if len(edf_fname) <= 8 and edf_fname.isalnum():
        break

edf_file = edf_fname + ".EDF"
results_dir = "eyetracker_data"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'Go No-Go Task'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': 'P000',
    'Study Name': '',
    'Task Version (required to run)': '1 or 2',
    'PRE/POST': 'Pre or Post',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1680, 1050]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\PERLadmin\\Desktop\\DOREA_Task_Battery\\AGNG\\Emotional Go No-Go Task (v1.4)_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[-0.3000, -0.3000, -0.3000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-0.3000, -0.3000, -0.3000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('First_Cont_Text') is None:
        # initialise First_Cont_Text
        First_Cont_Text = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='First_Cont_Text',
        )
    if deviceManager.getDevice('EmotionTaskInstructions1') is None:
        # initialise EmotionTaskInstructions1
        EmotionTaskInstructions1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='EmotionTaskInstructions1',
        )
    if deviceManager.getDevice('PressCont2') is None:
        # initialise PressCont2
        PressCont2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='PressCont2',
        )
    if deviceManager.getDevice('PressCont') is None:
        # initialise PressCont
        PressCont = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='PressCont',
        )
    if deviceManager.getDevice('Instr_Cont') is None:
        # initialise Instr_Cont
        Instr_Cont = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Instr_Cont',
        )
    if deviceManager.getDevice('InstrContPress') is None:
        # initialise InstrContPress
        InstrContPress = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='InstrContPress',
        )
    if deviceManager.getDevice('key_resp_7') is None:
        # initialise key_resp_7
        key_resp_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_7',
        )
    if deviceManager.getDevice('Pract') is None:
        # initialise Pract
        Pract = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Pract',
        )
    if deviceManager.getDevice('key_resp_8') is None:
        # initialise key_resp_8
        key_resp_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_8',
        )
    if deviceManager.getDevice('PressCalibKey') is None:
        # initialise PressCalibKey
        PressCalibKey = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='PressCalibKey',
        )
    if deviceManager.getDevice('key_resp_6') is None:
        # initialise key_resp_6
        key_resp_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_6',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('Calib_keys_1') is None:
        # initialise Calib_keys_1
        Calib_keys_1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Calib_keys_1',
        )
    if deviceManager.getDevice('Recalib_keys_2') is None:
        # initialise Recalib_keys_2
        Recalib_keys_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Recalib_keys_2',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Hard_Script" ---
    # Run 'Begin Experiment' code from Disable_Mouse
    win.setMouseVisible(False)
    # Run 'Begin Experiment' code from Block_Set
    BlockNo = 1
    PractNo = 1
    # Run 'Begin Experiment' code from Task_Ver_Set
    # Get and clean version input
    TaskVersion = str(expInfo.get('Task Version (required to run)', '')).strip()
    
    # Choose path based on version
    if TaskVersion == '1':
        basePath = 'ParentConditions/'
    elif TaskVersion == '2':
        basePath = 'ParentConditions/'
    else:
        # show error and exit
        errMsg = visual.TextStim(
            win=win,
            text="Warning: Must enter a valid task version number\n(i.e., 1, or 2). \n\n Press any key to quit.",
            color='black',
            height=0.025
        )
        errMsg.draw()
        win.flip()
        event.waitKeys()
        core.quit()
    
    # Construct filename
    VersionSelection = basePath + f'ConditionsMaster_v{TaskVersion}.xlsx'
    # Run 'Begin Experiment' code from Bgrd_Box
    grayBox = visual.rect.Rect(win, width=0.8, height=0.8, units='', lineWidth=0, lineColor=None, lineColorSpace=None, fillColor='grey', fillColorSpace=None, pos=(0, 0))
    
    # --- Initialize components for Routine "VersionNoDisplay" ---
    Version_Display_Text = visual.TextStim(win=win, name='Version_Display_Text',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.0275, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    First_Cont_Text = keyboard.Keyboard(deviceName='First_Cont_Text')
    
    # --- Initialize components for Routine "EmotionTaskInstructions" ---
    Instructions_Text_1 = visual.TextStim(win=win, name='Instructions_Text_1',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    EmotionTaskInstructions1 = keyboard.Keyboard(deviceName='EmotionTaskInstructions1')
    
    # --- Initialize components for Routine "EmotionalTaskInstructions2" ---
    Instructions_Text_2 = visual.TextStim(win=win, name='Instructions_Text_2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    PressCont2 = keyboard.Keyboard(deviceName='PressCont2')
    
    # --- Initialize components for Routine "EmotionalTaskInstructions3" ---
    Instructions_Text_3 = visual.TextStim(win=win, name='Instructions_Text_3',
        text="Rules are given at the start and change throughout.\n\nThe experiment will pause when instructed with a new rule.\n\n\nPlease press 'spacebar' to continue.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    PressCont = keyboard.Keyboard(deviceName='PressCont')
    
    # --- Initialize components for Routine "EmotionalTaskInstructions2p5" ---
    Instructions_Text_2p5 = visual.TextStim(win=win, name='Instructions_Text_2p5',
        text='Between images, you will see a cross like this:',
        font='Arial',
        pos=(0, 0.2), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Cross_demonstration = visual.TextStim(win=win, name='Cross_demonstration',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.175, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Focus_Instuctions = visual.TextStim(win=win, name='Focus_Instuctions',
        text="When it appears, please focus on it.\n\n\nPlease press 'spacebar' to continue.",
        font='Arial',
        pos=(0, -0.2), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    Instr_Cont = keyboard.Keyboard(deviceName='Instr_Cont')
    
    # --- Initialize components for Routine "PrePractice_Text" ---
    LastInstrText = visual.TextStim(win=win, name='LastInstrText',
        text="When you have completed 50% of the experiment, \nthere will be a break period.\n\nYou will begin practice on the next screen.\n\n\nPlease press 'spacebar' to begin practice.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    InstrContPress = keyboard.Keyboard(deviceName='InstrContPress')
    
    # --- Initialize components for Routine "EPracticeInstructions2" ---
    Practice_Rule_Set = visual.TextStim(win=win, name='Practice_Rule_Set',
        text='',
        font='Arial',
        pos=(0, -0.10), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color=[0.1686, -0.6000, -0.5608], colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    Continue_Pract_Text = visual.TextStim(win=win, name='Continue_Pract_Text',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    Practice_Block_Number_Text = visual.TextStim(win=win, name='Practice_Block_Number_Text',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    Practice_Block_Text = visual.TextStim(win=win, name='Practice_Block_Text',
        text='Practice block:',
        font='Arial',
        pos=(-0.0590, 0.05), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    Practice_Block_Text_End = visual.TextStim(win=win, name='Practice_Block_Text_End',
        text='of 2',
        font='Arial',
        pos=(0.095, 0.05), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "EPracticeISI" ---
    EPracticeISIMarker = visual.TextStim(win=win, name='EPracticeISIMarker',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "EPracticeTrial" ---
    Pract = keyboard.Keyboard(deviceName='Pract')
    PracticeFace = visual.ImageStim(
        win=win,
        name='PracticeFace', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(0.3, 0.125),
        color=[1, 1, 1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    ColourPractice = visual.ImageStim(
        win=win,
        name='ColourPractice', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=1.0,
        color=[1, 1, 1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "Blank_3" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "PracticeFeedbackBlock" ---
    Practice_Feedback = visual.TextStim(win=win, name='Practice_Feedback',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Add" ---
    
    # --- Initialize components for Routine "EndPracticeEndInstructions" ---
    EndOfPractice = visual.TextStim(win=win, name='EndOfPractice',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_8 = keyboard.Keyboard(deviceName='key_resp_8')
    
    # --- Initialize components for Routine "Pre_Calib_Instructions" ---
    PreCalib_Text = visual.TextStim(win=win, name='PreCalib_Text',
        text="On the next screen, you will begin the eyetracker calibration.\n\n\nPress 'spacebar' to continue.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    PressCalibKey = keyboard.Keyboard(deviceName='PressCalibKey')
    
    # --- Initialize components for Routine "EyeT_Calib" ---
    
    # --- Initialize components for Routine "EyeT_DriftCheck" ---
    
    # --- Initialize components for Routine "RealTaskPreInstructions" ---
    Begin_Real_Task_Text = visual.TextStim(win=win, name='Begin_Real_Task_Text',
        text="You will now begin the real task. \n\nPlease press 'spacebar' to continue.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    
    # --- Initialize components for Routine "Instructions_2" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color=[0.1686, -0.6000, -0.5608], colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    text_3 = visual.TextStim(win=win, name='text_3',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    TaskBlock = visual.TextStim(win=win, name='TaskBlock',
        text='',
        font='Arial',
        pos=(-0.07, 0.05), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    BlockNo1 = visual.TextStim(win=win, name='BlockNo1',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=1.0, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    OfBlock = visual.TextStim(win=win, name='OfBlock',
        text='',
        font='Arial',
        pos=(0.07, 0.05), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "Begin_Rec" ---
    
    # --- Initialize components for Routine "ISI_2" ---
    Pre_ISI_Text = visual.TextStim(win=win, name='Pre_ISI_Text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.18, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Blank_4" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "EmotTrial" ---
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    FaceSet = visual.ImageStim(
        win=win,
        name='FaceSet', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=1.0,
        color=[1, 1, 1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    Colour = visual.ImageStim(
        win=win,
        name='Colour', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=1.0,
        color=[1, 1, 1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "Blank_2" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "ISI_3" ---
    Post_ISI_Text = visual.TextStim(win=win, name='Post_ISI_Text',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.18, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "End_Record" ---
    
    # --- Initialize components for Routine "Add2" ---
    
    # --- Initialize components for Routine "EndBlock" ---
    EndBlockText = visual.TextStim(win=win, name='EndBlockText',
        text='End of block.',
        font='Arial',
        pos=(0, 0.05), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    BreakText2 = visual.TextStim(win=win, name='BreakText2',
        text='',
        font='Arial',
        pos=(0, -0.10), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    PressToContinue = visual.TextStim(win=win, name='PressToContinue',
        text='',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "Recalib_Text" ---
    Break_Text = visual.TextStim(win=win, name='Break_Text',
        text='This is an extended rest period for three minutes.\n\nPlease relax; you may exit the eyetracker.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "Recalib_Text_2" ---
    End_Break_Text = visual.TextStim(win=win, name='End_Break_Text',
        text="The break period has ended. Please call the researcher.\n\nYou will begin recalibration on the next screen.\n\n\nPlease press 'spacebar' to continue.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Calib_keys_1 = keyboard.Keyboard(deviceName='Calib_keys_1')
    
    # --- Initialize components for Routine "Recalib" ---
    
    # --- Initialize components for Routine "Drift_Check" ---
    
    # --- Initialize components for Routine "End_Calib_Text" ---
    Recalib_Text_3 = visual.TextStim(win=win, name='Recalib_Text_3',
        text="The recalibration has been completed.\n\nYou will return to the task on the next screen.\n\n\nPlease press 'spacebar' to continue.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Recalib_keys_2 = keyboard.Keyboard(deviceName='Recalib_keys_2')
    
    # --- Initialize components for Routine "EndEmotionTask" ---
    End_Text = visual.TextStim(win=win, name='End_Text',
        text="End of test.\n\nThank you for participating. \n\nPlease inform the researcher of your completion.\n\nPress 'escape' to close.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.025, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Hard_Script" ---
    # create an object to store info about Routine Hard_Script
    Hard_Script = data.Routine(
        name='Hard_Script',
        components=[],
    )
    Hard_Script.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Initialise_Eyetracker
    # === Connect to EyeLink ===
    try:
        el_tracker = pylink.EyeLink("100.1.1.1")
    except:
        el_tracker = pylink.EyeLink(None)  # Dummy Mode fallback
    
    el_tracker.setOfflineMode()
    el_tracker.openDataFile(edf_file)
    
    # === Screen and calibration setup ===
    scn_w, scn_h = win.size
    el_tracker.sendCommand(f"screen_pixel_coords = 0 0 {scn_w - 1} {scn_h - 1}")
    el_tracker.sendMessage(f"DISPLAY_COORDS 0 0 {scn_w - 1} {scn_h - 1}")
    genv = EyeLinkCoreGraphicsPsychoPy(el_tracker, win)
    pylink.openGraphicsEx(genv)
    
    # store start times for Hard_Script
    Hard_Script.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Hard_Script.tStart = globalClock.getTime(format='float')
    Hard_Script.status = STARTED
    thisExp.addData('Hard_Script.started', Hard_Script.tStart)
    Hard_Script.maxDuration = None
    # keep track of which components have finished
    Hard_ScriptComponents = Hard_Script.components
    for thisComponent in Hard_Script.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Hard_Script" ---
    Hard_Script.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Hard_Script.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Hard_Script.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Hard_Script" ---
    for thisComponent in Hard_Script.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Hard_Script
    Hard_Script.tStop = globalClock.getTime(format='float')
    Hard_Script.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Hard_Script.stopped', Hard_Script.tStop)
    thisExp.nextEntry()
    # the Routine "Hard_Script" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "VersionNoDisplay" ---
    # create an object to store info about Routine VersionNoDisplay
    VersionNoDisplay = data.Routine(
        name='VersionNoDisplay',
        components=[Version_Display_Text, First_Cont_Text],
    )
    VersionNoDisplay.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Version_Text
    VersionT = ("This is the AGNG task version "+"'"+ TaskVersion + "'."
    +"\n \n \n Press 'spacebar' to continue to the instructions.")
    
    Version_Display_Text.setText(VersionT)
    # create starting attributes for First_Cont_Text
    First_Cont_Text.keys = []
    First_Cont_Text.rt = []
    _First_Cont_Text_allKeys = []
    # store start times for VersionNoDisplay
    VersionNoDisplay.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    VersionNoDisplay.tStart = globalClock.getTime(format='float')
    VersionNoDisplay.status = STARTED
    thisExp.addData('VersionNoDisplay.started', VersionNoDisplay.tStart)
    VersionNoDisplay.maxDuration = None
    # keep track of which components have finished
    VersionNoDisplayComponents = VersionNoDisplay.components
    for thisComponent in VersionNoDisplay.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "VersionNoDisplay" ---
    VersionNoDisplay.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Version_Display_Text* updates
        
        # if Version_Display_Text is starting this frame...
        if Version_Display_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Version_Display_Text.frameNStart = frameN  # exact frame index
            Version_Display_Text.tStart = t  # local t and not account for scr refresh
            Version_Display_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Version_Display_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Version_Display_Text.started')
            # update status
            Version_Display_Text.status = STARTED
            Version_Display_Text.setAutoDraw(True)
        
        # if Version_Display_Text is active this frame...
        if Version_Display_Text.status == STARTED:
            # update params
            pass
        
        # *First_Cont_Text* updates
        waitOnFlip = False
        
        # if First_Cont_Text is starting this frame...
        if First_Cont_Text.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            First_Cont_Text.frameNStart = frameN  # exact frame index
            First_Cont_Text.tStart = t  # local t and not account for scr refresh
            First_Cont_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(First_Cont_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'First_Cont_Text.started')
            # update status
            First_Cont_Text.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(First_Cont_Text.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(First_Cont_Text.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if First_Cont_Text.status == STARTED and not waitOnFlip:
            theseKeys = First_Cont_Text.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _First_Cont_Text_allKeys.extend(theseKeys)
            if len(_First_Cont_Text_allKeys):
                First_Cont_Text.keys = _First_Cont_Text_allKeys[-1].name  # just the last key pressed
                First_Cont_Text.rt = _First_Cont_Text_allKeys[-1].rt
                First_Cont_Text.duration = _First_Cont_Text_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Box1
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            VersionNoDisplay.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VersionNoDisplay.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "VersionNoDisplay" ---
    for thisComponent in VersionNoDisplay.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for VersionNoDisplay
    VersionNoDisplay.tStop = globalClock.getTime(format='float')
    VersionNoDisplay.tStopRefresh = tThisFlipGlobal
    thisExp.addData('VersionNoDisplay.stopped', VersionNoDisplay.tStop)
    thisExp.nextEntry()
    # the Routine "VersionNoDisplay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "EmotionTaskInstructions" ---
    # create an object to store info about Routine EmotionTaskInstructions
    EmotionTaskInstructions = data.Routine(
        name='EmotionTaskInstructions',
        components=[Instructions_Text_1, EmotionTaskInstructions1],
    )
    EmotionTaskInstructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    Instructions_Text_1.setText("During this task, images appear \nonscreen. Images appear for a short\nperiod of time (450ms). \n\nAt times, you must press 'spacebar' while \nimages appear. Failing to do so leads to an \nincorrect result (miss).\n\n\nPlease press 'spacebar' to continue.")
    Instructions_Text_1.setHeight(0.025)
    # create starting attributes for EmotionTaskInstructions1
    EmotionTaskInstructions1.keys = []
    EmotionTaskInstructions1.rt = []
    _EmotionTaskInstructions1_allKeys = []
    # store start times for EmotionTaskInstructions
    EmotionTaskInstructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EmotionTaskInstructions.tStart = globalClock.getTime(format='float')
    EmotionTaskInstructions.status = STARTED
    thisExp.addData('EmotionTaskInstructions.started', EmotionTaskInstructions.tStart)
    EmotionTaskInstructions.maxDuration = None
    # keep track of which components have finished
    EmotionTaskInstructionsComponents = EmotionTaskInstructions.components
    for thisComponent in EmotionTaskInstructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EmotionTaskInstructions" ---
    EmotionTaskInstructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_Text_1* updates
        
        # if Instructions_Text_1 is starting this frame...
        if Instructions_Text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Text_1.frameNStart = frameN  # exact frame index
            Instructions_Text_1.tStart = t  # local t and not account for scr refresh
            Instructions_Text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Text_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_Text_1.started')
            # update status
            Instructions_Text_1.status = STARTED
            Instructions_Text_1.setAutoDraw(True)
        
        # if Instructions_Text_1 is active this frame...
        if Instructions_Text_1.status == STARTED:
            # update params
            pass
        
        # *EmotionTaskInstructions1* updates
        waitOnFlip = False
        
        # if EmotionTaskInstructions1 is starting this frame...
        if EmotionTaskInstructions1.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            EmotionTaskInstructions1.frameNStart = frameN  # exact frame index
            EmotionTaskInstructions1.tStart = t  # local t and not account for scr refresh
            EmotionTaskInstructions1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EmotionTaskInstructions1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EmotionTaskInstructions1.started')
            # update status
            EmotionTaskInstructions1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(EmotionTaskInstructions1.clock.reset)  # t=0 on next screen flip
        if EmotionTaskInstructions1.status == STARTED and not waitOnFlip:
            theseKeys = EmotionTaskInstructions1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _EmotionTaskInstructions1_allKeys.extend(theseKeys)
            if len(_EmotionTaskInstructions1_allKeys):
                EmotionTaskInstructions1.keys = _EmotionTaskInstructions1_allKeys[-1].name  # just the last key pressed
                EmotionTaskInstructions1.rt = _EmotionTaskInstructions1_allKeys[-1].rt
                EmotionTaskInstructions1.duration = _EmotionTaskInstructions1_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Box2
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EmotionTaskInstructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmotionTaskInstructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EmotionTaskInstructions" ---
    for thisComponent in EmotionTaskInstructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EmotionTaskInstructions
    EmotionTaskInstructions.tStop = globalClock.getTime(format='float')
    EmotionTaskInstructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EmotionTaskInstructions.stopped', EmotionTaskInstructions.tStop)
    thisExp.nextEntry()
    # the Routine "EmotionTaskInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "EmotionalTaskInstructions2" ---
    # create an object to store info about Routine EmotionalTaskInstructions2
    EmotionalTaskInstructions2 = data.Routine(
        name='EmotionalTaskInstructions2',
        components=[Instructions_Text_2, PressCont2],
    )
    EmotionalTaskInstructions2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    Instructions_Text_2.setText("The images will have different features \n(eyes or squares). You only need to focus \non the colour of the image.\n\nYou need to press 'spacebar' for most images. \nBut at times, you must withold pressing 'spacebar'. \n\nYou will be instructed how to respond to images by rules.\n\n\nPlease press 'spacebar' to continue.")
    Instructions_Text_2.setHeight(0.025)
    # create starting attributes for PressCont2
    PressCont2.keys = []
    PressCont2.rt = []
    _PressCont2_allKeys = []
    # store start times for EmotionalTaskInstructions2
    EmotionalTaskInstructions2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EmotionalTaskInstructions2.tStart = globalClock.getTime(format='float')
    EmotionalTaskInstructions2.status = STARTED
    thisExp.addData('EmotionalTaskInstructions2.started', EmotionalTaskInstructions2.tStart)
    EmotionalTaskInstructions2.maxDuration = None
    # keep track of which components have finished
    EmotionalTaskInstructions2Components = EmotionalTaskInstructions2.components
    for thisComponent in EmotionalTaskInstructions2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EmotionalTaskInstructions2" ---
    EmotionalTaskInstructions2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_Text_2* updates
        
        # if Instructions_Text_2 is starting this frame...
        if Instructions_Text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Text_2.frameNStart = frameN  # exact frame index
            Instructions_Text_2.tStart = t  # local t and not account for scr refresh
            Instructions_Text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_Text_2.started')
            # update status
            Instructions_Text_2.status = STARTED
            Instructions_Text_2.setAutoDraw(True)
        
        # if Instructions_Text_2 is active this frame...
        if Instructions_Text_2.status == STARTED:
            # update params
            pass
        
        # *PressCont2* updates
        waitOnFlip = False
        
        # if PressCont2 is starting this frame...
        if PressCont2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            PressCont2.frameNStart = frameN  # exact frame index
            PressCont2.tStart = t  # local t and not account for scr refresh
            PressCont2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressCont2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PressCont2.started')
            # update status
            PressCont2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PressCont2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PressCont2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PressCont2.status == STARTED and not waitOnFlip:
            theseKeys = PressCont2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _PressCont2_allKeys.extend(theseKeys)
            if len(_PressCont2_allKeys):
                PressCont2.keys = _PressCont2_allKeys[-1].name  # just the last key pressed
                PressCont2.rt = _PressCont2_allKeys[-1].rt
                PressCont2.duration = _PressCont2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Box3
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EmotionalTaskInstructions2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmotionalTaskInstructions2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EmotionalTaskInstructions2" ---
    for thisComponent in EmotionalTaskInstructions2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EmotionalTaskInstructions2
    EmotionalTaskInstructions2.tStop = globalClock.getTime(format='float')
    EmotionalTaskInstructions2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EmotionalTaskInstructions2.stopped', EmotionalTaskInstructions2.tStop)
    thisExp.nextEntry()
    # the Routine "EmotionalTaskInstructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "EmotionalTaskInstructions3" ---
    # create an object to store info about Routine EmotionalTaskInstructions3
    EmotionalTaskInstructions3 = data.Routine(
        name='EmotionalTaskInstructions3',
        components=[Instructions_Text_3, PressCont],
    )
    EmotionalTaskInstructions3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for PressCont
    PressCont.keys = []
    PressCont.rt = []
    _PressCont_allKeys = []
    # store start times for EmotionalTaskInstructions3
    EmotionalTaskInstructions3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EmotionalTaskInstructions3.tStart = globalClock.getTime(format='float')
    EmotionalTaskInstructions3.status = STARTED
    thisExp.addData('EmotionalTaskInstructions3.started', EmotionalTaskInstructions3.tStart)
    EmotionalTaskInstructions3.maxDuration = None
    # keep track of which components have finished
    EmotionalTaskInstructions3Components = EmotionalTaskInstructions3.components
    for thisComponent in EmotionalTaskInstructions3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EmotionalTaskInstructions3" ---
    EmotionalTaskInstructions3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_Text_3* updates
        
        # if Instructions_Text_3 is starting this frame...
        if Instructions_Text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Text_3.frameNStart = frameN  # exact frame index
            Instructions_Text_3.tStart = t  # local t and not account for scr refresh
            Instructions_Text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_Text_3.started')
            # update status
            Instructions_Text_3.status = STARTED
            Instructions_Text_3.setAutoDraw(True)
        
        # if Instructions_Text_3 is active this frame...
        if Instructions_Text_3.status == STARTED:
            # update params
            pass
        
        # *PressCont* updates
        waitOnFlip = False
        
        # if PressCont is starting this frame...
        if PressCont.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            PressCont.frameNStart = frameN  # exact frame index
            PressCont.tStart = t  # local t and not account for scr refresh
            PressCont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressCont, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PressCont.started')
            # update status
            PressCont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PressCont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PressCont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PressCont.status == STARTED and not waitOnFlip:
            theseKeys = PressCont.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _PressCont_allKeys.extend(theseKeys)
            if len(_PressCont_allKeys):
                PressCont.keys = _PressCont_allKeys[-1].name  # just the last key pressed
                PressCont.rt = _PressCont_allKeys[-1].rt
                PressCont.duration = _PressCont_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Box4
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EmotionalTaskInstructions3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmotionalTaskInstructions3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EmotionalTaskInstructions3" ---
    for thisComponent in EmotionalTaskInstructions3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EmotionalTaskInstructions3
    EmotionalTaskInstructions3.tStop = globalClock.getTime(format='float')
    EmotionalTaskInstructions3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EmotionalTaskInstructions3.stopped', EmotionalTaskInstructions3.tStop)
    thisExp.nextEntry()
    # the Routine "EmotionalTaskInstructions3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "EmotionalTaskInstructions2p5" ---
    # create an object to store info about Routine EmotionalTaskInstructions2p5
    EmotionalTaskInstructions2p5 = data.Routine(
        name='EmotionalTaskInstructions2p5',
        components=[Instructions_Text_2p5, Cross_demonstration, Focus_Instuctions, Instr_Cont],
    )
    EmotionalTaskInstructions2p5.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Instr_Cont
    Instr_Cont.keys = []
    Instr_Cont.rt = []
    _Instr_Cont_allKeys = []
    # store start times for EmotionalTaskInstructions2p5
    EmotionalTaskInstructions2p5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EmotionalTaskInstructions2p5.tStart = globalClock.getTime(format='float')
    EmotionalTaskInstructions2p5.status = STARTED
    thisExp.addData('EmotionalTaskInstructions2p5.started', EmotionalTaskInstructions2p5.tStart)
    EmotionalTaskInstructions2p5.maxDuration = None
    # keep track of which components have finished
    EmotionalTaskInstructions2p5Components = EmotionalTaskInstructions2p5.components
    for thisComponent in EmotionalTaskInstructions2p5.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EmotionalTaskInstructions2p5" ---
    EmotionalTaskInstructions2p5.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_Text_2p5* updates
        
        # if Instructions_Text_2p5 is starting this frame...
        if Instructions_Text_2p5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Text_2p5.frameNStart = frameN  # exact frame index
            Instructions_Text_2p5.tStart = t  # local t and not account for scr refresh
            Instructions_Text_2p5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Text_2p5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_Text_2p5.started')
            # update status
            Instructions_Text_2p5.status = STARTED
            Instructions_Text_2p5.setAutoDraw(True)
        
        # if Instructions_Text_2p5 is active this frame...
        if Instructions_Text_2p5.status == STARTED:
            # update params
            pass
        
        # *Cross_demonstration* updates
        
        # if Cross_demonstration is starting this frame...
        if Cross_demonstration.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cross_demonstration.frameNStart = frameN  # exact frame index
            Cross_demonstration.tStart = t  # local t and not account for scr refresh
            Cross_demonstration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross_demonstration, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Cross_demonstration.started')
            # update status
            Cross_demonstration.status = STARTED
            Cross_demonstration.setAutoDraw(True)
        
        # if Cross_demonstration is active this frame...
        if Cross_demonstration.status == STARTED:
            # update params
            pass
        
        # *Focus_Instuctions* updates
        
        # if Focus_Instuctions is starting this frame...
        if Focus_Instuctions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Focus_Instuctions.frameNStart = frameN  # exact frame index
            Focus_Instuctions.tStart = t  # local t and not account for scr refresh
            Focus_Instuctions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Focus_Instuctions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Focus_Instuctions.started')
            # update status
            Focus_Instuctions.status = STARTED
            Focus_Instuctions.setAutoDraw(True)
        
        # if Focus_Instuctions is active this frame...
        if Focus_Instuctions.status == STARTED:
            # update params
            pass
        
        # *Instr_Cont* updates
        waitOnFlip = False
        
        # if Instr_Cont is starting this frame...
        if Instr_Cont.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            Instr_Cont.frameNStart = frameN  # exact frame index
            Instr_Cont.tStart = t  # local t and not account for scr refresh
            Instr_Cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_Cont, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instr_Cont.started')
            # update status
            Instr_Cont.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Instr_Cont.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Instr_Cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Instr_Cont.status == STARTED and not waitOnFlip:
            theseKeys = Instr_Cont.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Instr_Cont_allKeys.extend(theseKeys)
            if len(_Instr_Cont_allKeys):
                Instr_Cont.keys = _Instr_Cont_allKeys[-1].name  # just the last key pressed
                Instr_Cont.rt = _Instr_Cont_allKeys[-1].rt
                Instr_Cont.duration = _Instr_Cont_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Box5
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EmotionalTaskInstructions2p5.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmotionalTaskInstructions2p5.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EmotionalTaskInstructions2p5" ---
    for thisComponent in EmotionalTaskInstructions2p5.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EmotionalTaskInstructions2p5
    EmotionalTaskInstructions2p5.tStop = globalClock.getTime(format='float')
    EmotionalTaskInstructions2p5.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EmotionalTaskInstructions2p5.stopped', EmotionalTaskInstructions2p5.tStop)
    thisExp.nextEntry()
    # the Routine "EmotionalTaskInstructions2p5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "PrePractice_Text" ---
    # create an object to store info about Routine PrePractice_Text
    PrePractice_Text = data.Routine(
        name='PrePractice_Text',
        components=[LastInstrText, InstrContPress],
    )
    PrePractice_Text.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for InstrContPress
    InstrContPress.keys = []
    InstrContPress.rt = []
    _InstrContPress_allKeys = []
    # store start times for PrePractice_Text
    PrePractice_Text.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    PrePractice_Text.tStart = globalClock.getTime(format='float')
    PrePractice_Text.status = STARTED
    thisExp.addData('PrePractice_Text.started', PrePractice_Text.tStart)
    PrePractice_Text.maxDuration = None
    # keep track of which components have finished
    PrePractice_TextComponents = PrePractice_Text.components
    for thisComponent in PrePractice_Text.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PrePractice_Text" ---
    PrePractice_Text.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LastInstrText* updates
        
        # if LastInstrText is starting this frame...
        if LastInstrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LastInstrText.frameNStart = frameN  # exact frame index
            LastInstrText.tStart = t  # local t and not account for scr refresh
            LastInstrText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LastInstrText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'LastInstrText.started')
            # update status
            LastInstrText.status = STARTED
            LastInstrText.setAutoDraw(True)
        
        # if LastInstrText is active this frame...
        if LastInstrText.status == STARTED:
            # update params
            pass
        
        # *InstrContPress* updates
        waitOnFlip = False
        
        # if InstrContPress is starting this frame...
        if InstrContPress.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            InstrContPress.frameNStart = frameN  # exact frame index
            InstrContPress.tStart = t  # local t and not account for scr refresh
            InstrContPress.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrContPress, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstrContPress.started')
            # update status
            InstrContPress.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstrContPress.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstrContPress.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstrContPress.status == STARTED and not waitOnFlip:
            theseKeys = InstrContPress.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _InstrContPress_allKeys.extend(theseKeys)
            if len(_InstrContPress_allKeys):
                InstrContPress.keys = _InstrContPress_allKeys[-1].name  # just the last key pressed
                InstrContPress.rt = _InstrContPress_allKeys[-1].rt
                InstrContPress.duration = _InstrContPress_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Box5p5
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            PrePractice_Text.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PrePractice_Text.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PrePractice_Text" ---
    for thisComponent in PrePractice_Text.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for PrePractice_Text
    PrePractice_Text.tStop = globalClock.getTime(format='float')
    PrePractice_Text.tStopRefresh = tThisFlipGlobal
    thisExp.addData('PrePractice_Text.stopped', PrePractice_Text.tStop)
    thisExp.nextEntry()
    # the Routine "PrePractice_Text" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    EPracticeOuterLoop = data.TrialHandler2(
        name='EPracticeOuterLoop',
        nReps=1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('EPracticeConditions/EPracticeMaster.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(EPracticeOuterLoop)  # add the loop to the experiment
    thisEPracticeOuterLoop = EPracticeOuterLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEPracticeOuterLoop.rgb)
    if thisEPracticeOuterLoop != None:
        for paramName in thisEPracticeOuterLoop:
            globals()[paramName] = thisEPracticeOuterLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisEPracticeOuterLoop in EPracticeOuterLoop:
        currentLoop = EPracticeOuterLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisEPracticeOuterLoop.rgb)
        if thisEPracticeOuterLoop != None:
            for paramName in thisEPracticeOuterLoop:
                globals()[paramName] = thisEPracticeOuterLoop[paramName]
        
        # --- Prepare to start Routine "EPracticeInstructions2" ---
        # create an object to store info about Routine EPracticeInstructions2
        EPracticeInstructions2 = data.Routine(
            name='EPracticeInstructions2',
            components=[Practice_Rule_Set, Continue_Pract_Text, key_resp_7, Practice_Block_Number_Text, Practice_Block_Text, Practice_Block_Text_End],
        )
        EPracticeInstructions2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Practice_Rule_Set.setText(Instructions)
        Continue_Pract_Text.setPos((0, -0.25))
        Continue_Pract_Text.setText("Please press 'spacebar' to begin.")
        # create starting attributes for key_resp_7
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        Practice_Block_Number_Text.setColor('green', colorSpace='rgb')
        Practice_Block_Number_Text.setPos((0.055, 0.05))
        Practice_Block_Number_Text.setText(PractNo)
        Practice_Block_Number_Text.setFont('Arial')
        Practice_Block_Number_Text.setHeight(0.03)
        # store start times for EPracticeInstructions2
        EPracticeInstructions2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        EPracticeInstructions2.tStart = globalClock.getTime(format='float')
        EPracticeInstructions2.status = STARTED
        thisExp.addData('EPracticeInstructions2.started', EPracticeInstructions2.tStart)
        EPracticeInstructions2.maxDuration = None
        # keep track of which components have finished
        EPracticeInstructions2Components = EPracticeInstructions2.components
        for thisComponent in EPracticeInstructions2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "EPracticeInstructions2" ---
        # if trial has changed, end Routine now
        if isinstance(EPracticeOuterLoop, data.TrialHandler2) and thisEPracticeOuterLoop.thisN != EPracticeOuterLoop.thisTrial.thisN:
            continueRoutine = False
        EPracticeInstructions2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Practice_Rule_Set* updates
            
            # if Practice_Rule_Set is starting this frame...
            if Practice_Rule_Set.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Practice_Rule_Set.frameNStart = frameN  # exact frame index
                Practice_Rule_Set.tStart = t  # local t and not account for scr refresh
                Practice_Rule_Set.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Practice_Rule_Set, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Practice_Rule_Set.started')
                # update status
                Practice_Rule_Set.status = STARTED
                Practice_Rule_Set.setAutoDraw(True)
            
            # if Practice_Rule_Set is active this frame...
            if Practice_Rule_Set.status == STARTED:
                # update params
                pass
            
            # *Continue_Pract_Text* updates
            
            # if Continue_Pract_Text is starting this frame...
            if Continue_Pract_Text.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Continue_Pract_Text.frameNStart = frameN  # exact frame index
                Continue_Pract_Text.tStart = t  # local t and not account for scr refresh
                Continue_Pract_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Continue_Pract_Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Continue_Pract_Text.started')
                # update status
                Continue_Pract_Text.status = STARTED
                Continue_Pract_Text.setAutoDraw(True)
            
            # if Continue_Pract_Text is active this frame...
            if Continue_Pract_Text.status == STARTED:
                # update params
                pass
            
            # *key_resp_7* updates
            waitOnFlip = False
            
            # if key_resp_7 is starting this frame...
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_7.started')
                # update status
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *Practice_Block_Number_Text* updates
            
            # if Practice_Block_Number_Text is starting this frame...
            if Practice_Block_Number_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Practice_Block_Number_Text.frameNStart = frameN  # exact frame index
                Practice_Block_Number_Text.tStart = t  # local t and not account for scr refresh
                Practice_Block_Number_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Practice_Block_Number_Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Practice_Block_Number_Text.started')
                # update status
                Practice_Block_Number_Text.status = STARTED
                Practice_Block_Number_Text.setAutoDraw(True)
            
            # if Practice_Block_Number_Text is active this frame...
            if Practice_Block_Number_Text.status == STARTED:
                # update params
                pass
            
            # *Practice_Block_Text* updates
            
            # if Practice_Block_Text is starting this frame...
            if Practice_Block_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Practice_Block_Text.frameNStart = frameN  # exact frame index
                Practice_Block_Text.tStart = t  # local t and not account for scr refresh
                Practice_Block_Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Practice_Block_Text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Practice_Block_Text.started')
                # update status
                Practice_Block_Text.status = STARTED
                Practice_Block_Text.setAutoDraw(True)
            
            # if Practice_Block_Text is active this frame...
            if Practice_Block_Text.status == STARTED:
                # update params
                pass
            
            # *Practice_Block_Text_End* updates
            
            # if Practice_Block_Text_End is starting this frame...
            if Practice_Block_Text_End.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Practice_Block_Text_End.frameNStart = frameN  # exact frame index
                Practice_Block_Text_End.tStart = t  # local t and not account for scr refresh
                Practice_Block_Text_End.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Practice_Block_Text_End, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Practice_Block_Text_End.started')
                # update status
                Practice_Block_Text_End.status = STARTED
                Practice_Block_Text_End.setAutoDraw(True)
            
            # if Practice_Block_Text_End is active this frame...
            if Practice_Block_Text_End.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from Box6
            grayBox.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                EPracticeInstructions2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EPracticeInstructions2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "EPracticeInstructions2" ---
        for thisComponent in EPracticeInstructions2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for EPracticeInstructions2
        EPracticeInstructions2.tStop = globalClock.getTime(format='float')
        EPracticeInstructions2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('EPracticeInstructions2.stopped', EPracticeInstructions2.tStop)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        EPracticeOuterLoop.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            EPracticeOuterLoop.addData('key_resp_7.rt', key_resp_7.rt)
            EPracticeOuterLoop.addData('key_resp_7.duration', key_resp_7.duration)
        # the Routine "EPracticeInstructions2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        EPracticeInnerLoop = data.TrialHandler2(
            name='EPracticeInnerLoop',
            nReps=1, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(CondFileP), 
            seed=None, 
        )
        thisExp.addLoop(EPracticeInnerLoop)  # add the loop to the experiment
        thisEPracticeInnerLoop = EPracticeInnerLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisEPracticeInnerLoop.rgb)
        if thisEPracticeInnerLoop != None:
            for paramName in thisEPracticeInnerLoop:
                globals()[paramName] = thisEPracticeInnerLoop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisEPracticeInnerLoop in EPracticeInnerLoop:
            currentLoop = EPracticeInnerLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisEPracticeInnerLoop.rgb)
            if thisEPracticeInnerLoop != None:
                for paramName in thisEPracticeInnerLoop:
                    globals()[paramName] = thisEPracticeInnerLoop[paramName]
            
            # --- Prepare to start Routine "EPracticeISI" ---
            # create an object to store info about Routine EPracticeISI
            EPracticeISI = data.Routine(
                name='EPracticeISI',
                components=[EPracticeISIMarker],
            )
            EPracticeISI.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            EPracticeISIMarker.setText('+')
            EPracticeISIMarker.setHeight(0.18)
            # store start times for EPracticeISI
            EPracticeISI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            EPracticeISI.tStart = globalClock.getTime(format='float')
            EPracticeISI.status = STARTED
            thisExp.addData('EPracticeISI.started', EPracticeISI.tStart)
            EPracticeISI.maxDuration = None
            # keep track of which components have finished
            EPracticeISIComponents = EPracticeISI.components
            for thisComponent in EPracticeISI.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "EPracticeISI" ---
            # if trial has changed, end Routine now
            if isinstance(EPracticeInnerLoop, data.TrialHandler2) and thisEPracticeInnerLoop.thisN != EPracticeInnerLoop.thisTrial.thisN:
                continueRoutine = False
            EPracticeISI.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *EPracticeISIMarker* updates
                
                # if EPracticeISIMarker is starting this frame...
                if EPracticeISIMarker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    EPracticeISIMarker.frameNStart = frameN  # exact frame index
                    EPracticeISIMarker.tStart = t  # local t and not account for scr refresh
                    EPracticeISIMarker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(EPracticeISIMarker, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EPracticeISIMarker.started')
                    # update status
                    EPracticeISIMarker.status = STARTED
                    EPracticeISIMarker.setAutoDraw(True)
                
                # if EPracticeISIMarker is active this frame...
                if EPracticeISIMarker.status == STARTED:
                    # update params
                    pass
                
                # if EPracticeISIMarker is stopping this frame...
                if EPracticeISIMarker.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > EPracticeISIMarker.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        EPracticeISIMarker.tStop = t  # not accounting for scr refresh
                        EPracticeISIMarker.tStopRefresh = tThisFlipGlobal  # on global time
                        EPracticeISIMarker.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'EPracticeISIMarker.stopped')
                        # update status
                        EPracticeISIMarker.status = FINISHED
                        EPracticeISIMarker.setAutoDraw(False)
                # Run 'Each Frame' code from Box7
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    EPracticeISI.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in EPracticeISI.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "EPracticeISI" ---
            for thisComponent in EPracticeISI.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for EPracticeISI
            EPracticeISI.tStop = globalClock.getTime(format='float')
            EPracticeISI.tStopRefresh = tThisFlipGlobal
            thisExp.addData('EPracticeISI.stopped', EPracticeISI.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if EPracticeISI.maxDurationReached:
                routineTimer.addTime(-EPracticeISI.maxDuration)
            elif EPracticeISI.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "EPracticeTrial" ---
            # create an object to store info about Routine EPracticeTrial
            EPracticeTrial = data.Routine(
                name='EPracticeTrial',
                components=[Pract, PracticeFace, ColourPractice],
            )
            EPracticeTrial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for Pract
            Pract.keys = []
            Pract.rt = []
            _Pract_allKeys = []
            PracticeFace.setImage(FaceE)
            ColourPractice.setOpacity(0.25)
            ColourPractice.setSize((0.3, 0.125))
            ColourPractice.setImage(ColourF)
            # store start times for EPracticeTrial
            EPracticeTrial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            EPracticeTrial.tStart = globalClock.getTime(format='float')
            EPracticeTrial.status = STARTED
            thisExp.addData('EPracticeTrial.started', EPracticeTrial.tStart)
            EPracticeTrial.maxDuration = None
            # keep track of which components have finished
            EPracticeTrialComponents = EPracticeTrial.components
            for thisComponent in EPracticeTrial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "EPracticeTrial" ---
            # if trial has changed, end Routine now
            if isinstance(EPracticeInnerLoop, data.TrialHandler2) and thisEPracticeInnerLoop.thisN != EPracticeInnerLoop.thisTrial.thisN:
                continueRoutine = False
            EPracticeTrial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Pract* updates
                waitOnFlip = False
                
                # if Pract is starting this frame...
                if Pract.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                    # keep track of start time/frame for later
                    Pract.frameNStart = frameN  # exact frame index
                    Pract.tStart = t  # local t and not account for scr refresh
                    Pract.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Pract, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Pract.started')
                    # update status
                    Pract.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Pract.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Pract.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if Pract is stopping this frame...
                if Pract.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Pract.tStartRefresh + 0.45-frameTolerance:
                        # keep track of stop time/frame for later
                        Pract.tStop = t  # not accounting for scr refresh
                        Pract.tStopRefresh = tThisFlipGlobal  # on global time
                        Pract.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Pract.stopped')
                        # update status
                        Pract.status = FINISHED
                        Pract.status = FINISHED
                if Pract.status == STARTED and not waitOnFlip:
                    theseKeys = Pract.getKeys(keyList=['space','None'], ignoreKeys=["escape"], waitRelease=False)
                    _Pract_allKeys.extend(theseKeys)
                    if len(_Pract_allKeys):
                        Pract.keys = _Pract_allKeys[-1].name  # just the last key pressed
                        Pract.rt = _Pract_allKeys[-1].rt
                        Pract.duration = _Pract_allKeys[-1].duration
                        # was this correct?
                        if (Pract.keys == str(CorrectAnsP)) or (Pract.keys == CorrectAnsP):
                            Pract.corr = 1
                        else:
                            Pract.corr = 0
                
                # *PracticeFace* updates
                
                # if PracticeFace is starting this frame...
                if PracticeFace.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                    # keep track of start time/frame for later
                    PracticeFace.frameNStart = frameN  # exact frame index
                    PracticeFace.tStart = t  # local t and not account for scr refresh
                    PracticeFace.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PracticeFace, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PracticeFace.started')
                    # update status
                    PracticeFace.status = STARTED
                    PracticeFace.setAutoDraw(True)
                
                # if PracticeFace is active this frame...
                if PracticeFace.status == STARTED:
                    # update params
                    pass
                
                # if PracticeFace is stopping this frame...
                if PracticeFace.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PracticeFace.tStartRefresh + 0.45-frameTolerance:
                        # keep track of stop time/frame for later
                        PracticeFace.tStop = t  # not accounting for scr refresh
                        PracticeFace.tStopRefresh = tThisFlipGlobal  # on global time
                        PracticeFace.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'PracticeFace.stopped')
                        # update status
                        PracticeFace.status = FINISHED
                        PracticeFace.setAutoDraw(False)
                
                # *ColourPractice* updates
                
                # if ColourPractice is starting this frame...
                if ColourPractice.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
                    # keep track of start time/frame for later
                    ColourPractice.frameNStart = frameN  # exact frame index
                    ColourPractice.tStart = t  # local t and not account for scr refresh
                    ColourPractice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ColourPractice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ColourPractice.started')
                    # update status
                    ColourPractice.status = STARTED
                    ColourPractice.setAutoDraw(True)
                
                # if ColourPractice is active this frame...
                if ColourPractice.status == STARTED:
                    # update params
                    pass
                
                # if ColourPractice is stopping this frame...
                if ColourPractice.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ColourPractice.tStartRefresh + 0.45-frameTolerance:
                        # keep track of stop time/frame for later
                        ColourPractice.tStop = t  # not accounting for scr refresh
                        ColourPractice.tStopRefresh = tThisFlipGlobal  # on global time
                        ColourPractice.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ColourPractice.stopped')
                        # update status
                        ColourPractice.status = FINISHED
                        ColourPractice.setAutoDraw(False)
                # Run 'Each Frame' code from Box8
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    EPracticeTrial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in EPracticeTrial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "EPracticeTrial" ---
            for thisComponent in EPracticeTrial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for EPracticeTrial
            EPracticeTrial.tStop = globalClock.getTime(format='float')
            EPracticeTrial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('EPracticeTrial.stopped', EPracticeTrial.tStop)
            # check responses
            if Pract.keys in ['', [], None]:  # No response was made
                Pract.keys = None
                # was no response the correct answer?!
                if str(CorrectAnsP).lower() == 'none':
                   Pract.corr = 1;  # correct non-response
                else:
                   Pract.corr = 0;  # failed to respond (incorrectly)
            # store data for EPracticeInnerLoop (TrialHandler)
            EPracticeInnerLoop.addData('Pract.keys',Pract.keys)
            EPracticeInnerLoop.addData('Pract.corr', Pract.corr)
            if Pract.keys != None:  # we had a response
                EPracticeInnerLoop.addData('Pract.rt', Pract.rt)
                EPracticeInnerLoop.addData('Pract.duration', Pract.duration)
            # Run 'End Routine' code from Feedback_code
            if Pract.corr==1:
                    PracticeFeedback = 'Correct'
                    FeedbackColour = 'darkgreen'
            
            if Pract.corr==0:
                    PracticeFeedback = 'Incorrect'
                    FeedbackColour = 'darkred'
            
            if Pract.corr==0 and Pract.keys== None:
                    PracticeFeedback = 'Miss (too slow)'
                    FeedbackColour = 'tan'
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if EPracticeTrial.maxDurationReached:
                routineTimer.addTime(-EPracticeTrial.maxDuration)
            elif EPracticeTrial.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            
            # --- Prepare to start Routine "Blank_3" ---
            # create an object to store info about Routine Blank_3
            Blank_3 = data.Routine(
                name='Blank_3',
                components=[text_5],
            )
            Blank_3.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for Blank_3
            Blank_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Blank_3.tStart = globalClock.getTime(format='float')
            Blank_3.status = STARTED
            thisExp.addData('Blank_3.started', Blank_3.tStart)
            Blank_3.maxDuration = None
            # keep track of which components have finished
            Blank_3Components = Blank_3.components
            for thisComponent in Blank_3.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Blank_3" ---
            # if trial has changed, end Routine now
            if isinstance(EPracticeInnerLoop, data.TrialHandler2) and thisEPracticeInnerLoop.thisN != EPracticeInnerLoop.thisTrial.thisN:
                continueRoutine = False
            Blank_3.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.05:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_5* updates
                
                # if text_5 is starting this frame...
                if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_5.frameNStart = frameN  # exact frame index
                    text_5.tStart = t  # local t and not account for scr refresh
                    text_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_5.started')
                    # update status
                    text_5.status = STARTED
                    text_5.setAutoDraw(True)
                
                # if text_5 is active this frame...
                if text_5.status == STARTED:
                    # update params
                    pass
                
                # if text_5 is stopping this frame...
                if text_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_5.tStartRefresh + 0.05-frameTolerance:
                        # keep track of stop time/frame for later
                        text_5.tStop = t  # not accounting for scr refresh
                        text_5.tStopRefresh = tThisFlipGlobal  # on global time
                        text_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_5.stopped')
                        # update status
                        text_5.status = FINISHED
                        text_5.setAutoDraw(False)
                # Run 'Each Frame' code from Box18_2
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Blank_3.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank_3.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Blank_3" ---
            for thisComponent in Blank_3.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Blank_3
            Blank_3.tStop = globalClock.getTime(format='float')
            Blank_3.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Blank_3.stopped', Blank_3.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Blank_3.maxDurationReached:
                routineTimer.addTime(-Blank_3.maxDuration)
            elif Blank_3.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.050000)
            
            # --- Prepare to start Routine "PracticeFeedbackBlock" ---
            # create an object to store info about Routine PracticeFeedbackBlock
            PracticeFeedbackBlock = data.Routine(
                name='PracticeFeedbackBlock',
                components=[Practice_Feedback],
            )
            PracticeFeedbackBlock.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            Practice_Feedback.setColor(FeedbackColour, colorSpace='rgb')
            Practice_Feedback.setText(PracticeFeedback)
            Practice_Feedback.setHeight(0.05)
            # store start times for PracticeFeedbackBlock
            PracticeFeedbackBlock.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            PracticeFeedbackBlock.tStart = globalClock.getTime(format='float')
            PracticeFeedbackBlock.status = STARTED
            thisExp.addData('PracticeFeedbackBlock.started', PracticeFeedbackBlock.tStart)
            PracticeFeedbackBlock.maxDuration = None
            # keep track of which components have finished
            PracticeFeedbackBlockComponents = PracticeFeedbackBlock.components
            for thisComponent in PracticeFeedbackBlock.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "PracticeFeedbackBlock" ---
            # if trial has changed, end Routine now
            if isinstance(EPracticeInnerLoop, data.TrialHandler2) and thisEPracticeInnerLoop.thisN != EPracticeInnerLoop.thisTrial.thisN:
                continueRoutine = False
            PracticeFeedbackBlock.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Practice_Feedback* updates
                
                # if Practice_Feedback is starting this frame...
                if Practice_Feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    Practice_Feedback.frameNStart = frameN  # exact frame index
                    Practice_Feedback.tStart = t  # local t and not account for scr refresh
                    Practice_Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Practice_Feedback, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Practice_Feedback.started')
                    # update status
                    Practice_Feedback.status = STARTED
                    Practice_Feedback.setAutoDraw(True)
                
                # if Practice_Feedback is active this frame...
                if Practice_Feedback.status == STARTED:
                    # update params
                    pass
                
                # if Practice_Feedback is stopping this frame...
                if Practice_Feedback.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Practice_Feedback.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Practice_Feedback.tStop = t  # not accounting for scr refresh
                        Practice_Feedback.tStopRefresh = tThisFlipGlobal  # on global time
                        Practice_Feedback.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Practice_Feedback.stopped')
                        # update status
                        Practice_Feedback.status = FINISHED
                        Practice_Feedback.setAutoDraw(False)
                # Run 'Each Frame' code from Box10
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    PracticeFeedbackBlock.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in PracticeFeedbackBlock.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "PracticeFeedbackBlock" ---
            for thisComponent in PracticeFeedbackBlock.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for PracticeFeedbackBlock
            PracticeFeedbackBlock.tStop = globalClock.getTime(format='float')
            PracticeFeedbackBlock.tStopRefresh = tThisFlipGlobal
            thisExp.addData('PracticeFeedbackBlock.stopped', PracticeFeedbackBlock.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if PracticeFeedbackBlock.maxDurationReached:
                routineTimer.addTime(-PracticeFeedbackBlock.maxDuration)
            elif PracticeFeedbackBlock.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.500000)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'EPracticeInnerLoop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "Add" ---
        # create an object to store info about Routine Add
        Add = data.Routine(
            name='Add',
            components=[],
        )
        Add.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_4
        PractNo = PractNo + 1
        # store start times for Add
        Add.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Add.tStart = globalClock.getTime(format='float')
        Add.status = STARTED
        thisExp.addData('Add.started', Add.tStart)
        Add.maxDuration = None
        # keep track of which components have finished
        AddComponents = Add.components
        for thisComponent in Add.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Add" ---
        # if trial has changed, end Routine now
        if isinstance(EPracticeOuterLoop, data.TrialHandler2) and thisEPracticeOuterLoop.thisN != EPracticeOuterLoop.thisTrial.thisN:
            continueRoutine = False
        Add.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Add.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Add.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Add" ---
        for thisComponent in Add.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Add
        Add.tStop = globalClock.getTime(format='float')
        Add.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Add.stopped', Add.tStop)
        # the Routine "Add" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'EPracticeOuterLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "EndPracticeEndInstructions" ---
    # create an object to store info about Routine EndPracticeEndInstructions
    EndPracticeEndInstructions = data.Routine(
        name='EndPracticeEndInstructions',
        components=[EndOfPractice, key_resp_8],
    )
    EndPracticeEndInstructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    EndOfPractice.setText('End of practice.\n\nPlease keep in mind: You will no longer \nreceive feedback on your performance\nin the real task (e.g. "correct"). \n\nPress \'spacebar\' to continue')
    EndOfPractice.setHeight(0.025)
    # create starting attributes for key_resp_8
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # store start times for EndPracticeEndInstructions
    EndPracticeEndInstructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EndPracticeEndInstructions.tStart = globalClock.getTime(format='float')
    EndPracticeEndInstructions.status = STARTED
    thisExp.addData('EndPracticeEndInstructions.started', EndPracticeEndInstructions.tStart)
    EndPracticeEndInstructions.maxDuration = None
    # keep track of which components have finished
    EndPracticeEndInstructionsComponents = EndPracticeEndInstructions.components
    for thisComponent in EndPracticeEndInstructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndPracticeEndInstructions" ---
    EndPracticeEndInstructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *EndOfPractice* updates
        
        # if EndOfPractice is starting this frame...
        if EndOfPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndOfPractice.frameNStart = frameN  # exact frame index
            EndOfPractice.tStart = t  # local t and not account for scr refresh
            EndOfPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndOfPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndOfPractice.started')
            # update status
            EndOfPractice.status = STARTED
            EndOfPractice.setAutoDraw(True)
        
        # if EndOfPractice is active this frame...
        if EndOfPractice.status == STARTED:
            # update params
            pass
        
        # *key_resp_8* updates
        waitOnFlip = False
        
        # if key_resp_8 is starting this frame...
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_8.started')
            # update status
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Box11
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EndPracticeEndInstructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndPracticeEndInstructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndPracticeEndInstructions" ---
    for thisComponent in EndPracticeEndInstructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EndPracticeEndInstructions
    EndPracticeEndInstructions.tStop = globalClock.getTime(format='float')
    EndPracticeEndInstructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EndPracticeEndInstructions.stopped', EndPracticeEndInstructions.tStop)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    thisExp.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        thisExp.addData('key_resp_8.rt', key_resp_8.rt)
        thisExp.addData('key_resp_8.duration', key_resp_8.duration)
    thisExp.nextEntry()
    # the Routine "EndPracticeEndInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Pre_Calib_Instructions" ---
    # create an object to store info about Routine Pre_Calib_Instructions
    Pre_Calib_Instructions = data.Routine(
        name='Pre_Calib_Instructions',
        components=[PreCalib_Text, PressCalibKey],
    )
    Pre_Calib_Instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for PressCalibKey
    PressCalibKey.keys = []
    PressCalibKey.rt = []
    _PressCalibKey_allKeys = []
    # store start times for Pre_Calib_Instructions
    Pre_Calib_Instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Pre_Calib_Instructions.tStart = globalClock.getTime(format='float')
    Pre_Calib_Instructions.status = STARTED
    thisExp.addData('Pre_Calib_Instructions.started', Pre_Calib_Instructions.tStart)
    Pre_Calib_Instructions.maxDuration = None
    # keep track of which components have finished
    Pre_Calib_InstructionsComponents = Pre_Calib_Instructions.components
    for thisComponent in Pre_Calib_Instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Pre_Calib_Instructions" ---
    Pre_Calib_Instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PreCalib_Text* updates
        
        # if PreCalib_Text is starting this frame...
        if PreCalib_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PreCalib_Text.frameNStart = frameN  # exact frame index
            PreCalib_Text.tStart = t  # local t and not account for scr refresh
            PreCalib_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PreCalib_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PreCalib_Text.started')
            # update status
            PreCalib_Text.status = STARTED
            PreCalib_Text.setAutoDraw(True)
        
        # if PreCalib_Text is active this frame...
        if PreCalib_Text.status == STARTED:
            # update params
            pass
        
        # *PressCalibKey* updates
        waitOnFlip = False
        
        # if PressCalibKey is starting this frame...
        if PressCalibKey.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            PressCalibKey.frameNStart = frameN  # exact frame index
            PressCalibKey.tStart = t  # local t and not account for scr refresh
            PressCalibKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressCalibKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PressCalibKey.started')
            # update status
            PressCalibKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PressCalibKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PressCalibKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PressCalibKey.status == STARTED and not waitOnFlip:
            theseKeys = PressCalibKey.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _PressCalibKey_allKeys.extend(theseKeys)
            if len(_PressCalibKey_allKeys):
                PressCalibKey.keys = _PressCalibKey_allKeys[-1].name  # just the last key pressed
                PressCalibKey.rt = _PressCalibKey_allKeys[-1].rt
                PressCalibKey.duration = _PressCalibKey_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Box12
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Pre_Calib_Instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pre_Calib_Instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Pre_Calib_Instructions" ---
    for thisComponent in Pre_Calib_Instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Pre_Calib_Instructions
    Pre_Calib_Instructions.tStop = globalClock.getTime(format='float')
    Pre_Calib_Instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Pre_Calib_Instructions.stopped', Pre_Calib_Instructions.tStop)
    thisExp.nextEntry()
    # the Routine "Pre_Calib_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "EyeT_Calib" ---
    # create an object to store info about Routine EyeT_Calib
    EyeT_Calib = data.Routine(
        name='EyeT_Calib',
        components=[],
    )
    EyeT_Calib.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from EyeT_Calib
    if TaskVersion == '1' or TaskVersion == '2':
        el_tracker.doTrackerSetup()
    
    # store start times for EyeT_Calib
    EyeT_Calib.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EyeT_Calib.tStart = globalClock.getTime(format='float')
    EyeT_Calib.status = STARTED
    thisExp.addData('EyeT_Calib.started', EyeT_Calib.tStart)
    EyeT_Calib.maxDuration = None
    # keep track of which components have finished
    EyeT_CalibComponents = EyeT_Calib.components
    for thisComponent in EyeT_Calib.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EyeT_Calib" ---
    EyeT_Calib.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EyeT_Calib.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EyeT_Calib.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EyeT_Calib" ---
    for thisComponent in EyeT_Calib.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EyeT_Calib
    EyeT_Calib.tStop = globalClock.getTime(format='float')
    EyeT_Calib.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EyeT_Calib.stopped', EyeT_Calib.tStop)
    thisExp.nextEntry()
    # the Routine "EyeT_Calib" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "EyeT_DriftCheck" ---
    # create an object to store info about Routine EyeT_DriftCheck
    EyeT_DriftCheck = data.Routine(
        name='EyeT_DriftCheck',
        components=[],
    )
    EyeT_DriftCheck.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for EyeT_DriftCheck
    EyeT_DriftCheck.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EyeT_DriftCheck.tStart = globalClock.getTime(format='float')
    EyeT_DriftCheck.status = STARTED
    thisExp.addData('EyeT_DriftCheck.started', EyeT_DriftCheck.tStart)
    EyeT_DriftCheck.maxDuration = None
    # keep track of which components have finished
    EyeT_DriftCheckComponents = EyeT_DriftCheck.components
    for thisComponent in EyeT_DriftCheck.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EyeT_DriftCheck" ---
    EyeT_DriftCheck.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EyeT_DriftCheck.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EyeT_DriftCheck.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EyeT_DriftCheck" ---
    for thisComponent in EyeT_DriftCheck.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EyeT_DriftCheck
    EyeT_DriftCheck.tStop = globalClock.getTime(format='float')
    EyeT_DriftCheck.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EyeT_DriftCheck.stopped', EyeT_DriftCheck.tStop)
    thisExp.nextEntry()
    # the Routine "EyeT_DriftCheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "RealTaskPreInstructions" ---
    # create an object to store info about Routine RealTaskPreInstructions
    RealTaskPreInstructions = data.Routine(
        name='RealTaskPreInstructions',
        components=[Begin_Real_Task_Text, key_resp_6],
    )
    RealTaskPreInstructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_6
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # store start times for RealTaskPreInstructions
    RealTaskPreInstructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    RealTaskPreInstructions.tStart = globalClock.getTime(format='float')
    RealTaskPreInstructions.status = STARTED
    thisExp.addData('RealTaskPreInstructions.started', RealTaskPreInstructions.tStart)
    RealTaskPreInstructions.maxDuration = None
    # keep track of which components have finished
    RealTaskPreInstructionsComponents = RealTaskPreInstructions.components
    for thisComponent in RealTaskPreInstructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RealTaskPreInstructions" ---
    RealTaskPreInstructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Begin_Real_Task_Text* updates
        
        # if Begin_Real_Task_Text is starting this frame...
        if Begin_Real_Task_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Begin_Real_Task_Text.frameNStart = frameN  # exact frame index
            Begin_Real_Task_Text.tStart = t  # local t and not account for scr refresh
            Begin_Real_Task_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Begin_Real_Task_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Begin_Real_Task_Text.started')
            # update status
            Begin_Real_Task_Text.status = STARTED
            Begin_Real_Task_Text.setAutoDraw(True)
        
        # if Begin_Real_Task_Text is active this frame...
        if Begin_Real_Task_Text.status == STARTED:
            # update params
            pass
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from Box13
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            RealTaskPreInstructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RealTaskPreInstructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RealTaskPreInstructions" ---
    for thisComponent in RealTaskPreInstructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for RealTaskPreInstructions
    RealTaskPreInstructions.tStop = globalClock.getTime(format='float')
    RealTaskPreInstructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('RealTaskPreInstructions.stopped', RealTaskPreInstructions.tStop)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "RealTaskPreInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    MasterLoop = data.TrialHandler2(
        name='MasterLoop',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(VersionSelection), 
        seed=None, 
    )
    thisExp.addLoop(MasterLoop)  # add the loop to the experiment
    thisMasterLoop = MasterLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMasterLoop.rgb)
    if thisMasterLoop != None:
        for paramName in thisMasterLoop:
            globals()[paramName] = thisMasterLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisMasterLoop in MasterLoop:
        currentLoop = MasterLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisMasterLoop.rgb)
        if thisMasterLoop != None:
            for paramName in thisMasterLoop:
                globals()[paramName] = thisMasterLoop[paramName]
        
        # set up handler to look after randomisation of conditions etc
        OuterLoop = data.TrialHandler2(
            name='OuterLoop',
            nReps=1, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(MasterCondFile), 
            seed=None, 
        )
        thisExp.addLoop(OuterLoop)  # add the loop to the experiment
        thisOuterLoop = OuterLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisOuterLoop.rgb)
        if thisOuterLoop != None:
            for paramName in thisOuterLoop:
                globals()[paramName] = thisOuterLoop[paramName]
        
        for thisOuterLoop in OuterLoop:
            currentLoop = OuterLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisOuterLoop.rgb)
            if thisOuterLoop != None:
                for paramName in thisOuterLoop:
                    globals()[paramName] = thisOuterLoop[paramName]
            
            # --- Prepare to start Routine "Instructions_2" ---
            # create an object to store info about Routine Instructions_2
            Instructions_2 = data.Routine(
                name='Instructions_2',
                components=[text_2, text_3, key_resp_3, TaskBlock, BlockNo1, OfBlock],
            )
            Instructions_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            text_2.setPos((0, -0.10))
            text_2.setText(Instructions
            
            )
            text_3.setPos((0, -0.25))
            text_3.setText("Please press 'spacebar' to begin.")
            # create starting attributes for key_resp_3
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            TaskBlock.setText(' Task block:')
            BlockNo1.setColor('green', colorSpace='rgb')
            BlockNo1.setPos((0.025, 0.05))
            BlockNo1.setText(BlockNo)
            BlockNo1.setHeight(0.03)
            OfBlock.setText('of 6.')
            # store start times for Instructions_2
            Instructions_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Instructions_2.tStart = globalClock.getTime(format='float')
            Instructions_2.status = STARTED
            thisExp.addData('Instructions_2.started', Instructions_2.tStart)
            Instructions_2.maxDuration = None
            # keep track of which components have finished
            Instructions_2Components = Instructions_2.components
            for thisComponent in Instructions_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Instructions_2" ---
            # if trial has changed, end Routine now
            if isinstance(OuterLoop, data.TrialHandler2) and thisOuterLoop.thisN != OuterLoop.thisTrial.thisN:
                continueRoutine = False
            Instructions_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                
                # if text_2 is starting this frame...
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    # update status
                    text_2.status = STARTED
                    text_2.setAutoDraw(True)
                
                # if text_2 is active this frame...
                if text_2.status == STARTED:
                    # update params
                    pass
                
                # *text_3* updates
                
                # if text_3 is starting this frame...
                if text_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.started')
                    # update status
                    text_3.status = STARTED
                    text_3.setAutoDraw(True)
                
                # if text_3 is active this frame...
                if text_3.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_3* updates
                waitOnFlip = False
                
                # if key_resp_3 is starting this frame...
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.started')
                    # update status
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                        key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                        key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *TaskBlock* updates
                
                # if TaskBlock is starting this frame...
                if TaskBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TaskBlock.frameNStart = frameN  # exact frame index
                    TaskBlock.tStart = t  # local t and not account for scr refresh
                    TaskBlock.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TaskBlock, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'TaskBlock.started')
                    # update status
                    TaskBlock.status = STARTED
                    TaskBlock.setAutoDraw(True)
                
                # if TaskBlock is active this frame...
                if TaskBlock.status == STARTED:
                    # update params
                    pass
                
                # *BlockNo1* updates
                
                # if BlockNo1 is starting this frame...
                if BlockNo1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BlockNo1.frameNStart = frameN  # exact frame index
                    BlockNo1.tStart = t  # local t and not account for scr refresh
                    BlockNo1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BlockNo1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'BlockNo1.started')
                    # update status
                    BlockNo1.status = STARTED
                    BlockNo1.setAutoDraw(True)
                
                # if BlockNo1 is active this frame...
                if BlockNo1.status == STARTED:
                    # update params
                    pass
                
                # *OfBlock* updates
                
                # if OfBlock is starting this frame...
                if OfBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    OfBlock.frameNStart = frameN  # exact frame index
                    OfBlock.tStart = t  # local t and not account for scr refresh
                    OfBlock.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(OfBlock, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'OfBlock.started')
                    # update status
                    OfBlock.status = STARTED
                    OfBlock.setAutoDraw(True)
                
                # if OfBlock is active this frame...
                if OfBlock.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from Box14
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Instructions_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Instructions_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Instructions_2" ---
            for thisComponent in Instructions_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Instructions_2
            Instructions_2.tStop = globalClock.getTime(format='float')
            Instructions_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Instructions_2.stopped', Instructions_2.tStop)
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys = None
            OuterLoop.addData('key_resp_3.keys',key_resp_3.keys)
            if key_resp_3.keys != None:  # we had a response
                OuterLoop.addData('key_resp_3.rt', key_resp_3.rt)
                OuterLoop.addData('key_resp_3.duration', key_resp_3.duration)
            # the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Begin_Rec" ---
            # create an object to store info about Routine Begin_Rec
            Begin_Rec = data.Routine(
                name='Begin_Rec',
                components=[],
            )
            Begin_Rec.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Record_Code
            if TaskVersion in ('1', '2'):
                el_tracker.sendMessage('!V START_BLOCK')
                el_tracker.sendMessage('!V RECORDING_START_BLOCK %s' % BlockNo)
                el_tracker.startRecording(1, 1, 1, 1)
                pylink.pumpDelay(200)
            
            # store start times for Begin_Rec
            Begin_Rec.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Begin_Rec.tStart = globalClock.getTime(format='float')
            Begin_Rec.status = STARTED
            thisExp.addData('Begin_Rec.started', Begin_Rec.tStart)
            Begin_Rec.maxDuration = None
            # keep track of which components have finished
            Begin_RecComponents = Begin_Rec.components
            for thisComponent in Begin_Rec.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Begin_Rec" ---
            # if trial has changed, end Routine now
            if isinstance(OuterLoop, data.TrialHandler2) and thisOuterLoop.thisN != OuterLoop.thisTrial.thisN:
                continueRoutine = False
            Begin_Rec.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Begin_Rec.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Begin_Rec.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Begin_Rec" ---
            for thisComponent in Begin_Rec.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Begin_Rec
            Begin_Rec.tStop = globalClock.getTime(format='float')
            Begin_Rec.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Begin_Rec.stopped', Begin_Rec.tStop)
            # the Routine "Begin_Rec" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            InnerLoop = data.TrialHandler2(
                name='InnerLoop',
                nReps=1, 
                method='sequential', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions(CondFile), 
                seed=None, 
            )
            thisExp.addLoop(InnerLoop)  # add the loop to the experiment
            thisInnerLoop = InnerLoop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisInnerLoop.rgb)
            if thisInnerLoop != None:
                for paramName in thisInnerLoop:
                    globals()[paramName] = thisInnerLoop[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisInnerLoop in InnerLoop:
                currentLoop = InnerLoop
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisInnerLoop.rgb)
                if thisInnerLoop != None:
                    for paramName in thisInnerLoop:
                        globals()[paramName] = thisInnerLoop[paramName]
                
                # --- Prepare to start Routine "ISI_2" ---
                # create an object to store info about Routine ISI_2
                ISI_2 = data.Routine(
                    name='ISI_2',
                    components=[Pre_ISI_Text],
                )
                ISI_2.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                Pre_ISI_Text.setText('+')
                # Run 'Begin Routine' code from Timer_1
                time_trialBegin = globalClock.getTime()
                
                if TaskVersion in ('1', '2'):
                
                    el_tracker.sendMessage(f"TRIAL_BEGIN")
                    el_tracker.sendMessage(f"TRIAL_TIME_BEGIN {time_trialBegin:.3f}")
                
                    el_tracker.sendMessage('!V PRE_ISI TRIAL_NO %s' % Trial_No)
                    el_tracker.sendMessage('!V PRE_ISI TRIAL_TYPE %s' % Trial_Type)
                    el_tracker.sendMessage('!V PRE_ISI EXPRESS %s' % Express)
                    el_tracker.sendMessage('!V PRE_ISI FACE_LUM %s' % FaceE_Luminance)
                    el_tracker.sendMessage('!V PRE_ISI COLOUR_LUM %s' % Colour_Luminance)
                # store start times for ISI_2
                ISI_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                ISI_2.tStart = globalClock.getTime(format='float')
                ISI_2.status = STARTED
                thisExp.addData('ISI_2.started', ISI_2.tStart)
                ISI_2.maxDuration = None
                # keep track of which components have finished
                ISI_2Components = ISI_2.components
                for thisComponent in ISI_2.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "ISI_2" ---
                # if trial has changed, end Routine now
                if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
                    continueRoutine = False
                ISI_2.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *Pre_ISI_Text* updates
                    
                    # if Pre_ISI_Text is starting this frame...
                    if Pre_ISI_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Pre_ISI_Text.frameNStart = frameN  # exact frame index
                        Pre_ISI_Text.tStart = t  # local t and not account for scr refresh
                        Pre_ISI_Text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Pre_ISI_Text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Pre_ISI_Text.started')
                        # update status
                        Pre_ISI_Text.status = STARTED
                        Pre_ISI_Text.setAutoDraw(True)
                    
                    # if Pre_ISI_Text is active this frame...
                    if Pre_ISI_Text.status == STARTED:
                        # update params
                        pass
                    
                    # if Pre_ISI_Text is stopping this frame...
                    if Pre_ISI_Text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Pre_ISI_Text.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            Pre_ISI_Text.tStop = t  # not accounting for scr refresh
                            Pre_ISI_Text.tStopRefresh = tThisFlipGlobal  # on global time
                            Pre_ISI_Text.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Pre_ISI_Text.stopped')
                            # update status
                            Pre_ISI_Text.status = FINISHED
                            Pre_ISI_Text.setAutoDraw(False)
                    # Run 'Each Frame' code from Box16
                    grayBox.draw()
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        ISI_2.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in ISI_2.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "ISI_2" ---
                for thisComponent in ISI_2.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for ISI_2
                ISI_2.tStop = globalClock.getTime(format='float')
                ISI_2.tStopRefresh = tThisFlipGlobal
                thisExp.addData('ISI_2.stopped', ISI_2.tStop)
                # Run 'End Routine' code from Timer_1
                time_trialEnd = globalClock.getTime()
                
                thisExp.addData('PRE_ISI_Begin', time_trialBegin)
                thisExp.addData('PRE_ISI_End', time_trialEnd)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if ISI_2.maxDurationReached:
                    routineTimer.addTime(-ISI_2.maxDuration)
                elif ISI_2.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                
                # --- Prepare to start Routine "Blank_4" ---
                # create an object to store info about Routine Blank_4
                Blank_4 = data.Routine(
                    name='Blank_4',
                    components=[text_6],
                )
                Blank_4.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from Timer_5
                
                
                
                # store start times for Blank_4
                Blank_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                Blank_4.tStart = globalClock.getTime(format='float')
                Blank_4.status = STARTED
                thisExp.addData('Blank_4.started', Blank_4.tStart)
                Blank_4.maxDuration = None
                # keep track of which components have finished
                Blank_4Components = Blank_4.components
                for thisComponent in Blank_4.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Blank_4" ---
                # if trial has changed, end Routine now
                if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
                    continueRoutine = False
                Blank_4.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.05:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_6* updates
                    
                    # if text_6 is starting this frame...
                    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_6.frameNStart = frameN  # exact frame index
                        text_6.tStart = t  # local t and not account for scr refresh
                        text_6.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_6.started')
                        # update status
                        text_6.status = STARTED
                        text_6.setAutoDraw(True)
                    
                    # if text_6 is active this frame...
                    if text_6.status == STARTED:
                        # update params
                        pass
                    
                    # if text_6 is stopping this frame...
                    if text_6.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_6.tStartRefresh + 0.05-frameTolerance:
                            # keep track of stop time/frame for later
                            text_6.tStop = t  # not accounting for scr refresh
                            text_6.tStopRefresh = tThisFlipGlobal  # on global time
                            text_6.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_6.stopped')
                            # update status
                            text_6.status = FINISHED
                            text_6.setAutoDraw(False)
                    # Run 'Each Frame' code from Box18_3
                    grayBox.draw()
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        Blank_4.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Blank_4.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Blank_4" ---
                for thisComponent in Blank_4.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for Blank_4
                Blank_4.tStop = globalClock.getTime(format='float')
                Blank_4.tStopRefresh = tThisFlipGlobal
                thisExp.addData('Blank_4.stopped', Blank_4.tStop)
                # Run 'End Routine' code from Timer_5
                time_trialEnd = globalClock.getTime()
                
                thisExp.addData('Pre_ISI_End', time_trialEnd)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if Blank_4.maxDurationReached:
                    routineTimer.addTime(-Blank_4.maxDuration)
                elif Blank_4.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.050000)
                
                # --- Prepare to start Routine "EmotTrial" ---
                # create an object to store info about Routine EmotTrial
                EmotTrial = data.Routine(
                    name='EmotTrial',
                    components=[key_resp, FaceSet, Colour],
                )
                EmotTrial.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # create starting attributes for key_resp
                key_resp.keys = []
                key_resp.rt = []
                _key_resp_allKeys = []
                FaceSet.setSize((0.3, 0.125))
                FaceSet.setImage(FaceE)
                Colour.setOpacity(0.25)
                Colour.setSize((0.3, 0.125))
                Colour.setImage(ColourF)
                # Run 'Begin Routine' code from Timer_2
                time_trialBegin = globalClock.getTime()
                
                if TaskVersion in ('1', '2'):
                
                    el_tracker.sendMessage('!V STIMULUS_DISPLAY TRIAL_NO %s' % Trial_No)
                    el_tracker.sendMessage('!V STIMULUS_DISPLAY TRIAL_TYPE %s' % Trial_Type)
                    el_tracker.sendMessage('!V STIMULUS_DISPLAY EXPRESS %s' % Express)
                    el_tracker.sendMessage('!V STIMULUS_DISPLAY FACE_LUM %s' % FaceE_Luminance)
                    el_tracker.sendMessage('!V STIMULUS_DISPLAY COLOUR_LUM %s' % Colour_Luminance)
                
                
                # store start times for EmotTrial
                EmotTrial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                EmotTrial.tStart = globalClock.getTime(format='float')
                EmotTrial.status = STARTED
                thisExp.addData('EmotTrial.started', EmotTrial.tStart)
                EmotTrial.maxDuration = None
                # keep track of which components have finished
                EmotTrialComponents = EmotTrial.components
                for thisComponent in EmotTrial.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "EmotTrial" ---
                # if trial has changed, end Routine now
                if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
                    continueRoutine = False
                EmotTrial.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.45:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *key_resp* updates
                    waitOnFlip = False
                    
                    # if key_resp is starting this frame...
                    if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp.frameNStart = frameN  # exact frame index
                        key_resp.tStart = t  # local t and not account for scr refresh
                        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp.started')
                        # update status
                        key_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if key_resp is stopping this frame...
                    if key_resp.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > key_resp.tStartRefresh + 0.45-frameTolerance:
                            # keep track of stop time/frame for later
                            key_resp.tStop = t  # not accounting for scr refresh
                            key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                            key_resp.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'key_resp.stopped')
                            # update status
                            key_resp.status = FINISHED
                            key_resp.status = FINISHED
                    if key_resp.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp.getKeys(keyList=['space', 'None'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_allKeys.extend(theseKeys)
                        if len(_key_resp_allKeys):
                            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                            key_resp.rt = _key_resp_allKeys[-1].rt
                            key_resp.duration = _key_resp_allKeys[-1].duration
                            # was this correct?
                            if (key_resp.keys == str(CorrectAnsP)) or (key_resp.keys == CorrectAnsP):
                                key_resp.corr = 1
                            else:
                                key_resp.corr = 0
                    
                    # *FaceSet* updates
                    
                    # if FaceSet is starting this frame...
                    if FaceSet.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        FaceSet.frameNStart = frameN  # exact frame index
                        FaceSet.tStart = t  # local t and not account for scr refresh
                        FaceSet.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(FaceSet, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'FaceSet.started')
                        # update status
                        FaceSet.status = STARTED
                        FaceSet.setAutoDraw(True)
                    
                    # if FaceSet is active this frame...
                    if FaceSet.status == STARTED:
                        # update params
                        pass
                    
                    # if FaceSet is stopping this frame...
                    if FaceSet.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > FaceSet.tStartRefresh + 0.45-frameTolerance:
                            # keep track of stop time/frame for later
                            FaceSet.tStop = t  # not accounting for scr refresh
                            FaceSet.tStopRefresh = tThisFlipGlobal  # on global time
                            FaceSet.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'FaceSet.stopped')
                            # update status
                            FaceSet.status = FINISHED
                            FaceSet.setAutoDraw(False)
                    
                    # *Colour* updates
                    
                    # if Colour is starting this frame...
                    if Colour.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        Colour.frameNStart = frameN  # exact frame index
                        Colour.tStart = t  # local t and not account for scr refresh
                        Colour.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Colour, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Colour.started')
                        # update status
                        Colour.status = STARTED
                        Colour.setAutoDraw(True)
                    
                    # if Colour is active this frame...
                    if Colour.status == STARTED:
                        # update params
                        pass
                    
                    # if Colour is stopping this frame...
                    if Colour.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Colour.tStartRefresh + 0.45-frameTolerance:
                            # keep track of stop time/frame for later
                            Colour.tStop = t  # not accounting for scr refresh
                            Colour.tStopRefresh = tThisFlipGlobal  # on global time
                            Colour.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Colour.stopped')
                            # update status
                            Colour.status = FINISHED
                            Colour.setAutoDraw(False)
                    # Run 'Each Frame' code from Box17
                    grayBox.draw()
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        EmotTrial.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in EmotTrial.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "EmotTrial" ---
                for thisComponent in EmotTrial.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for EmotTrial
                EmotTrial.tStop = globalClock.getTime(format='float')
                EmotTrial.tStopRefresh = tThisFlipGlobal
                thisExp.addData('EmotTrial.stopped', EmotTrial.tStop)
                # check responses
                if key_resp.keys in ['', [], None]:  # No response was made
                    key_resp.keys = None
                    # was no response the correct answer?!
                    if str(CorrectAnsP).lower() == 'none':
                       key_resp.corr = 1;  # correct non-response
                    else:
                       key_resp.corr = 0;  # failed to respond (incorrectly)
                # store data for InnerLoop (TrialHandler)
                InnerLoop.addData('key_resp.keys',key_resp.keys)
                InnerLoop.addData('key_resp.corr', key_resp.corr)
                if key_resp.keys != None:  # we had a response
                    InnerLoop.addData('key_resp.rt', key_resp.rt)
                    InnerLoop.addData('key_resp.duration', key_resp.duration)
                # Run 'End Routine' code from Timer_2
                time_trialEnd = globalClock.getTime()
                
                thisExp.addData('Stimulus_Display_Start', time_trialBegin)
                thisExp.addData('Stimulus_Display_End', time_trialEnd)
                
                if TaskVersion in ('1', '2'):
                    if key_resp.keys == 'space' and CorrectAnsP == 'space':
                        el_tracker.sendMessage("STIMULUS DISPLAY CORRECT GO")
                        
                    if key_resp.keys == 'space' and CorrectAnsP == 'None':
                        el_tracker.sendMessage("STIMULUS DISPLAY INCORRECT GO")
                        
                    if key_resp.keys == '' and CorrectAnsP == 'space':
                        el_tracker.sendMessage("STIMULUS DISPLAY INCORRECT NOGO")
                        
                    if key_resp.keys == '' and CorrectAnsP == 'None':
                        el_tracker.sendMessage("STIMULUS DISPLAY CORRECT NOGO")
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if EmotTrial.maxDurationReached:
                    routineTimer.addTime(-EmotTrial.maxDuration)
                elif EmotTrial.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.450000)
                
                # --- Prepare to start Routine "Blank_2" ---
                # create an object to store info about Routine Blank_2
                Blank_2 = data.Routine(
                    name='Blank_2',
                    components=[text_4],
                )
                Blank_2.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from Timer_4
                time_trialBegin = globalClock.getTime()
                
                el_tracker.sendMessage('!V POST_ISI TRIAL_NO %s' % Trial_No)
                el_tracker.sendMessage('!V POST_ISI TRIAL_TYPE %s' % Trial_Type)
                el_tracker.sendMessage('!V POST_ISI EXPRESS %s' % Express)
                el_tracker.sendMessage('!V POST_ISI FACE_LUM %s' % FaceE_Luminance)
                el_tracker.sendMessage('!V POST_ISI COLOUR_LUM %s' % Colour_Luminance)
                
                if TaskVersion in ('1', '2'):
                    if key_resp.corr == '1' and Trial_Type == 'Go':
                        el_tracker.sendMessage("POST_ISI CORRECT GO")
                        
                    if key_resp.corr == '0' and Trial_Type == 'Go':
                        el_tracker.sendMessage("POST_ISI INCORRECT GO")
                        
                    if key_resp.corr == '0' and Trial_Type == 'Inhibit':
                        el_tracker.sendMessage("POST_ISI INCORRECT NOGO")
                        
                    if key_resp.corr == '1' and Trial_Type == 'Inhibit':
                        el_tracker.sendMessage("POST_ISI CORRECT NOGO")
                
                # store start times for Blank_2
                Blank_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                Blank_2.tStart = globalClock.getTime(format='float')
                Blank_2.status = STARTED
                thisExp.addData('Blank_2.started', Blank_2.tStart)
                Blank_2.maxDuration = None
                # keep track of which components have finished
                Blank_2Components = Blank_2.components
                for thisComponent in Blank_2.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Blank_2" ---
                # if trial has changed, end Routine now
                if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
                    continueRoutine = False
                Blank_2.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.05:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_4* updates
                    
                    # if text_4 is starting this frame...
                    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_4.frameNStart = frameN  # exact frame index
                        text_4.tStart = t  # local t and not account for scr refresh
                        text_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_4.started')
                        # update status
                        text_4.status = STARTED
                        text_4.setAutoDraw(True)
                    
                    # if text_4 is active this frame...
                    if text_4.status == STARTED:
                        # update params
                        pass
                    
                    # if text_4 is stopping this frame...
                    if text_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_4.tStartRefresh + 0.05-frameTolerance:
                            # keep track of stop time/frame for later
                            text_4.tStop = t  # not accounting for scr refresh
                            text_4.tStopRefresh = tThisFlipGlobal  # on global time
                            text_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_4.stopped')
                            # update status
                            text_4.status = FINISHED
                            text_4.setAutoDraw(False)
                    # Run 'Each Frame' code from Box18
                    grayBox.draw()
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        Blank_2.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Blank_2.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Blank_2" ---
                for thisComponent in Blank_2.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for Blank_2
                Blank_2.tStop = globalClock.getTime(format='float')
                Blank_2.tStopRefresh = tThisFlipGlobal
                thisExp.addData('Blank_2.stopped', Blank_2.tStop)
                # Run 'End Routine' code from Timer_4
                time_trialEnd = globalClock.getTime()
                
                thisExp.addData('Post_ISI_Start', time_trialBegin)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if Blank_2.maxDurationReached:
                    routineTimer.addTime(-Blank_2.maxDuration)
                elif Blank_2.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.050000)
                
                # --- Prepare to start Routine "ISI_3" ---
                # create an object to store info about Routine ISI_3
                ISI_3 = data.Routine(
                    name='ISI_3',
                    components=[Post_ISI_Text],
                )
                ISI_3.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # store start times for ISI_3
                ISI_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                ISI_3.tStart = globalClock.getTime(format='float')
                ISI_3.status = STARTED
                thisExp.addData('ISI_3.started', ISI_3.tStart)
                ISI_3.maxDuration = None
                # keep track of which components have finished
                ISI_3Components = ISI_3.components
                for thisComponent in ISI_3.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "ISI_3" ---
                # if trial has changed, end Routine now
                if isinstance(InnerLoop, data.TrialHandler2) and thisInnerLoop.thisN != InnerLoop.thisTrial.thisN:
                    continueRoutine = False
                ISI_3.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *Post_ISI_Text* updates
                    
                    # if Post_ISI_Text is starting this frame...
                    if Post_ISI_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Post_ISI_Text.frameNStart = frameN  # exact frame index
                        Post_ISI_Text.tStart = t  # local t and not account for scr refresh
                        Post_ISI_Text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Post_ISI_Text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Post_ISI_Text.started')
                        # update status
                        Post_ISI_Text.status = STARTED
                        Post_ISI_Text.setAutoDraw(True)
                    
                    # if Post_ISI_Text is active this frame...
                    if Post_ISI_Text.status == STARTED:
                        # update params
                        pass
                    
                    # if Post_ISI_Text is stopping this frame...
                    if Post_ISI_Text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Post_ISI_Text.tStartRefresh + POST_ISI-frameTolerance:
                            # keep track of stop time/frame for later
                            Post_ISI_Text.tStop = t  # not accounting for scr refresh
                            Post_ISI_Text.tStopRefresh = tThisFlipGlobal  # on global time
                            Post_ISI_Text.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Post_ISI_Text.stopped')
                            # update status
                            Post_ISI_Text.status = FINISHED
                            Post_ISI_Text.setAutoDraw(False)
                    # Run 'Each Frame' code from Box19
                    grayBox.draw()
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        ISI_3.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in ISI_3.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "ISI_3" ---
                for thisComponent in ISI_3.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for ISI_3
                ISI_3.tStop = globalClock.getTime(format='float')
                ISI_3.tStopRefresh = tThisFlipGlobal
                thisExp.addData('ISI_3.stopped', ISI_3.tStop)
                # Run 'End Routine' code from Timer_3
                time_trialEnd = globalClock.getTime()
                
                if TaskVersion in ('1', '2'):
                
                    el_tracker.sendMessage('!V TRIAL END%s')
                    el_tracker.sendMessage(f"TRIAL_TIME_END {time_trialEnd:.3f}")
                
                thisExp.addData('Post_ISI_End', time_trialEnd)
                
                
                # the Routine "ISI_3" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 repeats of 'InnerLoop'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # --- Prepare to start Routine "End_Record" ---
            # create an object to store info about Routine End_Record
            End_Record = data.Routine(
                name='End_Record',
                components=[],
            )
            End_Record.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for End_Record
            End_Record.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            End_Record.tStart = globalClock.getTime(format='float')
            End_Record.status = STARTED
            thisExp.addData('End_Record.started', End_Record.tStart)
            End_Record.maxDuration = None
            # keep track of which components have finished
            End_RecordComponents = End_Record.components
            for thisComponent in End_Record.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "End_Record" ---
            # if trial has changed, end Routine now
            if isinstance(OuterLoop, data.TrialHandler2) and thisOuterLoop.thisN != OuterLoop.thisTrial.thisN:
                continueRoutine = False
            End_Record.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    End_Record.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in End_Record.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "End_Record" ---
            for thisComponent in End_Record.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for End_Record
            End_Record.tStop = globalClock.getTime(format='float')
            End_Record.tStopRefresh = tThisFlipGlobal
            thisExp.addData('End_Record.stopped', End_Record.tStop)
            # Run 'End Routine' code from End_Record_2
            # This End Routine tab of the elStopRecord component stops eye tracker recording
            
            if TaskVersion in ('1', '2'):
                core.wait(0.5)
            
                # stop recording; add 100 msec to catch final events before stopping
                el_tracker.sendMessage('!V END_BLOCK')
                el_tracker.sendMessage('!V RECORDING_END_BLOCK %s' % BlockNo)
                pylink.pumpDelay(100)
                el_tracker.stopRecording()
            
                core.wait(0.5)
            
                # Optional clean-up on the Host display
                el_tracker.sendCommand('clear_screen 0')             # Clear host display
                el_tracker.sendMessage('!V CLEAR 128 128 128')       # Clear overlay in Data Viewer
            
                continueRoutine = False
            # the Routine "End_Record" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Add2" ---
            # create an object to store info about Routine Add2
            Add2 = data.Routine(
                name='Add2',
                components=[],
            )
            Add2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_7
            BlockNo = BlockNo + 1
            # store start times for Add2
            Add2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Add2.tStart = globalClock.getTime(format='float')
            Add2.status = STARTED
            thisExp.addData('Add2.started', Add2.tStart)
            Add2.maxDuration = None
            # keep track of which components have finished
            Add2Components = Add2.components
            for thisComponent in Add2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Add2" ---
            # if trial has changed, end Routine now
            if isinstance(OuterLoop, data.TrialHandler2) and thisOuterLoop.thisN != OuterLoop.thisTrial.thisN:
                continueRoutine = False
            Add2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Add2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Add2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Add2" ---
            for thisComponent in Add2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Add2
            Add2.tStop = globalClock.getTime(format='float')
            Add2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Add2.stopped', Add2.tStop)
            # the Routine "Add2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "EndBlock" ---
            # create an object to store info about Routine EndBlock
            EndBlock = data.Routine(
                name='EndBlock',
                components=[EndBlockText, key_resp_4, BreakText2, PressToContinue],
            )
            EndBlock.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for key_resp_4
            key_resp_4.keys = []
            key_resp_4.rt = []
            _key_resp_4_allKeys = []
            # Run 'Begin Routine' code from code_8
            if BlockNo <= 6:
               Breaktext = 'Please take a break if needed.'
            else:
               Breaktext = '' 
            BreakText2.setText(Breaktext)
            PressToContinue.setText("Please press 'spacebar' to continue.")
            # Run 'Begin Routine' code from ContRouteMidLogic
            if BlockNo == 4:
                continueRoutine = False
            # store start times for EndBlock
            EndBlock.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            EndBlock.tStart = globalClock.getTime(format='float')
            EndBlock.status = STARTED
            thisExp.addData('EndBlock.started', EndBlock.tStart)
            EndBlock.maxDuration = None
            # keep track of which components have finished
            EndBlockComponents = EndBlock.components
            for thisComponent in EndBlock.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "EndBlock" ---
            # if trial has changed, end Routine now
            if isinstance(OuterLoop, data.TrialHandler2) and thisOuterLoop.thisN != OuterLoop.thisTrial.thisN:
                continueRoutine = False
            EndBlock.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *EndBlockText* updates
                
                # if EndBlockText is starting this frame...
                if EndBlockText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    EndBlockText.frameNStart = frameN  # exact frame index
                    EndBlockText.tStart = t  # local t and not account for scr refresh
                    EndBlockText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(EndBlockText, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'EndBlockText.started')
                    # update status
                    EndBlockText.status = STARTED
                    EndBlockText.setAutoDraw(True)
                
                # if EndBlockText is active this frame...
                if EndBlockText.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_4* updates
                waitOnFlip = False
                
                # if key_resp_4 is starting this frame...
                if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.tStart = t  # local t and not account for scr refresh
                    key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_4.started')
                    # update status
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_4.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_4_allKeys.extend(theseKeys)
                    if len(_key_resp_4_allKeys):
                        key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                        key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                        key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *BreakText2* updates
                
                # if BreakText2 is starting this frame...
                if BreakText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BreakText2.frameNStart = frameN  # exact frame index
                    BreakText2.tStart = t  # local t and not account for scr refresh
                    BreakText2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BreakText2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'BreakText2.started')
                    # update status
                    BreakText2.status = STARTED
                    BreakText2.setAutoDraw(True)
                
                # if BreakText2 is active this frame...
                if BreakText2.status == STARTED:
                    # update params
                    pass
                
                # *PressToContinue* updates
                
                # if PressToContinue is starting this frame...
                if PressToContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    PressToContinue.frameNStart = frameN  # exact frame index
                    PressToContinue.tStart = t  # local t and not account for scr refresh
                    PressToContinue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PressToContinue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PressToContinue.started')
                    # update status
                    PressToContinue.status = STARTED
                    PressToContinue.setAutoDraw(True)
                
                # if PressToContinue is active this frame...
                if PressToContinue.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from Box20
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    EndBlock.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in EndBlock.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "EndBlock" ---
            for thisComponent in EndBlock.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for EndBlock
            EndBlock.tStop = globalClock.getTime(format='float')
            EndBlock.tStopRefresh = tThisFlipGlobal
            thisExp.addData('EndBlock.stopped', EndBlock.tStop)
            # check responses
            if key_resp_4.keys in ['', [], None]:  # No response was made
                key_resp_4.keys = None
            OuterLoop.addData('key_resp_4.keys',key_resp_4.keys)
            if key_resp_4.keys != None:  # we had a response
                OuterLoop.addData('key_resp_4.rt', key_resp_4.rt)
                OuterLoop.addData('key_resp_4.duration', key_resp_4.duration)
            # the Routine "EndBlock" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Recalib_Text" ---
            # create an object to store info about Routine Recalib_Text
            Recalib_Text = data.Routine(
                name='Recalib_Text',
                components=[Break_Text],
            )
            Recalib_Text.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Skip_Routine_1
            if BlockNo != 4:
                continueRoutine = False
            # store start times for Recalib_Text
            Recalib_Text.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Recalib_Text.tStart = globalClock.getTime(format='float')
            Recalib_Text.status = STARTED
            thisExp.addData('Recalib_Text.started', Recalib_Text.tStart)
            Recalib_Text.maxDuration = None
            # keep track of which components have finished
            Recalib_TextComponents = Recalib_Text.components
            for thisComponent in Recalib_Text.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Recalib_Text" ---
            # if trial has changed, end Routine now
            if isinstance(OuterLoop, data.TrialHandler2) and thisOuterLoop.thisN != OuterLoop.thisTrial.thisN:
                continueRoutine = False
            Recalib_Text.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 180.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Break_Text* updates
                
                # if Break_Text is starting this frame...
                if Break_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Break_Text.frameNStart = frameN  # exact frame index
                    Break_Text.tStart = t  # local t and not account for scr refresh
                    Break_Text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Break_Text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Break_Text.started')
                    # update status
                    Break_Text.status = STARTED
                    Break_Text.setAutoDraw(True)
                
                # if Break_Text is active this frame...
                if Break_Text.status == STARTED:
                    # update params
                    pass
                
                # if Break_Text is stopping this frame...
                if Break_Text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Break_Text.tStartRefresh + 180-frameTolerance:
                        # keep track of stop time/frame for later
                        Break_Text.tStop = t  # not accounting for scr refresh
                        Break_Text.tStopRefresh = tThisFlipGlobal  # on global time
                        Break_Text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Break_Text.stopped')
                        # update status
                        Break_Text.status = FINISHED
                        Break_Text.setAutoDraw(False)
                # Run 'Each Frame' code from Box21
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Recalib_Text.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Recalib_Text.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Recalib_Text" ---
            for thisComponent in Recalib_Text.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Recalib_Text
            Recalib_Text.tStop = globalClock.getTime(format='float')
            Recalib_Text.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Recalib_Text.stopped', Recalib_Text.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Recalib_Text.maxDurationReached:
                routineTimer.addTime(-Recalib_Text.maxDuration)
            elif Recalib_Text.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-180.000000)
            
            # --- Prepare to start Routine "Recalib_Text_2" ---
            # create an object to store info about Routine Recalib_Text_2
            Recalib_Text_2 = data.Routine(
                name='Recalib_Text_2',
                components=[End_Break_Text, Calib_keys_1],
            )
            Recalib_Text_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Skip_Routine_2
            if BlockNo != 4:
                continueRoutine = False
            # create starting attributes for Calib_keys_1
            Calib_keys_1.keys = []
            Calib_keys_1.rt = []
            _Calib_keys_1_allKeys = []
            # store start times for Recalib_Text_2
            Recalib_Text_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Recalib_Text_2.tStart = globalClock.getTime(format='float')
            Recalib_Text_2.status = STARTED
            thisExp.addData('Recalib_Text_2.started', Recalib_Text_2.tStart)
            Recalib_Text_2.maxDuration = None
            # keep track of which components have finished
            Recalib_Text_2Components = Recalib_Text_2.components
            for thisComponent in Recalib_Text_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Recalib_Text_2" ---
            # if trial has changed, end Routine now
            if isinstance(OuterLoop, data.TrialHandler2) and thisOuterLoop.thisN != OuterLoop.thisTrial.thisN:
                continueRoutine = False
            Recalib_Text_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *End_Break_Text* updates
                
                # if End_Break_Text is starting this frame...
                if End_Break_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    End_Break_Text.frameNStart = frameN  # exact frame index
                    End_Break_Text.tStart = t  # local t and not account for scr refresh
                    End_Break_Text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(End_Break_Text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'End_Break_Text.started')
                    # update status
                    End_Break_Text.status = STARTED
                    End_Break_Text.setAutoDraw(True)
                
                # if End_Break_Text is active this frame...
                if End_Break_Text.status == STARTED:
                    # update params
                    pass
                
                # *Calib_keys_1* updates
                waitOnFlip = False
                
                # if Calib_keys_1 is starting this frame...
                if Calib_keys_1.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                    # keep track of start time/frame for later
                    Calib_keys_1.frameNStart = frameN  # exact frame index
                    Calib_keys_1.tStart = t  # local t and not account for scr refresh
                    Calib_keys_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Calib_keys_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Calib_keys_1.started')
                    # update status
                    Calib_keys_1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Calib_keys_1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Calib_keys_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Calib_keys_1.status == STARTED and not waitOnFlip:
                    theseKeys = Calib_keys_1.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _Calib_keys_1_allKeys.extend(theseKeys)
                    if len(_Calib_keys_1_allKeys):
                        Calib_keys_1.keys = _Calib_keys_1_allKeys[-1].name  # just the last key pressed
                        Calib_keys_1.rt = _Calib_keys_1_allKeys[-1].rt
                        Calib_keys_1.duration = _Calib_keys_1_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                # Run 'Each Frame' code from Box22
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Recalib_Text_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Recalib_Text_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Recalib_Text_2" ---
            for thisComponent in Recalib_Text_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Recalib_Text_2
            Recalib_Text_2.tStop = globalClock.getTime(format='float')
            Recalib_Text_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Recalib_Text_2.stopped', Recalib_Text_2.tStop)
            # the Routine "Recalib_Text_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Recalib" ---
            # create an object to store info about Routine Recalib
            Recalib = data.Routine(
                name='Recalib',
                components=[],
            )
            Recalib.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Recal_Code
            if BlockNo == 4:
                if TaskVersion in ('1', '2'):
                    el_tracker.doTrackerSetup()
                    ContinueRoutine = True
                else:
                    ContinueRoutine = False
            else:
                ContinueRoutine = False
            
            # store start times for Recalib
            Recalib.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Recalib.tStart = globalClock.getTime(format='float')
            Recalib.status = STARTED
            thisExp.addData('Recalib.started', Recalib.tStart)
            Recalib.maxDuration = None
            # keep track of which components have finished
            RecalibComponents = Recalib.components
            for thisComponent in Recalib.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Recalib" ---
            # if trial has changed, end Routine now
            if isinstance(OuterLoop, data.TrialHandler2) and thisOuterLoop.thisN != OuterLoop.thisTrial.thisN:
                continueRoutine = False
            Recalib.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Recalib.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Recalib.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Recalib" ---
            for thisComponent in Recalib.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Recalib
            Recalib.tStop = globalClock.getTime(format='float')
            Recalib.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Recalib.stopped', Recalib.tStop)
            # the Routine "Recalib" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Drift_Check" ---
            # create an object to store info about Routine Drift_Check
            Drift_Check = data.Routine(
                name='Drift_Check',
                components=[],
            )
            Drift_Check.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for Drift_Check
            Drift_Check.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Drift_Check.tStart = globalClock.getTime(format='float')
            Drift_Check.status = STARTED
            thisExp.addData('Drift_Check.started', Drift_Check.tStart)
            Drift_Check.maxDuration = None
            # keep track of which components have finished
            Drift_CheckComponents = Drift_Check.components
            for thisComponent in Drift_Check.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Drift_Check" ---
            # if trial has changed, end Routine now
            if isinstance(OuterLoop, data.TrialHandler2) and thisOuterLoop.thisN != OuterLoop.thisTrial.thisN:
                continueRoutine = False
            Drift_Check.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Drift_Check.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Drift_Check.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Drift_Check" ---
            for thisComponent in Drift_Check.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Drift_Check
            Drift_Check.tStop = globalClock.getTime(format='float')
            Drift_Check.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Drift_Check.stopped', Drift_Check.tStop)
            # the Routine "Drift_Check" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "End_Calib_Text" ---
            # create an object to store info about Routine End_Calib_Text
            End_Calib_Text = data.Routine(
                name='End_Calib_Text',
                components=[Recalib_Text_3, Recalib_keys_2],
            )
            End_Calib_Text.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Skip_Routine_5
            if BlockNo != 4:
                continueRoutine = False
            # create starting attributes for Recalib_keys_2
            Recalib_keys_2.keys = []
            Recalib_keys_2.rt = []
            _Recalib_keys_2_allKeys = []
            # store start times for End_Calib_Text
            End_Calib_Text.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            End_Calib_Text.tStart = globalClock.getTime(format='float')
            End_Calib_Text.status = STARTED
            thisExp.addData('End_Calib_Text.started', End_Calib_Text.tStart)
            End_Calib_Text.maxDuration = None
            # keep track of which components have finished
            End_Calib_TextComponents = End_Calib_Text.components
            for thisComponent in End_Calib_Text.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "End_Calib_Text" ---
            # if trial has changed, end Routine now
            if isinstance(OuterLoop, data.TrialHandler2) and thisOuterLoop.thisN != OuterLoop.thisTrial.thisN:
                continueRoutine = False
            End_Calib_Text.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Recalib_Text_3* updates
                
                # if Recalib_Text_3 is starting this frame...
                if Recalib_Text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Recalib_Text_3.frameNStart = frameN  # exact frame index
                    Recalib_Text_3.tStart = t  # local t and not account for scr refresh
                    Recalib_Text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Recalib_Text_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Recalib_Text_3.started')
                    # update status
                    Recalib_Text_3.status = STARTED
                    Recalib_Text_3.setAutoDraw(True)
                
                # if Recalib_Text_3 is active this frame...
                if Recalib_Text_3.status == STARTED:
                    # update params
                    pass
                
                # *Recalib_keys_2* updates
                waitOnFlip = False
                
                # if Recalib_keys_2 is starting this frame...
                if Recalib_keys_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                    # keep track of start time/frame for later
                    Recalib_keys_2.frameNStart = frameN  # exact frame index
                    Recalib_keys_2.tStart = t  # local t and not account for scr refresh
                    Recalib_keys_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Recalib_keys_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Recalib_keys_2.started')
                    # update status
                    Recalib_keys_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Recalib_keys_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Recalib_keys_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Recalib_keys_2.status == STARTED and not waitOnFlip:
                    theseKeys = Recalib_keys_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _Recalib_keys_2_allKeys.extend(theseKeys)
                    if len(_Recalib_keys_2_allKeys):
                        Recalib_keys_2.keys = _Recalib_keys_2_allKeys[-1].name  # just the last key pressed
                        Recalib_keys_2.rt = _Recalib_keys_2_allKeys[-1].rt
                        Recalib_keys_2.duration = _Recalib_keys_2_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                # Run 'Each Frame' code from Box23
                grayBox.draw()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    End_Calib_Text.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in End_Calib_Text.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "End_Calib_Text" ---
            for thisComponent in End_Calib_Text.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for End_Calib_Text
            End_Calib_Text.tStop = globalClock.getTime(format='float')
            End_Calib_Text.tStopRefresh = tThisFlipGlobal
            thisExp.addData('End_Calib_Text.stopped', End_Calib_Text.tStop)
            # the Routine "End_Calib_Text" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 1 repeats of 'OuterLoop'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'MasterLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "EndEmotionTask" ---
    # create an object to store info about Routine EndEmotionTask
    EndEmotionTask = data.Routine(
        name='EndEmotionTask',
        components=[End_Text],
    )
    EndEmotionTask.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Eyetracker_Send
    # Assume `el_tracker` and `edf_fname` are already defined
    
    if TaskVersion in ('1', '2'):
        if el_tracker.isConnected():
            el_tracker.setOfflineMode()
            pylink.msecDelay(500)
    
            try:
                el_tracker.closeDataFile()
            except RuntimeError as err:
                print("Error closing EDF on Host:", err)
    
            print("Transferring EDF file from Host...")
    
            # Define where to save locally
            local_path = f"eyetracker_data/{edf_fname}.EDF"  # or any path you want
    
            try:
                el_tracker.receiveDataFile(edf_fname + ".EDF", local_path)
                print(f"EDF successfully saved to {local_path}")
            except RuntimeError as err:
                print("Error downloading EDF:", err)
    
            el_tracker.close()
    
    # store start times for EndEmotionTask
    EndEmotionTask.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EndEmotionTask.tStart = globalClock.getTime(format='float')
    EndEmotionTask.status = STARTED
    thisExp.addData('EndEmotionTask.started', EndEmotionTask.tStart)
    EndEmotionTask.maxDuration = None
    # keep track of which components have finished
    EndEmotionTaskComponents = EndEmotionTask.components
    for thisComponent in EndEmotionTask.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndEmotionTask" ---
    EndEmotionTask.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *End_Text* updates
        
        # if End_Text is starting this frame...
        if End_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            End_Text.frameNStart = frameN  # exact frame index
            End_Text.tStart = t  # local t and not account for scr refresh
            End_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(End_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'End_Text.started')
            # update status
            End_Text.status = STARTED
            End_Text.setAutoDraw(True)
        
        # if End_Text is active this frame...
        if End_Text.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from Box24
        grayBox.draw()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EndEmotionTask.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndEmotionTask.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndEmotionTask" ---
    for thisComponent in EndEmotionTask.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EndEmotionTask
    EndEmotionTask.tStop = globalClock.getTime(format='float')
    EndEmotionTask.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EndEmotionTask.stopped', EndEmotionTask.tStop)
    thisExp.nextEntry()
    # the Routine "EndEmotionTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
