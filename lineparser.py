#!/usr/bin/python3
import re
import pickle

# Deprecated pattern (kept for reference)
# pattern = r'^(\s{6,}.+$|((((?P<speaker>[A-Z\s]{2,}\.)|\s+))\s+(?P<stanza>.+?[a-z](\s{0,2}[^\s]+)+)((\s{3,})*.*)?))$'
# Regex pattern magic to extract files from Project Gutenberg file.
pattern = r'^((?P<scrap>\s{6,}.+$)|((((?P<speaker>[A-Z\s]{2,}\.)|\s+))\s+(?P<scrap2>([A-Z]\s*){3,}\,.+)?(?P<stanza>.+?[a-z](\s{0,2}[^\s]+)+)?((\s{3,})*.*)?))$'

# Empty list to store lines
linesList = []
prog = re.compile(pattern)
speaker = ''
# 'source.txt' is source file for Shakespeare lines
with open('complete_works.txt') as f:
    for i, line in enumerate(f):
        # run regex and generate 'match' object
        match = prog.match(line)
        # if matches are found, add them to the list
        if prog.match(line) is not None:
            d = match.groupdict()
            if d['stanza'] is not None:
                if d['speaker'] is not None:
                    speaker = d['speaker']
                # Adds lines to the list as a tuple: (speaker, stanza)
                linesList.append((speaker.strip(), d['stanza'].strip()))
                # Prints lines (for testing):
                # print(d['stanza'])

        # This code runs the opposite, it displays all removed text:
        # if prog.match(line) is not None:
        #     d = match.groupdict()
        #     if d['scrap'] is not None or d['scrap2'] is not None:
        #         print(d['scrap'], d['scrap2'])

# Write generated line list to file 'lines.pkl'
with open('lines.pkl','wb') as f:
    pickle.dump(linesList, f)