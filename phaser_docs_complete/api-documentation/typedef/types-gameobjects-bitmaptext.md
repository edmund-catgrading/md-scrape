# Types.GameObjects.BitmapText

Phaser.Types.GameObjects.BitmapText

## BitmapFontCharacterData

### <static> BitmapFontCharacterData

The font data for an individual character of a Bitmap Font.

Describes the character's position, size, offset and kerning.

As of version 3.50 it also includes the WebGL texture uv data.

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the character. |
| --- | --- | --- | --- |
| y | number | No | The y position of the character. |
| width | number | No | The width of the character. |
| height | number | No | The height of the character. |
| centerX | number | No | The center x position of the character. |
| centerY | number | No | The center y position of the character. |
| xOffset | number | No | The x offset of the character. |
| yOffset | number | No | The y offset of the character. |
| u0 | number | No | WebGL texture u0. |
| v0 | number | No | WebGL texture v0. |
| u1 | number | No | WebGL texture u1. |
| v1 | number | No | WebGL texture v1. |
| data | object | No | Extra data for the character. |
| kerning | Object.<number> | No | Kerning values, keyed by character code. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/BitmapFontCharacterData.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/BitmapFontCharacterData.js#L1)  
> Since: 3.0.0

---

## BitmapFontData

### <static> BitmapFontData

Bitmap Font data that can be used by a BitmapText Game Object.

| name | type | optional | description |
| --- | --- | --- | --- |
| font | string | No | The name of the font. |
| --- | --- | --- | --- |
| size | number | No | The size of the font. |
| lineHeight | number | No | The line height of the font. |
| retroFont | boolean | No | Whether this font is a retro font (monospace). |
| chars | Object.<number, [Phaser.Types.GameObjects.BitmapText.BitmapFontCharacterData](types-gameobjects-bitmaptext.md)> | No | The character data of the font, keyed by character code. Each character datum includes a position, size, offset and more. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/BitmapFontData.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/BitmapFontData.js#L1)  
> Since: 3.0.0

---

## BitmapTextCharacter

### <static> BitmapTextCharacter

A single entry from the `BitmapTextSize` characters array.

The position and dimensions take the font size into account,

but are not translated into the local space of the Game Object itself.

| name | type | optional | description |
| --- | --- | --- | --- |
| i | number | No | The index of this character within the BitmapText wrapped text string. |
| --- | --- | --- | --- |
| idx | number | No | The index of this character within the BitmapText text string. |
| char | string | No | The character. |
| code | number | No | The character code of the character. |
| x | number | No | The x position of the character in the BitmapText. |
| y | number | No | The y position of the character in the BitmapText. |
| w | number | No | The width of the character. |
| h | number | No | The height of the character. |
| t | number | No | The top of the line this character is on. |
| r | number | No | The right-most point of this character, including xAdvance. |
| b | number | No | The bottom of the line this character is on. |
| line | number | No | The line number the character appears on. |
| glyph | [Phaser.Types.GameObjects.BitmapText.BitmapFontCharacterData](types-gameobjects-bitmaptext.md) | No | Reference to the glyph object this character is using. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/BitmapTextCharacter.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/BitmapTextCharacter.js#L1)  
> Since: 3.50.0

---

## BitmapTextConfig

### <static> BitmapTextConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| font | string | Yes | "''" | The key of the font to use from the BitmapFont cache. |
| --- | --- | --- | --- | --- |
| text | string | Yes | "''" | The string, or array of strings, to be set as the content of this Bitmap Text. |
| size | number | false | Yes | false | The font size to set. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/BitmapTextConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/BitmapTextConfig.js#L1)  
> Since: 3.0.0

---

## BitmapTextLines

### <static> BitmapTextLines

Details about the line data in the `BitmapTextSize` object.

| name | type | optional | description |
| --- | --- | --- | --- |
| shortest | number | No | The width of the shortest line of text. |
| --- | --- | --- | --- |
| longest | number | No | The width of the longest line of text. |
| height | number | No | The height of a line of text. |
| lengths | Array.<number> | No | An array where each entry contains the length of that line of text. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/BitmapTextLines.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/BitmapTextLines.js#L1)  
> Since: 3.50.0

---

