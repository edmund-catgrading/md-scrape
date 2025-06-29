# MoveTo

Phaser.Curves.MoveTo

A MoveTo Curve is a very simple curve consisting of only a single point.

Its intended use is to move the ending point in a Path.

**Constructor**

`new MoveTo([x], [y])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | `x` pixel coordinate. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | `y` pixel coordinate. |

---

**Scope**: static

> Source: [src/curves/path/MoveTo.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/MoveTo.js#L10)  
> Since: 3.0.0

# Public Members

## active

### active: boolean

**Description:**

Denotes that this Curve does not influence the bounds, points, and drawing of its parent Path. Must be `false` or some methods in the parent Path will throw errors.

> Source: [src/curves/path/MoveTo.js#L29](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/MoveTo.js#L29)  
> Since: 3.0.0

---

## p0

### p0: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The lone point which this curve consists of.

> Source: [src/curves/path/MoveTo.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/MoveTo.js#L39)  
> Since: 3.0.0

---

# Public Methods

## getLength

### <instance> getLength()

**Description:**

Gets the length of this curve.

**Returns:** number - The length of this curve. For a MoveTo the value is always 0.

> Source: [src/curves/path/MoveTo.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/MoveTo.js#L100)  
> Since: 3.0.0

---

## getPoint

### <instance> getPoint(t, [out])

**Description:**

Get point at relative position in curve according to length.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | No | The position along the curve to return. Where 0 is the start and 1 is the end. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2 object to store the result in. If not given will be created. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The coordinates of the point on the curve. If an `out` object was given this will be returned.

> Source: [src/curves/path/MoveTo.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/MoveTo.js#L49)  
> Since: 3.0.0

---

## getPointAt

### <instance> getPointAt(u, [out])

**Description:**

Retrieves the point at given position in the curve. This will always return this curve's only point.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| u | number | No | The position in the path to retrieve, between 0 and 1. Not used. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | An optional vector in which to store the point. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The modified `out` vector, or a new `Vector2` if none was provided.

> Source: [src/curves/path/MoveTo.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/MoveTo.js#L69)  
> Since: 3.0.0

---

## getResolution

### <instance> getResolution()

**Description:**

Gets the resolution of this curve.

**Returns:** number - The resolution of this curve. For a MoveTo the value is always 1.

> Source: [src/curves/path/MoveTo.js#L87](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/MoveTo.js#L87)  
> Since: 3.0.0

---

## toJSON

### <instance> toJSON()

**Description:**

Converts this curve into a JSON-serializable object.

**Returns:** [Phaser.Types.Curves.JSONCurve](../typedef/types-curves.md) - A primitive object with the curve's type and only point.

> Source: [src/curves/path/MoveTo.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/MoveTo.js#L113)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [p0](#p0)

    - [p0: Phaser.Math.Vector2](#p0-phasermathvector2)
* [Public Methods](#public-methods)

  + [getLength](#getlength)

    - [<instance> getLength()](#instance-getlength)
  + [getPoint](#getpoint)

    - [<instance> getPoint(t, [out])](#instance-getpointt-out)
  + [getPointAt](#getpointat)

    - [<instance> getPointAt(u, [out])](#instance-getpointatu-out)
  + [getResolution](#getresolution)

    - [<instance> getResolution()](#instance-getresolution)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)

Back to top

©2025[Phaser](https://docs.phaser.io)