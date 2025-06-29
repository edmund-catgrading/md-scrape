# BitmapText

Phaser.GameObjects.BitmapText

BitmapText objects work by taking a texture file and an XML or JSON file that describes the font structure.

During rendering for each letter of the text is rendered to the display, proportionally spaced out and aligned to

match the font structure.

BitmapText objects are less flexible than Text objects, in that they have less features such as shadows, fills and the ability

to use Web Fonts, however you trade this flexibility for rendering speed. You can also create visually compelling BitmapTexts by

processing the font texture in an image editor, applying fills and any other effects required.

To create multi-line text insert \r, \n or \r\n escape codes into the text string.

To create a BitmapText data files you need a 3rd party app such as:

BMFont (Windows, free): <http://www.angelcode.com/products/bmfont/>

Glyph Designer (OS X, commercial): <http://www.71squared.com/en/glyphdesigner>

Snow BMF (Web-based, free): [https://snowb.org/](https://snowb.org//)

Littera (Flash-based, free): <http://kvazars.com/littera/>

For most use cases it is recommended to use XML. If you wish to use JSON, the formatting should be equal to the result of

converting a valid XML file through the popular X2JS library. An online tool for conversion can be found here: <http://codebeautify.org/xmltojson>

**Constructor**

`new BitmapText(scene, x, y, font, [text], [size], [align])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No |  | The Scene to which this Game Object belongs. It can only belong to one Scene at any given time. |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of this Game Object in world space. |
| y | number | No |  | The y coordinate of this Game Object in world space. |
| font | string | No |  | The key of the font to use from the Bitmap Font cache. |
| text | string | Array.<string> | Yes |  | The string, or array of strings, to be set as the content of this Bitmap Text. |
| size | number | Yes |  | The font size of this Bitmap Text. |
| align | number | Yes | 0 | The alignment of the text in a multi-line BitmapText object. |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)  
> [Phaser.GameObjects.Components.Alpha](../namespace/gameobjects-components-alpha.md)  
> [Phaser.GameObjects.Components.BlendMode](../namespace/gameobjects-components-blendmode.md)  
> [Phaser.GameObjects.Components.Depth](../namespace/gameobjects-components-depth.md)  
> [Phaser.GameObjects.Components.GetBounds](../namespace/gameobjects-components-getbounds.md)  
> [Phaser.GameObjects.Components.Mask](../namespace/gameobjects-components-mask.md)  
> [Phaser.GameObjects.Components.Origin](../namespace/gameobjects-components-origin.md)  
> [Phaser.GameObjects.Components.Pipeline](../namespace/gameobjects-components-pipeline.md)  
> [Phaser.GameObjects.Components.PostPipeline](../namespace/gameobjects-components-postpipeline.md)  
> [Phaser.GameObjects.Components.ScrollFactor](../namespace/gameobjects-components-scrollfactor.md)  
> [Phaser.GameObjects.Components.Texture](../namespace/gameobjects-components-texture.md)  
> [Phaser.GameObjects.Components.Tint](../namespace/gameobjects-components-tint.md)  
> [Phaser.GameObjects.Components.Transform](../namespace/gameobjects-components-transform.md)  
> [Phaser.GameObjects.Components.Visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L17)  
> Since: 3.0.0

# Public Members

## active

### active: boolean

**Description:**

The active state of this Game Object.

A Game Object with an active state of `true` is processed by the Scenes UpdateList, if added to it.

An active object is one which is having its logic and internal systems updated.

**Inherits:** [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L113)  
> Since: 3.0.0

---

## align

### align: number

**Description:**

Controls the alignment of each line of text in this BitmapText object.

Only has any effect when this BitmapText contains multiple lines of text, split with carriage-returns.

Has no effect with single-lines of text.

See the methods `setLeftAlign`, `setCenterAlign` and `setRightAlign`.

0 = Left aligned (default)

1 = Middle aligned

2 = Right aligned

The alignment position is based on the longest line of text.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L855](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L855)  
> Since: 3.11.0

---

## ALIGN\_CENTER

### ALIGN\_CENTER: number

**Description:**

Center align the text characters in a multi-line BitmapText object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1153)  
> Since: 3.11.0

---

## ALIGN\_LEFT

### ALIGN\_LEFT: number

**Description:**

Left align the text characters in a multi-line BitmapText object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1144)  
> Since: 3.11.0

---

## ALIGN\_RIGHT

### ALIGN\_RIGHT: number

**Description:**

Right align the text characters in a multi-line BitmapText object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1162](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1162)  
> Since: 3.11.0

---

## alpha

### alpha: number

**Description:**

The alpha value of the Game Object.

This is a global value, impacting the entire Game Object, not just a region of it.

**Inherits:** [Phaser.GameObjects.Components.Alpha#alpha](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L129)  
> Since: 3.0.0

---

## alphaBottomLeft

### alphaBottomLeft: number

**Description:**

The alpha value starting from the bottom-left of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Alpha#alphaBottomLeft](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L227)  
> Since: 3.0.0

---

## alphaBottomRight

### alphaBottomRight: number

**Description:**

The alpha value starting from the bottom-right of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Alpha#alphaBottomRight](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L257](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L257)  
> Since: 3.0.0

---

## alphaTopLeft

### alphaTopLeft: number

**Description:**

The alpha value starting from the top-left of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Alpha#alphaTopLeft](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L167)  
> Since: 3.0.0

---

## alphaTopRight

### alphaTopRight: number

**Description:**

The alpha value starting from the top-right of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Alpha#alphaTopRight](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L197](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L197)  
> Since: 3.0.0

---

## angle

### angle: number

**Description:**

The angle of this Game Object as expressed in degrees.

Phaser uses a right-hand clockwise rotation system, where 0 is right, 90 is down, 180/-180 is left

and -90 is up.

If you prefer to work in radians, see the `rotation` property instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#angle](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L211](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L211)  
> Since: 3.0.0

---

## blendMode

### blendMode: [Phaser.BlendModes](../namespace/blendmodes.md), string, number

**Description:**

Sets the Blend Mode being used by this Game Object.

This can be a const, such as `Phaser.BlendModes.SCREEN`, or an integer, such as 4 (for Overlay)

Under WebGL only the following Blend Modes are available:

* NORMAL
* ADD
* MULTIPLY
* SCREEN
* ERASE

Canvas has more available depending on browser support.

You can also create your own custom Blend Modes in WebGL.

Blend modes have different effects under Canvas and WebGL, and from browser to browser, depending

on support. Blend Modes also cause a WebGL batch flush should it encounter a new blend mode. For these

reasons try to be careful about the construction of your Scene and the frequency of which blend modes

are used.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#blendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L30)  
> Since: 3.0.0

---

## body

### body: [Phaser.Physics.Arcade.Body](physics-arcade-body.md), [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md), MatterJS.BodyType

**Description:**

If this Game Object is enabled for Arcade or Matter Physics then this property will contain a reference to a Physics Body.

**Inherits:** [Phaser.GameObjects.GameObject#body](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L186)  
> Since: 3.0.0

---

## cameraFilter

### cameraFilter: number

**Description:**

A bitmask that controls if this Game Object is drawn by a Camera or not.

Not usually set directly, instead call `Camera.ignore`, however you can

set this property directly using the Camera.id property:

**Inherits:** [Phaser.GameObjects.GameObject#cameraFilter](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L160)  
> Since: 3.0.0

---

## data

### data: [Phaser.Data.DataManager](data-datamanager.md)

**Description:**

A Data Manager.

It allows you to store, query and get key/value paired information specific to this Game Object.

`null` by default. Automatically created if you use `getData` or `setData` or `setDataEnabled`.

**Inherits:** [Phaser.GameObjects.GameObject#data](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L136)  
> Since: 3.0.0

---

## defaultPipeline

### defaultPipeline: [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

**Description:**

The initial WebGL pipeline of this Game Object.

If you call `resetPipeline` on this Game Object, the pipeline is reset to this default.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Pipeline#defaultPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L19)  
> Since: 3.0.0

---

## depth

### depth: number

**Description:**

The depth of this Game Object within the Scene. Ensure this value is only ever set to a number data-type.

The depth is also known as the 'z-index' in some environments, and allows you to change the rendering order

of Game Objects, without actually moving their position in the display list.

The default depth is zero. A Game Object with a higher depth

value will always render in front of one with a lower value.

Setting the depth will queue a depth sort event within the Scene.

**Inherits:** [Phaser.GameObjects.Components.Depth#depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L30)  
> Since: 3.0.0

---

## displayHeight

### displayHeight: number

**Description:**

The displayed height of this Bitmap Text.

This value takes into account the scale factor.

This property is read-only.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1079](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1079)  
> Since: 3.60.0

---

## displayList

### displayList: [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md), [Phaser.GameObjects.Layer](gameobjects-layer.md)

**Description:**

Holds a reference to the Display List that contains this Game Object.

This is set automatically when this Game Object is added to a Scene or Layer.

You should treat this property as being read-only.

**Inherits:** [Phaser.GameObjects.GameObject#displayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L53)  
> Since: 3.50.0

---

## displayOriginX

### displayOriginX: number

**Description:**

The horizontal display origin of this Game Object.

The origin is a normalized value between 0 and 1.

The displayOrigin is a pixel value, based on the size of the Game Object combined with the origin.

**Inherits:** [Phaser.GameObjects.Components.Origin#displayOriginX](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L64)  
> Since: 3.0.0

---

## displayOriginY

### displayOriginY: number

**Description:**

The vertical display origin of this Game Object.

The origin is a normalized value between 0 and 1.

The displayOrigin is a pixel value, based on the size of the Game Object combined with the origin.

**Inherits:** [Phaser.GameObjects.Components.Origin#displayOriginY](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L88)  
> Since: 3.0.0

---

## displayWidth

### displayWidth: number

**Description:**

The displayed width of this Bitmap Text.

This value takes into account the scale factor.

This property is read-only.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1058](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1058)  
> Since: 3.60.0

---

## dropShadowAlpha

### dropShadowAlpha: number

**Description:**

The alpha value of the drop shadow.

You can set this directly, or use `Phaser.GameObjects.BitmapText#setDropShadow`.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L273](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L273)  
> Since: 3.50.0

---

## dropShadowColor

### dropShadowColor: number

**Description:**

The color of the drop shadow.

You can set this directly, or use `Phaser.GameObjects.BitmapText#setDropShadow`.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L262)  
> Since: 3.50.0

---

## dropShadowX

### dropShadowX: number

**Description:**

The horizontal offset of the drop shadow.

You can set this directly, or use `Phaser.GameObjects.BitmapText#setDropShadow`.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L240](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L240)  
> Since: 3.50.0

---

## dropShadowY

### dropShadowY: number

**Description:**

The vertical offset of the drop shadow.

You can set this directly, or use `Phaser.GameObjects.BitmapText#setDropShadow`.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L251)  
> Since: 3.50.0

---

## font

### font: string

**Description:**

The key of the Bitmap Font used by this Bitmap Text.

To change the font after creation please use `setFont`.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L98)  
> Since: 3.0.0

---

## fontData

### fontData: [Phaser.Types.GameObjects.BitmapText.BitmapFontData](../typedef/types-gameobjects-bitmaptext.md)

**Description:**

The data of the Bitmap Font used by this Bitmap Text.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L116)  
> Since: 3.0.0

---

## fontSize

### fontSize: number

**Description:**

The font size of this Bitmap Text.

You can also use the method `setFontSize` if you want a chainable way to change the font size.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L911](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L911)  
> Since: 3.0.0

---

## frame

### frame: [Phaser.Textures.Frame](textures-frame.md)

**Description:**

The Texture Frame this Game Object is using to render with.

**Inherits:** [Phaser.GameObjects.Components.Texture#frame](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L30)  
> Since: 3.0.0

---

## fromAtlas

### fromAtlas: boolean

**Description:**

Indicates whether the font texture is from an atlas or not.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L284](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L284)  
> Since: 3.54.0

---

## hasPostPipeline

### hasPostPipeline: boolean

**Description:**

Does this Game Object have any Post Pipelines set?

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#hasPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L21)  
> Since: 3.60.0

---

## hasTransformComponent

### hasTransformComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Inherits:** [Phaser.GameObjects.Components.Transform#hasTransformComponent](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L26](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L26)  
> Since: 3.60.0

---

## height

### height: number

**Description:**

The height of this Bitmap text.

This property is read-only.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1037](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1037)  
> Since: 3.0.0

---

## ignoreDestroy

### ignoreDestroy: boolean

**Description:**

This Game Object will ignore all calls made to its destroy method if this flag is set to `true`.

This includes calls that may come from a Group, Container or the Scene itself.

While it allows you to persist a Game Object across Scenes, please understand you are entirely

responsible for managing references to and from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#ignoreDestroy](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L196)  
> Since: 3.5.0

---

## input

### input: [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md)

**Description:**

If this Game Object is enabled for input then this property will contain an InteractiveObject instance.

Not usually set directly. Instead call `GameObject.setInteractive()`.

