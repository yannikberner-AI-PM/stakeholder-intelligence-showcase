export type TemplateKey = 'circle' | 'matrix';

export function isTemplateKey(value: string): value is TemplateKey {
  return value === 'circle' || value === 'matrix';
}
export type CircleZone = 'core' | 'direct' | 'indirect' | 'outside';
export type MatrixZone = 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';

const CORE_RADIUS = 1 / 6;
const DIRECT_RADIUS = 1 / 3;
const INDIRECT_RADIUS = 1 / 2;

export function ringForPosition(x: number, y: number): CircleZone {
  const dx = x - 0.5;
  const dy = y - 0.5;
  const distance = Math.sqrt(dx * dx + dy * dy);

  if (distance <= CORE_RADIUS) return 'core';
  if (distance <= DIRECT_RADIUS) return 'direct';
  if (distance <= INDIRECT_RADIUS) return 'indirect';
  return 'outside';
}

export function quadrantForPosition(x: number, y: number): MatrixZone {
  const isLeft = x < 0.5;
  const isTop = y < 0.5;
  if (isTop && isLeft) return 'top-left';
  if (isTop && !isLeft) return 'top-right';
  if (!isTop && isLeft) return 'bottom-left';
  return 'bottom-right';
}

export function clampToUnitSquare(x: number, y: number): { x: number; y: number } {
  return {
    x: Math.min(1, Math.max(0, x)),
    y: Math.min(1, Math.max(0, y)),
  };
}
