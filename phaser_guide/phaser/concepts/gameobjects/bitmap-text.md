# Bitmap Text

A Guide to creating and using Bitmap Text in Phaser

A Bitmap Text Game Object is created from a bitmap based texture file such as a PNG file. This texture contains each character arranged in a fixed structure. The following image is an example of a Bitmap Text texture file:

![image](https://cdn.hashnode.com/res/hashnode/image/upload/v1749042988436/bdda3853-15c4-4408-b4bb-6c1112a9481d.png?auto=compress,format&format=webp)

The texture file is nearly always accompanied by an XML or JSON based file that describes the font structure. This file contains the positions of each character in the texture, so the renderer knows how to cut them out, along with kerning data.

Because the font comes from a texture, there is no worrying about if it's installed on the users system. Or about loading it such as with Web Fonts. However, as a result of being drawn from a texture, you are more limited in what you can do with them. For example, you cannot do things like apply a stroke or fill pattern to a Bitmap Text. Also, you are limited to only the characters in the texture file, so if your game needs to support multiple languages, it has to cater for this in the font textures directly.

On the plus side, under WebGL Bitmap Texts are extremely fast to render and unlike Text Game Objects, you don't incur any speed penalty when updating their content because the underlying texture doesn't change. You can also create visually impressive fonts by preparing them in an image editor, applying fills and any other effect required. As you can see in the image above, this style would be extremely hard to achieve with a Web Font.

## Bitmap Text Creation Software

To create a Bitmap Text data files you need a 3rd party app. Here are four of the most common:

* [BMFont](http://www.angelcode.com/products/bmfont/) (Windows, free)
* [Glyph Designer](https://www.71squared.com/en/glyphdesigner) (macOS, commercial)
* [SnowB BMF](https://snowb.org/) (web-based, free)
* [Littera](http://kvazars.com/littera/) (Flash-based - yes, really, free)

In most use cases it is recommended to use the XML file format. For example, BMFont generates its data as XML. When it saves the files they have a `.fnt` extension, but you can simply rename them to `.xml`.

If you wish to use JSON, the formatting should be equal to the result of converting a valid XML file through the popular X2JS library. An online tool for conversion can be found on the [Code Beautify](https://codebeautify.org/xmltojson) site.

### From an image and font data

Bitmap font generators make an image and XML data file. Use `load.bitmapFont()`:

```
Copythis.load.bitmapFont('key', 'font.png', 'font.xml');

```

To create multi-line text insert \r, \n or \r\n escape codes into the text string.

### From an atlas and font data

Load the image and XML data separately, then call `ParseFromAtlas()` to create the font.

* [bitmap text from atlas](https://labs.phaser.io/edit.html?src=src/game%20objects/bitmaptext/static/bitmaptext-atlas.js)

### From a "retro font" image

Load the image and then call `RetroFont.Parse()` with the [font data](../../../docs/latest/Phaser.Types.GameObjects.BitmapText.RetroFontConfig.md).

* [retro text 1](https://labs.phaser.io/view.html?src=src%5Cgame%20objects%5Cbitmaptext%5Cretro%20font%5Cretro%20text%201.js)

## Bitmap text

These are game objects that display text using the font. There are two classes, [BitmapText](../../../docs/latest/Phaser.GameObjects.BitmapText.md) and [DynamicBitmapText](../../../docs/latest/Phaser.GameObjects.DynamicBitmapText.md). They are both "dynamic" in the sense that you can change the text contents at any time. The difference is that DynamicBitmapText has [callbacks](../../../docs/latest/Phaser.Types.GameObjects.BitmapText.DisplayCallbackConfig.md) for per-character rendering effects and [scrolling](https://labs.phaser.io/view.html?src=src%5Cgame%20objects%5Cbitmaptext%5Cdynamic%5Cvertical%20scroller.js).

### Load bitmap font

* Load bitmap font from texture and xml configuration

  ```
  Copythis.load.bitmapFont(key, textureURL, xmlURL);

  ```

  + Reference: [load bitmap font](../loader.md)
  + Loaded texture also can be used for [Image](#load-bitmap-font), [Sprite](#load-bitmap-font), or [Arcade Image](../physics/arcade.md), [Arcade Sprite](../physics/arcade.md)

    ```
    Copy```js
    this.add.image(x, y, key, char);
    ```

    ```

* Load retro bitmap font from texture and JSON configuration
  1. Load texture in *preload* stage

     ```
     Copythis.load.image(key, url);

     ```

     Reference: [load image](../loader.md)
  2. Add retro bitmap font

     ```
     Copyvar config = {
         // image
         image: '',
         offset: {
             x: 0,
             y: 0
         },
         // characters
         width: 32,
         height: 32,
         chars: '',
         charsPerRow: 10,
         // spacing
         spacing: {
             x: 0,
             y: 0
         },
         lineSpacing: 0
     }
     this.cache.bitmapFont.add(key, Phaser.GameObjects.RetroFont.Parse(scene, config));

     ```

     + Image :
       - `image` : The key of the image containing the font.
       - `offset` : If the font set doesn't start at the top left of the given image, specify the X/Y coordinate offset here.
     + Characters :
       - `width` : The width of each character in the font set.
       - `height` : The height of each character in the font set.
       - `chars` : The characters used in the font set, in display order.
         * [Default characters set](#default-characters-set-of-retro-font)
       - `charsPerRow` : The number of characters per row in the font set. If not given charsPerRow will be the image width / characterWidth.
     + Spacing :
       - `spacing` : If the characters in the font set have horizontal/vertical spacing between them set the required amount here.
       - `lineSpacing` : The amount of vertical space to add to the line height of the font.

### Add bitmap text object

```
Copyvar txt = this.add.bitmapText(x, y, key, text);
// var txt = this.add.bitmapText(x, y, key, text, size, align);

```

* `size` : The size of the font
* `align` : The alignment of the text in a *multi-line* BitmapText object.
  + `0` : Left aligned (default)
  + `1` : Middle aligned
  + `2` : Right aligned

Add text from JSON

```
Copyvar txt = this.make.bitmapText({
    x: 0,
    y: 0,
    text: 'Text\nGame Object\nCreated from config',
    font: '',
    size: false,
    align: 0,
    // origin: {x: 0.5, y: 0.5},
    add: true
});

```

### Custom class

* Define class

  ```
  Copyclass MyText extends Phaser.GameObjects.BitmapText {
      constructor(scene, x, y, key, text, size, align) {
          super(scene, x, y, key, text, size, align);
          // ...
          this.add.existing(this);
      }
      // ...

      // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar txt = new MyText(scene, x, y, key, text);

  ```

### Set text

```
Copytxt.setText('...');

```

or

```
Copytxt.text = '...';

```

### Set align

* Left aligned

  ```
  Copytxt.setLeftAlign();

  ```

* Middle aligned

  ```
  Copytxt.setCenterAlign();

  ```
* Right aligned

  ```
  Copytxt.setRightAlign();

  ```

or

```
Copytxt.align = align;

```

* `align` :
  + `0` : Left aligned (default)
  + `1` : Middle aligned
  + `2` : Right aligned

### Set letter spacing

```
Copytxt.setLetterSpacing(spacing);

```

or

```
Copytxt.letterSpacing = spacing;

```

Can be a positive value to increase the space, or negative to reduce it.

### Set line spacing

```
Copytxt.setLineSpacing(spacing);

```

or

```
Copytxt.lineSpacing = spacing;

```

Can be a positive value to increase the space, or negative to reduce it.

### Set font size

```
Copytxt.setFontSize(size);

```

or

```
Copytxt.fontSize = size;

```

### Set font

```
Copytxt.setFont(key);
// txt.setFont(key, size, align);

```

### Tint

See [Tint](../gameobjects.md).

### Color of characters

* By character

  ```
  Copytxt.setCharacterTint(start, length, tintFill, color);
  // txt.setCharacterTint(start, length, tintFill, topLeft, topRight, bottomLeft, bottomRight);

  ```

  + `start` : Index starting character.
    - `< 0` : Counts back from the end of the text.
  + `length` : Number of characters to tint.
    - `-1` : All characters from `start`
  + `tintFill` :
    - `true` : Fill-based tint
    - `false` : Additive tint
  + `color`, or `topLeft, topRight, bottomLeft, bottomRight` : Color integer.
* By word

  ```
  Copytxt.setWordTint(word, count, tintFill, color);
  // txt.setWordTint(word, count, tintFill, topLeft, topRight, bottomLeft, bottomRight);

  ```

  + `word` : The word to search for.
    - A string
    - An index of the word in the words array.
  + `count` : Number of matching words to tint.
    - `-1` : All matching words
  + `tintFill` :
    - `true` : Fill-based tint
    - `false` : Additive tint
  + `color`, or `topLeft, topRight, bottomLeft, bottomRight` : Color integer.

### Drop shadow effect

```
Copytxt.setDropShadow(x, y, color, alpha);

```

or

```
Copytxt.dropShadowX = x;
txt.dropShadowY = y;
txt.dropShadowColor = color;
txt.dropShadowAlpha = alpha;

```

* `x`, `y` : The horizontal/vertical offset of the drop shadow.
* `color` : The color of the drop shadow.
* `alpha` : The alpha of the drop shadow.

!!! note
WebGL only

### Wrap

* Wrap

  ```
  Copytxt.setMaxWidth(width);
  // txt.setMaxWidth(width, wordWrapCharCode);

  ```

  + `width` : Line width in pixels.
  + `wordWrapCharCode` : The character code to check for when word wrapping. Defaults to 32 (the *space* character)
* Disable wrapping

  ```
  Copytxt.setMaxWidth(0);

  ```

### Get bounds

```
Copyvar width = txt.width;
var height = txt.height;

```

or

```
Copyvar bounds = txt.getTextBounds(round);
// bounds = {
//     local: {
//         x: 0,
//         y: 0,
//         width: 0,
//         height: 0
//     },
//     global: {
//         x: 0,
//         y: 0,
//         width: 0,
//         height: 0
//     },
//     lines: {
//         shortest: 0,
//         longest: 0,
//         lengths: null,
//         height: 0
//     },
//     wrappedText: '',
//     words: [],
//     characters: [],
//     scaleX: 0,
//     scaleY: 0
// };

```

* `round` : Set `true` to round the results to the nearest integer.
* `local` : The BitmapText based on fontSize and 0x0 coords.
* `global` : The BitmapText, taking into account scale and world position.
* `lines` : The BitmapText line data.
* `wrappedText` : Wrapped content joined with `'\n'`.
* `characters` : Information of each character.

  ```
  Copy{
      char, code, i, idx, x, y, w, h, t, b, r, line
  }

  ```

  + `char` : Character (string).
  + `code`: Character code (number)
  + `i` : Index of character
  + `x` , `y` : World position of this character
  + `w`, `h` : Width/height of this character
  + `t`, `b` : The top/bottom of the line this character is on.
  + `r` : The right-most point of this character, including xAdvance.
  + `line` : The line number the character appears on.
* `words` : Information of each word.

  ```
  Copy{
      word, i, x, y, w, h, cr

  }

  ```

  + `word` : Word string.
  + `i` : Index of start character
  + `x`, `y` : World position of start character
  + `w` , `h` : Width/height of word
  + `cr` : Is last word of current line
* `scaleX`, `scaleY` : Scale of width and height.

#### Get information of character

```
Copyvar data = txt.getCharacterAt(x, y);
// var data = txt.getCharacterAt(x, y, camera);

```

* `x`, `y` : World position.
* `camera` : The Camera which is being tested against.
* `data` : Information of character at world position.

  ```
  Copy{
      char, code, i, x, y, w, h, t, b, r, line
  }

  ```

  + `char` : Character (string).
  + `code`: Character code (number)
  + `i` : Index of character
  + `x` , `y` : World position of this character
  + `w`, `h` : Width/height of this character
  + `t`, `b` : The top/bottom of the line this character is on.
  + `r` : The right-most point of this character, including xAdvance.
  + `line` : The line number the character appears on.

### Other properties

See [game object](../gameobjects.md)

### Create mask

```
Copyvar mask = txt.createBitmapMask();

```

### Shader effects

Only supports postFX effects.

## Appendix

### Default characters set of retro font

* `Phaser.GameObjects.RetroFont.TEXT_SET1` :

  ```
  Copy' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

  ```

* `Phaser.GameObjects.RetroFont.TEXT_SET2` :

  ```
  Copy' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  ```
* `Phaser.GameObjects.RetroFont.TEXT_SET3` :

  ```
  Copy'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '

  ```
* `Phaser.GameObjects.RetroFont.TEXT_SET4` :

  ```
  Copy'ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789'

  ```
* `Phaser.GameObjects.RetroFont.TEXT_SET5` :

  ```
  Copy'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,/() \'!?-*:0123456789'

  ```
* `Phaser.GameObjects.RetroFont.TEXT_SET6` :

  ```
  Copy'ABCDEFGHIJKLMNOPQRSTUVWXYZ!?:;0123456789"(),-.\' '

  ```
* `Phaser.GameObjects.RetroFont.TEXT_SET7` :

  ```
  Copy'AGMSY+:4BHNTZ!;5CIOU.?06DJPV,(17EKQW")28FLRX-\'39'

  ```
* `Phaser.GameObjects.RetroFont.TEXT_SET8` :

  ```
  Copy'0123456789 .ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  ```
* `Phaser.GameObjects.RetroFont.TEXT_SET9` :

  ```
  Copy'ABCDEFGHIJKLMNOPQRSTUVWXYZ()-0123456789.:,\'"?!'

  ```
* `Phaser.GameObjects.RetroFont.TEXT_SET10` :

  ```
  Copy'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  ```
* `Phaser.GameObjects.RetroFont.TEXT_SET11` :

  ```
  Copy'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,"-+!?()\':;0123456789'

  ```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)
* [samme](https://github.com/samme)

Updated on June 4, 2025, 1:16 PM UTC

---

[Game Object Factories](factories.md)

[Blitter](blitter.md)

On this page

* [Bitmap Text](#bitmap-text)

  + [Bitmap Text Creation Software](#bitmap-text-creation-software)

    - [From an image and font data](#from-an-image-and-font-data)
    - [From an atlas and font data](#from-an-atlas-and-font-data)
    - [From a "retro font" image](#from-a-retro-font-image)
  + [Bitmap text](#bitmap-text)

    - [Load bitmap font](#load-bitmap-font)
    - [Add bitmap text object](#add-bitmap-text-object)
    - [Custom class](#custom-class)
    - [Set text](#set-text)
    - [Set align](#set-align)
    - [Set letter spacing](#set-letter-spacing)
    - [Set line spacing](#set-line-spacing)
    - [Set font size](#set-font-size)
    - [Set font](#set-font)
    - [Tint](#tint)
    - [Color of characters](#color-of-characters)
    - [Drop shadow effect](#drop-shadow-effect)
    - [Wrap](#wrap)
    - [Get bounds](#get-bounds)
    - [Other properties](#other-properties)
    - [Create mask](#create-mask)
    - [Shader effects](#shader-effects)
  + [Appendix](#appendix)

    - [Default characters set of retro font](#default-characters-set-of-retro-font)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)