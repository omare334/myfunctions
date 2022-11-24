# see if a is within 10 percent of b
from turtle import pd
import pandas as pd

def within_10_percent(a,b):
 if abs( (a - b) / float(a) ) <= 0.10:
    print('True')
 else:
    print('False')


"""Return a grammatically correct human readable string (with an Oxford comma)."""
 # Ref: https://stackoverflow.com/a/53981846/
from typing import Any, List

def readable_list(seq: List[Any]) -> str:
    """Return a grammatically correct human readable string (with an Oxford comma)."""
    # Ref: https://stackoverflow.com/a/53981846/
    seq = [str(s) for s in seq]
    if len(seq) < 3:
        return ' and '.join(seq)
    return ', '.join(seq[:-1]) + ', and ' + seq[-1]



def readable_list2(_s):
  if len(_s) < 3:
    return ' and '.join(map(str, _s))
  *a, b = _s
  return f"{', '.join(map(str, a))}, and {b}"




def collatz_sequence(a, numOfDiv):
    if (a % 2) == 0:
        while a > 0:
            a = a // 2
            numOfDiv += 1
    else:
        while a > 0:
            a = (a * 3) + 1
            numOfDiv += 1

# filter through someone data best on thier charactristics
start = time.time()
df_to_match = pd.DataFrame(data=[['AfricanAmerican', 'Male', '[70-80)']],
                           columns=['race', 'gender', 'age'])
results = df.merge(df_to_match, on=['race', 'gender', 'age'])
count = len(results)
print('{0} records were found with matching features.'.format(count))
print('It took {0:.2f} seconds.'.format(time.time() - start))
#also allows you to time this stuff

#upload picture of dmg with change in colour map
base = r"C:\Users\omare\OneDrive\Documents\HDA\Clinical data managment\Week 6 privacy\CDM_Week6\practical_06"
pass_dicom = "image.dcm"
filename = pydicom.data.data_manager.get_files(base, pass_dicom)[0]
ds = pydicom.dcmread(filename)

plt.imshow(ds.pixel_array, cmap=plt.cm.bone)  # set the color map to bone
plt.show()
#meta data of pic
print(ds)
#odd numbers
import sys
def collatz (a):
    if a % 2 == 0:  # Even number
        result = a // 2
    elif a % 2 == 1:  # Odd number
        result = 3 * a + 1

    while result == 1:  # It would not print the number 1 without this loop
        print(result)
        sys.exit()  # So 1 is not printed forever.

    while result != 1:  # Goes through this loop until the condition in the previous one is True.
        print(result)
        number = result  # This makes it so collatz() is called with the number it has previously evaluated down to.
        return collatz(number)




