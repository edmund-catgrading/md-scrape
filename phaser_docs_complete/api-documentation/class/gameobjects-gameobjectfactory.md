# GameObjectFactory

Phaser.GameObjects.GameObjectFactory

The Game Object Factory is a Scene plugin that allows you to quickly create many common

types of Game Objects and have them automatically registered with the Scene.

Game Objects directly register themselves with the Factory and inject their own creation

methods into the class.

**Constructor**

`new GameObjectFactory(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to which this Game Object Factory belongs. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/gameobjects/GameObjectFactory.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L11)  
> Since: 3.0.0

# Public Methods

## arc

### <instance> arc([x], [y], [radius], [startAngle], [endAngle], [anticlockwise], [fillColor], [fillAlpha])

**Description:**

Creates a new Arc Shape Game Object and adds it to the Scene.

Note: This method will only be available if the Arc Game Object has been built into Phaser.

The Arc Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports both fill and stroke colors.

When it renders it displays an arc shape. You can control the start and end angles of the arc,

as well as if the angles are winding clockwise or anti-clockwise. With the default settings

it renders as a complete circle. By changing the angles you can create other arc shapes,

such as half-circles.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| radius | number | Yes | 128 | The radius of the arc. |
| startAngle | number | Yes | 0 | The start angle of the arc, in degrees. |
| endAngle | number | Yes | 360 | The end angle of the arc, in degrees. |
| anticlockwise | boolean | Yes | false | The winding order of the start and end angles. |
| fillColor | number | Yes |  | The color the arc will be filled with, i.e. 0xff0000 for red. |
| fillAlpha | number | Yes |  | The alpha the arc will be filled with. You can also set the alpha of the overall Shape using its `alpha` property. |

**Returns:** [Phaser.GameObjects.Arc](gameobjects-arc.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/arc/ArcFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/arc/ArcFactory.js#L10)  
> Since: 3.13.0

---

## bitmapMask

### <instance> bitmapMask([maskObject], [x], [y], [texture], [frame])

**Description:**

A Bitmap Mask combines the alpha (opacity) of a masked pixel with the alpha of another pixel.

Unlike the Geometry Mask, which is a clipping path, a Bitmap Mask behaves like an alpha mask,

not a clipping path. It is only available when using the WebGL Renderer.

A Bitmap Mask can use any Game Object, or Dynamic Texture, to determine the alpha of each pixel of the masked Game Object(s).

For any given point of a masked Game Object's texture, the pixel's alpha will be multiplied by the alpha

of the pixel at the same position in the Bitmap Mask's Game Object. The color of the pixel from the

Bitmap Mask doesn't matter.

For example, if a pure blue pixel with an alpha of 0.95 is masked with a pure red pixel with an

alpha of 0.5, the resulting pixel will be pure blue with an alpha of 0.475. Naturally, this means

that a pixel in the mask with an alpha of 0 will hide the corresponding pixel in all masked Game Objects

A pixel with an alpha of 1 in the masked Game Object will receive the same alpha as the

corresponding pixel in the mask.

Note: You cannot combine Bitmap Masks and Blend Modes on the same Game Object. You can, however,

combine Geometry Masks and Blend Modes together.

The Bitmap Mask's location matches the location of its Game Object, not the location of the

masked objects. Moving or transforming the underlying Game Object will change the mask

(and affect the visibility of any masked objects), whereas moving or transforming a masked object

will not affect the mask.

The Bitmap Mask will not render its Game Object by itself. If the Game Object is not in a

Scene's display list, it will only be used for the mask and its full texture will not be directly

visible. Adding the underlying Game Object to a Scene will not cause any problems - it will

render as a normal Game Object and will also serve as a mask.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| maskObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | [Phaser.Textures.DynamicTexture](textures-dynamictexture.md) | Yes | The Game Object or Texture that will be used as the mask. If `null` it will generate an Image Game Object using the rest of the arguments. |
| --- | --- | --- | --- |
| x | number | Yes | If creating a Game Object, the horizontal position in the world. |
| y | number | Yes | If creating a Game Object, the vertical position in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | Yes | If creating a Game Object, the key, or instance of the Texture it will use to render with, as stored in the Texture Manager. |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | Yes |

**Returns:** [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) - The Bitmap Mask that was created.

> Source: [src/display/mask/BitmapMask.js#L191](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/mask/BitmapMask.js#L191)  
> Since: 3.60.0

---

## bitmapText

### <instance> bitmapText(x, y, font, [text], [size], [align])

**Description:**

Creates a new Bitmap Text Game Object and adds it to the Scene.

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

Littera (Web-based, free): <http://kvazars.com/littera/>

For most use cases it is recommended to use XML. If you wish to use JSON, the formatting should be equal to the result of

converting a valid XML file through the popular X2JS library. An online tool for conversion can be found here: <http://codebeautify.org/xmltojson>

Note: This method will only be available if the Bitmap Text Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x position of the Game Object. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y position of the Game Object. |
| font | string | No |  | The key of the font to use from the BitmapFont cache. |
| text | string | Array.<string> | Yes |  | The string, or array of strings, to be set as the content of this Bitmap Text. |
| size | number | Yes |  | The font size to set. |
| align | number | Yes | 0 | The alignment of the text in a multi-line BitmapText object. |

**Returns:** [Phaser.GameObjects.BitmapText](gameobjects-bitmaptext.md) - The Game Object that was created.

> Source: [src/gameobjects/bitmaptext/static/BitmapTextFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/static/BitmapTextFactory.js#L10)  
> Since: 3.0.0

---

## blitter

### <instance> blitter(x, y, texture, [frame])

**Description:**

Creates a new Blitter Game Object and adds it to the Scene.

Note: This method will only be available if the Blitter Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the Game Object. |
| --- | --- | --- | --- |
| y | number | No | The y position of the Game Object. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | No | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes | The default Frame children of the Blitter will use. |

**Returns:** [Phaser.GameObjects.Blitter](gameobjects-blitter.md) - The Game Object that was created.

> Source: [src/gameobjects/blitter/BlitterFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/BlitterFactory.js#L10)  
> Since: 3.0.0

---

## circle

### <instance> circle([x], [y], [radius], [fillColor], [fillAlpha])

**Description:**

Creates a new Circle Shape Game Object and adds it to the Scene.

A Circle is an Arc with no defined start and end angle, making it render as a complete circle.

Note: This method will only be available if the Arc Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| radius | number | Yes | 128 | The radius of the circle. |
| fillColor | number | Yes |  | The color the circle will be filled with, i.e. 0xff0000 for red. |
| fillAlpha | number | Yes |  | The alpha the circle will be filled with. You can also set the alpha of the overall Shape using its `alpha` property. |

**Returns:** [Phaser.GameObjects.Arc](gameobjects-arc.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/arc/ArcFactory.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/arc/ArcFactory.js#L46)  
> Since: 3.13.0

---

## container

### <instance> container([x], [y], [children])

**Description:**

Creates a new Container Game Object and adds it to the Scene.

Note: This method will only be available if the Container Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| children | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | Yes |  | An optional array of Game Objects to add to this Container. |

**Returns:** [Phaser.GameObjects.Container](gameobjects-container.md) - The Game Object that was created.

> Source: [src/gameobjects/container/ContainerFactory.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/container/ContainerFactory.js#L11)  
> Since: 3.4.0

---

## curve

### <instance> curve([x], [y], [curve], [fillColor], [fillAlpha])

**Description:**

Creates a new Curve Shape Game Object and adds it to the Scene.

Note: This method will only be available if the Curve Game Object has been built into Phaser.

The Curve Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports both fill and stroke colors.

To render a Curve Shape you must first create a `Phaser.Curves.Curve` object, then pass it to

the Curve Shape in the constructor.

The Curve shape also has a `smoothness` property and corresponding `setSmoothness` method.

This allows you to control how smooth the shape renders in WebGL, by controlling the number of iterations

that take place during construction. Increase and decrease the default value for smoother, or more

jagged, shapes.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| curve | [Phaser.Curves.Curve](curves-curve.md) | Yes |  | The Curve object to use to create the Shape. |
| fillColor | number | Yes |  | The color the curve will be filled with, i.e. 0xff0000 for red. |
| fillAlpha | number | Yes |  | The alpha the curve will be filled with. You can also set the alpha of the overall Shape using its `alpha` property. |

**Returns:** [Phaser.GameObjects.Curve](gameobjects-curve.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/curve/CurveFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/curve/CurveFactory.js#L10)  
> Since: 3.13.0

---

## dom

### <instance> dom(x, y, [element], [style], [innerText])

**Description:**

DOM Element Game Objects are a way to control and manipulate HTML Elements over the top of your game.

In order for DOM Elements to display you have to enable them by adding the following to your game

configuration object:

```
Copy
dom {

  createContainer: true

}