**Inherits:** [Phaser.GameObjects.GameObject#input](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L175)  
> Since: 3.0.0

---

## isTinted

### isTinted: boolean

**Description:**

Does this Game Object have a tint applied?

It checks to see if the 4 tint properties are set to the value 0xffffff

and that the `tintFill` property is `false`. This indicates that a Game Object isn't tinted.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Tint#isTinted](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L205)  
> Since: 3.11.0

---

## letterSpacing

### letterSpacing: number

**Description:**

Adds / Removes spacing between characters.

Can be a negative or positive number.

You can also use the method `setLetterSpacing` if you want a chainable way to change the letter spacing.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L935](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L935)  
> Since: 3.0.0

---

## lineSpacing

### lineSpacing: number

**Description:**

Adds / Removes spacing between lines.

Can be a negative or positive number.

You can also use the method `setLineSpacing` if you want a chainable way to change the line spacing.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L961](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L961)  
> Since: 3.60.0

---

## mask

### mask: [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md), [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)

**Description:**

The Mask this Game Object is using during render.

**Inherits:** [Phaser.GameObjects.Components.Mask#mask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L19)  
> Since: 3.0.0

---

## maxWidth

### maxWidth: number

**Description:**

The maximum display width of this BitmapText in pixels.

If BitmapText.text is longer than maxWidth then the lines will be automatically wrapped

based on the last whitespace character found in the line.

If no whitespace was found then no wrapping will take place and consequently the maxWidth value will not be honored.

Disable maxWidth by setting the value to 0.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L987](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L987)  
> Since: 3.21.0

---

## name

### name: string

**Description:**

The name of this Game Object.

Empty by default and never populated by Phaser, this is left for developers to use.

**Inherits:** [Phaser.GameObjects.GameObject#name](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L102)  
> Since: 3.0.0

---

## originX

### originX: number

**Description:**

The horizontal origin of this Game Object.

The origin maps the relationship between the size and position of the Game Object.

The default value is 0.5, meaning all Game Objects are positioned based on their center.

Setting the value to 0 means the position now relates to the left of the Game Object.

Set this value with `setOrigin()`.

**Inherits:** [Phaser.GameObjects.Components.Origin#originX](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L30)  
> Since: 3.0.0

---

## originY

### originY: number

**Description:**

The vertical origin of this Game Object.

The origin maps the relationship between the size and position of the Game Object.

The default value is 0.5, meaning all Game Objects are positioned based on their center.

Setting the value to 0 means the position now relates to the top of the Game Object.

Set this value with `setOrigin()`.

**Inherits:** [Phaser.GameObjects.Components.Origin#originY](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L45)  
> Since: 3.0.0

---

## parentContainer

### parentContainer: [Phaser.GameObjects.Container](gameobjects-container.md)

**Description:**

The parent Container of this Game Object, if it has one.

**Inherits:** [Phaser.GameObjects.GameObject#parentContainer](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L93)  
> Since: 3.4.0

---

## pipeline

### pipeline: [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

**Description:**

The current WebGL pipeline of this Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Pipeline#pipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L32](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L32)  
> Since: 3.0.0

---

## pipelineData

### pipelineData: object

**Description:**

An object to store pipeline specific data in, to be read by the pipelines this Game Object uses.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Pipeline#pipelineData](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L43)  
> Since: 3.50.0

---

## postFX

### postFX: [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md)

**Description:**

The Post FX component of this Game Object.

This component allows you to apply a variety of built-in effects to this Game Object, such

as glow, blur, bloom, displacements, vignettes and more. You access them via this property,

for example:

```
Copy
const player = this.add.sprite();

player.postFX.addBloom();


```

All FX are WebGL only and do not have Canvas counterparts.

Please see the FX Class for more details and available methods.

This property is always `null` until the `initPostPipeline` method is called.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L88)  
> Since: 3.60.0

---

## postPipelineData

### postPipelineData: object

**Description:**

An object to store pipeline specific data in, to be read by the pipelines this Game Object uses.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postPipelineData](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L46)  
> Since: 3.60.0

---

## postPipelines

### postPipelines: Array.<[Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md)>

**Description:**

The WebGL Post FX Pipelines this Game Object uses for post-render effects.

The pipelines are processed in the order in which they appear in this array.

If you modify this array directly, be sure to set the

`hasPostPipeline` property accordingly.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postPipelines](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L31)  
> Since: 3.60.0

---

## preFX

### preFX: [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md)

**Description:**

The Pre FX component of this Game Object.

This component allows you to apply a variety of built-in effects to this Game Object, such

as glow, blur, bloom, displacements, vignettes and more. You access them via this property,

for example:

```
Copy
const player = this.add.sprite();

player.preFX.addBloom();


```

Only the following Game Objects support Pre FX:

* Image
* Sprite
* TileSprite
* Text
* RenderTexture
* Video

All FX are WebGL only and do not have Canvas counterparts.

Please see the FX Class for more details and available methods.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#preFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L56)  
> Since: 3.60.0

---

## renderFlags

### renderFlags: number

**Description:**

The flags that are compared against `RENDER_MASK` to determine if this Game Object will render or not.

The bits are 0001 | 0010 | 0100 | 1000 set by the components Visible, Alpha, Transform and Texture respectively.

If those components are not used by your custom class then you can use this bitmask as you wish.

**Inherits:** [Phaser.GameObjects.GameObject#renderFlags](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L148)  
> Since: 3.0.0

---

## rotation

### rotation: number

**Description:**

The angle of this Game Object in radians.

Phaser uses a right-hand clockwise rotation system, where 0 is right, PI/2 is down, +-PI is left

and -PI/2 is up.

If you prefer to work in degrees, see the `angle` property instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#rotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L238](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L238)  
> Since: 3.0.0

---

## scale

### scale: number

**Description:**

This is a special setter that allows you to set both the horizontal and vertical scale of this Game Object

to the same value, at the same time. When reading this value the result returned is `(scaleX + scaleY) / 2`.

Use of this property implies you wish the horizontal and vertical scales to be equal to each other. If this

isn't the case, use the `scaleX` or `scaleY` properties instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#scale](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L113)  
> Since: 3.18.0

---

## scaleX

### scaleX: number

**Description:**

The horizontal scale of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#scaleX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L149)  
> Since: 3.0.0

---

## scaleY

### scaleY: number

**Description:**

The vertical scale of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#scaleY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L180)  
> Since: 3.0.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene to which this Game Object belongs.

Game Objects can only belong to one Scene.

You should consider this property as being read-only. You cannot move a

Game Object to another Scene by simply changing it.

**Inherits:** [Phaser.GameObjects.GameObject#scene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L39)  
> Since: 3.0.0

---

## scrollFactorX

### scrollFactorX: number

**Description:**

The horizontal scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#scrollFactorX](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L16)  
> Since: 3.0.0

---

## scrollFactorY

### scrollFactorY: number

**Description:**

The vertical scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#scrollFactorY](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L40)  
> Since: 3.0.0

---

## state

### state: number, string

**Description:**

The current state of this Game Object.

Phaser itself will never modify this value, although plugins may do so.

Use this property to track the state of a Game Object during its lifetime. For example, it could change from

a state of 'moving', to 'attacking', to 'dead'. The state value should be an integer (ideally mapped to a constant

in your game code), or a string. These are recommended to keep it light and simple, with fast comparisons.

If you need to store complex data about your Game Object, look at using the Data Component instead.

**Inherits:** [Phaser.GameObjects.GameObject#state](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L77)  
> Since: 3.16.0

---

## tabIndex

### tabIndex: number

**Description:**

The Tab Index of the Game Object.

Reserved for future use by plugins and the Input Manager.

**Inherits:** [Phaser.GameObjects.GameObject#tabIndex](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L125)  
> Since: 3.0.0

---

## text

### text: string

**Description:**

The text that this Bitmap Text object displays.

You can also use the method `setText` if you want a chainable way to change the text content.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L888](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L888)  
> Since: 3.0.0

---

## texture

### texture: [Phaser.Textures.Texture](textures-texture.md), [Phaser.Textures.CanvasTexture](textures-canvastexture.md)

**Description:**

The Texture this Game Object is using to render with.

**Inherits:** [Phaser.GameObjects.Components.Texture#texture](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L21)  
> Since: 3.0.0

---

## tint

### tint: number

**Description:**

The tint value being applied to the whole of the Game Object.

Return `tintTopLeft` when read this tint property.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Tint#tint](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L183](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L183)  
> Since: 3.0.0

---

## tintBottomLeft

### tintBottomLeft: number

**Description:**

The tint value being applied to the bottom-left vertice of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

The value should be set as a hex number, i.e. 0xff0000 for red, or 0xff00ff for purple.

**Inherits:** [Phaser.GameObjects.Components.Tint#tintBottomLeft](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L42)  
> Since: 3.0.0

---

## tintBottomRight

### tintBottomRight: number

**Description:**

The tint value being applied to the bottom-right vertice of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

The value should be set as a hex number, i.e. 0xff0000 for red, or 0xff00ff for purple.

**Inherits:** [Phaser.GameObjects.Components.Tint#tintBottomRight](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L54)  
> Since: 3.0.0

---

## tintFill

### tintFill: boolean

**Description:**

The tint fill mode.

`false` = An additive tint (the default), where vertices colors are blended with the texture.

`true` = A fill tint, where the vertices colors replace the texture, but respects texture alpha.

**Inherits:** [Phaser.GameObjects.Components.Tint#tintFill](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L66)  
> Since: 3.11.0

---

## tintTopLeft

### tintTopLeft: number

**Description:**

The tint value being applied to the top-left vertice of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

The value should be set as a hex number, i.e. 0xff0000 for red, or 0xff00ff for purple.

**Inherits:** [Phaser.GameObjects.Components.Tint#tintTopLeft](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L18)  
> Since: 3.0.0

---

## tintTopRight

### tintTopRight: number

**Description:**

The tint value being applied to the top-right vertice of the Game Object.

This value is interpolated from the corner to the center of the Game Object.

The value should be set as a hex number, i.e. 0xff0000 for red, or 0xff00ff for purple.

**Inherits:** [Phaser.GameObjects.Components.Tint#tintTopRight](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L30)  
> Since: 3.0.0

---

## type

### type: string

**Description:**

A textual representation of this Game Object, i.e. `sprite`.

Used internally by Phaser but is available for your own custom classes to populate.

**Inherits:** [Phaser.GameObjects.GameObject#type](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L67)  
> Since: 3.0.0

---

## visible

### visible: boolean

**Description:**

The visible state of the Game Object.

An invisible Game Object will skip rendering, but will still process update logic.

**Inherits:** [Phaser.GameObjects.Components.Visible#visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L31)  
> Since: 3.0.0

---

## w

### w: number

**Description:**

The w position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#w](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L103)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The width of this Bitmap Text.

This property is read-only.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1016](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1016)  
> Since: 3.0.0

---

## wordWrapCharCode

### wordWrapCharCode: number

**Description:**

The character code used to detect for word wrapping.

Defaults to 32 (a space character).

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L220](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L220)  
> Since: 3.21.0

---

## x

### x: number

**Description:**

The x position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#x](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L70)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#y](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L80)  
> Since: 3.0.0

---

## z

### z: number

**Description:**

The z position of this Game Object.

Note: The z position does not control the rendering order of 2D Game Objects. Use

[Phaser.GameObjects.Components.Depth#depth](../namespace/gameobjects-components-depth.md) instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#z](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L90)  
> Since: 3.0.0

---

# Private Members

## \_align

### \_align: number

**Description:**

Controls the alignment of each line of text in this BitmapText object.

Only has any effect when this BitmapText contains multiple lines of text, split with carriage-returns.

Has no effect with single-lines of text.

See the methods `setLeftAlign`, `setCenterAlign` and `setRightAlign`.

0 = Left aligned (default)

1 = Middle aligned

2 = Right aligned

The alignment position is based on the longest line of text.

**Access:** private

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L170](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L170)  
> Since: 3.11.0

---

## \_alpha

### \_alpha: number

**Description:**

Private internal value. Holds the global alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alpha](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L22](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L22)  
> Since: 3.0.0

---

## \_alphaBL

### \_alphaBL: number

**Description:**

Private internal value. Holds the bottom-left alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaBL](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L55)  
> Since: 3.0.0

---

## \_alphaBR

### \_alphaBR: number

**Description:**

Private internal value. Holds the bottom-right alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaBR](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L66)  
> Since: 3.0.0

---

## \_alphaTL

### \_alphaTL: number

**Description:**

Private internal value. Holds the top-left alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaTL](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L33)  
> Since: 3.0.0

---

## \_alphaTR

### \_alphaTR: number

**Description:**

Private internal value. Holds the top-right alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaTR](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L44)  
> Since: 3.0.0

---

## \_blendMode

### \_blendMode: number

**Description:**

Private internal value. Holds the current blend mode.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.BlendMode#\_blendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L19)  
> Since: 3.0.0

---

## \_bounds

### \_bounds: [Phaser.Types.GameObjects.BitmapText.BitmapTextSize](../typedef/types-gameobjects-bitmaptext.md)

**Description:**

An object that describes the size of this Bitmap Text.

**Access:** private

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L190](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L190)  
> Since: 3.0.0

---

## \_depth

### \_depth: number

**Description:**

Private internal value. Holds the depth of the Game Object.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Depth#\_depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L19)  
> Since: 3.0.0

---

## \_dirty

### \_dirty: boolean

**Description:**

An internal dirty flag for bounds calculation.

**Access:** private

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L200](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L200)  
> Since: 3.11.0

---

## \_fontSize

### \_fontSize: number

**Description:**

The font size of this Bitmap Text.

**Access:** private

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L136)  
> Since: 3.0.0

---

## \_letterSpacing

### \_letterSpacing: number

**Description:**

Adds / Removes spacing between characters.

Can be a negative or positive number.

**Access:** private

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L146](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L146)  
> Since: 3.4.0

---

## \_lineSpacing

### \_lineSpacing: number

**Description:**

Adds / Removes line spacing in a multiline BitmapText object.

Can be a negative or positive number.

**Access:** private

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L158](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L158)  
> Since: 3.60.0

