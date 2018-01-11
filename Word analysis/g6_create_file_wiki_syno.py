# Group 6 LAFONT Nicolas, QUESNOT Sandy, VAYSSE Robin
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a list of words with wikipedia or a synonym.
"""

import g6_wordnet_synonym_V1_4 as syno
import wiki_search_v1_2 as wiki
import json

if __name__ == '__main__':
    path = '/home/Robin/Documents/M1/Inter_Promo/target_press_article/artfusc1002018-01-08_filtering.json'
    fic = open(path)
    text = json.load(fic)
    content = text['content']

    liste_result = []
    for key in content.keys():
        if key != 'words' and key != 'list_lemma':
            result = {}
            result['position'] = key
            result['title'] = content[key]['title']
            result['word'] = content[key]['word']
            result['type_entity'] = content[key]['type_entity']
            result['pos_tag'] = content[key]['pos_tag']
            result['id_article'] = '-4217'

            if result['type_entity'] != 'Null':
                result['file_wiki'] = wiki.wikipedia_search(result['word'])
                result['synonym'] = ''
            else:
                result['file_wiki'] = ''
                result['synonym'] = syno.give_the_first_synonym(result['word'])

            liste_result.append(result)
