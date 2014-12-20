# Documentatie

## Datastructuren

Er zijn twee grote types van datastructuren (en nog een kleine derde categorie),
zij die zichzelf gesorteerd houden, zij die zichzelf niet gesorteerd houden, en zij waarbij men niet kan
spreken van een sortering.

### Gesorteerde datastructuren

Hieronder valt het grote overschot van de datastructuren: Alle bomen, hashmap en Sorted Linked Chain.

Datastructuren die zichzelf gesorteerd houden doen dat maar op één attribuut, en dat attribuut moet
natuurlijk uniek zijn, bijvoorbeeld "ID".

Een uitzondering is de **hashmap**. De hashmap heeft wel een functie .inorder(), maar deze zal de 
hashmap niet in volgorde van ID doorlopen. De hashmap slaagt namelijk de volgorde van de items niet op,
maar heeft een hashfunctie die makelijk iets kan vinden in een array. De tests in test.py testen hierop,
maar zullen beweren dat er een fout is gebeurd. Dit is niet het geval.

Alle andere gesorteerde datastructuren zullen een functie .inorder() hebben die effectief alle elementen
yield in volgorde van de gekozen (unieke) zoeksleutel.

Als we .sort(attr) aanroepen op een gesorteerde datastructuur, zijn er twee mogelijkheden:
  - Als het gekozen attribuut hetzelfde is als de zoeksleutel, kunnen we gewoon yielden van self.inorder()
    Dit wil zeggen dat er niet gesorteerd moet worden, de datastructuur bevat als het ware al de nodige
    informatie over de volgorde.
  - Indien we niet zomaar de volgorde bepaald door de gekozen attribuut kennen, maken we eerst een lijst
    aan van de huidige elementen, en we roepen een sorteringsfunctie aan (standaard bubblesort, maar kan
    gespecifieerd worden als tweede parameter). We yielden dan alle elementen in de gesorteerde lijst.

Éen uitzondering: de hashmap heeft zoals gezegd geen informatie over de volgorde, en zal altijd de twee
optie nemen.

Een contract dat voor een gesorteerde datastructuur geldt, zal er ongeveer zo uit zien:

    +__init__(attribute)
    // Creëert een datatstructuur gesorteerd op attribute.

    +attribute(): string
    // Geeft de attribuut waarop gesorteerd wordt. (string)

    +retrieve(key: KeyType): ElementType {query}
    // Als er een element met element.__dict__[self.attribute()] == key in de datastructuur zit, geeft
    // dat element terug. Indien niet, geeft None terug.

    +delete(key: KeyType): Bool
    // Geeft terug of het deleten gelukt is. Geeft ook False terug als het gezochte element niet 
    // in de datastructuur zit.

    +isEmpty(): Bool

    +sort(attribute: string): generator {query}
    // Geeft een generator terug, in volgorde van de attribuut aangegeven.

    +inorder(): generator
    // Doorloopt de structuur in volgorde.

In de bovenstaande functies moet het volgende gelden: 
    KeyType == type(element.__dict__[attribute]

Bovendien moet element van het type ElementType zijn.

### Ongesorteerde datastructuren

Ongesorteerde datastructuren zijn de Unsorted Linked Chain en de Unsorted Array.
De verschillen met de gesorteerde datastructuren zijn als volgt:

.sort(attribute) zal sorteren op het gekozen attribuut en een bijhorende generator returnen, maar zal ook
de interne volgorde veranderen!

    +__init__(attribute)
    // Creëert een datatstructuur waarbij gezocht wordt op attribute.

    +attribute(): string
    // Geeft de attribuut waarop gezocht wordt. (string)

    +retrieve(key: KeyType): ElementType {query}
    // Als er een element met element.__dict__[self.attribute()] == key in de datastructuur zit, geeft
    // dat element terug. Indien niet, geeft None terug.

    +delete(key: KeyType): Bool
    // Geeft terug of het deleten gelukt is. Geeft ook False terug als het gezochte element niet 
    // in de datastructuur zit.

    +isEmpty(): Bool

    +sort(attribute: string): generator
    // Geeft een generator terug, in volgorde van de attribuut aangegeven.
    // geen query!

    +inorder(): generator
    // Doorloopt de structuur in de huidige volgorde. Deze volgorde kan bijvoorbeeld de volgorde zijn van
    // toevoegen, maar ook de volgorde die door een aanroep van .sort() werd gedefinieerd.

Een speciaal geval is de USLinkedChain. Als we geen functie specifiëeren om te gebruiken als
sorteringsalgoritme, zal deze standaard niet de 'gewone' bubblesort gebruiken maar een speciale versie van
bubblesort, specifiek gemaakt om gebruikt te maken van het gelinkte karakter van de USLinkedChain.

### Geen sortering: Stack en Queue

Stack en Queue zijn niet gesorteerd, en man kan ook geen element retrieven. De contracten hiervoor zijn
verschillend en staan bij de andere contracten. Ookal staan stack.py en queue.py beide in het mapje
'structures', ze zijn geen geldige tabelimplementatie.

## Datastructuren gebruiken

Men kan de datastructuren als volgt gebruiken:
  - Voor een tabelimplementatie, import datastruct, en roep createDataStructure() aan, bv. als volgt:
    hashmap = createDataStructure("Hashmap", "ID")
    hashmap zal nu een Hashmap zijn, waarbij men kan retrieven en deleten gebaseerd op de ID.
  - Voor de Stack en Queue:
    from structures.stack import Stack
    from structures.queue import Queue
