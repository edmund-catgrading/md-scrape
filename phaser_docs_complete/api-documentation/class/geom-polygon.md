# Polygon

Phaser.Geom.Polygon

A Polygon object

The polygon is a closed shape consists of a series of connected straight lines defined by list of ordered points.

Several formats are supported to define the list of points, check the setTo method for details.

This is a geometry object allowing you to define and inspect the shape.

It is not a Game Object, in that you cannot add it to the display list, and it has no texture.

To render a Polygon you should look at the capabilities of the Graphics class.

**Constructor**

`new Polygon([points])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| points | string | Array.<number> | Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> | Yes |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/geom/polygon/Polygon.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Polygon.js#L12)  
> Since: 3.0.0

# Public Methods

## calculateArea

### <instance> calculateArea()

**Description:**

Calculates the area of the Polygon. This is available in the property Polygon.area

**Returns:** number - The area of the polygon.

> Source: [src/geom/polygon/Polygon.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Polygon.js#L160)  
> Since: 3.0.0

---

## Clone

### <static> Clone(polygon)

**Description:**

Create a new polygon which is a copy of the specified polygon

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No | The polygon to create a clone of |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Polygon](geom-polygon.md) - A new separate Polygon cloned from the specified polygon, based on the same points.

> Source: [src/geom/polygon/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Clone.js#L9)  
> Since: 3.0.0

---

## contains

### <instance> contains(x, y)

**Description:**

Check to see if the Polygon contains the given x / y coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to check within the polygon. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate to check within the polygon. |

**Returns:** boolean - `true` if the coordinates are within the polygon, otherwise `false`.

> Source: [src/geom/polygon/Polygon.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Polygon.js#L76)  
> Since: 3.0.0

---

## Contains

### <static> Contains(polygon, x, y)

**Description:**

Checks if a point is within the bounds of a Polygon.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No | The Polygon to check against. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the point to check. |
| y | number | No | The Y coordinate of the point to check. |

**Returns:** boolean - `true` if the point is within the bounds of the Polygon, otherwise `false`.

> Source: [src/geom/polygon/Contains.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Contains.js#L10)  
> Since: 3.0.0

---

## ContainsPoint

### <static> ContainsPoint(polygon, point)

**Description:**

Checks the given Point again the Polygon to see if the Point lays within its vertices.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No | The Polygon to check. |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | No | The Point to check if it's within the Polygon. |

**Returns:** boolean - `true` if the Point is within the Polygon, otherwise `false`.

> Source: [src/geom/polygon/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/ContainsPoint.js#L9)  
> Since: 3.0.0

---

## Earcut

### <static> Earcut(data, [holeIndices], [dimensions])

**Description:**

This module implements a modified ear slicing algorithm, optimized by z-order curve hashing and extended to

handle holes, twisted polygons, degeneracies and self-intersections in a way that doesn't guarantee correctness

of triangulation, but attempts to always produce acceptable results for practical data.

Example:

```
Copy
const triangles = Phaser.Geom.Polygon.Earcut([10,0, 0,50, 60,60, 70,10]); // returns [1,0,3, 3,2,1]


```

Each group of three vertex indices in the resulting array forms a triangle.

```
Copy
// triangulating a polygon with a hole

earcut([0,0, 100,0, 100,100, 0,100,  20,20, 80,20, 80,80, 20,80], [4]);

// [3,0,4, 5,4,0, 3,4,7, 5,0,1, 2,3,7, 6,5,1, 2,7,6, 6,1,2]



// triangulating a polygon with 3d coords

earcut([10,0,1, 0,50,2, 60,60,3, 70,10,4], null, 3);

// [1,0,3, 3,2,1]


```

If you pass a single vertex as a hole, Earcut treats it as a Steiner point.

If your input is a multi-dimensional array (e.g. GeoJSON Polygon), you can convert it to the format

expected by Earcut with `Phaser.Geom.Polygon.Earcut.flatten`:

```
Copy
var data = earcut.flatten(geojson.geometry.coordinates);

var triangles = earcut(data.vertices, data.holes, data.dimensions);


```

After getting a triangulation, you can verify its correctness with `Phaser.Geom.Polygon.Earcut.deviation`:

```
Copy
var deviation = earcut.deviation(vertices, holes, dimensions, triangles);


