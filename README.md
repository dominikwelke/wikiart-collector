# wikiart-collector
download pictures and metadata from wikiart.org based on freely chosen categories

this allows you to filter the full wikiart database (all artists and their paintings) for a wanted category (e.g. 'genre' or 'style') from the wikiarts annotations.

it builds on the [wikiart](https://github.com/lucasdavid/wikiart) repository by @lucasdavid

how to use it:
- download all metainfo from wikiart using lucasdavid's code (takes forever) 
python3 wikiart.py --datadir ./wikiart-saved/ fetch --only paintings
- build custom subsets using my function
- use lucasdavid's code again to download the wanted jpegs
python3 wikiart.py --datadir wikiart-filtered/field/target-value/ fetch
