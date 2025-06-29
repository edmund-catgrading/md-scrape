# Curve

Phaser.Curves.Curve

A Base Curve class, which all other curve types extend.

Based on the three.js Curve classes created by [zz85](http://www.lab4games.net/zz85/blog)

**Constructor**

`new Curve(type)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| type | string | No | The curve type. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/curves/Curve.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L12)  
> Since: 3.0.0

# Public Members

## active

### active: boolean

**Description:**

For a curve on a Path, `false` means the Path will ignore this curve.

> Source: [src/curves/Curve.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L80)  
> Since: 3.0.0

---

## arcLengthDivisions

### arcLengthDivisions: number

**Description:**

The quantity of arc length divisions within the curve.

> Source: [src/curves/Curve.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L50)  
> Since: 3.0.0

---

## cacheArcLengths

### cacheArcLengths: Array.<number>

**Description:**

An array of cached arc length values.

> Source: [src/curves/Curve.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L60)  
> Since: 3.0.0

---

## defaultDivisions

### defaultDivisions: number

**Description:**

The default number of divisions within the curve.

> Source: [src/curves/Curve.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L40)  
> Since: 3.0.0

---

## needsUpdate

### needsUpdate: boolean

**Description:**

Does the data of this curve need updating?

> Source: [src/curves/Curve.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L70)  
> Since: 3.0.0

---

## type

### type: string

**Description:**

String based identifier for the type of curve.

> Source: [src/curves/Curve.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L31)  
> Since: 3.0.0

---

# Private Members

## \_tmpVec2A

### \_tmpVec2A: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A temporary calculation Vector.

**Access:** private

> Source: [src/curves/Curve.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L90)  
> Since: 3.0.0

---

## \_tmpVec2B

### \_tmpVec2B: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A temporary calculation Vector.

**Access:** private

> Source: [src/curves/Curve.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L100)  
> Since: 3.0.0

---

# Public Methods

## draw

### <instance> draw(graphics, [pointsTotal])

**Description:**

Draws this curve on the given Graphics object.

The curve is drawn using `Graphics.strokePoints` so will be drawn at whatever the present Graphics stroke color is.

The Graphics object is not cleared before the draw, so the curve will appear on-top of anything else already rendered to it.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No |  | The Graphics instance onto which this curve will be drawn. |
| --- | --- | --- | --- | --- |
| pointsTotal | number | Yes | 32 | The resolution of the curve. The higher the value the smoother it will render, at the cost of rendering performance. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - The Graphics object to which the curve was drawn.

> Source: [src/curves/Curve.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L111)  
> Since: 3.0.0

---

## getBounds

### <instance> getBounds([out], [accuracy])

**Description:**

Returns a Rectangle where the position and dimensions match the bounds of this Curve.

You can control the accuracy of the bounds. The value given is used to work out how many points

to plot across the curve. Higher values are more accurate at the cost of calculation speed.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes |  | The Rectangle to store the bounds in. If falsey a new object will be created. |
| --- | --- | --- | --- | --- |
| accuracy | number | Yes | 16 | The accuracy of the bounds calculations. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - A Rectangle object holding the bounds of this curve. If `out` was given it will be this object.

> Source: [src/curves/Curve.js#L135](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L135)  
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

> Source: [src/curves/Curve.js#L189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L189)  
> Since: 3.0.0

---

## getLength

### <instance> getLength()

**Description:**

Get total curve arc length

**Returns:** number - The total length of the curve.

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

> Source: [src/curves/Curve.js#L222](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L222)  
> Since: 3.0.0

---

## getPointAt

### <instance> getPointAt(u, [out])

**Description:**

Get a point at a relative position on the curve, by arc length.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| u | number | No | The relative position, [0..1]. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A point to store the result in. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The point.

> Source: [src/curves/Curve.js#L278](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L278)  
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

> Source: [src/curves/Curve.js#L349](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L349)  
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

> Source: [src/curves/Curve.js#L370](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L370)  
> Since: 3.0.0

---

## getStartPoint

### <instance> getStartPoint([out])

**Description:**

Get a point at the start of the curve.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A point to store the result in. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The point.

> Source: [src/curves/Curve.js#L411](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L411)  
> Since: 3.0.0

---

## getTangent

### <instance> getTangent(t, [out])

**Description:**

Get a unit vector tangent at a relative position on the curve.

In case any sub curve does not implement its tangent derivation,

2 points a small delta apart will be used to find its gradient

which seems to give a reasonable approximation

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | No | The relative position on the curve, [0..1]. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A vector to store the result in. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - Vector approximating the tangent line at the point t (delta +/- 0.0001)

> Source: [src/curves/Curve.js#L430](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L430)  
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

**Returns:** number - The equidistant value.

> Source: [src/curves/Curve.js#L513](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L513)  
> Since: 3.0.0

---

## updateArcLengths

### <instance> updateArcLengths()

**Description:**

Calculate and cache the arc lengths.

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
  + [type](#type)

    - [type: string](#type-string)
* [Private Members](#private-members)

  + [\_tmpVec2A](#_tmpvec2a)

    - [\_tmpVec2A: Phaser.Math.Vector2](#_tmpvec2a-phasermathvector2)
  + [\_tmpVec2B](#_tmpvec2b)

    - [\_tmpVec2B: Phaser.Math.Vector2](#_tmpvec2b-phasermathvector2)
* [Public Methods](#public-methods)

  + [draw](#draw)

    - [<instance> draw(graphics, [pointsTotal])](#instance-drawgraphics-pointstotal)
  + [getBounds](#getbounds)

    - [<instance> getBounds([out], [accuracy])](#instance-getboundsout-accuracy)
  + [getDistancePoints](#getdistancepoints)

    - [<instance> getDistancePoints(distance)](#instance-getdistancepointsdistance)
  + [getEndPoint](#getendpoint)

    - [<instance> getEndPoint([out])](#instance-getendpointout)
  + [getLength](#getlength)

    - [<instance> getLength()](#instance-getlength)
  + [getLengths](#getlengths)

    - [<instance> getLengths([divisions])](#instance-getlengthsdivisions)
  + [getPointAt](#getpointat)

    - [<instance> getPointAt(u, [out])](#instance-getpointatu-out)
  + [getPoints](#getpoints)

    - [<instance> getPoints([divisions], [stepRate], [out])](#instance-getpointsdivisions-steprate-out)
  + [getRandomPoint](#getrandompoint)

    - [<instance> getRandomPoint([out])](#instance-getrandompointout)
  + [getSpacedPoints](#getspacedpoints)

    - [<instance> getSpacedPoints([divisions], [stepRate], [out])](#instance-getspacedpointsdivisions-steprate-out)
  + [getStartPoint](#getstartpoint)

    - [<instance> getStartPoint([out])](#instance-getstartpointout)
  + [getTangent](#gettangent)

    - [<instance> getTangent(t, [out])](#instance-gettangentt-out)
  + [getTangentAt](#gettangentat)

    - [<instance> getTangentAt(u, [out])](#instance-gettangentatu-out)
  + [getTFromDistance](#gettfromdistance)

    - [<instance> getTFromDistance(distance, [divisions])](#instance-gettfromdistancedistance-divisions)
  + [getUtoTmapping](#getutotmapping)

    - [<instance> getUtoTmapping(u, distance, [divisions])](#instance-getutotmappingu-distance-divisions)
  + [updateArcLengths](#updatearclengths)

    - [<instance> updateArcLengths()](#instance-updatearclengths)

Back to top

©2025[Phaser](https://docs.phaser.io)



Curve