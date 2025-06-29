# TextStyle

Phaser.GameObjects.TextStyle

A TextStyle class manages all of the style settings for a Text object.

Text Game Objects create a TextStyle instance automatically, which is

accessed via the `Text.style` property. You do not normally need to

instantiate one yourself.

**Constructor**

`new TextStyle(text, style)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| text | [Phaser.GameObjects.Text](gameobjects-text.md) | No | The Text object that this TextStyle is styling. |
| --- | --- | --- | --- |
| style | [Phaser.Types.GameObjects.Text.TextStyle](../typedef/types-gameobjects-text.md) | No | The style settings to set. |

---

**Scope**: static

> Source: [src/gameobjects/text/TextStyle.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L43)  
> Since: 3.0.0

# Public Members

## align

### align: string

**Description:**

The text alignment.

> Source: [src/gameobjects/text/TextStyle.js#L202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L202)  
> Since: 3.0.0

---

## backgroundColor

### backgroundColor: string

**Description:**

The background color.

> Source: [src/gameobjects/text/TextStyle.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L103)  
> Since: 3.0.0

---

## baselineX

### baselineX: number

**Description:**

The amount of horizontal padding added to the width of the text when calculating the font metrics.

> Source: [src/gameobjects/text/TextStyle.js#L277](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L277)  
> Since: 3.3.0

---

## baselineY

### baselineY: number

**Description:**

The amount of vertical padding added to the height of the text when calculating the font metrics.

> Source: [src/gameobjects/text/TextStyle.js#L287](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L287)  
> Since: 3.3.0

---

## color

### color: string, CanvasGradient, CanvasPattern

**Description:**

The text fill color.

> Source: [src/gameobjects/text/TextStyle.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L112)  
> Since: 3.0.0

---

## fixedHeight

### fixedHeight: number

**Description:**

The fixed height of the text.

`0` means no fixed height.

> Source: [src/gameobjects/text/TextStyle.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L234)  
> Since: 3.0.0

---

## fixedWidth

### fixedWidth: number

**Description:**

The fixed width of the text.

`0` means no fixed with.

> Source: [src/gameobjects/text/TextStyle.js#L222](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L222)  
> Since: 3.0.0

---

## fontFamily

### fontFamily: string

**Description:**

The font family.

> Source: [src/gameobjects/text/TextStyle.js#L74](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L74)  
> Since: 3.0.0

---

## fontSize

### fontSize: string, number

**Description:**

The font size.

> Source: [src/gameobjects/text/TextStyle.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L84)  
> Since: 3.0.0

---

## fontStyle

### fontStyle: string

**Description:**

The font style.

> Source: [src/gameobjects/text/TextStyle.js#L94](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L94)  
> Since: 3.0.0

---

## maxLines

### maxLines: number

**Description:**

The maximum number of lines to draw.

> Source: [src/gameobjects/text/TextStyle.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L212)  
> Since: 3.0.0

---

## parent

### parent: [Phaser.GameObjects.Text](gameobjects-text.md)

**Description:**

The Text object that this TextStyle is styling.

> Source: [src/gameobjects/text/TextStyle.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L65)  
> Since: 3.0.0

---

## resolution

### resolution: number

**Description:**

The resolution the text is rendered to its internal canvas at.

The default is 0, which means it will use the resolution set in the Game Config.

> Source: [src/gameobjects/text/TextStyle.js#L246](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L246)  
> Since: 3.12.0

---

## rtl

### rtl: boolean

**Description:**

Whether the text should render right to left.

> Source: [src/gameobjects/text/TextStyle.js#L257](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L257)  
> Since: 3.0.0

---

## shadowBlur

### shadowBlur: number

**Description:**

The shadow blur radius.

> Source: [src/gameobjects/text/TextStyle.js#L172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L172)  
> Since: 3.0.0

---

## shadowColor

### shadowColor: string

**Description:**

The shadow color.

> Source: [src/gameobjects/text/TextStyle.js#L162](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L162)  
> Since: 3.0.0

---

## shadowFill

### shadowFill: boolean

**Description:**

Whether shadow fill is enabled or not.

> Source: [src/gameobjects/text/TextStyle.js#L192](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L192)  
> Since: 3.0.0

---

## shadowOffsetX

### shadowOffsetX: number

**Description:**

The horizontal shadow offset.

> Source: [src/gameobjects/text/TextStyle.js#L142](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L142)  
> Since: 3.0.0

---

## shadowOffsetY

### shadowOffsetY: number

**Description:**

The vertical shadow offset.

> Source: [src/gameobjects/text/TextStyle.js#L152](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L152)  
> Since: 3.0.0

---

## shadowStroke

### shadowStroke: boolean

**Description:**

Whether shadow stroke is enabled or not.

> Source: [src/gameobjects/text/TextStyle.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L182)  
> Since: 3.0.0

---

## stroke

### stroke: string, CanvasGradient, CanvasPattern

**Description:**

The text stroke color.

> Source: [src/gameobjects/text/TextStyle.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L122)  
> Since: 3.0.0

---

## strokeThickness

### strokeThickness: number

**Description:**

The text stroke thickness.

> Source: [src/gameobjects/text/TextStyle.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L132)  
> Since: 3.0.0

---

## testString

### testString: string

**Description:**

The test string to use when measuring the font.

> Source: [src/gameobjects/text/TextStyle.js#L267](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L267)  
> Since: 3.0.0

---

## wordWrapCallback

### wordWrapCallback: TextStyleWordWrapCallback, null

**Description:**

A custom function that will be responsible for wrapping the text. It will receive two

arguments: text (the string to wrap), textObject (this Text instance). It should return

the wrapped lines either as an array of lines or as a string with newline characters in

place to indicate where breaks should happen. Setting this directly will not re-run the

word wrapping algorithm. To change the callback and re-wrap, use

[Phaser.GameObjects.TextStyle#setWordWrapCallback](gameobjects-textstyle.md).

> Source: [src/gameobjects/text/TextStyle.js#L309](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L309)  
> Since: 3.24.0

---

## wordWrapCallbackScope

### wordWrapCallbackScope: object, null

**Description:**

The scope that will be applied when the wordWrapCallback is invoked. Setting this directly will not re-run the

word wrapping algorithm. To change the callback and re-wrap, use

[Phaser.GameObjects.TextStyle#setWordWrapCallback](gameobjects-textstyle.md).

> Source: [src/gameobjects/text/TextStyle.js#L324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L324)  
> Since: 3.24.0

---

## wordWrapUseAdvanced

### wordWrapUseAdvanced: boolean

**Description:**

Whether or not to use the advanced wrapping algorithm. If true, spaces are collapsed and

whitespace is trimmed from lines. If false, spaces and whitespace are left as is. Setting

this property directly will not re-run the word wrapping algorithm. To change the

advanced setting and re-wrap, use [Phaser.GameObjects.TextStyle#setWordWrapWidth](gameobjects-textstyle.md).

> Source: [src/gameobjects/text/TextStyle.js#L336](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L336)  
> Since: 3.24.0

---

## wordWrapWidth

### wordWrapWidth: number, null

**Description:**

The maximum width of a line of text in pixels. Null means no line wrapping. Setting this

property directly will not re-run the word wrapping algorithm. To change the width and

re-wrap, use [Phaser.GameObjects.TextStyle#setWordWrapWidth](gameobjects-textstyle.md).

> Source: [src/gameobjects/text/TextStyle.js#L297](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L297)  
> Since: 3.24.0

---

# Private Members

## \_font

### \_font: string

**Description:**

The font style, size and family.

**Access:** private

> Source: [src/gameobjects/text/TextStyle.js#L349](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L349)  
> Since: 3.0.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroy this Text Style.

> Source: [src/gameobjects/text/TextStyle.js#L1083](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L1083)  
> Since: 3.0.0

---

## getTextMetrics

### <instance> getTextMetrics()

**Description:**

Get the current text metrics.

**Returns:** [Phaser.Types.GameObjects.Text.TextMetrics](../typedef/types-gameobjects-text.md) - The text metrics.

> Source: [src/gameobjects/text/TextStyle.js#L1042](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L1042)  
> Since: 3.0.0

---

## setAlign

### <instance> setAlign([align])

**Description:**

Set the alignment of the text in this Text object.

The argument can be one of: `left`, `right`, `center` or `justify`.

Alignment only works if the Text object has more than one line of text.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| align | string | Yes | "'left'" | The text alignment for multi-line text. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L1000](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L1000)  
> Since: 3.0.0

---

## setBackgroundColor

### <instance> setBackgroundColor(color)

**Description:**

Set the background color.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| color | string | No | The background color. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L712](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L712)  
> Since: 3.0.0

---

## setColor

### <instance> setColor(color)

**Description:**

Set the text fill color.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| color | string | CanvasGradient | CanvasPattern | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L746](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L746)  
> Since: 3.0.0

---

## setFill

### <instance> setFill(color)

**Description:**

Set the text fill color.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| color | string | CanvasGradient | CanvasPattern | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L729](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L729)  
> Since: 3.0.0

---

## setFixedSize

### <instance> setFixedSize(width, height)

**Description:**

Set a fixed width and height for the text.

Pass in `0` for either of these parameters to disable fixed width or height respectively.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The fixed width to set. |
| --- | --- | --- | --- |
| height | number | No | The fixed height to set. |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L681](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L681)  
> Since: 3.0.0

---

## setFont

### <instance> setFont(font, [updateText])

**Description:**

Set the font.

If a string is given, the font family is set.

If an object is given, the `fontFamily`, `fontSize` and `fontStyle`

properties of that object are set.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| font | string | object | No |  | The font family or font settings to set. |
| --- | --- | --- | --- | --- |
| updateText | boolean | Yes | true | Whether to update the text immediately. |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L537](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L537)  
> Since: 3.0.0

---

## setFontFamily

### <instance> setFontFamily(family)

**Description:**

Set the font family.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| family | string | No | The font family. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L593](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L593)  
> Since: 3.0.0

---

## setFontSize

### <instance> setFontSize(size)

**Description:**

Set the font size. Can be a string with a valid CSS unit, i.e. `16px`, or a number.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| size | number | string | No | The font size. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L637](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L637)  
> Since: 3.0.0

---

## setFontStyle

### <instance> setFontStyle(style)

**Description:**

Set the font style.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| style | string | No | The font style. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L615](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L615)  
> Since: 3.0.0

---

## setMaxLines

### <instance> setMaxLines([max])

**Description:**

Set the maximum number of lines to draw.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| max | number | Yes | 0 | The maximum number of lines to draw. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L1023](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L1023)  
> Since: 3.0.0

---

## setResolution

### <instance> setResolution(value)

**Description:**

Set the resolution used by the Text object.

It allows for much clearer text on High DPI devices, at the cost of memory because

it uses larger internal Canvas textures for the Text.

Please use with caution, as the more high res Text you have, the more memory it uses up.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The resolution for this Text object to use. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L763](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L763)  
> Since: 3.12.0

---

## setShadow

### <instance> setShadow([x], [y], [color], [blur], [shadowStroke], [shadowFill])

**Description:**

Set the shadow settings.

Calling this method always re-measures the parent Text object,

so only call it when you actually change the shadow settings.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal shadow offset. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical shadow offset. |
| color | string | Yes | "'#000'" | The shadow color. |
| blur | number | Yes | 0 | The shadow blur radius. |
| shadowStroke | boolean | Yes | false | Whether to stroke the shadow. |
| shadowFill | boolean | Yes | true | Whether to fill the shadow. |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L818](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L818)  
> Since: 3.0.0

---

## setShadowBlur

### <instance> setShadowBlur([blur])

**Description:**

Set the shadow blur radius.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| blur | number | Yes | 0 | The shadow blur radius. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L896](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L896)  
> Since: 3.0.0

---

## setShadowColor

### <instance> setShadowColor([color])

**Description:**

Set the shadow color.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color | string | Yes | "'#000'" | The shadow color. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L877](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L877)  
> Since: 3.0.0

---

## setShadowFill

### <instance> setShadowFill(enabled)

**Description:**

Enable or disable shadow fill.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| enabled | boolean | No | Whether shadow fill is enabled or not. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L932](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L932)  
> Since: 3.0.0

---

## setShadowOffset

### <instance> setShadowOffset([x], [y])

**Description:**

Set the shadow offset.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal shadow offset. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical shadow offset. |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L855](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L855)  
> Since: 3.0.0

---

## setShadowStroke

### <instance> setShadowStroke(enabled)

**Description:**

Enable or disable shadow stroke.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| enabled | boolean | No | Whether shadow stroke is enabled or not. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L915](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L915)  
> Since: 3.0.0

---

## setStroke

### <instance> setStroke(color, thickness)

**Description:**

Set the stroke settings.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| color | string | CanvasGradient | CanvasPattern | No |
| --- | --- | --- | --- |
| thickness | number | No | The stroke thickness. |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L785](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L785)  
> Since: 3.0.0

---

## setStyle

### <instance> setStyle(style, [updateText], [setDefaults])

**Description:**

Set the text style.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| style | [Phaser.Types.GameObjects.Text.TextStyle](../typedef/types-gameobjects-text.md) | No |  | The style settings to set. |
| --- | --- | --- | --- | --- |
| updateText | boolean | Yes | true | Whether to update the text immediately. |
| setDefaults | boolean | Yes | false | Use the default values if not set, or the local values. |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L363](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L363)  
> Since: 3.0.0

---

## setTestString

### <instance> setTestString(string)

**Description:**

Set the test string to use when measuring the font.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| string | string | No | The test string to use when measuring the font. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L664](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L664)  
> Since: 3.0.0

---

## setWordWrapCallback

### <instance> setWordWrapCallback(callback, [scope])

**Description:**

Set a custom callback for wrapping lines.

Pass in null to remove wrapping by callback.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| callback | TextStyleWordWrapCallback | No |  | A custom function that will be responsible for wrapping the text. It will receive two arguments: text (the string to wrap), textObject (this Text instance). It should return the wrapped lines either as an array of lines or as a string with newline characters in place to indicate where breaks should happen. |
| --- | --- | --- | --- | --- |
| scope | object | Yes | null | The scope that will be applied when the callback is invoked. |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L974](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L974)  
> Since: 3.0.0

---

## setWordWrapWidth

### <instance> setWordWrapWidth(width, [useAdvancedWrap])

**Description:**

Set the width (in pixels) to use for wrapping lines.

Pass in null to remove wrapping by width.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | null | No |  | The maximum width of a line in pixels. Set to null to remove wrapping. |
| --- | --- | --- | --- | --- |
| useAdvancedWrap | boolean | Yes | false | Whether or not to use the advanced wrapping algorithm. If true, spaces are collapsed and whitespace is trimmed from lines. If false, spaces and whitespace are left as is. |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L949](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L949)  
> Since: 3.0.0

---

## syncFont

### <instance> syncFont(canvas, context)

**Description:**

Synchronize the font settings to the given Canvas Rendering Context.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| canvas | HTMLCanvasElement | No | The Canvas Element. |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | No | The Canvas Rendering Context. |

> Source: [src/gameobjects/text/TextStyle.js#L453](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L453)  
> Since: 3.0.0

---

## syncShadow

### <instance> syncShadow(context, enabled)

**Description:**

Synchronize the shadow settings to the given Canvas Rendering Context.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | No | The Canvas Rendering Context. |
| --- | --- | --- | --- |
| enabled | boolean | No | Whether shadows are enabled or not. |

> Source: [src/gameobjects/text/TextStyle.js#L488](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L488)  
> Since: 3.0.0

---

## syncStyle

### <instance> syncStyle(canvas, context)

**Description:**

Synchronize the text style settings to the given Canvas Rendering Context.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| canvas | HTMLCanvasElement | No | The Canvas Element. |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | No | The Canvas Rendering Context. |

> Source: [src/gameobjects/text/TextStyle.js#L467](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L467)  
> Since: 3.0.0

---

## toJSON

### <instance> toJSON()

**Description:**

Build a JSON representation of this Text Style.

**Returns:** object - A JSON representation of this Text Style.

> Source: [src/gameobjects/text/TextStyle.js#L1061](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L1061)  
> Since: 3.0.0

---

## update

### <instance> update(recalculateMetrics)

**Description:**

Update the style settings for the parent Text object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| recalculateMetrics | boolean | No | Whether to recalculate font and text metrics. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The parent Text object.

> Source: [src/gameobjects/text/TextStyle.js#L515](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextStyle.js#L515)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [align](#align)

    - [align: string](#align-string)
  + [backgroundColor](#backgroundcolor)

    - [backgroundColor: string](#backgroundcolor-string)
  + [baselineX](#baselinex)

    - [baselineX: number](#baselinex-number)
  + [baselineY](#baseliney)

    - [baselineY: number](#baseliney-number)
  + [color](#color)

    - [color: string, CanvasGradient, CanvasPattern](#color-string-canvasgradient-canvaspattern)
  + [fixedHeight](#fixedheight)

    - [fixedHeight: number](#fixedheight-number)
  + [fixedWidth](#fixedwidth)

    - [fixedWidth: number](#fixedwidth-number)
  + [fontFamily](#fontfamily)

    - [fontFamily: string](#fontfamily-string)
  + [fontSize](#fontsize)

    - [fontSize: string, number](#fontsize-string-number)
  + [fontStyle](#fontstyle)

    - [fontStyle: string](#fontstyle-string)
  + [maxLines](#maxlines)

    - [maxLines: number](#maxlines-number)
  + [parent](#parent)

    - [parent: Phaser.GameObjects.Text](#parent-phasergameobjectstext)
  + [resolution](#resolution)

    - [resolution: number](#resolution-number)
  + [rtl](#rtl)

    - [rtl: boolean](#rtl-boolean)
  + [shadowBlur](#shadowblur)

    - [shadowBlur: number](#shadowblur-number)
  + [shadowColor](#shadowcolor)

    - [shadowColor: string](#shadowcolor-string)
  + [shadowFill](#shadowfill)

    - [shadowFill: boolean](#shadowfill-boolean)
  + [shadowOffsetX](#shadowoffsetx)

    - [shadowOffsetX: number](#shadowoffsetx-number)
  + [shadowOffsetY](#shadowoffsety)

    - [shadowOffsetY: number](#shadowoffsety-number)
  + [shadowStroke](#shadowstroke)

    - [shadowStroke: boolean](#shadowstroke-boolean)
  + [stroke](#stroke)

    - [stroke: string, CanvasGradient, CanvasPattern](#stroke-string-canvasgradient-canvaspattern)
  + [strokeThickness](#strokethickness)

    - [strokeThickness: number](#strokethickness-number)
  + [testString](#teststring)

    - [testString: string](#teststring-string)
  + [wordWrapCallback](#wordwrapcallback)

    - [wordWrapCallback: TextStyleWordWrapCallback, null](#wordwrapcallback-textstylewordwrapcallback-null)
  + [wordWrapCallbackScope](#wordwrapcallbackscope)

    - [wordWrapCallbackScope: object, null](#wordwrapcallbackscope-object-null)
  + [wordWrapUseAdvanced](#wordwrapuseadvanced)

    - [wordWrapUseAdvanced: boolean](#wordwrapuseadvanced-boolean)
  + [wordWrapWidth](#wordwrapwidth)

    - [wordWrapWidth: number, null](#wordwrapwidth-number-null)
* [Private Members](#private-members)

  + [\_font](#_font)

    - [\_font: string](#_font-string)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [getTextMetrics](#gettextmetrics)

    - [<instance> getTextMetrics()](#instance-gettextmetrics)
  + [setAlign](#setalign)

    - [<instance> setAlign([align])](#instance-setalignalign)
  + [setBackgroundColor](#setbackgroundcolor)

    - [<instance> setBackgroundColor(color)](#instance-setbackgroundcolorcolor)
  + [setColor](#setcolor)

    - [<instance> setColor(color)](#instance-setcolorcolor)
  + [setFill](#setfill)

    - [<instance> setFill(color)](#instance-setfillcolor)
  + [setFixedSize](#setfixedsize)

    - [<instance> setFixedSize(width, height)](#instance-setfixedsizewidth-height)
  + [setFont](#setfont)

    - [<instance> setFont(font, [updateText])](#instance-setfontfont-updatetext)
  + [setFontFamily](#setfontfamily)

    - [<instance> setFontFamily(family)](#instance-setfontfamilyfamily)
  + [setFontSize](#setfontsize)

    - [<instance> setFontSize(size)](#instance-setfontsizesize)
  + [setFontStyle](#setfontstyle)

    - [<instance> setFontStyle(style)](#instance-setfontstylestyle)
  + [setMaxLines](#setmaxlines)

    - [<instance> setMaxLines([max])](#instance-setmaxlinesmax)
  + [setResolution](#setresolution)

    - [<instance> setResolution(value)](#instance-setresolutionvalue)
  + [setShadow](#setshadow)

    - [<instance> setShadow([x], [y], [color], [blur], [shadowStroke], [shadowFill])](#instance-setshadowx-y-color-blur-shadowstroke-shadowfill)
  + [setShadowBlur](#setshadowblur)

    - [<instance> setShadowBlur([blur])](#instance-setshadowblurblur)
  + [setShadowColor](#setshadowcolor)

    - [<instance> setShadowColor([color])](#instance-setshadowcolorcolor)
  + [setShadowFill](#setshadowfill)

    - [<instance> setShadowFill(enabled)](#instance-setshadowfillenabled)
  + [setShadowOffset](#setshadowoffset)

    - [<instance> setShadowOffset([x], [y])](#instance-setshadowoffsetx-y)
  + [setShadowStroke](#setshadowstroke)

    - [<instance> setShadowStroke(enabled)](#instance-setshadowstrokeenabled)
  + [setStroke](#setstroke)

    - [<instance> setStroke(color, thickness)](#instance-setstrokecolor-thickness)
  + [setStyle](#setstyle)

    - [<instance> setStyle(style, [updateText], [setDefaults])](#instance-setstylestyle-updatetext-setdefaults)
  + [setTestString](#setteststring)

    - [<instance> setTestString(string)](#instance-setteststringstring)
  + [setWordWrapCallback](#setwordwrapcallback)

    - [<instance> setWordWrapCallback(callback, [scope])](#instance-setwordwrapcallbackcallback-scope)
  + [setWordWrapWidth](#setwordwrapwidth)

    - [<instance> setWordWrapWidth(width, [useAdvancedWrap])](#instance-setwordwrapwidthwidth-useadvancedwrap)
  + [syncFont](#syncfont)

    - [<instance> syncFont(canvas, context)](#instance-syncfontcanvas-context)
  + [syncShadow](#syncshadow)

    - [<instance> syncShadow(context, enabled)](#instance-syncshadowcontext-enabled)
  + [syncStyle](#syncstyle)

    - [<instance> syncStyle(canvas, context)](#instance-syncstylecanvas-context)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [update](#update)

    - [<instance> update(recalculateMetrics)](#instance-updaterecalculatemetrics)

Back to top

©2025[Phaser](https://docs.phaser.io)



TextStyle