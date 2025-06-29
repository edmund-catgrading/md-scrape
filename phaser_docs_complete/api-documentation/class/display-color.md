# Color

Phaser.Display.Color

The Color class holds a single color value and allows for easy modification and reading of it.

**Constructor**

`new Color([red], [green], [blue], [alpha])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| red | number | Yes | 0 | The red color value. A number between 0 and 255. |
| --- | --- | --- | --- | --- |
| green | number | Yes | 0 | The green color value. A number between 0 and 255. |
| blue | number | Yes | 0 | The blue color value. A number between 0 and 255. |
| alpha | number | Yes | 255 | The alpha value. A number between 0 and 255. |

---

**Scope**: static

> Source: [src/display/color/Color.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L17)  
> Since: 3.0.0

# Public Members

## alpha

### alpha: number

**Description:**

The alpha color value, normalized to the range 0 to 255.

> Source: [src/display/color/Color.js#L756](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L756)  
> Since: 3.0.0

---

## alphaGL

### alphaGL: number

**Description:**

The alpha color value, normalized to the range 0 to 1.

> Source: [src/display/color/Color.js#L650](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L650)  
> Since: 3.0.0

---

## blue

### blue: number

**Description:**

The blue color value, normalized to the range 0 to 255.

> Source: [src/display/color/Color.js#L729](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L729)  
> Since: 3.0.0

---

## blueGL

### blueGL: number

**Description:**

The blue color value, normalized to the range 0 to 1.

> Source: [src/display/color/Color.js#L625](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L625)  
> Since: 3.0.0

---

## color

### color: number

**Description:**

The color of this Color component, not including the alpha channel.

> Source: [src/display/color/Color.js#L524](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L524)  
> Since: 3.0.0

---

## color32

### color32: number

**Description:**

The color of this Color component, including the alpha channel.

> Source: [src/display/color/Color.js#L541](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L541)  
> Since: 3.0.0

---

## gl

### gl: Array.<number>

**Description:**

An array containing the calculated color values for WebGL use.

> Source: [src/display/color/Color.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L132)  
> Since: 3.0.0

---

## green

### green: number

**Description:**

The green color value, normalized to the range 0 to 255.

> Source: [src/display/color/Color.js#L702](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L702)  
> Since: 3.0.0

---

## greenGL

### greenGL: number

**Description:**

The green color value, normalized to the range 0 to 1.

> Source: [src/display/color/Color.js#L600](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L600)  
> Since: 3.0.0

---

## h

### h: number

**Description:**

The hue color value. A number between 0 and 1.

This is the base color.

> Source: [src/display/color/Color.js#L783](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L783)  
> Since: 3.13.0

---

## red

### red: number

**Description:**

The red color value, normalized to the range 0 to 255.

> Source: [src/display/color/Color.js#L675](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L675)  
> Since: 3.0.0

---

## redGL

### redGL: number

**Description:**

The red color value, normalized to the range 0 to 1.

> Source: [src/display/color/Color.js#L575](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L575)  
> Since: 3.0.0

---

## rgba

### rgba: string

**Description:**

The color of this Color component as a string which can be used in CSS color values.

> Source: [src/display/color/Color.js#L558](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L558)  
> Since: 3.0.0

---

## s

### s: number

**Description:**

The saturation color value. A number between 0 and 1.

This controls how much of the hue will be in the final color, where 1 is fully saturated and 0 will give you white.

> Source: [src/display/color/Color.js#L807](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L807)  
> Since: 3.13.0

---

## v

### v: number

**Description:**

The lightness color value. A number between 0 and 1.

This controls how dark the color is. Where 1 is as bright as possible and 0 is black.

> Source: [src/display/color/Color.js#L831](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L831)  
> Since: 3.13.0

---

# Private Members

## \_color

### \_color: number

**Description:**

Pre-calculated internal color value.

**Access:** private

> Source: [src/display/color/Color.js#L141](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L141)  
> Since: 3.0.0

---

## \_color32

### \_color32: number

**Description:**

Pre-calculated internal color32 value.

**Access:** private

> Source: [src/display/color/Color.js#L152](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L152)  
> Since: 3.0.0

---

## \_h

### \_h: number

**Description:**

The hue color value. A number between 0 and 1.

This is the base color.

**Access:** private

> Source: [src/display/color/Color.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L86)  
> Since: 3.13.0

---

## \_locked

### \_locked: boolean

**Description:**

Is this color update locked?

**Access:** private

> Source: [src/display/color/Color.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L122)  
> Since: 3.13.0

---

## \_rgba

### \_rgba: string

**Description:**

Pre-calculated internal color rgb string value.

**Access:** private

> Source: [src/display/color/Color.js#L163](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L163)  
> Since: 3.0.0

---

## \_s

### \_s: number

**Description:**

The saturation color value. A number between 0 and 1.

This controls how much of the hue will be in the final color, where 1 is fully saturated and 0 will give you white.

**Access:** private

> Source: [src/display/color/Color.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L98)  
> Since: 3.13.0

---

## \_v

### \_v: number

**Description:**

The lightness color value. A number between 0 and 1.

This controls how dark the color is. Where 1 is as bright as possible and 0 is black.

**Access:** private

> Source: [src/display/color/Color.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L110)  
> Since: 3.13.0

---

## a

### a: number

**Description:**

The internal alpha color value.

**Access:** private

> Source: [src/display/color/Color.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L75)  
> Since: 3.0.0

---

## b

### b: number

**Description:**

The internal blue color value.

**Access:** private

> Source: [src/display/color/Color.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L64)  
> Since: 3.0.0

---

## g

### g: number

**Description:**

The internal green color value.

**Access:** private

> Source: [src/display/color/Color.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L53)  
> Since: 3.0.0

---

## r

### r: number

**Description:**

The internal red color value.

**Access:** private

> Source: [src/display/color/Color.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L42)  
> Since: 3.0.0

---

# Public Methods

## brighten

### <instance> brighten(amount)

**Description:**

Brighten this Color by the percentage amount given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| amount | number | No | The percentage amount to change this color by. A value between 0 and 100. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L501)  
> Since: 3.13.0

---

## clone

### <instance> clone()

**Description:**

Returns a new Color component using the values from this one.

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A new Color object.

> Source: [src/display/color/Color.js#L359](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L359)  
> Since: 3.0.0

---

## ColorSpectrum

### <static> ColorSpectrum([limit])

**Description:**

Return an array of Colors in a Color Spectrum.

The spectrum colors flow in the order: red, yellow, green, blue.

By default this function will return an array with 1024 elements in.

However, you can reduce this to a smaller quantity if needed, by specitying the `limit` parameter.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| limit | number | Yes | 1024 | How many colors should be returned? The maximum is 1024 but you can set a smaller quantity if required. |
| --- | --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Types.Display.ColorObject](../typedef/types-display.md)> - An array containing `limit` parameter number of elements, where each contains a Color Object.

> Source: [src/display/color/ColorSpectrum.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/ColorSpectrum.js#L9)  
> Since: 3.50.0

---

## ColorToRGBA

### <static> ColorToRGBA(color)

**Description:**

Converts the given color value into an Object containing r,g,b and a properties.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| color | number | No | A color value, optionally including the alpha value. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md) - An object containing the parsed color values.

> Source: [src/display/color/ColorToRGBA.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/ColorToRGBA.js#L7)  
> Since: 3.0.0

---

## ComponentToHex

### <static> ComponentToHex(color)

**Description:**

Returns a string containing a hex representation of the given color component.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| color | number | No | The color channel to get the hex value for, must be a value between 0 and 255. |
| --- | --- | --- | --- |

**Returns:** string - A string of length 2 characters, i.e. 255 = ff, 100 = 64.

> Source: [src/display/color/ComponentToHex.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/ComponentToHex.js#L7)  
> Since: 3.0.0

---

## darken

### <instance> darken(amount)

**Description:**

Decrease the lightness of this Color by the percentage amount given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| amount | number | No | The percentage amount to change this color by. A value between 0 and 100. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L484](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L484)  
> Since: 3.13.0

---

## desaturate

### <instance> desaturate(amount)

**Description:**

Decrease the saturation of this Color by the percentage amount given.

The saturation is the amount of the base color in the hue.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| amount | number | No | The percentage amount to change this color by. A value between 0 and 100. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L449](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L449)  
> Since: 3.13.0

---

## GetColor

### <static> GetColor(red, green, blue)

**Description:**

Given 3 separate color values this will return an integer representation of it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| red | number | No | The red color value. A number between 0 and 255. |
| --- | --- | --- | --- |
| green | number | No | The green color value. A number between 0 and 255. |
| blue | number | No | The blue color value. A number between 0 and 255. |

**Returns:** number - The combined color value.

> Source: [src/display/color/GetColor.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/GetColor.js#L7)  
> Since: 3.0.0

---

## GetColor32

### <static> GetColor32(red, green, blue, alpha)

**Description:**

Given an alpha and 3 color values this will return an integer representation of it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| red | number | No | The red color value. A number between 0 and 255. |
| --- | --- | --- | --- |
| green | number | No | The green color value. A number between 0 and 255. |
| blue | number | No | The blue color value. A number between 0 and 255. |
| alpha | number | No | The alpha color value. A number between 0 and 255. |

**Returns:** number - The combined color value.

> Source: [src/display/color/GetColor32.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/GetColor32.js#L7)  
> Since: 3.0.0

---

## gray

### <instance> gray(shade)

**Description:**

Sets this Color object to be grayscaled based on the shade value given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| shade | number | No | A value between 0 and 255. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L372](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L372)  
> Since: 3.13.0

---

## HexStringToColor

### <static> HexStringToColor(hex)

**Description:**

Converts a hex string into a Phaser Color object.

The hex string can supplied as `'#0033ff'` or the short-hand format of `'#03f'`; it can begin with an optional "#" or "0x", or be unprefixed.

An alpha channel is *not* supported.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| hex | string | No | The hex color value to convert, such as `#0033ff` or the short-hand format: `#03f`. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object populated by the values of the given string.

