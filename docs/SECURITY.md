# Sicherheits- und Vertrauensmodell

## Zwei verschiedene Grenzen

**Dieses Showcase:** Dokumentation, ein reiner Originalauszug und synthetische Zahlen in Tests. Keine laufende Anwendung, gespeicherten Stakeholder, Screenshots, Netzwerkdienste oder Zugangsdaten. Es wurde aus einer expliziten Dateiauswahl aufgebaut, nicht aus einem Klon der privaten Historie.

**Privates Produkt:** verarbeitet potenziell sensible personenbezogene Notizen und subjektive Einschätzungen. Lokal-first reduziert einen Datenübertragungsweg, ersetzt aber weder Rechtsgrundlage noch Zugriffsschutz, Zweckbindung, Löschkonzept oder menschliche Verantwortung. Eine DSGVO- oder Sicherheitszertifizierung wird nicht behauptet.

## Implementierte Schutzmechanismen und ihre Grenzen

| Mechanismus | Was tatsächlich belegt ist | Was daraus nicht folgt |
| --- | --- | --- |
| Lokale Persistenz | SQLite-Datei im lokalen Prozesskontext. | Keine nachgewiesene Verschlüsselung, Benutzerisolation oder sichere Datenträgerlöschung. |
| Modell-Default | Ollama über Loopback im Standard. | Keine technische Garantie für ausschließlich lokale Übertragung; Basis-URL kann auf entfernte Dienste zeigen. |
| Prompt-Minimierung | Name und E-Mail werden nicht direkt in den Prompt eingesetzt. | Notizen und Rolle können Personen identifizierbar machen. |
| Vorschau/Freigabe | Modelltext erscheint zunächst als Vorschlag; Übernahme hängt ihn an Notizen an. | Die Vorschau findet **nach** der Übertragung an den Modell-Endpunkt statt; sie ist keine vorherige Übertragungsfreigabe. |
| Ethisches Framing | Prompt fokussiert eigenes Kommunikationsverhalten und untersagt Dossier-/Manipulationssprache. | Keine geprüfte Inhaltsgarantie, keine Abwehr aller Prompt-Injections. |
| Regel-Fallback | Bei Modellfehler und ausreichenden DISC-Daten explizit als Regelquelle gekennzeichnet. | Keine objektive Beurteilung einer Person und kein Qualitätsnachweis. |
| Markdown-Darstellung | ReactMarkdown mit `skipHtml` und erlaubten Elementen. | Kein vollständiger Anwendungssicherheitsnachweis; Links bleiben ein zusätzlicher Prüfpunkt. |
| Soft-Archiv | Auftragszuordnung wird archiviert; Positionsdaten bleiben erhalten. | Kein Löschen personenbezogener Daten. |

## Offene Risiken / Voraussetzungen vor einem öffentlichen Betrieb

- In den betrachteten API-Routen ist keine Authentifizierung oder auftragsbezogene Autorisierung implementiert. Ein Auftrag ist kein Konto. Anwendung und Datenbank nicht als öffentlich freigegebenen Dienst behandeln.
- Bind-Adresse, Netzwerkzugriff, Origin-/CSRF-Schutz, Rate Limits, Zugriffsrechte und sichere Fehlerbehandlung müssen vor jedem externen Betrieb separat geprüft und gehärtet werden. Es wurde kein Penetrationstest ausgeführt.
- `OLLAMA_BASE_URL` wird nicht auf Loopback beschränkt. Betreiber müssen die wirksame Zieladresse prüfen; ein Prompt-Satz „nur lokal“ erzwingt keinen sicheren Transport. Remote-Endpunkte und Redirects sind nicht durch dieses Showcase validiert.
- Keine Modellanfragen mit realen Notizen für diese Kuratierung. Modellqualität, Halluzinationen, stereotype Ableitungen und Angriffe über Freitext bleiben ungetestet. Vorschläge als verwerfbare Hypothesen prüfen, nicht für Personalentscheidungen verwenden.
- Aufbewahrung, Korrektur und vollständige Löschung einschließlich WAL/SHM, Backups, Modellserver-Logs und sonstiger Kopien benötigen eine bewusste Regelung. Archivieren erfüllt diese Aufgabe nicht.
- Abhängigkeiten und produktive Laufzeit wurden hier nicht auf aktuelle Schwachstellen geprüft. Das Showcase hat keine externen Paketabhängigkeiten und übernimmt keinen Lockfile des Produkts.

## Veröffentlichungsschranke

Vor Veröffentlichung: alle Dateien und Rechte durch den Eigentümer prüfen, den exakt freigegebenen Dateisatz bestätigen und erst danach separat Commit/Remote/Publikation erlauben. Der lokale Validator ist eine Heuristik plus Inventar-/Integritätsprüfung, **keine Garantie**, dass jede vertrauliche Information erkannt wird. Fundstellen oder mögliche Schwachstellen zunächst nicht mit realen Personendaten in öffentlichen Issues teilen.