---

## \_maxWidth

### \_maxWidth: number

**Description:**

Internal cache var holding the maxWidth.

**Access:** private

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L210](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L210)  
> Since: 3.21.0

---

## \_originComponent

### \_originComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Origin#\_originComponent](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L19)  
> Since: 3.2.0

---

## \_rotation

### \_rotation: number

**Description:**

Private internal value. Holds the rotation value in radians.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_rotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L59)  
> Since: 3.0.0

---

## \_scaleX

### \_scaleX: number

**Description:**

Private internal value. Holds the horizontal scale value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_scaleX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L37)  
> Since: 3.0.0

---

## \_scaleY

### \_scaleY: number

**Description:**

Private internal value. Holds the vertical scale value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_scaleY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L48)  
> Since: 3.0.0

---

## \_text

### \_text: string

**Description:**

The text that this Bitmap Text object displays.

**Access:** private

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L126)  
> Since: 3.0.0

---

## \_visible

### \_visible: boolean

**Description:**

Private internal value. Holds the visible value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Visible#\_visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L20](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L20)  
> Since: 3.0.0

---

## charColors

### charColors: array

**Description:**

Internal array holding the character tint color data.

**Access:** private

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L230](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L230)  
> Since: 3.50.0

---

## isCropped

### isCropped: boolean

**Description:**

Internal flag. Not to be set by this Game Object.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Texture#isCropped](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L39)  
> Since: 3.11.0

---

# Public Methods

## addedToScene

### <instance> addedToScene()

**Description:**

This callback is invoked when this Game Object is added to a Scene.

Can be overriden by custom Game Objects, but be aware of some Game Objects that

will use this, such as Sprites, to add themselves into the Update List.

You can also listen for the `ADDED_TO_SCENE` event from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addedToScene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L562](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L562)  
> Since: 3.50.0

---

## addListener

### <instance> addListener(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addToDisplayList

### <instance> addToDisplayList([displayList])

**Description:**

Adds this Game Object to the given Display List.

If no Display List is specified, it will default to the Display List owned by the Scene to which

this Game Object belongs.

A Game Object can only exist on one Display List at any given time, but may move freely between them.

If this Game Object is already on another Display List when this method is called, it will first

be removed from it, before being added to the new list.

You can query which list it is on by looking at the `Phaser.GameObjects.GameObject#displayList` property.

If a Game Object isn't on any display list, it will not be rendered. If you just wish to temporarly

disable it from rendering, consider using the `setVisible` method, instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| displayList | [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md) | [Phaser.GameObjects.Layer](gameobjects-layer.md) | Yes | The Display List to add to. Defaults to the Scene Display List. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object.

**Fires:** [Phaser.Scenes.Events#event:ADDED\_TO\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:ADDED\_TO\_SCENE](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#addToDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L684](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L684)  
> Since: 3.53.0

---

## addToUpdateList

### <instance> addToUpdateList()

**Description:**

Adds this Game Object to the Update List belonging to the Scene.

When a Game Object is added to the Update List it will have its `preUpdate` method called

every game frame. This method is passed two parameters: `delta` and `time`.

If you wish to run your own logic within `preUpdate` then you should always call

`super.preUpdate(delta, time)` within it, or it may fail to process required operations,

such as Sprite animations.

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addToUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L735](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L735)  
> Since: 3.53.0

---

## clearAlpha

### <instance> clearAlpha()

**Description:**

Clears all alpha values associated with this Game Object.

Immediately sets the alpha levels back to 1 (fully opaque).

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Alpha#clearAlpha](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L77)  
> Since: 3.0.0

---

## clearFX

### <instance> clearFX()

**Description:**

Removes all Pre and Post FX Controllers from this Game Object.

If you wish to remove a single controller, use the `preFX.remove(fx)` or `postFX.remove(fx)` methods instead.

If you wish to clear a single controller, use the `preFX.clear()` or `postFX.clear()` methods instead.

**Tags:**

* webglOnly

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#clearFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L337](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L337)  
> Since: 3.60.0

---

## clearMask

### <instance> clearMask([destroyMask])

**Description:**

Clears the mask that this Game Object was using.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| destroyMask | boolean | Yes | false | Destroy the mask before clearing it? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#clearMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L56)  
> Since: 3.6.2

---

## clearTint

### <instance> clearTint()

**Description:**

Clears all tint values associated with this Game Object.

Immediately sets the color values back to 0xffffff and the tint type to 'additive',

which results in no visible change to the texture.

**Tags:**

* webglOnly

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Tint#clearTint](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L79)  
> Since: 3.0.0

---

## copyPosition

### <instance> copyPosition(source)

**Description:**

Copies an object's coordinates to this Game Object's position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | [Phaser.Types.Math.Vector3Like](../typedef/types-math.md) | [Phaser.Types.Math.Vector4Like](../typedef/types-math.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#copyPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L293)  
> Since: 3.50.0

---

## createBitmapMask

### <instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])

**Description:**

Creates and returns a Bitmap Mask. This mask can be used by any Game Object,

including this one, or a Dynamic Texture.

Note: Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.

To create the mask you need to pass in a reference to a renderable Game Object.

A renderable Game Object is one that uses a texture to render with, such as an

Image, Sprite, Render Texture or BitmapText.

If you do not provide a renderable object, and this Game Object has a texture,

it will use itself as the object. This means you can call this method to create

a Bitmap Mask from any renderable texture-based Game Object.

**Tags:**

* generic
* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| maskObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | [Phaser.Textures.DynamicTexture](textures-dynamictexture.md) | Yes | The Game Object or Dynamic Texture that will be used as the mask. If `null` it will generate an Image Game Object using the rest of the arguments. |
| --- | --- | --- | --- |
| x | number | Yes | If creating a Game Object, the horizontal position in the world. |
| y | number | Yes | If creating a Game Object, the vertical position in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | Yes | If creating a Game Object, the key, or instance of the Texture it will use to render with, as stored in the Texture Manager. |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | Yes |

**Returns:** [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) - This Bitmap Mask that was created.

**Inherits:** [Phaser.GameObjects.Components.Mask#createBitmapMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L80)  
> Since: 3.6.2

---

## createGeometryMask

### <instance> createGeometryMask([graphics])

**Description:**

Creates and returns a Geometry Mask. This mask can be used by any Game Object,

including this one.

To create the mask you need to pass in a reference to a Graphics Game Object.

If you do not provide a graphics object, and this Game Object is an instance

of a Graphics object, then it will use itself to create the mask.

This means you can call this method to create a Geometry Mask from any Graphics Game Object.

**Tags:**

* generic
* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | [Phaser.GameObjects.Shape](gameobjects-shape.md) | Yes | A Graphics Game Object, or any kind of Shape Game Object. The geometry within it will be used as the mask. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md) - This Geometry Mask that was created.

**Inherits:** [Phaser.GameObjects.Components.Mask#createGeometryMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L120)  
> Since: 3.6.2

---

## destroy

### <instance> destroy([fromScene])

**Description:**

Destroys this Game Object removing it from the Display List and Update List and

severing all ties to parent resources.

Also removes itself from the Input Manager and Physics Manager if previously enabled.

Use this to remove a Game Object from your game if you don't ever plan to use it again.

As long as no reference to it exists within your own code it should become free for

garbage collection by the browser.

If you just want to temporarily disable an object then look at using the

Game Object Pool instead of destroying it, as destroyed objects cannot be resurrected.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| fromScene | boolean | Yes | false | `True` if this Game Object is being destroyed by the Scene, `false` if not. |
| --- | --- | --- | --- | --- |

**Fires:** [Phaser.GameObjects.Events#event:DESTROY](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#destroy](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L855](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L855)  
> Since: 3.0.0

---

## disableInteractive

### <instance> disableInteractive([resetCursor])

**Description:**

If this Game Object has previously been enabled for input, this will disable it.

An object that is disabled for input stops processing or being considered for

input events, but can be turned back on again at any time by simply calling

`setInteractive()` with no arguments provided.

If want to completely remove interaction from this Game Object then use `removeInteractive` instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetCursor | boolean | Yes | false | Should the currently active Input cursor, if any, be reset to the default cursor? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#disableInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L494](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L494)  
> Since: 3.7.0

---

## emit

### <instance> emit(event, [args])

**Description:**

Calls each of the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| args | \* | Yes | Additional arguments that will be passed to the event handler. |

**Returns:** boolean - `true` if the event had listeners, else `false`.

**Inherits:** [Phaser.Events.EventEmitter#emit](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L86)  
> Since: 3.0.0

---

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## getBottomCenter

### <instance> getBottomCenter([output], [includeParent])

**Description:**

Gets the bottom-center coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getBottomCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L236)  
> Since: 3.18.0

---

## getBottomLeft

### <instance> getBottomLeft([output], [includeParent])

**Description:**

Gets the bottom-left corner coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getBottomLeft](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L210](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L210)  
> Since: 3.0.0

---

## getBottomRight

### <instance> getBottomRight([output], [includeParent])

**Description:**

Gets the bottom-right corner coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getBottomRight](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L262)  
> Since: 3.0.0

---

## getBounds

### <instance> getBounds([output])

**Description:**

Gets the bounds of this Game Object, regardless of origin.

The values are stored and returned in a Rectangle, or Rectangle-like, object.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| output | [Phaser.Geom.Rectangle](geom-rectangle.md) | object | Yes | An object to store the values in. If not provided a new Rectangle will be created. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md), object - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getBounds](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L288](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L288)  
> Since: 3.0.0

---

## getCenter

### <instance> getCenter([output], [includeParent])

**Description:**

Gets the center coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L54)  
> Since: 3.0.0

---

## getCharacterAt

### <instance> getCharacterAt(x, y, [camera])

**Description:**

Gets the character located at the given x/y coordinate within this Bitmap Text.

The coordinates you pass in are translated into the local space of the

Bitmap Text, however, it is up to you to first translate the input coordinates to world space.

If you wish to use this in combination with an input event, be sure

to pass in `Pointer.worldX` and `worldY` so they are in world space.

In some cases, based on kerning, characters can overlap. When this happens,

the first character in the word is returned.

Note that this does not work for DynamicBitmapText if you have changed the

character positions during render. It will only scan characters in their un-translated state.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position to check. |
| --- | --- | --- | --- |
| y | number | No | The y position to check. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera which is being tested against. If not given will use the Scene default camera. |

**Returns:** [Phaser.Types.GameObjects.BitmapText.BitmapTextCharacter](../typedef/types-gameobjects-bitmaptext.md) - The character object at the given position, or `null`.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L716](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L716)  
> Since: 3.50.0

---

## getData

### <instance> getData(key)

**Description:**

Retrieves the value for the given key in this Game Objects Data Manager, or undefined if it doesn't exist.

You can also access values via the `values` object. For example, if you had a key called `gold` you can do either:

```
Copy
sprite.getData('gold');


```

Or access the value directly:

```
Copy
sprite.data.values.gold;


```

You can also pass in an array of keys, in which case an array of values will be returned:

```
Copy
sprite.getData([ 'gold', 'armor', 'health' ]);


```

This approach is useful for destructuring arrays in ES6.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | Array.<string> | No | The key of the value to retrieve, or an array of keys. |
| --- | --- | --- | --- |

**Returns:** \* - The value belonging to the given key, or an array of values, the order of which will match the input array.

