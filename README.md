[Kor Description 한국어 설명](https://github.com/ghkimvfx/dopesheet_range_lock/blob/main/Readme_kr.md)
![dsrl_thumbnail](https://github.com/user-attachments/assets/fcca0172-b24e-40df-8f54-aef88aa94eca)
# dopesheet_range_lock
Align and lock the Dope Sheet within Nuke to the project frame range
<br>
## Description
When applying effects such as Roto or Dissolve, keyframes are adjusted through the Dope Sheet, but sometimes the range starts from 0, which can be cumbersome.

Apply the code to `menu.py` to adjust and fix the range of the Dope Sheet to the frame range when Nuke is executed.

It may not work in projects before `menu.py` is applied.
<br>
## How to install
1. Download `dopesheet_range_lock.py` from this page.
2. Apply the code to `menu.py`
## How to use
Hover your mouse over the Dope sheet and press the F button.
If there is no change, close all the property windows and press F in the DopeSheet window to fix it.
This is useful for nodes that start from 0, such as Roto.
