from wikiart_filter.wikiart_filter import wikiart_filter


# call function to collect the wanted info
# get genre and targets from https://www.wikiart.org/en/paintings-by-genre
wikiart_filter(folder_in='wikiart-saved', folder_out='wikiart-filtered/genres/abstract', field='genre', target_value='abstract')
wikiart_filter(folder_in='wikiart-saved', folder_out='wikiart-filtered/genres/allegory', field='genre', target_value='allegorical painting')
wikiart_filter(folder_in='wikiart-saved', folder_out='wikiart-filtered/genres/myths', field='genre', target_value='mythological painting')
wikiart_filter(folder_in='wikiart-saved', folder_out='wikiart-filtered/genres/myths', field='genre', target_value='history painting')
wikiart_filter(folder_in='wikiart-saved', folder_out='wikiart-filtered/genres/myths', field='genre', target_value='symbolic painting')


# get style and targets from https://www.wikiart.org/en/paintings-by-style

wikiart_filter(folder_in='wikiart-saved', folder_out='wikiart-filtered/styles/surrealism', field='style', target_value='Surrealism')
wikiart_filter(folder_in='wikiart-saved', folder_out='wikiart-filtered/styles/symbolism', field='style', target_value='Symbolism')
wikiart_filter(folder_in='wikiart-saved', folder_out='wikiart-filtered/styles/cubism', field='style', target_value='Cubism')
wikiart_filter(folder_in='wikiart-saved', folder_out='wikiart-filtered/styles/abstract_expressionism', field='style', target_value='Abstract Expressionism')
