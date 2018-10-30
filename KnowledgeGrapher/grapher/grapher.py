"""
    **grapher.py**
    Populates the graph database with all the files generated by the importer.py module: 
    Ontologies, Databases and Experiments.
    The module loads all the entities and relationships defined in the importer files. It
    calls Cypher queries defined in the cypher.py module. Further, it generates an hdf object
    with the number of enities and relationships loaded for each Database, Ontology and Experiment.
    This module also generates a compressed backup file of all the loaded files.
    There are two types of updates: 
    - Full: all the entities and relationships in the graph database are populated
    - Partial: only the specified entities and relationships are loaded
    The compressed files for each type of update are named accordingly and saved in the archive/ folder
    in data/.
"""
import os
import sys
from datetime import datetime
from KnowledgeConnector import graph_controller
import ckg_config as graph_config
import grapher_config as config
import cypher as cy
from KnowledgeGrapher import utils
import logging
import logging.config

log_config = graph_config.log
logger = utils.setup_logging(log_config, key="grapher")

START_TIME = datetime.now()

def updateDB(driver, imports=None):
    """
    Populates the graph database with information for each Database, Ontology or Experiment
    specified in imports. If imports is not defined, the function populates the entire graph 
    database based on the graph variable defined in the grapher_config.py module.
    This function also updates the graph stats object with numbers from the loaded entities and
    relationships.
    Args:
        driver (py2neo driver): py2neo driver, which provides the 
                                connection to the neo4j graph database
        imports (list): A list of entities to be loaded into the graph
    """
    if imports is None:
        imports = config.graph
    
    for i in imports:
        logger.info("Loading {} into the database".format(i))
        try:
            importDir = os.path.join(os.getcwd(),config.databasesDirectory)
            #Get the cypher queries to build the graph
            #Ontologies
            if "ontologies" == i:
                entities = config.ontology_entities
                importDir = os.path.join(os.getcwd(), config.ontologiesDirectory)
                ontologyDataImportCode = cy.IMPORT_ONTOLOGY_DATA
                for entity in entities:
                    cypherCode = ontologyDataImportCode.replace("ENTITY", entity).replace("IMPORTDIR", importDir).split(';')[0:-1]
                    for statement in cypherCode:
                        #print(statement)
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Creating {}\n cypher query: {}".format(i, entity, statement))
            #Databases
            #Chromosomes
            elif "chromosomes" == i:
                chromosomeDataImportCode = cy.IMPORT_CHROMOSOME_DATA
                for statement in chromosomeDataImportCode.replace("IMPORTDIR", importDir).split(';')[0:-1]:
                    #print(statement+";")
                    graph_controller.sendQuery(driver, statement+';')
                    logger.info("{} - cypher query: {}".format(i, statement))
            #Genes
            elif "genes" == i:
                geneDataImportCode = cy.IMPORT_GENE_DATA
                for statement in geneDataImportCode.replace("IMPORTDIR", importDir).split(';')[0:-1]:
                    #print(statement+";")
                    graph_controller.sendQuery(driver, statement+';')
                    logger.info("{} - cypher query: {}".format(i, statement))
            #Transcripts
            elif "transcripts" == i:
                transcriptDataImportCode = cy.IMPORT_TRANSCRIPT_DATA
                for statement in transcriptDataImportCode.replace("IMPORTDIR", importDir).split(';')[0:-1]:
                    #print(statement+";")
                    graph_controller.sendQuery(driver, statement+';')
                    logger.info("{} - cypher query: {}".format(i, statement))
            #Proteins
            elif "proteins" == i:
                proteinDataImportCode = cy.IMPORT_PROTEIN_DATA
                for statement in proteinDataImportCode.replace("IMPORTDIR", importDir).split(';')[0:-1]:
                    #print(statement+";")
                    graph_controller.sendQuery(driver, statement+';')
                    logger.info("{} - cypher query: {}".format(i, statement))
            #Protein annotations
            elif "annotations" == i:
                proteinAnnotationsImportCode = cy.IMPORT_PROTEIN_ANNOTATIONS
                for statement in proteinAnnotationsImportCode.replace("IMPORTDIR", importDir).split(';')[0:-1]:
                    #print(statement+";")
                    graph_controller.sendQuery(driver, statement+';')
                    logger.info("{} - cypher query: {}".format(i, statement))
            #Protein complexes
            elif "complexes" == i:
                complexDataImportCode = cy.IMPORT_COMPLEXES
                for resource in config.complexes_resources:
                    for statement in complexDataImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
            #Modified proteins
            elif "modified_proteins" == i:
                modified_proteinsImportCode = cy.IMPORT_MODIFIED_PROTEINS
                for resource in config.modified_proteins_resources:
                    for statement in modified_proteinsImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
                modified_proteins_annotationsImportCode = cy.IMPORT_MODIFIED_PROTEIN_ANNOTATIONS
                for resource in config.modified_proteins_resources:
                    for statement in modified_proteins_annotationsImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
            #Pathology expression
            elif "pathology_expression" == i:
                pathology_expression_DataImportCode = cy.IMPORT_PATHOLOGY_EXPRESSION
                for resource in config.pathology_expression_resources:
                    for statement in pathology_expression_DataImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
            #PPIs
            elif "ppi" == i:
                ppiDataImportCode = cy.IMPORT_CURATED_PPI_DATA
                for resource in config.curated_PPI_resources:
                    for statement in ppiDataImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
                ppiDataImportCode = cy.IMPORT_COMPILED_PPI_DATA
                for resource in config.compiled_PPI_resources:
                    for statement in ppiDataImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
                ppiDataImportCode = cy.IMPORT_PPI_ACTION
                for resource in config.PPI_action_resources:
                    for statement in ppiDataImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
            #Diseases
            elif "diseases" == i:
                diseaseDataImportCode = cy.IMPORT_DISEASE_DATA
                for entity, resource in config.disease_resources:
                    for statement in diseaseDataImportCode.replace("IMPORTDIR", importDir).replace("ENTITY", entity).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\nEntity: {}\ncypher query: {}".format(i, resource, entity, statement))
            #Drugs  
            elif "drugs" == i:
                drugsDataImportCode = cy.IMPORT_DRUG_DATA
                for statement in drugsDataImportCode.replace("IMPORTDIR", importDir).split(';')[0:-1]:
                    #print(statement+";")
                    graph_controller.sendQuery(driver, statement+';')
                    logger.info("{} - cypher query: {}".format(i, statement))
                drugsDataImportCode = cy.IMPORT_CURATED_DRUG_DATA
                for resource in config.curated_drug_resources:
                    for statement in drugsDataImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
                drugsDataImportCode = cy.IMPORT_COMPILED_DRUG_DATA
                for resource in config.compiled_drug_resources:
                    for statement in drugsDataImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
                drugsDataImportCode = cy.IMPORT_DRUG_ACTS_ON
                for resource in config.drug_action_resources:
                    for statement in drugsDataImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
            #Side effects
            elif "side effects" == i:
                sideEffectsDataImportCode = cy.IMPORT_DRUG_SIDE_EFFECTS
                for resource in config.side_effects_resources:
                    for statement in sideEffectsDataImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
            #Pathway
            elif 'pathway' == i:
                pathwayImportCode = cy.IMPORT_PATHWAY_DATA
                for resource in config.pathway_resources:
                    for statement in pathwayImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+';')
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
            #Metabolite
            elif 'metabolite' == i:
                metaboliteImportCode = cy.IMPORT_METABOLITE_DATA
                for resource in config.metabolite_resources:
                    for statement in metaboliteImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+';')
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
            #Food
            elif 'food' == i:
                foodImportCode = cy.IMPORT_FOOD_DATA
                for resource in config.food_resources:
                    for statement in foodImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+';')
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
            #GWAS
            elif "gwas" == i:
                code = cy.IMPORT_GWAS
                for statement in code.replace("IMPORTDIR", importDir).split(';')[0:-1]:
                    #print(statement+';')
                    graph_controller.sendQuery(driver, statement+';')
                    logger.info("{} - cypher query: {}".format(i, statement))
            #Known variants
            elif "known_variants" == i:
                variantsImportCode = cy.IMPORT_KNOWN_VARIANT_DATA
                for statement in variantsImportCode.replace("IMPORTDIR", importDir).split(';')[0:-1]:
                    #print(statement+";")
                    graph_controller.sendQuery(driver, statement+';')
                    logger.info("{} - cypher query: {}".format(i, statement))
            #Clinically_relevant_variants
            elif "clinical variants" == i:
                variantsImportCode = cy.IMPORT_CLINICALLY_RELEVANT_VARIANT_DATA
                for resource in config.clinical_variant_resources:
                    for statement in variantsImportCode.replace("IMPORTDIR", importDir).replace("RESOURCE", resource.lower()).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Resource: {}\ncypher query: {}".format(i, resource, statement))
            #Internal
            elif "internal" == i:
                internalDataImportCode = cy.IMPORT_INTERNAL_DATA
                for (entity1, entity2) in config.internalEntities:
                    for statement in internalDataImportCode.replace("IMPORTDIR", importDir).replace("ENTITY1", entity1).replace("ENTITY2", entity2).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Entity1: {}, Entity2: {}\ncypher query: {}".format(i, entity1, entity2, statement))
            #Mentions
            elif "mentions" == i:
                publicationsImportCode = cy.CREATE_PUBLICATIONS
                for statement in publicationsImportCode.replace("IMPORTDIR", importDir).split(';')[0:-1]:
                    #print(statement+";")
                    graph_controller.sendQuery(driver, statement+';')
                    logger.info("{} - cypher query: {}".format(i, statement))

                mentionsImportCode = cy.IMPORT_MENTIONS
                for entity in config.mentionEntities:
                    for statement in mentionsImportCode.replace("IMPORTDIR", importDir).replace("ENTITY", entity).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - cypher query: {}".format(i, statement))
             #Published in
            elif "published" == i:
                publicationImportCode = cy.IMPORT_PUBLISHED_IN
                for entity in config.publicationEntities:
                    for statement in publicationImportCode.replace("IMPORTDIR", importDir).replace("ENTITY", entity).split(';')[0:-1]:
                        #print(statement+";")
                        graph_controller.sendQuery(driver, statement+';')
                        logger.info("{} - Entity: {}\ncypher query: {}".format(i, entity, statement))
            #Projects
            elif "project" == i:
                importDir = os.path.join(os.getcwd(),config.experimentsDirectory)
                projects = utils.listDirectoryFolders(importDir)
                projectCode = cy.IMPORT_PROJECT
                for project in projects:
                    projectDir = os.path.join(importDir, project)
                    for code in projectCode:
                        for statement in code.replace("IMPORTDIR", projectDir).replace('PROJECTID', project).split(';')[0:-1]:
                            #print(statement+';')
                            graph_controller.sendQuery(driver, statement+';')
                            logger.info("{} - Project: {}\nCode: {}\ncypher query: {}".format(i, project, code, statement))
            #Datasets
            elif "experiment" == i:
                importDir = os.path.join(os.getcwd(),config.experimentsDirectory)
                datasetsCode = cy.IMPORT_DATASETS
                projects = utils.listDirectoryFolders(importDir)
                for project in projects:
                    projectDir = os.path.join(importDir, project)
                    datasetTypes = utils.listDirectoryFolders(projectDir)
                    for dtype in datasetTypes:
                        datasetDir = os.path.join(projectDir, dtype)
                        code = datasetsCode[dtype]
                        for statement in code.replace("IMPORTDIR", datasetDir).replace('PROJECTID', project).split(';')[0:-1]:
                            #print(statement+';')
                            graph_controller.sendQuery(driver, statement+';')
                            logger.info("{} - Project: {}\nData type: {}\ncypher query: {}".format(i, project, dtype, statement))
        except Exception as err:
            logger.error("{} > {}.\n Query:{}".format(i, err, statement))

