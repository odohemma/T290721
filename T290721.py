# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:35:53 2021

@author: USER
"""

import pywikibot
from pywikibot.data import api

# Connect to english wiki
en_wiki = pywikibot.Site('en', 'wikipedia')

# Then connect to wikidata
en_wiki_repo = en_wiki.data_repository()


def search_entities(site, itemtitle):
     params = { 'action' :'wbsearchentities', 
                'format' : 'json',
                'language' : 'en',
                'type' : 'item',
                'search': itemtitle}
     request = api.Request(site=site, parameters=params)
     return request.submit()
 
search_term = input("Type a term to be searched for: ")
 
wikidataEntries = search_entities(en_wiki_repo, search_term)
if wikidataEntries['search'] != []:
    results = wikidataEntries['search']
    numresults = len(results)
    for i in range(0,numresults):
        qid = results[i]['id']
        label = results[i]['label']
        print (qid + " - " + label)
else:
    print ("The inputted term does not have a QID in Wikidata.")