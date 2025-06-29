# Types.GameObjects.Text

Phaser.Types.GameObjects.Text

## GetTextSizeObject

### <static> GetTextSizeObject

Results object from a call to GetTextSize.

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of the longest line in the Text object. |
| --- | --- | --- | --- |
| height | number | No | The height of the Text object. |
| lines | number | No | The number of lines in the Text object. |
| lineWidths | Array.<number> | No | An array of the lines for each line in the Text object. |
| lineSpacing | number | No | The line spacing of the Text object. |
| lineHeight | number | No | The height of a line factoring in font and stroke. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.Text

> Source: [src/gameobjects/text/typedefs/GetTextSizeObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/typedefs/GetTextSizeObject.js#L1)  
> Since: 3.0.0

---

## TextConfig

### <static> TextConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| text | string | Array.<string> | Yes | The text this Text object will display. |
| --- | --- | --- | --- |
| style | [Phaser.Types.GameObjects.Text.TextStyle](types-gameobjects-text.md) | Yes | The Text style configuration object. |
| padding | [Phaser.Types.GameObjects.Text.TextPadding](types-gameobjects-text.md) | Yes | A Text Padding object. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.Text

> Source: [src/gameobjects/text/typedefs/TextConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/typedefs/TextConfig.js#L1)  
> Since: 3.0.0

---

## TextMetrics

### <static> TextMetrics

Font metrics for a Text Style object.

| name | type | optional | description |
| --- | --- | --- | --- |
| ascent | number | No | The ascent of the font. |
| --- | --- | --- | --- |
| descent | number | No | The descent of the font. |
| fontSize | number | No | The size of the font. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.Text

> Source: [src/gameobjects/text/typedefs/TextMetrics.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/typedefs/TextMetrics.js#L1)  
> Since: 3.0.0

---

## TextPadding

### <static> TextPadding

A Text Padding configuration object as used by the Text Style.

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | Yes | If set this value is used for both the left and right padding. |
| --- | --- | --- | --- |
| y | number | Yes | If set this value is used for both the top and bottom padding. |
| left | number | Yes | The amount of padding added to the left of the Text object. |
| right | number | Yes | The amount of padding added to the right of the Text object. |
| top | number | Yes | The amount of padding added to the top of the Text object. |
| bottom | number | Yes | The amount of padding added to the bottom of the Text object. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.Text

> Source: [src/gameobjects/text/typedefs/TextPadding.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/typedefs/TextPadding.js#L1)  
> Since: 3.18.0

---

## TextShadow

### <static> TextShadow

A Text Shadow configuration object as used by the Text Style.

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| offsetX | number | Yes | 0 | The horizontal offset of the shadow. |
| --- | --- | --- | --- | --- |
| offsetY | number | Yes | 0 | The vertical offset of the shadow. |
| color | string | Yes | "'#000'" | The color of the shadow, given as a CSS string value. |
| blur | number | Yes | 0 | The amount of blur applied to the shadow. Leave as zero for a hard shadow. |
| stroke | boolean | Yes | false | Apply the shadow to the stroke effect on the Text object? |
| fill | boolean | Yes | false | Apply the shadow to the fill effect on the Text object? |

**Type**: object

**Member of**: Phaser.Types.GameObjects.Text

> Source: [src/gameobjects/text/typedefs/TextShadow.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/typedefs/TextShadow.js#L1)  
> Since: 3.0.0

---

## TextStyle

### <static> TextStyle

A Text Style configuration object as used by the Text Game Object.

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| fontFamily | string | Yes | "'Courier'" | The font the Text object will render with. This is a Canvas style font string. |
| --- | --- | --- | --- | --- |
| fontSize | number | string | Yes | "'16px'" | The font size, as a CSS size string. |
| fontStyle | string | Yes |  | Any addition font styles, such as 'bold'. |
| font | string | Yes |  | The font family or font settings to set. Overrides the other font settings. |
| backgroundColor | string | Yes |  | A solid fill color that is rendered behind the Text object. Given as a CSS string color such as `#ff0`. |
| color | string | CanvasGradient | CanvasPattern | Yes | "'#fff'" |
| stroke | string | CanvasGradient | CanvasPattern | Yes | "'#fff'" |
| strokeThickness | number | Yes | 0 | The thickness of the stroke around the Text. Set to zero for no stroke. |
| shadow | [Phaser.Types.GameObjects.Text.TextShadow](types-gameobjects-text.md) | Yes |  | The Text shadow configuration object. |
| padding | [Phaser.Types.GameObjects.Text.TextPadding](types-gameobjects-text.md) | Yes |  | A Text Padding object. |
| align | string | Yes | "'left'" | The alignment of the Text. This only impacts multi-line text. Either `left`, `right`, `center` or `justify`. |
| maxLines | number | Yes | 0 | The maximum number of lines to display within the Text object. |
| fixedWidth | number | Yes | 0 | Force the Text object to have the exact width specified in this property. Leave as zero for it to change accordingly to content. |
| fixedHeight | number | Yes | 0 | Force the Text object to have the exact height specified in this property. Leave as zero for it to change accordingly to content. |
| resolution | number | Yes | 0 | Sets the resolution (DPI setting) of the Text object. Leave at zero for it to use the game resolution. |
| rtl | boolean | Yes | false | Set to `true` if this Text object should render from right-to-left. |
| testString | string | Yes | "'|MÃ‰qgy'" | This is the string used to aid Canvas in calculating the height of the font. |
| baselineX | number | Yes | 1.2 | The amount of horizontal padding added to the width of the text when calculating the font metrics. |
| baselineY | number | Yes | 1.4 | The amount of vertical padding added to the height of the text when calculating the font metrics. |
| wordWrap | [Phaser.Types.GameObjects.Text.TextWordWrap](types-gameobjects-text.md) | Yes |  | The Text Word wrap configuration object. |
| metrics | [Phaser.Types.GameObjects.Text.TextMetrics](types-gameobjects-text.md) | Yes |  | A Text Metrics object. Use this to avoid expensive font size calculations in text heavy games. |
| lineSpacing | number | Yes |  | The amount to add to the font height to achieve the overall line height. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.Text

> Source: [src/gameobjects/text/typedefs/TextStyle.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/typedefs/TextStyle.js#L1)  
> Since: 3.0.0

---

## TextWordWrap

### <static> TextWordWrap

A Text Word Wrap configuration object as used by the Text Style configuration.

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | Yes |  | The width at which text should be considered for word-wrapping. |
| --- | --- | --- | --- | --- |
| callback | TextStyleWordWrapCallback | Yes |  | Provide a custom callback when word wrapping is enabled. |
| callbackScope | any | Yes |  | The context in which the word wrap callback is invoked. |
| useAdvancedWrap | boolean | Yes | false | Use basic or advanced word wrapping? |

**Type**: object

**Member of**: Phaser.Types.GameObjects.Text

> Source: [src/gameobjects/text/typedefs/TextWordWrap.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/typedefs/TextWordWrap.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.GameObjects.Text](#typesgameobjectstext)

  + [GetTextSizeObject](#gettextsizeobject)

    - [<static> GetTextSizeObject](#static-gettextsizeobject)
  + [TextConfig](#textconfig)

    - [<static> TextConfig](#static-textconfig)
  + [TextMetrics](#textmetrics)

    - [<static> TextMetrics](#static-textmetrics)
  + [TextPadding](#textpadding)

    - [<static> TextPadding](#static-textpadding)
  + [TextShadow](#textshadow)

    - [<static> TextShadow](#static-textshadow)
  + [TextStyle](#textstyle)

    - [<static> TextStyle](#static-textstyle)
  + [TextWordWrap](#textwordwrap)

    - [<static> TextWordWrap](#static-textwordwrap)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.GameObjects.Text