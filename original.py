r/bin/python

# All Pitch Conversion Functions in One Place!
# (And the imports and globals they need to run)
#
# !IMPORTANT!
# These functions call each other so should be
# kept as a group and defined in the order below
#
# So we gots the following:
#
# 1) Imports and Globals
#
# 2) MilsToFrequency(x)
#   Receives an interval from the frequency
#   of root_pitch root_pitch[‘freq’]), expressed
#   in mils. A positive value means the interval
#   extends above root_pitch while a negative
#   value means the interval extends below.
#   Returns the frequency of the pitch that
#   interval away from root_pitch.
#
# 3) FreqToMils(x)
#   Receives a frequency, returns interval in
#   mils between that frequency and the
#   frequency of root_pitch (root_pitch[‘freq’]).
#   Returns positive value if given frequency
#   is higher than root_pitch, negative if lower
#
# 4) MilsToNote(x)
#   Receives an interval from the frequency
#   of root_pitch root_pitch[‘freq’]), expressed
#   in mils. A positive value means the interval
#   extends above root_pitch while a negative
#   value means the interval extends below.
#   Returns a dictionary with three objects:
#       ‘note’ - C, D, F etc
#       ‘8ve’ - What octave the note is in.
#       Octaves run from C up to B, A4
#       being concert A
#       ‘mils’ - how ‘sharp’ (positive value)
#       or ‘flat’ (negative value) the note is
#
# 5)FreqToNote(x)
#   Recieves frequency.
#   Returns a dictionary with three objects:
#       ‘note’ - C, D, F etc
#       ‘8ve’ - What octave the note is in.
#       Octaves run from C up to B, A4
#       being concert A
#       ‘mils’ - how ‘sharp’ (positive value)
#       or ‘flat’ (negative value) the note is
# 6)FreqToValidFreq(x)
#   Recieves a frequency, returns the closest
#   frequency with a valid (int) mils value

# 1) Imports and Globals

from math import log

root_pitch = {\
'note': 'C', \
'8ve': -10, \
'mils': 0, \
'freq': 0.0159683837891}

# 2) MilsToFreq

def MilsToFreq(m):
    f = root_pitch['freq']*(2**(float(m)/12000))
    return f;

# 3) FreqToMils

def FreqToMils(f):
    if f == 0:
        print '0 not a valid frequency, what you playing at!?'
    else:
        m = int(round(12000* log(f/root_pitch['freq'],2)))
        return m;

# 4) MilsToNote

def MilsToNote(n):

    NoteNameTuple = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
    
        
    def PosNeg(mils):
        if mils > 500:
            mils -= 1000
        return mils;

    return_value = {\
    'note': NoteNameTuple[int(((n+499)%12000)/1000)],\
    '8ve': int((n/12000)+root_pitch['8ve']),\
    'mils': PosNeg(n%1000)}

    return return_value;

# 5) FreqToNote

def FreqToNote(f):
    return MilsToNote(FreqToMils(f));

#6) FreqToValidFreq

def FreqToValidFreq(f):
    return MilsToFreq(FreqToMils(f));


