# Belegmatrix und Herkunft

Die Aussagen beruhen auf eingesehenem Anwendungscode und dem privaten Produktbrief. Die SHA-256-Fingerprints in [provenance.json](../provenance.json) identifizieren genau die gelesenen Dateiinhalte; Pfade sind relativ zum privaten Repository, keine maschinenspezifischen absoluten Pfade. Ein Fingerprint macht den privaten Code nicht öffentlich prüfbar und beweist weder Urheberschaft noch Laufzeitverhalten.

Der betrachtete Arbeitsstand enthält lokale Änderungen in Kontext-/Anweisungsdateien. Deshalb wird kein Commit als vollständiger Snapshot behauptet. Es wurde keine private Git-Historie übernommen und keine Änderung am Quellrepository vorgenommen.

| Aussage | Quellen relativ zum privaten Repository | Evidenzart / Grenze |
| --- | --- | --- |
| Next.js, React, TypeScript, SQLite, Vitest | `Code/package.json`, `Code/app/page.tsx` | Paketdefinition und Einstieg, keine aktuelle Abhängigkeitsprüfung. |
| Kreis/Matrix, Post-its, Beschriftung und Auftragswechsel | `Code/components/Board.tsx`, `Code/lib/repositories/boardConfig.ts` | Implementierter UI-/Persistenzpfad, kein neuer Browserlauf. |
| Gemeinsame Stammdaten; duplizierte Auftragszuordnungen und Soft-Archiv | `Code/lib/db.ts`, `Code/lib/repositories/engagements.ts`, `Code/lib/repositories/stakeholders.ts` | Schema und Repository-Logik, keine hier ausgeführten Datenbankmigrationen. |
| Notizen, manuelles DISC, Vorschau und Übernahme als Anhang | `Code/components/StakeholderPanel.tsx`, `Code/lib/apiClient.ts`, `Code/lib/discStrategy.ts` | Implementierte Handlungen, keine UX-Wirkungsmessung. |
| Ollama, Defaults und konfigurierbares Übertragungsziel | `Code/lib/ollama.ts` | Transportcode; kein installierter Modellstand oder garantiert lokaler Betrieb. |
| Profilpflicht und bedingter Regel-Fallback | `Code/lib/suggestions.ts`, `Code/lib/discStrategy.ts` | Kontrollfluss; kein neuer Live-LLM-Test. |
| Rolle, DISC und Notizen im Prompt; kein direktes Namens-/E-Mail-Feld | `Code/lib/suggestionPrompt.ts` | Quelltextprüfung; Freitext ist nicht automatisch anonym. |
| Begrenzte Markdown-Darstellung | `Code/components/MarkdownBody.tsx` | `skipHtml` und Elementliste, kein vollständiger XSS-Audit. |
| Geometrische Rechenregeln | `Code/lib/geometry.ts` | Bytegleicher öffentlicher Auszug und separate ausführbare Showcase-Tests. |
| Connectoren, Reminder, Kanban als Zukunft | `Product-brief.md` | Absicht, nicht Implementierungsnachweis. |

## Auswahl statt Repository-Kopie

Nur `Code/lib/geometry.ts` wurde als Originalcode übernommen. Die übrigen Quellen werden durch Pfade und Hashes referenziert, nicht als Volltext veröffentlicht. Die deutsche Dokumentation und die Tests sind für dieses Showcase neu formuliert. Weder Hardware-/Sessionnotizen noch operative Dateien oder reale Daten wurden übernommen. Die Testeingaben sind rein synthetische Koordinaten und ungültige Eingabewerte; keine Personenbeispiele.

Es sind keine Screenshots enthalten. Im betrachteten Quellcodebaum lagen außerhalb generierter Abhängigkeiten und Build-Verzeichnisse keine Produktbilder vor; insbesondere wurde die private Datenbank für keine Aufnahme geöffnet.

## Reproduzierbarkeit

`python3 scripts/validate.py --source-root ../stakeholder-intelligence-agent` prüft den lokalen Quellstand gegen alle referenzierten Hashes und den Auszug gegen die Originaldatei. Nach Änderungen am privaten Produkt kann dieser Abgleich absichtlich fehlschlagen. Ohne private Quellen prüft `npm test` weiterhin Auszug, Herkunftsstruktur, Inventar, Links und Showcase-Dateiintegrität, nicht die Wahrheit aller privaten Implementierungsbehauptungen.

[MANIFEST.sha256](../MANIFEST.sha256) umfasst alle kuratierten Dateien außer sich selbst und `.git/`. Hashes ersetzen keine Freigabe; eine Veröffentlichung bedarf weiterhin der in [README](../README.md) genannten Eigentümerprüfung.
