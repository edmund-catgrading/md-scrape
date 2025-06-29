# Phaser.Scale.ScaleModes

Scope:
static

> Source: [src/scale/const/SCALE\_MODE\_CONST.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/SCALE_MODE_CONST.js#L7)  
> Since: 3.16.0

# Static functions

## ENVELOP

### ENVELOP: number

**Description:**

The width and height are automatically adjusted to make the size cover the entire target

area while keeping the aspect ratio. This may extend further out than the target size.

> Source: [src/scale/const/SCALE\_MODE\_CONST.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/SCALE_MODE_CONST.js#L71)  
> Since: 3.16.0

---

## EXPAND

### EXPAND: number

**Description:**

The Canvas's visible area is resized to fit all available *parent* space like RESIZE mode,

and scale canvas size to fit inside the visible area like FIT mode.

> Source: [src/scale/const/SCALE\_MODE\_CONST.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/SCALE_MODE_CONST.js#L92)  
> Since: 3.80.0

---

## FIT

### FIT: number

**Description:**

The width and height are automatically adjusted to fit inside the given target area,

while keeping the aspect ratio. Depending on the aspect ratio there may be some space

inside the area which is not covered.

> Source: [src/scale/const/SCALE\_MODE\_CONST.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/SCALE_MODE_CONST.js#L59)  
> Since: 3.16.0

---

## HEIGHT\_CONTROLS\_WIDTH

### HEIGHT\_CONTROLS\_WIDTH: number

**Description:**

The width is automatically adjusted based on the height.

> Source: [src/scale/const/SCALE\_MODE\_CONST.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/SCALE_MODE_CONST.js#L49)  
> Since: 3.16.0

---

## NONE

### NONE: number

**Description:**

No scaling happens at all. The canvas is set to the size given in the game config and Phaser doesn't change it

again from that point on. If you change the canvas size, either via CSS, or directly via code, then you need

to call the Scale Managers `resize` method to give the new dimensions, or input events will stop working.

> Source: [src/scale/const/SCALE\_MODE\_CONST.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/SCALE_MODE_CONST.js#L27)  
> Since: 3.16.0

---

## RESIZE

### RESIZE: number

**Description:**

The Canvas is resized to fit all available *parent* space, regardless of aspect ratio.

> Source: [src/scale/const/SCALE\_MODE\_CONST.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/SCALE_MODE_CONST.js#L82)  
> Since: 3.16.0

---

## WIDTH\_CONTROLS\_HEIGHT

### WIDTH\_CONTROLS\_HEIGHT: number

**Description:**

The height is automatically adjusted based on the width.

> Source: [src/scale/const/SCALE\_MODE\_CONST.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/SCALE_MODE_CONST.js#L39)  
> Since: 3.16.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [ENVELOP](#envelop)

    - [ENVELOP: number](#envelop-number)
  + [EXPAND](#expand)

    - [EXPAND: number](#expand-number)
  + [FIT](#fit)

    - [FIT: number](#fit-number)
  + [HEIGHT\_CONTROLS\_WIDTH](#height_controls_width)

    - [HEIGHT\_CONTROLS\_WIDTH: number](#height_controls_width-number)
  + [NONE](#none)

    - [NONE: number](#none-number)
  + [RESIZE](#resize)

    - [RESIZE: number](#resize-number)
  + [WIDTH\_CONTROLS\_HEIGHT](#width_controls_height)

    - [WIDTH\_CONTROLS\_HEIGHT: number](#width_controls_height-number)

Back to top

©2025[Phaser](https://docs.phaser.io)