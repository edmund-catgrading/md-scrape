# Text

A Guide to the Phaser Text Game Object

Text objects work by creating their own internal hidden Canvas and then renders text to it using the standard Canvas `fillText` API. It then creates a texture from this canvas which is rendered to your game during the render pass.

Because it uses the Canvas API you can take advantage of all the features this offers, such as applying gradient fills to the text, or strokes, shadows and more. You can also use custom fonts loaded externally, such as Google or TypeKit Web fonts.

Important: The font name must be quoted if it contains certain combinations of digits or special characters, either when creating the Text object, or when setting the font via `setFont` or `setFontFamily`, e.g.:

```
Copythis.add.text(0, 0, 'Hello World', { fontFamily: 'Georgia, "Goudy Bookletter 1911", Times, serif' });

```

```
Copythis.add.text(0, 0, 'Hello World', { font: '"Press Start 2P"' });

```

You can only display fonts that are currently loaded and available to the browser: therefore fonts must be pre-loaded. Phaser does not do this for you, so you will require the use of a 3rd party font loader, or have the fonts ready available in the CSS on the page in which your Phaser game resides.

See [this](http://www.jordanm.co.uk/tinytype) for the available default fonts across mobile browsers.

A note on performance: Every time the contents of a Text object changes, i.e. changing the text being displayed, or the style of the text, it needs to remake the Text canvas, and if on WebGL, re-upload the new texture to the GPU. This can be an expensive operation if used often, or with large quantities of Text objects in your game. If you run into performance issues you would be better off using Bitmap Text instead, as it benefits from batching and avoids expensive Canvas API calls.

## Add text object

```
Copyvar txt = this.add.text(x, y, 'hello');
// var txt = this.add.text(x, y, 'hello', { fontFamily: 'Arial', fontSize: 64, color: '#00ff00' });

```

Default style

```
Copy{
    fontFamily: 'Courier',
    fontSize: '16px',
    fontStyle: '',
    backgroundColor: null,
    color: '#fff',
    stroke: '#fff',
    strokeThickness: 0,
    shadow: {
        offsetX: 0,
        offsetY: 0,
        color: '#000',
        blur: 0,
        stroke: false,
        fill: false
    },
    align: 'left',  // 'left'|'center'|'right'|'justify'
    padding: {
        left: 0,
        right: 0,
        top: 0,
        bottom: 0,
    },
    maxLines: 0,
    lineSpacing: 0,
    fixedWidth: 0,
    fixedHeight: 0,
    rtl: false,
    testString: '|MÉqgy',
    wordWrap: {
        width: null,
        callback: null,
        callbackScope: null,
        useAdvancedWrap: false
    },
    metrics: false,
    // metrics: {
    //     ascent: 0,
    //     descent: 0,
    //     fontSize: 0
    // },
}

```

Add text from JSON

```
Copyvar txt = this.make.text({
    x: 100,
    y: 100,
    padding: {
        left: 64,
        right: 16,
        top: 20,
        bottom: 40
        //x: 32,    // 32px padding on the left/right
        //y: 16     // 16px padding on the top/bottom
    },
    text: 'Text\nGame Object\nCreated from config',
    style: {
        fontSize: '64px',
        fontFamily: 'Arial',
        color: '#ffffff',
        align: 'center',  // 'left'|'center'|'right'|'justify'
        backgroundColor: '#ff00ff'
    },
    // origin: {x: 0.5, y: 0.5},
    add: true
});

```

## Custom class

* Define class

  ```
  Copyclass MyText extends Phaser.GameObjects.Text {
      constructor(scene, x, y, text, style) {
          super(scene, x, y, text, style);
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
  Copyvar txt = new MyText(scene, x, y, 'hello');

  ```

## Word wrap

* Wrap by width

  ```
  Copyvar txt = this.make.text({
      x: 400,
      y: 100,
      text: 'The sky above the port was the color of television, tuned to a dead channel.',
      origin: { x: 0.5, y: 0.5 },
      style: {
          font: 'bold 25px Arial',
          fill: 'white',
          wordWrap: { width: 300 }
      },
      // origin: {x: 0.5, y: 0.5},
  });

  ```
* Wrap by callback

  ```
  Copyvar txt = this.make.text({
      x: 400,
      y: 300,
      text: 'The sky above the port was the color of television, tuned to a dead channel.',
      origin: 0.5,
      style: {
          font: 'bold 30px Arial',
          fill: 'white',
          wordWrap: { callback: wordWrap, scope: this }
      },
      // origin: {x: 0.5, y: 0.5},
  });

  function wordWrap (text, textObject)
  {
      // First parameter will be the string that needs to be wrapped
      // Second parameter will be the Text game object that is being wrapped currently

      // This wrap just puts each word on a separate line, but you could inject your own
      // language-specific logic here.
      var words = text.split(' ');

      // You can return either an array of individual lines or a string with line breaks (e.g. \n) in
      // the correct place.
      return words;
  }

  ```
* Wrap width

  + Get

    ```
    Copyvar width = txt.style.wordWrapWidth;
    var useAdvancedWrap = txt.style.wordWrapUseAdvanced;

    ```
  + Set

    ```
    Copytxt.setWordWrapWidth(width);
    // txt.setWordWrapWidth(width, useAdvancedWrap);

    ```
* Wrap callback

  + Get

    ```
    Copyvar callback = txt.style.wordWrapCallback;
    var scope = txt.style.wordWrapCallbackScope;

    ```
  + Set

    ```
    Copytxt.setWordWrapCallback(callback, scope);

    ```

## Content

* Get

  ```
  Copyvar content = txt.text;

  ```
* Set

  ```
  Copytxt.setText(text);
  // txt.text = text;

  ```
* Append

  ```
  Copytxt.appendText(text);
  // txt.text += '\n' + text;

  ```

  or

  ```
  Copytxt.appendText(text, false);
  // txt.text += text;

  ```

## Set style

```
Copytxt.setStyle(style);
txt.setFont(font);
txt.setFontFamily(family);
txt.setFontSize(size);
txt.setFontStyle(style);

```

## Set align

```
Copytxt.setAlign(align);

```

* `align` : `'left'`, `'center'`, `'right'`, `'justify'`

## Color

* Text color

  + Get

    ```
    Copyvar color = txt.style.color;

    ```
  + Set

    ```
    Copytxt.setColor(color);

    ```

    or

    ```
    Copytxt.setFill(color);

    ```
* Stroke color, thickness

  + Get

    ```
    Copyvar color = txt.style.stroke;
    var thickness = txt.style.strokeThickness;

    ```
  + Set

    ```
    Copytxt.setStroke(color, thickness);

    ```
  + Clear

    ```
    Copytxt.setStroke();

    ```
* Background color

  + Get

    ```
    Copyvar color = txt.style.backgroundColor;

    ```
  + Set

    ```
    Copytxt.setBackgroundColor(color);

    ```
* Shadow

  + Get

    ```
    Copyvar color = txt.style.shadowColor;
    var offsetX = txt.style.shadowOffsetX;
    var offsetY = txt.style.shadowOffsetY;
    var blur = txt.style.shadowBlur;
    var stroke = txt.style.shadowStroke;
    var enabled = txt.style.shadowFill;

    ```
  + Set

    ```
    Copytxt.setShadow(x, y, color, blur, shadowStroke, shadowFill);
    txt.setShadowOffset(x, y);
    txt.setShadowColor(color);
    txt.setShadowBlur(blur);
    txt.setShadowStroke(enabled);
    txt.setShadowFill(enabled);

    ```

## Line spacing

This value is *added* to the height of the font when calculating the overall line height.

* Get

  ```
  Copyvar lineSpacing = txt.lineSpacing;

  ```
* Set

  ```
  Copytxt.setLineSpacing(value);

  ```

## Letter spacing

* Get

  ```
  Copyvar letterSpacing = txt.letterSpacing;

  ```
* Set

  ```
  Copytxt.setLetterSpacing(value);

  ```

  + `value` : Positive or negative value.

!!! note
Enabling this feature will cause Phaser to render each character in this Text object
one by one, rather than use a draw for the whole string.
This makes it extremely expensive when used with either long strings, or lots of strings in total.

## Padding

* Get

  ```
  Copyvar left = txt.padding.left;
  var top = txt.padding.top;
  var right = txt.padding.right;
  var bottom = txt.padding.bottom;

  ```
* Set

  ```
  Copytxt.setPadding(left, top, right, bottom);
  // txt.setPadding(padding); // padding: {left, top, right, bottom}

  ```

## Max lines

* Get

  ```
  Copyvar maxLines = txt.style.maxLines;

  ```
* Set

  ```
  Copytxt.setMaxLines(max);

  ```

## Fixed size

* Get

  ```
  Copyvar width = txt.style.fixedWidth;
  var height = txt.style.fixedHeight;

  ```
* Set

  ```
  Copytxt.setFixedSize(width, height);

  ```

## Test string

Set the test string to use when measuring the font.

```
Copytxt.style.setTestString(text);

```

## RTL

* Set `rtl` in style config when creating this text game object
* Change `rtl` during runtime

  ```
  Copytxt.setRTL(rtl).setText(newContent);

  ```

  + Invoke `setRTL` method before setting new content.

## Other properties

See [game object](../gameobjects.md)

## Create mask

```
Copyvar mask = txt.createBitmapMask();

```

See [mask](../display.md)

## Shader effects

Support [preFX and postFX effects](shader.md)

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Sprite](sprite.md)

[Tile Sprite](tile-sprite.md)

On this page

* [Text](#text)

  + [Add text object](#add-text-object)
  + [Custom class](#custom-class)
  + [Word wrap](#word-wrap)
  + [Content](#content)
  + [Set style](#set-style)
  + [Set align](#set-align)
  + [Color](#color)
  + [Line spacing](#line-spacing)
  + [Letter spacing](#letter-spacing)
  + [Padding](#padding)
  + [Max lines](#max-lines)
  + [Fixed size](#fixed-size)
  + [Test string](#test-string)
  + [RTL](#rtl)
  + [Other properties](#other-properties)
  + [Create mask](#create-mask)
  + [Shader effects](#shader-effects)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)