# dopesheet_range_lock
Align and lock the Dope Sheet within Nuke to the project frame range
<br>
## Description
When applying effects such as Roto or Dissolve, keyframes are adjusted through the Dope Sheet, but sometimes the range starts from 0, which can be cumbersome.

Apply the code to `menu.py` to adjust and fix the range of the Dope Sheet to the frame range when Nuke is executed.

It may not work in projects before `menu.py` is applied.
<br>
## How to install
Apply the code to `menu.py`
<br>
## How to use
Hover your mouse over the Dope sheet and press the F button.
If there is no change, close all the property windows and press F in the DopeSheet window to fix it.
This is useful for nodes that start from 0, such as Roto.
