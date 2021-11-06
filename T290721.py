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
 
search_term = input("Type a term to be searched for in the appropriate capitalization: ")
 
wikidataEntries = search_entities(en_wiki_repo, search_term)
if wikidataEntries['search'] != []:
    results = wikidataEntries['search']
    numresults = len(results)
    returned_labels = []
    for i in range(0,numresults):
        returned_labels.append(results[i]['label'])
        
    if search_term not in returned_labels:
        print ("There isn't an exact match, but see below for closely related matches:")
        for i in range(0,numresults):
            qid = results[i]['id']
            label = results[i]['label']
            print (qid + " - " + label)
            
    else:    
        for i in range(0,numresults):
            if results[i]['label'] == search_term:
                qid = results[i]['id']
                label = results[i]['label']
                print ("Here is an exact match: " + qid + " - " + label)

else:
    print ("The inputted term does not have a QID in Wikidata.")