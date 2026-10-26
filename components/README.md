# Originalauszug: normierte Boardgeometrie

`geometry.ts` stammt unverändert aus `Code/lib/geometry.ts` des privaten Produkts. Quell- und Auszugshash sind in [provenance.json](../provenance.json) identisch. Ein lokaler Abgleich ist mit dem optionalen `--source-root` des Validators möglich.

Enthalten: Vorlagenprüfung, Einordnung in Kreisringe und Matrixquadranten sowie numerische Begrenzung auf das Einheitsquadrat. Die Datei hat keine Imports, Seiteneffekte, Personendaten, Netzwerk- oder Datenbankzugriffe.

Der Auszug illustriert eine kleine fachliche Rechenregel, keine vollständige Board-Interaktion. Insbesondere verwendet der eingesehene Vorschlagspfad die geometrische Zonenklassifikation nicht. `NaN` und nichtendliche Werte sind keine validierten Nutzereingaben; `clampToUnitSquare` ist kein API-Validator.

Die Tests sind eigens für das Showcase mit `node:test` geschrieben, nicht als unveränderte Produkttests ausgegeben. Sie dokumentieren auch Grenzverhalten. Proprietär gemäß [LICENSE](../LICENSE); kein Open-Source-SDK.