```

Returns the relative difference between the total area of triangles and the area of the input polygon.

0 means the triangulation is fully correct.

For more information see <https://github.com/mapbox/earcut>

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | Array.<number> | No |  | A flat array of vertex coordinate, like [x0,y0, x1,y1, x2,y2, ...] |
| --- | --- | --- | --- | --- |
| holeIndices | Array.<number> | Yes |  | An array of hole indices if any (e.g. [5, 8] for a 12-vertex input would mean one hole with vertices 5–7 and another with 8–11). |
| dimensions | number | Yes | 2 | The number of coordinates per vertex in the input array (2 by default). |

**Returns:** Array.<number> - An array of triangulated data.

> Source: [src/geom/polygon/Earcut.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Earcut.js#L7)  
> Since: 3.50.0

---

## GetAABB

### <static> GetAABB(polygon, [out])

**Description:**

Calculates the bounding AABB rectangle of a polygon.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No | The polygon that should be calculated. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | object | Yes | The rectangle or object that has x, y, width, and height properties to store the result. Optional. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md), object - The resulting rectangle or object that is passed in with position and dimensions of the polygon's AABB.

> Source: [src/geom/polygon/GetAABB.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/GetAABB.js#L9)  
> Since: 3.0.0

---

## GetNumberArray

### <static> GetNumberArray(polygon, [output])

**Description:**

Stores all of the points of a Polygon into a flat array of numbers following the sequence [ x,y, x,y, x,y ],

i.e. each point of the Polygon, in the order it's defined, corresponds to two elements of the resultant

array for the point's X and Y coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No | The Polygon whose points to export. |
| --- | --- | --- | --- |
| output | array | Array.<number> | Yes | An array to which the points' coordinates should be appended. |

**Returns:** array, Array.<number> - The modified `output` array, or a new array if none was given.

> Source: [src/geom/polygon/GetNumberArray.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/GetNumberArray.js#L9)  
> Since: 3.0.0

---

## getPoints

### <instance> getPoints(quantity, [stepRate], [output])

**Description:**

Returns an array of Point objects containing the coordinates of the points around the perimeter of the Polygon,

based on the given quantity or stepRate values.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| quantity | number | No | The amount of points to return. If a falsey value the quantity will be derived from the `stepRate` instead. |
| --- | --- | --- | --- |
| stepRate | number | Yes | Sets the quantity by getting the perimeter of the Polygon and dividing it by the stepRate. |
| output | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An array to insert the points in to. If not provided a new array will be created. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Point objects pertaining to the points around the perimeter of the Polygon.

> Source: [src/geom/polygon/Polygon.js#L199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Polygon.js#L199)  
> Since: 3.12.0

---

## GetPoints

### <static> GetPoints(polygon, quantity, [stepRate], [output])

**Description:**

Returns an array of Point objects containing the coordinates of the points around the perimeter of the Polygon,

based on the given quantity or stepRate values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No | The Polygon to get the points from. |
| --- | --- | --- | --- |
| quantity | number | No | The amount of points to return. If a falsey value the quantity will be derived from the `stepRate` instead. |
| stepRate | number | Yes | Sets the quantity by getting the perimeter of the Polygon and dividing it by the stepRate. |
| output | array | Yes | An array to insert the points in to. If not provided a new array will be created. |

**Returns:** Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Point objects pertaining to the points around the perimeter of the Polygon.

> Source: [src/geom/polygon/GetPoints.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/GetPoints.js#L11)  
> Since: 3.12.0

---

## Perimeter

### <static> Perimeter(polygon)

**Description:**

Returns the perimeter of the given Polygon.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No | The Polygon to get the perimeter of. |
| --- | --- | --- | --- |

**Returns:** number - The perimeter of the Polygon.

> Source: [src/geom/polygon/Perimeter.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Perimeter.js#L10)  
> Since: 3.12.0

---

## Reverse

### <static> Reverse(polygon)

**Description:**

Reverses the order of the points of a Polygon.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No | The Polygon to modify. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Polygon](geom-polygon.md) - The modified Polygon.

> Source: [src/geom/polygon/Reverse.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Reverse.js#L7)  
> Since: 3.0.0

---

## setTo

### <instance> setTo([points])

**Description:**

Sets this Polygon to the given points.

The points can be set from a variety of formats:

* A string containing paired values separated by a single space: `'40 0 40 20 100 20 100 80 40 80 40 100 0 50'`
* An array of Point objects: `[new Phaser.Point(x1, y1), ...]`
* An array of objects with public x/y properties: `[obj1, obj2, ...]`
* An array of paired numbers that represent point coordinates: `[x1,y1, x2,y2, ...]`
* An array of arrays with two elements representing x/y coordinates: `[[x1, y1], [x2, y2], ...]`

`setTo` may also be called without any arguments to remove all points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| points | string | Array.<number> | Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> | Yes |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Polygon](geom-polygon.md) - This Polygon object.

> Source: [src/geom/polygon/Polygon.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Polygon.js#L92)  
> Since: 3.0.0

---

## Simplify

### <static> Simplify(polygon, [tolerance], [highestQuality])

**Description:**

Takes a Polygon object and simplifies the points by running them through a combination of

Douglas-Peucker and Radial Distance algorithms. Simplification dramatically reduces the number of

points in a polygon while retaining its shape, giving a huge performance boost when processing

it and also reducing visual noise.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No |  | The polygon to be simplified. The polygon will be modified in-place and returned. |
| --- | --- | --- | --- | --- |
| tolerance | number | Yes | 1 | Affects the amount of simplification (in the same metric as the point coordinates). |
| highestQuality | boolean | Yes | false | Excludes distance-based preprocessing step which leads to highest quality simplification but runs ~10-20 times slower. |

**Returns:** [Phaser.Geom.Polygon](geom-polygon.md) - The input polygon.

> Source: [src/geom/polygon/Simplify.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Simplify.js#L160)  
> Since: 3.50.0

---

## Smooth

### <static> Smooth(polygon)

**Description:**

Takes a Polygon object and applies Chaikin's smoothing algorithm on its points.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No | The polygon to be smoothed. The polygon will be modified in-place and returned. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Polygon](geom-polygon.md) - The input polygon.

> Source: [src/geom/polygon/Smooth.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Smooth.js#L19)  
> Since: 3.13.0

---

## Translate

### <static> Translate(polygon, x, y)

**Description:**

Tranlates the points of the given Polygon.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| polygon | [Phaser.Geom.Polygon](geom-polygon.md) | No | The Polygon to modify. |
| --- | --- | --- | --- |
| x | number | No | The amount to horizontally translate the points by. |
| y | number | No | The amount to vertically translate the points by. |

**Returns:** [Phaser.Geom.Polygon](geom-polygon.md) - The modified Polygon.

> Source: [src/geom/polygon/Translate.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Translate.js#L7)  
> Since: 3.50.0

---

# Public Members

## area

### area: number

**Description:**

The area of this Polygon.

> Source: [src/geom/polygon/Polygon.js#L51](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Polygon.js#L51)  
> Since: 3.0.0

---

## points

### points: Array.<[Phaser.Geom.Point](geom-point.md)>

**Description:**

An array of number pair objects that make up this polygon. I.e. [ {x,y}, {x,y}, {x,y} ]

> Source: [src/geom/polygon/Polygon.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Polygon.js#L61)  
> Since: 3.0.0

---

## type

### type: number

**Description:**

The geometry constant type of this object: `GEOM_CONST.POLYGON`.

Used for fast type comparisons.

> Source: [src/geom/polygon/Polygon.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/polygon/Polygon.js#L40)  
> Since: 3.19.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Methods](#public-methods)

  + [calculateArea](#calculatearea)

    - [<instance> calculateArea()](#instance-calculatearea)
  + [Clone](#clone)

    - [<static> Clone(polygon)](#static-clonepolygon)
  + [contains](#contains)

    - [<instance> contains(x, y)](#instance-containsx-y)
  + [Contains](#contains-1)

    - [<static> Contains(polygon, x, y)](#static-containspolygon-x-y)
  + [ContainsPoint](#containspoint)

    - [<static> ContainsPoint(polygon, point)](#static-containspointpolygon-point)
  + [Earcut](#earcut)

    - [<static> Earcut(data, [holeIndices], [dimensions])](#static-earcutdata-holeindices-dimensions)
  + [GetAABB](#getaabb)

    - [<static> GetAABB(polygon, [out])](#static-getaabbpolygon-out)
  + [GetNumberArray](#getnumberarray)

    - [<static> GetNumberArray(polygon, [output])](#static-getnumberarraypolygon-output)
  + [getPoints](#getpoints)

    - [<instance> getPoints(quantity, [stepRate], [output])](#instance-getpointsquantity-steprate-output)
  + [GetPoints](#getpoints-1)

    - [<static> GetPoints(polygon, quantity, [stepRate], [output])](#static-getpointspolygon-quantity-steprate-output)
  + [Perimeter](#perimeter)

    - [<static> Perimeter(polygon)](#static-perimeterpolygon)
  + [Reverse](#reverse)

    - [<static> Reverse(polygon)](#static-reversepolygon)
  + [setTo](#setto)

    - [<instance> setTo([points])](#instance-settopoints)
  + [Simplify](#simplify)

    - [<static> Simplify(polygon, [tolerance], [highestQuality])](#static-simplifypolygon-tolerance-highestquality)
  + [Smooth](#smooth)

    - [<static> Smooth(polygon)](#static-smoothpolygon)
  + [Translate](#translate)

    - [<static> Translate(polygon, x, y)](#static-translatepolygon-x-y)
* [Public Members](#public-members)

  + [area](#area)

    - [area: number](#area-number)
  + [points](#points)

    - [points: Array.<Phaser.Geom.Point>](#points-arrayphasergeompoint)
  + [type](#type)

    - [type: number](#type-number)

Back to top

©2025[Phaser](https://docs.phaser.io)