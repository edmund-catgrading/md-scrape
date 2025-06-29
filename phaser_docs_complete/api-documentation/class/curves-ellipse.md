# Ellipse

Phaser.Curves.Ellipse

An Elliptical Curve derived from the Base Curve class.

See <https://en.wikipedia.org/wiki/Elliptic_curve> for more details.

**Constructor**

`new Ellipse([x], [y], [xRadius], [yRadius], [startAngle], [endAngle], [clockwise], [rotation])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | [Phaser.Types.Curves.EllipseCurveConfig](../typedef/types-curves.md) | Yes | 0 | The x coordinate of the ellipse, or an Ellipse Curve configuration object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y coordinate of the ellipse. |
| xRadius | number | Yes | 0 | The horizontal radius of ellipse. |
| yRadius | number | Yes | 0 | The vertical radius of ellipse. |
| startAngle | number | Yes | 0 | The start angle of the ellipse, in degrees. |
| endAngle | number | Yes | 360 | The end angle of the ellipse, in degrees. |
| clockwise | boolean | Yes | false | Whether the ellipse angles are given as clockwise (`true`) or counter-clockwise (`false`). |
| rotation | number | Yes | 0 | The rotation of the ellipse, in degrees. |

---

**Scope**: static

**Extends**

> [Phaser.Curves.Curve](curves-curve.md)

> Source: [src/curves/EllipseCurve.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L16)  
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

## angle

### angle: number

**Description:**

The rotation of the ellipse, relative to the center, in degrees.

> Source: [src/curves/EllipseCurve.js#L536](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L536)  
> Since: 3.14.0

---

## arcLengthDivisions

### arcLengthDivisions: number

**Description:**

The quantity of arc length divisions within the curve.

**Inherits:** [Phaser.Curves.Curve#arcLengthDivisions](curves-curve.md)

> Source: [src/curves/Curve.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L50)  
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

## clockwise

### clockwise: boolean

**Description:**

`true` if the ellipse rotation is clockwise or `false` if anti-clockwise.

> Source: [src/curves/EllipseCurve.js#L515](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L515)  
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

## endAngle

### endAngle: number

**Description:**

The end angle of the ellipse in degrees.

> Source: [src/curves/EllipseCurve.js#L494](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L494)  
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

The center point of the ellipse. Used for calculating rotation.

> Source: [src/curves/EllipseCurve.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L71)  
> Since: 3.0.0

---

## rotation

### rotation: number

**Description:**

The rotation of the ellipse, relative to the center, in radians.

> Source: [src/curves/EllipseCurve.js#L557](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L557)  
> Since: 3.0.0

---

## startAngle

### startAngle: number

**Description:**

The start angle of the ellipse in degrees.

> Source: [src/curves/EllipseCurve.js#L473](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L473)  
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

## x

### x: number

**Description:**

The x coordinate of the center of the ellipse.

> Source: [src/curves/EllipseCurve.js#L389](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L389)  
> Since: 3.0.0

---

## xRadius

### xRadius: number

**Description:**

The horizontal radius of the ellipse.

> Source: [src/curves/EllipseCurve.js#L431](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L431)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y coordinate of the center of the ellipse.

> Source: [src/curves/EllipseCurve.js#L410](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L410)  
> Since: 3.0.0

---

## yRadius

### yRadius: number

**Description:**

The vertical radius of the ellipse.

> Source: [src/curves/EllipseCurve.js#L452](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L452)  
> Since: 3.0.0

---

# Private Members

## \_clockwise

### \_clockwise: boolean

**Description:**

Anti-clockwise direction.

**Access:** private

> Source: [src/curves/EllipseCurve.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L122)  
> Since: 3.0.0

---

## \_endAngle

### \_endAngle: number

**Description:**

The end angle of the ellipse in radians.

**Access:** private

> Source: [src/curves/EllipseCurve.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L112)  
> Since: 3.0.0

---

## \_rotation

### \_rotation: number

**Description:**

The rotation of the arc.

**Access:** private

> Source: [src/curves/EllipseCurve.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L132)  
> Since: 3.0.0

---

## \_startAngle

### \_startAngle: number

**Description:**

The starting angle of the ellipse in radians.

**Access:** private

> Source: [src/curves/EllipseCurve.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L102)  
> Since: 3.0.0

---

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

## \_xRadius

### \_xRadius: number

**Description:**

The horizontal radius of the ellipse.

**Access:** private

> Source: [src/curves/EllipseCurve.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L80)  
> Since: 3.0.0

---

## \_yRadius

### \_yRadius: number

**Description:**

The vertical radius of the ellipse.

**Access:** private

> Source: [src/curves/EllipseCurve.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L90)  
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

**Inherits:** [Phaser.Curves.Curve#draw](curves-curve.md)

> Source: [src/curves/Curve.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L111)  
> Since: 3.0.0

---

## fromJSON

### <static> fromJSON(data)

**Description:**

Creates a curve from the provided Ellipse Curve Configuration object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | [Phaser.Types.Curves.JSONEllipseCurve](../typedef/types-curves.md) | No | The JSON object containing this curve data. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Ellipse](curves-ellipse.md) - The ellipse curve constructed from the configuration object.

> Source: [src/curves/EllipseCurve.js#L603](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L603)  
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

**Inherits:** [Phaser.Curves.Curve#getBounds](curves-curve.md)

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

> Source: [src/curves/EllipseCurve.js#L177](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L177)  
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

**Inherits:** [Phaser.Curves.Curve#getPointAt](curves-curve.md)

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

### <instance> getResolution(divisions)

**Description:**

Get the resolution of the curve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| divisions | number | No | Optional divisions value. |
| --- | --- | --- | --- |

**Returns:** number - The curve resolution.

> Source: [src/curves/EllipseCurve.js#L162](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L162)  
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

> Source: [src/curves/EllipseCurve.js#L143](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L143)  
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

**Inherits:** [Phaser.Curves.Curve#getTangent](curves-curve.md)

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

**Returns:** number - The equidistant value.

**Inherits:** [Phaser.Curves.Curve#getUtoTmapping](curves-curve.md)

> Source: [src/curves/Curve.js#L513](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/Curve.js#L513)  
> Since: 3.0.0

---

## setClockwise

### <instance> setClockwise(value)

**Description:**

Sets if this curve extends clockwise or anti-clockwise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The clockwise state of this curve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Ellipse](curves-ellipse.md) - This curve object.

> Source: [src/curves/EllipseCurve.js#L355](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L355)  
> Since: 3.0.0

---

## setEndAngle

### <instance> setEndAngle(value)

**Description:**

Sets the end angle of this curve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The end angle of this curve, in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Ellipse](curves-ellipse.md) - This curve object.

> Source: [src/curves/EllipseCurve.js#L338](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L338)  
> Since: 3.0.0

---

## setHeight

### <instance> setHeight(value)

**Description:**

Sets the height of this curve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The height of this curve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Ellipse](curves-ellipse.md) - This curve object.

> Source: [src/curves/EllipseCurve.js#L304](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L304)  
> Since: 3.0.0

---

## setRotation

### <instance> setRotation(value)

**Description:**

Sets the rotation of this curve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The rotation of this curve, in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Ellipse](curves-ellipse.md) - This curve object.

> Source: [src/curves/EllipseCurve.js#L372](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L372)  
> Since: 3.0.0

---

## setStartAngle

### <instance> setStartAngle(value)

**Description:**

Sets the start angle of this curve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The start angle of this curve, in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Ellipse](curves-ellipse.md) - This curve object.

> Source: [src/curves/EllipseCurve.js#L321](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L321)  
> Since: 3.0.0

---

## setWidth

### <instance> setWidth(value)

**Description:**

Sets the width of this curve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The width of this curve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Ellipse](curves-ellipse.md) - This curve object.

> Source: [src/curves/EllipseCurve.js#L287](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L287)  
> Since: 3.0.0

---

## setXRadius

### <instance> setXRadius(value)

**Description:**

Sets the horizontal radius of this curve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The horizontal radius of this curve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Ellipse](curves-ellipse.md) - This curve object.

> Source: [src/curves/EllipseCurve.js#L253](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L253)  
> Since: 3.0.0

---

## setYRadius

### <instance> setYRadius(value)

**Description:**

Sets the vertical radius of this curve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The vertical radius of this curve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Ellipse](curves-ellipse.md) - This curve object.

> Source: [src/curves/EllipseCurve.js#L270](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L270)  
> Since: 3.0.0

---

## toJSON

### <instance> toJSON()

**Description:**

JSON serialization of the curve.

**Returns:** [Phaser.Types.Curves.JSONEllipseCurve](../typedef/types-curves.md) - The JSON object containing this curve data.

> Source: [src/curves/EllipseCurve.js#L578](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/EllipseCurve.js#L578)  
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
  + [angle](#angle)

    - [angle: number](#angle-number)
  + [arcLengthDivisions](#arclengthdivisions)

    - [arcLengthDivisions: number](#arclengthdivisions-number)
  + [cacheArcLengths](#cachearclengths)

    - [cacheArcLengths: Array.<number>](#cachearclengths-arraynumber)
  + [clockwise](#clockwise)

    - [clockwise: boolean](#clockwise-boolean)
  + [defaultDivisions](#defaultdivisions)

    - [defaultDivisions: number](#defaultdivisions-number)
  + [endAngle](#endangle)

    - [endAngle: number](#endangle-number)
  + [needsUpdate](#needsupdate)

    - [needsUpdate: boolean](#needsupdate-boolean)
  + [p0](#p0)

    - [p0: Phaser.Math.Vector2](#p0-phasermathvector2)
  + [rotation](#rotation)

    - [rotation: number](#rotation-number)
  + [startAngle](#startangle)

    - [startAngle: number](#startangle-number)
  + [type](#type)

    - [type: string](#type-string)
  + [x](#x)

    - [x: number](#x-number)
  + [xRadius](#xradius)

    - [xRadius: number](#xradius-number)
  + [y](#y)

    - [y: number](#y-number)
  + [yRadius](#yradius)

    - [yRadius: number](#yradius-number)
* [Private Members](#private-members)

  + [\_clockwise](#_clockwise)

    - [\_clockwise: boolean](#_clockwise-boolean)
  + [\_endAngle](#_endangle)

    - [\_endAngle: number](#_endangle-number)
  + [\_rotation](#_rotation)

    - [\_rotation: number](#_rotation-number)
  + [\_startAngle](#_startangle)

    - [\_startAngle: number](#_startangle-number)
  + [\_tmpVec2A](#_tmpvec2a)

    - [\_tmpVec2A: Phaser.Math.Vector2](#_tmpvec2a-phasermathvector2)
  + [\_tmpVec2B](#_tmpvec2b)

    - [\_tmpVec2B: Phaser.Math.Vector2](#_tmpvec2b-phasermathvector2)
  + [\_xRadius](#_xradius)

    - [\_xRadius: number](#_xradius-number)
  + [\_yRadius](#_yradius)

    - [\_yRadius: number](#_yradius-number)
* [Public Methods](#public-methods)

  + [draw](#draw)

    - [<instance> draw(graphics, [pointsTotal])](#instance-drawgraphics-pointstotal)
  + [fromJSON](#fromjson)

    - [<static> fromJSON(data)](#static-fromjsondata)
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
  + [getPoint](#getpoint)

    - [<instance> getPoint(t, [out])](#instance-getpointt-out)
  + [getPointAt](#getpointat)

    - [<instance> getPointAt(u, [out])](#instance-getpointatu-out)
  + [getPoints](#getpoints)

    - [<instance> getPoints([divisions], [stepRate], [out])](#instance-getpointsdivisions-steprate-out)
  + [getRandomPoint](#getrandompoint)

    - [<instance> getRandomPoint([out])](#instance-getrandompointout)
  + [getResolution](#getresolution)

    - [<instance> getResolution(divisions)](#instance-getresolutiondivisions)
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
  + [setClockwise](#setclockwise)

    - [<instance> setClockwise(value)](#instance-setclockwisevalue)
  + [setEndAngle](#setendangle)

    - [<instance> setEndAngle(value)](#instance-setendanglevalue)
  + [setHeight](#setheight)

    - [<instance> setHeight(value)](#instance-setheightvalue)
  + [setRotation](#setrotation)

    - [<instance> setRotation(value)](#instance-setrotationvalue)
  + [setStartAngle](#setstartangle)

    - [<instance> setStartAngle(value)](#instance-setstartanglevalue)
  + [setWidth](#setwidth)

    - [<instance> setWidth(value)](#instance-setwidthvalue)
  + [setXRadius](#setxradius)

    - [<instance> setXRadius(value)](#instance-setxradiusvalue)
  + [setYRadius](#setyradius)

    - [<instance> setYRadius(value)](#instance-setyradiusvalue)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [updateArcLengths](#updatearclengths)

    - [<instance> updateArcLengths()](#instance-updatearclengths)

Back to top

©2025[Phaser](https://docs.phaser.io)