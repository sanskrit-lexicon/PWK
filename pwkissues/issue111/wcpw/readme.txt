04-18-2024

------------------------------
Link from Thomas email
https://powo.science.kew.org/
-----
Royal Botanic Gardens KEW | Plants of the World Online

Govaerts R (ed.). 2023. WCVP:
World Checklist of Vascular Plants.
Facilitated by the Royal Botanic Gardens, Kew.
[WWW document] URL https://doi.org/10.34885/jdh2-dr22 [accessed 28 September 2023].
-----------------------------------------------
Download of DATA: wcvp.zip
https://sftp.kew.org/pub/data-repositories/WCVP/

 unzip -l wcvp.zip
Archive:  wcvp.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
    17825  2023-10-04 10:06   README_WCVP.xlsx
139048722  2023-09-28 11:46   wcvp_distribution.csv
293398005  2023-09-28 12:20   wcvp_names.csv
---------                     -------
432464552                     3 files

-----------------------------------------------
Download of DATA: wcvp_dwca.zip
https://sftp.kew.org/pub/data-repositories/WCVP/

 unzip -l wcvp_dwca.zip
Archive:  wcvp_dwca.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
    53945  2023-10-04 10:16   eml.xml
     3190  2022-12-14 13:19   meta.xml
 63331284  2023-09-28 13:51   wcvp_distribution.csv
  1686591  2023-09-28 13:54   wcvp_replacementNames.csv
496724435  2023-09-28 13:58   wcvp_taxon.csv
---------                     -------
561799445                     5 files
===============================================

unzip -d wcvp1 wcvp.zip
unzip -d wcvp2 wcvp_dwca.zip

  wcvp2/wcvp_taxon.csv  Sci
------------------------------

********************************************************
wcp1/wcvp_names.csv  work
********************************************************
title line
plant_name_id|ipni_id|taxon_rank|taxon_status|family|genus_hybrid|genus|species_hybrid|species|infraspecific_rank|infraspecies|parenthetical_author|primary_author|publication_author|place_of_publication|volume_and_page|first_published|nomenclatural_remarks|geographic_area|lifeform_description|climate_description|taxon_name|taxon_authors|accepted_plant_name_id|basionym_plant_name_id|replaced_synonym_author|homotypic_synonym|parent_plant_name_id|powo_id|hybrid_formula|reviewed
x
plant_name_id
ipni_id
taxon_rank
taxon_status
family
genus_hybrid
genus
species_hybrid
species
infraspecific_rank
infraspecies
parenthetical_author
primary_author
publication_author
place_of_publication
volume_and_page
first_published
nomenclatural_remarks
geographic_area
lifeform_description
climate_description
taxon_name
taxon_authors
accepted_plant_name_id
basionym_plant_name_id
replaced_synonym_author
homotypic_synonym
parent_plant_name_id
powo_id
hybrid_formula
reviewed
--------------------------------------------------
README_WCVP/README.html
An html version of README_WCVP.xlsx
documentation of the WCVP Dataset
(opened README_WCVP.xlsx in Google Sheets
 Downloaded as HTML
)
--------------------------------------------------
wc -l wcvp1/wcvp_names.csv
1422869 wcvp1/wcvp_names.csv

# use a csv.reader
python wcvp_names_read.py 0 wcvp1/wcvp_names.csv temp.txt

 python wcvp_names_read.py 0 wcvp1/wcvp_names.csv temp.txt
['plant_name_id', 'ipni_id', 'taxon_rank', 'taxon_status', 'family', 'genus_hybr
id', 'genus', 'species_hybrid', 'species', 'infraspecific_rank', 'infraspecies',
 'parenthetical_author', 'primary_author', 'publication_author', 'place_of_publi
cation', 'volume_and_page', 'first_published', 'nomenclatural_remarks', 'geograp
hic_area', 'lifeform_description', 'climate_description', 'taxon_name', 'taxon_a
uthors', 'accepted_plant_name_id', 'basionym_plant_name_id', 'replaced_synonym_a
uthor', 'homotypic_synonym', 'parent_plant_name_id', 'powo_id', 'hybrid_formula'
, 'reviewed']
first row has 31 columns
1422869 rows read from wcvp1/wcvp_names.csv

# use a csv.DictReader
python wcvp_names_read.py 1 wcvp1/wcvp_names.csv temp.txt

{'plant_name_id': '411059', 'ipni_id': '400227-1', 'taxon_rank': 'Species', 'tax
on_status': 'Accepted', 'family': 'Poaceae', 'genus_hybrid': '', 'genus': 'Elymu
s', 'species_hybrid': '', 'species': 'czimganicus', 'infraspecific_rank': '', 'i
nfraspecies': '', 'parenthetical_author': 'Drobow', 'primary_author': 'Tzvelev',
 'publication_author': '', 'place_of_publication': 'Trudy Bot. Inst. Akad. Nauk
S.S.S.R., Rast. Tsentral. Azii', 'volume_and_page': ' 4: 22', 'first_published':
 '(1968)', 'nomenclatural_remarks': '', 'geographic_area': 'C. Asia to W. Himala
ya', 'lifeform_description': 'perennial', 'climate_description': 'temperate', 't
axon_name': 'Elymus czimganicus', 'taxon_authors': '(Drobow) Tzvelev', 'accepted
_plant_name_id': '411059', 'basionym_plant_name_id': '388366', 'replaced_synonym
_author': '', 'homotypic_synonym': '', 'parent_plant_name_id': '451462', 'powo_i
d': '400227-1', 'hybrid_formula': '', 'reviewed': 'Y'}
first row has 31 columns
1422868 rows read from wcvp1/wcvp_names.csv

Notes:
 1 less row with DictReader
 taxon_name  may be comparable to PW
 taxon_authors may also be of use

# use a csv.DictReader
# match genus = xxx, species = yyy
python wcvp_names_read.py 2 wcvp1/wcvp_names.csv temp.txt

---------------------------------------------------------
'genus','species'
python wcvp_gs.py  wcvp1/wcvp_names.csv temp_wcvp_gs.txt
1021628 distinct values of ['genus', 'species']
1021628 written to temp_wcvp_gs.txt

---------------------------------------------------------
'primary_author'
Use 'taxon_authors' field. Each value appears to be

python wcvp_auth.py primary_author wcvp1/wcvp_names.csv temp_wcvp_primary_auth.txt
75753 distinct values of ['primary_author']
75753 written to temp_wcvp_primary_auth.txt

python wcvp_auth.py taxon_authors wcvp1/wcvp_names.csv temp_wcvp_taxon_auth.txt
235926 distinct values of ['taxon_authors']
235926 written to temp_wcvp_taxon_auth.txt
