# Line

Phaser.Curves.Line

A LineCurve is a "curve" comprising exactly two points (a line segment).

**Constructor**

`new Line(p0, [p1])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| p0 | [Phaser.Math.Vector2](math-vector2.md) | Array.<number> | No | The first endpoint. |
| --- | --- | --- | --- |
| p1 | [Phaser.Math.Vector2](math-vector2.md) | Yes | The second endpoint. |

---

**Scope**: static

**Extends**

> [Phaser.Curves.Curve](curves-curve.md)

> Source: [src/curves/LineCurve.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L15)  
> Since: 3.0.0

# Public Members

## active

### active: boolean

**Description:**

For a curve on a Path, `false` means the Path will ignore this curve.

**Inherits:** [Phaser.Curves.Curve#active](curves-curve.md)

> Source: [src/curves/Curve.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L80)  
> Since: 3.0.0

---

## arcLengthDivisions

### arcLengthDivisions: number

**Description:**

The quantity of arc length divisions within the curve.

**Overrides:** Phaser.Curves.Curve#arcLengthDivisions

> Source: [src/curves/LineCurve.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L65)  
> Since: 3.0.0

---

## cacheArcLengths

### cacheArcLengths: Array.<number>

**Description:**

An array of cached arc length values.

**Inherits:** [Phaser.Curves.Curve#cacheArcLengths](curves-curve.md)

> Source: [src/curves/Curve.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L60)  
> Since: 3.0.0

---

## defaultDivisions

### defaultDivisions: number

**Description:**

The default number of divisions within the curve.

**Inherits:** [Phaser.Curves.Curve#defaultDivisions](curves-curve.md)

> Source: [src/curves/Curve.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L40)  
> Since: 3.0.0

---

## needsUpdate

### needsUpdate: boolean

**Description:**

Does the data of this curve need updating?

**Inherits:** [Phaser.Curves.Curve#needsUpdate](curves-curve.md)

> Source: [src/curves/Curve.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L70)  
> Since: 3.0.0

---

## p0

### p0: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The first endpoint.

> Source: [src/curves/LineCurve.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L45)  
> Since: 3.0.0

---

## p1

### p1: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The second endpoint.

> Source: [src/curves/LineCurve.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L54)  
> Since: 3.0.0

---

## type

### type: string

**Description:**

String based identifier for the type of curve.

**Inherits:** [Phaser.Curves.Curve#type](curves-curve.md)

> Source: [src/curves/Curve.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L31)  
> Since: 3.0.0

---

# Private Members

## \_tmpVec2A

### \_tmpVec2A: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A temporary calculation Vector.

**Access:** private

**Inherits:** [Phaser.Curves.Curve#\_tmpVec2A](curves-curve.md)

> Source: [src/curves/Curve.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L90)  
> Since: 3.0.0

---

## \_tmpVec2B

### \_tmpVec2B: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A temporary calculation Vector.

**Access:** private

**Inherits:** [Phaser.Curves.Curve#\_tmpVec2B](curves-curve.md)

> Source: [src/curves/Curve.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L100)  
> Since: 3.0.0

---

# Public Methods

## draw

### <instance> draw(graphics)

**Description:**

Draws this curve on the given Graphics object.

The curve is drawn using `Graphics.lineBetween` so will be drawn at whatever the present Graphics line color is.

The Graphics object is not cleared before the draw, so the curve will appear on-top of anything else already rendered to it.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Graphics instance onto which this curve will be drawn. |
| --- | --- | --- | --- |

**Overrides:** Phaser.Curves.Curve#draw

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - The Graphics object to which the curve was drawn.

> Source: [src/curves/LineCurve.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L236)  
> Since: 3.0.0

---

## fromJSON

### <static> fromJSON(data)

**Description:**

Configures this line from a JSON representation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | [Phaser.Types.Curves.JSONCurve](../typedef/types-curves.md) | No | The JSON object containing this curve data. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Line](curves-line.md) - A new LineCurve object.

> Source: [src/curves/LineCurve.js#L280](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L280)  
> Since: 3.0.0

---

## getBounds

### <instance> getBounds([out])

**Description:**

Returns a Rectangle where the position and dimensions match the bounds of this Curve.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | A Rectangle object to store the bounds in. If not given a new Rectangle will be created. |
| --- | --- | --- | --- |

**Overrides:** Phaser.Curves.Curve#getBounds

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - A Rectangle object holding the bounds of this curve. If `out` was given it will be this object.

> Source: [src/curves/LineCurve.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L76)  
> Since: 3.0.0

---

## getDistancePoints

### <instance> getDistancePoints(distance)

**Description:**

Returns an array of points, spaced out X distance pixels apart.

The smaller the distance, the larger the array will be.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| distance | number | No | The distance, in pixels, between each point along the curve. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Geom.Point](geom-point.md)> - An Array of Point objects.

**Inherits:** [Phaser.Curves.Curve#getDistancePoints](curves-curve.md)

> Source: [src/curves/Curve.js#L169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L169)  
> Since: 3.0.0

---

## getEndPoint

### <instance> getEndPoint([out])

**Description:**

Get a point at the end of the curve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | Optional Vector object to store the result in. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - Vector2 containing the coordinates of the curves end point.

**Inherits:** [Phaser.Curves.Curve#getEndPoint](curves-curve.md)

> Source: [src/curves/Curve.js#L189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L189)  
> Since: 3.0.0

---

## getLength

### <instance> getLength()

**Description:**

Get total curve arc length

**Returns:** number - The total length of the curve.

**Inherits:** [Phaser.Curves.Curve#getLength](curves-curve.md)

> Source: [src/curves/Curve.js#L206](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L206)  
> Since: 3.0.0

---

## getLengths

### <instance> getLengths([divisions])

**Description:**

Get a list of cumulative segment lengths.

These lengths are

* [0] 0
* [1] The first segment
* [2] The first and second segment
* ...
* [divisions] All segments

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| divisions | number | Yes | The number of divisions or segments. |
| --- | --- | --- | --- |

**Returns:** Array.<number> - An array of cumulative lengths.

**Inherits:** [Phaser.Curves.Curve#getLengths](curves-curve.md)

> Source: [src/curves/Curve.js#L222](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L222)  
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

> Source: [src/curves/LineCurve.js#L131](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L131)  
> Since: 3.0.0

---

## getPointAt

### <instance> getPointAt(u, [out])

**Description:**

Gets a point at a given position on the line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| u | number | No | The position along the curve to return. Where 0 is the start and 1 is the end. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2 object to store the result in. If not given will be created. |

**Overrides:** Phaser.Curves.Curve#getPointAt

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The coordinates of the point on the curve. If an `out` object was given this will be returned.

> Source: [src/curves/LineCurve.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L160)  
> Since: 3.0.0

---

## getPoints

### <instance> getPoints([divisions], [stepRate], [out])

**Description:**

Get a sequence of evenly spaced points from the curve.

You can pass `divisions`, `stepRate`, or neither.

The number of divisions will be

1. `divisions`, if `divisions` > 0; or
2. `this.getLength / stepRate`, if `stepRate` > 0; or
3. `this.defaultDivisions`

`1 + divisions` points will be returned.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| divisions | number | Yes | The number of divisions to make. |
| --- | --- | --- | --- |
| stepRate | number | Yes | The curve distance between points, implying `divisions`. |
| out | array | Array.<[Phaser.Math.Vector2](math-vector2.md)> | Yes | An optional array to store the points in. |

**Returns:** array, Array.<[Phaser.Math.Vector2](math-vector2.md)> - An array of Points from the curve.

**Inherits:** [Phaser.Curves.Curve#getPoints](curves-curve.md)

> Source: [src/curves/Curve.js#L300](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L300)  
> Since: 3.0.0

---

## getRandomPoint

### <instance> getRandomPoint([out])

**Description:**

Get a random point from the curve.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A point object to store the result in. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The point.

**Inherits:** [Phaser.Curves.Curve#getRandomPoint](curves-curve.md)

> Source: [src/curves/Curve.js#L349](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L349)  
> Since: 3.0.0

---

## getResolution

### <instance> getResolution([divisions])

**Description:**

Gets the resolution of the line.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| divisions | number | Yes | 1 | The number of divisions to consider. |
| --- | --- | --- | --- | --- |

**Returns:** number - The resolution. Equal to the number of divisions.

> Source: [src/curves/LineCurve.js#L114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L114)  
> Since: 3.0.0

---

## getSpacedPoints

### <instance> getSpacedPoints([divisions], [stepRate], [out])

**Description:**

Get a sequence of equally spaced points (by arc distance) from the curve.

`1 + divisions` points will be returned.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| divisions | number | Yes | "this.defaultDivisions" | The number of divisions to make. |
| --- | --- | --- | --- | --- |
| stepRate | number | Yes |  | Step between points. Used to calculate the number of points to return when divisions is falsy. Ignored if divisions is positive. |
| out | array | Array.<[Phaser.Math.Vector2](math-vector2.md)> | Yes |  | An optional array to store the points in. |

**Returns:** Array.<[Phaser.Math.Vector2](math-vector2.md)> - An array of points.

**Inherits:** [Phaser.Curves.Curve#getSpacedPoints](curves-curve.md)

> Source: [src/curves/Curve.js#L370](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L370)  
> Since: 3.0.0

---

## getStartPoint

### <instance> getStartPoint([out])

**Description:**

Gets the starting point on the curve.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2 object to store the result in. If not given will be created. |
| --- | --- | --- | --- |

**Overrides:** Phaser.Curves.Curve#getStartPoint

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The coordinates of the point on the curve. If an `out` object was given this will be returned.

> Source: [src/curves/LineCurve.js#L95](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L95)  
> Since: 3.0.0

---

## getTangent

### <instance> getTangent([t], [out])

**Description:**

Gets the slope of the line as a unit vector.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | Yes | The relative position on the line, [0..1]. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A vector to store the result in. |

**Overrides:** Phaser.Curves.Curve#getTangent

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The tangent vector.

> Source: [src/curves/LineCurve.js#L178](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L178)  
> Since: 3.0.0

---

## getTangentAt

### <instance> getTangentAt(u, [out])

**Description:**

Get a unit vector tangent at a relative position on the curve, by arc length.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| u | number | No | The relative position on the curve, [0..1]. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A vector to store the result in. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The tangent vector.

**Inherits:** [Phaser.Curves.Curve#getTangentAt](curves-curve.md)

> Source: [src/curves/Curve.js#L472](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L472)  
> Since: 3.0.0

---

## getTFromDistance

### <instance> getTFromDistance(distance, [divisions])

**Description:**

Given a distance in pixels, get a t to find p.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| distance | number | No | The distance, in pixels. |
| --- | --- | --- | --- |
| divisions | number | Yes | Optional amount of divisions. |

**Returns:** number - The distance.

**Inherits:** [Phaser.Curves.Curve#getTFromDistance](curves-curve.md)

> Source: [src/curves/Curve.js#L492](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L492)  
> Since: 3.0.0

---

## getUtoTmapping

### <instance> getUtoTmapping(u, distance, [divisions])

**Description:**

Given u ( 0 .. 1 ), get a t to find p. This gives you points which are equidistant.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| u | number | No | A float between 0 and 1. |
| --- | --- | --- | --- |
| distance | number | No | The distance, in pixels. |
| divisions | number | Yes | Optional amount of divisions. |

**Overrides:** Phaser.Curves.Curve#getUtoTmapping

**Returns:** number - The equidistant value.

> Source: [src/curves/LineCurve.js#L200](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L200)  
> Since: 3.0.0

---

## toJSON

### <instance> toJSON()

**Description:**

Gets a JSON representation of the line.

**Returns:** [Phaser.Types.Curves.JSONCurve](../typedef/types-curves.md) - The JSON object containing this curve data.

> Source: [src/curves/LineCurve.js#L259](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/LineCurve.js#L259)  
> Since: 3.0.0

---

## updateArcLengths

### <instance> updateArcLengths()

**Description:**

Calculate and cache the arc lengths.

**Inherits:** [Phaser.Curves.Curve#updateArcLengths](curves-curve.md)

> Source: [src/curves/Curve.js#L594](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L594)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [arcLengthDivisions](#arclengthdivisions)

    - [arcLengthDivisions: number](#arclengthdivisions-number)
  + [cacheArcLengths](#cachearclengths)

    - [cacheArcLengths: Array.<number>](#cachearclengths-arraynumber)
  + [defaultDivisions](#defaultdivisions)

    - [defaultDivisions: number](#defaultdivisions-number)
  + [needsUpdate](#needsupdate)

    - [needsUpdate: boolean](#needsupdate-boolean)
  + [p0](#p0)

    - [p0: Phaser.Math.Vector2](#p0-phasermathvector2)
  + [p1](#p1)

    - [p1: Phaser.Math.Vector2](#p1-phasermathvector2)
  + [type](#type)

    - [type: string](#type-string)
* [Private Members](#private-members)

  + [\_tmpVec2A](#_tmpvec2a)

    - [\_tmpVec2A: Phaser.Math.Vector2](#_tmpvec2a-phasermathvector2)
  + [\_tmpVec2B](#_tmpvec2b)

    - [\_tmpVec2B: Phaser.Math.Vector2](#_tmpvec2b-phasermathvector2)
* [Public Methods](#public-methods)

  + [draw](#draw)

    - [<instance> draw(graphics)](#instance-drawgraphics)
  + [fromJSON](#fromjson)

    - [<static> fromJSON(data)](#static-fromjsondata)
  + [getBounds](#getbounds)

    - [<instance> getBounds([out])](#instance-getboundsout)
  + [getDistancePoints](#getdistancepoints)

    - [<instance> getDistancePoints(distance)](#instance-getdistancepointsdistance)
  + [getEndPoint](#getendpoint)

    - [<instance> getEndPoint([out])](#instance-getendpointout)
  + [getLength](#getlength)

    - [<instance> getLength()](#instance-getlength)
  + [getLengths](#getlengths)

    - [<instance> getLengths([divisions])](#instance-getlengthsdivisions)
  + [getPoint](#getpoint)

    - [<instance> getPoint(t, [out])](#instance-getpointt-out)
  + [getPointAt](#getpointat)

    - [<instance> getPointAt(u, [out])](#instance-getpointatu-out)
  + [getPoints](#getpoints)

    - [<instance> getPoints([divisions], [stepRate], [out])](#instance-getpointsdivisions-steprate-out)
  + [getRandomPoint](#getrandompoint)

    - [<instance> getRandomPoint([out])](#instance-getrandompointout)
  + [getResolution](#getresolution)

    - [<instance> getResolution([divisions])](#instance-getresolutiondivisions)
  + [getSpacedPoints](#getspacedpoints)

    - [<instance> getSpacedPoints([divisions], [stepRate], [out])](#instance-getspacedpointsdivisions-steprate-out)
  + [getStartPoint](#getstartpoint)

    - [<instance> getStartPoint([out])](#instance-getstartpointout)
  + [getTangent](#gettangent)

    - [<instance> getTangent([t], [out])](#instance-gettangentt-out)
  + [getTangentAt](#gettangentat)

    - [<instance> getTangentAt(u, [out])](#instance-gettangentatu-out)
  + [getTFromDistance](#gettfromdistance)

    - [<instance> getTFromDistance(distance, [divisions])](#instance-gettfromdistancedistance-divisions)
  + [getUtoTmapping](#getutotmapping)

    - [<instance> getUtoTmapping(u, distance, [divisions])](#instance-getutotmappingu-distance-divisions)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [updateArcLengths](#updatearclengths)

    - [<instance> updateArcLengths()](#instance-updatearclengths)

Back to top

©2025[Phaser](https://docs.phaser.io)