```

When this is added, Phaser will automatically create a DOM Container div that is positioned over the top

of the game canvas. This div is sized to match the canvas, and if the canvas size changes, as a result of

settings within the Scale Manager, the dom container is resized accordingly.

You can create a DOM Element by either passing in DOMStrings, or by passing in a reference to an existing

Element that you wish to be placed under the control of Phaser. For example:

```
Copy
this.add.dom(x, y, 'div', 'background-color: lime; width: 220px; height: 100px; font: 48px Arial', 'Phaser');


```

The above code will insert a div element into the DOM Container at the given x/y coordinate. The DOMString in

the 4th argument sets the initial CSS style of the div and the final argument is the inner text. In this case,

it will create a lime colored div that is 220px by 100px in size with the text Phaser in it, in an Arial font.

You should nearly always, without exception, use explicitly sized HTML Elements, in order to fully control

alignment and positioning of the elements next to regular game content.

Rather than specify the CSS and HTML directly you can use the `load.html` File Loader to load it into the

cache and then use the `createFromCache` method instead. You can also use `createFromHTML` and various other

methods available in this class to help construct your elements.

Once the element has been created you can then control it like you would any other Game Object. You can set its

position, scale, rotation, alpha and other properties. It will move as the main Scene Camera moves and be clipped

at the edge of the canvas. It's important to remember some limitations of DOM Elements: The obvious one is that

they appear above or below your game canvas. You cannot blend them into the display list, meaning you cannot have

a DOM Element, then a Sprite, then another DOM Element behind it.

They also cannot be enabled for input. To do that, you have to use the `addListener` method to add native event

listeners directly. The final limitation is to do with cameras. The DOM Container is sized to match the game canvas

entirely and clipped accordingly. DOM Elements respect camera scrolling and scrollFactor settings, but if you

change the size of the camera so it no longer matches the size of the canvas, they won't be clipped accordingly.

Also, all DOM Elements are inserted into the same DOM Container, regardless of which Scene they are created in.

DOM Elements are a powerful way to align native HTML with your Phaser Game Objects. For example, you can insert

a login form for a multiplayer game directly into your title screen. Or a text input box for a highscore table.

Or a banner ad from a 3rd party service. Or perhaps you'd like to use them for high resolution text display and

UI. The choice is up to you, just remember that you're dealing with standard HTML and CSS floating over the top

of your game, and should treat it accordingly.

Note: This method will only be available if the DOM Element Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this DOM Element in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this DOM Element in the world. |
| element | HTMLElement | string | Yes | An existing DOM element, or a string. If a string starting with a # it will do a `getElementById` look-up on the string (minus the hash). Without a hash, it represents the type of element to create, i.e. 'div'. |
| style | string | any | Yes | If a string, will be set directly as the elements `style` property value. If a plain object, will be iterated and the values transferred. In both cases the values replacing whatever CSS styles may have been previously set. |
| innerText | string | Yes | If given, will be set directly as the elements `innerText` property value, replacing whatever was there before. |

**Returns:** [Phaser.GameObjects.DOMElement](gameobjects-domelement.md) - The Game Object that was created.

> Source: [src/gameobjects/domelement/DOMElementFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/domelement/DOMElementFactory.js#L10)  
> Since: 3.17.0

---

## dynamicBitmapText

### <instance> dynamicBitmapText(x, y, font, [text], [size])

**Description:**

Creates a new Dynamic Bitmap Text Game Object and adds it to the Scene.

BitmapText objects work by taking a texture file and an XML or JSON file that describes the font structure.

During rendering for each letter of the text is rendered to the display, proportionally spaced out and aligned to

match the font structure.

Dynamic Bitmap Text objects are different from Static Bitmap Text in that they invoke a callback for each

letter being rendered during the render pass. This callback allows you to manipulate the properties of

each letter being rendered, such as its position, scale or tint, allowing you to create interesting effects

like jiggling text, which can't be done with Static text. This means that Dynamic Text takes more processing

time, so only use them if you require the callback ability they have.

BitmapText objects are less flexible than Text objects, in that they have less features such as shadows, fills and the ability

to use Web Fonts, however you trade this flexibility for rendering speed. You can also create visually compelling BitmapTexts by

processing the font texture in an image editor, applying fills and any other effects required.

To create multi-line text insert \r, \n or \r\n escape codes into the text string.

To create a BitmapText data files you need a 3rd party app such as:

BMFont (Windows, free): <http://www.angelcode.com/products/bmfont/>

Glyph Designer (OS X, commercial): <http://www.71squared.com/en/glyphdesigner>

Littera (Web-based, free): <http://kvazars.com/littera/>

For most use cases it is recommended to use XML. If you wish to use JSON, the formatting should be equal to the result of

converting a valid XML file through the popular X2JS library. An online tool for conversion can be found here: <http://codebeautify.org/xmltojson>

Note: This method will only be available if the Dynamic Bitmap Text Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the Game Object. |
| --- | --- | --- | --- |
| y | number | No | The y position of the Game Object. |
| font | string | No | The key of the font to use from the BitmapFont cache. |
| text | string | Array.<string> | Yes | The string, or array of strings, to be set as the content of this Bitmap Text. |
| size | number | Yes | The font size to set. |

**Returns:** [Phaser.GameObjects.DynamicBitmapText](gameobjects-dynamicbitmaptext.md) - The Game Object that was created.

> Source: [src/gameobjects/bitmaptext/dynamic/DynamicBitmapTextFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapTextFactory.js#L10)  
> Since: 3.0.0

---

## ellipse

### <instance> ellipse([x], [y], [width], [height], [fillColor], [fillAlpha])

**Description:**

Creates a new Ellipse Shape Game Object and adds it to the Scene.

Note: This method will only be available if the Ellipse Game Object has been built into Phaser.

The Ellipse Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports both fill and stroke colors.

When it renders it displays an ellipse shape. You can control the width and height of the ellipse.

If the width and height match it will render as a circle. If the width is less than the height,

it will look more like an egg shape.

The Ellipse shape also has a `smoothness` property and corresponding `setSmoothness` method.

This allows you to control how smooth the shape renders in WebGL, by controlling the number of iterations

that take place during construction. Increase and decrease the default value for smoother, or more

jagged, shapes.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| width | number | Yes | 128 | The width of the ellipse. An ellipse with equal width and height renders as a circle. |
| height | number | Yes | 128 | The height of the ellipse. An ellipse with equal width and height renders as a circle. |
| fillColor | number | Yes |  | The color the ellipse will be filled with, i.e. 0xff0000 for red. |
| fillAlpha | number | Yes |  | The alpha the ellipse will be filled with. You can also set the alpha of the overall Shape using its `alpha` property. |

**Returns:** [Phaser.GameObjects.Ellipse](gameobjects-ellipse.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/ellipse/EllipseFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/ellipse/EllipseFactory.js#L10)  
> Since: 3.13.0

---

## existing

### <instance> existing(child)

**Description:**

Adds an existing Game Object to this Scene.

If the Game Object renders, it will be added to the Display List.

If it has a `preUpdate` method, it will be added to the Update List.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | [Phaser.GameObjects.Group](gameobjects-group.md) | [Phaser.GameObjects.Layer](gameobjects-layer.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) - The Game Object that was added.

> Source: [src/gameobjects/GameObjectFactory.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L116)  
> Since: 3.0.0

---

## extern

### <instance> extern()

**Description:**

Creates a new Extern Game Object and adds it to the Scene.

Note: This method will only be available if the Extern Game Object has been built into Phaser.

**Returns:** [Phaser.GameObjects.Extern](gameobjects-extern.md) - The Game Object that was created.

> Source: [src/gameobjects/extern/ExternFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/extern/ExternFactory.js#L10)  
> Since: 3.16.0

---

## follower

### <instance> follower(path, x, y, texture, [frame])

**Description:**

Creates a new PathFollower Game Object and adds it to the Scene.

Note: This method will only be available if the PathFollower Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| path | [Phaser.Curves.Path](curves-path.md) | No | The Path this PathFollower is connected to. |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| y | number | No | The vertical position of this Game Object in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | No | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes | An optional frame from the Texture this Game Object is rendering with. |

**Returns:** [Phaser.GameObjects.PathFollower](gameobjects-pathfollower.md) - The Game Object that was created.

> Source: [src/gameobjects/pathfollower/PathFollowerFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/pathfollower/PathFollowerFactory.js#L10)  
> Since: 3.0.0

---

## graphics

### <instance> graphics([config])

**Description:**

Creates a new Graphics Game Object and adds it to the Scene.

Note: This method will only be available if the Graphics Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.GameObjects.Graphics.Options](../typedef/types-gameobjects-graphics.md) | Yes | The Graphics configuration. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - The Game Object that was created.

> Source: [src/gameobjects/graphics/GraphicsFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/GraphicsFactory.js#L10)  
> Since: 3.0.0

---

## grid

### <instance> grid([x], [y], [width], [height], [cellWidth], [cellHeight], [fillColor], [fillAlpha], [outlineFillColor], [outlineFillAlpha])

**Description:**

Creates a new Grid Shape Game Object and adds it to the Scene.

Note: This method will only be available if the Grid Game Object has been built into Phaser.

The Grid Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports only fill colors and cannot be stroked.

A Grid Shape allows you to display a grid in your game, where you can control the size of the

grid as well as the width and height of the grid cells. You can set a fill color for each grid

cell as well as an alternate fill color. When the alternate fill color is set then the grid

cells will alternate the fill colors as they render, creating a chess-board effect. You can

also optionally have an outline fill color. If set, this draws lines between the grid cells

in the given color. If you specify an outline color with an alpha of zero, then it will draw

the cells spaced out, but without the lines between them.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| width | number | Yes | 128 | The width of the grid. |
| height | number | Yes | 128 | The height of the grid. |
| cellWidth | number | Yes | 32 | The width of one cell in the grid. |
| cellHeight | number | Yes | 32 | The height of one cell in the grid. |
| fillColor | number | Yes |  | The color the grid cells will be filled with, i.e. 0xff0000 for red. |
| fillAlpha | number | Yes |  | The alpha the grid cells will be filled with. You can also set the alpha of the overall Shape using its `alpha` property. |
| outlineFillColor | number | Yes |  | The color of the lines between the grid cells. |
| outlineFillAlpha | number | Yes |  | The alpha of the lines between the grid cells. |

**Returns:** [Phaser.GameObjects.Grid](gameobjects-grid.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/grid/GridFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/grid/GridFactory.js#L10)  
> Since: 3.13.0

---

## group

### <instance> group([children], [config])

**Description:**

Creates a new Group Game Object and adds it to the Scene.

Note: This method will only be available if the Group Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| children | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | [Phaser.Types.GameObjects.Group.GroupConfig](../typedef/types-gameobjects-group.md) | Array.<[Phaser.Types.GameObjects.Group.GroupConfig](../typedef/types-gameobjects-group.md)> | [Phaser.Types.GameObjects.Group.GroupCreateConfig](../typedef/types-gameobjects-group.md) |
| --- | --- | --- | --- |
| config | [Phaser.Types.GameObjects.Group.GroupConfig](../typedef/types-gameobjects-group.md) | [Phaser.Types.GameObjects.Group.GroupCreateConfig](../typedef/types-gameobjects-group.md) | Yes | A Group Configuration object. |

**Returns:** [Phaser.GameObjects.Group](gameobjects-group.md) - The Game Object that was created.

> Source: [src/gameobjects/group/GroupFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/GroupFactory.js#L10)  
> Since: 3.0.0

---

## image

### <instance> image(x, y, texture, [frame])

**Description:**

Creates a new Image Game Object and adds it to the Scene.

Note: This method will only be available if the Image Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this Game Object in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | No | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes | An optional frame from the Texture this Game Object is rendering with. |

**Returns:** [Phaser.GameObjects.Image](gameobjects-image.md) - The Game Object that was created.

> Source: [src/gameobjects/image/ImageFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/image/ImageFactory.js#L10)  
> Since: 3.0.0

---

## isobox

### <instance> isobox([x], [y], [size], [height], [fillTop], [fillLeft], [fillRight])

**Description:**

Creates a new IsoBox Shape Game Object and adds it to the Scene.

Note: This method will only be available if the IsoBox Game Object has been built into Phaser.

The IsoBox Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports only fill colors and cannot be stroked.

An IsoBox is an 'isometric' rectangle. Each face of it has a different fill color. You can set

the color of the top, left and right faces of the rectangle respectively. You can also choose

which of the faces are rendered via the `showTop`, `showLeft` and `showRight` properties.

You cannot view an IsoBox from under-neath, however you can change the 'angle' by setting

the `projection` property.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| size | number | Yes | 48 | The width of the iso box in pixels. The left and right faces will be exactly half this value. |
| height | number | Yes | 32 | The height of the iso box. The left and right faces will be this tall. The overall height of the isobox will be this value plus half the `size` value. |
| fillTop | number | Yes | "0xeeeeee" | The fill color of the top face of the iso box. |
| fillLeft | number | Yes | "0x999999" | The fill color of the left face of the iso box. |
| fillRight | number | Yes | "0xcccccc" | The fill color of the right face of the iso box. |

**Returns:** [Phaser.GameObjects.IsoBox](gameobjects-isobox.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/isobox/IsoBoxFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/isobox/IsoBoxFactory.js#L10)  
> Since: 3.13.0

---

## isotriangle

### <instance> isotriangle([x], [y], [size], [height], [reversed], [fillTop], [fillLeft], [fillRight])

**Description:**

Creates a new IsoTriangle Shape Game Object and adds it to the Scene.

Note: This method will only be available if the IsoTriangle Game Object has been built into Phaser.

The IsoTriangle Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports only fill colors and cannot be stroked.

An IsoTriangle is an 'isometric' triangle. Think of it like a pyramid. Each face has a different

fill color. You can set the color of the top, left and right faces of the triangle respectively

You can also choose which of the faces are rendered via the `showTop`, `showLeft` and `showRight` properties.

You cannot view an IsoTriangle from under-neath, however you can change the 'angle' by setting

the `projection` property. The `reversed` property controls if the IsoTriangle is rendered upside

down or not.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| size | number | Yes | 48 | The width of the iso triangle in pixels. The left and right faces will be exactly half this value. |
| height | number | Yes | 32 | The height of the iso triangle. The left and right faces will be this tall. The overall height of the iso triangle will be this value plus half the `size` value. |
| reversed | boolean | Yes | false | Is the iso triangle upside down? |
| fillTop | number | Yes | "0xeeeeee" | The fill color of the top face of the iso triangle. |
| fillLeft | number | Yes | "0x999999" | The fill color of the left face of the iso triangle. |
| fillRight | number | Yes | "0xcccccc" | The fill color of the right face of the iso triangle. |

**Returns:** [Phaser.GameObjects.IsoTriangle](gameobjects-isotriangle.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/isotriangle/IsoTriangleFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/isotriangle/IsoTriangleFactory.js#L10)  
> Since: 3.13.0

---

## layer

### <instance> layer([children])

**Description:**

Creates a new Layer Game Object and adds it to the Scene.

Note: This method will only be available if the Layer Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| children | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | Yes | An optional array of Game Objects to add to this Layer. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Layer](gameobjects-layer.md) - The Game Object that was created.

> Source: [src/gameobjects/layer/LayerFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/layer/LayerFactory.js#L10)  
> Since: 3.50.0

---

## line

### <instance> line([x], [y], [x1], [y1], [x2], [y2], [strokeColor], [strokeAlpha])

**Description:**

Creates a new Line Shape Game Object and adds it to the Scene.

Note: This method will only be available if the Line Game Object has been built into Phaser.

The Line Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports only stroke colors and cannot be filled.

A Line Shape allows you to draw a line between two points in your game. You can control the

stroke color and thickness of the line. In WebGL only you can also specify a different

thickness for the start and end of the line, allowing you to render lines that taper-off.

If you need to draw multiple lines in a sequence you may wish to use the Polygon Shape instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| x1 | number | Yes | 0 | The horizontal position of the start of the line. |
| y1 | number | Yes | 0 | The vertical position of the start of the line. |
| x2 | number | Yes | 128 | The horizontal position of the end of the line. |
| y2 | number | Yes | 0 | The vertical position of the end of the line. |
| strokeColor | number | Yes |  | The color the line will be drawn in, i.e. 0xff0000 for red. |
| strokeAlpha | number | Yes |  | The alpha the line will be drawn in. You can also set the alpha of the overall Shape using its `alpha` property. |

**Returns:** [Phaser.GameObjects.Line](gameobjects-line.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/line/LineFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/line/LineFactory.js#L10)  
> Since: 3.13.0

---

## mesh

### <instance> mesh([x], [y], [texture], [frame], [vertices], [uvs], [indicies], [containsZ], [normals], [colors], [alphas])

**Description:**

Creates a new Mesh Game Object and adds it to the Scene.

Note: This method will only be available if the Mesh Game Object and WebGL support have been built into Phaser.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes |  | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes |  | The vertical position of this Game Object in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | Yes |  | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes |  | An optional frame from the Texture this Game Object is rendering with. |
| vertices | Array.<number> | Yes |  | The vertices array. Either `xy` pairs, or `xyz` if the `containsZ` parameter is `true`. |
| uvs | Array.<number> | Yes |  | The UVs pairs array. |
| indicies | Array.<number> | Yes |  | Optional vertex indicies array. If you don't have one, pass `null` or an empty array. |
| containsZ | boolean | Yes | false | Does the vertices data include a `z` component? |
| normals | Array.<number> | Yes |  | Optional vertex normals array. If you don't have one, pass `null` or an empty array. |
| colors | number | Array.<number> | Yes | "0xffffff" | An array of colors, one per vertex, or a single color value applied to all vertices. |
| alphas | number | Array.<number> | Yes | 1 | An array of alpha values, one per vertex, or a single alpha value applied to all vertices. |

**Returns:** [Phaser.GameObjects.Mesh](gameobjects-mesh.md) - The Game Object that was created.

> Source: [src/gameobjects/mesh/MeshFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/mesh/MeshFactory.js#L10)  
> Since: 3.0.0

---

## nineslice

### <instance> nineslice(x, y, texture, [frame], [width], [height], [leftWidth], [rightWidth], [topHeight], [bottomHeight])

**Description:**

A Nine Slice Game Object allows you to display a texture-based object that

can be stretched both horizontally and vertically, but that retains

fixed-sized corners. The dimensions of the corners are set via the

parameters to this class.

This is extremely useful for UI and button like elements, where you need

them to expand to accommodate the content without distorting the texture.

The texture you provide for this Game Object should be based on the

following layout structure:

```
Copy
     A                          B

   +---+----------------------+---+

 C | 1 |          2           | 3 |

   +---+----------------------+---+

   |   |                      |   |

   | 4 |          5           | 6 |

   |   |                      |   |

   +---+----------------------+---+

 D | 7 |          8           | 9 |

   +---+----------------------+---+


