# Research on Ontology Matching

## Ontology Matching Techniques
1. Element-level ontology matching
    - String-based - matching names or descriptions of entities
    - Linguistic-based - use NLP, lexicons, or domain specific thesauri to match words based on linguistic relations (homonymy, synonymy, partonymy, etc.), or exploiting morphological properties
    - Constrained-based - take into account internal constraints applied to the definitions of entities, as e.g. types, cardinality of properties, etc.
    - Extensional-based - use individual representation of classes, i.e. classes are considered similar if they share many instances
2. Structure-level ontology matching
    - Graph-based - consider ontologies as labeled graphs, assumption: if nodes are similar, then also their neighbors must be similar
    - Taxonomy-based - like graph-based algorithms, but consider only specialization/generalization relation
    - Method-based - take into account semantic interpretation of the ontologies, assumption: if two entities are the same, then they share the same interpretation
    - Data analysis and statistics - take a large sample, try to find regularities, discrepancies, allows grouping or determining distance metrics, etc.