**Inherits:** [Phaser.GameObjects.GameObject#getData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L416](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L416)  
> Since: 3.0.0

---

## getDisplayList

### <instance> getDisplayList()

**Description:**

Returns a reference to the underlying display list *array* that contains this Game Object,

which will be either the Scene's Display List or the internal list belonging

to its parent Container, if it has one.

If this Game Object is not on a display list or in a container, it will return `null`.

You should be very careful with this method, and understand that it returns a direct reference to the

internal array used by the Display List. Mutating this array directly can cause all kinds of subtle

and difficult to debug issues in your game.

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - The internal Display List array of Game Objects, or `null`.

**Inherits:** [Phaser.GameObjects.GameObject#getDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L823](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L823)  
> Since: 3.85.0

---

## getIndexList

### <instance> getIndexList()

**Description:**

Returns an array containing the display list index of either this Game Object, or if it has one,

its parent Container. It then iterates up through all of the parent containers until it hits the

root of the display list (which is index 0 in the returned array).

Used internally by the InputPlugin but also useful if you wish to find out the display depth of

this Game Object and all of its ancestors.

**Returns:** Array.<number> - An array of display list position indexes.

**Inherits:** [Phaser.GameObjects.GameObject#getIndexList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L635](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L635)  
> Since: 3.4.0

---

## getLeftCenter

### <instance> getLeftCenter([output], [includeParent])

**Description:**

Gets the left-center coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getLeftCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L158](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L158)  
> Since: 3.18.0

---

## getLocalPoint

### <instance> getLocalPoint(x, y, [point], [camera])

**Description:**

Takes the given `x` and `y` coordinates and converts them into local space for this

Game Object, taking into account parent and local transforms, and the Display Origin.

The returned Vector2 contains the translated point in its properties.

A Camera needs to be provided in order to handle modified scroll factors. If no

camera is specified, it will use the `main` camera from the Scene to which this

Game Object belongs.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position to translate. |
| --- | --- | --- | --- |
| y | number | No | The y position to translate. |
| point | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2, or point-like object, to store the results in. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera which is being tested against. If not given will use the Scene default camera. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The translated point.

**Inherits:** [Phaser.GameObjects.Components.Transform#getLocalPoint](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L542](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L542)  
> Since: 3.50.0

---

## getLocalTransformMatrix

### <instance> getLocalTransformMatrix([tempMatrix])

**Description:**

Gets the local transform matrix for this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | The matrix to populate with the values from this Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - The populated Transform Matrix.

**Inherits:** [Phaser.GameObjects.Components.Transform#getLocalTransformMatrix](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L484](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L484)  
> Since: 3.4.0

---

## getParentRotation

### <instance> getParentRotation()

**Description:**

Gets the sum total rotation of all of this Game Objects parent Containers.

The returned value is in radians and will be zero if this Game Object has no parent container.

**Returns:** number - The sum total rotation, in radians, of all parent containers of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#getParentRotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L592](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L592)  
> Since: 3.18.0

---

## getPipelineName

### <instance> getPipelineName()

**Description:**

Gets the name of the WebGL Pipeline this Game Object is currently using.

**Tags:**

* webglOnly

**Returns:** string - The string-based name of the pipeline being used by this Game Object, or null.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#getPipelineName](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L201](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L201)  
> Since: 3.0.0

---

## getPostPipeline

### <instance> getPostPipeline(pipeline)

**Description:**

Gets a Post Pipeline instance from this Game Object, based on the given name, and returns it.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | function | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md), Array.<[Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md)> - An array of all the Post Pipelines matching the name. This array will be empty if there was no match. If there was only one single match, that pipeline is returned directly, not in an array.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#getPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L237)  
> Since: 3.60.0

---

## getRightCenter

### <instance> getRightCenter([output], [includeParent])

**Description:**

Gets the right-center coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getRightCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L184](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L184)  
> Since: 3.18.0

---

## getTextBounds

### <instance> getTextBounds([round])

**Description:**

Calculate the bounds of this Bitmap Text.

An object is returned that contains the position, width and height of the Bitmap Text in local and global

contexts.

Local size is based on just the font size and a [0, 0] position.

Global size takes into account the Game Object's scale, world position and display origin.

Also in the object is data regarding the length of each line, should this be a multi-line BitmapText.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| round | boolean | Yes | false | Whether to round the results up to the nearest integer. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Types.GameObjects.BitmapText.BitmapTextSize](../typedef/types-gameobjects-bitmaptext.md) - An object that describes the size of this Bitmap Text.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L679](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L679)  
> Since: 3.0.0

---

## getTopCenter

### <instance> getTopCenter([output], [includeParent])

**Description:**

Gets the top-center coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getTopCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L106)  
> Since: 3.18.0

---

## getTopLeft

### <instance> getTopLeft([output], [includeParent])

**Description:**

Gets the top-left corner coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getTopLeft](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L80)  
> Since: 3.0.0

---

## getTopRight

### <instance> getTopRight([output], [includeParent])

**Description:**

Gets the top-right corner coordinate of this Game Object, regardless of origin.

The returned point is calculated in local space and does not factor in any parent Containers,

unless the `includeParent` argument is set to `true`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getTopRight](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L132)  
> Since: 3.0.0

---

## getWorldTransformMatrix

### <instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])

**Description:**

Gets the world transform matrix for this Game Object, factoring in any parent Containers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | The matrix to populate with the values from this Game Object. |
| --- | --- | --- | --- |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | A temporary matrix to hold parent values during the calculations. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - The populated Transform Matrix.

**Inherits:** [Phaser.GameObjects.Components.Transform#getWorldTransformMatrix](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L501)  
> Since: 3.4.0

---

## incData

### <instance> incData(key, [amount])

**Description:**

Increase a value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is increased from 0.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

When the value is first set, a `setdata` event is emitted from this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key to change the value for. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The amount to increase the given key by. Pass a negative value to decrease the key. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#incData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L357](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L357)  
> Since: 3.23.0

---

## initPipeline

### <instance> initPipeline([pipeline])

**Description:**

Sets the initial WebGL Pipeline of this Game Object.

This should only be called during the instantiation of the Game Object. After that, use `setPipeline`.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | Yes | Either the string-based name of the pipeline, or a pipeline instance to set. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the pipeline was set successfully, otherwise `false`.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#initPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L53)  
> Since: 3.0.0

---

## initPostPipeline

### <instance> initPostPipeline([preFX])

**Description:**

This should only be called during the instantiation of the Game Object.

It is called by default by all core Game Objects and doesn't need

calling again.

After that, use `setPostPipeline`.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| preFX | boolean | Yes | false | Does this Game Object support Pre FX? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#initPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L113)  
> Since: 3.60.0

---

## listenerCount

### <instance> listenerCount(event)

**Description:**

Return the number of listeners listening to a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** number - The number of listeners.

**Inherits:** [Phaser.Events.EventEmitter#listenerCount](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L75)  
> Since: 3.0.0

---

## listeners

### <instance> listeners(event)

**Description:**

Return the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** Array.<function()> - The registered listeners.

**Inherits:** [Phaser.Events.EventEmitter#listeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L64)  
> Since: 3.0.0

---

## off

### <instance> off(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#off](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L151)  
> Since: 3.0.0

---

## on

### <instance> on(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## once

### <instance> once(event, fn, [context])

**Description:**

Add a one-time listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## ParseFromAtlas

### <static> ParseFromAtlas(scene, fontName, textureKey, frameKey, xmlKey, [xSpacing], [ySpacing])

**Description:**

Parse an XML Bitmap Font from an Atlas.

Adds the parsed Bitmap Font data to the cache with the `fontName` key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to parse the Bitmap Font for. |
| --- | --- | --- | --- |
| fontName | string | No | The key of the font to add to the Bitmap Font cache. |
| textureKey | string | No | The key of the BitmapFont's texture. |
| frameKey | string | No | The key of the BitmapFont texture's frame. |
| xmlKey | string | No | The key of the XML data of the font to parse. |
| xSpacing | number | Yes | The x-axis spacing to add between each letter. |
| ySpacing | number | Yes | The y-axis spacing to add to the line height. |

**Returns:** boolean - Whether the parsing was successful or not.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1171](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1171)  
> Since: 3.0.0

---

## ParseXMLBitmapFont

### <static> ParseXMLBitmapFont(xml, frame, [xSpacing], [ySpacing])

**Description:**

Parse an XML font to Bitmap Font data for the Bitmap Font cache.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| xml | XMLDocument | No |  | The XML Document to parse the font from. |
| --- | --- | --- | --- | --- |
| frame | [Phaser.Textures.Frame](textures-frame.md) | No |  | The texture frame to take into account when creating the uv data. |
| xSpacing | number | Yes | 0 | The x-axis spacing to add between each letter. |
| ySpacing | number | Yes | 0 | The y-axis spacing to add to the line height. |

**Returns:** [Phaser.Types.GameObjects.BitmapText.BitmapFontData](../typedef/types-gameobjects-bitmaptext.md) - The parsed Bitmap Font data.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1191](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1191)  
> Since: 3.17.0

---

## preDestroy

### <instance> preDestroy()

**Description:**

Internal destroy handler, called as part of the destroy process.

**Access:** protected

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1128](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1128)  
> Since: 3.50.0

---

## removeAllListeners

### <instance> removeAllListeners([event])

**Description:**

Remove all listeners, or those of the specified event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | Yes | The event name. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removedFromScene

### <instance> removedFromScene()

**Description:**

This callback is invoked when this Game Object is removed from a Scene.

Can be overriden by custom Game Objects, but be aware of some Game Objects that

will use this, such as Sprites, to removed themselves from the Update List.

You can also listen for the `REMOVED_FROM_SCENE` event from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#removedFromScene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L577](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L577)  
> Since: 3.50.0

---

## removeFromDisplayList

### <instance> removeFromDisplayList()

**Description:**

Removes this Game Object from the Display List it is currently on.

A Game Object can only exist on one Display List at any given time, but may move freely removed

and added back at a later stage.

You can query which list it is on by looking at the `Phaser.GameObjects.GameObject#displayList` property.

If a Game Object isn't on any Display List, it will not be rendered. If you just wish to temporarly

disable it from rendering, consider using the `setVisible` method, instead.

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object.

**Fires:** [Phaser.Scenes.Events#event:REMOVED\_FROM\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:REMOVED\_FROM\_SCENE](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#removeFromDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L760](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L760)  
> Since: 3.53.0

---

## removeFromUpdateList

### <instance> removeFromUpdateList()

**Description:**

Removes this Game Object from the Scene's Update List.

When a Game Object is on the Update List, it will have its `preUpdate` method called

every game frame. Calling this method will remove it from the list, preventing this.

Removing a Game Object from the Update List will stop most internal functions working.

For example, removing a Sprite from the Update List will prevent it from being able to

run animations.

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#removeFromUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L798](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L798)  
> Since: 3.53.0

---

## removeInteractive

### <instance> removeInteractive([resetCursor])

**Description:**

If this Game Object has previously been enabled for input, this will queue it

for removal, causing it to no longer be interactive. The removal happens on

the next game step, it is not immediate.

The Interactive Object that was assigned to this Game Object will be destroyed,

removed from the Input Manager and cleared from this Game Object.

If you wish to re-enable this Game Object at a later date you will need to

re-create its InteractiveObject by calling `setInteractive` again.

If you wish to only temporarily stop an object from receiving input then use

`disableInteractive` instead, as that toggles the interactive state, where-as

this erases it completely.

If you wish to resize a hit area, don't remove and then set it as being

interactive. Instead, access the hitarea object directly and resize the shape

being used. I.e.: `sprite.input.hitArea.setSize(width, height)` (assuming the

shape is a Rectangle, which it is by default.)

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetCursor | boolean | Yes | false | Should the currently active Input cursor, if any, be reset to the default cursor? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#removeInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L519](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L519)  
> Since: 3.7.0

---

## removeListener

### <instance> removeListener(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## removePostPipeline

### <instance> removePostPipeline(pipeline)

**Description:**

Removes a type of Post Pipeline instances from this Game Object, based on the given name, and destroys them.

If you wish to remove all Post Pipelines use the `resetPostPipeline` method instead.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) | No | The string-based name of the pipeline, or a pipeline class. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#removePostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L299)  
> Since: 3.60.0

---

## resetPipeline

### <instance> resetPipeline([resetData])

**Description:**

Resets the WebGL Pipeline of this Game Object back to the default it was created with.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetData | boolean | Yes | false | Reset the `pipelineData` object to being an empty object? |
| --- | --- | --- | --- | --- |

**Returns:** boolean - `true` if the pipeline was reset successfully, otherwise `false`.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#resetPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L176)  
> Since: 3.0.0

---

## resetPostPipeline

### <instance> resetPostPipeline([resetData])

**Description:**

Resets the WebGL Post Pipelines of this Game Object. It does this by calling

the `destroy` method on each post pipeline and then clearing the local array.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetData | boolean | Yes | false | Reset the `postPipelineData` object to being an empty object? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#resetPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L269](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L269)  
> Since: 3.60.0

---

## setAbove

### <instance> setAbove(gameObject)

**Description:**

Move this Game Object so that it appears above the given Game Object.

This means it will render immediately after the other object in the display list.

Both objects must belong to the same display list, or parent container.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that this Game Object will be moved to be above. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setAbove](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L139)  
> Since: 3.85.0

---

## setActive

### <instance> setActive(value)

**Description:**

Sets the `active` property of this Game Object and returns this Game Object for further chaining.

A Game Object with its `active` property set to `true` will be updated by the Scenes UpdateList.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | True if this Game Object should be set as active, false if not. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setActive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L216)  
> Since: 3.0.0

---

## setAlpha

### <instance> setAlpha([topLeft], [topRight], [bottomLeft], [bottomRight])

**Description:**

Set the Alpha level of this Game Object. The alpha controls the opacity of the Game Object as it renders.

Alpha values are provided as a float between 0, fully transparent, and 1, fully opaque.

If your game is running under WebGL you can optionally specify four different alpha values, each of which

