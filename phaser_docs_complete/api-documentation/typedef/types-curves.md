# Types.Curves

Phaser.Types.Curves

## EllipseCurveConfig

### <static> EllipseCurveConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x coordinate of the ellipse. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y coordinate of the ellipse. |
| xRadius | number | Yes | 0 | The horizontal radius of the ellipse. |
| yRadius | number | Yes | 0 | The vertical radius of the ellipse. |
| startAngle | number | Yes | 0 | The start angle of the ellipse, in degrees. |
| endAngle | number | Yes | 360 | The end angle of the ellipse, in degrees. |
| clockwise | boolean | Yes | false | Sets if the the ellipse rotation is clockwise (true) or anti-clockwise (false) |
| rotation | number | Yes | 0 | The rotation of the ellipse, in degrees. |

**Type**: object

**Member of**: Phaser.Types.Curves

> Source: [src/curves/typedefs/EllipseCurveConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/typedefs/EllipseCurveConfig.js#L1)

---

## JSONCurve

### <static> JSONCurve

| name | type | optional | description |
| --- | --- | --- | --- |
| type | string | No | The of the curve |
| --- | --- | --- | --- |
| points | Array.<number> | No | The arrays of points like `[x1, y1, x2, y2]` |

**Type**: object

**Member of**: Phaser.Types.Curves

> Source: [src/curves/typedefs/JSONCurve.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/typedefs/JSONCurve.js#L1)  
> Since: 3.0.0

---

## JSONEllipseCurve

### <static> JSONEllipseCurve

| name | type | optional | description |
| --- | --- | --- | --- |
| type | string | No | The of the curve. |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the ellipse. |
| y | number | No | The y coordinate of the ellipse. |
| xRadius | number | No | The horizontal radius of ellipse. |
| yRadius | number | No | The vertical radius of ellipse. |
| startAngle | number | No | The start angle of the ellipse, in degrees. |
| endAngle | number | No | The end angle of the ellipse, in degrees. |
| clockwise | boolean | No | Sets if the the ellipse rotation is clockwise (true) or anti-clockwise (false) |
| rotation | number | No | The rotation of ellipse, in degrees. |

**Type**: object

**Member of**: Phaser.Types.Curves

> Source: [src/curves/typedefs/JSONEllipseCurve.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/typedefs/JSONEllipseCurve.js#L1)  
> Since: 3.0.0

---

## JSONPath

### <static> JSONPath

| name | type | optional | description |
| --- | --- | --- | --- |
| type | string | No | The of the curve. |
| --- | --- | --- | --- |
| x | number | No | The X coordinate of the curve's starting point. |
| y | number | No | The Y coordinate of the path's starting point. |
| autoClose | boolean | No | The path is auto closed. |
| curves | Array.<[Phaser.Types.Curves.JSONCurve](types-curves.md)> | No | The list of the curves |

**Type**: object

**Member of**: Phaser.Types.Curves

> Source: [src/curves/typedefs/JSONPath.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/typedefs/JSONPath.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Curves](#typescurves)

  + [EllipseCurveConfig](#ellipsecurveconfig)

    - [<static> EllipseCurveConfig](#static-ellipsecurveconfig)
  + [JSONCurve](#jsoncurve)

    - [<static> JSONCurve](#static-jsoncurve)
  + [JSONEllipseCurve](#jsonellipsecurve)

    - [<static> JSONEllipseCurve](#static-jsonellipsecurve)
  + [JSONPath](#jsonpath)

    - [<static> JSONPath](#static-jsonpath)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Curves