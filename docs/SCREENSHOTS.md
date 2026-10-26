# Produktaufnahmen mit synthetischen Daten

Die drei PNG-Dateien zeigen die tatsächlich laufende private Anwendung, keine Mockups und keine nachträglich veränderte Oberfläche. Aufgenommen am 26.10.2026 in einem frischen Playwright-Chromium-Kontext mit 1600 × 1100 Pixeln. Alle vier Demo-Personen, Rollen, Notizen und das Projekt Morgenlicht sind eigens erstellte synthetische Eingaben.

## Isolierter Aufbau

- Unveränderter Anwendungscode aus Quellcommit `30496be208ce770d20c3f895b47bc93cb21c4fad`, Paketversion `0.1.0`. Lokale Änderungen an privaten Kontextdateien wurden nicht übernommen.
- Ausschließlich versionierte Code-Dateien in eine neue Scratch-Kopie übernommen. Keine Datenbank, Umgebungsdateien, private Historie oder Betriebsdaten kopiert. Vor Start existierte dort kein Datenverzeichnis.
- Vorhandene Paketabhängigkeiten nur zur Auflösung verlinkt, nicht verändert oder veröffentlicht. Eigener Produktionsbuild und Server ausschließlich an Loopback. SQLite wird über das unveränderte `process.cwd()`-Verhalten nur in der Scratch-Kopie neu angelegt.
- Synthetische Datensätze über die echten Anwendungs-APIs angelegt und zurückgelesen. Manuelle DISC-Demoauswahl: eigenes Profil D, Demo Alex S. Keine Aussage über reale Personen.
- Ollama-Ziel bewusst auf den nicht erreichbaren Loopback-Port 1 gesetzt. Die echte Fehlerbehandlung erzeugte den sichtbaren Regel-Fallback. Kein Modelltext und kein erfolgreicher LLM-Lauf werden behauptet.
- Browser ohne persönliches Profil, Cookies oder Anmeldung. Browserrequests außerhalb von Loopback blockiert. Der Cloud-Browser lehnte Loopback ab; deshalb erfolgte die Aufnahme mit lokalem, unabhängig gestartetem Playwright-Chromium statt mit persönlichem Chrome.

## Sichtbarer und geprüfter Ablauf

1. Demo-Auftrag ausgewählt, Kreis-Modell mit vier positionierten Post-its aufgenommen.
2. Demo Alex geöffnet, gespeicherte Markdown-Notizen und offene Punkte aufgenommen.
3. Kommunikations-Strategie abgeleitet und die echte Vorschau mit Herkunft **Regel-Fallback**, Übernehmen und Verwerfen aufgenommen.
4. Erst nach der Aufnahme übernommen und per API zurückgelesen: bisherige Kommunikationsnotizen bleiben erhalten, Vorschlag wird angehängt. Keine Browser-Laufzeitfehler beobachtet.

Alle drei veröffentlichten Bilder wurden assistentengestützt visuell auf synthetische Inhalte, Lesbarkeit und sichtbare sensible Daten geprüft. Die leere E-Mail-Eingabe zeigt nur den unveränderten UI-Platzhalter. Kein privater Datenbankinhalt wurde für diese Arbeit geöffnet. Bilder sind unveränderte Viewport-Aufnahmen; kleine Controls und die englischen Ringlabels entsprechen dem Produktstand.

## Build und Grenzen

`npm run build` war erfolgreich, anschließend bestanden `npm test` mit **21 Testdateien und 128 Tests** in der isolierten Anwendungskopie. Build-ID: `H1fFUUefeWpfPzycQ2z9G`. Quellfingerprint und Bildhashes stehen in [provenance.json](../provenance.json).

Der Quellfingerprint ist SHA-256 über die lexikografisch sortierten kopierten Git-Pfade: pro Datei relativer Repository-Pfad, NUL, SHA-256 der Dateibytes, Newline. Er umfasst die versionierten kopierten Code-Eingaben, nicht Datenbank, Abhängigkeiten oder Build-Ausgaben.

Dies ist ein begrenzter lokaler Produktnachweis, kein vollständiger E2E-Test, kein Drag-and-drop-Test, keine Modellqualitätsevaluation und keine Produktiv- oder Datenschutzfreigabe. Der öffentliche Dateisatz enthält nur Dokumentation, Originalauszug, Tests und die drei geprüften Bilder. Die Anwendung und synthetische Datenbank werden nicht mitveröffentlicht.