correspond to the four corners of the Game Object. Under Canvas only the `topLeft` value given is used.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| topLeft | number | Yes | 1 | The alpha value used for the top-left of the Game Object. If this is the only value given it's applied across the whole Game Object. |
| --- | --- | --- | --- | --- |
| topRight | number | Yes |  | The alpha value used for the top-right of the Game Object. WebGL only. |
| bottomLeft | number | Yes |  | The alpha value used for the bottom-left of the Game Object. WebGL only. |
| bottomRight | number | Yes |  | The alpha value used for the bottom-right of the Game Object. WebGL only. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Alpha#setAlpha](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L92)  
> Since: 3.0.0

---

## setAngle

### <instance> setAngle([degrees])

**Description:**

Sets the angle of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| degrees | number | Yes | 0 | The rotation of this Game Object, in degrees. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setAngle](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L364](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L364)  
> Since: 3.0.0

---

## setBelow

### <instance> setBelow(gameObject)

**Description:**

Move this Game Object so that it appears below the given Game Object.

This means it will render immediately under the other object in the display list.

Both objects must belong to the same display list, or parent container.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that this Game Object will be moved to be below. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setBelow](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L167)  
> Since: 3.85.0

---

## setBlendMode

### <instance> setBlendMode(value)

**Description:**

Sets the Blend Mode being used by this Game Object.

This can be a const, such as `Phaser.BlendModes.SCREEN`, or an integer, such as 4 (for Overlay)

Under WebGL only the following Blend Modes are available:

* NORMAL
* ADD
* MULTIPLY
* SCREEN
* ERASE (only works when rendering to a framebuffer, like a Render Texture)

Canvas has more available depending on browser support.

You can also create your own custom Blend Modes in WebGL.

Blend modes have different effects under Canvas and WebGL, and from browser to browser, depending

on support. Blend Modes also cause a WebGL batch flush should it encounter a new blend mode. For these

reasons try to be careful about the construction of your Scene and the frequency in which blend modes

are used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | [Phaser.BlendModes](../namespace/blendmodes.md) | number | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#setBlendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L80)  
> Since: 3.0.0

---

## setCenterAlign

### <instance> setCenterAlign()

**Description:**

Set the lines of text in this BitmapText to be center-aligned.

This only has any effect if this BitmapText contains more than one line of text.

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L321](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L321)  
> Since: 3.11.0

---

## setCharacterTint

### <instance> setCharacterTint([start], [length], [tintFill], [topLeft], [topRight], [bottomLeft], [bottomRight])

**Description:**

Sets a tint on a range of characters in this Bitmap Text, starting from the `start` parameter index

and running for `length` quantity of characters.

The `start` parameter can be negative. In this case, it starts at the end of the text and counts

backwards `start` places.

You can also pass in -1 as the `length` and it will tint all characters from `start`

up until the end of the string.

Remember that spaces and punctuation count as characters.

This is a WebGL only feature and only works with Static Bitmap Text, not Dynamic.

The tint works by taking the pixel color values from the Bitmap Text texture, and then

multiplying it by the color value of the tint. You can provide either one color value,

in which case the whole character will be tinted in that color. Or you can provide a color

per corner. The colors are blended together across the extent of the character range.

To swap this from being an additive tint to a fill based tint, set the `tintFill` parameter to `true`.

To modify the tint color once set, call this method again with new color values.

Using `setWordTint` can override tints set by this function, and vice versa.

To remove a tint call this method with just the `start`, and optionally, the `length` parameters defined.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| start | number | Yes | 0 | The starting character to begin the tint at. If negative, it counts back from the end of the text. |
| --- | --- | --- | --- | --- |
| length | number | Yes | 1 | The number of characters to tint. Remember that spaces count as a character too. Pass -1 to tint all characters from `start` onwards. |
| tintFill | boolean | Yes | false | Use a fill-based tint (true), or an additive tint (false) |
| topLeft | number | Yes | "0xffffff" | The tint being applied to the top-left of the character. If not other values are given this value is applied evenly, tinting the whole character. |
| topRight | number | Yes |  | The tint being applied to the top-right of the character. |
| bottomLeft | number | Yes |  | The tint being applied to the bottom-left of the character. |
| bottomRight | number | Yes |  | The tint being applied to the bottom-right of the character. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L497](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L497)  
> Since: 3.50.0

---

## setData

### <instance> setData(key, [data])

**Description:**

Allows you to store a key value pair within this Game Objects Data Manager.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

```
Copy
sprite.setData('name', 'Red Gem Stone');


```

You can also pass in an object of key value pairs as the first argument:

```
Copy
sprite.setData({ name: 'Red Gem Stone', level: 2, owner: 'Link', gold: 50 });


```

To get a value back again you can call `getData`:

```
Copy
sprite.getData('gold');


```

Or you can access the value directly via the `values` property, where it works like any other variable:

```
Copy
sprite.data.values.gold += 50;


```

When the value is first set, a `setdata` event is emitted from this Game Object.

If the key already exists, a `changedata` event is emitted instead, along an event named after the key.

For example, if you updated an existing key called `PlayerLives` then it would emit the event `changedata-PlayerLives`.

These events will be emitted regardless if you use this method to set the value, or the direct `values` setter.

Please note that the data keys are case-sensitive and must be valid JavaScript Object property strings.

This means the keys `gold` and `Gold` are treated as two unique values within the Data Manager.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | object | No | The key to set the value for. Or an object of key value pairs. If an object the `data` argument is ignored. |
| --- | --- | --- | --- |
| data | \* | Yes | The value to set for the given key. If an object is provided as the key this argument is ignored. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L295)  
> Since: 3.0.0

---

## setDataEnabled

### <instance> setDataEnabled()

**Description:**

Adds a Data Manager component to this Game Object.

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setDataEnabled](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L276)  
> Since: 3.0.0

---

## setDepth

### <instance> setDepth(value)

**Description:**

The depth of this Game Object within the Scene.

The depth is also known as the 'z-index' in some environments, and allows you to change the rendering order

of Game Objects, without actually moving their position in the display list.

The default depth is zero. A Game Object with a higher depth

value will always render in front of one with a lower value.

Setting the depth will queue a depth sort event within the Scene.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The depth of this Game Object. Ensure this value is only ever a number data-type. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L64)  
> Since: 3.0.0

---

## setDisplayOrigin

### <instance> setDisplayOrigin([x], [y])

**Description:**

Sets the display origin of this Game Object.

The difference between this and setting the origin is that you can use pixel values for setting the display origin.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal display origin value. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical display origin value. If not defined it will be set to the value of `x`. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setDisplayOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L159)  
> Since: 3.0.0

---

## setDropShadow

### <instance> setDropShadow([x], [y], [color], [alpha])

**Description:**

Sets a drop shadow effect on this Bitmap Text.

This is a WebGL only feature and only works with Static Bitmap Text, not Dynamic.

You can set the vertical and horizontal offset of the shadow, as well as the color and alpha.

Once a shadow has been enabled you can modify the `dropShadowX` and `dropShadowY` properties of this

Bitmap Text directly to adjust the position of the shadow in real-time.

If you wish to clear the shadow, call this method with no parameters specified.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal offset of the drop shadow. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical offset of the drop shadow. |
| color | number | Yes | "0x000000" | The color of the drop shadow, given as a hex value, i.e. `0x000000` for black. |
| alpha | number | Yes | 0.5 | The alpha of the drop shadow, given as a float between 0 and 1. This is combined with the Bitmap Text alpha as well. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L459](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L459)  
> Since: 3.50.0

---

## setFont

### <instance> setFont(font, [size], [align])

**Description:**

Changes the font this BitmapText is using to render.

The new texture is loaded and applied to the BitmapText. The existing text, size and alignment are preserved,

unless overridden via the arguments.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| font | string | No |  | The key of the font to use from the Bitmap Font cache. |
| --- | --- | --- | --- | --- |
| size | number | Yes |  | The font size of this Bitmap Text. If not specified the current size will be used. |
| align | number | Yes | 0 | The alignment of the text in a multi-line BitmapText object. If not specified the current alignment will be used. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L783](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L783)  
> Since: 3.11.0

---

## setFontSize

### <instance> setFontSize(size)

**Description:**

Set the font size of this Bitmap Text.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| size | number | No | The font size to set. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L357](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L357)  
> Since: 3.0.0

---

## setFrame

### <instance> setFrame(frame, [updateSize], [updateOrigin])

**Description:**

Sets the frame this Game Object will use to render with.

If you pass a string or index then the Frame has to belong to the current Texture being used

by this Game Object.

If you pass a Frame instance, then the Texture being used by this Game Object will also be updated.

Calling `setFrame` will modify the `width` and `height` properties of your Game Object.

It will also change the `origin` if the Frame has a custom pivot point, as exported from packages like Texture Packer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | No |  |
| --- | --- | --- | --- | --- |
| updateSize | boolean | Yes | true | Should this call adjust the size of the Game Object? |
| updateOrigin | boolean | Yes | true | Should this call adjust the origin of the Game Object? |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Texture#setFrame](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L75)  
> Since: 3.0.0

---

## setInteractive

### <instance> setInteractive([hitArea], [callback], [dropZone])

**Description:**

Pass this Game Object to the Input Manager to enable it for Input.

Input works by using hit areas, these are nearly always geometric shapes, such as rectangles or circles, that act as the hit area

for the Game Object. However, you can provide your own hit area shape and callback, should you wish to handle some more advanced

input detection.

If no arguments are provided it will try and create a rectangle hit area based on the texture frame the Game Object is using. If

this isn't a texture-bound object, such as a Graphics or BitmapText object, this will fail, and you'll need to provide a specific

shape for it to use.

You can also provide an Input Configuration Object as the only argument to this method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| hitArea | [Phaser.Types.Input.InputConfiguration](../typedef/types-input.md) | any | Yes |  | Either an input configuration object, or a geometric shape that defines the hit area for the Game Object. If not given it will try to create a Rectangle based on the texture frame. |
| --- | --- | --- | --- | --- |
| callback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes |  | The callback that determines if the pointer is within the Hit Area shape or not. If you provide a shape you must also provide a callback. |
| dropZone | boolean | Yes | false | Should this Game Object be treated as a drop zone target? |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L456](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L456)  
> Since: 3.0.0

---

## setLeftAlign

### <instance> setLeftAlign()

**Description:**

Set the lines of text in this BitmapText to be left-aligned.

This only has any effect if this BitmapText contains more than one line of text.

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L303](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L303)  
> Since: 3.11.0

---

## setLetterSpacing

### <instance> setLetterSpacing([spacing])

**Description:**

Sets the letter spacing between each character of this Bitmap Text.

Can be a positive value to increase the space, or negative to reduce it.

Spacing is applied after the kerning values have been set.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| spacing | number | Yes | 0 | The amount of horizontal space to add between each character. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L376](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L376)  
> Since: 3.4.0

---

## setLineSpacing

### <instance> setLineSpacing([spacing])

**Description:**

Sets the line spacing value. This value is added to the font height to

calculate the overall line height.

Spacing can be a negative or positive number.

Only has an effect if this BitmapText object contains multiple lines of text.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| spacing | number | Yes | 0 | The amount of space to add between each line in multi-line text. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L399](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L399)  
> Since: 3.60.0

---

## setMask

### <instance> setMask(mask)

**Description:**

Sets the mask that this Game Object will use to render with.

The mask must have been previously created and can be either a GeometryMask or a BitmapMask.

Note: Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.

If a mask is already set on this Game Object it will be immediately replaced.

Masks are positioned in global space and are not relative to the Game Object to which they

are applied. The reason for this is that multiple Game Objects can all share the same mask.

Masks have no impact on physics or input detection. They are purely a rendering component

that allows you to limit what is visible during the render pass.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mask | [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) | [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md) | No | The mask this Game Object will use when rendering. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#setMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L28](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L28)  
> Since: 3.6.2

---

## setMaxWidth

### <instance> setMaxWidth(value, [wordWrapCharCode])

**Description:**

Sets the maximum display width of this BitmapText in pixels.

If `BitmapText.text` is longer than `maxWidth` then the lines will be automatically wrapped

based on the previous whitespace character found in the line.

If no whitespace was found then no wrapping will take place and consequently the `maxWidth` value will not be honored.

Disable maxWidth by setting the value to 0.

You can set the whitespace character to be searched for by setting the `wordWrapCharCode` parameter or property.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The maximum display width of this BitmapText in pixels. Set to zero to disable. |
| --- | --- | --- | --- |
| wordWrapCharCode | number | Yes | The character code to check for when word wrapping. Defaults to 32 (the space character). |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L821](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L821)  
> Since: 3.21.0

---

## setName

### <instance> setName(value)

**Description:**

Sets the `name` property of this Game Object and returns this Game Object for further chaining.

The `name` property is not populated by Phaser and is presented for your own use.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | No | The name to be given to this Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setName](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L234)  
> Since: 3.0.0

---

## setOrigin

### <instance> setOrigin([x], [y])

**Description:**

Sets the origin of this Game Object.

The values are given in the range 0 to 1.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0.5 | The horizontal origin value. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical origin value. If not defined it will be set to the value of `x`. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L112)  
> Since: 3.0.0

---