```

When changing this objects width and / or height:

```
Copyareas 1, 3, 7 and 9 (the corners) will remain unscaled

areas 2 and 8 will be stretched horizontally only

areas 4 and 6 will be stretched vertically only

area 5 will be stretched both horizontally and vertically

```

You can also create a 3 slice Game Object:

This works in a similar way, except you can only stretch it horizontally.

Therefore, it requires less configuration:

```
Copy
     A                          B

   +---+----------------------+---+

   |   |                      |   |

 C | 1 |          2           | 3 |

   |   |                      |   |

   +---+----------------------+---+


```

When changing this objects width (you cannot change its height)

```
Copyareas 1 and 3 will remain unscaled

area 2 will be stretched horizontally

```

The above configuration concept is adapted from the Pixi NineSlicePlane.

To specify a 3 slice object instead of a 9 slice you should only

provide the `leftWidth` and `rightWidth` parameters. To create a 9 slice

you must supply all parameters.

The *minimum* width this Game Object can be is the total of

`leftWidth` + `rightWidth`. The *minimum* height this Game Object

can be is the total of `topHeight` + `bottomHeight`.

If you need to display this object at a smaller size, you can scale it.

In terms of performance, using a 3 slice Game Object is the equivalent of

having 3 Sprites in a row. Using a 9 slice Game Object is the equivalent

of having 9 Sprites in a row. The vertices of this object are all batched

together and can co-exist with other Sprites and graphics on the display

list, without incurring any additional overhead.

As of Phaser 3.60 this Game Object is WebGL only.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal position of the center of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The vertical position of the center of this Game Object in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | No |  | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes |  | An optional frame from the Texture this Game Object is rendering with. |
| width | number | Yes | 256 | The width of the Nine Slice Game Object. You can adjust the width post-creation. |
| height | number | Yes | 256 | The height of the Nine Slice Game Object. If this is a 3 slice object the height will be fixed to the height of the texture and cannot be changed. |
| leftWidth | number | Yes | 10 | The size of the left vertical column (A). |
| rightWidth | number | Yes | 10 | The size of the right vertical column (B). |
| topHeight | number | Yes | 0 | The size of the top horiztonal row (C). Set to zero or undefined to create a 3 slice object. |
| bottomHeight | number | Yes | 0 | The size of the bottom horiztonal row (D). Set to zero or undefined to create a 3 slice object. |

**Returns:** [Phaser.GameObjects.NineSlice](gameobjects-nineslice.md) - The Game Object that was created.

> Source: [src/gameobjects/nineslice/NineSliceFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/nineslice/NineSliceFactory.js#L10)  
> Since: 3.60.0

---

## particles

### <instance> particles([x], [y], [texture], [config])

**Description:**

Creates a new Particle Emitter Game Object and adds it to the Scene.

If you wish to configure the Emitter after creating it, use the `ParticleEmitter.setConfig` method.

Prior to Phaser v3.60 this function would create a `ParticleEmitterManager`. These were removed

in v3.60 and replaced with creating a `ParticleEmitter` instance directly. Please see the

updated function parameters and class documentation for more details.

Note: This method will only be available if the Particles Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | Yes | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- |
| y | number | Yes | The vertical position of this Game Object in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | Yes | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](../typedef/types-gameobjects-particles.md) | Yes | Configuration settings for the Particle Emitter. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - The Game Object that was created.

> Source: [src/gameobjects/particles/ParticleEmitterFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitterFactory.js#L10)  
> Since: 3.60.0

---

## path

### <instance> path(x, y)

**Description:**

Creates a new Path Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Path. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this Path. |

**Returns:** [Phaser.Curves.Path](curves-path.md) - The Path Object that was created.

> Source: [src/curves/path/Path.js#L907](https://github.com/phaserjs/phaser/blob/v3.87.0/src/curves/path/Path.js#L907)  
> Since: 3.0.0

---

## plane

### <instance> plane([x], [y], [texture], [frame], [width], [height], [tile])

**Description:**

Creates a new Plane Game Object and adds it to the Scene.

Note: This method will only be available if the Plane Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes |  | The horizontal position of this Plane in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes |  | The vertical position of this Plane in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | Yes |  | The key, or instance of the Texture this Plane will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes |  | An optional frame from the Texture this Plane is rendering with. |
| width | number | Yes | 8 | The width of this Plane, in cells, not pixels. |
| height | number | Yes | 8 | The height of this Plane, in cells, not pixels. |
| tile | boolean | Yes | false | Is the texture tiled? I.e. repeated across each cell. |

**Returns:** [Phaser.GameObjects.Plane](gameobjects-plane.md) - The Plane Game Object that was created.

> Source: [src/gameobjects/plane/PlaneFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/plane/PlaneFactory.js#L10)  
> Since: 3.60.0

---

## pointlight

### <instance> pointlight(x, y, [color], [radius], [intensity], [attenuation])

**Description:**

Creates a new Point Light Game Object and adds it to the Scene.

Note: This method will only be available if the Point Light Game Object has been built into Phaser.

The Point Light Game Object provides a way to add a point light effect into your game,

without the expensive shader processing requirements of the traditional Light Game Object.

The difference is that the Point Light renders using a custom shader, designed to give the

impression of a point light source, of variable radius, intensity and color, in your game.

However, unlike the Light Game Object, it does not impact any other Game Objects, or use their

normal maps for calcuations. This makes them extremely fast to render compared to Lights

and perfect for special effects, such as flickering torches or muzzle flashes.

For maximum performance you should batch Point Light Game Objects together. This means

ensuring they follow each other consecutively on the display list. Ideally, use a Layer

Game Object and then add just Point Lights to it, so that it can batch together the rendering

of the lights. You don't *have* to do this, and if you've only a handful of Point Lights in

your game then it's perfectly safe to mix them into the dislay list as normal. However, if

you're using a large number of them, please consider how they are mixed into the display list.

The renderer will automatically cull Point Lights. Those with a radius that does not intersect

with the Camera will be skipped in the rendering list. This happens automatically and the

culled state is refreshed every frame, for every camera.

The origin of a Point Light is always 0.5 and it cannot be changed.

Point Lights are a WebGL only feature and do not have a Canvas counterpart.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal position of this Point Light in the world. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The vertical position of this Point Light in the world. |
| color | number | Yes | "0xffffff" | The color of the Point Light, given as a hex value. |
| radius | number | Yes | 128 | The radius of the Point Light. |
| intensity | number | Yes | 1 | The intensity, or color blend, of the Point Light. |
| attenuation | number | Yes | 0.1 | The attenuation of the Point Light. This is the reduction of light from the center point. |

**Returns:** [Phaser.GameObjects.PointLight](gameobjects-pointlight.md) - The Game Object that was created.

> Source: [src/gameobjects/pointlight/PointLightFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/pointlight/PointLightFactory.js#L10)  
> Since: 3.50.0

---

## polygon

### <instance> polygon([x], [y], [points], [fillColor], [fillAlpha])

**Description:**

Creates a new Polygon Shape Game Object and adds it to the Scene.

Note: This method will only be available if the Polygon Game Object has been built into Phaser.

The Polygon Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports both fill and stroke colors.

The Polygon Shape is created by providing a list of points, which are then used to create an

internal Polygon geometry object. The points can be set from a variety of formats:

* An array of Point or Vector2 objects: `[new Phaser.Math.Vector2(x1, y1), ...]`
* An array of objects with public x/y properties: `[obj1, obj2, ...]`
* An array of paired numbers that represent point coordinates: `[x1,y1, x2,y2, ...]`
* An array of arrays with two elements representing x/y coordinates: `[[x1, y1], [x2, y2], ...]`

By default the `x` and `y` coordinates of this Shape refer to the center of it. However, depending

on the coordinates of the points provided, the final shape may be rendered offset from its origin.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| points | any | Yes |  | The points that make up the polygon. |
| fillColor | number | Yes |  | The color the polygon will be filled with, i.e. 0xff0000 for red. |
| fillAlpha | number | Yes |  | The alpha the polygon will be filled with. You can also set the alpha of the overall Shape using its `alpha` property. |

**Returns:** [Phaser.GameObjects.Polygon](gameobjects-polygon.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/polygon/PolygonFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/polygon/PolygonFactory.js#L10)  
> Since: 3.13.0

---

## rectangle

### <instance> rectangle([x], [y], [width], [height], [fillColor], [fillAlpha])

**Description:**

Creates a new Rectangle Shape Game Object and adds it to the Scene.

Note: This method will only be available if the Rectangle Game Object has been built into Phaser.

The Rectangle Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports both fill and stroke colors.

You can change the size of the rectangle by changing the `width` and `height` properties.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| width | number | Yes | 128 | The width of the rectangle. |
| height | number | Yes | 128 | The height of the rectangle. |
| fillColor | number | Yes |  | The color the rectangle will be filled with, i.e. 0xff0000 for red. |
| fillAlpha | number | Yes |  | The alpha the rectangle will be filled with. You can also set the alpha of the overall Shape using its `alpha` property. |

**Returns:** [Phaser.GameObjects.Rectangle](gameobjects-rectangle.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/rectangle/RectangleFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/rectangle/RectangleFactory.js#L10)  
> Since: 3.13.0

---

## register

### <static> register(factoryType, factoryFunction)

**Description:**

Static method called directly by the Game Object factory functions.

With this method you can register a custom GameObject factory in the GameObjectFactory,

providing a name (`factoryType`) and the constructor (`factoryFunction`) in order

to be called when you call to Phaser.Scene.add[ factoryType ] method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| factoryType | string | No | The key of the factory that you will use to call to Phaser.Scene.add[ factoryType ] method. |
| --- | --- | --- | --- |
| factoryFunction | function | No | The constructor function to be called when you invoke to the Phaser.Scene.add method. |

> Source: [src/gameobjects/GameObjectFactory.js#L185](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L185)  
> Since: 3.0.0

---

## remove

### <static> remove(factoryType)

**Description:**

Static method called directly by the Game Object factory functions.

With this method you can remove a custom GameObject factory registered in the GameObjectFactory,

providing a its `factoryType`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| factoryType | string | No | The key of the factory that you want to remove from the GameObjectFactory. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/GameObjectFactory.js#L206](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L206)  
> Since: 3.0.0

---

## renderTexture

### <instance> renderTexture(x, y, [width], [height])

**Description:**

Creates a new Render Texture Game Object and adds it to the Scene.

Note: This method will only be available if the Render Texture Game Object has been built into Phaser.

A Render Texture is a combination of Dynamic Texture and an Image Game Object, that uses the

Dynamic Texture to display itself with.

A Dynamic Texture is a special texture that allows you to draw textures, frames and most kind of

Game Objects directly to it.

You can take many complex objects and draw them to this one texture, which can then be used as the

base texture for other Game Objects, such as Sprites. Should you then update this texture, all

Game Objects using it will instantly be updated as well, reflecting the changes immediately.

It's a powerful way to generate dynamic textures at run-time that are WebGL friendly and don't invoke

expensive GPU uploads on each change.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The vertical position of this Game Object in the world. |
| width | number | Yes | 32 | The width of the Render Texture. |
| height | number | Yes | 32 | The height of the Render Texture. |

**Returns:** [Phaser.GameObjects.RenderTexture](gameobjects-rendertexture.md) - The Game Object that was created.

> Source: [src/gameobjects/rendertexture/RenderTextureFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/rendertexture/RenderTextureFactory.js#L10)  
> Since: 3.2.0

---

## rope

### <instance> rope(x, y, texture, [frame], [points], [horizontal], [colors], [alphas])

**Description:**

Creates a new Rope Game Object and adds it to the Scene.

Note: This method will only be available if the Rope Game Object and WebGL support have been built into Phaser.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The vertical position of this Game Object in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | No |  | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes |  | An optional frame from the Texture this Game Object is rendering with. |
| points | Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> | Yes |  | An array containing the vertices data for this Rope. If none is provided a simple quad is created. See `setPoints` to set this post-creation. |
| horizontal | boolean | Yes | true | Should the vertices of this Rope be aligned horizontally (`true`), or vertically (`false`)? |
| colors | Array.<number> | Yes |  | An optional array containing the color data for this Rope. You should provide one color value per pair of vertices. |
| alphas | Array.<number> | Yes |  | An optional array containing the alpha data for this Rope. You should provide one alpha value per pair of vertices. |

**Returns:** [Phaser.GameObjects.Rope](gameobjects-rope.md) - The Game Object that was created.

> Source: [src/gameobjects/rope/RopeFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/rope/RopeFactory.js#L10)  
> Since: 3.23.0

---

## shader

### <instance> shader(key, [x], [y], [width], [height], [textures], [textureData])

**Description:**

Creates a new Shader Game Object and adds it to the Scene.

Note: This method will only be available if the Shader Game Object and WebGL support have been built into Phaser.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Display.BaseShader](display-baseshader.md) | No |  | The key of the shader to use from the shader cache, or a BaseShader instance. |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| width | number | Yes | 128 | The width of the Game Object. |
| height | number | Yes | 128 | The height of the Game Object. |
| textures | Array.<string> | Yes |  | Optional array of texture keys to bind to the iChannel0...3 uniforms. The textures must already exist in the Texture Manager. |
| textureData | object | Yes |  | Optional additional texture data. |

**Returns:** [Phaser.GameObjects.Shader](gameobjects-shader.md) - The Game Object that was created.

> Source: [src/gameobjects/shader/ShaderFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shader/ShaderFactory.js#L10)  
> Since: 3.17.0

---

## sprite

### <instance> sprite(x, y, texture, [frame])

**Description:**

Creates a new Sprite Game Object and adds it to the Scene.

Note: This method will only be available if the Sprite Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this Game Object in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | No | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes | An optional frame from the Texture this Game Object is rendering with. |

**Returns:** [Phaser.GameObjects.Sprite](gameobjects-sprite.md) - The Game Object that was created.

> Source: [src/gameobjects/sprite/SpriteFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/sprite/SpriteFactory.js#L10)  
> Since: 3.0.0

---

## star

### <instance> star([x], [y], [points], [innerRadius], [outerRadius], [fillColor], [fillAlpha])

**Description:**

Creates a new Star Shape Game Object and adds it to the Scene.

Note: This method will only be available if the Star Game Object has been built into Phaser.

The Star Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports both fill and stroke colors.

As the name implies, the Star shape will display a star in your game. You can control several

aspects of it including the number of points that constitute the star. The default is 5. If

you change it to 4 it will render as a diamond. If you increase them, you'll get a more spiky

star shape.

You can also control the inner and outer radius, which is how 'long' each point of the star is.

Modify these values to create more interesting shapes.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| points | number | Yes | 5 | The number of points on the star. |
| innerRadius | number | Yes | 32 | The inner radius of the star. |
| outerRadius | number | Yes | 64 | The outer radius of the star. |
| fillColor | number | Yes |  | The color the star will be filled with, i.e. 0xff0000 for red. |
| fillAlpha | number | Yes |  | The alpha the star will be filled with. You can also set the alpha of the overall Shape using its `alpha` property. |

**Returns:** [Phaser.GameObjects.Star](gameobjects-star.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/star/StarFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/star/StarFactory.js#L10)  
> Since: 3.13.0

---

## text

### <instance> text(x, y, text, [style])

**Description:**

Creates a new Text Game Object and adds it to the Scene.

A Text Game Object.

Text objects work by creating their own internal hidden Canvas and then renders text to it using

the standard Canvas `fillText` API. It then creates a texture from this canvas which is rendered

to your game during the render pass.

Because it uses the Canvas API you can take advantage of all the features this offers, such as

applying gradient fills to the text, or strokes, shadows and more. You can also use custom fonts

loaded externally, such as Google or TypeKit Web fonts.

You can only display fonts that are currently loaded and available to the browser: therefore fonts must

be pre-loaded. Phaser does not do this for you, so you will require the use of a 3rd party font loader,

or have the fonts ready available in the CSS on the page in which your Phaser game resides.

See [this](http://www.jordanm.co.uk/tinytype) for the available default fonts

across mobile browsers.

A note on performance: Every time the contents of a Text object changes, i.e. changing the text being

displayed, or the style of the text, it needs to remake the Text canvas, and if on WebGL, re-upload the

new texture to the GPU. This can be an expensive operation if used often, or with large quantities of

Text objects in your game. If you run into performance issues you would be better off using Bitmap Text

instead, as it benefits from batching and avoids expensive Canvas API calls.

Note: This method will only be available if the Text Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this Game Object in the world. |
| text | string | Array.<string> | No | The text this Text object will display. |
| style | [Phaser.Types.GameObjects.Text.TextStyle](../typedef/types-gameobjects-text.md) | Yes | The Text style configuration object. |

**Returns:** [Phaser.GameObjects.Text](gameobjects-text.md) - The Game Object that was created.

> Source: [src/gameobjects/text/TextFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/text/TextFactory.js#L10)  
> Since: 3.0.0

---

## tilemap

### <instance> tilemap([key], [tileWidth], [tileHeight], [width], [height], [data], [insertNull])

**Description:**

Creates a Tilemap from the given key or data, or creates a blank Tilemap if no key/data provided.

When loading from CSV or a 2D array, you should specify the tileWidth & tileHeight. When parsing

from a map from Tiled, the tileWidth, tileHeight, width & height will be pulled from the map

data. For an empty map, you should specify tileWidth, tileHeight, width & height.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | Yes |  | The key in the Phaser cache that corresponds to the loaded tilemap data. |
| --- | --- | --- | --- | --- |
| tileWidth | number | Yes | 32 | The width of a tile in pixels. Pass in `null` to leave as the default. |
| tileHeight | number | Yes | 32 | The height of a tile in pixels. Pass in `null` to leave as the default. |
| width | number | Yes | 10 | The width of the map in tiles. Pass in `null` to leave as the default. |
| height | number | Yes | 10 | The height of the map in tiles. Pass in `null` to leave as the default. |
| data | Array.<Array.<number>> | Yes |  | Instead of loading from the cache, you can also load directly from a 2D array of tile indexes. Pass in `null` for no data. |
| insertNull | boolean | Yes | false | Controls how empty tiles, tiles with an index of -1, in the map data are handled. If `true`, empty locations will get a value of `null`. If `false`, empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to `true` will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set. |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - undefined

> Source: [src/tilemaps/TilemapFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/TilemapFactory.js#L10)  
> Since: 3.0.0

---

## tileSprite

### <instance> tileSprite(x, y, width, height, texture, [frame])

**Description:**

Creates a new TileSprite Game Object and adds it to the Scene.

Note: This method will only be available if the TileSprite Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this Game Object in the world. |
| width | number | No | The width of the Game Object. If zero it will use the size of the texture frame. |
| height | number | No | The height of the Game Object. If zero it will use the size of the texture frame. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | No | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. Cannot be a DynamicTexture. |
| frame | string | number | Yes | An optional frame from the Texture this Game Object is rendering with. |

**Returns:** [Phaser.GameObjects.TileSprite](gameobjects-tilesprite.md) - The Game Object that was created.

> Source: [src/gameobjects/tilesprite/TileSpriteFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/tilesprite/TileSpriteFactory.js#L10)  
> Since: 3.0.0

---

## timeline

### <instance> timeline(config)

**Description:**

A Timeline is a way to schedule events to happen at specific times in the future.

You can think of it as an event sequencer for your game, allowing you to schedule the

running of callbacks, events and other actions at specific times in the future.

A Timeline is a Scene level system, meaning you can have as many Timelines as you like, each

belonging to a different Scene. You can also have multiple Timelines running at the same time.

If the Scene is paused, the Timeline will also pause. If the Scene is destroyed, the Timeline

will be automatically destroyed. However, you can control the Timeline directly, pausing,

resuming and stopping it at any time.

Create an instance of a Timeline via the Game Object Factory:

```
Copy
const timeline = this.add.timeline();


