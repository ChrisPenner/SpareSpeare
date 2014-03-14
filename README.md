SpareSpeare
===========
SpareSpeare is a Lorem ipsum style Shakespeare filler text generator written in Python 3. Lorem ipsum is old news.

It contains a large library of lines from the complete works of shakespeare.

Simply ask for a certain amount of lines or words, sparespeare will deliver, useful for projects in which filler text is needed.

#Usage
Import the module, then call getLines(#) or getWords(#)

```
Python 3:
>>> import sparespeare
>>> sparespeare.getLines(3)
'Canst thou not minister to a mind diseased,\nPluck from the memory a rooted sorrow,\nRaze out the written troubles of the brain,'
>>> print(sparespeare.getLines(3))
And your courtesy, for a ring-carrier!
The troop is past. Come, pilgrim, I will bring you
Where you shall host. Of enjoin'd penitents

>>> sparespeare.getWords(10)
'A joyless, dismal, black, and sorrowful issue! Here is the'

```

Keyword options (default)  include:

* returnList (False) : returns lines as a python list instead of a string.
* listSpeaker (False) : prints the speaker of the line before the line itself
* newLine (True) : adds newline to end of each line

Use caution with listSpeaker, as it's not perfect at guessing and sometimes inserts strange heading artifacts, e.g. "ACT III. ......"

```python
>>> sparespeare.getLines(3, returnList=True)
['That seeks not to find that her search implies,\n', 'But, riddle-like, lives sweetly where she dies!\n', 'Had you not lately an intent-speak truly-']
>>> print(sparespeare.getLines(3, listSpeaker=True))
LENNOX. For Fleance fled. Men must not walk too late.
LENNOX. Who cannot want the thought, how monstrous
LENNOX. It was for Malcolm and for Donalbain
>>> sparespeare.getLines(3, newLine=False)
'You do him wrong, surely. Sir, I was an inward of his. A shy fellow was the Duke; and I believe I know the cause of his withdrawing.'

```

#MISC
Only **sparespeare.py** and **lines.pkl** are necessary for proper usage.

* **complete_works.txt** is included for reference and copyright information
* **lineparser.py** is the script used to generate the database, though it's so specialized it likely won't be useful for much else.
