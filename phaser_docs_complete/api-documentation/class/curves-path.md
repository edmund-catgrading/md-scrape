# Path

Phaser.Curves.Path

A Path combines multiple Curves into one continuous compound curve.

It does not matter how many Curves are in the Path or what type they are.

A Curve in a Path does not have to start where the previous Curve ends - that is to say, a Path does not

have to be an uninterrupted curve. Only the order of the Curves influences the actual points on the Path.

**Constructor**

`new Path([x], [y])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The X coordinate of the Path's starting point or a {@link Phaser.Types.Curves.JSONPath}. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The Y coordinate of the Path's starting point. |

---

**Scope**: static

> Source: [src/curves/path/Path.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L21)  
> Since: 3.0.0

# Public Members

## autoClose

### autoClose: boolean

**Description:**

Automatically closes the path.

> Source: [src/curves/path/Path.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L89)  
> Since: 3.0.0

---

## cacheLengths

### cacheLengths: Array.<number>

**Description:**

The cached length of each Curve in the Path.

Used internally by <#getCurveLengths>.

> Source: [src/curves/path/Path.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L77)  
> Since: 3.0.0

---

## curves

### curves: Array.<[Phaser.Curves.Curve](curves-curve.md)>

**Description:**

The list of Curves which make up this Path.

> Source: [src/curves/path/Path.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L67)  
> Since: 3.0.0

---

## defaultDivisions

### defaultDivisions: number

**Description:**

The default number of divisions within a curve.

> Source: [src/curves/path/Path.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L57)  
> Since: 3.70.0

---

## name

### name: string

**Description:**

The name of this Path.

Empty by default and never populated by Phaser, this is left for developers to use.

> Source: [src/curves/path/Path.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L46)  
> Since: 3.0.0

---

## startPoint

### startPoint: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The starting point of the Path.

This is not necessarily equivalent to the starting point of the first Curve in the Path. In an empty Path, it's also treated as the ending point.

> Source: [src/curves/path/Path.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L99)  
> Since: 3.0.0

---

# Private Members

## \_tmpVec2A

### \_tmpVec2A: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A temporary vector used to avoid object creation when adding a Curve to the Path.

**Access:** private

> Source: [src/curves/path/Path.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L110)  
> Since: 3.0.0

---

## \_tmpVec2B

### \_tmpVec2B: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A temporary vector used to avoid object creation when adding a Curve to the Path.

**Access:** private

> Source: [src/curves/path/Path.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L120)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(curve)

**Description:**

Appends a Curve to the end of the Path.

The Curve does not have to start where the Path ends or, for an empty Path, at its defined starting point.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| curve | [Phaser.Curves.Curve](curves-curve.md) | No | The Curve to append. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Path](curves-path.md) - This Path object.

> Source: [src/curves/path/Path.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L140)  
> Since: 3.0.0

---

## circleTo

### <instance> circleTo(radius, [clockwise], [rotation])

**Description:**

Creates a circular Ellipse Curve positioned at the end of the Path.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radius | number | No |  | The radius of the circle. |
| --- | --- | --- | --- | --- |
| clockwise | boolean | Yes | false | `true` to create a clockwise circle as opposed to a counter-clockwise circle. |
| rotation | number | Yes | 0 | The rotation of the circle in degrees. |

**Returns:** [Phaser.Curves.Path](curves-path.md) - This Path object.

> Source: [src/curves/path/Path.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L159)  
> Since: 3.0.0

---

## closePath

### <instance> closePath()

**Description:**

Ensures that the Path is closed.

A closed Path starts and ends at the same point. If the Path is not closed, a straight Line Curve will be created from the ending point directly to the starting point. During the check, the actual starting point of the Path, i.e. the starting point of the first Curve, will be used as opposed to the Path's defined [startPoint](startPoint.md), which could differ.

Calling this method on an empty Path will result in an error.

**Returns:** [Phaser.Curves.Path](curves-path.md) - This Path object.

> Source: [src/curves/path/Path.js#L178](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L178)  
> Since: 3.0.0

---

## cubicBezierTo

### <instance> cubicBezierTo(x, y, control1X, [control1Y], [control2X], [control2Y])

**Description:**

Creates a cubic bezier curve starting at the previous end point and ending at p3, using p1 and p2 as control points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | [Phaser.Math.Vector2](math-vector2.md) | No | The x coordinate of the end point. Or, if a Vector2, the p1 value. |
| --- | --- | --- | --- |
| y | number | [Phaser.Math.Vector2](math-vector2.md) | No | The y coordinate of the end point. Or, if a Vector2, the p2 value. |
| control1X | number | [Phaser.Math.Vector2](math-vector2.md) | No | The x coordinate of the first control point. Or, if a Vector2, the p3 value. |
| control1Y | number | Yes | The y coordinate of the first control point. Not used if Vector2s are provided as the first 3 arguments. |
| control2X | number | Yes | The x coordinate of the second control point. Not used if Vector2s are provided as the first 3 arguments. |
| control2Y | number | Yes | The y coordinate of the second control point. Not used if Vector2s are provided as the first 3 arguments. |

**Returns:** [Phaser.Curves.Path](curves-path.md) - This Path object.

> Source: [src/curves/path/Path.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L205)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Disposes of this Path, clearing its internal references to objects so they can be garbage-collected.

> Source: [src/curves/path/Path.js#L892](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L892)  
> Since: 3.0.0

---

## draw

### <instance> draw(graphics, [pointsTotal])

**Description:**

Draws all Curves in the Path to a Graphics Game Object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No |  | The Graphics Game Object to draw to. |
| --- | --- | --- | --- | --- |
| pointsTotal | number | Yes | 32 | The number of points to draw for each Curve. Higher numbers result in a smoother curve but require more processing. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - The Graphics object which was drawn to.

> Source: [src/curves/path/Path.js#L280](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L280)  
> Since: 3.0.0

---

## ellipseTo

### <instance> ellipseTo([xRadius], [yRadius], [startAngle], [endAngle], [clockwise], [rotation])

**Description:**

Creates an ellipse curve positioned at the previous end point, using the given parameters.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| xRadius | number | Yes | 0 | The horizontal radius of ellipse. |
| --- | --- | --- | --- | --- |
| yRadius | number | Yes | 0 | The vertical radius of ellipse. |
| startAngle | number | Yes | 0 | The start angle of the ellipse, in degrees. |
| endAngle | number | Yes | 360 | The end angle of the ellipse, in degrees. |
| clockwise | boolean | Yes | false | Whether the ellipse angles are given as clockwise (`true`) or counter-clockwise (`false`). |
| rotation | number | Yes | 0 | The rotation of the ellipse, in degrees. |

**Returns:** [Phaser.Curves.Path](curves-path.md) - This Path object.

> Source: [src/curves/path/Path.js#L310](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L310)  
> Since: 3.0.0

---

## fromJSON

### <instance> fromJSON(data)

**Description:**

Creates a Path from a Path Configuration object.

The provided object should be a [Phaser.Types.Curves.JSONPath](../typedef/types-curves.md), as returned by <#toJSON>. Providing a malformed object may cause errors.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | [Phaser.Types.Curves.JSONPath](../typedef/types-curves.md) | No | The JSON object containing the Path data. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Path](curves-path.md) - This Path object.

> Source: [src/curves/path/Path.js#L342](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L342)  
> Since: 3.0.0

---

## getBounds

### <instance> getBounds([out], [accuracy])

**Description:**

Returns a Rectangle with a position and size matching the bounds of this Path.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes |  | The Rectangle to store the bounds in. |
| --- | --- | --- | --- | --- |
| accuracy | number | Yes | 16 | The accuracy of the bounds calculations. Higher values are more accurate at the cost of calculation speed. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The modified `out` Rectangle, or a new Rectangle if none was provided.

> Source: [src/curves/path/Path.js#L396](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L396)  
> Since: 3.0.0

---

## getCurveAt

### <instance> getCurveAt(t)

**Description:**

Returns the Curve that forms the Path at the given normalized location (between 0 and 1).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | No | The normalized location on the Path, between 0 and 1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Curve](curves-curve.md) - The Curve that is part of this Path at a given location, or `null` if no curve was found.

> Source: [src/curves/path/Path.js#L482](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L482)  
> Since: 3.60.0

---

## getCurveLengths

### <instance> getCurveLengths()

**Description:**

Returns an array containing the length of the Path at the end of each Curve.

The result of this method will be cached to avoid recalculating it in subsequent calls. The cache is only invalidated when the <#curves> array changes in length, leading to potential inaccuracies if a Curve in the Path is changed, or if a Curve is removed and another is added in its place.

**Returns:** Array.<number> - An array containing the length of the Path at the end of each one of its Curves.

> Source: [src/curves/path/Path.js#L445](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L445)  
> Since: 3.0.0

---

## getEndPoint

### <instance> getEndPoint([out])

**Description:**

Returns the ending point of the Path.

A Path's ending point is equivalent to the ending point of the last Curve in the Path. For an empty Path, the ending point is at the Path's defined <#startPoint>.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | The object to store the point in. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The modified `out` object, or a new Vector2 if none was provided.

> Source: [src/curves/path/Path.js#L511](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L511)  
> Since: 3.0.0

---

## getLength

### <instance> getLength()

**Description:**

Returns the total length of the Path.

**Returns:** number - The total length of the Path.

> Source: [src/curves/path/Path.js#L541](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L541)  
> Since: 3.0.0

---

## getPoint

### <instance> getPoint(t, [out])

**Description:**

Calculates the coordinates of the point at the given normalized location (between 0 and 1) on the Path.

The location is relative to the entire Path, not to an individual Curve. A location of 0.5 is always in the middle of the Path and is thus an equal distance away from both its starting and ending points. In a Path with one Curve, it would be in the middle of the Curve; in a Path with two Curves, it could be anywhere on either one of them depending on their lengths.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | No | The location of the point to return, between 0 and 1. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | The object in which to store the calculated point. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The modified `out` object, or a new `Vector2` if none was provided.

> Source: [src/curves/path/Path.js#L567](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L567)  
> Since: 3.0.0

---

## getPoints

### <instance> getPoints([divisions], [stepRate])

**Description:**

Get a sequence of points on the path.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| divisions | number | Yes | The number of divisions to make per resolution per curve. |
| --- | --- | --- | --- |
| stepRate | number | Yes | The curve distance between points per curve, implying `divisions`. |

**Returns:** Array.<[Phaser.Math.Vector2](math-vector2.md)> - An array of Vector2 objects that containing the points along the Path.

> Source: [src/curves/path/Path.js#L610](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L610)  
> Since: 3.0.0

---

## getRandomPoint

### <instance> getRandomPoint([out])

**Description:**

Returns a randomly chosen point anywhere on the path. This follows the same rules as `getPoint` in that it may return a point on any Curve inside this path.

When calling this method multiple times, the points are not guaranteed to be equally spaced spatially.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | `Vector2` instance that should be used for storing the result. If `undefined` a new `Vector2` will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The modified `out` object, or a new `Vector2` if none was provided.

> Source: [src/curves/path/Path.js#L669](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L669)  
> Since: 3.0.0

---

## getSpacedPoints

### <instance> getSpacedPoints([divisions])

**Description:**

Divides this Path into a set of equally spaced points,

The resulting points are equally spaced with respect to the points' position on the path, but not necessarily equally spaced spatially.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| divisions | number | Yes | 40 | The amount of points to divide this Path into. |
| --- | --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Math.Vector2](math-vector2.md)> - A list of the points this path was subdivided into.

> Source: [src/curves/path/Path.js#L690](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L690)  
> Since: 3.0.0

---

## getStartPoint

### <instance> getStartPoint([out])

**Description:**

Returns the starting point of the Path.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | `Vector2` instance that should be used for storing the result. If `undefined` a new `Vector2` will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The modified `out` object, or a new Vector2 if none was provided.

> Source: [src/curves/path/Path.js#L721](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L721)  
> Since: 3.0.0

---

## getTangent

### <instance> getTangent(t, [out])

**Description:**

Gets a unit vector tangent at a relative position on the path.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| t | number | No | The relative position on the path, [0..1]. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Vector2](math-vector2.md) | Yes | A vector to store the result in. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - Vector approximating the tangent line at the point t (delta +/- 0.0001)

> Source: [src/curves/path/Path.js#L740](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L740)  
> Since: 3.23.0

---

## lineTo

### <instance> lineTo(x, [y])

**Description:**

Creates a line curve from the previous end point to x/y.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No |
| --- | --- | --- | --- |
| y | number | Yes | The Y coordinate of the line's end point, if a number was passed as the X parameter. |

**Returns:** [Phaser.Curves.Path](curves-path.md) - This Path object.

> Source: [src/curves/path/Path.js#L780](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L780)  
> Since: 3.0.0

---

## moveTo

### <instance> moveTo(x, [y])

**Description:**

Creates a "gap" in this path from the path's current end point to the given coordinates.

After calling this function, this Path's end point will be equal to the given coordinates

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No |
| --- | --- | --- | --- |
| y | number | Yes | The Y coordinate of the position to move the path's end point to, if a number was passed as the X coordinate. |

**Returns:** [Phaser.Curves.Path](curves-path.md) - This Path object.

> Source: [src/curves/path/Path.js#L828](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L828)  
> Since: 3.0.0

---

## quadraticBezierTo

### <instance> quadraticBezierTo(x, [y], [controlX], [controlY])

**Description:**

Creates a Quadratic Bezier Curve starting at the ending point of the Path.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | Array.<[Phaser.Math.Vector2](math-vector2.md)> | No | The X coordinate of the second control point or, if it's a `Vector2`, the first control point. |
| --- | --- | --- | --- |
| y | number | Yes | The Y coordinate of the second control point or, if `x` is a `Vector2`, the second control point. |
| controlX | number | Yes | If `x` is not a `Vector2`, the X coordinate of the first control point. |
| controlY | number | Yes | If `x` is not a `Vector2`, the Y coordinate of the first control point. |

**Returns:** [Phaser.Curves.Path](curves-path.md) - This Path object.

> Source: [src/curves/path/Path.js#L246](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L246)  
> Since: 3.2.0

---

## splineTo

### <instance> splineTo(points)

**Description:**

Creates a spline curve starting at the previous end point, using the given points on the curve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| points | Array.<[Phaser.Math.Vector2](math-vector2.md)> | No | The points the newly created spline curve should consist of. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Curves.Path](curves-path.md) - This Path object.

> Source: [src/curves/path/Path.js#L811](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L811)  
> Since: 3.0.0

---

## toJSON

### <instance> toJSON()

**Description:**

Converts this Path to a JSON object containing the path information and its constituent curves.

**Returns:** [Phaser.Types.Curves.JSONPath](../typedef/types-curves.md) - The JSON object containing this path's data.

> Source: [src/curves/path/Path.js#L853](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L853)  
> Since: 3.0.0

---

## updateArcLengths

### <instance> updateArcLengths()

**Description:**

cacheLengths must be recalculated.

> Source: [src/curves/path/Path.js#L879](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L879)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [autoClose](#autoclose)

    - [autoClose: boolean](#autoclose-boolean)
  + [cacheLengths](#cachelengths)

    - [cacheLengths: Array.<number>](#cachelengths-arraynumber)
  + [curves](#curves)

    - [curves: Array.<Phaser.Curves.Curve>](#curves-arrayphasercurvescurve)
  + [defaultDivisions](#defaultdivisions)

    - [defaultDivisions: number](#defaultdivisions-number)
  + [name](#name)

    - [name: string](#name-string)
  + [startPoint](#startpoint)

    - [startPoint: Phaser.Math.Vector2](#startpoint-phasermathvector2)
* [Private Members](#private-members)

  + [\_tmpVec2A](#_tmpvec2a)

    - [\_tmpVec2A: Phaser.Math.Vector2](#_tmpvec2a-phasermathvector2)
  + [\_tmpVec2B](#_tmpvec2b)

    - [\_tmpVec2B: Phaser.Math.Vector2](#_tmpvec2b-phasermathvector2)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(curve)](#instance-addcurve)
  + [circleTo](#circleto)

    - [<instance> circleTo(radius, [clockwise], [rotation])](#instance-circletoradius-clockwise-rotation)
  + [closePath](#closepath)

    - [<instance> closePath()](#instance-closepath)
  + [cubicBezierTo](#cubicbezierto)

    - [<instance> cubicBezierTo(x, y, control1X, [control1Y], [control2X], [control2Y])](#instance-cubicbeziertox-y-control1x-control1y-control2x-control2y)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [draw](#draw)

    - [<instance> draw(graphics, [pointsTotal])](#instance-drawgraphics-pointstotal)
  + [ellipseTo](#ellipseto)

    - [<instance> ellipseTo([xRadius], [yRadius], [startAngle], [endAngle], [clockwise], [rotation])](#instance-ellipsetoxradius-yradius-startangle-endangle-clockwise-rotation)
  + [fromJSON](#fromjson)

    - [<instance> fromJSON(data)](#instance-fromjsondata)
  + [getBounds](#getbounds)

    - [<instance> getBounds([out], [accuracy])](#instance-getboundsout-accuracy)
  + [getCurveAt](#getcurveat)

    - [<instance> getCurveAt(t)](#instance-getcurveatt)
  + [getCurveLengths](#getcurvelengths)

    - [<instance> getCurveLengths()](#instance-getcurvelengths)
  + [getEndPoint](#getendpoint)

    - [<instance> getEndPoint([out])](#instance-getendpointout)
  + [getLength](#getlength)

    - [<instance> getLength()](#instance-getlength)
  + [getPoint](#getpoint)

    - [<instance> getPoint(t, [out])](#instance-getpointt-out)
  + [getPoints](#getpoints)

    - [<instance> getPoints([divisions], [stepRate])](#instance-getpointsdivisions-steprate)
  + [getRandomPoint](#getrandompoint)

    - [<instance> getRandomPoint([out])](#instance-getrandompointout)
  + [getSpacedPoints](#getspacedpoints)

    - [<instance> getSpacedPoints([divisions])](#instance-getspacedpointsdivisions)
  + [getStartPoint](#getstartpoint)

    - [<instance> getStartPoint([out])](#instance-getstartpointout)
  + [getTangent](#gettangent)

    - [<instance> getTangent(t, [out])](#instance-gettangentt-out)
  + [lineTo](#lineto)

    - [<instance> lineTo(x, [y])](#instance-linetox-y)
  + [moveTo](#moveto)

    - [<instance> moveTo(x, [y])](#instance-movetox-y)
  + [quadraticBezierTo](#quadraticbezierto)

    - [<instance> quadraticBezierTo(x, [y], [controlX], [controlY])](#instance-quadraticbeziertox-y-controlx-controly)
  + [splineTo](#splineto)

    - [<instance> splineTo(points)](#instance-splinetopoints)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [updateArcLengths](#updatearclengths)

    - [<instance> updateArcLengths()](#instance-updatearclengths)

Back to top

©2025[Phaser](https://docs.phaser.io)