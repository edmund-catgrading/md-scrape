# Phaser.Scale

Scope:
static

> Source: [src/scale/index.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/index.js#L10)

# Static functions

* [ScaleManager](../class/scale-scalemanager.md)

# Static functions

* [Center](scale-center.md)
* [Events](scale-events.md)
* [Orientation](scale-orientation.md)
* [ScaleModes](scale-scalemodes.md)
* [Zoom](scale-zoom.md)

# Static functions

## CenterType

### CenterType

**Description:**

Phaser Scale Manager constants for centering the game canvas.

To find out what each mode does please see [Phaser.Scale.Center](Phaser.Scale.Center.md).

> Source: [src/scale/const/CENTER\_CONST.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/CENTER_CONST.js#L15)  
> Since: 3.16.0

---

## OrientationType

### OrientationType

**Description:**

Phaser Scale Manager constants for orientation.

To find out what each mode does please see [Phaser.Scale.Orientation](Phaser.Scale.Orientation.md).

> Source: [src/scale/const/ORIENTATION\_CONST.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/ORIENTATION_CONST.js#L15)  
> Since: 3.16.0

---

## ScaleModeType

### ScaleModeType

**Description:**

Phaser Scale Manager constants for the different scale modes available.

To find out what each mode does please see [Phaser.Scale.ScaleModes](Phaser.Scale.ScaleModes.md).

> Source: [src/scale/const/SCALE\_MODE\_CONST.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/SCALE_MODE_CONST.js#L15)  
> Since: 3.16.0

---

## ZoomType

### ZoomType

**Description:**

Phaser Scale Manager constants for zoom modes.

To find out what each mode does please see [Phaser.Scale.Zoom](Phaser.Scale.Zoom.md).

> Source: [src/scale/const/ZOOM\_CONST.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/ZOOM_CONST.js#L15)  
> Since: 3.16.0

---

# Static functions

## CENTER\_BOTH

### CENTER\_BOTH: number

**Description:**

The game canvas is centered both horizontally and vertically within the parent.

To do this, the parent has to have a bounds that can be calculated and not be empty.

Centering is achieved by setting the margin left and top properties of the

game canvas, and does not factor in any other CSS styles you may have applied.

> Source: [src/scale/const/CENTER\_CONST.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/CENTER_CONST.js#L38)  
> Since: 3.16.0

---

## CENTER\_HORIZONTALLY

### CENTER\_HORIZONTALLY: number

**Description:**

The game canvas is centered horizontally within the parent.

To do this, the parent has to have a bounds that can be calculated and not be empty.

Centering is achieved by setting the margin left and top properties of the

game canvas, and does not factor in any other CSS styles you may have applied.

> Source: [src/scale/const/CENTER\_CONST.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/CENTER_CONST.js#L52)  
> Since: 3.16.0

---

## CENTER\_VERTICALLY

### CENTER\_VERTICALLY: number

**Description:**

The game canvas is centered both vertically within the parent.

To do this, the parent has to have a bounds that can be calculated and not be empty.

Centering is achieved by setting the margin left and top properties of the

game canvas, and does not factor in any other CSS styles you may have applied.

> Source: [src/scale/const/CENTER\_CONST.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/CENTER_CONST.js#L66)  
> Since: 3.16.0

---

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

## LANDSCAPE

### LANDSCAPE: string

**Description:**

The primary landscape orientation.

> Source: [src/scale/const/ORIENTATION\_CONST.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/ORIENTATION_CONST.js#L27)  
> Since: 3.16.0

---

## MAX\_ZOOM

### MAX\_ZOOM: number

**Description:**

Calculate the zoom value based on the maximum multiplied game size that will

fit into the parent, or browser window if no parent is set.

> Source: [src/scale/const/ZOOM\_CONST.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/ZOOM_CONST.js#L57)  
> Since: 3.16.0

---

## NO\_CENTER

### NO\_CENTER: number

**Description:**

The game canvas is not centered within the parent by Phaser.

You can still center it yourself via CSS.

> Source: [src/scale/const/CENTER\_CONST.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/CENTER_CONST.js#L27)  
> Since: 3.16.0

---

## NO\_ZOOM

### NO\_ZOOM: number

**Description:**

The game canvas will not be zoomed by Phaser.

> Source: [src/scale/const/ZOOM\_CONST.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/ZOOM_CONST.js#L27)  
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

## PORTRAIT

### PORTRAIT: string

**Description:**

The primary portrait orientation.

> Source: [src/scale/const/ORIENTATION\_CONST.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/ORIENTATION_CONST.js#L47)  
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

## ZOOM\_2X

### ZOOM\_2X: number

**Description:**

The game canvas will be 2x zoomed by Phaser.

> Source: [src/scale/const/ZOOM\_CONST.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/ZOOM_CONST.js#L37)  
> Since: 3.16.0

---

## ZOOM\_4X

### ZOOM\_4X: number

**Description:**

The game canvas will be 4x zoomed by Phaser.

> Source: [src/scale/const/ZOOM\_CONST.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/const/ZOOM_CONST.js#L47)  
> Since: 3.16.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)
* [Static functions](#static-functions-2)

  + [CenterType](#centertype)

    - [CenterType](#centertype-1)
  + [OrientationType](#orientationtype)

    - [OrientationType](#orientationtype-1)
  + [ScaleModeType](#scalemodetype)

    - [ScaleModeType](#scalemodetype-1)
  + [ZoomType](#zoomtype)

    - [ZoomType](#zoomtype-1)
* [Static functions](#static-functions-3)

  + [CENTER\_BOTH](#center_both)

    - [CENTER\_BOTH: number](#center_both-number)
  + [CENTER\_HORIZONTALLY](#center_horizontally)

    - [CENTER\_HORIZONTALLY: number](#center_horizontally-number)
  + [CENTER\_VERTICALLY](#center_vertically)

    - [CENTER\_VERTICALLY: number](#center_vertically-number)
  + [ENVELOP](#envelop)

    - [ENVELOP: number](#envelop-number)
  + [EXPAND](#expand)

    - [EXPAND: number](#expand-number)
  + [FIT](#fit)

    - [FIT: number](#fit-number)
  + [HEIGHT\_CONTROLS\_WIDTH](#height_controls_width)

    - [HEIGHT\_CONTROLS\_WIDTH: number](#height_controls_width-number)
  + [LANDSCAPE](#landscape)

    - [LANDSCAPE: string](#landscape-string)
  + [MAX\_ZOOM](#max_zoom)

    - [MAX\_ZOOM: number](#max_zoom-number)
  + [NO\_CENTER](#no_center)

    - [NO\_CENTER: number](#no_center-number)
  + [NO\_ZOOM](#no_zoom)

    - [NO\_ZOOM: number](#no_zoom-number)
  + [NONE](#none)

    - [NONE: number](#none-number)
  + [PORTRAIT](#portrait)

    - [PORTRAIT: string](#portrait-string)
  + [RESIZE](#resize)

    - [RESIZE: number](#resize-number)
  + [WIDTH\_CONTROLS\_HEIGHT](#width_controls_height)

    - [WIDTH\_CONTROLS\_HEIGHT: number](#width_controls_height-number)
  + [ZOOM\_2X](#zoom_2x)

    - [ZOOM\_2X: number](#zoom_2x-number)
  + [ZOOM\_4X](#zoom_4x)

    - [ZOOM\_4X: number](#zoom_4x-number)

Back to top

©2025[Phaser](https://docs.phaser.io)