```

The Timeline always starts paused. You must call `play` on it to start it running.

You can also pass in a configuration object on creation, or an array of them:

```
Copy
const timeline = this.add.timeline({

    at: 1000,

    run: () => {

        this.add.sprite(400, 300, 'logo');

    }

});



timeline.play();


```

In this example we sequence a few different events:

```
Copy
const timeline = this.add.timeline([

    {

        at: 1000,

        run: () => { this.logo = this.add.sprite(400, 300, 'logo'); },

        sound: 'TitleMusic'

    },

    {

        at: 2500,

        tween: {

            targets: this.logo,

            y: 600,

            yoyo: true

        },

        sound: 'Explode'

    },

    {

        at: 8000,

        event: 'HURRY_PLAYER',

        target: this.background,

        set: {

            tint: 0xff0000

        }

    }

]);



timeline.play();


```

The Timeline can also be looped with the repeat method:

```
Copy
timeline.repeat().play();


```

There are lots of options available to you via the configuration object. See the

[Phaser.Types.Time.TimelineEventConfig](../typedef/types-time.md) typedef for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Time.TimelineEventConfig](../typedef/types-time.md) | Array.<[Phaser.Types.Time.TimelineEventConfig](../typedef/types-time.md)> | No | The configuration object for this Timeline Event, or an array of them. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Time.Timeline](time-timeline.md) - The Timeline that was created.

> Source: [src/time/Timeline.js#L795](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Timeline.js#L795)  
> Since: 3.60.0

---

## triangle

### <instance> triangle([x], [y], [x1], [y1], [x2], [y2], [x3], [y3], [fillColor], [fillAlpha])

**Description:**

Creates a new Triangle Shape Game Object and adds it to the Scene.

Note: This method will only be available if the Triangle Game Object has been built into Phaser.

The Triangle Shape is a Game Object that can be added to a Scene, Group or Container. You can

treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling

it for input or physics. It provides a quick and easy way for you to render this shape in your

game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports both fill and stroke colors.

The Triangle consists of 3 lines, joining up to form a triangular shape. You can control the

position of each point of these lines. The triangle is always closed and cannot have an open

face. If you require that, consider using a Polygon instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| x1 | number | Yes | 0 | The horizontal position of the first point in the triangle. |
| y1 | number | Yes | 128 | The vertical position of the first point in the triangle. |
| x2 | number | Yes | 64 | The horizontal position of the second point in the triangle. |
| y2 | number | Yes | 0 | The vertical position of the second point in the triangle. |
| x3 | number | Yes | 128 | The horizontal position of the third point in the triangle. |
| y3 | number | Yes | 128 | The vertical position of the third point in the triangle. |
| fillColor | number | Yes |  | The color the triangle will be filled with, i.e. 0xff0000 for red. |
| fillAlpha | number | Yes |  | The alpha the triangle will be filled with. You can also set the alpha of the overall Shape using its `alpha` property. |

**Returns:** [Phaser.GameObjects.Triangle](gameobjects-triangle.md) - The Game Object that was created.

> Source: [src/gameobjects/shape/triangle/TriangleFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/shape/triangle/TriangleFactory.js#L10)  
> Since: 3.13.0

---

## tween

### <instance> tween(config)

**Description:**

Creates a new Tween object.

Note: This method will only be available if Tweens have been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](../typedef/types-tweens.md) | [Phaser.Types.Tweens.TweenChainBuilderConfig](../typedef/types-tweens.md) | [Phaser.Tweens.Tween](tweens-tween.md) | [Phaser.Tweens.TweenChain](tweens-tweenchain.md) |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.Tween](tweens-tween.md) - The Tween that was created.

> Source: [src/tweens/tween/Tween.js#L811](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/Tween.js#L811)  
> Since: 3.0.0

---

## tweenchain

### <instance> tweenchain(config)

**Description:**

Creates a new TweenChain object and adds it to the Tween Manager.

Note: This method will only be available if Tweens have been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](../typedef/types-tweens.md) | object | No | The TweenChain configuration. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tweens.TweenChain](tweens-tweenchain.md) - The TweenChain that was created.

> Source: [src/tweens/tween/TweenChain.js#L529](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/TweenChain.js#L529)  
> Since: 3.60.0

---

## video

### <instance> video(x, y, [key])

**Description:**

Creates a new Video Game Object and adds it to the Scene.

This Game Object is capable of handling playback of a video file, video stream or media stream.

You can optionally 'preload' the video into the Phaser Video Cache:

```
Copy
preload () {

  this.load.video('ripley', 'assets/aliens.mp4');

}



