# Beeldprompts — Nano Banana (Gemini) sjablonen en werkwijze

Doel: de gebruiker genereert zelf beelden met kopieerbare prompts; de tool koppelt ze daarna automatisch. Beeld is altijd optioneel — zonder beeld is de game volwaardig speelbaar.

## Stap A — Stijl bepalen
Vraag of er een huisstijl/illustratiestijl is. Twee routes:
1. **Stijl uit het game-bestand afleiden (voorkeur):** bekijk de achtergrond-PNG in het game-bestand en beschrijf de stijl in de prompt (kleurpalet, vormentaal, sfeer). Voorbeeld-stijlprofiel: *flat vector illustration, muted lavender-grey pastel palette, subtle pink-to-peach organic blob accents, minimalist shapes, no outlines, clean light background*.
2. **Geen duidelijke stijl:** gebruik een neutraal profiel: *friendly flat vector illustration, soft pastel colors, minimalist, clean background*.

## Stap B — Prompts leveren (kopieerbaar blok)
Basisprompt (vervang [STIJLPROFIEL] en [ONDERWERP]):

> "Flat vector illustration: [STIJLPROFIEL]. Subject: [ONDERWERP]. [WERKCONTEXT van de doelgroep]. Simple, calm, friendly educational style, suitable as a small illustration on a quiz card. No text in the image, no detailed faces. PNG, landscape 3:2."

Lever standaard **5 onderwerp-varianten** die het thema dekken maar generiek genoeg zijn om bij meerdere vragen te passen (de beelden worden verdeeld over de vragen, niet 1-op-1 gekoppeld). Kies herkenbare objecten en situaties uit de werkcontext, geen abstracties.

Tips voor de gebruiker: genereer 2-3 varianten per prompt en kies de rustigste; houd alle beelden in één chatsessie voor stijlconsistentie; geen tekst in beeld.

## Stap C — Formaat en klaarzetten (simpel stappenplan voor de gebruiker)
1. Sla de vijf gekozen beelden op als **PNG, liggend, 640 × 432 pixels** (of groter in 3:2 — de tool schaalt zelf terug naar het juiste formaat).
2. Zet ze in één map (bv. "Afbeeldingen") en geef ze korte namen zonder rare tekens, bv. `beeld-1.png` t/m `beeld-5.png`.
3. Zeg "de afbeeldingen staan klaar" — de tool doet de rest (schalen, koppelen, controleren).

## Stap D — Verwerken
Draai de generatie opnieuw met `--images <map>`. Controleer daarna in het controle-overzicht welke afbeelding bij welke vragen hoort, en wijs de gebruiker erop bij de speeltest te checken of de beelden scherp en passend zijn (zo niet: groter formaat aanleveren of andere prompt kiezen).
