SpareSpeare
===========
-----------
Lorem ipsum style Shakespeare Text Generator,

Contains a large library of lines from the complete works of shakespeare
simply ask for a certain amount of lines.

#Usage
------
Import the module, then call getLines()

```python
>>> import sparespeare
>>> sparespeare.getLines(3)
'Canst thou not minister to a mind diseased,\nPluck from the memory a rooted sorrow,\nRaze out the written troubles of the brain,'
>>> print(sparespeare.getLines(3))
And your courtesy, for a ring-carrier!
The troop is past. Come, pilgrim, I will bring you
Where you shall host. Of enjoin'd penitents
```

Keyword options (default)  include:

* returnList (False) : returns lines as a python list instead of a string.
* listSpeaker (False) : prints the speaker of the line before the line itself

Use caution with listSpeaker, as it's not perfect at guessing and sometimes inserts strange heading artifacts, e.g. "ACT III. ......"

```python
>>> sparespeare.getLines(3, returnList=True)
['That seeks not to find that her search implies,\n', 'But, riddle-like, lives sweetly where she dies!\n', 'Had you not lately an intent-speak truly-']
>>> print(sparespeare.getLines(3, listSpeaker=True))
LENNOX. For Fleance fled. Men must not walk too late.
LENNOX. Who cannot want the thought, how monstrous
LENNOX. It was for Malcolm and for Donalbain
```

