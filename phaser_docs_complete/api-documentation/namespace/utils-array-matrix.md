# Phaser.Utils.Array.Matrix

Scope:
static

> Source: [src/utils/array/matrix/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/index.js#L7)

# Static functions

## CheckMatrix

### <static> CheckMatrix([matrix])

**Description:**

Checks if an array can be used as a matrix.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes | The array to check. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the given `matrix` array is a valid matrix.

> Source: [src/utils/array/matrix/CheckMatrix.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/CheckMatrix.js#L7)  
> Since: 3.0.0

---

## MatrixToString

### <static> MatrixToString([matrix])

**Description:**

Generates a string (which you can pass to console.log) from the given Array Matrix.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes | A 2-dimensional array. |
| --- | --- | --- | --- |

**Returns:** string - A string representing the matrix.

> Source: [src/utils/array/matrix/MatrixToString.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/MatrixToString.js#L10)  
> Since: 3.0.0

---

## ReverseColumns

### <static> ReverseColumns([matrix])

**Description:**

Reverses the columns in the given Array Matrix.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes | The array matrix to reverse the columns for. |
| --- | --- | --- | --- |

**Returns:** Array.<Array.<T>> - The column reversed matrix.

> Source: [src/utils/array/matrix/ReverseColumns.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/ReverseColumns.js#L7)  
> Since: 3.0.0

---

## ReverseRows

### <static> ReverseRows([matrix])

**Description:**

Reverses the rows in the given Array Matrix.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes | The array matrix to reverse the rows for. |
| --- | --- | --- | --- |

**Returns:** Array.<Array.<T>> - The column reversed matrix.

> Source: [src/utils/array/matrix/ReverseRows.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/ReverseRows.js#L7)  
> Since: 3.0.0

---

## Rotate180

### <static> Rotate180([matrix])

**Description:**

Rotates the array matrix 180 degrees.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes | The array to rotate. |
| --- | --- | --- | --- |

**Returns:** Array.<Array.<T>> - The rotated matrix array. The source matrix should be discard for the returned matrix.

> Source: [src/utils/array/matrix/Rotate180.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/Rotate180.js#L9)  
> Since: 3.0.0

---

## RotateLeft

### <static> RotateLeft([matrix], [amount])

**Description:**

Rotates the array matrix to the left (or 90 degrees)

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes |  | The array to rotate. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The number of times to rotate the matrix. |

**Returns:** Array.<Array.<T>> - The rotated matrix array. The source matrix should be discard for the returned matrix.

> Source: [src/utils/array/matrix/RotateLeft.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/RotateLeft.js#L9)  
> Since: 3.0.0

---

## RotateMatrix

### <static> RotateMatrix([matrix], [direction])

**Description:**

Rotates the array matrix based on the given rotation value.

The value can be given in degrees: 90, -90, 270, -270 or 180,

or a string command: `rotateLeft`, `rotateRight` or `rotate180`.

Based on the routine from <http://jsfiddle.net/MrPolywhirl/NH42z/>.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes |  | The array to rotate. |
| --- | --- | --- | --- | --- |
| direction | number | string | Yes | 90 | The amount to rotate the matrix by. |

**Returns:** Array.<Array.<T>> - The rotated matrix array. The source matrix should be discard for the returned matrix.

> Source: [src/utils/array/matrix/RotateMatrix.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/RotateMatrix.js#L10)  
> Since: 3.0.0

---

## RotateRight

### <static> RotateRight([matrix], [amount])

**Description:**

Rotates the array matrix to the left (or -90 degrees)

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes |  | The array to rotate. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The number of times to rotate the matrix. |

**Returns:** Array.<Array.<T>> - The rotated matrix array. The source matrix should be discard for the returned matrix.

> Source: [src/utils/array/matrix/RotateRight.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/RotateRight.js#L9)  
> Since: 3.0.0

---

## Translate

### <static> Translate([matrix], [x], [y])

**Description:**

Translates the given Array Matrix by shifting each column and row the

amount specified.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| matrix | Array.<Array.<T>> | Yes |  | The array matrix to translate. |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The amount to horizontally translate the matrix by. |
| y | number | Yes | 0 | The amount to vertically translate the matrix by. |

**Returns:** Array.<Array.<T>> - The translated matrix.

> Source: [src/utils/array/matrix/TranslateMatrix.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/TranslateMatrix.js#L10)  
> Since: 3.50.0

---

## TransposeMatrix

### <static> TransposeMatrix([array])

**Description:**

Transposes the elements of the given matrix (array of arrays).

The transpose of a matrix is a new matrix whose rows are the columns of the original.

A matrix is a two-dimensional array (array of arrays), where all sub-arrays (rows)

have the same length. There must be at least two rows. This is an example matrix:

```
Copy
[

   [ 1, 1, 1, 1, 1, 1 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 2, 0, 1, 2, 0, 4 ],

   [ 2, 0, 3, 4, 0, 4 ],

   [ 2, 0, 0, 0, 0, 4 ],

   [ 3, 3, 3, 3, 3, 3 ]

]


```

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| array | Array.<Array.<T>> | Yes | The array matrix to transpose. |
| --- | --- | --- | --- |

**Returns:** Array.<Array.<T>> - A new array matrix which is a transposed version of the given array.

> Source: [src/utils/array/matrix/TransposeMatrix.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/array/matrix/TransposeMatrix.js#L7)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [CheckMatrix](#checkmatrix)

    - [<static> CheckMatrix([matrix])](#static-checkmatrixmatrix)
  + [MatrixToString](#matrixtostring)

    - [<static> MatrixToString([matrix])](#static-matrixtostringmatrix)
  + [ReverseColumns](#reversecolumns)

    - [<static> ReverseColumns([matrix])](#static-reversecolumnsmatrix)
  + [ReverseRows](#reverserows)

    - [<static> ReverseRows([matrix])](#static-reverserowsmatrix)
  + [Rotate180](#rotate180)

    - [<static> Rotate180([matrix])](#static-rotate180matrix)
  + [RotateLeft](#rotateleft)

    - [<static> RotateLeft([matrix], [amount])](#static-rotateleftmatrix-amount)
  + [RotateMatrix](#rotatematrix)

    - [<static> RotateMatrix([matrix], [direction])](#static-rotatematrixmatrix-direction)
  + [RotateRight](#rotateright)

    - [<static> RotateRight([matrix], [amount])](#static-rotaterightmatrix-amount)
  + [Translate](#translate)

    - [<static> Translate([matrix], [x], [y])](#static-translatematrix-x-y)
  + [TransposeMatrix](#transposematrix)

    - [<static> TransposeMatrix([array])](#static-transposematrixarray)

Back to top

©2025[Phaser](https://docs.phaser.io)