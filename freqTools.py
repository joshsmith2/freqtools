#!usr/bin/python

"""
All Pitch Conversion Functions in One Place!
(And the imports and globals they need to run)

!IMPORTANT!
These functions call each other so should be
kept as a group and defined in the order below

So we gots the following:

1) Imports and Globals

2) mils_to_frequency(x)
  Receives an interval from the frequency
  of root_pitch root_pitch['freq']), expressed
  in mils. A positive value means the interval
  extends above root_pitch while a negative
  value means the interval extends below.
  Returns the frequency of the pitch that
  interval away from root_pitch.

3) freq_to_mils(x)
  Receives a frequency, returns interval in
  mils between that frequency and the
  frequency of root_pitch (root_pitch['freq']).
  Returns positive value if given frequency
  is higher than root_pitch, negative if lower

4) mils_to_note(x)
  Receives an interval from the frequency
  of root_pitch root_pitch['freq']), expressed
  in mils. A positive value means the interval
  extends above root_pitch while a negative
  value means the interval extends below.
  Returns a dictionary with three objects:
      note - C, D, F etc
      8ve - What octave the note is in.
      Octaves run from C up to B, A4
      being concert A
      mils - how 'sharp' (positive value)
      or 'flat' (negative value) the note is

5)freq_to_note(x)
  Receives frequency.
  Returns a dictionary with three objects:
      note - C, D, F etc
      8ve - What octave the note is in.
      Octaves run from C up to B, A4
      being concert A
      mils - how 'sharp' (positive value)
      or 'flat' (negative value) the note is
6)freq_to_valid_freq(x)
  Receives a frequency, returns the closest
  frequency with a valid (int) mils value
"""

from math import log

root_pitch = {\
'note': 'C', \
'8ve': -10, \
'mils': 0, \
'freq': 0.0159683837891}

def mils_to_freq(m):
    """
    Receives an interval from the frequency
    of root_pitch root_pitch['freq']), expressed
    in mils. A positive value means the interval
    extends above root_pitch while a negative
    value means the interval extends below.
    Returns the frequency of the pitch that
    interval away from root_pitch."""
    f = root_pitch['freq']*(2**(float(m)/12000))
    return f;

def freq_to_mils(f):
    """  Receives a frequency, returns interval in
    mils between that frequency and the
    frequency of root_pitch (root_pitch['freq']).
    Returns positive value if given frequency
    is higher than root_pitch, negative if lower"""
    if f == 0:
        raise Exception('0 not a valid frequency, what you playing at!?')
    else:
        m = int(round(12000* log(f/root_pitch['freq'],2)))
        return m;

def mils_to_note(n):
    """  Receives an interval from the frequency
    of root_pitch root_pitch['freq']), expressed
    in mils. A positive value means the interval
    extends above root_pitch while a negative
    value means the interval extends below.
    Returns a dictionary with three objects:
        note - C, D, F etc
        8ve - What octave the note is in.
        Octaves run from C up to B, A4
        being concert A
        mils - how 'sharp' (positive value)
        or 'flat' (negative value) the note is"""

    note_name_tuple = ('C', 'C#', 'D', 'D#', 'E', 'F',
                       'F#','G', 'G#', 'A', 'A#', 'B')
        
    def pos_neg(mils):
        """Receives a value in mils between 0 and 999.
        If this is more than 500 it subtracts 1000
        """
        if mils > 500:
            mils -= 1000
        return mils;

    return_value = {\
    'note': note_name_tuple[int(((n+499)%12000)/1000)],\
    '8ve': int((n/12000)+root_pitch['8ve']),\
    'mils': pos_neg(n%1000)}

    return return_value;

def freq_to_note(f):
    """Receives frequency.
    Returns a dictionary with three objects:
        note - C, D, F etc
        8ve - What octave the note is in.
        Octaves run from C up to B, A4
        being concert A
        mils - how 'sharp' (positive value)
        or 'flat' (negative value) the note is"""
    return mils_to_note(freq_to_mils(f));

def freq_to_valid_freq(f):
    """
    Receives a frequency, returns the closest
    frequency with a valid (int) mils value"""
    return mils_to_freq(freq_to_mils(f));

def freq_at_octave(freq_at_zero, target_octave):
    """Given the frequency at octave 0, returns the frequency at 
    target_octave.
    """
    target_frequency = 0

    if target_octave<0:
        b = (target_octave*-2)/2
    else:
        b = target_octave


    for a in range(0,b):
        if target_octave>0:
           target_frequency *=2
        else:
           target_frequency /=2
    target_frequency = freq_at_zero
    return target_frequency;

