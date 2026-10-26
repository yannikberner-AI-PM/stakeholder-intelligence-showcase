import test from 'node:test';
import assert from 'node:assert/strict';
import { isTemplateKey, ringForPosition, quadrantForPosition, clampToUnitSquare } from '../components/geometry.ts';

test('Vorlagen: nur circle und matrix', () => {
  assert.equal(isTemplateKey('circle'), true);
  assert.equal(isTemplateKey('matrix'), true);
  for (const value of ['', 'Circle', 'kanban']) assert.equal(isTemplateKey(value), false);
});
test('Kreismitte gehört zum Kern', () => {
  assert.equal(ringForPosition(0.5, 0.5), 'core');
});
test('Punkte innerhalb der vier Ringzonen', () => {
  for (const [offset, expected] of [[0.1, 'core'], [0.2, 'direct'], [0.4, 'indirect'], [0.6, 'outside']]) {
    assert.equal(ringForPosition(0.5 + offset, 0.5), expected);
  }
});
test('Äußerer Kreisrand ist inklusive', () => {
  assert.equal(ringForPosition(1, 0.5), 'indirect');
  assert.equal(ringForPosition(1 + Number.EPSILON, 0.5), 'outside');
});
test('Innere Ringgrenzen von beiden Seiten prüfen', () => {
  for (const [radius, inner, outer] of [[1 / 6, 'core', 'direct'], [1 / 3, 'direct', 'indirect']]) {
    assert.equal(ringForPosition(0.5 + radius - 1e-10, 0.5), inner);
    assert.equal(ringForPosition(0.5 + radius + 1e-10, 0.5), outer);
  }
});
test('Kreis ist rotationssymmetrisch für gleich große Achsabstände', () => {
  for (const d of [0.1, 0.25, 0.4, 0.6]) {
    const expected = ringForPosition(0.5 + d, 0.5);
    assert.equal(ringForPosition(0.5 - d, 0.5), expected);
    assert.equal(ringForPosition(0.5, 0.5 + d), expected);
    assert.equal(ringForPosition(0.5, 0.5 - d), expected);
  }
});
test('Alle vier Matrixquadranten', () => {
  for (const [x, y, expected] of [[0.2, 0.2, 'top-left'], [0.8, 0.2, 'top-right'], [0.2, 0.8, 'bottom-left'], [0.8, 0.8, 'bottom-right']]) {
    assert.equal(quadrantForPosition(x, y), expected);
  }
});
test('Matrixtrennlinien zählen zu rechts bzw. unten', () => {
  assert.equal(quadrantForPosition(0.5, 0.2), 'top-right');
  assert.equal(quadrantForPosition(0.2, 0.5), 'bottom-left');
  assert.equal(quadrantForPosition(0.5, 0.5), 'bottom-right');
});
test('Begrenzung erhält zulässige Werte und Ecken', () => {
  for (const [x, y] of [[0, 0], [1, 1], [0.3, 0.7]]) assert.deepEqual(clampToUnitSquare(x, y), { x, y });
});
test('Begrenzung schneidet Unter- und Überschreitungen ab', () => {
  assert.deepEqual(clampToUnitSquare(-0.2, 1.4), { x: 0, y: 1 });
  assert.deepEqual(clampToUnitSquare(2, -3), { x: 1, y: 0 });
});
test('Begrenzung ist idempotent auf einem synthetischen Raster', () => {
  for (const x of [-2, 0, 0.25, 0.5, 1, 2]) for (const y of [-2, 0, 0.75, 1, 3]) {
    const a = clampToUnitSquare(x, y);
    assert.deepEqual(clampToUnitSquare(a.x, a.y), a);
    assert.ok(a.x >= 0 && a.x <= 1 && a.y >= 0 && a.y <= 1);
  }
});
test('Dokumentierte Grenze: keine Validierung von NaN oder unendlichen Eingaben', () => {
  assert.ok(Number.isNaN(clampToUnitSquare(NaN, 0.5).x));
  assert.deepEqual(clampToUnitSquare(Infinity, -Infinity), { x: 1, y: 0 });
  assert.equal(ringForPosition(NaN, 0.5), 'outside');
  assert.equal(quadrantForPosition(NaN, NaN), 'bottom-right');
});
