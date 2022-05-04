

import time
from random import choice

def intro():
    print('The Guitar Oracle is listening.')
    time.sleep(2)

def ask():
    practicing = True
    while practicing:
        keys = ['C','F','Bb','Eb','Ab','Db','Gb','Cb','G','D','A','E','B','F#','C#','Something else']
        key = input("Choose your key: ").capitalize()
        if (key not in keys):
            responses1 = ["How dare you defy me??", "Try a letter between A and G", "Do not anger the Guitar Gods", "Don't get cheeky", "Try again"]
            q1 = choice(responses1)
            print(q1)

        if (key == 'C'):
            print('You chose C, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                cmajor = ['C Ionian: C – D – E – F – G – A – B','C Lydian: C - D - E - F# - G - A - B','C Mixolydian: C - D - E - F - G - A - Bb', 'C Maj Pentatonic: C - D - E - G - A']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(cmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(cmajor),choice(cmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(cmajor),choice(cmajor),choice(cmajor)
                        print(q2)
            if (majmin == "minor"):
                cminor = ['C Dorian: C - D - Eb - F - G - A - Bb','C Phrygian: C - Db - Eb - F - G - Ab - Bb', 'C Aeolian: C - D - Eb - F - G - Ab - Bb','C Locrian: C - Db - Eb - F - Gb - Ab - Bb', 'C Harmonic Minor: C - D - Eb - F - G - Ab - B','C Melodic Minor: C - D - Eb - F - G - A - B','C Min Pentatonic: C - Eb - F - G - Bb']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(cminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(cminor),choice(cminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(cminor),choice(cminor),choice(cminor)
                        print(q2)

        if (key == 'F'):
            print('You chose F, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                fmajor = ['F Ionian: F – G – A – Bb – C – D – E','F Lydian: F - G - A - B - C - D - E','F Mixolydian: F - G - A - Bb - C - D - Eb','F Maj Pentatonic: F - G - A - C - D']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(fmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(fmajor),choice(fmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(fmajor),choice(fmajor),choice(fmajor)
                        print(q2)
            if (majmin == "minor"):
                fminor = ['F Dorian: F - G - Ab - Bb - C - D - Eb','F Phrygian: F - Gb - Ab - Bb - C - Db - Eb', 'F Aeolian: F - G - Ab - Bb - C - Db - Eb','F Locrian: F - Gb - Ab - Bb - Cb - Db - Eb','F Melodic Minor: F - G - Ab - Bb - C - D - E','F Min Pentatonic: F - Ab - Bb - C - Eb']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(fminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(fminor),choice(fminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(fminor),choice(fminor),choice(fminor)
                        print(q2)

        if (key == 'Bb'):
            print('You chose Bb, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                bbmajor = ['Bb Ionian: Bb – C – D – Eb – F – G – A','Bb Lydian: Bb – C – D – E – F – G – A','Bb Mixolydian: Bb – C – D – Eb – F – G – Ab','Bb Maj Pentatonic: Bb - C - D - F - G']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(bbmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(bbmajor),choice(bbmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(bbmajor),choice(bbmajor),choice(bbmajor)
                        print(q2)
            if (majmin == "minor"):
                bbminor = ['Bb Dorian: Bb - C - Db - Eb - F - G - Ab','Bb Phrygian: Bb – Cb – Db – Eb – F – Gb – Ab','Bb Aeolian: Bb - C - Db - Eb - F - Gb - Ab','Bb Locrian: Bb - B - Db - Eb - E - Gb - Ab', 'Bb Harmonic Minor: Bb - C - Db -Eb - F - Gb - A','Bb Melodic Minor: Bb - C - Db - Eb - F - G - A', 'B Flat Min Pentatonic: Bb - Db - Eb - F - Ab']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(bbminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(bbminor),choice(bbminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(bbminor),choice(bbminor),choice(bbminor)
                        print(q2)

        if (key == 'Eb'):
            print('You chose Eb, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                ebmajor = ['Eb Ionian: ','Eb Lydian: Eb - F - G - A - Bb - C - D','Eb Mixolydian: Eb - F - G - A - Bb - C - D','Eb Maj Pentatonic: Eb - F - G - Bb - C']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(ebmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(ebmajor),choice(ebmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(ebmajor),choice(ebmajor),choice(ebmajor)
                        print(q2)
            if (majmin == "minor"):
                ebminor = ['Eb Dorian: Eb – F – Gb – Ab – Bb – C – Db','Eb Phrygian: Eb – Fb – Gb – Ab – Bb – Cb – Db','Eb Aeolian: Eb – F – Gb – Ab – Bb – Cb – Db','Eb Locrian: Eb – Fb – Gb – Ab – Bbb – Cb – Db.', 'Eb Harmonic Minor: Eb - F - Gb - Ab - Bb - Cb - D', 'Eb Melodic Minor: Eb - F - Gb - Ab - Bb - C - D','Eb Min Pentatonic: Eb - Gb - Ab - Bb - Db']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(ebminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(ebminor),choice(ebminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(ebminor),choice(ebminor),choice(ebminor)
                        print(q2)

        if (key == 'Ab'):
            print('You chose Ab, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                abmajor = ['Ab Ionian: Ab – Bb – C – Db –Eb – F – G','Ab Lydian: Ab – Bb – C – D – Eb – F – G','Ab Mixolydian: Ab – Bb –C – Db – Eb – F – Gb','G# Maj Pentatonic: G# - A# - B# - D# - E#']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(abmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(abmajor),choice(abmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(abmajor),choice(abmajor),choice(abmajor)
                        print(q2)
            if (majmin == "minor"):
                abminor = ['Ab Dorian: Ab – Bb – Cb – Db – Eb – F – Gb','Ab Phrygian: Ab – Bbb – Cb – Db – Eb – Fb – Gb','Ab Aeolian: Ab – Bb – Cb – Db – Eb – Fb – Gb','Ab Locrian: Ab - Bbb - Cb - Db - Ebb - Fb - Gb', 'Ab Harmonic Minor: Ab, Bb, Cb, Db, Eb, Fb, G','Ab Melodic Minor: Ab - Bb - Cb - Db - Eb - F - G','G# Min Pentatonic: G# - B - C# - D# - F#']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(abminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(abminor),choice(abminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(abminor),choice(abminor),choice(abminor)
                        print(q2)

        if (key == 'Db'):
            print('You chose Db, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                dbmajor = ['Db Ionian: Db – Eb – F – Gb – Ab – Bb – C','Db Lydian: Db - Eb - F - G - Ab - Bb - C', 'Db Mixolydian: Db - Eb - F - Gb - Ab - Bb - Cb', 'C# Maj Pentatonic: C# - D# - E# - G# - A#']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(dbmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(dbmajor),choice(dbmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(dbmajor),choice(dbmajor),choice(dbmajor)
                        print(q2)
            if (majmin == "minor"):
                dbminor = ['Db Aeolian: Db – Eb – Fb – Gb – Ab – Bbb – Cb','Db Melodic Minor: Db - Eb - Fb - Gb - Ab - Bb - C','C# Min Pentatonic: C# - E - F# - G# - B']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(dbminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(dbminor),choice(dbminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(dbminor),choice(dbminor),choice(dbminor)
                        print(q2)

        if (key == 'Gb'):
            print('You chose Gb, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                gbmajor = []
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(gbmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(gbmajor),choice(gbmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(gbmajor),choice(gbmajor),choice(gbmajor)
                        print(q2)
            if (majmin == "minor"):
                gbminor = ['F# Dorian: F# - G# - A - B - C# - D# - E','F# Phrygian: F# - G - A - B - C# - D - E','F# Aeolian: F# - G# - A - B - C# - D - E','F# Locrian: F# - G - A - B - C - D - E','F# Harmonic Minor: F# - G# - A - B - C# - D - E#','F# Melodic Minor: F# - G# - A - B - C# - D# - E#','F# Min Pentatonic: F# - A - B - C# - E']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(gbminor)
                        print('The guitar gods have shown mercy, and answered your question in the key of F#: ',q2)
                    elif (levels == 2):
                        q2 = choice(gbminor),choice(gbminor)
                        print('The guitar gods have shown mercy, and answered your question in the key of F#: ',q2)
                    elif (levels == 3):
                        q2 = choice(gbminor),choice(gbminor),choice(gbminor)
                        print('The guitar gods have shown mercy, and answered your question in the key of F#: ',q2)

        if (key == 'Cb'):
            print('C flat? Continue...')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                cbmajor = ['B Ionian: B - C# - D# - E - F# - G# - A#','B Lydian: B - C# - D#- E# - F# - G#- A#','B Mixolydian: B - C# - D# - E - F# - G# - A','B Maj Pentatonic: B - C# - D# - F# - G#']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(cbmajor)
                        print('The guitar gods have shown mercy, and answered your question in the key of B: ',q2)
                    elif (levels == 2):
                        q2 = choice(cbmajor),choice(cbmajor)
                        print('The guitar gods have shown mercy, and answered your question in the key of B: ',q2)
                    elif (levels == 3):
                        q2 = choice(cbmajor),choice(cbmajor),choice(cbmajor)
                        print('The guitar gods have shown mercy, and answered your question in the key of B: ',q2)
            if (majmin == "minor"):
                cbminor = ['B Dorian: B - C# - D - E - F# - G# - A','B Phrygian: B - C - D - E - F# - G - A','B Aeolian: B - C# - D - E - F# - G - A','B Locrian: B - C - D - E - F - G - A','B Melodic Minor: B - C# - D - E - F# - G# - A#','B Min Pentatonic: B - D - E - F# - A']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(cbminor)
                        print('The guitar gods have shown mercy, and answered your question in the key of B: ',q2)
                    elif (levels == 2):
                        q2 = choice(cbminor),choice(cbminor)
                        print('The guitar gods have shown mercy, and answered your question in the key of B: ',q2)
                    elif (levels == 3):
                        q2 = choice(cbminor),choice(cbminor),choice(cbminor)
                        print('The guitar gods have shown mercy, and answered your question in the key of B: ',q2)

        if (key == 'G'):
            print('You chose G, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                gmajor = ['G Ionian: G – A – B – C – D – E – F#','G Lydian: G - A - B - C# - D - E - F#','G Mixolydian: G - A - B - C - D - E - F','G Maj Pentatonic: G - A - B - D - E']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(gmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(gmajor),choice(gmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(gmajor),choice(gmajor),choice(gmajor)
                        print(q2)
            if (majmin == "minor"):
                gminor = ['G Dorian: G - A - Bb - C - D - E - F','G Phrygian: G - Ab - Bb - C - D - Eb - F','G Aeolian: G - A - Bb - C - D - Eb - F','G Locrian: G - Ab - Bb - C - Db - Eb - F','G Melodic Minor: G - A - Bb - C - D - E - F#','G Min Pentatonic: G - Bb - C - D - F']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(gminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(gminor),choice(gminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(gminor),choice(gminor),choice(gminor)
                        print(q2)

        if (key == 'D'):
            print('You chose D, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                dmajor = ['D Ionian: D - E - F♯ - G - A - B - C♯','D Lydian: D – E – F# – G# – A – B – C#','D Mixolydian: D - E - F# - G - A - B - C', 'D Maj Pentatonic: D - E - F# - A - B']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(dmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(dmajor),choice(dmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(dmajor),choice(dmajor),choice(dmajor)
                        print(q2)
            if (majmin == "minor"):
                dminor = ['D Dorian: D - E - F - G  - A - B - C - D','D Phrygian: D – Eb – F – G – A – Bb – C', 'D Aeolian: D - E - F - G - A - Bb - C','D Locrian: D - Eb - F - G - Ab - Bb - C','D Melodic Minor: D - E - F - G - A - B - C#','D Min Pentatonic: D - F - G - A - C']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(dminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(dminor),choice(dminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(dminor),choice(dminor),choice(dminor)
                        print(q2)

        if (key == 'A'):
            print('You chose A, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                amajor = ['A Lydian: A - B - C#- D# - E - F#- G#','A Mixolydian: A - B - C# - D - E - F# - G', 'A Ionian: A – B – C# – D – E – F# – G#','A Maj Pentatonic: A - B - C# - E - F#']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(amajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(amajor),choice(amajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(amajor),choice(amajor),choice(amajor)
                        print(q2)
            if (majmin == "minor"):
                aminor = ['A Dorian: A - B - C - D - E - F# - G','A Phrygian: A - Bb - C - D - E - F - G','A Aeolian: A - B - C - D - E - F - G','A Locrian: A - Bb - C - D - Eb - F - G','A Melodic Minor: A - B - C - D - E - F# - G#','A Min Pentatonic: A - C - D - E - G']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(aminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(aminor),choice(aminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(aminor),choice(aminor),choice(aminor)
                        print(q2)

        if (key == 'E'):
            print('You chose E, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                emajor = ['E Ionian: E – F# – G# – A – B – C# – D#','E Lydian: E - F# - G# - A# - B - C# - D#','E Mixolydian: E - F# - G# - A - B - C# - D','E Maj Pentatonic: E - F# - G# - B - C#']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(emajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(emajor),choice(emajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(emajor),choice(emajor),choice(emajor)
                        print(q2)
            if (majmin == "minor"):
                eminor = ['E Dorian: E - F# - G - A - B - C# - D','E Phrygian: E - F - G - A - B - C - D', 'E Aeolian: E - F# - G - A - B - C - D','E Locrian: E - F - G - A - Bb - C - D','E Melodic Minor: E - F# - G - A - B - C# - D#','E Min Pentatonic: E - G - A - B - D','E Harmonic Minor: E - F# - G - A - B - C - D#']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(eminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(eminor),choice(eminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(eminor),choice(eminor),choice(eminor)
                        print(q2)

        if (key == 'B'):
            print('You chose B, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                bmajor = ['B Ionian: B - C# - D# - E - F# - G# - A#','B Lydian: B - C# - D#- E# - F# - G#- A#','B Mixolydian: B - C# - D# - E - F# - G# - A','B Maj Pentatonic: B - C# - D# - F# - G#']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(emajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(emajor),choice(emajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(emajor),choice(emajor),choice(emajor)
                        print(q2)
            if (majmin == "minor"):
                bminor = ['B Dorian: B - C# - D - E - F# - G# - A','B Phrygian: B - C - D - E - F# - G - A','B Aeolian: B - C# - D - E - F# - G - A','B Locrian: B - C - D - E - F - G - A','B Melodic Minor: B - C# - D - E - F# - G# - A#','B Min Pentatonic: B - D - E - F# - A']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(bminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(bminor),choice(bminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(bminor),choice(bminor),choice(bminor)
                        print(q2)

        if (key == 'F#'):
            print('You chose F#, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                fsmajor = ['F# Major: F# G# A# B C# D# E#','F# Lydian: F# – G# – A# – B# – C# – D# – E#','F# Mixolydian: F# – G# – A# – B – C# – D# – E','F# Maj Pentatonic: F# - G# - A# - C# - D#']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(fsmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(fsmajor),choice(fsmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(fsmajor),choice(fsmajor),choice(fsmajor)
                        print(q2)
            if (majmin == "minor"):
                fsminor = ['F# Dorian: F# - G# - A - B - C# - D# - E','F# Phrygian: F# - G - A - B - C# - D - E','F# Aeolian: F# - G# - A - B - C# - D - E','F# Locrian: F# - G - A - B - C - D - E','F# Harmonic Minor: F# - G# - A - B - C# - D - E#','F# Melodic Minor: F# - G# - A - B - C# - D# - E#','F# Min Pentatonic: F# - A - B - C# - E']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(fsminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(fsminor),choice(fsminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(fsminor),choice(fsminor),choice(fsminor)
                        print(q2)

        if (key == 'C#'):
            print('You chose C#, Excellent')
            majmin = input("Major or Minor?: ").lower()
            if (majmin == "major"):
                csmajor = ['C# Ionian: C# – D# – E# – F# – G# – A# – B#','C# Lydian: C# - D# - E# - Fx - G# - A# - B','C# Mixolydian C# - D# - E# - F# - G# - A# - B','C# Maj Pentatonic: C# - D# - E# - G# - A#']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(csmajor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(csmajor),choice(csmajor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(csmajor),choice(csmajor),choice(csmajor)
                        print(q2)
            if (majmin == "minor"):
                csminor = ['C# Phyrgian: C# - D - E - F# - G# - A - B', 'C# Aeolian: C# D# E F# G# A B','C# Melodic Minor: C# - D# -E - F# - G# - A# - B#','C# Locrian: C# - D - E - F# - G - A - B''C# Harmonic Minor: C# - D# - E - F# - G# - A - B#','C# Min Pentatonic: C# - E - F# - G# - B']
                levels = input("Choose your level (1, 2, or 3): ")
                validLevel = range(1,4)
                if (levels.isnumeric()):
                    levels = int(levels)
                    if (levels == 1):
                        q2 = choice(csminor)
                        print(q2)
                    elif (levels == 2):
                        q2 = choice(csminor),choice(csminor)
                        print(q2)
                    elif (levels == 3):
                        q2 = choice(csminor),choice(csminor),choice(csminor)
                        print(q2)


                if (levels not in validLevel):
                    responses2 = ["You are not worthy","A brave, foolish soul once asked the same thing","Some day...", "The Guitar Gods have denied your request"]
                    levRes = choice(responses2)
                    print(levRes)

        if (key == 'Something else'):
            ask2 = input("What would you like to know?").lower()
            if (ask2 == 'circle of fifths' or 'circle of fourths' or 'cycle of fourths'):
                print("Very well...")
                time.sleep(1.0)
                print("The circle of fifths reads clockwise starting with C - which has no sharps or flats. The (a) shown, is the relative minor key of C. G shows (e) as the relative minor, and the 1# shows there is 1 sharp in the key. Follow this pattern and notice the number of flats decrease from Gb back to F.")
                print("C(a) - G(e) 1# - D(b) 2# - A(f#) 3# - E(c#) 4# - B(g#) 5# - Gb/F#(e#/d#) 6#(6b)  - Db/C#(bb/a#) 7#(5b) - Ab(f) 4b - Eb(c) 3b - Bb(g) 2b - F(d) 1b")

        keepPracticing = input("Do you want to keep practicing (yes or no): ")
        validUser = ["yes","sure","yup","ok","okay","k","hell yeah","mkay","yeah","yea"]
        if (keepPracticing not in validUser):
            practicing = False
            print("Goodbye")

if __name__ == "__main__":
    intro()
    ask()
