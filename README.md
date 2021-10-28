# wikiart-collector
download pictures and metadata from wikiart.org based on freely chosen categories

this repository allows you to filter the huge [WikiArt database](https://www.wikiart.org) (thousands of paintings from hundreds of artists) for any wanted category from the wikiarts annotations (e.g. 'genre' or 'style') before downloading the actual pictures.

this code builds on the [wikiart](https://github.com/lucasdavid/wikiart) repository by [lucasdavid](https://github.com/lucasdavid). thanks for your work!  

all the actual interaction with WikiArt's API happens there, my code is just a fancy json manipulator.  
please be sure to check and agree with [WikiArt's terms of use](https://www.wikiart.org/en/terms-of-use) before using any of the retrieved content ;)


**how to use it:**
1. download all metainfo from wikiart using lucasdavid's code (not included in this repository; this arguably takes forever)  
commandline: `python3 wikiart.py --datadir X fetch --only paintings`

2. build your custom subsets using my function  
commandline: `python filter_wikiart_cmd.py --folder-in X --folder-out Y --field foo --target-value bar`  
script based: see `filter_wikiart_script_example.py`

3. use lucasdavid's code again to download the wanted jpegs  
commandline: `python3 wikiart.py --datadir wikiart-filtered/field/target-value/ fetch`  
(*attention!* be sure to doublecheck your paths. lucasdavid's code will simply download all of WikiArt if you call the above line pointing to an empty or nonexisting `--datadir`)


**a typical use case:**

you want to filter the WikiArt database for a specific art style and only download these artworks. 
in this case you have to set the `field` parameter to  `field='style'`, and the `target_value` parameter to your wanted style (check out https://www.wikiart.org/en/paintings-by-style for options)


