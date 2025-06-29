# Phaser.BlendModes

Scope:
static

> Source: [src/renderer/BlendModes.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L7)  
> Since: 3.0.0

# Static functions

## ADD

### ADD: number

**Description:**

Add blend mode. For Canvas and WebGL.

Where both shapes overlap the color is determined by adding color values.

> Source: [src/renderer/BlendModes.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L37)  
> Since: 3.0.0

---

## COLOR

### COLOR: number

**Description:**

Color blend mode. For Canvas only.

Preserves the luma of the bottom layer, while adopting the hue and chroma of the top layer.

> Source: [src/renderer/BlendModes.js#L191](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L191)  
> Since: 3.0.0

---

## COLOR\_BURN

### COLOR\_BURN: number

**Description:**

Color Burn blend mode. For Canvas only.

Divides the inverted bottom layer by the top layer, and then inverts the result.

> Source: [src/renderer/BlendModes.js#L114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L114)  
> Since: 3.0.0

---

## COLOR\_DODGE

### COLOR\_DODGE: number

**Description:**

Color Dodge blend mode. For Canvas only.

Divides the bottom layer by the inverted top layer.

> Source: [src/renderer/BlendModes.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L103)  
> Since: 3.0.0

---

## COPY

### COPY: number

**Description:**

Copy blend mode. For Canvas only.

Only the new shape is shown.

> Source: [src/renderer/BlendModes.js#L311](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L311)  
> Since: 3.0.0

---

## DARKEN

### DARKEN: number

**Description:**

Darken blend mode. For Canvas only.

Retains the darkest pixels of both layers.

> Source: [src/renderer/BlendModes.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L81)  
> Since: 3.0.0

---

## DESTINATION\_ATOP

### DESTINATION\_ATOP: number

**Description:**

Destination-out blend mode. For Canvas only.

The existing canvas is only kept where it overlaps the new shape. The new shape is drawn behind the canvas content.

> Source: [src/renderer/BlendModes.js#L289](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L289)  
> Since: 3.0.0

---

## DESTINATION\_IN

### DESTINATION\_IN: number

**Description:**

Destination-in blend mode. For Canvas only.

The existing canvas content is kept where both the new shape and existing canvas content overlap. Everything else is made transparent.

> Source: [src/renderer/BlendModes.js#L267](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L267)  
> Since: 3.0.0

---

## DESTINATION\_OUT

### DESTINATION\_OUT: number

**Description:**

Destination-out blend mode. For Canvas only.

The existing content is kept where it doesn't overlap the new shape.

> Source: [src/renderer/BlendModes.js#L278](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L278)  
> Since: 3.0.0

---

## DESTINATION\_OVER

### DESTINATION\_OVER: number

**Description:**

Destination-over blend mode. For Canvas only.

New shapes are drawn behind the existing canvas content.

> Source: [src/renderer/BlendModes.js#L256](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L256)  
> Since: 3.0.0

---

## DIFFERENCE

### DIFFERENCE: number

**Description:**

Difference blend mode. For Canvas only.

Subtracts the bottom layer from the top layer or the other way round to always get a positive value.

> Source: [src/renderer/BlendModes.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L147)  
> Since: 3.0.0

---

## ERASE

### ERASE: number

**Description:**

Alpha erase blend mode. For Canvas and WebGL.

> Source: [src/renderer/BlendModes.js#L213](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L213)  
> Since: 3.0.0

---

## EXCLUSION

### EXCLUSION: number

**Description:**

Exclusion blend mode. For Canvas only.

Like difference, but with lower contrast.

> Source: [src/renderer/BlendModes.js#L158](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L158)  
> Since: 3.0.0

---

## HARD\_LIGHT

### HARD\_LIGHT: number

**Description:**

Hard Light blend mode. For Canvas only.

A combination of multiply and screen like overlay, but with top and bottom layer swapped.

> Source: [src/renderer/BlendModes.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L125)  
> Since: 3.0.0

---

## HUE

### HUE: number

**Description:**

Hue blend mode. For Canvas only.

Preserves the luma and chroma of the bottom layer, while adopting the hue of the top layer.

> Source: [src/renderer/BlendModes.js#L169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L169)  
> Since: 3.0.0

---

## LIGHTEN

### LIGHTEN: number

**Description:**

Lighten blend mode. For Canvas only.

Retains the lightest pixels of both layers.

> Source: [src/renderer/BlendModes.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L92)  
> Since: 3.0.0

---

## LIGHTER

### LIGHTER: number

**Description:**

Lighten blend mode. For Canvas only.

Where both shapes overlap the color is determined by adding color values.

> Source: [src/renderer/BlendModes.js#L300](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L300)  
> Since: 3.0.0

---

## LUMINOSITY

### LUMINOSITY: number

**Description:**

Luminosity blend mode. For Canvas only.

Preserves the hue and chroma of the bottom layer, while adopting the luma of the top layer.

> Source: [src/renderer/BlendModes.js#L202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L202)  
> Since: 3.0.0

---

## MULTIPLY

### MULTIPLY: number

**Description:**

Multiply blend mode. For Canvas and WebGL.

The pixels are of the top layer are multiplied with the corresponding pixel of the bottom layer. A darker picture is the result.

> Source: [src/renderer/BlendModes.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L48)  
> Since: 3.0.0

---

## NORMAL

### NORMAL: number

**Description:**

Normal blend mode. For Canvas and WebGL.

This is the default setting and draws new shapes on top of the existing canvas content.

> Source: [src/renderer/BlendModes.js#L26](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L26)  
> Since: 3.0.0

---

## OVERLAY

### OVERLAY: number

**Description:**

Overlay blend mode. For Canvas only.

A combination of multiply and screen. Dark parts on the base layer become darker, and light parts become lighter.

> Source: [src/renderer/BlendModes.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L70)  
> Since: 3.0.0

---

## SATURATION

### SATURATION: number

**Description:**

Saturation blend mode. For Canvas only.

Preserves the luma and hue of the bottom layer, while adopting the chroma of the top layer.

> Source: [src/renderer/BlendModes.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L180)  
> Since: 3.0.0

---

## SCREEN

### SCREEN: number

**Description:**

Screen blend mode. For Canvas and WebGL.

The pixels are inverted, multiplied, and inverted again. A lighter picture is the result (opposite of multiply)

> Source: [src/renderer/BlendModes.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L59)  
> Since: 3.0.0

---

## SKIP\_CHECK

### SKIP\_CHECK: number

**Description:**

Skips the Blend Mode check in the renderer.

> Source: [src/renderer/BlendModes.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L16)  
> Since: 3.0.0

---

## SOFT\_LIGHT

### SOFT\_LIGHT: number

**Description:**

Soft Light blend mode. For Canvas only.

A softer version of hard-light. Pure black or white does not result in pure black or white.

> Source: [src/renderer/BlendModes.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L136)  
> Since: 3.0.0

---

## SOURCE\_ATOP

### SOURCE\_ATOP: number

**Description:**

Source-out blend mode. For Canvas only.

The new shape is only drawn where it overlaps the existing canvas content.

> Source: [src/renderer/BlendModes.js#L245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L245)  
> Since: 3.0.0

---

## SOURCE\_IN

### SOURCE\_IN: number

**Description:**

Source-in blend mode. For Canvas only.

The new shape is drawn only where both the new shape and the destination canvas overlap. Everything else is made transparent.

> Source: [src/renderer/BlendModes.js#L223](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L223)  
> Since: 3.0.0

---

## SOURCE\_OUT

### SOURCE\_OUT: number

**Description:**

Source-out blend mode. For Canvas only.

The new shape is drawn where it doesn't overlap the existing canvas content.

> Source: [src/renderer/BlendModes.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L234)  
> Since: 3.0.0

---

## XOR

### XOR: number

**Description:**

Xor blend mode. For Canvas only.

Shapes are made transparent where both overlap and drawn normal everywhere else.

> Source: [src/renderer/BlendModes.js#L322](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/BlendModes.js#L322)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [ADD](#add)

    - [ADD: number](#add-number)
  + [COLOR](#color)

    - [COLOR: number](#color-number)
  + [COLOR\_BURN](#color_burn)

    - [COLOR\_BURN: number](#color_burn-number)
  + [COLOR\_DODGE](#color_dodge)

    - [COLOR\_DODGE: number](#color_dodge-number)
  + [COPY](#copy)

    - [COPY: number](#copy-number)
  + [DARKEN](#darken)

    - [DARKEN: number](#darken-number)
  + [DESTINATION\_ATOP](#destination_atop)

    - [DESTINATION\_ATOP: number](#destination_atop-number)
  + [DESTINATION\_IN](#destination_in)

    - [DESTINATION\_IN: number](#destination_in-number)
  + [DESTINATION\_OUT](#destination_out)

    - [DESTINATION\_OUT: number](#destination_out-number)
  + [DESTINATION\_OVER](#destination_over)

    - [DESTINATION\_OVER: number](#destination_over-number)
  + [DIFFERENCE](#difference)

    - [DIFFERENCE: number](#difference-number)
  + [ERASE](#erase)

    - [ERASE: number](#erase-number)
  + [EXCLUSION](#exclusion)

    - [EXCLUSION: number](#exclusion-number)
  + [HARD\_LIGHT](#hard_light)

    - [HARD\_LIGHT: number](#hard_light-number)
  + [HUE](#hue)

    - [HUE: number](#hue-number)
  + [LIGHTEN](#lighten)

    - [LIGHTEN: number](#lighten-number)
  + [LIGHTER](#lighter)

    - [LIGHTER: number](#lighter-number)
  + [LUMINOSITY](#luminosity)

    - [LUMINOSITY: number](#luminosity-number)
  + [MULTIPLY](#multiply)

    - [MULTIPLY: number](#multiply-number)
  + [NORMAL](#normal)

    - [NORMAL: number](#normal-number)
  + [OVERLAY](#overlay)

    - [OVERLAY: number](#overlay-number)
  + [SATURATION](#saturation)

    - [SATURATION: number](#saturation-number)
  + [SCREEN](#screen)

    - [SCREEN: number](#screen-number)
  + [SKIP\_CHECK](#skip_check)

    - [SKIP\_CHECK: number](#skip_check-number)
  + [SOFT\_LIGHT](#soft_light)

    - [SOFT\_LIGHT: number](#soft_light-number)
  + [SOURCE\_ATOP](#source_atop)

    - [SOURCE\_ATOP: number](#source_atop-number)
  + [SOURCE\_IN](#source_in)

    - [SOURCE\_IN: number](#source_in-number)
  + [SOURCE\_OUT](#source_out)

    - [SOURCE\_OUT: number](#source_out-number)
  + [XOR](#xor)

    - [XOR: number](#xor-number)

Back to top

©2025[Phaser](https://docs.phaser.io)