#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on July 21, 2021, at 12:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'Go No-Go Task'  # from the Builder filename that created this script
expInfo = {'participant': 'P000', 'Study Name': '', 'Task Version (required to run)': '1 or 2', 'PRE/POST': 'Pre or Post'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mcolwell\\Desktop\\Cognitive Task Battery\\2. Go No Go\\Emotional Go No-Go Task (Psychopy)\\Emotional Go No-Go Task (v1.2)_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Hard_Script"
Hard_ScriptClock = core.Clock()
win.setMouseVisible(False)
BlockNo = 1
PractNo = 1
TaskVersion = expInfo['Task Version (required to run)'] 

TaskVersion = TaskVersion.replace(' ', '')

if TaskVersion == '1':
        VersionSelection = 'ParentConditions/ConditionsMaster_v1.xlsx'
       
        
if TaskVersion == '2':
        VersionSelection = 'ParentConditions/ConditionsMaster_v2.xlsx'

# Initialize components for Routine "VersionNoDisplay"
VersionNoDisplayClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "EmotionTaskInstructions"
EmotionTaskInstructionsClock = core.Clock()
text4 = visual.TextStim(win=win, name='text4',
    text='',
    font='Arial',
    pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
EmotionTaskInstructions1 = keyboard.Keyboard()

# Initialize components for Routine "EmotionalTaskInstructions2"
EmotionalTaskInstructions2Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Arial',
    pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "EmotionalTaskInstructions3"
EmotionalTaskInstructions3Clock = core.Clock()
Text_14 = visual.TextStim(win=win, name='Text_14',
    text="Rules are given at the start and change throughout.\n\nThe experiment will pause when instructed with a new rule.\n\nYou will now enter practice before the real task.\n\nPlease press 'spacebar' to begin practice.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "EPracticeInstructions2"
EPracticeInstructions2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Arial',
    pos=(0, -0.10), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Arial',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_7 = keyboard.Keyboard()
text_10 = visual.TextStim(win=win, name='text_10',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='Practice block:',
    font='Arial',
    pos=(-0.089, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='of 4',
    font='Arial',
    pos=(0.163, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "EPracticeISI"
EPracticeISIClock = core.Clock()
EPracticeISIMarker = visual.TextStim(win=win, name='EPracticeISIMarker',
    text='',
    font='Arial',
    pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "EPracticeTrial"
EPracticeTrialClock = core.Clock()
Pract = keyboard.Keyboard()
PracticeFace = visual.ImageStim(
    win=win,
    name='PracticeFace', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.7, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
ColourPractice = visual.ImageStim(
    win=win,
    name='ColourPractice', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "PracticeFeedbackBlock"
PracticeFeedbackBlockClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='',
    font='Arial',
    pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Add"
AddClock = core.Clock()

# Initialize components for Routine "EndPracticeEndInstructions"
EndPracticeEndInstructionsClock = core.Clock()
EndOfPractice = visual.TextStim(win=win, name='EndOfPractice',
    text='',
    font='Arial',
    pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "RealTaskPreInstructions"
RealTaskPreInstructionsClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text="You will now begin the real task. \n\nPlease press 'spacebar' to continue.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Instructions_2"
Instructions_2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()
TaskBlock = visual.TextStim(win=win, name='TaskBlock',
    text='',
    font='Arial',
    pos=(-0.07, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
BlockNo1 = visual.TextStim(win=win, name='BlockNo1',
    text='',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
OfBlock = visual.TextStim(win=win, name='OfBlock',
    text='',
    font='Arial',
    pos=(0.17, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "ISI_2"
ISI_2Clock = core.Clock()
ISImarker = visual.TextStim(win=win, name='ISImarker',
    text='',
    font='Arial',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "EmotTrial"
EmotTrialClock = core.Clock()
key_resp = keyboard.Keyboard()
FaceSet = visual.ImageStim(
    win=win,
    name='FaceSet', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Colour = visual.ImageStim(
    win=win,
    name='Colour', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "Add2"
Add2Clock = core.Clock()

# Initialize components for Routine "EndBlock"
EndBlockClock = core.Clock()
EndBlockText = visual.TextStim(win=win, name='EndBlockText',
    text='End of block.',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
BreakText2 = visual.TextStim(win=win, name='BreakText2',
    text='',
    font='Arial',
    pos=(0, -0.10), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
PressToContinue = visual.TextStim(win=win, name='PressToContinue',
    text='',
    font='Arial',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "EndEmotionTask"
EndEmotionTaskClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text="End of test.\n\nThank you for participating. \n\nPlease inform the researcher of your completion.\n\nPress 'escape' to close.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Hard_Script"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Hard_ScriptComponents = []
for thisComponent in Hard_ScriptComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Hard_ScriptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Hard_Script"-------
while continueRoutine:
    # get current time
    t = Hard_ScriptClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Hard_ScriptClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Hard_ScriptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Hard_Script"-------
for thisComponent in Hard_ScriptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Hard_Script" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "VersionNoDisplay"-------
continueRoutine = True
# update component parameters for each repeat
VersionT = ('This is the Go/No Go task version '+'"'+ TaskVersion + '"'
+'\n \n \n Please press spacebar to continue to the instructions.')
text_13.setText(VersionT)
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
VersionNoDisplayComponents = [text_13, key_resp_10]
for thisComponent in VersionNoDisplayComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VersionNoDisplayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VersionNoDisplay"-------
while continueRoutine:
    # get current time
    t = VersionNoDisplayClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VersionNoDisplayClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VersionNoDisplayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VersionNoDisplay"-------
for thisComponent in VersionNoDisplayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "VersionNoDisplay" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EmotionTaskInstructions"-------
continueRoutine = True
# update component parameters for each repeat
text4.setText("For this task, you will see a series of images appear onscreen. They will only appear for a short period of 300ms. \n\nYou must press spacebar when images appear onscreen. Failing to do so will result in a miss (incorrect) result.\n\nPlease press 'spacebar' to continue.")
text4.setHeight(0.04)
EmotionTaskInstructions1.keys = []
EmotionTaskInstructions1.rt = []
_EmotionTaskInstructions1_allKeys = []
# keep track of which components have finished
EmotionTaskInstructionsComponents = [text4, EmotionTaskInstructions1]
for thisComponent in EmotionTaskInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EmotionTaskInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EmotionTaskInstructions"-------
while continueRoutine:
    # get current time
    t = EmotionTaskInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EmotionTaskInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text4* updates
    if text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text4.frameNStart = frameN  # exact frame index
        text4.tStart = t  # local t and not account for scr refresh
        text4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text4, 'tStartRefresh')  # time at next scr refresh
        text4.setAutoDraw(True)
    
    # *EmotionTaskInstructions1* updates
    waitOnFlip = False
    if EmotionTaskInstructions1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EmotionTaskInstructions1.frameNStart = frameN  # exact frame index
        EmotionTaskInstructions1.tStart = t  # local t and not account for scr refresh
        EmotionTaskInstructions1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EmotionTaskInstructions1, 'tStartRefresh')  # time at next scr refresh
        EmotionTaskInstructions1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EmotionTaskInstructions1.clock.reset)  # t=0 on next screen flip
    if EmotionTaskInstructions1.status == STARTED and not waitOnFlip:
        theseKeys = EmotionTaskInstructions1.getKeys(keyList=['space'], waitRelease=False)
        _EmotionTaskInstructions1_allKeys.extend(theseKeys)
        if len(_EmotionTaskInstructions1_allKeys):
            EmotionTaskInstructions1.keys = _EmotionTaskInstructions1_allKeys[-1].name  # just the last key pressed
            EmotionTaskInstructions1.rt = _EmotionTaskInstructions1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EmotionTaskInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EmotionTaskInstructions"-------
for thisComponent in EmotionTaskInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text4.started', text4.tStartRefresh)
thisExp.addData('text4.stopped', text4.tStopRefresh)
# check responses
if EmotionTaskInstructions1.keys in ['', [], None]:  # No response was made
    EmotionTaskInstructions1.keys = None
thisExp.addData('EmotionTaskInstructions1.keys',EmotionTaskInstructions1.keys)
if EmotionTaskInstructions1.keys != None:  # we had a response
    thisExp.addData('EmotionTaskInstructions1.rt', EmotionTaskInstructions1.rt)
thisExp.addData('EmotionTaskInstructions1.started', EmotionTaskInstructions1.tStartRefresh)
thisExp.addData('EmotionTaskInstructions1.stopped', EmotionTaskInstructions1.tStopRefresh)
thisExp.nextEntry()
# the Routine "EmotionTaskInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EmotionalTaskInstructions2"-------
continueRoutine = True
# update component parameters for each repeat
text_4.setText("The images will have different features (eyes or blocks). You only need to focus on the colour of the image.\n\nYou need to press 'spacebar' for most images, but for some you must not. You will be instructed when not to by rules.\n\nPlease press 'spacebar' to continue.")
text_4.setHeight(0.04)
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
EmotionalTaskInstructions2Components = [text_4, key_resp_5]
for thisComponent in EmotionalTaskInstructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EmotionalTaskInstructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EmotionalTaskInstructions2"-------
while continueRoutine:
    # get current time
    t = EmotionalTaskInstructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EmotionalTaskInstructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EmotionalTaskInstructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EmotionalTaskInstructions2"-------
for thisComponent in EmotionalTaskInstructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "EmotionalTaskInstructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EmotionalTaskInstructions3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
EmotionalTaskInstructions3Components = [Text_14, key_resp_9]
for thisComponent in EmotionalTaskInstructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EmotionalTaskInstructions3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EmotionalTaskInstructions3"-------
while continueRoutine:
    # get current time
    t = EmotionalTaskInstructions3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EmotionalTaskInstructions3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Text_14* updates
    if Text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Text_14.frameNStart = frameN  # exact frame index
        Text_14.tStart = t  # local t and not account for scr refresh
        Text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Text_14, 'tStartRefresh')  # time at next scr refresh
        Text_14.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EmotionalTaskInstructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EmotionalTaskInstructions3"-------
for thisComponent in EmotionalTaskInstructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Text_14.started', Text_14.tStartRefresh)
thisExp.addData('Text_14.stopped', Text_14.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "EmotionalTaskInstructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
EPracticeOuterLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('EPracticeConditions/EPracticeMaster.xlsx'),
    seed=None, name='EPracticeOuterLoop')
thisExp.addLoop(EPracticeOuterLoop)  # add the loop to the experiment
thisEPracticeOuterLoop = EPracticeOuterLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEPracticeOuterLoop.rgb)
if thisEPracticeOuterLoop != None:
    for paramName in thisEPracticeOuterLoop:
        exec('{} = thisEPracticeOuterLoop[paramName]'.format(paramName))

for thisEPracticeOuterLoop in EPracticeOuterLoop:
    currentLoop = EPracticeOuterLoop
    # abbreviate parameter names if possible (e.g. rgb = thisEPracticeOuterLoop.rgb)
    if thisEPracticeOuterLoop != None:
        for paramName in thisEPracticeOuterLoop:
            exec('{} = thisEPracticeOuterLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "EPracticeInstructions2"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_5.setText(Instructions)
    text_6.setPos((0, -0.25))
    text_6.setText('Please press spacebar to begin.')
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    text_10.setColor('green', colorSpace='rgb')
    text_10.setPos((0.095, 0.05))
    text_10.setText(PractNo)
    text_10.setFont('Arial')
    text_10.setHeight(0.05)
    # keep track of which components have finished
    EPracticeInstructions2Components = [text_5, text_6, key_resp_7, text_10, text_11, text_12]
    for thisComponent in EPracticeInstructions2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EPracticeInstructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "EPracticeInstructions2"-------
    while continueRoutine:
        # get current time
        t = EPracticeInstructions2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EPracticeInstructions2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EPracticeInstructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "EPracticeInstructions2"-------
    for thisComponent in EPracticeInstructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    EPracticeOuterLoop.addData('text_5.started', text_5.tStartRefresh)
    EPracticeOuterLoop.addData('text_5.stopped', text_5.tStopRefresh)
    EPracticeOuterLoop.addData('text_6.started', text_6.tStartRefresh)
    EPracticeOuterLoop.addData('text_6.stopped', text_6.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    EPracticeOuterLoop.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        EPracticeOuterLoop.addData('key_resp_7.rt', key_resp_7.rt)
    EPracticeOuterLoop.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    EPracticeOuterLoop.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    EPracticeOuterLoop.addData('text_10.started', text_10.tStartRefresh)
    EPracticeOuterLoop.addData('text_10.stopped', text_10.tStopRefresh)
    EPracticeOuterLoop.addData('text_11.started', text_11.tStartRefresh)
    EPracticeOuterLoop.addData('text_11.stopped', text_11.tStopRefresh)
    EPracticeOuterLoop.addData('text_12.started', text_12.tStartRefresh)
    EPracticeOuterLoop.addData('text_12.stopped', text_12.tStopRefresh)
    # the Routine "EPracticeInstructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    EPracticeInnerLoop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CondFileP),
        seed=None, name='EPracticeInnerLoop')
    thisExp.addLoop(EPracticeInnerLoop)  # add the loop to the experiment
    thisEPracticeInnerLoop = EPracticeInnerLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEPracticeInnerLoop.rgb)
    if thisEPracticeInnerLoop != None:
        for paramName in thisEPracticeInnerLoop:
            exec('{} = thisEPracticeInnerLoop[paramName]'.format(paramName))
    
    for thisEPracticeInnerLoop in EPracticeInnerLoop:
        currentLoop = EPracticeInnerLoop
        # abbreviate parameter names if possible (e.g. rgb = thisEPracticeInnerLoop.rgb)
        if thisEPracticeInnerLoop != None:
            for paramName in thisEPracticeInnerLoop:
                exec('{} = thisEPracticeInnerLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "EPracticeISI"-------
        continueRoutine = True
        # update component parameters for each repeat
        if EPracticeInnerLoop.thisN == 0: # only on the first trial
            jitters = [1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9] # create the list
            shuffle(jitters) # randomise its order
        
        current_jitter = jitters.pop() # extract one entry on each trial
        thisExp.addData('ISIjitterPractice', current_jitter) # record in the data for this trial
        EPracticeISIMarker.setText('+')
        EPracticeISIMarker.setHeight(0.25)
        # keep track of which components have finished
        EPracticeISIComponents = [EPracticeISIMarker]
        for thisComponent in EPracticeISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        EPracticeISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "EPracticeISI"-------
        while continueRoutine:
            # get current time
            t = EPracticeISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=EPracticeISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EPracticeISIMarker* updates
            if EPracticeISIMarker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EPracticeISIMarker.frameNStart = frameN  # exact frame index
                EPracticeISIMarker.tStart = t  # local t and not account for scr refresh
                EPracticeISIMarker.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EPracticeISIMarker, 'tStartRefresh')  # time at next scr refresh
                EPracticeISIMarker.setAutoDraw(True)
            if EPracticeISIMarker.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EPracticeISIMarker.tStartRefresh + current_jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    EPracticeISIMarker.tStop = t  # not accounting for scr refresh
                    EPracticeISIMarker.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(EPracticeISIMarker, 'tStopRefresh')  # time at next scr refresh
                    EPracticeISIMarker.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EPracticeISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "EPracticeISI"-------
        for thisComponent in EPracticeISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        EPracticeInnerLoop.addData('EPracticeISIMarker.started', EPracticeISIMarker.tStartRefresh)
        EPracticeInnerLoop.addData('EPracticeISIMarker.stopped', EPracticeISIMarker.tStopRefresh)
        # the Routine "EPracticeISI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "EPracticeTrial"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        Pract.keys = []
        Pract.rt = []
        _Pract_allKeys = []
        PracticeFace.setImage(FaceE)
        ColourPractice.setOpacity(0.36)
        ColourPractice.setSize((0.7, 0.3))
        ColourPractice.setImage(ColourF)
        # keep track of which components have finished
        EPracticeTrialComponents = [Pract, PracticeFace, ColourPractice]
        for thisComponent in EPracticeTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        EPracticeTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "EPracticeTrial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = EPracticeTrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=EPracticeTrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Pract* updates
            waitOnFlip = False
            if Pract.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                Pract.frameNStart = frameN  # exact frame index
                Pract.tStart = t  # local t and not account for scr refresh
                Pract.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pract, 'tStartRefresh')  # time at next scr refresh
                Pract.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Pract.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Pract.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Pract.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Pract.tStartRefresh + 0.40-frameTolerance:
                    # keep track of stop time/frame for later
                    Pract.tStop = t  # not accounting for scr refresh
                    Pract.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Pract, 'tStopRefresh')  # time at next scr refresh
                    Pract.status = FINISHED
            if Pract.status == STARTED and not waitOnFlip:
                theseKeys = Pract.getKeys(keyList=['space', 'None'], waitRelease=False)
                _Pract_allKeys.extend(theseKeys)
                if len(_Pract_allKeys):
                    Pract.keys = _Pract_allKeys[-1].name  # just the last key pressed
                    Pract.rt = _Pract_allKeys[-1].rt
                    # was this correct?
                    if (Pract.keys == str(CorrectAnsP)) or (Pract.keys == CorrectAnsP):
                        Pract.corr = 1
                    else:
                        Pract.corr = 0
            
            # *PracticeFace* updates
            if PracticeFace.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                PracticeFace.frameNStart = frameN  # exact frame index
                PracticeFace.tStart = t  # local t and not account for scr refresh
                PracticeFace.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeFace, 'tStartRefresh')  # time at next scr refresh
                PracticeFace.setAutoDraw(True)
            if PracticeFace.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PracticeFace.tStartRefresh + 0.40-frameTolerance:
                    # keep track of stop time/frame for later
                    PracticeFace.tStop = t  # not accounting for scr refresh
                    PracticeFace.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PracticeFace, 'tStopRefresh')  # time at next scr refresh
                    PracticeFace.setAutoDraw(False)
            
            # *ColourPractice* updates
            if ColourPractice.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                ColourPractice.frameNStart = frameN  # exact frame index
                ColourPractice.tStart = t  # local t and not account for scr refresh
                ColourPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ColourPractice, 'tStartRefresh')  # time at next scr refresh
                ColourPractice.setAutoDraw(True)
            if ColourPractice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ColourPractice.tStartRefresh + 0.40-frameTolerance:
                    # keep track of stop time/frame for later
                    ColourPractice.tStop = t  # not accounting for scr refresh
                    ColourPractice.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ColourPractice, 'tStopRefresh')  # time at next scr refresh
                    ColourPractice.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EPracticeTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "EPracticeTrial"-------
        for thisComponent in EPracticeTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
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
        EPracticeInnerLoop.addData('Pract.started', Pract.tStartRefresh)
        EPracticeInnerLoop.addData('Pract.stopped', Pract.tStopRefresh)
        EPracticeInnerLoop.addData('PracticeFace.started', PracticeFace.tStartRefresh)
        EPracticeInnerLoop.addData('PracticeFace.stopped', PracticeFace.tStopRefresh)
        EPracticeInnerLoop.addData('ColourPractice.started', ColourPractice.tStartRefresh)
        EPracticeInnerLoop.addData('ColourPractice.stopped', ColourPractice.tStopRefresh)
        if Pract.corr==1:
                PracticeFeedback = 'Correct'
                FeedbackColour = 'green'
        
        if Pract.corr==0:
                PracticeFeedback = 'Incorrect'
                FeedbackColour = 'red'
        
        if Pract.corr==0 and Pract.keys== None:
                PracticeFeedback = 'Miss (too slow)'
                FeedbackColour = 'orange'
        
        # ------Prepare to start Routine "PracticeFeedbackBlock"-------
        continueRoutine = True
        routineTimer.add(2.500000)
        # update component parameters for each repeat
        text_7.setColor(FeedbackColour, colorSpace='rgb')
        text_7.setText(PracticeFeedback)
        text_7.setHeight(0.07)
        # keep track of which components have finished
        PracticeFeedbackBlockComponents = [text_7]
        for thisComponent in PracticeFeedbackBlockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeFeedbackBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracticeFeedbackBlock"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PracticeFeedbackBlockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeFeedbackBlockClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_7* updates
            if text_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                text_7.setAutoDraw(True)
            if text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_7.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_7.tStop = t  # not accounting for scr refresh
                    text_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                    text_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeFeedbackBlockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeFeedbackBlock"-------
        for thisComponent in PracticeFeedbackBlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        EPracticeInnerLoop.addData('text_7.started', text_7.tStartRefresh)
        EPracticeInnerLoop.addData('text_7.stopped', text_7.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'EPracticeInnerLoop'
    
    
    # ------Prepare to start Routine "Add"-------
    continueRoutine = True
    # update component parameters for each repeat
    PractNo = PractNo + 1
    # keep track of which components have finished
    AddComponents = []
    for thisComponent in AddComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AddClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Add"-------
    while continueRoutine:
        # get current time
        t = AddClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AddClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AddComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Add"-------
    for thisComponent in AddComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Add" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'EPracticeOuterLoop'


# ------Prepare to start Routine "EndPracticeEndInstructions"-------
continueRoutine = True
# update component parameters for each repeat
EndOfPractice.setText('End of practice.\n\nPlease keep in mind: You will no longer receive feedback on responses ("correct","incorrect", or "too slow") in the real task. \n\nPress \'spacebar\' to continue')
EndOfPractice.setHeight(0.05)
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
EndPracticeEndInstructionsComponents = [EndOfPractice, key_resp_8]
for thisComponent in EndPracticeEndInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndPracticeEndInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndPracticeEndInstructions"-------
while continueRoutine:
    # get current time
    t = EndPracticeEndInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndPracticeEndInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndOfPractice* updates
    if EndOfPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndOfPractice.frameNStart = frameN  # exact frame index
        EndOfPractice.tStart = t  # local t and not account for scr refresh
        EndOfPractice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndOfPractice, 'tStartRefresh')  # time at next scr refresh
        EndOfPractice.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndPracticeEndInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndPracticeEndInstructions"-------
for thisComponent in EndPracticeEndInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndOfPractice.started', EndOfPractice.tStartRefresh)
thisExp.addData('EndOfPractice.stopped', EndOfPractice.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndPracticeEndInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "RealTaskPreInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
RealTaskPreInstructionsComponents = [text_8, key_resp_6]
for thisComponent in RealTaskPreInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RealTaskPreInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RealTaskPreInstructions"-------
while continueRoutine:
    # get current time
    t = RealTaskPreInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RealTaskPreInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RealTaskPreInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RealTaskPreInstructions"-------
for thisComponent in RealTaskPreInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "RealTaskPreInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
MasterLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(VersionSelection),
    seed=None, name='MasterLoop')
thisExp.addLoop(MasterLoop)  # add the loop to the experiment
thisMasterLoop = MasterLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMasterLoop.rgb)
if thisMasterLoop != None:
    for paramName in thisMasterLoop:
        exec('{} = thisMasterLoop[paramName]'.format(paramName))

for thisMasterLoop in MasterLoop:
    currentLoop = MasterLoop
    # abbreviate parameter names if possible (e.g. rgb = thisMasterLoop.rgb)
    if thisMasterLoop != None:
        for paramName in thisMasterLoop:
            exec('{} = thisMasterLoop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    OuterLoop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(MasterCondFile),
        seed=None, name='OuterLoop')
    thisExp.addLoop(OuterLoop)  # add the loop to the experiment
    thisOuterLoop = OuterLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOuterLoop.rgb)
    if thisOuterLoop != None:
        for paramName in thisOuterLoop:
            exec('{} = thisOuterLoop[paramName]'.format(paramName))
    
    for thisOuterLoop in OuterLoop:
        currentLoop = OuterLoop
        # abbreviate parameter names if possible (e.g. rgb = thisOuterLoop.rgb)
        if thisOuterLoop != None:
            for paramName in thisOuterLoop:
                exec('{} = thisOuterLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Instructions_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        text_2.setPos((0, -0.10))
        text_2.setText(Instructions

)
        text_3.setPos((0, -0.25))
        text_3.setText("Please press 'spacebar' to begin.")
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        TaskBlock.setText('  Task block:')
        BlockNo1.setColor('green', colorSpace='rgb')
        BlockNo1.setPos((0.095, 0.05))
        BlockNo1.setText(BlockNo)
        BlockNo1.setHeight(0.05)
        OfBlock.setText('of 6.')
        # keep track of which components have finished
        Instructions_2Components = [text_2, text_3, key_resp_3, TaskBlock, BlockNo1, OfBlock]
        for thisComponent in Instructions_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Instructions_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Instructions_2"-------
        while continueRoutine:
            # get current time
            t = Instructions_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Instructions_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *TaskBlock* updates
            if TaskBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TaskBlock.frameNStart = frameN  # exact frame index
                TaskBlock.tStart = t  # local t and not account for scr refresh
                TaskBlock.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TaskBlock, 'tStartRefresh')  # time at next scr refresh
                TaskBlock.setAutoDraw(True)
            
            # *BlockNo1* updates
            if BlockNo1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BlockNo1.frameNStart = frameN  # exact frame index
                BlockNo1.tStart = t  # local t and not account for scr refresh
                BlockNo1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BlockNo1, 'tStartRefresh')  # time at next scr refresh
                BlockNo1.setAutoDraw(True)
            
            # *OfBlock* updates
            if OfBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                OfBlock.frameNStart = frameN  # exact frame index
                OfBlock.tStart = t  # local t and not account for scr refresh
                OfBlock.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(OfBlock, 'tStartRefresh')  # time at next scr refresh
                OfBlock.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instructions_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Instructions_2"-------
        for thisComponent in Instructions_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        OuterLoop.addData('text_2.started', text_2.tStartRefresh)
        OuterLoop.addData('text_2.stopped', text_2.tStopRefresh)
        OuterLoop.addData('text_3.started', text_3.tStartRefresh)
        OuterLoop.addData('text_3.stopped', text_3.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        OuterLoop.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            OuterLoop.addData('key_resp_3.rt', key_resp_3.rt)
        OuterLoop.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        OuterLoop.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        OuterLoop.addData('TaskBlock.started', TaskBlock.tStartRefresh)
        OuterLoop.addData('TaskBlock.stopped', TaskBlock.tStopRefresh)
        OuterLoop.addData('BlockNo1.started', BlockNo1.tStartRefresh)
        OuterLoop.addData('BlockNo1.stopped', BlockNo1.tStopRefresh)
        OuterLoop.addData('OfBlock.started', OfBlock.tStartRefresh)
        OuterLoop.addData('OfBlock.stopped', OfBlock.tStopRefresh)
        # the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        InnerLoop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(CondFile),
            seed=None, name='InnerLoop')
        thisExp.addLoop(InnerLoop)  # add the loop to the experiment
        thisInnerLoop = InnerLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisInnerLoop.rgb)
        if thisInnerLoop != None:
            for paramName in thisInnerLoop:
                exec('{} = thisInnerLoop[paramName]'.format(paramName))
        
        for thisInnerLoop in InnerLoop:
            currentLoop = InnerLoop
            # abbreviate parameter names if possible (e.g. rgb = thisInnerLoop.rgb)
            if thisInnerLoop != None:
                for paramName in thisInnerLoop:
                    exec('{} = thisInnerLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "ISI_2"-------
            continueRoutine = True
            # update component parameters for each repeat
            if InnerLoop.thisN == 0: # only on the first trial
                jitters = [1.2,1.21,1.22,1.23,1.24,1.25,1.26,1.27,1.28
                ,1.29,1.30,1.31,1.32,1.33,1.34,1.35,1.36,1.37,1.38,1.39,1.4,1.41,
                1.42,1.43,1.44,1.45,1.46,1.47,1.48,1.49,1.5,1.51,1.52,1.53,
                1.54,1.55,1.56,1.57,1.58,1.59,1.6,1.61,1.62,1.63,1.64,
                1.65,1.66,1.67,1.68,1.69,1.7,1.71,1.72,1.73,1.74,1.75,1.76,
                1.77,1.78,1.79,1.8,1.81,1.82,1.83,1.84,1.85,1.86,1.87,1.88,1.89,1.9,1.91,1.92,1.93,
                1.94,1.95,1.96,1.97,1.98,1.99,2] # create the list
                shuffle(jitters) # randomise its order
            
            current_jitter = jitters.pop() # extract one entry on each trial
            thisExp.addData('ISIjitter', current_jitter) # record in the data for this trial
            ISImarker.setText('+')
            # keep track of which components have finished
            ISI_2Components = [ISImarker]
            for thisComponent in ISI_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ISI_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ISI_2"-------
            while continueRoutine:
                # get current time
                t = ISI_2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ISI_2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ISImarker* updates
                if ISImarker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ISImarker.frameNStart = frameN  # exact frame index
                    ISImarker.tStart = t  # local t and not account for scr refresh
                    ISImarker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISImarker, 'tStartRefresh')  # time at next scr refresh
                    ISImarker.setAutoDraw(True)
                if ISImarker.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISImarker.tStartRefresh + current_jitter-frameTolerance:
                        # keep track of stop time/frame for later
                        ISImarker.tStop = t  # not accounting for scr refresh
                        ISImarker.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ISImarker, 'tStopRefresh')  # time at next scr refresh
                        ISImarker.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ISI_2"-------
            for thisComponent in ISI_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            InnerLoop.addData('ISImarker.started', ISImarker.tStartRefresh)
            InnerLoop.addData('ISImarker.stopped', ISImarker.tStopRefresh)
            # the Routine "ISI_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "EmotTrial"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            FaceSet.setSize((0.7, 0.3))
            FaceSet.setImage(FaceE)
            Colour.setOpacity(0.36)
            Colour.setSize((0.7, 0.3))
            Colour.setImage(ColourF)
            # keep track of which components have finished
            EmotTrialComponents = [key_resp, FaceSet, Colour]
            for thisComponent in EmotTrialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            EmotTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "EmotTrial"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = EmotTrialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=EmotTrialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp* updates
                waitOnFlip = False
                if key_resp.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp.frameNStart = frameN  # exact frame index
                    key_resp.tStart = t  # local t and not account for scr refresh
                    key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp.tStartRefresh + 0.40-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp.tStop = t  # not accounting for scr refresh
                        key_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                        key_resp.status = FINISHED
                if key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp.getKeys(keyList=['space', 'None'], waitRelease=False)
                    _key_resp_allKeys.extend(theseKeys)
                    if len(_key_resp_allKeys):
                        key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                        key_resp.rt = _key_resp_allKeys[-1].rt
                        # was this correct?
                        if (key_resp.keys == str(CorrectAnsP)) or (key_resp.keys == CorrectAnsP):
                            key_resp.corr = 1
                        else:
                            key_resp.corr = 0
                
                # *FaceSet* updates
                if FaceSet.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    FaceSet.frameNStart = frameN  # exact frame index
                    FaceSet.tStart = t  # local t and not account for scr refresh
                    FaceSet.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FaceSet, 'tStartRefresh')  # time at next scr refresh
                    FaceSet.setAutoDraw(True)
                if FaceSet.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > FaceSet.tStartRefresh + 0.40-frameTolerance:
                        # keep track of stop time/frame for later
                        FaceSet.tStop = t  # not accounting for scr refresh
                        FaceSet.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(FaceSet, 'tStopRefresh')  # time at next scr refresh
                        FaceSet.setAutoDraw(False)
                
                # *Colour* updates
                if Colour.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                    # keep track of start time/frame for later
                    Colour.frameNStart = frameN  # exact frame index
                    Colour.tStart = t  # local t and not account for scr refresh
                    Colour.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Colour, 'tStartRefresh')  # time at next scr refresh
                    Colour.setAutoDraw(True)
                if Colour.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Colour.tStartRefresh + 0.40-frameTolerance:
                        # keep track of stop time/frame for later
                        Colour.tStop = t  # not accounting for scr refresh
                        Colour.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Colour, 'tStopRefresh')  # time at next scr refresh
                        Colour.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in EmotTrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "EmotTrial"-------
            for thisComponent in EmotTrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
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
            InnerLoop.addData('key_resp.started', key_resp.tStartRefresh)
            InnerLoop.addData('key_resp.stopped', key_resp.tStopRefresh)
            InnerLoop.addData('FaceSet.started', FaceSet.tStartRefresh)
            InnerLoop.addData('FaceSet.stopped', FaceSet.tStopRefresh)
            InnerLoop.addData('Colour.started', Colour.tStartRefresh)
            InnerLoop.addData('Colour.stopped', Colour.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'InnerLoop'
        
        
        # ------Prepare to start Routine "Add2"-------
        continueRoutine = True
        # update component parameters for each repeat
        BlockNo = BlockNo + 1
        # keep track of which components have finished
        Add2Components = []
        for thisComponent in Add2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Add2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Add2"-------
        while continueRoutine:
            # get current time
            t = Add2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Add2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Add2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Add2"-------
        for thisComponent in Add2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Add2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "EndBlock"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        if BlockNo <= 6:
           Breaktext = 'Please take a break if needed.'
        else:
           Breaktext = '' 
        BreakText2.setText(Breaktext)
        PressToContinue.setText("Please press 'spacebar' to continue.")
        # keep track of which components have finished
        EndBlockComponents = [EndBlockText, key_resp_4, BreakText2, PressToContinue]
        for thisComponent in EndBlockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        EndBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "EndBlock"-------
        while continueRoutine:
            # get current time
            t = EndBlockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=EndBlockClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EndBlockText* updates
            if EndBlockText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EndBlockText.frameNStart = frameN  # exact frame index
                EndBlockText.tStart = t  # local t and not account for scr refresh
                EndBlockText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EndBlockText, 'tStartRefresh')  # time at next scr refresh
                EndBlockText.setAutoDraw(True)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *BreakText2* updates
            if BreakText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BreakText2.frameNStart = frameN  # exact frame index
                BreakText2.tStart = t  # local t and not account for scr refresh
                BreakText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BreakText2, 'tStartRefresh')  # time at next scr refresh
                BreakText2.setAutoDraw(True)
            
            # *PressToContinue* updates
            if PressToContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PressToContinue.frameNStart = frameN  # exact frame index
                PressToContinue.tStart = t  # local t and not account for scr refresh
                PressToContinue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PressToContinue, 'tStartRefresh')  # time at next scr refresh
                PressToContinue.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EndBlockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "EndBlock"-------
        for thisComponent in EndBlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        OuterLoop.addData('EndBlockText.started', EndBlockText.tStartRefresh)
        OuterLoop.addData('EndBlockText.stopped', EndBlockText.tStopRefresh)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        OuterLoop.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            OuterLoop.addData('key_resp_4.rt', key_resp_4.rt)
        OuterLoop.addData('key_resp_4.started', key_resp_4.tStartRefresh)
        OuterLoop.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
        OuterLoop.addData('BreakText2.started', BreakText2.tStartRefresh)
        OuterLoop.addData('BreakText2.stopped', BreakText2.tStopRefresh)
        OuterLoop.addData('PressToContinue.started', PressToContinue.tStartRefresh)
        OuterLoop.addData('PressToContinue.stopped', PressToContinue.tStopRefresh)
        # the Routine "EndBlock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1 repeats of 'OuterLoop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'MasterLoop'


# ------Prepare to start Routine "EndEmotionTask"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EndEmotionTaskComponents = [text_9]
for thisComponent in EndEmotionTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndEmotionTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndEmotionTask"-------
while continueRoutine:
    # get current time
    t = EndEmotionTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndEmotionTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndEmotionTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndEmotionTask"-------
for thisComponent in EndEmotionTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# the Routine "EndEmotionTask" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
