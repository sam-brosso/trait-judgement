#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on Wed Apr 14 22:04:20 2021
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
psychopyVersion = '2021.1.2'
expName = 'trait judgement task'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='/Users/keelylab/Desktop/fMRI Grad Class/Project/trait judgement task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
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

# Initialize components for Routine "get_ready"
get_readyClock = core.Clock()
trigger = visual.TextStim(win=win, name='trigger',
    text='Get Ready!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instructions_beg"
instructions_begClock = core.Clock()
inst_beg = visual.TextStim(win=win, name='inst_beg',
    text='Look at screen',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "null_beg"
null_begClock = core.Clock()
null1_3 = visual.ImageStim(
    win=win,
    name='null1_3', 
    image='/Users/keelylab/Desktop/fMRI Grad Class/Project/astericks.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
null2_3 = visual.ImageStim(
    win=win,
    name='null2_3', 
    image='/Users/keelylab/Desktop/fMRI Grad Class/Project/astericks2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
answer_null_3 = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instr = visual.TextStim(win=win, name='instr',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
cues = visual.TextStim(win=win, name='cues',
    text='',
    font='Open Sans',
    pos=(0, .12), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
adjectives = visual.TextStim(win=win, name='adjectives',
    text='',
    font='Open Sans',
    pos=(0, -.12), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
answer = keyboard.Keyboard()

# Initialize components for Routine "instructions_null"
instructions_nullClock = core.Clock()
inst_null = visual.TextStim(win=win, name='inst_null',
    text='Look at screen',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "null"
nullClock = core.Clock()
null1 = visual.ImageStim(
    win=win,
    name='null1', 
    image='/Users/keelylab/Desktop/fMRI Grad Class/Project/astericks.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
null2 = visual.ImageStim(
    win=win,
    name='null2', 
    image='/Users/keelylab/Desktop/fMRI Grad Class/Project/astericks2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
answer_null = keyboard.Keyboard()

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
BREAK = visual.TextStim(win=win, name='BREAK',
    text='BREAK',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "get_ready_2"
get_ready_2Clock = core.Clock()
trigger_2 = visual.TextStim(win=win, name='trigger_2',
    text='Get Ready!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "instructions_beg2"
instructions_beg2Clock = core.Clock()
inst_beg2 = visual.TextStim(win=win, name='inst_beg2',
    text='Look at screen',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "null_beg_2"
null_beg_2Clock = core.Clock()
null1_4 = visual.ImageStim(
    win=win,
    name='null1_4', 
    image='/Users/keelylab/Desktop/fMRI Grad Class/Project/astericks.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
null2_4 = visual.ImageStim(
    win=win,
    name='null2_4', 
    image='/Users/keelylab/Desktop/fMRI Grad Class/Project/astericks2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
answer_null_4 = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instr_2 = visual.TextStim(win=win, name='instr_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
cues_2 = visual.TextStim(win=win, name='cues_2',
    text='',
    font='Open Sans',
    pos=(0, .12), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
adjectives_2 = visual.TextStim(win=win, name='adjectives_2',
    text='',
    font='Open Sans',
    pos=(0, -.12), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
answer_2 = keyboard.Keyboard()

# Initialize components for Routine "instructions_null2"
instructions_null2Clock = core.Clock()
inst_null2 = visual.TextStim(win=win, name='inst_null2',
    text='Look at screen',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "null_2"
null_2Clock = core.Clock()
null1_2 = visual.ImageStim(
    win=win,
    name='null1_2', 
    image='/Users/keelylab/Desktop/fMRI Grad Class/Project/astericks.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
null2_2 = visual.ImageStim(
    win=win,
    name='null2_2', 
    image='/Users/keelylab/Desktop/fMRI Grad Class/Project/astericks2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
answer_null_2 = keyboard.Keyboard()

# Initialize components for Routine "END"
ENDClock = core.Clock()
end = visual.TextStim(win=win, name='end',
    text='END OF TASK',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "get_ready"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
get_readyComponents = [trigger, key_resp]
for thisComponent in get_readyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
get_readyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "get_ready"-------
while continueRoutine:
    # get current time
    t = get_readyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=get_readyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger* updates
    if trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger.frameNStart = frameN  # exact frame index
        trigger.tStart = t  # local t and not account for scr refresh
        trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger, 'tStartRefresh')  # time at next scr refresh
        trigger.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['o'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in get_readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "get_ready"-------
for thisComponent in get_readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('trigger.started', trigger.tStartRefresh)
thisExp.addData('trigger.stopped', trigger.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "get_ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions_beg"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
instructions_begComponents = [inst_beg]
for thisComponent in instructions_begComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_begClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_beg"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructions_begClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_begClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_beg* updates
    if inst_beg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_beg.frameNStart = frameN  # exact frame index
        inst_beg.tStart = t  # local t and not account for scr refresh
        inst_beg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_beg, 'tStartRefresh')  # time at next scr refresh
        inst_beg.setAutoDraw(True)
    if inst_beg.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inst_beg.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            inst_beg.tStop = t  # not accounting for scr refresh
            inst_beg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inst_beg, 'tStopRefresh')  # time at next scr refresh
            inst_beg.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_begComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_beg"-------
for thisComponent in instructions_begComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('inst_beg.started', inst_beg.tStartRefresh)
thisExp.addData('inst_beg.stopped', inst_beg.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=10.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7:
        exec('{} = thisTrial_7[paramName]'.format(paramName))

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            exec('{} = thisTrial_7[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "null_beg"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    answer_null_3.keys = []
    answer_null_3.rt = []
    _answer_null_3_allKeys = []
    # keep track of which components have finished
    null_begComponents = [null1_3, null2_3, answer_null_3]
    for thisComponent in null_begComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    null_begClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "null_beg"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = null_begClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=null_begClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *null1_3* updates
        if null1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            null1_3.frameNStart = frameN  # exact frame index
            null1_3.tStart = t  # local t and not account for scr refresh
            null1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(null1_3, 'tStartRefresh')  # time at next scr refresh
            null1_3.setAutoDraw(True)
        if null1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > null1_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                null1_3.tStop = t  # not accounting for scr refresh
                null1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(null1_3, 'tStopRefresh')  # time at next scr refresh
                null1_3.setAutoDraw(False)
        
        # *null2_3* updates
        if null2_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            null2_3.frameNStart = frameN  # exact frame index
            null2_3.tStart = t  # local t and not account for scr refresh
            null2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(null2_3, 'tStartRefresh')  # time at next scr refresh
            null2_3.setAutoDraw(True)
        if null2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > null2_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                null2_3.tStop = t  # not accounting for scr refresh
                null2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(null2_3, 'tStopRefresh')  # time at next scr refresh
                null2_3.setAutoDraw(False)
        
        # *answer_null_3* updates
        waitOnFlip = False
        if answer_null_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            answer_null_3.frameNStart = frameN  # exact frame index
            answer_null_3.tStart = t  # local t and not account for scr refresh
            answer_null_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer_null_3, 'tStartRefresh')  # time at next scr refresh
            answer_null_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(answer_null_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(answer_null_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if answer_null_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > answer_null_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                answer_null_3.tStop = t  # not accounting for scr refresh
                answer_null_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer_null_3, 'tStopRefresh')  # time at next scr refresh
                answer_null_3.status = FINISHED
        if answer_null_3.status == STARTED and not waitOnFlip:
            theseKeys = answer_null_3.getKeys(keyList=['2', '3'], waitRelease=False)
            _answer_null_3_allKeys.extend(theseKeys)
            if len(_answer_null_3_allKeys):
                answer_null_3.keys = _answer_null_3_allKeys[-1].name  # just the last key pressed
                answer_null_3.rt = _answer_null_3_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in null_begComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "null_beg"-------
    for thisComponent in null_begComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('null1_3.started', null1_3.tStartRefresh)
    thisExp.addData('null1_3.stopped', null1_3.tStopRefresh)
    thisExp.addData('null2_3.started', null2_3.tStartRefresh)
    thisExp.addData('null2_3.stopped', null2_3.tStopRefresh)
    # check responses
    if answer_null_3.keys in ['', [], None]:  # No response was made
        answer_null_3.keys = None
    thisExp.addData('answer_null_3.keys',answer_null_3.keys)
    if answer_null_3.keys != None:  # we had a response
        thisExp.addData('answer_null_3.rt', answer_null_3.rt)
    thisExp.addData('answer_null_3.started', answer_null_3.tStartRefresh)
    thisExp.addData('answer_null_3.stopped', answer_null_3.tStopRefresh)
    thisExp.nextEntry()
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'trials_7'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=8.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    instr.setText(instructions_run1)
    # keep track of which components have finished
    instructionsComponents = [instr]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr* updates
        if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr.frameNStart = frameN  # exact frame index
            instr.tStart = t  # local t and not account for scr refresh
            instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
            instr.setAutoDraw(True)
        if instr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                instr.tStop = t  # not accounting for scr refresh
                instr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr, 'tStopRefresh')  # time at next scr refresh
                instr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('instr.started', instr.tStartRefresh)
    trials_3.addData('instr.stopped', instr.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.xlsx', selection=rows),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        cues.setText(cue_run1)
        adjectives.setText(adjective_run1)
        answer.keys = []
        answer.rt = []
        _answer_allKeys = []
        # keep track of which components have finished
        trialComponents = [cues, adjectives, answer]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cues* updates
            if cues.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cues.frameNStart = frameN  # exact frame index
                cues.tStart = t  # local t and not account for scr refresh
                cues.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cues, 'tStartRefresh')  # time at next scr refresh
                cues.setAutoDraw(True)
            if cues.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cues.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cues.tStop = t  # not accounting for scr refresh
                    cues.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cues, 'tStopRefresh')  # time at next scr refresh
                    cues.setAutoDraw(False)
            
            # *adjectives* updates
            if adjectives.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                adjectives.frameNStart = frameN  # exact frame index
                adjectives.tStart = t  # local t and not account for scr refresh
                adjectives.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(adjectives, 'tStartRefresh')  # time at next scr refresh
                adjectives.setAutoDraw(True)
            if adjectives.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > adjectives.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    adjectives.tStop = t  # not accounting for scr refresh
                    adjectives.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(adjectives, 'tStopRefresh')  # time at next scr refresh
                    adjectives.setAutoDraw(False)
            
            # *answer* updates
            waitOnFlip = False
            if answer.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                answer.frameNStart = frameN  # exact frame index
                answer.tStart = t  # local t and not account for scr refresh
                answer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answer, 'tStartRefresh')  # time at next scr refresh
                answer.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(answer.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(answer.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if answer.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > answer.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    answer.tStop = t  # not accounting for scr refresh
                    answer.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(answer, 'tStopRefresh')  # time at next scr refresh
                    answer.status = FINISHED
            if answer.status == STARTED and not waitOnFlip:
                theseKeys = answer.getKeys(keyList=['2', '3'], waitRelease=False)
                _answer_allKeys.extend(theseKeys)
                if len(_answer_allKeys):
                    answer.keys = _answer_allKeys[-1].name  # just the last key pressed
                    answer.rt = _answer_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('cues.started', cues.tStartRefresh)
        trials.addData('cues.stopped', cues.tStopRefresh)
        trials.addData('adjectives.started', adjectives.tStartRefresh)
        trials.addData('adjectives.stopped', adjectives.tStopRefresh)
        # check responses
        if answer.keys in ['', [], None]:  # No response was made
            answer.keys = None
        trials.addData('answer.keys',answer.keys)
        if answer.keys != None:  # we had a response
            trials.addData('answer.rt', answer.rt)
        trials.addData('answer.started', answer.tStartRefresh)
        trials.addData('answer.stopped', answer.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    
    # ------Prepare to start Routine "instructions_null"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    instructions_nullComponents = [inst_null]
    for thisComponent in instructions_nullComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_nullClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_null"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instructions_nullClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_nullClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst_null* updates
        if inst_null.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst_null.frameNStart = frameN  # exact frame index
            inst_null.tStart = t  # local t and not account for scr refresh
            inst_null.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst_null, 'tStartRefresh')  # time at next scr refresh
            inst_null.setAutoDraw(True)
        if inst_null.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > inst_null.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                inst_null.tStop = t  # not accounting for scr refresh
                inst_null.frameNStop = frameN  # exact frame index
                win.timeOnFlip(inst_null, 'tStopRefresh')  # time at next scr refresh
                inst_null.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_nullComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_null"-------
    for thisComponent in instructions_nullComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('inst_null.started', inst_null.tStartRefresh)
    trials_3.addData('inst_null.stopped', inst_null.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=10.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "null"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        answer_null.keys = []
        answer_null.rt = []
        _answer_null_allKeys = []
        # keep track of which components have finished
        nullComponents = [null1, null2, answer_null]
        for thisComponent in nullComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        nullClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "null"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = nullClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=nullClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *null1* updates
            if null1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                null1.frameNStart = frameN  # exact frame index
                null1.tStart = t  # local t and not account for scr refresh
                null1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(null1, 'tStartRefresh')  # time at next scr refresh
                null1.setAutoDraw(True)
            if null1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > null1.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    null1.tStop = t  # not accounting for scr refresh
                    null1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(null1, 'tStopRefresh')  # time at next scr refresh
                    null1.setAutoDraw(False)
            
            # *null2* updates
            if null2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                null2.frameNStart = frameN  # exact frame index
                null2.tStart = t  # local t and not account for scr refresh
                null2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(null2, 'tStartRefresh')  # time at next scr refresh
                null2.setAutoDraw(True)
            if null2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > null2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    null2.tStop = t  # not accounting for scr refresh
                    null2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(null2, 'tStopRefresh')  # time at next scr refresh
                    null2.setAutoDraw(False)
            
            # *answer_null* updates
            waitOnFlip = False
            if answer_null.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                answer_null.frameNStart = frameN  # exact frame index
                answer_null.tStart = t  # local t and not account for scr refresh
                answer_null.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answer_null, 'tStartRefresh')  # time at next scr refresh
                answer_null.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(answer_null.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(answer_null.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if answer_null.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > answer_null.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    answer_null.tStop = t  # not accounting for scr refresh
                    answer_null.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(answer_null, 'tStopRefresh')  # time at next scr refresh
                    answer_null.status = FINISHED
            if answer_null.status == STARTED and not waitOnFlip:
                theseKeys = answer_null.getKeys(keyList=['2', '3'], waitRelease=False)
                _answer_null_allKeys.extend(theseKeys)
                if len(_answer_null_allKeys):
                    answer_null.keys = _answer_null_allKeys[-1].name  # just the last key pressed
                    answer_null.rt = _answer_null_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in nullComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "null"-------
        for thisComponent in nullComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('null1.started', null1.tStartRefresh)
        trials_2.addData('null1.stopped', null1.tStopRefresh)
        trials_2.addData('null2.started', null2.tStartRefresh)
        trials_2.addData('null2.stopped', null2.tStopRefresh)
        # check responses
        if answer_null.keys in ['', [], None]:  # No response was made
            answer_null.keys = None
        trials_2.addData('answer_null.keys',answer_null.keys)
        if answer_null.keys != None:  # we had a response
            trials_2.addData('answer_null.rt', answer_null.rt)
        trials_2.addData('answer_null.started', answer_null.tStartRefresh)
        trials_2.addData('answer_null.stopped', answer_null.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'trials_2'
    
# completed 8.0 repeats of 'trials_3'


# ------Prepare to start Routine "break_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
break_2Components = [BREAK, key_resp_2]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *BREAK* updates
    if BREAK.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BREAK.frameNStart = frameN  # exact frame index
        BREAK.tStart = t  # local t and not account for scr refresh
        BREAK.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BREAK, 'tStartRefresh')  # time at next scr refresh
        BREAK.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['p'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BREAK.started', BREAK.tStartRefresh)
thisExp.addData('BREAK.stopped', BREAK.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "break_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "get_ready_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
get_ready_2Components = [trigger_2, key_resp_3]
for thisComponent in get_ready_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
get_ready_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "get_ready_2"-------
while continueRoutine:
    # get current time
    t = get_ready_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=get_ready_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger_2* updates
    if trigger_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_2.frameNStart = frameN  # exact frame index
        trigger_2.tStart = t  # local t and not account for scr refresh
        trigger_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_2, 'tStartRefresh')  # time at next scr refresh
        trigger_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        theseKeys = key_resp_3.getKeys(keyList=['o'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in get_ready_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "get_ready_2"-------
for thisComponent in get_ready_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('trigger_2.started', trigger_2.tStartRefresh)
thisExp.addData('trigger_2.stopped', trigger_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "get_ready_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions_beg2"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
instructions_beg2Components = [inst_beg2]
for thisComponent in instructions_beg2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_beg2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_beg2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructions_beg2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_beg2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_beg2* updates
    if inst_beg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_beg2.frameNStart = frameN  # exact frame index
        inst_beg2.tStart = t  # local t and not account for scr refresh
        inst_beg2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_beg2, 'tStartRefresh')  # time at next scr refresh
        inst_beg2.setAutoDraw(True)
    if inst_beg2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inst_beg2.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            inst_beg2.tStop = t  # not accounting for scr refresh
            inst_beg2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inst_beg2, 'tStopRefresh')  # time at next scr refresh
            inst_beg2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_beg2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_beg2"-------
for thisComponent in instructions_beg2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('inst_beg2.started', inst_beg2.tStartRefresh)
thisExp.addData('inst_beg2.stopped', inst_beg2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=10.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_8')
thisExp.addLoop(trials_8)  # add the loop to the experiment
thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
if thisTrial_8 != None:
    for paramName in thisTrial_8:
        exec('{} = thisTrial_8[paramName]'.format(paramName))

for thisTrial_8 in trials_8:
    currentLoop = trials_8
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            exec('{} = thisTrial_8[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "null_beg_2"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    answer_null_4.keys = []
    answer_null_4.rt = []
    _answer_null_4_allKeys = []
    # keep track of which components have finished
    null_beg_2Components = [null1_4, null2_4, answer_null_4]
    for thisComponent in null_beg_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    null_beg_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "null_beg_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = null_beg_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=null_beg_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *null1_4* updates
        if null1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            null1_4.frameNStart = frameN  # exact frame index
            null1_4.tStart = t  # local t and not account for scr refresh
            null1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(null1_4, 'tStartRefresh')  # time at next scr refresh
            null1_4.setAutoDraw(True)
        if null1_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > null1_4.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                null1_4.tStop = t  # not accounting for scr refresh
                null1_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(null1_4, 'tStopRefresh')  # time at next scr refresh
                null1_4.setAutoDraw(False)
        
        # *null2_4* updates
        if null2_4.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            null2_4.frameNStart = frameN  # exact frame index
            null2_4.tStart = t  # local t and not account for scr refresh
            null2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(null2_4, 'tStartRefresh')  # time at next scr refresh
            null2_4.setAutoDraw(True)
        if null2_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > null2_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                null2_4.tStop = t  # not accounting for scr refresh
                null2_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(null2_4, 'tStopRefresh')  # time at next scr refresh
                null2_4.setAutoDraw(False)
        
        # *answer_null_4* updates
        waitOnFlip = False
        if answer_null_4.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            answer_null_4.frameNStart = frameN  # exact frame index
            answer_null_4.tStart = t  # local t and not account for scr refresh
            answer_null_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer_null_4, 'tStartRefresh')  # time at next scr refresh
            answer_null_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(answer_null_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(answer_null_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if answer_null_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > answer_null_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                answer_null_4.tStop = t  # not accounting for scr refresh
                answer_null_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(answer_null_4, 'tStopRefresh')  # time at next scr refresh
                answer_null_4.status = FINISHED
        if answer_null_4.status == STARTED and not waitOnFlip:
            theseKeys = answer_null_4.getKeys(keyList=['2', '3'], waitRelease=False)
            _answer_null_4_allKeys.extend(theseKeys)
            if len(_answer_null_4_allKeys):
                answer_null_4.keys = _answer_null_4_allKeys[-1].name  # just the last key pressed
                answer_null_4.rt = _answer_null_4_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in null_beg_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "null_beg_2"-------
    for thisComponent in null_beg_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('null1_4.started', null1_4.tStartRefresh)
    thisExp.addData('null1_4.stopped', null1_4.tStopRefresh)
    thisExp.addData('null2_4.started', null2_4.tStartRefresh)
    thisExp.addData('null2_4.stopped', null2_4.tStopRefresh)
    # check responses
    if answer_null_4.keys in ['', [], None]:  # No response was made
        answer_null_4.keys = None
    thisExp.addData('answer_null_4.keys',answer_null_4.keys)
    if answer_null_4.keys != None:  # we had a response
        thisExp.addData('answer_null_4.rt', answer_null_4.rt)
    thisExp.addData('answer_null_4.started', answer_null_4.tStartRefresh)
    thisExp.addData('answer_null_4.stopped', answer_null_4.tStopRefresh)
    thisExp.nextEntry()
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'trials_8'


# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=8.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions2"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    instr_2.setText(instructions2)
    # keep track of which components have finished
    instructions2Components = [instr_2]
    for thisComponent in instructions2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instructions2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_2* updates
        if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_2.frameNStart = frameN  # exact frame index
            instr_2.tStart = t  # local t and not account for scr refresh
            instr_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
            instr_2.setAutoDraw(True)
        if instr_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                instr_2.tStop = t  # not accounting for scr refresh
                instr_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_2, 'tStopRefresh')  # time at next scr refresh
                instr_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions2"-------
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instr_2.started', instr_2.tStartRefresh)
    thisExp.addData('instr_2.stopped', instr_2.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.xlsx', selection=rows),
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_2"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        cues_2.setText(cue_run2)
        adjectives_2.setText(adjective_run2)
        answer_2.keys = []
        answer_2.rt = []
        _answer_2_allKeys = []
        # keep track of which components have finished
        trial_2Components = [cues_2, adjectives_2, answer_2]
        for thisComponent in trial_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cues_2* updates
            if cues_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cues_2.frameNStart = frameN  # exact frame index
                cues_2.tStart = t  # local t and not account for scr refresh
                cues_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cues_2, 'tStartRefresh')  # time at next scr refresh
                cues_2.setAutoDraw(True)
            if cues_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cues_2.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    cues_2.tStop = t  # not accounting for scr refresh
                    cues_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cues_2, 'tStopRefresh')  # time at next scr refresh
                    cues_2.setAutoDraw(False)
            
            # *adjectives_2* updates
            if adjectives_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                adjectives_2.frameNStart = frameN  # exact frame index
                adjectives_2.tStart = t  # local t and not account for scr refresh
                adjectives_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(adjectives_2, 'tStartRefresh')  # time at next scr refresh
                adjectives_2.setAutoDraw(True)
            if adjectives_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > adjectives_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    adjectives_2.tStop = t  # not accounting for scr refresh
                    adjectives_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(adjectives_2, 'tStopRefresh')  # time at next scr refresh
                    adjectives_2.setAutoDraw(False)
            
            # *answer_2* updates
            waitOnFlip = False
            if answer_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                answer_2.frameNStart = frameN  # exact frame index
                answer_2.tStart = t  # local t and not account for scr refresh
                answer_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answer_2, 'tStartRefresh')  # time at next scr refresh
                answer_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(answer_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(answer_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if answer_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > answer_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    answer_2.tStop = t  # not accounting for scr refresh
                    answer_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(answer_2, 'tStopRefresh')  # time at next scr refresh
                    answer_2.status = FINISHED
            if answer_2.status == STARTED and not waitOnFlip:
                theseKeys = answer_2.getKeys(keyList=['2', '3'], waitRelease=False)
                _answer_2_allKeys.extend(theseKeys)
                if len(_answer_2_allKeys):
                    answer_2.keys = _answer_2_allKeys[-1].name  # just the last key pressed
                    answer_2.rt = _answer_2_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_2"-------
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('cues_2.started', cues_2.tStartRefresh)
        thisExp.addData('cues_2.stopped', cues_2.tStopRefresh)
        thisExp.addData('adjectives_2.started', adjectives_2.tStartRefresh)
        thisExp.addData('adjectives_2.stopped', adjectives_2.tStopRefresh)
        # check responses
        if answer_2.keys in ['', [], None]:  # No response was made
            answer_2.keys = None
        thisExp.addData('answer_2.keys',answer_2.keys)
        if answer_2.keys != None:  # we had a response
            thisExp.addData('answer_2.rt', answer_2.rt)
        thisExp.addData('answer_2.started', answer_2.tStartRefresh)
        thisExp.addData('answer_2.stopped', answer_2.tStopRefresh)
        thisExp.nextEntry()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_4'
    
    
    # ------Prepare to start Routine "instructions_null2"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    instructions_null2Components = [inst_null2]
    for thisComponent in instructions_null2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_null2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_null2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instructions_null2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_null2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst_null2* updates
        if inst_null2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst_null2.frameNStart = frameN  # exact frame index
            inst_null2.tStart = t  # local t and not account for scr refresh
            inst_null2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst_null2, 'tStartRefresh')  # time at next scr refresh
            inst_null2.setAutoDraw(True)
        if inst_null2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > inst_null2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                inst_null2.tStop = t  # not accounting for scr refresh
                inst_null2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(inst_null2, 'tStopRefresh')  # time at next scr refresh
                inst_null2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_null2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_null2"-------
    for thisComponent in instructions_null2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_6.addData('inst_null2.started', inst_null2.tStartRefresh)
    trials_6.addData('inst_null2.stopped', inst_null2.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials_5 = data.TrialHandler(nReps=10.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_5')
    thisExp.addLoop(trials_5)  # add the loop to the experiment
    thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    for thisTrial_5 in trials_5:
        currentLoop = trials_5
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "null_2"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        answer_null_2.keys = []
        answer_null_2.rt = []
        _answer_null_2_allKeys = []
        # keep track of which components have finished
        null_2Components = [null1_2, null2_2, answer_null_2]
        for thisComponent in null_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        null_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "null_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = null_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=null_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *null1_2* updates
            if null1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                null1_2.frameNStart = frameN  # exact frame index
                null1_2.tStart = t  # local t and not account for scr refresh
                null1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(null1_2, 'tStartRefresh')  # time at next scr refresh
                null1_2.setAutoDraw(True)
            if null1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > null1_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    null1_2.tStop = t  # not accounting for scr refresh
                    null1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(null1_2, 'tStopRefresh')  # time at next scr refresh
                    null1_2.setAutoDraw(False)
            
            # *null2_2* updates
            if null2_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                null2_2.frameNStart = frameN  # exact frame index
                null2_2.tStart = t  # local t and not account for scr refresh
                null2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(null2_2, 'tStartRefresh')  # time at next scr refresh
                null2_2.setAutoDraw(True)
            if null2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > null2_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    null2_2.tStop = t  # not accounting for scr refresh
                    null2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(null2_2, 'tStopRefresh')  # time at next scr refresh
                    null2_2.setAutoDraw(False)
            
            # *answer_null_2* updates
            waitOnFlip = False
            if answer_null_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                answer_null_2.frameNStart = frameN  # exact frame index
                answer_null_2.tStart = t  # local t and not account for scr refresh
                answer_null_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answer_null_2, 'tStartRefresh')  # time at next scr refresh
                answer_null_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(answer_null_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(answer_null_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if answer_null_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > answer_null_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    answer_null_2.tStop = t  # not accounting for scr refresh
                    answer_null_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(answer_null_2, 'tStopRefresh')  # time at next scr refresh
                    answer_null_2.status = FINISHED
            if answer_null_2.status == STARTED and not waitOnFlip:
                theseKeys = answer_null_2.getKeys(keyList=['2', '3'], waitRelease=False)
                _answer_null_2_allKeys.extend(theseKeys)
                if len(_answer_null_2_allKeys):
                    answer_null_2.keys = _answer_null_2_allKeys[-1].name  # just the last key pressed
                    answer_null_2.rt = _answer_null_2_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in null_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "null_2"-------
        for thisComponent in null_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('null1_2.started', null1_2.tStartRefresh)
        thisExp.addData('null1_2.stopped', null1_2.tStopRefresh)
        thisExp.addData('null2_2.started', null2_2.tStartRefresh)
        thisExp.addData('null2_2.stopped', null2_2.tStopRefresh)
        # check responses
        if answer_null_2.keys in ['', [], None]:  # No response was made
            answer_null_2.keys = None
        thisExp.addData('answer_null_2.keys',answer_null_2.keys)
        if answer_null_2.keys != None:  # we had a response
            thisExp.addData('answer_null_2.rt', answer_null_2.rt)
        thisExp.addData('answer_null_2.started', answer_null_2.tStartRefresh)
        thisExp.addData('answer_null_2.stopped', answer_null_2.tStopRefresh)
        thisExp.nextEntry()
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'trials_5'
    
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'trials_6'


# ------Prepare to start Routine "END"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
ENDComponents = [end]
for thisComponent in ENDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ENDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "END"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ENDClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ENDClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end* updates
    if end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end.frameNStart = frameN  # exact frame index
        end.tStart = t  # local t and not account for scr refresh
        end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end, 'tStartRefresh')  # time at next scr refresh
        end.setAutoDraw(True)
    if end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            end.tStop = t  # not accounting for scr refresh
            end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end, 'tStopRefresh')  # time at next scr refresh
            end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "END"-------
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end.started', end.tStartRefresh)
thisExp.addData('end.stopped', end.tStopRefresh)

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
