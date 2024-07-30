# Emotional Go/No-Go Task

Build V1.2 : 04/06/2021

Created by Michael Colwell (michael.colwell@psych.ox.ac.uk / ORCID 0000-0001-7846-2879), 2021

## License: 
The task materials and preprocessing script are offered free of charge for researchers. **It is requested that researchers who publish data using these materials (task or preprocessing script) cite the below paper(s) in relevant publications.**

**Please cite the reference below**:

*Main paper reference:*

Colwell, M. J., Tagomori, H., Shang, F., Hoi Iao, C., Wigg, C. E., Browning, M., Cowen, P. J., Murphy, S. E., & Harmer, C. J. (2024). 
Direct serotonin release in humans shapes aversive learning and inhibition. _Nature Communications_, **15**. https://doi.org/10.1038/s41467-024-50394-x

You may also wish to include reference to the below image sets which were used as stimuli within the task:

*KDEF reference:*

Lundqvist, D., Flykt, A., &  Öhman, A. (1998). _The Karolinska Directed Emotional Faces - KDEF_, CD ROM from Department of Clinical Neuroscience, Psychology section, Karolinska Institutet, ISBN 91-630-7164-9.

*RADIATE reference:*

Conley, M. I., Dellarco, D. V., Rubien-Thomas, E., Cohen, A. O., Cervera, A., Tottenham, N., & Casey, B. J. (2018). The racially diverse affective expression (RADIATE) face stimulus set. _Psychiatry Research_, **270**.

This task is currently in-use in the Psychopharmacology and Emotion Laboratory (PERL) at the Department of Psychiatry, University of Oxford. Multiple ongoing psychopharmacology projects are using this task (e.g., PEACE; NCT05849675). 

## Change log
*21/01/2022 Note: Updated Readme.md and pushed folder containing preprocessing scripts for researchers to use, to better enhance reproducibility.*

**1.1 -> 1.2** Update - Added two versions for between-subjects designs. You no longer need to use excel to randomise the excel
files at the beginning of experiments. I have retained the randomiser within the excel sheet in case anyone would like to use
this for future designs that require random stimuli orders for each participant.

This is a psychopy-based emotional go/no-go task. Go/No-go tasks measure response inhibition, an index of executive functioning.
This particular task has been created to embded emotional distractors to observe their impact on response inhibition.
The task contains happy and fearful faces, as well as 'scrambled' faces to serve as non-emotional controls.
Please follow the instructions below to run the task. (NOTE: Ideally this task should run on a high refresh rate monitor (e.g.
120hz) given the timing at which stimuli appear. Psychopy will automatically sync the frame rate to the monitor refresh rate.)

## Instructions:

*Basics*
1. Download Psychopy (version v2020.2.8 and above) - https://www.psychopy.org/download.html
2. Once installed, unzip the contents of this folder to a location on your computer
3. Open the 'Emotional Go No-Go Task (Psychopy) folder and double click on 'Emotional Go No-Go Task.psyexp'

*NO LONGER REQUIRED: Set up conditions files*
4. Nagivate to the 'Conditions' folder and open 'BlueFearStop.xlsx' in excel
5. Once open, double click on any blank cell and hit enter (the numbers in column 'H' should shuffle)
6. Go to cell H2 ('SORT_BY_SMALLEST') and click on the filter box - set filter to sort 'smallest to largest'.
7. Check if there are any cells in column 'G' which say 'TRIPLICATE DETECTED' in red; if there are, then repeat Step 6 until the there are no 'TRIPLICATES DETECTED' in column G.
8. Save the file once completed (Ctrl + S)
9. Repeat Steps 5-8 for the other 5 .xlsx files in this folder.

*Run Experiment*
10. Once all conditions files have been saved, go back to the PsychoPy builder window
11. Click 'run' experiment and follow onscreen instructions
12. Once the experiment has ended, you will find your test data in the 'data' folder.

**Thank you for reading!**

------------------------------------------

## Additional details about task:

- This task contains six blocks with a possibility of two randomly selected block orders; the block orders were chosen so that there was an equal number of rule set-shifts (3 blocks per run),
and a fixed-rate where it does not occur (3 blocks per run). Rules are balanced with emotional distractors so that each emotional distract appears once with a set-shift and once without a set shift. The two block orders
are detailed below:

........................Order_1.........Order_2
Colour rule.............YYB YBB   OR    YBB YYB
Emotional distractor....FSS HFH         HFH FSS
SETSHIFT/WITHOUT........WWS SSW         WSW SWS

*Abbrv.: Y=Yellow, B=Blue; F=Fear, SS=Scrambled, H=Happy; W = Without set-shifting, S = set-shifting*

- All images in the task were derived from the KDEF and RADIATE face packages. The original filenames from these packages were retained in this program. 
- All images from the RADIATE package were adjusted to match the luminosity of the KDEF package.
- Scrambled faces were achieved using the third-party plugin for Photoshop 'Scramble' (credit to Telegraphics) set at a 5px5p scramble.
- 'Gos' are presented at 75% across all blocks, and 'No-Gos' 25%
- Images appear for 300ms
- Both 'Go' and 'No-go' trials are balanced so that each block contains an equal gender and use of both face packages (50:50 both).

------------------------------------------
