import re
import json
from collections import defaultdict
from docx import Document

head_line_of_entry = r"^[mMnNptksSh’wyaioáíóI.]+\s*(nan|nin|nar|nir|vii|vai|vti|vta|und|adt|med|fin|suf|vrt|dem|pro)(/(nan|nin|nar|nir|vii|vai|vti|vta|und|adt|med|fin|suf|vrt|dem|pro))?;"
top_of_page = r"^[mMnNptksSh’wyaioáíóI]+\s*[mMnNptksSh’wyaioáíóI]+$"

def create_bl2en_dictionary():

    # open word file
    doc = Document('Blackfoot_Dictionary.docx')
    paragraphs = doc.paragraphs

    # separate word file
    bl2en = paragraphs[:7700]
    en2bl = paragraphs[7700:]

    bl2en_processed_dict = dict()   # {bl_word : (pos, definition)}

    i = 0
    while i < len(bl2en):
        line = bl2en[i].text

        if re.match(head_line_of_entry, line): # if head line of entry

            bl_word = line.split()[0]
            pos = line.split()[1][:-1] # exclude ;
            definition = " ".join(line.split()[2:])  # definition on first (and possibly only) line

            # look at following lines to check if they're a continuation of definition
            j = i + 1
            while (not re.match(head_line_of_entry, bl2en[j].text) # next line not new entry
               and not re.match(top_of_page, bl2en[j].text)        # next line not header of page
               and bl2en[j].text.strip()):                         # next line not empty
                definition = definition + " " + bl2en[j].text
                j += 1

            bl2en_processed_dict[bl_word] = (pos, definition) # create entry

            i = j

        else: # if non-head line that's doesn't belong to previous entry
            i += 1

    return bl2en_processed_dict





def output_lexicon_files():

    with open("blackfoot_dict.json","r") as f:
        dictionary = json.load(f)

    lexicon_by_pos = defaultdict(list)

    for entry in dictionary.keys():
        pos = dictionary[entry][0].split("/")
        lexicon_by_pos[pos[0]].append(entry)
        if len(pos) == 2:
            lexicon_by_pos[pos[1]].append(entry)

    for pos in lexicon_by_pos.keys():
        with open("./blackfoot_lexicon/"+pos, "w") as f:
            for word in lexicon_by_pos[pos]:
                f.write(word)
                f.write("\n")

    #print(lexicon_by_pos.keys())

if __name__ == '__main__':

    #dictionary = create_bl2en_dictionary() # first two entries are edge cases

    #with open("blackfoot_dict.json","w") as f:
    #    json.dump(dictionary,f,ensure_ascii=False)

    output_lexicon_files()