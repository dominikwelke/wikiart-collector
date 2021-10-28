from filter_wikiart.filter_wikiart import filter_wikiart


# call function to collect the wanted info
# get genre and targets from https://www.wikiart.org/en/paintings-by-genre
filter_wikiart(folder_in='wikiart-saved', folder_out='wikiart-filtered/genres/abstract', field='genre', target_value='abstract')
filter_wikiart(folder_in='wikiart-saved', folder_out='wikiart-filtered/genres/allegory', field='genre', target_value='allegorical painting')
filter_wikiart(folder_in='wikiart-saved', folder_out='wikiart-filtered/genres/myths', field='genre', target_value='mythological painting')
filter_wikiart(folder_in='wikiart-saved', folder_out='wikiart-filtered/genres/myths', field='genre', target_value='history painting')
filter_wikiart(folder_in='wikiart-saved', folder_out='wikiart-filtered/genres/myths', field='genre', target_value='symbolic painting')


# get style and targets from https://www.wikiart.org/en/paintings-by-style

filter_wikiart(folder_in='wikiart-saved', folder_out='wikiart-filtered/styles/surrealism', field='style', target_value='Surrealism')
filter_wikiart(folder_in='wikiart-saved', folder_out='wikiart-filtered/styles/symbolism', field='style', target_value='Symbolism')
filter_wikiart(folder_in='wikiart-saved', folder_out='wikiart-filtered/styles/cubism', field='style', target_value='Cubism')
filter_wikiart(folder_in='wikiart-saved', folder_out='wikiart-filtered/styles/abstract_expressionism', field='style', target_value='Abstract Expressionism')
