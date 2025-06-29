# Phaser.Display.Color.Interpolate

Scope:
static

> Source: [src/display/color/Interpolate.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Interpolate.js#L9)  
> Since: 3.0.0

# Static functions

## ColorWithColor

### <static> ColorWithColor(color1, color2, [length], [index])

**Description:**

Interpolates between the two given color objects over the length supplied.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color1 | [Phaser.Display.Color](display-color.md) | No |  | The first Color object. |
| --- | --- | --- | --- | --- |
| color2 | [Phaser.Display.Color](display-color.md) | No |  | The second Color object. |
| length | number | Yes | 100 | Distance to interpolate over. |
| index | number | Yes | 0 | Index to start from. |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md) - An object containing the interpolated color values.

> Source: [src/display/color/Interpolate.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Interpolate.js#L48)  
> Since: 3.0.0

---

## ColorWithRGB

### <static> ColorWithRGB(color1, r, g, b, [length], [index])

**Description:**

Interpolates between the Color object and color values over the length supplied.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color1 | [Phaser.Display.Color](display-color.md) | No |  | The first Color object. |
| --- | --- | --- | --- | --- |
| r | number | No |  | Red value. |
| g | number | No |  | Blue value. |
| b | number | No |  | Green value. |
| length | number | Yes | 100 | Distance to interpolate over. |
| index | number | Yes | 0 | Index to start from. |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md) - An object containing the interpolated color values.

> Source: [src/display/color/Interpolate.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Interpolate.js#L71)  
> Since: 3.0.0

---

## RGBWithRGB

### <static> RGBWithRGB(r1, g1, b1, r2, g2, b2, [length], [index])

**Description:**

Interpolates between the two given color ranges over the length supplied.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| r1 | number | No |  | Red value. |
| --- | --- | --- | --- | --- |
| g1 | number | No |  | Blue value. |
| b1 | number | No |  | Green value. |
| r2 | number | No |  | Red value. |
| g2 | number | No |  | Blue value. |
| b2 | number | No |  | Green value. |
| length | number | Yes | 100 | Distance to interpolate over. |
| index | number | Yes | 0 | Index to start from. |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md) - An object containing the interpolated color values.

> Source: [src/display/color/Interpolate.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Interpolate.js#L15)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [ColorWithColor](#colorwithcolor)

    - [<static> ColorWithColor(color1, color2, [length], [index])](#static-colorwithcolorcolor1-color2-length-index)
  + [ColorWithRGB](#colorwithrgb)

    - [<static> ColorWithRGB(color1, r, g, b, [length], [index])](#static-colorwithrgbcolor1-r-g-b-length-index)
  + [RGBWithRGB](#rgbwithrgb)

    - [<static> RGBWithRGB(r1, g1, b1, r2, g2, b2, [length], [index])](#static-rgbwithrgbr1-g1-b1-r2-g2-b2-length-index)

Back to top

©2025[Phaser](https://docs.phaser.io)