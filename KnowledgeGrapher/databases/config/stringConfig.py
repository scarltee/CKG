###### STRING database #######
STRING_cutoff = 0.4

STRING_mapping_url = "https://stringdb-static.org/download/protein.aliases.v10.5/9606.protein.aliases.v10.5.txt.gz"
STITCH_mapping_url = "http://stitch.embl.de/download/chemical.aliases.v5.0.tsv.gz"

STITCH_url = "http://stitch.embl.de/download/protein_chemical.links.detailed.v5.0/9606.protein_chemical.links.detailed.v5.0.tsv.gz"
STRING_url = "https://stringdb-static.org/download/protein.links.detailed.v10.5/9606.protein.links.detailed.v10.5.txt.gz"

STRING_actions_url = "https://stringdb-static.org/download/protein.actions.v10.5/9606.protein.actions.v10.5.txt.gz"
STITCH_actions_url = "http://stitch.embl.de/download/actions.v5.0/9606.actions.v5.0.tsv.gz"

header = ['START_ID', 'END_ID','TYPE', 'interaction_type', 'source', 'evidences','scores', 'score']
header_actions = ['START_ID', 'END_ID','TYPE', 'action', 'score', 'source']
