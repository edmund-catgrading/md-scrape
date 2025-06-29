# Vertex

Phaser.Geom.Mesh.Vertex

A Vertex Geometry Object.

This class consists of all the information required for a single vertex within a Face Geometry Object.

Faces, and thus Vertex objects, are used by the Mesh Game Object in order to render objects in WebGL.

**Constructor**

`new Vertex(x, y, z, u, v, [color], [alpha], [nx], [ny], [nz])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x position of the vertex. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y position of the vertex. |
| z | number | No |  | The z position of the vertex. |
| u | number | No |  | The UV u coordinate of the vertex. |
| v | number | No |  | The UV v coordinate of the vertex. |
| color | number | Yes | "0xffffff" | The color value of the vertex. |
| alpha | number | Yes | 1 | The alpha value of the vertex. |
| nx | number | Yes | 0 | The x normal value of the vertex. |
| ny | number | Yes | 0 | The y normal value of the vertex. |
| nz | number | Yes | 0 | The z normal value of the vertex. |

---

**Scope**: static

**Extends**

> [Phaser.Math.Vector3](math-vector3.md)

> Source: [src/geom/mesh/Vertex.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L11)  
> Since: 3.50.0

# Public Members

## alpha

### alpha: number

**Description:**

The alpha value of this vertex.

> Source: [src/geom/mesh/Vertex.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L133)  
> Since: 3.50.0

---

## color

### color: number

**Description:**

The color value of this vertex.

> Source: [src/geom/mesh/Vertex.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L124)  
> Since: 3.50.0

---

## nx

### nx: number

**Description:**

The normalized projected x coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L79)  
> Since: 3.50.0

---

## ny

### ny: number

**Description:**

The normalized projected y coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L88)  
> Since: 3.50.0

---

## nz

### nz: number

**Description:**

The normalized projected z coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L97)  
> Since: 3.50.0

---

## ta

### ta: number

**Description:**

The translated alpha value of this vertex.

> Source: [src/geom/mesh/Vertex.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L160)  
> Since: 3.50.0

---

## tu

### tu: number

**Description:**

The translated uv u coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L169)  
> Since: 3.60.0

---

## tv

### tv: number

**Description:**

The translated uv v coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L178](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L178)  
> Since: 3.60.0

---

## tx

### tx: number

**Description:**

The translated x coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L142](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L142)  
> Since: 3.50.0

---

## ty

### ty: number

**Description:**

The translated y coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L151)  
> Since: 3.50.0

---

## u

### u: number

**Description:**

UV u coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L106)  
> Since: 3.50.0

---

## v

### v: number

**Description:**

UV v coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L115)  
> Since: 3.50.0

---

## vx

### vx: number

**Description:**

The projected x coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L52)  
> Since: 3.50.0

---

## vy

### vy: number

**Description:**

The projected y coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L61)  
> Since: 3.50.0

---

## vz

### vz: number

**Description:**

The projected z coordinate of this vertex.

> Source: [src/geom/mesh/Vertex.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L70)  
> Since: 3.50.0

---

## x

### x: number

**Description:**

The x component of this Vector.

**Inherits:** [Phaser.Math.Vector3#x](math-vector3.md)

> Source: [src/math/Vector3.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L33)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y component of this Vector.

**Inherits:** [Phaser.Math.Vector3#y](math-vector3.md)

> Source: [src/math/Vector3.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L43)  
> Since: 3.0.0

---

## z

### z: number

**Description:**

The z component of this Vector.

**Inherits:** [Phaser.Math.Vector3#z](math-vector3.md)

> Source: [src/math/Vector3.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L53)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(v)

**Description:**

Add a given Vector to this Vector. Addition is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to add to this Vector. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#add](math-vector3.md)

> Source: [src/math/Vector3.js#L337](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L337)  
> Since: 3.0.0

---

## addScalar

### <instance> addScalar(s)

**Description:**

Add the given value to each component of this Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| s | number | No | The amount to add to this Vector. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#addScalar](math-vector3.md)

> Source: [src/math/Vector3.js#L356](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L356)  
> Since: 3.50.0

---

## addScale

### <instance> addScale(v, scale)

**Description:**

Add and scale a given Vector to this Vector. Addition is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to add to this Vector. |
| --- | --- | --- | --- |
| scale | number | No | The amount to scale `v` by. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#addScale](math-vector3.md)

> Source: [src/math/Vector3.js#L375](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L375)  
> Since: 3.50.0

---

## addVectors

### <instance> addVectors(a, b)

**Description:**

Adds the two given Vector3s and sets the results into this Vector3.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.Math.Vector3](math-vector3.md) | No | The first Vector to add. |
| --- | --- | --- | --- |
| b | [Phaser.Math.Vector3](math-vector3.md) | No | The second Vector to add. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#addVectors](math-vector3.md)

> Source: [src/math/Vector3.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L147)  
> Since: 3.50.0

---

## applyMatrix3

### <instance> applyMatrix3(mat3)

**Description:**

Takes a Matrix3 and applies it to this Vector3.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat3 | [Phaser.Math.Matrix3](math-matrix3.md) | No | The Matrix3 to apply to this Vector3. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#applyMatrix3](math-vector3.md)

> Source: [src/math/Vector3.js#L671](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L671)  
> Since: 3.50.0

---

## applyMatrix4

### <instance> applyMatrix4(mat4)

**Description:**

Takes a Matrix4 and applies it to this Vector3.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat4 | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to apply to this Vector3. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#applyMatrix4](math-vector3.md)

> Source: [src/math/Vector3.js#L695](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L695)  
> Since: 3.50.0

---

## clone

### <instance> clone()

**Description:**

Make a clone of this Vector3.

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - A new Vector3 object containing this Vectors values.

**Inherits:** [Phaser.Math.Vector3#clone](math-vector3.md)

> Source: [src/math/Vector3.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L134)  
> Since: 3.0.0

---

## copy

### <instance> copy(src)

**Description:**

Copy the components of a given Vector into this Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to copy the components from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#copy](math-vector3.md)

> Source: [src/math/Vector3.js#L231](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L231)  
> Since: 3.0.0

---

## cross

### <instance> cross(v)

**Description:**

Calculate the cross (vector) product of this Vector (which will be modified) and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to cross product with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#cross](math-vector3.md)

> Source: [src/math/Vector3.js#L617](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L617)  
> Since: 3.0.0

---

## crossVectors

### <instance> crossVectors(a, b)

**Description:**

Calculate the cross (vector) product of two given Vectors.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.Math.Vector3](math-vector3.md) | No | The first Vector to multiply. |
| --- | --- | --- | --- |
| b | [Phaser.Math.Vector3](math-vector3.md) | No | The second Vector to multiply. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#crossVectors](math-vector3.md)

> Source: [src/math/Vector3.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L187)  
> Since: 3.0.0

---

## distance

### <instance> distance(v)

**Description:**

Calculate the distance between this Vector and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to calculate the distance to. |
| --- | --- | --- | --- |

**Returns:** number - The distance from this Vector to the given Vector.

**Inherits:** [Phaser.Math.Vector3#distance](math-vector3.md)

> Source: [src/math/Vector3.js#L501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L501)  
> Since: 3.0.0

---

## distanceSq

### <instance> distanceSq(v)

**Description:**

Calculate the distance between this Vector and the given Vector, squared.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to calculate the distance to. |
| --- | --- | --- | --- |

**Returns:** number - The distance from this Vector to the given Vector, squared.

**Inherits:** [Phaser.Math.Vector3#distanceSq](math-vector3.md)

> Source: [src/math/Vector3.js#L520](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L520)  
> Since: 3.0.0

---

## divide

### <instance> divide(v)

**Description:**

Perform a component-wise division between this Vector and the given Vector.

Divides this Vector by the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to divide this Vector by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#divide](math-vector3.md)

> Source: [src/math/Vector3.js#L463](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L463)  
> Since: 3.0.0

---

## dot

### <instance> dot(v)

**Description:**

Calculate the dot product of this Vector and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector3 to dot product with this Vector3. |
| --- | --- | --- | --- |

**Returns:** number - The dot product of this Vector and `v`.

**Inherits:** [Phaser.Math.Vector3#dot](math-vector3.md)

> Source: [src/math/Vector3.js#L602](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L602)  
> Since: 3.0.0

---

## equals

### <instance> equals(v)

**Description:**

Check whether this Vector is equal to a given Vector.

Performs a strict equality check against each Vector's components.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector3 to compare against. |
| --- | --- | --- | --- |

**Returns:** boolean - True if the two vectors strictly match, otherwise false.

**Inherits:** [Phaser.Math.Vector3#equals](math-vector3.md)

> Source: [src/math/Vector3.js#L214](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L214)  
> Since: 3.0.0

---

## fromArray

### <instance> fromArray(array, [offset])

**Description:**

Sets the components of this Vector3 from the given array, based on the offset.

Vector3.x = array[offset]

Vector3.y = array[offset + 1]

Vector3.z = array[offset + 2]

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| array | Array.<number> | No |  | The array of values to get this Vector from. |
| --- | --- | --- | --- | --- |
| offset | number | Yes | 0 | The offset index into the array. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#fromArray](math-vector3.md)

> Source: [src/math/Vector3.js#L311](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L311)  
> Since: 3.50.0

---

## length

### <instance> length()

**Description:**

Calculate the length (or magnitude) of this Vector.

**Returns:** number - The length of this Vector.

**Inherits:** [Phaser.Math.Vector3#length](math-vector3.md)

> Source: [src/math/Vector3.js#L539](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L539)  
> Since: 3.0.0

---

## lengthSq

### <instance> lengthSq()

**Description:**

Calculate the length of this Vector squared.

**Returns:** number - The length of this Vector, squared.

**Inherits:** [Phaser.Math.Vector3#lengthSq](math-vector3.md)

> Source: [src/math/Vector3.js#L556](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L556)  
> Since: 3.0.0

---

## lerp

### <instance> lerp(v, [t])

**Description:**

Linearly interpolate between this Vector and the given Vector.

Interpolates this Vector towards the given Vector.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No |  | The Vector3 to interpolate towards. |
| --- | --- | --- | --- | --- |
| t | number | Yes | 0 | The interpolation percentage, between 0 and 1. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#lerp](math-vector3.md)

> Source: [src/math/Vector3.js#L643](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L643)  
> Since: 3.0.0

---

## load

### <instance> load(F32, U32, offset, textureUnit, tintEffect)

**Description:**

Loads the data from this Vertex into the given Typed Arrays.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| F32 | Float32Array | No | A Float32 Array to insert the position, UV and unit data in to. |
| --- | --- | --- | --- |
| U32 | Uint32Array | No | A Uint32 Array to insert the color and alpha data in to. |
| offset | number | No | The index of the array to insert this Vertex to. |
| textureUnit | number | No | The texture unit currently in use. |
| tintEffect | number | No | The tint effect to use. |

**Returns:** number - The new array offset.

> Source: [src/geom/mesh/Vertex.js#L379](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L379)  
> Since: 3.50.0

---

## max

### <instance> max(v)

**Description:**

Sets the components of this Vector to be the `Math.max` result from the given vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector3 to check the maximum values against. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#max](math-vector3.md)

> Source: [src/math/Vector3.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L115)  
> Since: 3.50.0

---

## min

### <instance> min(v)

**Description:**

Sets the components of this Vector to be the `Math.min` result from the given vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector3 to check the minimum values against. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#min](math-vector3.md)

> Source: [src/math/Vector3.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L96)  
> Since: 3.50.0

---

## multiply

### <instance> multiply(v)

**Description:**

Perform a component-wise multiplication between this Vector and the given Vector.

Multiplies this Vector by the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to multiply this Vector by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#multiply](math-vector3.md)

> Source: [src/math/Vector3.js#L414](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L414)  
> Since: 3.0.0

---

## negate

### <instance> negate()

**Description:**

Negate the `x`, `y` and `z` components of this Vector.

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#negate](math-vector3.md)

> Source: [src/math/Vector3.js#L484](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L484)  
> Since: 3.0.0

---

## normalize

### <instance> normalize()

**Description:**

Normalize this Vector.

Makes the vector a unit length vector (magnitude of 1) in the same direction.

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#normalize](math-vector3.md)

> Source: [src/math/Vector3.js#L573](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L573)  
> Since: 3.0.0

---

## project

### <instance> project(mat)

**Description:**

Multiplies this Vector3 by the specified matrix, applying a W divide. This is useful for projection,

e.g. unprojecting a 2D point into 3D space.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to multiply this Vector3 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#project](math-vector3.md)

> Source: [src/math/Vector3.js#L833](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L833)  
> Since: 3.0.0

---

## projectViewMatrix

### <instance> projectViewMatrix(viewMatrix, projectionMatrix)

**Description:**

Multiplies this Vector3 by the given view and projection matrices.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| viewMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | No | A View Matrix. |
| --- | --- | --- | --- |
| projectionMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | No | A Projection Matrix. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#projectViewMatrix](math-vector3.md)

> Source: [src/math/Vector3.js#L877](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L877)  
> Since: 3.50.0

---

## reset

### <instance> reset()

**Description:**

Make this Vector the zero vector (0, 0, 0).

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#reset](math-vector3.md)

> Source: [src/math/Vector3.js#L945](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L945)  
> Since: 3.0.0

---

## resize

### <instance> resize(x, y, width, height, originX, originY)

**Description:**

Resizes this Vertex by setting the x and y coordinates, then transforms this vertex

by an identity matrix and dimensions, storing the results in `vx`, `vy` and `vz`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the vertex. |
| --- | --- | --- | --- |
| y | number | No | The y position of the vertex. |
| width | number | No | The width of the parent Mesh. |
| height | number | No | The height of the parent Mesh. |
| originX | number | No | The originX of the parent Mesh. |
| originY | number | No | The originY of the parent Mesh. |

**Returns:** [Phaser.Geom.Mesh.Vertex](geom-mesh-vertex.md) - This Vertex.

> Source: [src/geom/mesh/Vertex.js#L298](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L298)  
> Since: 3.60.0

---

## scale

### <instance> scale(scale)

**Description:**

Scale this Vector by the given value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scale | number | No | The value to scale this Vector by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#scale](math-vector3.md)

> Source: [src/math/Vector3.js#L435](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L435)  
> Since: 3.0.0

---

## scaleUV

### <instance> scaleUV(x, y)

**Description:**

Scales the original UV values by the given amounts.

The original properties `Vertex.u` and `Vertex.v`

remain unchanged, only the translated properties

`Vertex.tu` and `Vertex.tv`, as used in rendering,

are updated.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The amount to scale the UV u coordinate by. |
| --- | --- | --- | --- |
| y | number | No | The amount to scale the UV v coordinate by. |

**Returns:** [Phaser.Geom.Mesh.Vertex](geom-mesh-vertex.md) - This Vertex.

> Source: [src/geom/mesh/Vertex.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L237)  
> Since: 3.60.0

---

## scrollUV

### <instance> scrollUV(x, y)

**Description:**

Translates the original UV positions by the given amounts.

The original properties `Vertex.u` and `Vertex.v`

remain unchanged, only the translated properties

`Vertex.tu` and `Vertex.tv`, as used in rendering,

are updated.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The amount to scroll the UV u coordinate by. |
| --- | --- | --- | --- |
| y | number | No | The amount to scroll the UV v coordinate by. |

**Returns:** [Phaser.Geom.Mesh.Vertex](geom-mesh-vertex.md) - This Vertex.

> Source: [src/geom/mesh/Vertex.js#L213](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L213)  
> Since: 3.60.0

---

## set

### <instance> set(x, [y], [z])

**Description:**

Set the `x`, `y`, and `z` components of this Vector to the given `x`, `y`, and `z` values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | object | No | The x value to set for this Vector, or an object containing x, y and z components. |
| --- | --- | --- | --- |
| y | number | Yes | The y value to set for this Vector. |
| z | number | Yes | The z value to set for this Vector. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#set](math-vector3.md)

> Source: [src/math/Vector3.js#L250](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L250)  
> Since: 3.0.0

---

## setFromMatrixColumn

### <instance> setFromMatrixColumn(mat4, index)

**Description:**

Sets the components of this Vector3 from the Matrix4 column specified.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat4 | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to get the column from. |
| --- | --- | --- | --- |
| index | number | No | The column index. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#setFromMatrixColumn](math-vector3.md)

> Source: [src/math/Vector3.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L295)  
> Since: 3.50.0

---

## setFromMatrixPosition

### <instance> setFromMatrixPosition(mat4)

**Description:**

Sets the components of this Vector3 from the position of the given Matrix4.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat4 | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to get the position from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#setFromMatrixPosition](math-vector3.md)

> Source: [src/math/Vector3.js#L280](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L280)  
> Since: 3.50.0

---

## setUVs

### <instance> setUVs(u, v)

**Description:**

Sets the U and V properties.

Also resets the translated uv properties, undoing any scale

or shift they may have had.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| u | number | No | The UV u coordinate of the vertex. |
| --- | --- | --- | --- |
| v | number | No | The UV v coordinate of the vertex. |

**Returns:** [Phaser.Geom.Mesh.Vertex](geom-mesh-vertex.md) - This Vertex.

> Source: [src/geom/mesh/Vertex.js#L188](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L188)  
> Since: 3.50.0

---

## subtract

### <instance> subtract(v)

**Description:**

Subtract the given Vector from this Vector. Subtraction is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to subtract from this Vector. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#subtract](math-vector3.md)

> Source: [src/math/Vector3.js#L395](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L395)  
> Since: 3.0.0

---

## subVectors

### <instance> subVectors(a, b)

**Description:**

Subtracts the two given Vector3s and sets the results into this Vector3.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.Math.Vector3](math-vector3.md) | No | The first Vector to sub. |
| --- | --- | --- | --- |
| b | [Phaser.Math.Vector3](math-vector3.md) | No | The second Vector to sub. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#subVectors](math-vector3.md)

> Source: [src/math/Vector3.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L167)  
> Since: 3.85.0

---

## transformCoordinates

### <instance> transformCoordinates(mat)

**Description:**

Transforms the coordinates of this Vector3 with the given Matrix4.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to transform this Vector3 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#transformCoordinates](math-vector3.md)

> Source: [src/math/Vector3.js#L769](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L769)  
> Since: 3.0.0

---

## transformCoordinatesLocal

### <instance> transformCoordinatesLocal(transformMatrix, width, height, cameraZ)

**Description:**

Transforms this vertex by the given matrix, storing the results in `vx`, `vy` and `vz`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| transformMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | No | The transform matrix to apply to this vertex. |
| --- | --- | --- | --- |
| width | number | No | The width of the parent Mesh. |
| height | number | No | The height of the parent Mesh. |
| cameraZ | number | No | The z position of the MeshCamera. |

> Source: [src/geom/mesh/Vertex.js#L261](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L261)  
> Since: 3.50.0

---

## transformMat3

### <instance> transformMat3(mat)

**Description:**

Transform this Vector with the given Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix3](math-matrix3.md) | No | The Matrix3 to transform this Vector3 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#transformMat3](math-vector3.md)

> Source: [src/math/Vector3.js#L721](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L721)  
> Since: 3.0.0

---

## transformMat4

### <instance> transformMat4(mat)

**Description:**

Transform this Vector with the given Matrix4.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to transform this Vector3 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#transformMat4](math-vector3.md)

> Source: [src/math/Vector3.js#L745](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L745)  
> Since: 3.0.0

---

## transformQuat

### <instance> transformQuat(q)

**Description:**

Transform this Vector with the given Quaternion.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| q | [Phaser.Math.Quaternion](math-quaternion.md) | No | The Quaternion to transform this Vector with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#transformQuat](math-vector3.md)

> Source: [src/math/Vector3.js#L798](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L798)  
> Since: 3.0.0

---

## unproject

### <instance> unproject(viewport, invProjectionView)

**Description:**

Unproject this point from 2D space to 3D space.

The point should have its x and y properties set to

2D screen space, and the z either at 0 (near plane)

or 1 (far plane). The provided matrix is assumed to already

be combined, i.e. projection \* view \* model.

After this operation, this vector's (x, y, z) components will

represent the unprojected 3D coordinate.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| viewport | [Phaser.Math.Vector4](math-vector4.md) | No | Screen x, y, width and height in pixels. |
| --- | --- | --- | --- |
| invProjectionView | [Phaser.Math.Matrix4](math-matrix4.md) | No | Combined projection and view matrix. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#unproject](math-vector3.md)

> Source: [src/math/Vector3.js#L909](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L909)  
> Since: 3.0.0

---

## unprojectViewMatrix

### <instance> unprojectViewMatrix(projectionMatrix, worldMatrix)

**Description:**

Multiplies this Vector3 by the given inversed projection matrix and world matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| projectionMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | No | An inversed Projection Matrix. |
| --- | --- | --- | --- |
| worldMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | No | A World View Matrix. |

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#unprojectViewMatrix](math-vector3.md)

> Source: [src/math/Vector3.js#L893](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L893)  
> Since: 3.50.0

---

## up

### <instance> up()

**Description:**

Set this Vector to point up.

Sets the y component of the vector to 1, and the others to 0.

**Returns:** [Phaser.Math.Vector3](math-vector3.md) - This Vector3.

**Inherits:** [Phaser.Math.Vector3#up](math-vector3.md)

> Source: [src/math/Vector3.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector3.js#L77)  
> Since: 3.0.0

---

## update

### <instance> update(a, b, c, d, e, f, roundPixels, alpha)

**Description:**

Updates this Vertex based on the given transform.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | number | No | The parent transform matrix data a component. |
| --- | --- | --- | --- |
| b | number | No | The parent transform matrix data b component. |
| c | number | No | The parent transform matrix data c component. |
| d | number | No | The parent transform matrix data d component. |
| e | number | No | The parent transform matrix data e component. |
| f | number | No | The parent transform matrix data f component. |
| roundPixels | boolean | No | Round the vertex position or not? |
| alpha | number | No | The alpha of the parent object. |

**Returns:** [Phaser.Geom.Mesh.Vertex](geom-mesh-vertex.md) - This Vertex.

> Source: [src/geom/mesh/Vertex.js#L344](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/Vertex.js#L344)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [color](#color)

    - [color: number](#color-number)
  + [nx](#nx)

    - [nx: number](#nx-number)
  + [ny](#ny)

    - [ny: number](#ny-number)
  + [nz](#nz)

    - [nz: number](#nz-number)
  + [ta](#ta)

    - [ta: number](#ta-number)
  + [tu](#tu)

    - [tu: number](#tu-number)
  + [tv](#tv)

    - [tv: number](#tv-number)
  + [tx](#tx)

    - [tx: number](#tx-number)
  + [ty](#ty)

    - [ty: number](#ty-number)
  + [u](#u)

    - [u: number](#u-number)
  + [v](#v)

    - [v: number](#v-number)
  + [vx](#vx)

    - [vx: number](#vx-number)
  + [vy](#vy)

    - [vy: number](#vy-number)
  + [vz](#vz)

    - [vz: number](#vz-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
  + [z](#z)

    - [z: number](#z-number)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(v)](#instance-addv)
  + [addScalar](#addscalar)

    - [<instance> addScalar(s)](#instance-addscalars)
  + [addScale](#addscale)

    - [<instance> addScale(v, scale)](#instance-addscalev-scale)
  + [addVectors](#addvectors)

    - [<instance> addVectors(a, b)](#instance-addvectorsa-b)
  + [applyMatrix3](#applymatrix3)

    - [<instance> applyMatrix3(mat3)](#instance-applymatrix3mat3)
  + [applyMatrix4](#applymatrix4)

    - [<instance> applyMatrix4(mat4)](#instance-applymatrix4mat4)
  + [clone](#clone)

    - [<instance> clone()](#instance-clone)
  + [copy](#copy)

    - [<instance> copy(src)](#instance-copysrc)
  + [cross](#cross)

    - [<instance> cross(v)](#instance-crossv)
  + [crossVectors](#crossvectors)

    - [<instance> crossVectors(a, b)](#instance-crossvectorsa-b)
  + [distance](#distance)

    - [<instance> distance(v)](#instance-distancev)
  + [distanceSq](#distancesq)

    - [<instance> distanceSq(v)](#instance-distancesqv)
  + [divide](#divide)

    - [<instance> divide(v)](#instance-dividev)
  + [dot](#dot)

    - [<instance> dot(v)](#instance-dotv)
  + [equals](#equals)

    - [<instance> equals(v)](#instance-equalsv)
  + [fromArray](#fromarray)

    - [<instance> fromArray(array, [offset])](#instance-fromarrayarray-offset)
  + [length](#length)

    - [<instance> length()](#instance-length)
  + [lengthSq](#lengthsq)

    - [<instance> lengthSq()](#instance-lengthsq)
  + [lerp](#lerp)

    - [<instance> lerp(v, [t])](#instance-lerpv-t)
  + [load](#load)

    - [<instance> load(F32, U32, offset, textureUnit, tintEffect)](#instance-loadf32-u32-offset-textureunit-tinteffect)
  + [max](#max)

    - [<instance> max(v)](#instance-maxv)
  + [min](#min)

    - [<instance> min(v)](#instance-minv)
  + [multiply](#multiply)

    - [<instance> multiply(v)](#instance-multiplyv)
  + [negate](#negate)

    - [<instance> negate()](#instance-negate)
  + [normalize](#normalize)

    - [<instance> normalize()](#instance-normalize)
  + [project](#project)

    - [<instance> project(mat)](#instance-projectmat)
  + [projectViewMatrix](#projectviewmatrix)

    - [<instance> projectViewMatrix(viewMatrix, projectionMatrix)](#instance-projectviewmatrixviewmatrix-projectionmatrix)
  + [reset](#reset)

    - [<instance> reset()](#instance-reset)
  + [resize](#resize)

    - [<instance> resize(x, y, width, height, originX, originY)](#instance-resizex-y-width-height-originx-originy)
  + [scale](#scale)

    - [<instance> scale(scale)](#instance-scalescale)
  + [scaleUV](#scaleuv)

    - [<instance> scaleUV(x, y)](#instance-scaleuvx-y)
  + [scrollUV](#scrolluv)

    - [<instance> scrollUV(x, y)](#instance-scrolluvx-y)
  + [set](#set)

    - [<instance> set(x, [y], [z])](#instance-setx-y-z)
  + [setFromMatrixColumn](#setfrommatrixcolumn)

    - [<instance> setFromMatrixColumn(mat4, index)](#instance-setfrommatrixcolumnmat4-index)
  + [setFromMatrixPosition](#setfrommatrixposition)

    - [<instance> setFromMatrixPosition(mat4)](#instance-setfrommatrixpositionmat4)
  + [setUVs](#setuvs)

    - [<instance> setUVs(u, v)](#instance-setuvsu-v)
  + [subtract](#subtract)

    - [<instance> subtract(v)](#instance-subtractv)
  + [subVectors](#subvectors)

    - [<instance> subVectors(a, b)](#instance-subvectorsa-b)
  + [transformCoordinates](#transformcoordinates)

    - [<instance> transformCoordinates(mat)](#instance-transformcoordinatesmat)
  + [transformCoordinatesLocal](#transformcoordinateslocal)

    - [<instance> transformCoordinatesLocal(transformMatrix, width, height, cameraZ)](#instance-transformcoordinateslocaltransformmatrix-width-height-cameraz)
  + [transformMat3](#transformmat3)

    - [<instance> transformMat3(mat)](#instance-transformmat3mat)
  + [transformMat4](#transformmat4)

    - [<instance> transformMat4(mat)](#instance-transformmat4mat)
  + [transformQuat](#transformquat)

    - [<instance> transformQuat(q)](#instance-transformquatq)
  + [unproject](#unproject)

    - [<instance> unproject(viewport, invProjectionView)](#instance-unprojectviewport-invprojectionview)
  + [unprojectViewMatrix](#unprojectviewmatrix)

    - [<instance> unprojectViewMatrix(projectionMatrix, worldMatrix)](#instance-unprojectviewmatrixprojectionmatrix-worldmatrix)
  + [up](#up)

    - [<instance> up()](#instance-up)
  + [update](#update)

    - [<instance> update(a, b, c, d, e, f, roundPixels, alpha)](#instance-updatea-b-c-d-e-f-roundpixels-alpha)

Back to top

©2025[Phaser](https://docs.phaser.io)