## setOriginFromFrame

### <instance> setOriginFromFrame()

**Description:**

Sets the origin of this Game Object based on the Pivot values in its Frame.

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setOriginFromFrame](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L136)  
> Since: 3.0.0

---

## setPipeline

### <instance> setPipeline(pipeline, [pipelineData], [copyData])

**Description:**

Sets the main WebGL Pipeline of this Game Object.

Also sets the `pipelineData` property, if the parameter is given.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | No |  | Either the string-based name of the pipeline, or a pipeline instance to set. |
| --- | --- | --- | --- | --- |
| pipelineData | object | Yes |  | Optional pipeline data object that is set in to the `pipelineData` property of this Game Object. |
| copyData | boolean | Yes | true | Should the pipeline data object be *deep copied* into the `pipelineData` property of this Game Object? If `false` it will be set by reference instead. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#setPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L100)  
> Since: 3.0.0

---

## setPipelineData

### <instance> setPipelineData(key, [value])

**Description:**

Adds an entry to the `pipelineData` object belonging to this Game Object.

If the 'key' already exists, its value is updated. If it doesn't exist, it is created.

If `value` is undefined, and `key` exists, `key` is removed from the data object.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the pipeline data to set, update, or delete. |
| --- | --- | --- | --- |
| value | any | Yes | The value to be set with the key. If `undefined` then `key` will be deleted from the object. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#setPipelineData](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L144)  
> Since: 3.50.0

---

## setPosition

### <instance> setPosition([x], [y], [z], [w])

**Description:**

Sets the position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The y position of this Game Object. If not set it will use the `x` value. |
| z | number | Yes | 0 | The z position of this Game Object. |
| w | number | Yes | 0 | The w position of this Game Object. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L265](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L265)  
> Since: 3.0.0

---

## setPostPipeline

### <instance> setPostPipeline(pipelines, [pipelineData], [copyData])

**Description:**

Sets one, or more, Post Pipelines on this Game Object.

Post Pipelines are invoked after this Game Object has rendered to its target and

are commonly used for post-fx.

The post pipelines are appended to the `postPipelines` array belonging to this

Game Object. When the renderer processes this Game Object, it iterates through the post

pipelines in the order in which they appear in the array. If you are stacking together

multiple effects, be aware that the order is important.

If you call this method multiple times, the new pipelines will be appended to any existing

post pipelines already set. Use the `resetPostPipeline` method to clear them first, if required.

You can optionally also set the `postPipelineData` property, if the parameter is given.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| pipelines | string | Array.<string> | function | Array.<function()> | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) |
| --- | --- | --- | --- | --- |
| pipelineData | object | Yes |  | Optional pipeline data object that is set in to the `postPipelineData` property of this Game Object. |
| copyData | boolean | Yes | true | Should the pipeline data object be *deep copied* into the `postPipelineData` property of this Game Object? If `false` it will be set by reference instead. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#setPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L140)  
> Since: 3.60.0

---

## setPostPipelineData

### <instance> setPostPipelineData(key, [value])

**Description:**

Adds an entry to the `postPipelineData` object belonging to this Game Object.

If the 'key' already exists, its value is updated. If it doesn't exist, it is created.

If `value` is undefined, and `key` exists, `key` is removed from the data object.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the pipeline data to set, update, or delete. |
| --- | --- | --- | --- |
| value | any | Yes | The value to be set with the key. If `undefined` then `key` will be deleted from the object. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#setPostPipelineData](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L205)  
> Since: 3.60.0

---

## setRandomPosition

### <instance> setRandomPosition([x], [y], [width], [height])

**Description:**

Sets the position of this Game Object to be a random position within the confines of

the given area.

If no area is specified a random position between 0 x 0 and the game width x height is used instead.

The position does not factor in the size of this Game Object, meaning that only the origin is

guaranteed to be within the area.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of the top-left of the random area. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y position of the top-left of the random area. |
| width | number | Yes |  | The width of the random area. |
| height | number | Yes |  | The height of the random area. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRandomPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L313](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L313)  
> Since: 3.8.0

---

## setRightAlign

### <instance> setRightAlign()

**Description:**

Set the lines of text in this BitmapText to be right-aligned.

This only has any effect if this BitmapText contains more than one line of text.

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L339](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L339)  
> Since: 3.11.0

---

## setRotation

### <instance> setRotation([radians])

**Description:**

Sets the rotation of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radians | number | Yes | 0 | The rotation of this Game Object, in radians. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L345](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L345)  
> Since: 3.0.0

---

## setScale

### <instance> setScale([x], [y])

**Description:**

Sets the scale of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 1 | The horizontal scale of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scale of this Game Object. If not set it will use the `x` value. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setScale](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L383](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L383)  
> Since: 3.0.0

---

## setScrollFactor

### <instance> setScrollFactor(x, [y])

**Description:**

Sets the scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal scroll factor of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scroll factor of this Game Object. If not set it will use the `x` value. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#setScrollFactor](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L64)  
> Since: 3.0.0

---

## setState

### <instance> setState(value)

**Description:**

Sets the current state of this Game Object.

Phaser itself will never modify the State of a Game Object, although plugins may do so.

For example, a Game Object could change from a state of 'moving', to 'attacking', to 'dead'.

The state value should typically be an integer (ideally mapped to a constant

in your game code), but could also be a string. It is recommended to keep it light and simple.

If you need to store complex data about your Game Object, look at using the Data Component instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | string | No | The state of the Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setState](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L252)  
> Since: 3.16.0

---

## setText

### <instance> setText(value)

**Description:**

Set the textual content of this BitmapText.

An array of strings will be converted into multi-line text. Use the align methods to change multi-line alignment.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | Array.<string> | No | The string, or array of strings, to be set as the content of this BitmapText. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L423](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L423)  
> Since: 3.0.0

---

## setTexture

### <instance> setTexture(key, [frame], [updateSize], [updateOrigin])

**Description:**

Sets the texture and frame this Game Object will use to render with.

Textures are referenced by their string-based keys, as stored in the Texture Manager.

Calling this method will modify the `width` and `height` properties of your Game Object.

It will also change the `origin` if the Frame has a custom pivot point, as exported from packages like Texture Packer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Textures.Texture](textures-texture.md) | No |  | The key of the texture to be used, as stored in the Texture Manager, or a Texture instance. |
| --- | --- | --- | --- | --- |
| frame | string | number | Yes |  | The name or index of the frame within the Texture. |
| updateSize | boolean | Yes | true | Should this call adjust the size of the Game Object? |
| updateOrigin | boolean | Yes | true | Should this call change the origin of the Game Object? |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Texture#setTexture](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L49)  
> Since: 3.0.0

---

## setTint

### <instance> setTint([topLeft], [topRight], [bottomLeft], [bottomRight])

**Description:**

Sets an additive tint on this Game Object.

The tint works by taking the pixel color values from the Game Objects texture, and then

multiplying it by the color value of the tint. You can provide either one color value,

in which case the whole Game Object will be tinted in that color. Or you can provide a color

per corner. The colors are blended together across the extent of the Game Object.

To modify the tint color once set, either call this method again with new values or use the

`tint` property to set all colors at once. Or, use the properties `tintTopLeft`, `tintTopRight,

`tintBottomLeft` and `tintBottomRight` to set the corner color values independently.

To remove a tint call `clearTint`.

To swap this from being an additive tint to a fill based tint set the property `tintFill` to `true`.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| topLeft | number | Yes | "0xffffff" | The tint being applied to the top-left of the Game Object. If no other values are given this value is applied evenly, tinting the whole Game Object. |
| --- | --- | --- | --- | --- |
| topRight | number | Yes |  | The tint being applied to the top-right of the Game Object. |
| bottomLeft | number | Yes |  | The tint being applied to the bottom-left of the Game Object. |
| bottomRight | number | Yes |  | The tint being applied to the bottom-right of the Game Object. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Tint#setTint](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L98)  
> Since: 3.0.0

---

## setTintFill

### <instance> setTintFill([topLeft], [topRight], [bottomLeft], [bottomRight])

**Description:**

Sets a fill-based tint on this Game Object.

Unlike an additive tint, a fill-tint literally replaces the pixel colors from the texture

with those in the tint. You can use this for effects such as making a player flash 'white'

if hit by something. You can provide either one color value, in which case the whole

Game Object will be rendered in that color. Or you can provide a color per corner. The colors

are blended together across the extent of the Game Object.

To modify the tint color once set, either call this method again with new values or use the

`tint` property to set all colors at once. Or, use the properties `tintTopLeft`, `tintTopRight,

`tintBottomLeft` and `tintBottomRight` to set the corner color values independently.

To remove a tint call `clearTint`.

To swap this from being a fill-tint to an additive tint set the property `tintFill` to `false`.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| topLeft | number | Yes | "0xffffff" | The tint being applied to the top-left of the Game Object. If not other values are given this value is applied evenly, tinting the whole Game Object. |
| --- | --- | --- | --- | --- |
| topRight | number | Yes |  | The tint being applied to the top-right of the Game Object. |
| bottomLeft | number | Yes |  | The tint being applied to the bottom-left of the Game Object. |
| bottomRight | number | Yes |  | The tint being applied to the bottom-right of the Game Object. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Tint#setTintFill](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L146](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L146)  
> Since: 3.11.0

---

## setToBack

### <instance> setToBack()

**Description:**

Sets this Game Object to the back of the display list, or the back of its parent container.

Being at the back means it will render below everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToBack](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L115)  
> Since: 3.85.0

---

## setToTop

### <instance> setToTop()

**Description:**

Sets this Game Object to be at the top of the display list, or the top of its parent container.

Being at the top means it will render on-top of everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToTop](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L91)  
> Since: 3.85.0

---

## setVisible

### <instance> setVisible(value)

**Description:**

Sets the visibility of this Game Object.

An invisible Game Object will skip rendering, but will still process update logic.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The visible state of the Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Visible#setVisible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L63)  
> Since: 3.0.0

---

## setW

### <instance> setW([value])

**Description:**

Sets the w position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The w position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setW](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L465](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L465)  
> Since: 3.0.0

---

## setWordTint

### <instance> setWordTint(word, [count], [tintFill], [topLeft], [topRight], [bottomLeft], [bottomRight])

**Description:**

Sets a tint on a matching word within this Bitmap Text.

The `word` parameter can be either a string or a number.

If a string, it will run a string comparison against the text contents, and if matching,

it will tint the whole word.

If a number, if till that word, based on its offset within the text contents.

The `count` parameter controls how many words are replaced. Pass in -1 to replace them all.

This parameter is ignored if you pass a number as the `word` to be searched for.

This is a WebGL only feature and only works with Static Bitmap Text, not Dynamic.

The tint works by taking the pixel color values from the Bitmap Text texture, and then

multiplying it by the color value of the tint. You can provide either one color value,

in which case the whole character will be tinted in that color. Or you can provide a color

per corner. The colors are blended together across the extent of the character range.

To swap this from being an additive tint to a fill based tint, set the `tintFill` parameter to `true`.

To modify the tint color once set, call this method again with new color values.

Using `setCharacterTint` can override tints set by this function, and vice versa.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| word | string | number | No |  | The word to search for. Either a string, or an index of the word in the words array. |
| --- | --- | --- | --- | --- |
| count | number | Yes | 1 | The number of matching words to tint. Pass -1 to tint all matching words. |
| tintFill | boolean | Yes | false | Use a fill-based tint (true), or an additive tint (false) |
| topLeft | number | Yes | "0xffffff" | The tint being applied to the top-left of the word. If not other values are given this value is applied evenly, tinting the whole word. |
| topRight | number | Yes |  | The tint being applied to the top-right of the word. |
| bottomLeft | number | Yes |  | The tint being applied to the bottom-left of the word. |
| bottomRight | number | Yes |  | The tint being applied to the bottom-right of the word. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This BitmapText Object.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L606](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L606)  
> Since: 3.50.0

---

## setX

### <instance> setX([value])

**Description:**

Sets the x position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The x position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L405](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L405)  
> Since: 3.0.0

---

## setY

### <instance> setY([value])

**Description:**

Sets the y position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The y position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L424](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L424)  
> Since: 3.0.0

---

## setZ

### <instance> setZ([value])

**Description:**

Sets the z position of this Game Object.

Note: The z position does not control the rendering order of 2D Game Objects. Use

[Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md) instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The z position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setZ](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L443](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L443)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## toggleData

### <instance> toggleData(key)

**Description:**

Toggle a boolean value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is toggled from false.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

When the value is first set, a `setdata` event is emitted from this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key to toggle the value for. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#toggleData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L387)  
> Since: 3.23.0

---

## toJSON

### <instance> toJSON()

**Description:**

Build a JSON representation of this Bitmap Text.

**Overrides:** Phaser.GameObjects.GameObject#toJSON

**Returns:** [Phaser.Types.GameObjects.BitmapText.JSONBitmapText](../typedef/types-gameobjects-bitmaptext.md) - A JSON representation of this Bitmap Text.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L1100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1100)  
> Since: 3.0.0

---

## update

### <instance> update([args])

**Description:**