create () {

  this.add.video(400, 300, 'ripley');

}


```

You don't have to 'preload' the video. You can also play it directly from a URL:

```
Copy
create () {

  this.add.video(400, 300).loadURL('assets/aliens.mp4');

}


```

To all intents and purposes, a video is a standard Game Object, just like a Sprite. And as such, you can do

all the usual things to it, such as scaling, rotating, cropping, tinting, making interactive, giving a

physics body, etc.

Transparent videos are also possible via the WebM file format. Providing the video file has was encoded with

an alpha channel, and providing the browser supports WebM playback (not all of them do), then it will render

in-game with full transparency.

### Autoplaying Videos

Videos can only autoplay if the browser has been unlocked with an interaction, or satisfies the MEI settings.

The policies that control autoplaying are vast and vary between browser. You can, and should, read more about

it here: <https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide>

If your video doesn't contain any audio, then set the `noAudio` parameter to `true` when the video is *loaded*,

and it will often allow the video to play immediately:

```
Copy
preload () {

  this.load.video('pixar', 'nemo.mp4', true);

}


```

The 3rd parameter in the load call tells Phaser that the video doesn't contain any audio tracks. Video without

audio can autoplay without requiring a user interaction. Video with audio cannot do this unless it satisfies

the browsers MEI settings. See the MDN Autoplay Guide for further details.

Or:

```
Copy
create () {

  this.add.video(400, 300).loadURL('assets/aliens.mp4', true);

}


