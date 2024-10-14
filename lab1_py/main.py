from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, XSD, RDFS

# Ініціалізація графа
g = Graph()

# Визначаємо базовий простір імен
EX = Namespace("http://example.org/")
SCHEMA = Namespace("http://schema.org/")
g.bind("foaf", FOAF)
g.bind("xsd", XSD)
g.bind("schema", SCHEMA)

# Створюємо URI для Кейда та Емми
cade = URIRef(EX + "Cade")
emma = URIRef(EX + "Emma")

# Додаємо інформацію про Кейда
g.add((cade, RDF.type, FOAF.Person))
g.add((cade, FOAF.name, Literal("Cade")))
g.add((cade, FOAF.based_near, Literal("1516 Henry Street, Berkeley, CA 94709, USA")))
g.add((cade, FOAF.knows, emma))
g.add((cade, FOAF.topic_interest, Literal("Birds")))
g.add((cade, FOAF.topic_interest, Literal("Ecology")))
g.add((cade, FOAF.topic_interest, Literal("Environment")))
g.add((cade, FOAF.topic_interest, Literal("Photography")))
g.add((cade, FOAF.topic_interest, Literal("Travel")))
g.add((cade, FOAF.pastProject, Literal("Canada")))
g.add((cade, FOAF.pastProject, Literal("France")))
g.add((cade, SCHEMA.educationalCredentialAwarded, Literal("Bachelor in Biology from UC Berkeley (2011)", datatype=XSD.string)))

# Додаємо інформацію про Емму
g.add((emma, RDF.type, FOAF.Person))
g.add((emma, FOAF.name, Literal("Emma")))
g.add((emma, FOAF.based_near, Literal("Carrer de la Guardia Civil 20, 46020 Valencia, Spain")))
g.add((emma, FOAF.topic_interest, Literal("Waste Management")))
g.add((emma, FOAF.topic_interest, Literal("Toxic Waste")))
g.add((emma, FOAF.topic_interest, Literal("Air Pollution")))
g.add((emma, FOAF.topic_interest, Literal("Cycling")))
g.add((emma, FOAF.topic_interest, Literal("Music")))
g.add((emma, FOAF.topic_interest, Literal("Travel")))
g.add((emma, FOAF.pastProject, Literal("Portugal")))
g.add((emma, FOAF.pastProject, Literal("Italy")))
g.add((emma, FOAF.pastProject, Literal("France")))
g.add((emma, FOAF.pastProject, Literal("Germany")))
g.add((emma, FOAF.pastProject, Literal("Denmark")))
g.add((emma, FOAF.pastProject, Literal("Sweden")))
g.add((emma, FOAF.age, Literal(36, datatype=XSD.integer)))
g.add((emma, SCHEMA.educationalCredentialAwarded, Literal("Master in Chemistry from University of Valencia (2015)", datatype=XSD.string)))

# Вони зустрілися в Парижі в серпні 2014
meeting_place = URIRef(EX + "Meeting_Paris_2014")
g.add((cade, FOAF.knows, emma))
g.add((meeting_place, RDFS.label, Literal("Cade met Emma in Paris in August 2014")))
g.add((cade, FOAF.based_near, Literal("Germany")))  # Додаємо, що Кейд також відвідував Німеччину

# Серіалізація у формат Turtle
turtle_data = g.serialize(format="turtle")

# Записуємо граф у файл
with open("semantic_web_graph.ttl", "w") as f:
    f.write(turtle_data)

# Виведення всіх трійок
print("All triples in the graph:")
for s, p, o in g:
    print(s, p, o)

# Виведення трійок, що стосуються лише Емми
print("\nTriples related to Emma:")
for s, p, o in g.triples((emma, None, None)):
    print(s, p, o)

# Виведення трійок, що містять імена людей
print("\nTriples that contain person names:")
for s, p, o in g.triples((None, FOAF.name, None)):
    print(s, p, o)
