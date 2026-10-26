# Prüfumfang und lokale Abnahme

## Ausgeführte Prüfungen

- `npm test`: zwölf separate Node-Tests für den unveränderten Geometrieauszug und anschließender Standardbibliothek-Validator.
- `python3 scripts/validate.py --source-root ../stakeholder-intelligence-agent`: Quellfingerprints und Bytegleichheit des Auszugs zusätzlich zum normalen Showcase-Gate.
- `git diff --check`: Whitespace-Kontrolle; bei noch unversionierten Dateien zusätzlich die Dateiprüfung des Validators beachten.
- Git-Zustand geprüft: Branch `docs/initial-showcase`, kein Commit, kein Remote; alle kuratierten Dateien bleiben unstaged.

Diese Einordnung wird beim lokalen Aufbau mit realen Befehlen geprüft. Es werden keine Produkt- oder Modelltestergebnisse aus früheren Sessions übernommen.

## Geometrie: abgedeckte Verträge

Gültige/ungültige Vorlagennamen, Kreismitte, vier Ringzonen, äußerer inklusiver Rand, beide Seiten innerer Ringgrenzen, Achsensymmetrie, vier Quadranten, Trennlinienzuordnung, unveränderte zulässige Werte, Clamping außerhalb des Bereichs, Idempotenz auf synthetischem Raster und das nichtvalidierende Verhalten bei `NaN`/Unendlichkeit.

Tests beschreiben auch Grenzen statt die Originaldatei still zu verbessern: `NaN` bleibt beim Clamping `NaN`; Zonenfunktionen klassifizieren solche ungültigen Eingaben ohne Fehler. Die Funktionen sind keine Sicherheitsvalidierung und ihre Zonen fließen im betrachteten Produktpfad nicht in die Vorschlagserstellung ein.

## Kuratierungsvalidator

Explizite Datei-Allowlist, keine Symlinks, keine unbekannten Dateien außerhalb `.git`, SHA-256-Dateimanifest, lokale Markdown-Dateilinks ohne externe Requests, JSON-Struktur, sichere relative Herkunftspfade, identischer Auszugshash sowie ausgewählte sensible Muster und Whitespace. Musterfunde geben nur Dateiname und Regelbezeichnung aus, nicht den gefundenen Inhalt.

Der optionale Originalabgleich benötigt private Quellen. Der normale Test läuft ohne private Quellen, Netzwerk, Paketinstallation, Zugangsdaten, Datenbank und Modellserver. `MANIFEST.sha256` enthält den Prüfumfang selbst; vor einer bewussten Änderung muss das Manifest nach Review aktualisiert werden. Es ist kein signierter Herkunftsnachweis.

## Nicht ausgeführt / nicht beansprucht

Kein Build und kein vollständiger Vitest-Lauf des privaten Produkts, kein Browser-/Drag-and-drop-Test, keine Datenbankmigration an Nutzerdaten, kein Ollama-Aufruf, keine Modellqualitätsevaluation, keine Vulnerability-Datenbankabfrage und kein Penetrationstest. Der Showcase enthält keine vollständige Anwendung und benötigt solche Ergebnisse nicht für die isolierte Auszugsprüfung. Produktfreigaben dürfen daraus nicht abgeleitet werden.

Die öffentliche Sicherheit des Dateisatzes beruht auf einer assistentengestützten Auswahl und Durchsicht plus heuristischen Checks, nicht auf einer unabhängigen Datenschutzprüfung oder bereits erteilter Eigentümerfreigabe.
