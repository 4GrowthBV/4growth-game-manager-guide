# Speltype-advies — heuristiek (v2)

De tool ondersteunt zes speltype-families. Adviseer op basis van leerdoel en content; de gebruiker beslist. Het speltype ligt vast in het aangeleverde game-bestand — de tool verandert de spelstructuur nooit. Wijkt je advies af van het aangeleverde bestand, geef twee routes: doorgaan met het huidige speltype, of het passende template-game-bestand (laten) exporteren.

## Ondersteund

### Waar / Niet waar (tf)
Stelling naar "WAAR" of "NIET WAAR" slepen (labels aanpasbaar, bv. FEIT/FABEL).
**Kies bij:** misvattingen ontkrachten; binaire regels (mag wel/niet); laagdrempelige instap. **Let op:** nuance ("soms") past er niet in.

### Meerkeuze 3 of 4 opties (mc3/mc4)
Vraag of mini-casus, kies A/B/C(/D).
**Kies bij:** handelingsvragen ("wat doe je?") met plausibele alternatieven; feitenkennis met verwarringsgevaar. MC4 alleen als er 3 échte distractors bestaan; bij twijfel MC3.
**Combinatie-advies bij "kennen + doen"-leerdoelen:** per deelonderwerp één kennisvraag + één casusvraag.

### Sorteren / classificeren (pum en sort)
- **Puzzle Motion (pum):** items bewegen het scherm binnen; de speler sleept ze onder tijdsdruk naar het juiste vak. Energiek, hoge activatie.
- **Sort-to-target (sort):** rustiger sorteren van items naar categorieën.
**Kies bij:** leerdoelen rond indelen in categorieën, klassen of risiconiveaus (triage, sorteerregels, begrippen bij definities). Vereist 2-6 heldere, elkaar uitsluitende categorieën. De categorieën (vakken) liggen vast in het game-bestand: aantal en visuals zijn structuur; alleen de labels en de items zijn content.
**Let op (pum):** casusteksten kort houden — de speler leest terwijl items bewegen.

### Zoekplaat met vragen — Locate & Answer (loa)
De speler zoekt spots op een afbeelding, zoomt in en beantwoordt een vraag bij dat beeld.
**Kies bij:** beeldgebonden leerdoelen: iets herkennen of beoordelen óp een afbeelding (röntgenfoto's, schermafbeeldingen, werkplekken, producten).
**Let op:** de kracht zit in de beelden, en die liggen per ronde vast in het game-bestand. Nieuwe vragen moeten dus inhoudelijk passen bij de bestáánde beelden — check dit expliciet in de intake ("waar gaan de afbeeldingen in jouw game over?"). Eigen beelden toevoegen kan alleen met assets die al in de game staan of via de editor.

### Vaste-rondes-games (vast)
Games zonder vragenpool: elke ronde heeft een vast aantal sleep-items op vaste posities (bv. anatomie-benoemoefeningen). 
**Wat kan:** alle tekstuele content vervangen (labels, vragen, uitleg, game-teksten) op de bestaande structuur — het aantal items per ronde ligt vast.
**Wat niet kan:** items toevoegen/verwijderen of posities wijzigen (Game Designer-werk). Meld dit eerlijk: "jouw game heeft per ronde een vast aantal plekken; ik kan de teksten vernieuwen, niet de opzet."

### MIX-games (container)
Eén game met rondes van verschillende speltypes (bv. sorteren + meerkeuze). De tool detecteert het speltype per ronde en vult per ronde. Vraag in de intake per ronde welk deelonderwerp erin moet, of stel zelf een logische verdeling voor.

## Nog niet ondersteund (eerlijk melden)
Tik-spellen (Whack a Mole, Pop the Bubble) en gesprekssimulaties (Dialog, JSON-beslisboom). Past zo'n vorm duidelijk beter, zeg dat en bied het beste ondersteunde alternatief.

## Keuzehulp in één zin
Feit of fabel → **tf** · situatie + beste handeling → **mc** · indelen in categorieën → **pum/sort** · herkennen op beeld → **loa** · afwisseling in één game → **mix**.
