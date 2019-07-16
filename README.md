##instructions

-The code simply needs an input from the user (CIK or ticker)

-tsv file saved under the name: Lior_Beyderman.tsv

##features/comments

-To search for historical docs the following code will apply instead of line 12:

    for document in soup.findAll('a', {'id':'documentsbutton'}):
        print (document.get('href'))

-Instead of taking the direct approach of manually writing headers for each mutual fund (since the format of the 13F reports differs),
I decided to find where text is within tags, and then in reverse find the texts'(child) parent, whereby the child & the parent become key/value pairs in a dictionary.

-The dictionary on line 35 is flipped so that the keys are unique


"# Index-fund-financial-info-scraper" 
