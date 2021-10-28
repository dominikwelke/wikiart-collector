# wikiart-collector
download pictures and metadata from wikiart.org based on freely chosen categories

this allows you to filter the huge [WikiArt database](https://www.wikiart.org) (thousands of paintings from hundreds of artists) for any wanted category from the wikiarts annotations (e.g. 'genre' or 'style') before downloading the actual pictures.

this code builds on the [wikiart](https://github.com/lucasdavid/wikiart) repository by [lucasdavid](https://github.com/lucasdavid). thanks for your previous work! 

**how to use it:**
1. download all metainfo from wikiart using lucasdavid's code (not included in this repository - this arguably takes forever) 
`python3 wikiart.py --datadir ./wikiart-saved/ fetch --only paintings`

2. build your custom subsets using my function
commandline: `python filter_wikiart_cmd.py --folder-in X --folder-out Y --field foo --target-value bar` 
script based: see `filter_wikiart_script_example.py`

3. use lucasdavid's code again to download the wanted jpegs
`python3 wikiart.py --datadir wikiart-filtered/field/target-value/ fetch`


**a typical use case:**
you want to filter the huge WikiArt database for a specific art style and only download these artworks. 
in this case you have to set the `field` parameter to  `field='style'`, and the `target_value` parameter to your wanted style (check out https://www.wikiart.org/en/paintings-by-style for options)