> Source: [src/display/color/HexStringToColor.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/HexStringToColor.js#L9)  
> Since: 3.0.0

---

## HSLToColor

### <static> HSLToColor(h, s, l)

**Description:**

Converts HSL (hue, saturation and lightness) values to a Phaser Color object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| h | number | No | The hue value in the range 0 to 1. |
| --- | --- | --- | --- |
| s | number | No | The saturation value in the range 0 to 1. |
| l | number | No | The lightness value in the range 0 to 1. |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object created from the results of the h, s and l values.

> Source: [src/display/color/HSLToColor.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/HSLToColor.js#L10)  
> Since: 3.0.0

---

## HSVColorWheel

### <static> HSVColorWheel([s], [v])

**Description:**

Generates an HSV color wheel which is an array of 360 Color objects, for each step of the wheel.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| s | number | Yes | 1 | The saturation, in the range 0 - 1. |
| --- | --- | --- | --- | --- |
| v | number | Yes | 1 | The value, in the range 0 - 1. |

**Returns:** Array.<[Phaser.Types.Display.ColorObject](../typedef/types-display.md)> - An array containing 360 ColorObject elements, where each element contains a Color object corresponding to the color at that point in the HSV color wheel.

> Source: [src/display/color/HSVColorWheel.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/HSVColorWheel.js#L9)  
> Since: 3.0.0

---

## HSVToRGB

### <static> HSVToRGB(h, s, v, [out])

**Description:**

Converts a HSV (hue, saturation and value) color set to RGB.

Conversion formula from <https://en.wikipedia.org/wiki/HSL_and_HSV>

Assumes HSV values are contained in the set [0, 1].

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| h | number | No | The hue, in the range 0 - 1. This is the base color. |
| --- | --- | --- | --- |
| s | number | No | The saturation, in the range 0 - 1. This controls how much of the hue will be in the final color, where 1 is fully saturated and 0 will give you white. |
| v | number | No | The value, in the range 0 - 1. This controls how dark the color is. Where 1 is as bright as possible and 0 is black. |
| out | [Phaser.Types.Display.ColorObject](../typedef/types-display.md) | [Phaser.Display.Color](../namespace/display-color.md) | Yes | A Color object to store the results in. If not given a new ColorObject will be created. |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md), [Phaser.Display.Color](../namespace/display-color.md) - An object with the red, green and blue values set in the r, g and b properties.

> Source: [src/display/color/HSVToRGB.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/HSVToRGB.js#L30)  
> Since: 3.0.0

---

## HueToComponent

### <static> HueToComponent(p, q, t)

**Description:**

Converts a hue to an RGB color.

Based on code by Michael Jackson (<https://github.com/mjijackson>)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| p | number | No | No description provided |
| --- | --- | --- | --- |
| q | number | No | No description provided |
| t | number | No | No description provided |

**Returns:** number - The combined color value.

> Source: [src/display/color/HueToComponent.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/HueToComponent.js#L7)  
> Since: 3.0.0

---

## IntegerToColor

### <static> IntegerToColor(input)

**Description:**

Converts the given color value into an instance of a Color object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| input | number | No | The color value to convert into a Color object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object.

> Source: [src/display/color/IntegerToColor.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/IntegerToColor.js#L10)  
> Since: 3.0.0

---

## IntegerToRGB

### <static> IntegerToRGB(input)

**Description:**

Return the component parts of a color as an Object with the properties alpha, red, green, blue.

Alpha will only be set if it exists in the given color (0xAARRGGBB)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| input | number | No | The color value to convert into a Color object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md) - An object with the red, green and blue values set in the r, g and b properties.

> Source: [src/display/color/IntegerToRGB.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/IntegerToRGB.js#L7)  
> Since: 3.0.0

---

## lighten

### <instance> lighten(amount)

**Description:**

Increase the lightness of this Color by the percentage amount given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| amount | number | No | The percentage amount to change this color by. A value between 0 and 100. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L467](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L467)  
> Since: 3.13.0

---

## ObjectToColor

### <static> ObjectToColor(input)

**Description:**

Converts an object containing `r`, `g`, `b` and `a` properties into a Color class instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| input | [Phaser.Types.Display.InputColorObject](../typedef/types-display.md) | No | An object containing `r`, `g`, `b` and `a` properties in the range 0 to 255. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object.

> Source: [src/display/color/ObjectToColor.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/ObjectToColor.js#L9)  
> Since: 3.0.0

---

## random

### <instance> random([min], [max])

**Description:**

Sets this Color object to be a random color between the `min` and `max` values given.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| min | number | Yes | 0 | The minimum random color value. Between 0 and 255. |
| --- | --- | --- | --- | --- |
| max | number | Yes | 255 | The maximum random color value. Between 0 and 255. |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L387)  
> Since: 3.13.0

---

## randomGray

### <instance> randomGray([min], [max])

**Description:**

Sets this Color object to be a random grayscale color between the `min` and `max` values given.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| min | number | Yes | 0 | The minimum random color value. Between 0 and 255. |
| --- | --- | --- | --- | --- |
| max | number | Yes | 255 | The maximum random color value. Between 0 and 255. |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L410](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L410)  
> Since: 3.13.0

---

## RandomRGB

### <static> RandomRGB([min], [max])

**Description:**

Creates a new Color object where the r, g, and b values have been set to random values

based on the given min max values.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| min | number | Yes | 0 | The minimum value to set the random range from (between 0 and 255) |
| --- | --- | --- | --- | --- |
| max | number | Yes | 255 | The maximum value to set the random range from (between 0 and 255) |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object.

> Source: [src/display/color/RandomRGB.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/RandomRGB.js#L10)  
> Since: 3.0.0

---

## RGBStringToColor

### <static> RGBStringToColor(rgb)

**Description:**

Converts a CSS 'web' string into a Phaser Color object.

The web string can be in the format `'rgb(r,g,b)'` or `'rgba(r,g,b,a)'` where r/g/b are in the range [0..255] and a is in the range [0..1].

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rgb | string | No | The CSS format color string, using the `rgb` or `rgba` format. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object.

> Source: [src/display/color/RGBStringToColor.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/RGBStringToColor.js#L9)  
> Since: 3.0.0

---

## RGBToHSV

### <static> RGBToHSV(r, g, b, [out])

**Description:**

Converts an RGB color value to HSV (hue, saturation and value).

Conversion formula from <http://en.wikipedia.org/wiki/HSL_color_space.>

Assumes RGB values are contained in the set [0, 255] and returns h, s and v in the set [0, 1].

Based on code by Michael Jackson (<https://github.com/mjijackson>)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| r | number | No | The red color value. A number between 0 and 255. |
| --- | --- | --- | --- |
| g | number | No | The green color value. A number between 0 and 255. |
| b | number | No | The blue color value. A number between 0 and 255. |
| out | [Phaser.Types.Display.HSVColorObject](../typedef/types-display.md) | [Phaser.Display.Color](../namespace/display-color.md) | Yes | An object to store the color values in. If not given an HSV Color Object will be created. |

**Returns:** [Phaser.Types.Display.HSVColorObject](../typedef/types-display.md), [Phaser.Display.Color](../namespace/display-color.md) - An object with the properties `h`, `s` and `v` set.

> Source: [src/display/color/RGBToHSV.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/RGBToHSV.js#L7)  
> Since: 3.0.0

---

## RGBToString

### <static> RGBToString(r, g, b, [a], [prefix])

**Description:**

Converts the color values into an HTML compatible color string, prefixed with either `#` or `0x`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| r | number | No |  | The red color value. A number between 0 and 255. |
| --- | --- | --- | --- | --- |
| g | number | No |  | The green color value. A number between 0 and 255. |
| b | number | No |  | The blue color value. A number between 0 and 255. |
| a | number | Yes | 255 | The alpha value. A number between 0 and 255. |
| prefix | string | Yes | "#" | The prefix of the string. Either `#` or `0x`. |

**Returns:** string - A string-based representation of the color values.

> Source: [src/display/color/RGBToString.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/RGBToString.js#L9)  
> Since: 3.0.0

---

## saturate

### <instance> saturate(amount)

**Description:**

Increase the saturation of this Color by the percentage amount given.

The saturation is the amount of the base color in the hue.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| amount | number | No | The percentage amount to change this color by. A value between 0 and 100. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L431](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L431)  
> Since: 3.13.0

---

## setFromHSV

### <instance> setFromHSV(h, s, v)

**Description:**

Sets the color based on the hue, saturation and lightness values given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| h | number | No | The hue, in the range 0 - 1. This is the base color. |
| --- | --- | --- | --- |
| s | number | No | The saturation, in the range 0 - 1. This controls how much of the hue will be in the final color, where 1 is fully saturated and 0 will give you white. |
| v | number | No | The value, in the range 0 - 1. This controls how dark the color is. Where 1 is as bright as possible and 0 is black. |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L287](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L287)  
> Since: 3.13.0

---

## setFromRGB

### <instance> setFromRGB(color)

**Description:**

Sets the color based on the color object given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| color | [Phaser.Types.Display.InputColorObject](../typedef/types-display.md) | No | An object containing `r`, `g`, `b` and optionally `a` values in the range 0 to 255. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L259](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L259)  
> Since: 3.0.0

---

## setGLTo

### <instance> setGLTo(red, green, blue, [alpha])

**Description:**

Sets the red, green, blue and alpha GL values of this Color component.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| red | number | No |  | The red color value. A number between 0 and 1. |
| --- | --- | --- | --- | --- |
| green | number | No |  | The green color value. A number between 0 and 1. |
| blue | number | No |  | The blue color value. A number between 0 and 1. |
| alpha | number | Yes | 1 | The alpha value. A number between 0 and 1. |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L230](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L230)  
> Since: 3.0.0

---

## setTo

### <instance> setTo(red, green, blue, [alpha], [updateHSV])

**Description:**

Sets the color of this Color component.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| red | number | No |  | The red color value. A number between 0 and 255. |
| --- | --- | --- | --- | --- |
| green | number | No |  | The green color value. A number between 0 and 255. |
| blue | number | No |  | The blue color value. A number between 0 and 255. |
| alpha | number | Yes | 255 | The alpha value. A number between 0 and 255. |
| updateHSV | boolean | Yes | true | Update the HSV values after setting the RGB values? |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L199)  
> Since: 3.0.0

---

## transparent

### <instance> transparent()

**Description:**

Sets this color to be transparent. Sets all values to zero.

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L177](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L177)  
> Since: 3.0.0

---

## ValueToColor

### <static> ValueToColor(input)

**Description:**

Converts the given source color value into an instance of a Color class.

The value can be either a string, prefixed with `rgb` or a hex string, a number or an Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| input | string | number | [Phaser.Types.Display.InputColorObject](../typedef/types-display.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object.

> Source: [src/display/color/ValueToColor.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/ValueToColor.js#L12)  
> Since: 3.0.0

---

# Private Methods

## update

### <instance> update()

**Description:**

Updates the internal cache values.

**Access:** private

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L304](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L304)  
> Since: 3.0.0

---

## updateHSV

### <instance> updateHSV()

**Description:**

Updates the internal hsv cache values.

**Access:** private

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - This Color object.

> Source: [src/display/color/Color.js#L339](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Color.js#L339)  
> Since: 3.13.0

---

# Namespaces:

* [Interpolate](../namespace/display-color-interpolate.md)

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [alphaGL](#alphagl)

    - [alphaGL: number](#alphagl-number)
  + [blue](#blue)

    - [blue: number](#blue-number)
  + [blueGL](#bluegl)

    - [blueGL: number](#bluegl-number)
  + [color](#color)

    - [color: number](#color-number)
  + [color32](#color32)

    - [color32: number](#color32-number)
  + [gl](#gl)

    - [gl: Array.<number>](#gl-arraynumber)
  + [green](#green)

    - [green: number](#green-number)
  + [greenGL](#greengl)

    - [greenGL: number](#greengl-number)
  + [h](#h)

    - [h: number](#h-number)
  + [red](#red)

    - [red: number](#red-number)
  + [redGL](#redgl)

    - [redGL: number](#redgl-number)
  + [rgba](#rgba)

    - [rgba: string](#rgba-string)
  + [s](#s)

    - [s: number](#s-number)
  + [v](#v)

    - [v: number](#v-number)
* [Private Members](#private-members)

  + [\_color](#_color)

    - [\_color: number](#_color-number)
  + [\_color32](#_color32)

    - [\_color32: number](#_color32-number)
  + [\_h](#_h)

    - [\_h: number](#_h-number)
  + [\_locked](#_locked)

    - [\_locked: boolean](#_locked-boolean)
  + [\_rgba](#_rgba)

    - [\_rgba: string](#_rgba-string)
  + [\_s](#_s)

    - [\_s: number](#_s-number)
  + [\_v](#_v)

    - [\_v: number](#_v-number)
  + [a](#a)

    - [a: number](#a-number)
  + [b](#b)

    - [b: number](#b-number)
  + [g](#g)

    - [g: number](#g-number)
  + [r](#r)

    - [r: number](#r-number)
* [Public Methods](#public-methods)

  + [brighten](#brighten)

    - [<instance> brighten(amount)](#instance-brightenamount)
  + [clone](#clone)

    - [<instance> clone()](#instance-clone)
  + [ColorSpectrum](#colorspectrum)

    - [<static> ColorSpectrum([limit])](#static-colorspectrumlimit)
  + [ColorToRGBA](#colortorgba)

    - [<static> ColorToRGBA(color)](#static-colortorgbacolor)
  + [ComponentToHex](#componenttohex)

    - [<static> ComponentToHex(color)](#static-componenttohexcolor)
  + [darken](#darken)

    - [<instance> darken(amount)](#instance-darkenamount)
  + [desaturate](#desaturate)

    - [<instance> desaturate(amount)](#instance-desaturateamount)
  + [GetColor](#getcolor)

    - [<static> GetColor(red, green, blue)](#static-getcolorred-green-blue)
  + [GetColor32](#getcolor32)

    - [<static> GetColor32(red, green, blue, alpha)](#static-getcolor32red-green-blue-alpha)
  + [gray](#gray)

    - [<instance> gray(shade)](#instance-grayshade)
  + [HexStringToColor](#hexstringtocolor)

    - [<static> HexStringToColor(hex)](#static-hexstringtocolorhex)
  + [HSLToColor](#hsltocolor)

    - [<static> HSLToColor(h, s, l)](#static-hsltocolorh-s-l)
  + [HSVColorWheel](#hsvcolorwheel)

    - [<static> HSVColorWheel([s], [v])](#static-hsvcolorwheels-v)
  + [HSVToRGB](#hsvtorgb)

    - [<static> HSVToRGB(h, s, v, [out])](#static-hsvtorgbh-s-v-out)
  + [HueToComponent](#huetocomponent)

    - [<static> HueToComponent(p, q, t)](#static-huetocomponentp-q-t)
  + [IntegerToColor](#integertocolor)

    - [<static> IntegerToColor(input)](#static-integertocolorinput)
  + [IntegerToRGB](#integertorgb)

    - [<static> IntegerToRGB(input)](#static-integertorgbinput)
  + [lighten](#lighten)

    - [<instance> lighten(amount)](#instance-lightenamount)
  + [ObjectToColor](#objecttocolor)

    - [<static> ObjectToColor(input)](#static-objecttocolorinput)
  + [random](#random)

    - [<instance> random([min], [max])](#instance-randommin-max)
  + [randomGray](#randomgray)

    - [<instance> randomGray([min], [max])](#instance-randomgraymin-max)
  + [RandomRGB](#randomrgb)

    - [<static> RandomRGB([min], [max])](#static-randomrgbmin-max)
  + [RGBStringToColor](#rgbstringtocolor)

    - [<static> RGBStringToColor(rgb)](#static-rgbstringtocolorrgb)
  + [RGBToHSV](#rgbtohsv)

    - [<static> RGBToHSV(r, g, b, [out])](#static-rgbtohsvr-g-b-out)
  + [RGBToString](#rgbtostring)

    - [<static> RGBToString(r, g, b, [a], [prefix])](#static-rgbtostringr-g-b-a-prefix)
  + [saturate](#saturate)

    - [<instance> saturate(amount)](#instance-saturateamount)
  + [setFromHSV](#setfromhsv)

    - [<instance> setFromHSV(h, s, v)](#instance-setfromhsvh-s-v)
  + [setFromRGB](#setfromrgb)

    - [<instance> setFromRGB(color)](#instance-setfromrgbcolor)
  + [setGLTo](#setglto)

    - [<instance> setGLTo(red, green, blue, [alpha])](#instance-setgltored-green-blue-alpha)
  + [setTo](#setto)

    - [<instance> setTo(red, green, blue, [alpha], [updateHSV])](#instance-settored-green-blue-alpha-updatehsv)
  + [transparent](#transparent)

    - [<instance> transparent()](#instance-transparent)
  + [ValueToColor](#valuetocolor)

    - [<static> ValueToColor(input)](#static-valuetocolorinput)
* [Private Methods](#private-methods)

  + [update](#update)

    - [<instance> update()](#instance-update)
  + [updateHSV](#updatehsv)

    - [<instance> updateHSV()](#instance-updatehsv)
* [Namespaces:](#namespaces)

Back to top

©2025[Phaser](https://docs.phaser.io)