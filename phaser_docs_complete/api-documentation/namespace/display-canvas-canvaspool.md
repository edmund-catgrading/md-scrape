# Phaser.Display.Canvas.CanvasPool

Scope:
static

> Source: [src/display/canvas/CanvasPool.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L16)  
> Since: 3.0.0

# Static functions

## create

### <static> create(parent, [width], [height], [canvasType], [selfParent])

**Description:**

Creates a new Canvas DOM element, or pulls one from the pool if free.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| parent | \* | No |  | The parent of the Canvas object. |
| --- | --- | --- | --- | --- |
| width | number | Yes | 1 | The width of the Canvas. |
| height | number | Yes | 1 | The height of the Canvas. |
| canvasType | number | Yes | "Phaser.CANVAS" | The type of the Canvas. Either `Phaser.CANVAS` or `Phaser.WEBGL`. |
| selfParent | boolean | Yes | false | Use the generated Canvas element as the parent? |

**Returns:** HTMLCanvasElement - The canvas element that was created or pulled from the pool

> Source: [src/display/canvas/CanvasPool.js#L29](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L29)  
> Since: 3.0.0

---

## create2D

### <static> create2D(parent, [width], [height])

**Description:**

Creates a new Canvas DOM element, or pulls one from the pool if free.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| parent | \* | No |  | The parent of the Canvas object. |
| --- | --- | --- | --- | --- |
| width | number | Yes | 1 | The width of the Canvas. |
| height | number | Yes | 1 | The height of the Canvas. |

**Returns:** HTMLCanvasElement - The created canvas.

> Source: [src/display/canvas/CanvasPool.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L91)  
> Since: 3.0.0

---

## createWebGL

### <static> createWebGL(parent, [width], [height])

**Description:**

Creates a new Canvas DOM element, or pulls one from the pool if free.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| parent | \* | No |  | The parent of the Canvas object. |
| --- | --- | --- | --- | --- |
| width | number | Yes | 1 | The width of the Canvas. |
| height | number | Yes | 1 | The height of the Canvas. |

**Returns:** HTMLCanvasElement - The created WebGL canvas.

> Source: [src/display/canvas/CanvasPool.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L108)  
> Since: 3.0.0

---

## disableSmoothing

### <static> disableSmoothing()

**Description:**

Disable context smoothing on any new Canvas element created.

> Source: [src/display/canvas/CanvasPool.js#L218](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L218)  
> Since: 3.0.0

---

## enableSmoothing

### <static> enableSmoothing()

**Description:**

Enable context smoothing on any new Canvas element created.

> Source: [src/display/canvas/CanvasPool.js#L229](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L229)  
> Since: 3.0.0

---

## first

### <static> first([canvasType])

**Description:**

Gets the first free canvas index from the pool.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| canvasType | number | Yes | "Phaser.CANVAS" | The type of the Canvas. Either `Phaser.CANVAS` or `Phaser.WEBGL`. |
| --- | --- | --- | --- | --- |

**Returns:** HTMLCanvasElement - The first free canvas, or `null` if a WebGL canvas was requested or if the pool doesn't have free canvases.

> Source: [src/display/canvas/CanvasPool.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L125)  
> Since: 3.0.0

---

## free

### <static> free()

**Description:**

Gets the total number of free canvas elements in the pool.

**Returns:** number - The number of free canvases.

> Source: [src/display/canvas/CanvasPool.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L205)  
> Since: 3.0.0

---

## remove

### <static> remove(parent)

**Description:**

Looks up a canvas based on its parent, and if found puts it back in the pool, freeing it up for re-use.

The canvas has its width and height set to 1, and its parent attribute nulled.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | \* | No | The canvas or the parent of the canvas to free. |
| --- | --- | --- | --- |

> Source: [src/display/canvas/CanvasPool.js#L157](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L157)  
> Since: 3.0.0

---

## total

### <static> total()

**Description:**

Gets the total number of used canvas elements in the pool.

**Returns:** number - The number of used canvases.

> Source: [src/display/canvas/CanvasPool.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L182)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [create](#create)

    - [<static> create(parent, [width], [height], [canvasType], [selfParent])](#static-createparent-width-height-canvastype-selfparent)
  + [create2D](#create2d)

    - [<static> create2D(parent, [width], [height])](#static-create2dparent-width-height)
  + [createWebGL](#createwebgl)

    - [<static> createWebGL(parent, [width], [height])](#static-createwebglparent-width-height)
  + [disableSmoothing](#disablesmoothing)

    - [<static> disableSmoothing()](#static-disablesmoothing)
  + [enableSmoothing](#enablesmoothing)

    - [<static> enableSmoothing()](#static-enablesmoothing)
  + [first](#first)

    - [<static> first([canvasType])](#static-firstcanvastype)
  + [free](#free)

    - [<static> free()](#static-free)
  + [remove](#remove)

    - [<static> remove(parent)](#static-removeparent)
  + [total](#total)

    - [<static> total()](#static-total)

Back to top

©2025[Phaser](https://docs.phaser.io)