## BitmapTextSize

### <static> BitmapTextSize

| name | type | optional | description |
| --- | --- | --- | --- |
| global | [Phaser.Types.GameObjects.BitmapText.GlobalBitmapTextSize](types-gameobjects-bitmaptext.md) | No | The position and size of the BitmapText, taking into account the position and scale of the Game Object. |
| --- | --- | --- | --- |
| local | [Phaser.Types.GameObjects.BitmapText.LocalBitmapTextSize](types-gameobjects-bitmaptext.md) | No | The position and size of the BitmapText, taking just the font size into account. |
| lines | [Phaser.Types.GameObjects.BitmapText.BitmapTextLines](types-gameobjects-bitmaptext.md) | No | Data about the lines of text within the BitmapText. |
| characters | Array.<[Phaser.Types.GameObjects.BitmapText.BitmapTextCharacter](types-gameobjects-bitmaptext.md)> | No | An array containing per-character data. Only populated if `includeChars` is `true` in the `getTextBounds` call. |
| words | Array.<[Phaser.Types.GameObjects.BitmapText.BitmapTextWord](types-gameobjects-bitmaptext.md)> | No | An array containing the word data from the BitmapText. |
| scale | number | No | The scale of the BitmapText font being rendered vs. font size in the text data. |
| scaleX | number | No | The scale X value of the BitmapText. |
| scaleY | number | No | The scale Y value of the BitmapText. |
| wrappedText | string | No | The wrapped text, if wrapping enabled and required. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/BitmapTextSize.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/BitmapTextSize.js#L1)  
> Since: 3.0.0

---

## BitmapTextWord

### <static> BitmapTextWord

Details about a single world entry in the `BitmapTextSize` object words array.

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the word in the BitmapText. |
| --- | --- | --- | --- |
| y | number | No | The y position of the word in the BitmapText. |
| w | number | No | The width of the word. |
| h | number | No | The height of the word. |
| i | number | No | The index of the first character of this word within the entire string. Note: this index factors in spaces, quotes, carriage-returns, etc. |
| word | string | No | The word. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/BitmapTextWord.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/BitmapTextWord.js#L1)  
> Since: 3.50.0

---

## DisplayCallbackConfig

### <static> DisplayCallbackConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | [Phaser.GameObjects.DynamicBitmapText](../class/gameobjects-dynamicbitmaptext.md) | No | The Dynamic Bitmap Text object that owns this character being rendered. |
| --- | --- | --- | --- |
| tint | [Phaser.Types.GameObjects.BitmapText.TintConfig](types-gameobjects-bitmaptext.md) | No | The tint of the character being rendered. Always zero in Canvas. |
| index | number | No | The index of the character being rendered. |
| charCode | number | No | The character code of the character being rendered. |
| x | number | No | The x position of the character being rendered. |
| y | number | No | The y position of the character being rendered. |
| scale | number | No | The scale of the character being rendered. |
| rotation | number | No | The rotation of the character being rendered. |
| data | any | No | Custom data stored with the character being rendered. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L1)  
> Since: 3.0.0

---

## DisplayCallback

### <static> DisplayCallback

**Type**: function

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L16)

---

## GlobalBitmapTextSize

### <static> GlobalBitmapTextSize

The position and size of the Bitmap Text in global space, taking into account the Game Object's scale and world position.

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the BitmapText, taking into account the x position and scale of the Game Object. |
| --- | --- | --- | --- |
| y | number | No | The y position of the BitmapText, taking into account the y position and scale of the Game Object. |
| width | number | No | The width of the BitmapText, taking into account the x scale of the Game Object. |
| height | number | No | The height of the BitmapText, taking into account the y scale of the Game Object. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/GlobalBitmapTextSize.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/GlobalBitmapTextSize.js#L1)  
> Since: 3.0.0

---

## JSONBitmapText

### <static> JSONBitmapText

| name | type | optional | description |
| --- | --- | --- | --- |
| font | string | No | The name of the font. |
| --- | --- | --- | --- |
| text | string | No | The text that this Bitmap Text displays. |
| fontSize | number | No | The size of the font. |
| letterSpacing | number | No | Adds / Removes spacing between characters. |
| lineSpacing | number | No | Adds / Removes spacing between lines in multi-line text. |
| align | number | No | The alignment of the text in a multi-line BitmapText object. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/JSONBitmapText.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/JSONBitmapText.js#L1)  
> Since: 3.0.0

