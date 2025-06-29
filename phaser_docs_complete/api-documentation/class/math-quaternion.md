# Quaternion

Phaser.Math.Quaternion

A quaternion.

**Constructor**

`new Quaternion([x], [y], [z], [w])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x component. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y component. |
| z | number | Yes | 0 | The z component. |
| w | number | Yes | 1 | The w component. |

---

**Scope**: static

> Source: [src/math/Quaternion.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L27)  
> Since: 3.0.0

# Public Members

## onChangeCallback

### onChangeCallback: function

**Description:**

This callback is invoked, if set, each time a value in this quaternion is changed.

The callback is passed one argument, a reference to this quaternion.

> Source: [src/math/Quaternion.js#L87](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L87)  
> Since: 3.50.0

---

## w

### w: number

**Description:**

The w component of this Quaternion.

> Source: [src/math/Quaternion.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L166)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x component of this Quaternion.

> Source: [src/math/Quaternion.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L100)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y component of this Quaternion.

> Source: [src/math/Quaternion.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L122)  
> Since: 3.0.0

---

## z

### z: number

**Description:**

The z component of this Quaternion.

> Source: [src/math/Quaternion.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L144)  
> Since: 3.0.0

---

# Private Members

## \_w

### \_w: number

**Description:**

The w component of this Quaternion.

**Access:** private

> Source: [src/math/Quaternion.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L77)  
> Since: 3.50.0

---

## \_x

### \_x: number

**Description:**

The x component of this Quaternion.

**Access:** private

> Source: [src/math/Quaternion.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L47)  
> Since: 3.50.0

---

## \_y

### \_y: number

**Description:**

The y component of this Quaternion.

**Access:** private

> Source: [src/math/Quaternion.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L57)  
> Since: 3.50.0

---

## \_z

### \_z: number

**Description:**

The z component of this Quaternion.

**Access:** private

> Source: [src/math/Quaternion.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L67)  
> Since: 3.50.0

---

# Public Methods

## add

### <instance> add(v)

**Description:**

Add a given Quaternion or Vector to this Quaternion. Addition is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Quaternion](math-quaternion.md) | [Phaser.Math.Vector4](math-vector4.md) | No | The Quaternion or Vector to add to this Quaternion. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L244](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L244)  
> Since: 3.0.0

---

## calculateW

### <instance> calculateW()

**Description:**

Create a unit (or rotation) Quaternion from its x, y, and z components.

Sets the w component.

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L763](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L763)  
> Since: 3.0.0

---

## conjugate

### <instance> conjugate()

**Description:**

Convert this Quaternion into its conjugate.

Sets the x, y and z components.

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L652](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L652)  
> Since: 3.0.0

---

## copy

### <instance> copy(src)

**Description:**

Copy the components of a given Quaternion or Vector into this Quaternion.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Quaternion](math-quaternion.md) | [Phaser.Math.Vector4](math-vector4.md) | No | The Quaternion or Vector to copy the components from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L188](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L188)  
> Since: 3.0.0

---

## dot

### <instance> dot(v)

**Description:**

Calculate the dot product of this Quaternion and the given Quaternion or Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Quaternion](math-quaternion.md) | [Phaser.Math.Vector4](math-vector4.md) | No | The Quaternion or Vector to dot product with this Quaternion. |
| --- | --- | --- | --- |

**Returns:** number - The dot product of this Quaternion and the given Quaternion or Vector.

> Source: [src/math/Quaternion.js#L377](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L377)  
> Since: 3.0.0

---

## fromMat3

### <instance> fromMat3(mat)

**Description:**

Convert the given Matrix into this Quaternion.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix3](math-matrix3.md) | No | The Matrix to convert from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L968](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L968)  
> Since: 3.0.0

---

## identity

### <instance> identity()

**Description:**

Reset this Matrix to an identity (default) Quaternion.

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L495](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L495)  
> Since: 3.0.0

---

## invert

### <instance> invert()

**Description:**

Invert this Quaternion.

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L626](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L626)  
> Since: 3.0.0

---

## length

### <instance> length()

**Description:**

Calculate the length of this Quaternion.

**Returns:** number - The length of this Quaternion.

> Source: [src/math/Quaternion.js#L310](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L310)  
> Since: 3.0.0

---

## lengthSq

### <instance> lengthSq()

**Description:**

Calculate the length of this Quaternion squared.

**Returns:** number - The length of this Quaternion, squared.

> Source: [src/math/Quaternion.js#L328](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L328)  
> Since: 3.0.0

---

## lerp

### <instance> lerp(v, [t])

**Description:**

Linearly interpolate this Quaternion towards the given Quaternion or Vector.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | [Phaser.Math.Quaternion](math-quaternion.md) | [Phaser.Math.Vector4](math-vector4.md) | No |  | The Quaternion or Vector to interpolate towards. |
| --- | --- | --- | --- | --- |
| t | number | Yes | 0 | The percentage of interpolation. |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L392](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L392)  
> Since: 3.0.0

---

## multiply

### <instance> multiply(b)

**Description:**

Multiply this Quaternion by the given Quaternion or Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| b | [Phaser.Math.Quaternion](math-quaternion.md) | [Phaser.Math.Vector4](math-vector4.md) | No | The Quaternion or Vector to multiply this Quaternion by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L533](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L533)  
> Since: 3.0.0

---

## normalize

### <instance> normalize()

**Description:**

Normalize this Quaternion.

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L346](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L346)  
> Since: 3.0.0

---

## rotateX

### <instance> rotateX(rad)

**Description:**

Rotate this Quaternion on the X axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rad | number | No | The rotation angle in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L673](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L673)  
> Since: 3.0.0

---

## rotateY

### <instance> rotateY(rad)

**Description:**

Rotate this Quaternion on the Y axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rad | number | No | The rotation angle in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L703](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L703)  
> Since: 3.0.0

---

## rotateZ

### <instance> rotateZ(rad)

**Description:**

Rotate this Quaternion on the Z axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rad | number | No | The rotation angle in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L733](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L733)  
> Since: 3.0.0

---

## rotationTo

### <instance> rotationTo(a, b)

**Description:**

Rotates this Quaternion based on the two given vectors.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.Math.Vector3](math-vector3.md) | No | The transform rotation vector. |
| --- | --- | --- | --- |
| b | [Phaser.Math.Vector3](math-vector3.md) | No | The target rotation vector. |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L420](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L420)  
> Since: 3.0.0

---

## scale

### <instance> scale(scale)

**Description:**

Scale this Quaternion by the given value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scale | number | No | The value to scale this Quaternion by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L288](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L288)  
> Since: 3.0.0

---

## set

### <instance> set([x], [y], [z], [w], [update])

**Description:**

Set the components of this Quaternion and optionally call the `onChangeCallback`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | object | Yes | 0 | The x component, or an object containing x, y, z, and w components. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y component. |
| z | number | Yes | 0 | The z component. |
| w | number | Yes | 0 | The w component. |
| update | boolean | Yes | true | Call the `onChangeCallback`? |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L203](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L203)  
> Since: 3.0.0

---

## setAxes

### <instance> setAxes(view, right, up)

**Description:**

Set the axes of this Quaternion.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| view | [Phaser.Math.Vector3](math-vector3.md) | No | The view axis. |
| --- | --- | --- | --- |
| right | [Phaser.Math.Vector3](math-vector3.md) | No | The right axis. |
| up | [Phaser.Math.Vector3](math-vector3.md) | No | The upwards axis. |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L464](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L464)  
> Since: 3.0.0

---

## setAxisAngle

### <instance> setAxisAngle(axis, rad)

**Description:**

Set the axis angle of this Quaternion.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| axis | [Phaser.Math.Vector3](math-vector3.md) | No | The axis. |
| --- | --- | --- | --- |
| rad | number | No | The angle in radians. |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L508](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L508)  
> Since: 3.0.0

---

## setFromEuler

### <instance> setFromEuler(euler, [update])

**Description:**

Set this Quaternion from the given Euler, based on Euler order.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| euler | [Phaser.Math.Euler](math-euler.md) | No |  | The Euler to convert from. |
| --- | --- | --- | --- | --- |
| update | boolean | Yes | true | Run the `onChangeCallback`? |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L784](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L784)  
> Since: 3.50.0

---

## setFromRotationMatrix

### <instance> setFromRotationMatrix(mat4)

**Description:**

Sets the rotation of this Quaternion from the given Matrix4.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat4 | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to set the rotation from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L893](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L893)  
> Since: 3.50.0

---

## slerp

### <instance> slerp(b, t)

**Description:**

Smoothly linearly interpolate this Quaternion towards the given Quaternion or Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| b | [Phaser.Math.Quaternion](math-quaternion.md) | [Phaser.Math.Vector4](math-vector4.md) | No | The Quaternion or Vector to interpolate towards. |
| --- | --- | --- | --- |
| t | number | No | The percentage of interpolation. |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L563](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L563)  
> Since: 3.0.0

---

## subtract

### <instance> subtract(v)

**Description:**

Subtract a given Quaternion or Vector from this Quaternion. Subtraction is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Quaternion](math-quaternion.md) | [Phaser.Math.Vector4](math-vector4.md) | No | The Quaternion or Vector to subtract from this Quaternion. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Quaternion](math-quaternion.md) - This Quaternion.

> Source: [src/math/Quaternion.js#L266](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Quaternion.js#L266)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [onChangeCallback](#onchangecallback)

    - [onChangeCallback: function](#onchangecallback-function)
  + [w](#w)

    - [w: number](#w-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
  + [z](#z)

    - [z: number](#z-number)
* [Private Members](#private-members)

  + [\_w](#_w)

    - [\_w: number](#_w-number)
  + [\_x](#_x)

    - [\_x: number](#_x-number)
  + [\_y](#_y)

    - [\_y: number](#_y-number)
  + [\_z](#_z)

    - [\_z: number](#_z-number)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(v)](#instance-addv)
  + [calculateW](#calculatew)

    - [<instance> calculateW()](#instance-calculatew)
  + [conjugate](#conjugate)

    - [<instance> conjugate()](#instance-conjugate)
  + [copy](#copy)

    - [<instance> copy(src)](#instance-copysrc)
  + [dot](#dot)

    - [<instance> dot(v)](#instance-dotv)
  + [fromMat3](#frommat3)

    - [<instance> fromMat3(mat)](#instance-frommat3mat)
  + [identity](#identity)

    - [<instance> identity()](#instance-identity)
  + [invert](#invert)

    - [<instance> invert()](#instance-invert)
  + [length](#length)

    - [<instance> length()](#instance-length)
  + [lengthSq](#lengthsq)

    - [<instance> lengthSq()](#instance-lengthsq)
  + [lerp](#lerp)

    - [<instance> lerp(v, [t])](#instance-lerpv-t)
  + [multiply](#multiply)

    - [<instance> multiply(b)](#instance-multiplyb)
  + [normalize](#normalize)

    - [<instance> normalize()](#instance-normalize)
  + [rotateX](#rotatex)

    - [<instance> rotateX(rad)](#instance-rotatexrad)
  + [rotateY](#rotatey)

    - [<instance> rotateY(rad)](#instance-rotateyrad)
  + [rotateZ](#rotatez)

    - [<instance> rotateZ(rad)](#instance-rotatezrad)
  + [rotationTo](#rotationto)

    - [<instance> rotationTo(a, b)](#instance-rotationtoa-b)
  + [scale](#scale)

    - [<instance> scale(scale)](#instance-scalescale)
  + [set](#set)

    - [<instance> set([x], [y], [z], [w], [update])](#instance-setx-y-z-w-update)
  + [setAxes](#setaxes)

    - [<instance> setAxes(view, right, up)](#instance-setaxesview-right-up)
  + [setAxisAngle](#setaxisangle)

    - [<instance> setAxisAngle(axis, rad)](#instance-setaxisangleaxis-rad)
  + [setFromEuler](#setfromeuler)

    - [<instance> setFromEuler(euler, [update])](#instance-setfromeulereuler-update)
  + [setFromRotationMatrix](#setfromrotationmatrix)

    - [<instance> setFromRotationMatrix(mat4)](#instance-setfromrotationmatrixmat4)
  + [slerp](#slerp)

    - [<instance> slerp(b, t)](#instance-slerpb-t)
  + [subtract](#subtract)

    - [<instance> subtract(v)](#instance-subtractv)

Back to top

©2025[Phaser](https://docs.phaser.io)