def fullUpdate():
    """
    Main method that controls the population of the graph database. Firstly, it gets a connection
    to the database (driver) and then initiates the update of the entire database getting
    all the graph entities to update from configuration. Once the graph database has been 
    populated, the imports folder in data/ is compressed and archived in the archive/ folder
    so that a backup of the imports files is kept (full).
    """
    imports = config.graph
    driver = graph_controller.getGraphDatabaseConnectionConfiguration()
    logger.info("Full update of the database - Updating: {}".format(",".join(imports)))
    updateDB(driver, imports)
    logger.info("Full update of the database - Update took: {}".format(datetime.now() - START_TIME))
    logger.info("Full update of the database - Archiving imports folder")
    archiveImportDirectory(archive_type="full")
    logger.info("Full update of the database - Archiving took: {}".format(datetime.now() - START_TIME))

def partialUpdate(imports):
    """
    Method that controls the update of the graph database with the specified entities and 
    relationships. Firstly, it gets a connection
    to the database (driver) and then initiates the update of the specified graph entities. 
    Once the graph database has been populated, the data files uploaded to the graph are compressed 
    and archived in the archive/ folder (partial).
    Args:
        imports (list): list of entities to update
    """
    driver = graph_controller.getGraphDatabaseConnectionConfiguration()
    logger.info("Partial update of the database - Updating: {}".format(",".join(imports)))
    updateDB(driver, imports)
    logger.info("Partial update of the database - Update took: {}".format(datetime.now() - START_TIME))
    logger.info("Partial update of the database - Archiving imports folder")
    archiveImportDirectory(archive_type="partial")
    logger.info("Partial update of the database - Archiving {} took: {}".format(",".join(imports), datetime.now() - START_TIME))
    
def archiveImportDirectory(archive_type="full"):
    """
    This function creates the compressed backup imports folder with either the whole folder
    (full update) or with only the files uploaded (partial update). The folder or files are
    compressed into a gzipped tarball file and stored in the archive/ folder defined in the 
    configuration.
    Args:
        archive_type (string): whether it is a full update or a partial update
    """
    dest_folder = config.archiveDirectory
    utils.checkDirectory(dest_folder)
    folder_to_backup = config.importDirectory
    date, time = utils.getCurrentTime()
    file_name = "{}_{}_{}".format(archive_type, date.replace('-', ''), time.replace(':', ''))
    logger.info("Archiving {} to file: {}".format(folder_to_backup, file_name))
    utils.compress_directory(folder_to_backup, dest_folder, file_name)
    logger.info("New backup created: {}".format(file_name))

if __name__ == "__main__":
    fullUpdate()
    #partialUpdate(datasets=["project","experiment"])

