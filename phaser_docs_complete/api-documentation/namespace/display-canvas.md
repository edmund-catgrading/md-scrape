# Phaser.Display.Canvas

Scope:
static

> Source: [src/display/canvas/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/index.js#L7)

# Static functions

* [CanvasInterpolation](display-canvas-canvasinterpolation.md)
* [CanvasPool](display-canvas-canvaspool.md)
* [Smoothing](display-canvas-smoothing.md)

# Static functions

## TouchAction

### <static> TouchAction(canvas, [value])

**Description:**

Sets the touch-action property on the canvas style. Can be used to disable default browser touch actions.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| canvas | HTMLCanvasElement | No |  | The canvas element to have the style applied to. |
| --- | --- | --- | --- | --- |
| value | string | Yes | "'none'" | The touch action value to set on the canvas. Set to `none` to disable touch actions. |

**Returns:** HTMLCanvasElement - The canvas element.

> Source: [src/display/canvas/TouchAction.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/TouchAction.js#L7)  
> Since: 3.0.0

---

## UserSelect

### <static> UserSelect(canvas, [value])

**Description:**

Sets the user-select property on the canvas style. Can be used to disable default browser selection actions.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| canvas | HTMLCanvasElement | No |  | The canvas element to have the style applied to. |
| --- | --- | --- | --- | --- |
| value | string | Yes | "'none'" | The touch callout value to set on the canvas. Set to `none` to disable touch callouts. |

**Returns:** HTMLCanvasElement - The canvas element.

> Source: [src/display/canvas/UserSelect.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/UserSelect.js#L7)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)

  + [TouchAction](#touchaction)

    - [<static> TouchAction(canvas, [value])](#static-touchactioncanvas-value)
  + [UserSelect](#userselect)

    - [<static> UserSelect(canvas, [value])](#static-userselectcanvas-value)

Back to top

©2025[Phaser](https://docs.phaser.io)