#
# Author: Normand
#
import re

def replace_tag(value, tag):
    if "\\" in tag:
        tag = tag.replace("\\" , "")
    return float(replace_comma(value.replace(tag,"")))

def get_after_colon(value):
    return float(replace_comma(value.split(":")[-1]))

def replace_comma(value):
    # should only expect one comma obviously 
    comma = ","
    if "'" in value:
        comma = "'"
    if len(value.split(comma)[-1].rstrip()) == 3:
        return value.replace(comma, "")
    return value.replace(comma, ".")

# so many different tags man can people just learn to type the information normally
# finally get the complete list and filter out more information
# the all one is kind of bullshit but whatever
TAGS=["chf", "chf:", "euro", "fr\.", "\.--", "\.-","\.–","\.–","incl\.", "inkl\.",
      "pro", "per","miete","miete:","all","franc","beträgt"]

def get_rent(text, tags=TAGS):
    # replace the commas and ending zeros
    text = text.replace("`", ",").replace("’", ",").replace(".00", "")
    text = text.lower()
    prices = []
    for tag in tags:
        regex = r'\d+[\,\']?\d+{0}|{0}\d+[\,\']?\d+|\d+[\,\']?\d+ {0}|{0} \d+[\,\']?\d+'.format(tag)
        #print(regex)
        matches = re.findall(regex, text)
        if matches:
            prices.extend([replace_tag(x, tag) for x in matches])
    if len(prices) > 0:
        return max(prices)
    print("NO IDEA")
    return None

if __name__ == "__main__":
    text = "400 CHF"
    print(get_rent(text))