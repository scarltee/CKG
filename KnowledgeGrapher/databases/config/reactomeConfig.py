###### Reactome Database #######
reactome_urls = {"pathway":"https://reactome.org/download/current/ReactomePathways.txt",
                "hierarchy":"https://reactome.org/download/current/ReactomePathwaysRelation.txt",
                "protein":"https://reactome.org/download/current/UniProt2Reactome_PE_Pathway.txt",
                "metabolite":"https://reactome.org/download/current/ChEBI2Reactome_PE_Pathway.txt",
                "drug":"https://reactome.org/download/current/ChEBI2Reactome_PE_Pathway.txt"
                }
pathway_header = ['ID', ':LABEL', 'name', 'description', 'type', 'linkout', 'source']
relationships_header = {"pathway":['START_ID', 'END_ID','TYPE', 'source'],
                        "protein":['START_ID', 'END_ID','TYPE', 'evidence', 'organism', 'cellular_component', 'source'],
                        "metabolite":['START_ID', 'END_ID','TYPE', 'evidence', 'organism', 'cellular_component', 'source'],
                        "drug":['START_ID', 'END_ID','TYPE', 'evidence', 'organism', 'cellular_component', 'source']
                        }
linkout_url = "https://reactome.org/PathwayBrowser/#/PATHWAY"
organisms = {"Homo sapiens":9606}