---

## LocalBitmapTextSize

### <static> LocalBitmapTextSize

The position and size of the Bitmap Text in local space, taking just the font size into account.

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the BitmapText. |
| --- | --- | --- | --- |
| y | number | No | The y position of the BitmapText. |
| width | number | No | The width of the BitmapText. |
| height | number | No | The height of the BitmapText. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/LocalBitmapTextSize.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/LocalBitmapTextSize.js#L1)  
> Since: 3.0.0

---

## RetroFontConfig

### <static> RetroFontConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| image | string | No | The key of the image containing the font. |
| --- | --- | --- | --- |
| offset.x | number | No | If the font set doesn't start at the top left of the given image, specify the X coordinate offset here. |
| offset.y | number | No | If the font set doesn't start at the top left of the given image, specify the Y coordinate offset here. |
| width | number | No | The width of each character in the font set. |
| height | number | No | The height of each character in the font set. |
| chars | string | No | The characters used in the font set, in display order. You can use the TEXT\_SET consts for common font set arrangements. |
| charsPerRow | number | No | The number of characters per row in the font set. If not given charsPerRow will be the image width / characterWidth. |
| spacing.x | number | No | If the characters in the font set have horizontal spacing between them set the required amount here. |
| spacing.y | number | No | If the characters in the font set have vertical spacing between them set the required amount here. |
| lineSpacing | number | No | The amount of vertical space to add to the line height of the font. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/RetroFontConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/RetroFontConfig.js#L1)  
> Since: 3.6.0

---

## TintConfig

### <static> TintConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| topLeft | number | No | The top left tint value. Always zero in canvas. |
| --- | --- | --- | --- |
| topRight | number | No | The top right tint value. Always zero in canvas. |
| bottomLeft | number | No | The bottom left tint value. Always zero in canvas. |
| bottomRight | number | No | The bottom right tint value. Always zero in canvas. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.BitmapText

> Source: [src/gameobjects/bitmaptext/typedefs/TintConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/typedefs/TintConfig.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.GameObjects.BitmapText](#typesgameobjectsbitmaptext)

  + [BitmapFontCharacterData](#bitmapfontcharacterdata)

    - [<static> BitmapFontCharacterData](#static-bitmapfontcharacterdata)
  + [BitmapFontData](#bitmapfontdata)

    - [<static> BitmapFontData](#static-bitmapfontdata)
  + [BitmapTextCharacter](#bitmaptextcharacter)

    - [<static> BitmapTextCharacter](#static-bitmaptextcharacter)
  + [BitmapTextConfig](#bitmaptextconfig)

    - [<static> BitmapTextConfig](#static-bitmaptextconfig)
  + [BitmapTextLines](#bitmaptextlines)

    - [<static> BitmapTextLines](#static-bitmaptextlines)
  + [BitmapTextSize](#bitmaptextsize)

    - [<static> BitmapTextSize](#static-bitmaptextsize)
  + [BitmapTextWord](#bitmaptextword)

    - [<static> BitmapTextWord](#static-bitmaptextword)
  + [DisplayCallbackConfig](#displaycallbackconfig)

    - [<static> DisplayCallbackConfig](#static-displaycallbackconfig)
  + [DisplayCallback](#displaycallback)

    - [<static> DisplayCallback](#static-displaycallback)
  + [GlobalBitmapTextSize](#globalbitmaptextsize)

    - [<static> GlobalBitmapTextSize](#static-globalbitmaptextsize)
  + [JSONBitmapText](#jsonbitmaptext)

    - [<static> JSONBitmapText](#static-jsonbitmaptext)
  + [LocalBitmapTextSize](#localbitmaptextsize)

    - [<static> LocalBitmapTextSize](#static-localbitmaptextsize)
  + [RetroFontConfig](#retrofontconfig)

    - [<static> RetroFontConfig](#static-retrofontconfig)
  + [TintConfig](#tintconfig)

    - [<static> TintConfig](#static-tintconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.GameObjects.BitmapText