# Architektur

## Geltungsbereich

Beschreibung anhand des privaten Arbeitsstands, nicht eines laufenden Deployments. Die [Belegmatrix](PROVENANCE.md) nennt die zugehörigen Quelldateien. Nur `geometry.ts` ist hier als Anwendungscode enthalten; die restliche Architektur ist dokumentiert, nicht in diesem Repository ausführbar.

## Implementierter Datenfluss

```text
Browser: Board / Auftrag / Kreis oder Matrix / Stakeholder-Panel
  → relativer API-Client
  → Next.js Route Handler
  → Repository-Funktionen
  → better-sqlite3 → lokale SQLite-Datei (WAL)

Explizite Vorschlagsanforderung im Panel
  → POST /api/suggestions mit Stakeholder-ID
  → Stakeholder + eigenes Profil aus SQLite
  → Pflichtprüfung: eigener primärer DISC-Typ
  → Prompt aus Rolle, DISC und vorhandenen Notizfeldern
  → Ollama /api/chat (Standard: Loopback, nicht gestreamt)
     ├─ Erfolg → Text mit Herkunft „llm“
     └─ Fehler → DISC-Regelmatrix, wenn Stakeholder-Primärtyp vorhanden
                sonst sichtbarer Fehler statt erfundener Antwort
  → Vorschau mit Herkunft
  → explizites Übernehmen → Anhang an Kommunikationsnotizen → SQLite
```

Das Modell verändert die Datenbank nicht selbst und versendet keine Nachrichten. Vorschau und Übernahme sind im Panel getrennte Handlungen. Der Vorschlag nutzt gespeicherte Daten; ungespeicherte Textänderungen im Panel sind nicht automatisch Prompt-Eingaben.

## Domänenmodell und Speichergrenzen

| Baustein | Zuständigkeit |
| --- | --- |
| `stakeholder` | Gemeinsame Stammdaten, optionale E-Mail, manuelle DISC-Werte und vier Notizfelder. |
| `engagement` | Benannter Auftrag. |
| `engagement_stakeholder` | Zuordnung und Soft-Archivstatus innerhalb eines Auftrags. |
| `sh_postit` | Position, Farbe und Größe je Auftrag, Stakeholder und Vorlage. |
| `board_config` | Beschriftungen je Auftrag und Vorlage. |
| `self_profile` | Ein einzelnes eigenes DISC-Profil. |

Aufträge strukturieren die Darstellung, sind **keine Berechtigungs- oder Mandantengrenze**. Derselbe Stakeholder verweist in mehreren Aufträgen auf dieselben Notizen. Das Duplizieren kopiert aktive Zuordnungen, Post-it-Daten und Boardbeschriftungen, nicht neue unabhängige Personenakten. Wiederzuordnen hebt die lokale Zuordnungsarchivierung auf; erhaltene Positionen können wieder erscheinen.

`db.ts` legt die Datenbank standardmäßig unter `data/stakeholders.sqlite3` relativ zum Prozess-Arbeitsverzeichnis an und führt Migrationen aus. WAL bedeutet, dass Sicherung und Löschung nicht allein die Hauptdatei betreffen. Keine Verschlüsselung oder Benutzeridentität ist aus dieser Speicherarchitektur abzuleiten.

## Vorschlagsgrenze

Der Ollama-Client verwendet standardmäßig `http://127.0.0.1:11434`, Modelltag `llama3.1:8b` und einen Timeout von 60 Sekunden. Das sind Quellcode-Defaults, keine hier überprüfte Modellinstallation. Modell und Basis-URL sind über `OLLAMA_MODEL` und `OLLAMA_BASE_URL` überschreibbar. Es gibt in diesem Pfad keine Loopback-Allowlist oder garantierte Redirect-Sperre.

Der Prompt enthält Rolle, manuelle DISC-Werte und vorhandene Beobachtungs-, Kommunikations-, Kontext- und Follow-up-Notizen. Name und E-Mail werden vom betrachteten Prompt-Builder nicht eingefügt; Freitext kann sie trotzdem enthalten. Das Prompt-Framing verlangt Empfehlungen zur eigenen Anpassung. Eine solche Instruktion garantiert weder Datenlokalität noch sichere oder richtige Ausgaben.

Fehlt der eigene Primärtyp, wird der Vorschlag mit Status 412 blockiert. Scheitert Ollama, kann die Regelmatrix nur bei vorhandenem Stakeholder-Primärtyp helfen; sonst liefert der API-Pfad einen Fehler. Die Regelmatrix ist eine feste Heuristik, kein wissenschaftlicher Nachweis der DISC-Typologie.

## Öffentlicher Auszug

`geometry.ts` arbeitet mit normierten Koordinaten um den Mittelpunkt `(0.5, 0.5)`. Kreisradien sind `1/6`, `1/3` und `1/2`; Matrixtrennlinien liegen bei `0.5`. `clampToUnitSquare` begrenzt Werte numerisch, validiert aber keine endlichen Zahlen. `NaN` wird nicht abgefangen. Diese Grenze wird in den Showcase-Tests ausdrücklich festgehalten.

Die Geometrie ist kein Input des betrachteten Vorschlagsablaufs. Eine positionsabhängige Strategie wäre eine neue Produktfunktion, nicht eine hier nachgewiesene Eigenschaft.