```

You can set the `noAudio` parameter to `true` even if the video does contain audio. It will still allow the video

to play immediately, but the audio will not start.

Note that due to a bug in IE11 you cannot play a video texture to a Sprite in WebGL. For IE11 force Canvas mode.

More details about video playback and the supported media formats can be found on MDN:

<https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement>

<https://developer.mozilla.org/en-US/docs/Web/Media/Formats>

Note: This method will only be available if the Video Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this Game Object in the world. |
| key | string | Yes | Optional key of the Video this Game Object will play, as stored in the Video Cache. |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - The Game Object that was created.

> Source: [src/gameobjects/video/VideoFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/VideoFactory.js#L10)  
> Since: 3.20.0

---

## zone

### <instance> zone(x, y, width, height)

**Description:**

Creates a new Zone Game Object and adds it to the Scene.

Note: This method will only be available if the Zone Game Object has been built into Phaser.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of this Game Object in the world. |
| width | number | No | The width of the Game Object. |
| height | number | No | The height of the Game Object. |

**Returns:** [Phaser.GameObjects.Zone](gameobjects-zone.md) - The Game Object that was created.

> Source: [src/gameobjects/zone/ZoneFactory.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/zone/ZoneFactory.js#L10)  
> Since: 3.0.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

> Source: [src/gameobjects/GameObjectFactory.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L86)  
> Since: 3.5.1

---

## destroy

### <instance> destroy()

**Description:**

The Scene that owns this plugin is being destroyed.

We need to shutdown and then kill off all external references.

**Access:** private

> Source: [src/gameobjects/GameObjectFactory.js#L161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L161)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

The Scene that owns this plugin is shutting down.

We need to kill and reset all internal properties as well as stop listening to Scene events.

**Access:** private

> Source: [src/gameobjects/GameObjectFactory.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L148)  
> Since: 3.0.0

---

## start

### <instance> start()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

> Source: [src/gameobjects/GameObjectFactory.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L102)  
> Since: 3.5.0

---

# Public Members

## displayList

### displayList: [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md)

**Description:**

A reference to the Scene Display List.

**Access:** protected

> Source: [src/gameobjects/GameObjectFactory.js#L62](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L62)  
> Since: 3.0.0

---

## events

### events: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

A reference to the Scene Event Emitter.

**Access:** protected

> Source: [src/gameobjects/GameObjectFactory.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L52)  
> Since: 3.50.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene to which this Game Object Factory belongs.

**Access:** protected

> Source: [src/gameobjects/GameObjectFactory.js#L32](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L32)  
> Since: 3.0.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

A reference to the Scene.Systems.

**Access:** protected

> Source: [src/gameobjects/GameObjectFactory.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L42)  
> Since: 3.0.0

---

## updateList

### updateList: [Phaser.GameObjects.UpdateList](gameobjects-updatelist.md)

**Description:**

A reference to the Scene Update List.

**Access:** protected

> Source: [src/gameobjects/GameObjectFactory.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObjectFactory.js#L72)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Methods](#public-methods)

  + [arc](#arc)

    - [<instance> arc([x], [y], [radius], [startAngle], [endAngle], [anticlockwise], [fillColor], [fillAlpha])](#instance-arcx-y-radius-startangle-endangle-anticlockwise-fillcolor-fillalpha)
  + [bitmapMask](#bitmapmask)

    - [<instance> bitmapMask([maskObject], [x], [y], [texture], [frame])](#instance-bitmapmaskmaskobject-x-y-texture-frame)
  + [bitmapText](#bitmaptext)

    - [<instance> bitmapText(x, y, font, [text], [size], [align])](#instance-bitmaptextx-y-font-text-size-align)
  + [blitter](#blitter)

    - [<instance> blitter(x, y, texture, [frame])](#instance-blitterx-y-texture-frame)
  + [circle](#circle)

    - [<instance> circle([x], [y], [radius], [fillColor], [fillAlpha])](#instance-circlex-y-radius-fillcolor-fillalpha)
  + [container](#container)

    - [<instance> container([x], [y], [children])](#instance-containerx-y-children)
  + [curve](#curve)

    - [<instance> curve([x], [y], [curve], [fillColor], [fillAlpha])](#instance-curvex-y-curve-fillcolor-fillalpha)
  + [dom](#dom)

    - [<instance> dom(x, y, [element], [style], [innerText])](#instance-domx-y-element-style-innertext)
  + [dynamicBitmapText](#dynamicbitmaptext)

    - [<instance> dynamicBitmapText(x, y, font, [text], [size])](#instance-dynamicbitmaptextx-y-font-text-size)
  + [ellipse](#ellipse)

    - [<instance> ellipse([x], [y], [width], [height], [fillColor], [fillAlpha])](#instance-ellipsex-y-width-height-fillcolor-fillalpha)
  + [existing](#existing)

    - [<instance> existing(child)](#instance-existingchild)
  + [extern](#extern)

    - [<instance> extern()](#instance-extern)
  + [follower](#follower)

    - [<instance> follower(path, x, y, texture, [frame])](#instance-followerpath-x-y-texture-frame)
  + [graphics](#graphics)

    - [<instance> graphics([config])](#instance-graphicsconfig)
  + [grid](#grid)

    - [<instance> grid([x], [y], [width], [height], [cellWidth], [cellHeight], [fillColor], [fillAlpha], [outlineFillColor], [outlineFillAlpha])](#instance-gridx-y-width-height-cellwidth-cellheight-fillcolor-fillalpha-outlinefillcolor-outlinefillalpha)
  + [group](#group)

    - [<instance> group([children], [config])](#instance-groupchildren-config)
  + [image](#image)

    - [<instance> image(x, y, texture, [frame])](#instance-imagex-y-texture-frame)
  + [isobox](#isobox)

    - [<instance> isobox([x], [y], [size], [height], [fillTop], [fillLeft], [fillRight])](#instance-isoboxx-y-size-height-filltop-fillleft-fillright)
  + [isotriangle](#isotriangle)

    - [<instance> isotriangle([x], [y], [size], [height], [reversed], [fillTop], [fillLeft], [fillRight])](#instance-isotrianglex-y-size-height-reversed-filltop-fillleft-fillright)
  + [layer](#layer)

    - [<instance> layer([children])](#instance-layerchildren)
  + [line](#line)

    - [<instance> line([x], [y], [x1], [y1], [x2], [y2], [strokeColor], [strokeAlpha])](#instance-linex-y-x1-y1-x2-y2-strokecolor-strokealpha)
  + [mesh](#mesh)

    - [<instance> mesh([x], [y], [texture], [frame], [vertices], [uvs], [indicies], [containsZ], [normals], [colors], [alphas])](#instance-meshx-y-texture-frame-vertices-uvs-indicies-containsz-normals-colors-alphas)
  + [nineslice](#nineslice)

    - [<instance> nineslice(x, y, texture, [frame], [width], [height], [leftWidth], [rightWidth], [topHeight], [bottomHeight])](#instance-nineslicex-y-texture-frame-width-height-leftwidth-rightwidth-topheight-bottomheight)
  + [particles](#particles)

    - [<instance> particles([x], [y], [texture], [config])](#instance-particlesx-y-texture-config)
  + [path](#path)

    - [<instance> path(x, y)](#instance-pathx-y)
  + [plane](#plane)

    - [<instance> plane([x], [y], [texture], [frame], [width], [height], [tile])](#instance-planex-y-texture-frame-width-height-tile)
  + [pointlight](#pointlight)

    - [<instance> pointlight(x, y, [color], [radius], [intensity], [attenuation])](#instance-pointlightx-y-color-radius-intensity-attenuation)
  + [polygon](#polygon)

    - [<instance> polygon([x], [y], [points], [fillColor], [fillAlpha])](#instance-polygonx-y-points-fillcolor-fillalpha)
  + [rectangle](#rectangle)

    - [<instance> rectangle([x], [y], [width], [height], [fillColor], [fillAlpha])](#instance-rectanglex-y-width-height-fillcolor-fillalpha)
  + [register](#register)

    - [<static> register(factoryType, factoryFunction)](#static-registerfactorytype-factoryfunction)
  + [remove](#remove)

    - [<static> remove(factoryType)](#static-removefactorytype)
  + [renderTexture](#rendertexture)

    - [<instance> renderTexture(x, y, [width], [height])](#instance-rendertexturex-y-width-height)
  + [rope](#rope)

    - [<instance> rope(x, y, texture, [frame], [points], [horizontal], [colors], [alphas])](#instance-ropex-y-texture-frame-points-horizontal-colors-alphas)
  + [shader](#shader)

    - [<instance> shader(key, [x], [y], [width], [height], [textures], [textureData])](#instance-shaderkey-x-y-width-height-textures-texturedata)
  + [sprite](#sprite)

    - [<instance> sprite(x, y, texture, [frame])](#instance-spritex-y-texture-frame)
  + [star](#star)

    - [<instance> star([x], [y], [points], [innerRadius], [outerRadius], [fillColor], [fillAlpha])](#instance-starx-y-points-innerradius-outerradius-fillcolor-fillalpha)
  + [text](#text)

    - [<instance> text(x, y, text, [style])](#instance-textx-y-text-style)
  + [tilemap](#tilemap)

    - [<instance> tilemap([key], [tileWidth], [tileHeight], [width], [height], [data], [insertNull])](#instance-tilemapkey-tilewidth-tileheight-width-height-data-insertnull)
  + [tileSprite](#tilesprite)

    - [<instance> tileSprite(x, y, width, height, texture, [frame])](#instance-tilespritex-y-width-height-texture-frame)
  + [timeline](#timeline)

    - [<instance> timeline(config)](#instance-timelineconfig)
  + [triangle](#triangle)

    - [<instance> triangle([x], [y], [x1], [y1], [x2], [y2], [x3], [y3], [fillColor], [fillAlpha])](#instance-trianglex-y-x1-y1-x2-y2-x3-y3-fillcolor-fillalpha)
  + [tween](#tween)

    - [<instance> tween(config)](#instance-tweenconfig)
  + [tweenchain](#tweenchain)

    - [<instance> tweenchain(config)](#instance-tweenchainconfig)
  + [video](#video)

    - [<instance> video(x, y, [key])](#instance-videox-y-key)
    - [Autoplaying Videos](#autoplaying-videos)
  + [zone](#zone)

    - [<instance> zone(x, y, width, height)](#instance-zonex-y-width-height)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [start](#start)

    - [<instance> start()](#instance-start)
* [Public Members](#public-members)

  + [displayList](#displaylist)

    - [displayList: Phaser.GameObjects.DisplayList](#displaylist-phasergameobjectsdisplaylist)
  + [events](#events)

    - [events: Phaser.Events.EventEmitter](#events-phasereventseventemitter)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
  + [updateList](#updatelist)

    - [updateList: Phaser.GameObjects.UpdateList](#updatelist-phasergameobjectsupdatelist)

Back to top

©2025[Phaser](https://docs.phaser.io)