To be overridden by custom GameObjects. Allows base objects to be used in a Pool.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| args | \* | Yes | args |
| --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.GameObject#update](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L592](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L592)  
> Since: 3.0.0

---

## updateDisplayOrigin

### <instance> updateDisplayOrigin()

**Description:**

Updates the Display Origin cached values internally stored on this Game Object.

You don't usually call this directly, but it is exposed for edge-cases where you may.

**Overrides:** Phaser.GameObjects.Components.Origin#updateDisplayOrigin

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - This Game Object instance.

> Source: [src/gameobjects/bitmaptext/static/BitmapText.js#L765](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapText.js#L765)  
> Since: 3.0.0

---

## willRender

### <instance> willRender(camera)

**Description:**

Compares the renderMask with the renderFlags to see if this Game Object will render or not.

Also checks the Game Object against the given Cameras exclusion list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera to check against this Game Object. |
| --- | --- | --- | --- |

**Returns:** boolean - True if the Game Object should be rendered, otherwise false.

**Inherits:** [Phaser.GameObjects.GameObject#willRender](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L617](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L617)  
> Since: 3.0.0

---

# Private Methods

## prepareBoundsOutput

### <instance> prepareBoundsOutput(output, [includeParent])

**Description:**

Processes the bounds output vector before returning it.

**Tags:**

* generic

**Access:** private

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No |  | An object to store the values in. If not provided a new Vector2 will be created. |
| --- | --- | --- | --- | --- |
| includeParent | boolean | Yes | false | If this Game Object has a parent Container, include it (and all other ancestors) in the resulting vector? |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#prepareBoundsOutput](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L21)  
> Since: 3.18.0

---

## renderCanvas

### <instance> renderCanvas(renderer, src, camera, parentMatrix)

**Description:**

Renders this Game Object with the Canvas Renderer to the given Camera.

The object will not render if any of its renderFlags are set or it is being actively filtered out by the Camera.

This method should not be called directly. It is a utility function of the Render module.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) | No | A reference to the current active Canvas renderer. |
| --- | --- | --- | --- |
| src | [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

> Source: [src/gameobjects/bitmaptext/static/BitmapTextCanvasRenderer.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapTextCanvasRenderer.js#L9)  
> Since: 3.0.0

---

## renderWebGL

### <instance> renderWebGL(renderer, src, camera, parentMatrix)

**Description:**

Renders this Game Object with the WebGL Renderer to the given Camera.

The object will not render if any of its renderFlags are set or it is being actively filtered out by the Camera.

This method should not be called directly. It is a utility function of the Render module.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) | No | A reference to the current active WebGL renderer. |
| --- | --- | --- | --- |
| src | [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

> Source: [src/gameobjects/bitmaptext/static/BitmapTextWebGLRenderer.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapTextWebGLRenderer.js#L11)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [align](#align)

    - [align: number](#align-number)
  + [ALIGN\_CENTER](#align_center)

    - [ALIGN\_CENTER: number](#align_center-number)
  + [ALIGN\_LEFT](#align_left)

    - [ALIGN\_LEFT: number](#align_left-number)
  + [ALIGN\_RIGHT](#align_right)

    - [ALIGN\_RIGHT: number](#align_right-number)
  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [alphaBottomLeft](#alphabottomleft)

    - [alphaBottomLeft: number](#alphabottomleft-number)
  + [alphaBottomRight](#alphabottomright)

    - [alphaBottomRight: number](#alphabottomright-number)
  + [alphaTopLeft](#alphatopleft)

    - [alphaTopLeft: number](#alphatopleft-number)
  + [alphaTopRight](#alphatopright)

    - [alphaTopRight: number](#alphatopright-number)
  + [angle](#angle)

    - [angle: number](#angle-number)
  + [blendMode](#blendmode)

    - [blendMode: Phaser.BlendModes, string, number](#blendmode-phaserblendmodes-string-number)
  + [body](#body)

    - [body: Phaser.Physics.Arcade.Body, Phaser.Physics.Arcade.StaticBody, MatterJS.BodyType](#body-phaserphysicsarcadebody-phaserphysicsarcadestaticbody-matterjsbodytype)
  + [cameraFilter](#camerafilter)

    - [cameraFilter: number](#camerafilter-number)
  + [data](#data)

    - [data: Phaser.Data.DataManager](#data-phaserdatadatamanager)
  + [defaultPipeline](#defaultpipeline)

    - [defaultPipeline: Phaser.Renderer.WebGL.WebGLPipeline](#defaultpipeline-phaserrendererwebglwebglpipeline)
  + [depth](#depth)

    - [depth: number](#depth-number)
  + [displayHeight](#displayheight)

    - [displayHeight: number](#displayheight-number)
  + [displayList](#displaylist)

    - [displayList: Phaser.GameObjects.DisplayList, Phaser.GameObjects.Layer](#displaylist-phasergameobjectsdisplaylist-phasergameobjectslayer)
  + [displayOriginX](#displayoriginx)

    - [displayOriginX: number](#displayoriginx-number)
  + [displayOriginY](#displayoriginy)

    - [displayOriginY: number](#displayoriginy-number)
  + [displayWidth](#displaywidth)

    - [displayWidth: number](#displaywidth-number)
  + [dropShadowAlpha](#dropshadowalpha)

    - [dropShadowAlpha: number](#dropshadowalpha-number)
  + [dropShadowColor](#dropshadowcolor)

    - [dropShadowColor: number](#dropshadowcolor-number)
  + [dropShadowX](#dropshadowx)

    - [dropShadowX: number](#dropshadowx-number)
  + [dropShadowY](#dropshadowy)

    - [dropShadowY: number](#dropshadowy-number)
  + [font](#font)

    - [font: string](#font-string)
  + [fontData](#fontdata)

    - [fontData: Phaser.Types.GameObjects.BitmapText.BitmapFontData](#fontdata-phasertypesgameobjectsbitmaptextbitmapfontdata)
  + [fontSize](#fontsize)

    - [fontSize: number](#fontsize-number)
  + [frame](#frame)

    - [frame: Phaser.Textures.Frame](#frame-phasertexturesframe)
  + [fromAtlas](#fromatlas)

    - [fromAtlas: boolean](#fromatlas-boolean)
  + [hasPostPipeline](#haspostpipeline)

    - [hasPostPipeline: boolean](#haspostpipeline-boolean)
  + [hasTransformComponent](#hastransformcomponent)

    - [hasTransformComponent: boolean](#hastransformcomponent-boolean)
  + [height](#height)

    - [height: number](#height-number)
  + [ignoreDestroy](#ignoredestroy)

    - [ignoreDestroy: boolean](#ignoredestroy-boolean)
  + [input](#input)

    - [input: Phaser.Types.Input.InteractiveObject](#input-phasertypesinputinteractiveobject)
  + [isTinted](#istinted)

    - [isTinted: boolean](#istinted-boolean)
  + [letterSpacing](#letterspacing)

    - [letterSpacing: number](#letterspacing-number)
  + [lineSpacing](#linespacing)

    - [lineSpacing: number](#linespacing-number)
  + [mask](#mask)

    - [mask: Phaser.Display.Masks.BitmapMask, Phaser.Display.Masks.GeometryMask](#mask-phaserdisplaymasksbitmapmask-phaserdisplaymasksgeometrymask)
  + [maxWidth](#maxwidth)

    - [maxWidth: number](#maxwidth-number)
  + [name](#name)

    - [name: string](#name-string)
  + [originX](#originx)

    - [originX: number](#originx-number)
  + [originY](#originy)

    - [originY: number](#originy-number)
  + [parentContainer](#parentcontainer)

    - [parentContainer: Phaser.GameObjects.Container](#parentcontainer-phasergameobjectscontainer)
  + [pipeline](#pipeline)

    - [pipeline: Phaser.Renderer.WebGL.WebGLPipeline](#pipeline-phaserrendererwebglwebglpipeline)
  + [pipelineData](#pipelinedata)

    - [pipelineData: object](#pipelinedata-object)
  + [postFX](#postfx)

    - [postFX: Phaser.GameObjects.Components.FX](#postfx-phasergameobjectscomponentsfx)
  + [postPipelineData](#postpipelinedata)

    - [postPipelineData: object](#postpipelinedata-object)
  + [postPipelines](#postpipelines)

    - [postPipelines: Array.<Phaser.Renderer.WebGL.Pipelines.PostFXPipeline>](#postpipelines-arrayphaserrendererwebglpipelinespostfxpipeline)
  + [preFX](#prefx)

    - [preFX: Phaser.GameObjects.Components.FX](#prefx-phasergameobjectscomponentsfx)
  + [renderFlags](#renderflags)

    - [renderFlags: number](#renderflags-number)
  + [rotation](#rotation)

    - [rotation: number](#rotation-number)
  + [scale](#scale)

    - [scale: number](#scale-number)
  + [scaleX](#scalex)

    - [scaleX: number](#scalex-number)
  + [scaleY](#scaley)

    - [scaleY: number](#scaley-number)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [scrollFactorX](#scrollfactorx)

    - [scrollFactorX: number](#scrollfactorx-number)
  + [scrollFactorY](#scrollfactory)

    - [scrollFactorY: number](#scrollfactory-number)
  + [state](#state)

    - [state: number, string](#state-number-string)
  + [tabIndex](#tabindex)

    - [tabIndex: number](#tabindex-number)
  + [text](#text)

    - [text: string](#text-string)
  + [texture](#texture)

    - [texture: Phaser.Textures.Texture, Phaser.Textures.CanvasTexture](#texture-phasertexturestexture-phasertexturescanvastexture)
  + [tint](#tint)

    - [tint: number](#tint-number)
  + [tintBottomLeft](#tintbottomleft)

    - [tintBottomLeft: number](#tintbottomleft-number)
  + [tintBottomRight](#tintbottomright)

    - [tintBottomRight: number](#tintbottomright-number)
  + [tintFill](#tintfill)

    - [tintFill: boolean](#tintfill-boolean)
  + [tintTopLeft](#tinttopleft)

    - [tintTopLeft: number](#tinttopleft-number)
  + [tintTopRight](#tinttopright)

    - [tintTopRight: number](#tinttopright-number)
  + [type](#type)

    - [type: string](#type-string)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
  + [w](#w)

    - [w: number](#w-number)
  + [width](#width)

    - [width: number](#width-number)
  + [wordWrapCharCode](#wordwrapcharcode)

    - [wordWrapCharCode: number](#wordwrapcharcode-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
  + [z](#z)

    - [z: number](#z-number)
* [Private Members](#private-members)

  + [\_align](#_align)

    - [\_align: number](#_align-number)
  + [\_alpha](#_alpha)

    - [\_alpha: number](#_alpha-number)
  + [\_alphaBL](#_alphabl)

    - [\_alphaBL: number](#_alphabl-number)
  + [\_alphaBR](#_alphabr)

    - [\_alphaBR: number](#_alphabr-number)
  + [\_alphaTL](#_alphatl)

    - [\_alphaTL: number](#_alphatl-number)
  + [\_alphaTR](#_alphatr)

    - [\_alphaTR: number](#_alphatr-number)
  + [\_blendMode](#_blendmode)

    - [\_blendMode: number](#_blendmode-number)
  + [\_bounds](#_bounds)

    - [\_bounds: Phaser.Types.GameObjects.BitmapText.BitmapTextSize](#_bounds-phasertypesgameobjectsbitmaptextbitmaptextsize)
  + [\_depth](#_depth)

    - [\_depth: number](#_depth-number)
  + [\_dirty](#_dirty)

    - [\_dirty: boolean](#_dirty-boolean)
  + [\_fontSize](#_fontsize)

    - [\_fontSize: number](#_fontsize-number)
  + [\_letterSpacing](#_letterspacing)

    - [\_letterSpacing: number](#_letterspacing-number)
  + [\_lineSpacing](#_linespacing)

    - [\_lineSpacing: number](#_linespacing-number)
  + [\_maxWidth](#_maxwidth)

    - [\_maxWidth: number](#_maxwidth-number)
  + [\_originComponent](#_origincomponent)

    - [\_originComponent: boolean](#_origincomponent-boolean)
  + [\_rotation](#_rotation)

    - [\_rotation: number](#_rotation-number)
  + [\_scaleX](#_scalex)

    - [\_scaleX: number](#_scalex-number)
  + [\_scaleY](#_scaley)

    - [\_scaleY: number](#_scaley-number)
  + [\_text](#_text)

    - [\_text: string](#_text-string)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
  + [charColors](#charcolors)

    - [charColors: array](#charcolors-array)
  + [isCropped](#iscropped)

    - [isCropped: boolean](#iscropped-boolean)
* [Public Methods](#public-methods)

  + [addedToScene](#addedtoscene)

    - [<instance> addedToScene()](#instance-addedtoscene)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addToDisplayList](#addtodisplaylist)

    - [<instance> addToDisplayList([displayList])](#instance-addtodisplaylistdisplaylist)
  + [addToUpdateList](#addtoupdatelist)

    - [<instance> addToUpdateList()](#instance-addtoupdatelist)
  + [clearAlpha](#clearalpha)

    - [<instance> clearAlpha()](#instance-clearalpha)
  + [clearFX](#clearfx)

    - [<instance> clearFX()](#instance-clearfx)
  + [clearMask](#clearmask)

    - [<instance> clearMask([destroyMask])](#instance-clearmaskdestroymask)
  + [clearTint](#cleartint)

    - [<instance> clearTint()](#instance-cleartint)
  + [copyPosition](#copyposition)

    - [<instance> copyPosition(source)](#instance-copypositionsource)
  + [createBitmapMask](#createbitmapmask)

    - [<instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])](#instance-createbitmapmaskmaskobject-x-y-texture-frame)
  + [createGeometryMask](#creategeometrymask)

    - [<instance> createGeometryMask([graphics])](#instance-creategeometrymaskgraphics)
  + [destroy](#destroy)

    - [<instance> destroy([fromScene])](#instance-destroyfromscene)
  + [disableInteractive](#disableinteractive)

    - [<instance> disableInteractive([resetCursor])](#instance-disableinteractiveresetcursor)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [getBottomCenter](#getbottomcenter)

    - [<instance> getBottomCenter([output], [includeParent])](#instance-getbottomcenteroutput-includeparent)
  + [getBottomLeft](#getbottomleft)

    - [<instance> getBottomLeft([output], [includeParent])](#instance-getbottomleftoutput-includeparent)
  + [getBottomRight](#getbottomright)

    - [<instance> getBottomRight([output], [includeParent])](#instance-getbottomrightoutput-includeparent)
  + [getBounds](#getbounds)

    - [<instance> getBounds([output])](#instance-getboundsoutput)
  + [getCenter](#getcenter)

    - [<instance> getCenter([output], [includeParent])](#instance-getcenteroutput-includeparent)
  + [getCharacterAt](#getcharacterat)

    - [<instance> getCharacterAt(x, y, [camera])](#instance-getcharacteratx-y-camera)
  + [getData](#getdata)

    - [<instance> getData(key)](#instance-getdatakey)
  + [getDisplayList](#getdisplaylist)

    - [<instance> getDisplayList()](#instance-getdisplaylist)
  + [getIndexList](#getindexlist)

    - [<instance> getIndexList()](#instance-getindexlist)
  + [getLeftCenter](#getleftcenter)

    - [<instance> getLeftCenter([output], [includeParent])](#instance-getleftcenteroutput-includeparent)
  + [getLocalPoint](#getlocalpoint)

    - [<instance> getLocalPoint(x, y, [point], [camera])](#instance-getlocalpointx-y-point-camera)
  + [getLocalTransformMatrix](#getlocaltransformmatrix)

    - [<instance> getLocalTransformMatrix([tempMatrix])](#instance-getlocaltransformmatrixtempmatrix)
  + [getParentRotation](#getparentrotation)

    - [<instance> getParentRotation()](#instance-getparentrotation)
  + [getPipelineName](#getpipelinename)

    - [<instance> getPipelineName()](#instance-getpipelinename)
  + [getPostPipeline](#getpostpipeline)

    - [<instance> getPostPipeline(pipeline)](#instance-getpostpipelinepipeline)
  + [getRightCenter](#getrightcenter)

    - [<instance> getRightCenter([output], [includeParent])](#instance-getrightcenteroutput-includeparent)
  + [getTextBounds](#gettextbounds)

    - [<instance> getTextBounds([round])](#instance-gettextboundsround)
  + [getTopCenter](#gettopcenter)

    - [<instance> getTopCenter([output], [includeParent])](#instance-gettopcenteroutput-includeparent)
  + [getTopLeft](#gettopleft)

    - [<instance> getTopLeft([output], [includeParent])](#instance-gettopleftoutput-includeparent)
  + [getTopRight](#gettopright)

    - [<instance> getTopRight([output], [includeParent])](#instance-gettoprightoutput-includeparent)
  + [getWorldTransformMatrix](#getworldtransformmatrix)

    - [<instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])](#instance-getworldtransformmatrixtempmatrix-parentmatrix)
  + [incData](#incdata)

    - [<instance> incData(key, [amount])](#instance-incdatakey-amount)
  + [initPipeline](#initpipeline)

    - [<instance> initPipeline([pipeline])](#instance-initpipelinepipeline)
  + [initPostPipeline](#initpostpipeline)

    - [<instance> initPostPipeline([preFX])](#instance-initpostpipelineprefx)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [ParseFromAtlas](#parsefromatlas)

    - [<static> ParseFromAtlas(scene, fontName, textureKey, frameKey, xmlKey, [xSpacing], [ySpacing])](#static-parsefromatlasscene-fontname-texturekey-framekey-xmlkey-xspacing-yspacing)
  + [ParseXMLBitmapFont](#parsexmlbitmapfont)

    - [<static> ParseXMLBitmapFont(xml, frame, [xSpacing], [ySpacing])](#static-parsexmlbitmapfontxml-frame-xspacing-yspacing)
  + [preDestroy](#predestroy)

    - [<instance> preDestroy()](#instance-predestroy)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removedFromScene](#removedfromscene)

    - [<instance> removedFromScene()](#instance-removedfromscene)
  + [removeFromDisplayList](#removefromdisplaylist)

    - [<instance> removeFromDisplayList()](#instance-removefromdisplaylist)
  + [removeFromUpdateList](#removefromupdatelist)

    - [<instance> removeFromUpdateList()](#instance-removefromupdatelist)
  + [removeInteractive](#removeinteractive)

    - [<instance> removeInteractive([resetCursor])](#instance-removeinteractiveresetcursor)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [removePostPipeline](#removepostpipeline)

    - [<instance> removePostPipeline(pipeline)](#instance-removepostpipelinepipeline)
  + [resetPipeline](#resetpipeline)

    - [<instance> resetPipeline([resetData])](#instance-resetpipelineresetdata)
  + [resetPostPipeline](#resetpostpipeline)

    - [<instance> resetPostPipeline([resetData])](#instance-resetpostpipelineresetdata)
  + [setAbove](#setabove)

    - [<instance> setAbove(gameObject)](#instance-setabovegameobject)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha([topLeft], [topRight], [bottomLeft], [bottomRight])](#instance-setalphatopleft-topright-bottomleft-bottomright)
  + [setAngle](#setangle)

    - [<instance> setAngle([degrees])](#instance-setangledegrees)
  + [setBelow](#setbelow)

    - [<instance> setBelow(gameObject)](#instance-setbelowgameobject)
  + [setBlendMode](#setblendmode)

    - [<instance> setBlendMode(value)](#instance-setblendmodevalue)
  + [setCenterAlign](#setcenteralign)

    - [<instance> setCenterAlign()](#instance-setcenteralign)
  + [setCharacterTint](#setcharactertint)

    - [<instance> setCharacterTint([start], [length], [tintFill], [topLeft], [topRight], [bottomLeft], [bottomRight])](#instance-setcharactertintstart-length-tintfill-topleft-topright-bottomleft-bottomright)
  + [setData](#setdata)

    - [<instance> setData(key, [data])](#instance-setdatakey-data)
  + [setDataEnabled](#setdataenabled)

    - [<instance> setDataEnabled()](#instance-setdataenabled)
  + [setDepth](#setdepth)

    - [<instance> setDepth(value)](#instance-setdepthvalue)
  + [setDisplayOrigin](#setdisplayorigin)

    - [<instance> setDisplayOrigin([x], [y])](#instance-setdisplayoriginx-y)
  + [setDropShadow](#setdropshadow)

    - [<instance> setDropShadow([x], [y], [color], [alpha])](#instance-setdropshadowx-y-color-alpha)
  + [setFont](#setfont)

    - [<instance> setFont(font, [size], [align])](#instance-setfontfont-size-align)
  + [setFontSize](#setfontsize)

    - [<instance> setFontSize(size)](#instance-setfontsizesize)
  + [setFrame](#setframe)

    - [<instance> setFrame(frame, [updateSize], [updateOrigin])](#instance-setframeframe-updatesize-updateorigin)
  + [setInteractive](#setinteractive)

    - [<instance> setInteractive([hitArea], [callback], [dropZone])](#instance-setinteractivehitarea-callback-dropzone)
  + [setLeftAlign](#setleftalign)

    - [<instance> setLeftAlign()](#instance-setleftalign)
  + [setLetterSpacing](#setletterspacing)

    - [<instance> setLetterSpacing([spacing])](#instance-setletterspacingspacing)
  + [setLineSpacing](#setlinespacing)

    - [<instance> setLineSpacing([spacing])](#instance-setlinespacingspacing)
  + [setMask](#setmask)

    - [<instance> setMask(mask)](#instance-setmaskmask)
  + [setMaxWidth](#setmaxwidth)

    - [<instance> setMaxWidth(value, [wordWrapCharCode])](#instance-setmaxwidthvalue-wordwrapcharcode)
  + [setName](#setname)

    - [<instance> setName(value)](#instance-setnamevalue)
  + [setOrigin](#setorigin)

    - [<instance> setOrigin([x], [y])](#instance-setoriginx-y)
  + [setOriginFromFrame](#setoriginfromframe)

    - [<instance> setOriginFromFrame()](#instance-setoriginfromframe)
  + [setPipeline](#setpipeline)

    - [<instance> setPipeline(pipeline, [pipelineData], [copyData])](#instance-setpipelinepipeline-pipelinedata-copydata)
  + [setPipelineData](#setpipelinedata)

    - [<instance> setPipelineData(key, [value])](#instance-setpipelinedatakey-value)
  + [setPosition](#setposition)

    - [<instance> setPosition([x], [y], [z], [w])](#instance-setpositionx-y-z-w)
  + [setPostPipeline](#setpostpipeline)

    - [<instance> setPostPipeline(pipelines, [pipelineData], [copyData])](#instance-setpostpipelinepipelines-pipelinedata-copydata)
  + [setPostPipelineData](#setpostpipelinedata)

    - [<instance> setPostPipelineData(key, [value])](#instance-setpostpipelinedatakey-value)
  + [setRandomPosition](#setrandomposition)

    - [<instance> setRandomPosition([x], [y], [width], [height])](#instance-setrandompositionx-y-width-height)
  + [setRightAlign](#setrightalign)

    - [<instance> setRightAlign()](#instance-setrightalign)
  + [setRotation](#setrotation)

    - [<instance> setRotation([radians])](#instance-setrotationradians)
  + [setScale](#setscale)

    - [<instance> setScale([x], [y])](#instance-setscalex-y)
  + [setScrollFactor](#setscrollfactor)

    - [<instance> setScrollFactor(x, [y])](#instance-setscrollfactorx-y)
  + [setState](#setstate)

    - [<instance> setState(value)](#instance-setstatevalue)
  + [setText](#settext)

    - [<instance> setText(value)](#instance-settextvalue)
  + [setTexture](#settexture)

    - [<instance> setTexture(key, [frame], [updateSize], [updateOrigin])](#instance-settexturekey-frame-updatesize-updateorigin)
  + [setTint](#settint)

    - [<instance> setTint([topLeft], [topRight], [bottomLeft], [bottomRight])](#instance-settinttopleft-topright-bottomleft-bottomright)
  + [setTintFill](#settintfill)

    - [<instance> setTintFill([topLeft], [topRight], [bottomLeft], [bottomRight])](#instance-settintfilltopleft-topright-bottomleft-bottomright)
  + [setToBack](#settoback)

    - [<instance> setToBack()](#instance-settoback)
  + [setToTop](#settotop)

    - [<instance> setToTop()](#instance-settotop)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value)](#instance-setvisiblevalue)
  + [setW](#setw)

    - [<instance> setW([value])](#instance-setwvalue)
  + [setWordTint](#setwordtint)

    - [<instance> setWordTint(word, [count], [tintFill], [topLeft], [topRight], [bottomLeft], [bottomRight])](#instance-setwordtintword-count-tintfill-topleft-topright-bottomleft-bottomright)
  + [setX](#setx)

    - [<instance> setX([value])](#instance-setxvalue)
  + [setY](#sety)

    - [<instance> setY([value])](#instance-setyvalue)
  + [setZ](#setz)

    - [<instance> setZ([value])](#instance-setzvalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [toggleData](#toggledata)

    - [<instance> toggleData(key)](#instance-toggledatakey)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [update](#update)

    - [<instance> update([args])](#instance-updateargs)
  + [updateDisplayOrigin](#updatedisplayorigin)

    - [<instance> updateDisplayOrigin()](#instance-updatedisplayorigin)
  + [willRender](#willrender)

    - [<instance> willRender(camera)](#instance-willrendercamera)
* [Private Methods](#private-methods)

  + [prepareBoundsOutput](#prepareboundsoutput)

    - [<instance> prepareBoundsOutput(output, [includeParent])](#instance-prepareboundsoutputoutput-includeparent)
  + [renderCanvas](#rendercanvas)

    - [<instance> renderCanvas(renderer, src, camera, parentMatrix)](#instance-rendercanvasrenderer-src-camera-parentmatrix)
  + [renderWebGL](#renderwebgl)

    - [<instance> renderWebGL(renderer, src, camera, parentMatrix)](#instance-renderwebglrenderer-src-camera-parentmatrix)

Back to top

©2025[Phaser](https://docs.phaser.io)



BitmapText