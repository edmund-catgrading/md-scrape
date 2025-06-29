# Graphics

Phaser.GameObjects.Graphics

A Graphics object is a way to draw primitive shapes to your game. Primitives include forms of geometry, such as

Rectangles, Circles, and Polygons. They also include lines, arcs and curves. When you initially create a Graphics

object it will be empty.

To draw to it you must first specify a line style or fill style (or both), draw shapes using paths, and finally

fill or stroke them. For example:

```
Copy
graphics.lineStyle(5, 0xFF00FF, 1.0);

graphics.beginPath();

graphics.moveTo(100, 100);

graphics.lineTo(200, 200);

graphics.closePath();

graphics.strokePath();


```

There are also many helpful methods that draw and fill/stroke common shapes for you.

```
Copy
graphics.lineStyle(5, 0xFF00FF, 1.0);

graphics.fillStyle(0xFFFFFF, 1.0);

graphics.fillRect(50, 50, 400, 200);

graphics.strokeRect(50, 50, 400, 200);


```

When a Graphics object is rendered it will render differently based on if the game is running under Canvas or WebGL.

Under Canvas it will use the HTML Canvas context drawing operations to draw the path.

Under WebGL the graphics data is decomposed into polygons. Both of these are expensive processes, especially with

complex shapes.

If your Graphics object doesn't change much (or at all) once you've drawn your shape to it, then you will help

performance by calling [Phaser.GameObjects.Graphics#generateTexture](gameobjects-graphics.md). This will 'bake' the Graphics object into

a Texture, and return it. You can then use this Texture for Sprites or other display objects. If your Graphics object

updates frequently then you should avoid doing this, as it will constantly generate new textures, which will consume

memory.

As you can tell, Graphics objects are a bit of a trade-off. While they are extremely useful, you need to be careful

in their complexity and quantity of them in your game.

**Constructor**

`new Graphics(scene, [options])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to which this Graphics object belongs. |
| --- | --- | --- | --- |
| options | [Phaser.Types.GameObjects.Graphics.Options](../typedef/types-gameobjects-graphics.md) | Yes | Options that set the position and default style of this Graphics object. |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)  
> [Phaser.GameObjects.Components.AlphaSingle](../namespace/gameobjects-components-alphasingle.md)  
> [Phaser.GameObjects.Components.BlendMode](../namespace/gameobjects-components-blendmode.md)  
> [Phaser.GameObjects.Components.Depth](../namespace/gameobjects-components-depth.md)  
> [Phaser.GameObjects.Components.Mask](../namespace/gameobjects-components-mask.md)  
> [Phaser.GameObjects.Components.Pipeline](../namespace/gameobjects-components-pipeline.md)  
> [Phaser.GameObjects.Components.PostPipeline](../namespace/gameobjects-components-postpipeline.md)  
> [Phaser.GameObjects.Components.Transform](../namespace/gameobjects-components-transform.md)  
> [Phaser.GameObjects.Components.Visible](../namespace/gameobjects-components-visible.md)  
> [Phaser.GameObjects.Components.ScrollFactor](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/graphics/Graphics.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L18)  
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

## alpha

### alpha: number

**Description:**

The alpha value of the Game Object.

This is a global value, impacting the entire Game Object, not just a region of it.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#alpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L68)  
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

## commandBuffer

### commandBuffer: array

**Description:**

The array of commands used to render the Graphics.

> Source: [src/gameobjects/graphics/Graphics.js#L128](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L128)  
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

## defaultFillAlpha

### defaultFillAlpha: number

**Description:**

The default fill alpha for shapes rendered by this Graphics object.

Set this value with `setDefaultStyles()`.

> Source: [src/gameobjects/graphics/Graphics.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L150)  
> Since: 3.0.0

---

## defaultFillColor

### defaultFillColor: number

**Description:**

The default fill color for shapes rendered by this Graphics object.

Set this value with `setDefaultStyles()`.

> Source: [src/gameobjects/graphics/Graphics.js#L138](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L138)  
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

## defaultStrokeAlpha

### defaultStrokeAlpha: number

**Description:**

The default stroke alpha for shapes rendered by this Graphics object.

Set this value with `setDefaultStyles()`.

> Source: [src/gameobjects/graphics/Graphics.js#L186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L186)  
> Since: 3.0.0

---

## defaultStrokeColor

### defaultStrokeColor: number

**Description:**

The default stroke color for shapes rendered by this Graphics object.

Set this value with `setDefaultStyles()`.

> Source: [src/gameobjects/graphics/Graphics.js#L174](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L174)  
> Since: 3.0.0

---

## defaultStrokeWidth

### defaultStrokeWidth: number

**Description:**

The default stroke width for shapes rendered by this Graphics object.

Set this value with `setDefaultStyles()`.

> Source: [src/gameobjects/graphics/Graphics.js#L162](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L162)  
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

The horizontal display origin of the Graphics.

> Source: [src/gameobjects/graphics/Graphics.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L108)  
> Since: 3.0.0

---

## displayOriginY

### displayOriginY: number

**Description:**

The vertical display origin of the Graphics.

> Source: [src/gameobjects/graphics/Graphics.js#L118](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L118)  
> Since: 3.0.0

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

## mask

### mask: [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md), [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)

**Description:**

The Mask this Game Object is using during render.

**Inherits:** [Phaser.GameObjects.Components.Mask#mask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L19)  
> Since: 3.0.0

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

## TargetCamera

### TargetCamera: [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md)

**Description:**

A Camera used specifically by the Graphics system for rendering to textures.

> Source: [src/gameobjects/graphics/Graphics.js#L1565](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1565)  
> Since: 3.1.0

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

## \_alpha

### \_alpha: number

**Description:**

Private internal value. Holds the global alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#\_alpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L22](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L22)  
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

## \_depth

### \_depth: number

**Description:**

Private internal value. Holds the depth of the Game Object.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Depth#\_depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L19)  
> Since: 3.0.0

---

## \_lineWidth

### \_lineWidth: number

**Description:**

Internal property that keeps track of the line width style setting.

**Access:** private

> Source: [src/gameobjects/graphics/Graphics.js#L198](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L198)  
> Since: 3.0.0

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

## \_visible

### \_visible: boolean

**Description:**

Private internal value. Holds the visible value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Visible#\_visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L20](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L20)  
> Since: 3.0.0

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - `this`.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addToUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L735](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L735)  
> Since: 3.53.0

---

## arc

### <instance> arc(x, y, radius, startAngle, endAngle, [anticlockwise], [overshoot])

**Description:**

Draw an arc.

This method can be used to create circles, or parts of circles.

Make sure you call `beginPath` before starting the arc unless you wish for the arc to automatically

close when filled or stroked.

Use the optional `overshoot` argument increase the number of iterations that take place when

the arc is rendered in WebGL. This is useful if you're drawing an arc with an especially thick line,

as it will allow the arc to fully join-up. Try small values at first, i.e. 0.01.

Call [Phaser.GameObjects.Graphics#fillPath](gameobjects-graphics.md) or [Phaser.GameObjects.Graphics#strokePath](gameobjects-graphics.md) after calling

this method to draw the arc.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of the center of the circle. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate of the center of the circle. |
| radius | number | No |  | The radius of the circle. |
| startAngle | number | No |  | The starting angle, in radians. |
| endAngle | number | No |  | The ending angle, in radians. |
| anticlockwise | boolean | Yes | false | Whether the drawing should be anticlockwise or clockwise. |
| overshoot | number | Yes | 0 | This value allows you to increase the segment iterations in WebGL rendering. Useful if the arc has a thick stroke and needs to overshoot to join-up cleanly. Use small numbers such as 0.01 to start with and increase as needed. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1242](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1242)  
> Since: 3.0.0

---

## beginPath

### <instance> beginPath()

**Description:**

Start a new shape path.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L379](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L379)  
> Since: 3.0.0

---

## clear

### <instance> clear()

**Description:**

Clear the command buffer and reset the fill style and line style to their defaults.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1442](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1442)  
> Since: 3.0.0

---

## clearAlpha

### <instance> clearAlpha()

**Description:**

Clears all alpha values associated with this Game Object.

Immediately sets the alpha levels back to 1 (fully opaque).

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#clearAlpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L33)  
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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#clearMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L56)  
> Since: 3.6.2

---

## closePath

### <instance> closePath()

**Description:**

Close the current path.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L396](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L396)  
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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This GameObject.

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

## fill

### <instance> fill()

**Description:**

Fill the current path.

This is an alias for `Graphics.fillPath` and does the same thing.

It was added to match the CanvasRenderingContext 2D API.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L430](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L430)  
> Since: 3.16.0

---

## fillCircle

### <instance> fillCircle(x, y, radius)

**Description:**

Fill a circle with the given position and radius.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the center of the circle. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the center of the circle. |
| radius | number | No | The radius of the circle. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L517](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L517)  
> Since: 3.0.0

---

## fillCircleShape

### <instance> fillCircleShape(circle)

**Description:**

Fill the given circle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The circle to fill. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L487](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L487)  
> Since: 3.0.0

---

## fillEllipse

### <instance> fillEllipse(x, y, width, height, [smoothness])

**Description:**

Fill an ellipse with the given position and size.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of the center of the ellipse. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate of the center of the ellipse. |
| width | number | No |  | The width of the ellipse. |
| height | number | No |  | The height of the ellipse. |
| smoothness | number | Yes | 32 | The number of points to draw the ellipse with. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1217)  
> Since: 3.0.0

---

## fillEllipseShape

### <instance> fillEllipseShape(ellipse, [smoothness])

**Description:**

Fill the given ellipse.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No |  | The ellipse to fill. |
| --- | --- | --- | --- | --- |
| smoothness | number | Yes | 32 | The number of points to draw the ellipse with. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1197](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1197)  
> Since: 3.0.0

---

## fillGradientStyle

### <instance> fillGradientStyle(topLeft, topRight, bottomLeft, bottomRight, [alphaTopLeft], [alphaTopRight], [alphaBottomLeft], [alphaBottomRight])

**Description:**

Sets a gradient fill style. This is a WebGL only feature.

The gradient color values represent the 4 corners of an untransformed rectangle.

The gradient is used to color all filled shapes and paths drawn after calling this method.

If you wish to turn a gradient off, call `fillStyle` and provide a new single fill color.

When filling a triangle only the first 3 color values provided are used for the 3 points of a triangle.

This feature is best used only on rectangles and triangles. All other shapes will give strange results.

Note that for objects such as arcs or ellipses, or anything which is made out of triangles, each triangle used

will be filled with a gradient on its own. There is no ability to gradient fill a shape or path as a single

entity at this time.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| topLeft | number | No |  | The top left fill color. |
| --- | --- | --- | --- | --- |
| topRight | number | No |  | The top right fill color. |
| bottomLeft | number | No |  | The bottom left fill color. |
| bottomRight | number | No |  | The bottom right fill color. Not used when filling triangles. |
| alphaTopLeft | number | Yes | 1 | The top left alpha value. If you give only this value, it's used for all corners. |
| alphaTopRight | number | Yes | 1 | The top right alpha value. |
| alphaBottomLeft | number | Yes | 1 | The bottom left alpha value. |
| alphaBottomRight | number | Yes | 1 | The bottom right alpha value. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L295)  
> Since: 3.12.0

---

## fillPath

### <instance> fillPath()

**Description:**

Fill the current path.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L413](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L413)  
> Since: 3.0.0

---

## fillPoint

### <instance> fillPoint(x, y, [size])

**Description:**

Fill a point at the given position.

Draws a square at the given position, 1 pixel in size by default.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of the point. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate of the point. |
| size | number | Yes | 1 | The size of the square to draw. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L862](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L862)  
> Since: 3.0.0

---

## fillPoints

### <instance> fillPoints(points, [closeShape], [closePath], [endIndex])

**Description:**

Fill the shape represented by the given array of points.

Pass `closeShape` to automatically close the shape by joining the last to the first point.

Pass `closePath` to automatically close the path before it is filled.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| points | array | Array.<[Phaser.Geom.Point](geom-point.md)> | No |  | The points to fill. |
| --- | --- | --- | --- | --- |
| closeShape | boolean | Yes | false | When `true`, the shape is closed by joining the last point to the first point. |
| closePath | boolean | Yes | false | When `true`, the path is closed before being stroked. |
| endIndex | number | Yes |  | The index of `points` to stop at. Defaults to `points.length`. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1105](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1105)  
> Since: 3.0.0

---

## fillPointShape

### <instance> fillPointShape(point, [size])

**Description:**

Fill the given point.

Draws a square at the given position, 1 pixel in size by default.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | [Phaser.Math.Vector2](math-vector2.md) | object | No |  |
| --- | --- | --- | --- | --- |
| size | number | Yes | 1 | The size of the square to draw. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L844](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L844)  
> Since: 3.0.0

---

## fillRect

### <instance> fillRect(x, y, width, height)

**Description:**

Fill a rectangle with the given position and size.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the top-left of the rectangle. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the top-left of the rectangle. |
| width | number | No | The width of the rectangle. |
| height | number | No | The height of the rectangle. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L589](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L589)  
> Since: 3.0.0

---

## fillRectShape

### <instance> fillRectShape(rect)

**Description:**

Fill the given rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The rectangle to fill. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L559](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L559)  
> Since: 3.0.0

---

## fillRoundedRect

### <instance> fillRoundedRect(x, y, width, height, [radius])

**Description:**

Fill a rounded rectangle with the given position, size and radius.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of the top-left of the rectangle. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate of the top-left of the rectangle. |
| width | number | No |  | The width of the rectangle. |
| height | number | No |  | The height of the rectangle. |
| radius | [Phaser.Types.GameObjects.Graphics.RoundedRectRadius](../typedef/types-gameobjects-graphics.md) | number | Yes | 20 | The corner radius; It can also be an object to specify different radius for corners. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L654](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L654)  
> Since: 3.11.0

---

## fillStyle

### <instance> fillStyle(color, [alpha])

**Description:**

Set the current fill style. Used for all 'fill' related functions.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color | number | No |  | The fill color. |
| --- | --- | --- | --- | --- |
| alpha | number | Yes | 1 | The fill alpha. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L272)  
> Since: 3.0.0

---

## fillTriangle

### <instance> fillTriangle(x0, y0, x1, y1, x2, y2)

**Description:**

Fill a triangle with the given points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x0 | number | No | The x coordinate of the first point. |
| --- | --- | --- | --- |
| y0 | number | No | The y coordinate of the first point. |
| x1 | number | No | The x coordinate of the second point. |
| y1 | number | No | The y coordinate of the second point. |
| x2 | number | No | The x coordinate of the third point. |
| y2 | number | No | The y coordinate of the third point. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L926](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L926)  
> Since: 3.0.0

---

## fillTriangleShape

### <instance> fillTriangleShape(triangle)

**Description:**

Fill the given triangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The triangle to fill. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L896](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L896)  
> Since: 3.0.0

---

## generateTexture

### <instance> generateTexture(key, [width], [height])

**Description:**

Generate a texture from this Graphics object.

If `key` is a string it'll generate a new texture using it and add it into the

Texture Manager (assuming no key conflict happens).

If `key` is a Canvas it will draw the texture to that canvas context. Note that it will NOT

automatically upload it to the GPU in WebGL mode.

Please understand that the texture is created via the Canvas API of the browser, therefore some

Graphics features, such as `fillGradientStyle`, will not appear on the resulting texture,

as they're unsupported by the Canvas API.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | HTMLCanvasElement | No | The key to store the texture with in the Texture Manager, or a Canvas to draw to. |
| --- | --- | --- | --- |
| width | number | Yes | The width of the graphics to generate. |
| height | number | Yes | The height of the graphics to generate. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1467](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1467)  
> Since: 3.0.0

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This GameObject.

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

## lineBetween

### <instance> lineBetween(x1, y1, x2, y2)

**Description:**

Draw a line between the given points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x1 | number | No | The x coordinate of the start point of the line. |
| --- | --- | --- | --- |
| y1 | number | No | The y coordinate of the start point of the line. |
| x2 | number | No | The x coordinate of the end point of the line. |
| y2 | number | No | The y coordinate of the end point of the line. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L991](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L991)  
> Since: 3.0.0

---

## lineGradientStyle

### <instance> lineGradientStyle(lineWidth, topLeft, topRight, bottomLeft, bottomRight, [alpha])

**Description:**

Sets a gradient line style. This is a WebGL only feature.

The gradient color values represent the 4 corners of an untransformed rectangle.

The gradient is used to color all stroked shapes and paths drawn after calling this method.

If you wish to turn a gradient off, call `lineStyle` and provide a new single line color.

This feature is best used only on single lines. All other shapes will give strange results.

Note that for objects such as arcs or ellipses, or anything which is made out of triangles, each triangle used

will be filled with a gradient on its own. There is no ability to gradient stroke a shape or path as a single

entity at this time.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| lineWidth | number | No |  | The stroke width. |
| --- | --- | --- | --- | --- |
| topLeft | number | No |  | The tint being applied to the top-left of the Game Object. |
| topRight | number | No |  | The tint being applied to the top-right of the Game Object. |
| bottomLeft | number | No |  | The tint being applied to the bottom-left of the Game Object. |
| bottomRight | number | No |  | The tint being applied to the bottom-right of the Game Object. |
| alpha | number | Yes | 1 | The fill alpha. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L341](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L341)  
> Since: 3.12.0

---

## lineStyle

### <instance> lineStyle(lineWidth, color, [alpha])

**Description:**

Set the current line style. Used for all 'stroke' related functions.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| lineWidth | number | No |  | The stroke width. |
| --- | --- | --- | --- | --- |
| color | number | No |  | The stroke color. |
| alpha | number | Yes | 1 | The stroke alpha. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L246](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L246)  
> Since: 3.0.0

---

## lineTo

### <instance> lineTo(x, y)

**Description:**

Draw a line from the current drawing position to the given position.

Moves the current drawing position to the given position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to draw the line to. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate to draw the line to. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1014](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1014)  
> Since: 3.0.0

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

## moveTo

### <instance> moveTo(x, y)

**Description:**

Move the current drawing position to the given position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to move to. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate to move to. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1037](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1037)  
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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - `this`.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - `this`.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## preDestroy

### <instance> preDestroy()

**Description:**

Internal destroy handler, called as part of the destroy process.

**Access:** protected

> Source: [src/gameobjects/graphics/Graphics.js#L1551](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1551)  
> Since: 3.9.0

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - `this`.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This GameObject.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - `this`.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

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

## restore

### <instance> restore()

**Description:**

Restores the most recently saved state of the Graphics by popping from the state stack.

Use [Phaser.GameObjects.Graphics#save](gameobjects-graphics.md) to save the current state, and call this afterwards to restore that state.

If there is no saved state, this command does nothing.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1341](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1341)  
> Since: 3.0.0

---

## rotateCanvas

### <instance> rotateCanvas(radians)

**Description:**

Inserts a rotation command into this Graphics objects command buffer.

All objects drawn *after* calling this method will be rotated

by the given amount.

This does not change the rotation of the Graphics object itself,

only of the objects drawn by it after calling this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| radians | number | No | The rotation angle, in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1416](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1416)  
> Since: 3.0.0

---

## save

### <instance> save()

**Description:**

Saves the state of the Graphics by pushing the current state onto a stack.

The most recently saved state can then be restored with [Phaser.GameObjects.Graphics#restore](gameobjects-graphics.md).

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1322](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1322)  
> Since: 3.0.0

---

## scaleCanvas

### <instance> scaleCanvas(x, y)

**Description:**

Inserts a scale command into this Graphics objects command buffer.

All objects drawn *after* calling this method will be scaled

by the given amount.

This does not change the scale of the Graphics object itself,

only of the objects drawn by it after calling this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal scale to apply. |
| --- | --- | --- | --- |
| y | number | No | The vertical scale to apply. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1389](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1389)  
> Since: 3.0.0

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setActive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L216)  
> Since: 3.0.0

---

## setAlpha

### <instance> setAlpha([value])

**Description:**

Set the Alpha level of this Game Object. The alpha controls the opacity of the Game Object as it renders.

Alpha values are provided as a float between 0, fully transparent, and 1, fully opaque.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 1 | The alpha value applied across the whole Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#setAlpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L48)  
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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#setBlendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L80)  
> Since: 3.0.0

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L295)  
> Since: 3.0.0

---

## setDataEnabled

### <instance> setDataEnabled()

**Description:**

Adds a Data Manager component to this Game Object.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setDataEnabled](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L276)  
> Since: 3.0.0

---

## setDefaultStyles

### <instance> setDefaultStyles(options)

**Description:**

Set the default style settings for this Graphics object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| options | [Phaser.Types.GameObjects.Graphics.Styles](../typedef/types-gameobjects-graphics.md) | No | The styles to set as defaults. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L214](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L214)  
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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L64)  
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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L456](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L456)  
> Since: 3.0.0

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#setMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L28](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L28)  
> Since: 3.6.2

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setName](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L234)  
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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRandomPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L313](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L313)  
> Since: 3.8.0

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setState](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L252)  
> Since: 3.16.0

---

## setToBack

### <instance> setToBack()

**Description:**

Sets this Game Object to the back of the display list, or the back of its parent container.

Being at the back means it will render below everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setW](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L465](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L465)  
> Since: 3.0.0

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object instance.

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

## slice

### <instance> slice(x, y, radius, startAngle, endAngle, [anticlockwise], [overshoot])

**Description:**

Creates a pie-chart slice shape centered at `x`, `y` with the given radius.

You must define the start and end angle of the slice.

Setting the `anticlockwise` argument to `true` creates a shape similar to Pacman.

Setting it to `false` creates a shape like a slice of pie.

This method will begin a new path and close the path at the end of it.

To display the actual slice you need to call either `strokePath` or `fillPath` after it.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal center of the slice. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The vertical center of the slice. |
| radius | number | No |  | The radius of the slice. |
| startAngle | number | No |  | The start angle of the slice, given in radians. |
| endAngle | number | No |  | The end angle of the slice, given in radians. |
| anticlockwise | boolean | Yes | false | Whether the drawing should be anticlockwise or clockwise. |
| overshoot | number | Yes | 0 | This value allows you to overshoot the endAngle by this amount. Useful if the arc has a thick stroke and needs to overshoot to join-up cleanly. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1283)  
> Since: 3.4.0

---

## stroke

### <instance> stroke()

**Description:**

Stroke the current path.

This is an alias for `Graphics.strokePath` and does the same thing.

It was added to match the CanvasRenderingContext 2D API.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L467](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L467)  
> Since: 3.16.0

---

## strokeCircle

### <instance> strokeCircle(x, y, radius)

**Description:**

Stroke a circle with the given position and radius.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the center of the circle. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the center of the circle. |
| radius | number | No | The radius of the circle. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L538](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L538)  
> Since: 3.0.0

---

## strokeCircleShape

### <instance> strokeCircleShape(circle)

**Description:**

Stroke the given circle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](geom-circle.md) | No | The circle to stroke. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L502](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L502)  
> Since: 3.0.0

---

## strokeEllipse

### <instance> strokeEllipse(x, y, width, height, [smoothness])

**Description:**

Stroke an ellipse with the given position and size.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of the center of the ellipse. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate of the center of the ellipse. |
| width | number | No |  | The width of the ellipse. |
| height | number | No |  | The height of the ellipse. |
| smoothness | number | Yes | 32 | The number of points to draw the ellipse with. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1172)  
> Since: 3.0.0

---

## strokeEllipseShape

### <instance> strokeEllipseShape(ellipse, [smoothness])

**Description:**

Stroke the given ellipse.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](geom-ellipse.md) | No |  | The ellipse to stroke. |
| --- | --- | --- | --- | --- |
| smoothness | number | Yes | 32 | The number of points to draw the ellipse with. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1152](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1152)  
> Since: 3.0.0

---

## strokeLineShape

### <instance> strokeLineShape(line)

**Description:**

Draw the given line.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](geom-line.md) | No | The line to stroke. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L976](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L976)  
> Since: 3.0.0

---

## strokePath

### <instance> strokePath()

**Description:**

Stroke the current path.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L450](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L450)  
> Since: 3.0.0

---

## strokePoints

### <instance> strokePoints(points, [closeShape], [closePath], [endIndex])

**Description:**

Stroke the shape represented by the given array of points.

Pass `closeShape` to automatically close the shape by joining the last to the first point.

Pass `closePath` to automatically close the path before it is stroked.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| points | array | Array.<[Phaser.Geom.Point](geom-point.md)> | No |  | The points to stroke. |
| --- | --- | --- | --- | --- |
| closeShape | boolean | Yes | false | When `true`, the shape is closed by joining the last point to the first point. |
| closePath | boolean | Yes | false | When `true`, the path is closed before being stroked. |
| endIndex | number | Yes |  | The index of `points` to stop drawing at. Defaults to `points.length`. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1058](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1058)  
> Since: 3.0.0

---

## strokeRect

### <instance> strokeRect(x, y, width, height)

**Description:**

Stroke a rectangle with the given position and size.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the top-left of the rectangle. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the top-left of the rectangle. |
| width | number | No | The width of the rectangle. |
| height | number | No | The height of the rectangle. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L612](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L612)  
> Since: 3.0.0

---

## strokeRectShape

### <instance> strokeRectShape(rect)

**Description:**

Stroke the given rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](geom-rectangle.md) | No | The rectangle to stroke. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L574](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L574)  
> Since: 3.0.0

---

## strokeRoundedRect

### <instance> strokeRoundedRect(x, y, width, height, [radius])

**Description:**

Stroke a rounded rectangle with the given position, size and radius.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of the top-left of the rectangle. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate of the top-left of the rectangle. |
| width | number | No |  | The width of the rectangle. |
| height | number | No |  | The height of the rectangle. |
| radius | [Phaser.Types.GameObjects.Graphics.RoundedRectRadius](../typedef/types-gameobjects-graphics.md) | number | Yes | 20 | The corner radius; It can also be an object to specify different radii for corners. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L746](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L746)  
> Since: 3.11.0

---

## strokeTriangle

### <instance> strokeTriangle(x0, y0, x1, y1, x2, y2)

**Description:**

Stroke a triangle with the given points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x0 | number | No | The x coordinate of the first point. |
| --- | --- | --- | --- |
| y0 | number | No | The y coordinate of the first point. |
| x1 | number | No | The x coordinate of the second point. |
| y1 | number | No | The y coordinate of the second point. |
| x2 | number | No | The x coordinate of the third point. |
| y2 | number | No | The y coordinate of the third point. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L951](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L951)  
> Since: 3.0.0

---

## strokeTriangleShape

### <instance> strokeTriangleShape(triangle)

**Description:**

Stroke the given triangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](geom-triangle.md) | No | The triangle to stroke. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L911](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L911)  
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

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#toggleData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L387)  
> Since: 3.23.0

---

## toJSON

### <instance> toJSON()

**Description:**

Returns a JSON representation of the Game Object.

**Returns:** [Phaser.Types.GameObjects.JSONGameObject](../typedef/types-gameobjects.md) - A JSON representation of the Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#toJSON](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L604](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L604)  
> Since: 3.0.0

---

## translateCanvas

### <instance> translateCanvas(x, y)

**Description:**

Inserts a translation command into this Graphics objects command buffer.

All objects drawn *after* calling this method will be translated

by the given amount.

This does not change the position of the Graphics object itself,

only of the objects drawn by it after calling this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal translation to apply. |
| --- | --- | --- | --- |
| y | number | No | The vertical translation to apply. |

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - This Game Object.

> Source: [src/gameobjects/graphics/Graphics.js#L1362](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/Graphics.js#L1362)  
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

## renderCanvas

### <instance> renderCanvas(renderer, src, camera, parentMatrix, [renderTargetCtx], allowClip)

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
| src | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |
| renderTargetCtx | CanvasRenderingContext2D | Yes | The target rendering context. |
| allowClip | boolean | No | If `true` then path operations will be used instead of fill operations. |

> Source: [src/gameobjects/graphics/GraphicsCanvasRenderer.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/GraphicsCanvasRenderer.js#L10)  
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
| src | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

> Source: [src/gameobjects/graphics/GraphicsWebGLRenderer.js#L29](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/graphics/GraphicsWebGLRenderer.js#L29)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [angle](#angle)

    - [angle: number](#angle-number)
  + [blendMode](#blendmode)

    - [blendMode: Phaser.BlendModes, string, number](#blendmode-phaserblendmodes-string-number)
  + [body](#body)

    - [body: Phaser.Physics.Arcade.Body, Phaser.Physics.Arcade.StaticBody, MatterJS.BodyType](#body-phaserphysicsarcadebody-phaserphysicsarcadestaticbody-matterjsbodytype)
  + [cameraFilter](#camerafilter)

    - [cameraFilter: number](#camerafilter-number)
  + [commandBuffer](#commandbuffer)

    - [commandBuffer: array](#commandbuffer-array)
  + [data](#data)

    - [data: Phaser.Data.DataManager](#data-phaserdatadatamanager)
  + [defaultFillAlpha](#defaultfillalpha)

    - [defaultFillAlpha: number](#defaultfillalpha-number)
  + [defaultFillColor](#defaultfillcolor)

    - [defaultFillColor: number](#defaultfillcolor-number)
  + [defaultPipeline](#defaultpipeline)

    - [defaultPipeline: Phaser.Renderer.WebGL.WebGLPipeline](#defaultpipeline-phaserrendererwebglwebglpipeline)
  + [defaultStrokeAlpha](#defaultstrokealpha)

    - [defaultStrokeAlpha: number](#defaultstrokealpha-number)
  + [defaultStrokeColor](#defaultstrokecolor)

    - [defaultStrokeColor: number](#defaultstrokecolor-number)
  + [defaultStrokeWidth](#defaultstrokewidth)

    - [defaultStrokeWidth: number](#defaultstrokewidth-number)
  + [depth](#depth)

    - [depth: number](#depth-number)
  + [displayList](#displaylist)

    - [displayList: Phaser.GameObjects.DisplayList, Phaser.GameObjects.Layer](#displaylist-phasergameobjectsdisplaylist-phasergameobjectslayer)
  + [displayOriginX](#displayoriginx)

    - [displayOriginX: number](#displayoriginx-number)
  + [displayOriginY](#displayoriginy)

    - [displayOriginY: number](#displayoriginy-number)
  + [hasPostPipeline](#haspostpipeline)

    - [hasPostPipeline: boolean](#haspostpipeline-boolean)
  + [hasTransformComponent](#hastransformcomponent)

    - [hasTransformComponent: boolean](#hastransformcomponent-boolean)
  + [ignoreDestroy](#ignoredestroy)

    - [ignoreDestroy: boolean](#ignoredestroy-boolean)
  + [input](#input)

    - [input: Phaser.Types.Input.InteractiveObject](#input-phasertypesinputinteractiveobject)
  + [mask](#mask)

    - [mask: Phaser.Display.Masks.BitmapMask, Phaser.Display.Masks.GeometryMask](#mask-phaserdisplaymasksbitmapmask-phaserdisplaymasksgeometrymask)
  + [name](#name)

    - [name: string](#name-string)
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
  + [TargetCamera](#targetcamera)

    - [TargetCamera: Phaser.Cameras.Scene2D.Camera](#targetcamera-phasercamerasscene2dcamera)
  + [type](#type)

    - [type: string](#type-string)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
  + [w](#w)

    - [w: number](#w-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
  + [z](#z)

    - [z: number](#z-number)
* [Private Members](#private-members)

  + [\_alpha](#_alpha)

    - [\_alpha: number](#_alpha-number)
  + [\_blendMode](#_blendmode)

    - [\_blendMode: number](#_blendmode-number)
  + [\_depth](#_depth)

    - [\_depth: number](#_depth-number)
  + [\_lineWidth](#_linewidth)

    - [\_lineWidth: number](#_linewidth-number)
  + [\_rotation](#_rotation)

    - [\_rotation: number](#_rotation-number)
  + [\_scaleX](#_scalex)

    - [\_scaleX: number](#_scalex-number)
  + [\_scaleY](#_scaley)

    - [\_scaleY: number](#_scaley-number)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
* [Public Methods](#public-methods)

  + [addedToScene](#addedtoscene)

    - [<instance> addedToScene()](#instance-addedtoscene)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addToDisplayList](#addtodisplaylist)

    - [<instance> addToDisplayList([displayList])](#instance-addtodisplaylistdisplaylist)
  + [addToUpdateList](#addtoupdatelist)

    - [<instance> addToUpdateList()](#instance-addtoupdatelist)
  + [arc](#arc)

    - [<instance> arc(x, y, radius, startAngle, endAngle, [anticlockwise], [overshoot])](#instance-arcx-y-radius-startangle-endangle-anticlockwise-overshoot)
  + [beginPath](#beginpath)

    - [<instance> beginPath()](#instance-beginpath)
  + [clear](#clear)

    - [<instance> clear()](#instance-clear)
  + [clearAlpha](#clearalpha)

    - [<instance> clearAlpha()](#instance-clearalpha)
  + [clearFX](#clearfx)

    - [<instance> clearFX()](#instance-clearfx)
  + [clearMask](#clearmask)

    - [<instance> clearMask([destroyMask])](#instance-clearmaskdestroymask)
  + [closePath](#closepath)

    - [<instance> closePath()](#instance-closepath)
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
  + [fill](#fill)

    - [<instance> fill()](#instance-fill)
  + [fillCircle](#fillcircle)

    - [<instance> fillCircle(x, y, radius)](#instance-fillcirclex-y-radius)
  + [fillCircleShape](#fillcircleshape)

    - [<instance> fillCircleShape(circle)](#instance-fillcircleshapecircle)
  + [fillEllipse](#fillellipse)

    - [<instance> fillEllipse(x, y, width, height, [smoothness])](#instance-fillellipsex-y-width-height-smoothness)
  + [fillEllipseShape](#fillellipseshape)

    - [<instance> fillEllipseShape(ellipse, [smoothness])](#instance-fillellipseshapeellipse-smoothness)
  + [fillGradientStyle](#fillgradientstyle)

    - [<instance> fillGradientStyle(topLeft, topRight, bottomLeft, bottomRight, [alphaTopLeft], [alphaTopRight], [alphaBottomLeft], [alphaBottomRight])](#instance-fillgradientstyletopleft-topright-bottomleft-bottomright-alphatopleft-alphatopright-alphabottomleft-alphabottomright)
  + [fillPath](#fillpath)

    - [<instance> fillPath()](#instance-fillpath)
  + [fillPoint](#fillpoint)

    - [<instance> fillPoint(x, y, [size])](#instance-fillpointx-y-size)
  + [fillPoints](#fillpoints)

    - [<instance> fillPoints(points, [closeShape], [closePath], [endIndex])](#instance-fillpointspoints-closeshape-closepath-endindex)
  + [fillPointShape](#fillpointshape)

    - [<instance> fillPointShape(point, [size])](#instance-fillpointshapepoint-size)
  + [fillRect](#fillrect)

    - [<instance> fillRect(x, y, width, height)](#instance-fillrectx-y-width-height)
  + [fillRectShape](#fillrectshape)

    - [<instance> fillRectShape(rect)](#instance-fillrectshaperect)
  + [fillRoundedRect](#fillroundedrect)

    - [<instance> fillRoundedRect(x, y, width, height, [radius])](#instance-fillroundedrectx-y-width-height-radius)
  + [fillStyle](#fillstyle)

    - [<instance> fillStyle(color, [alpha])](#instance-fillstylecolor-alpha)
  + [fillTriangle](#filltriangle)

    - [<instance> fillTriangle(x0, y0, x1, y1, x2, y2)](#instance-filltrianglex0-y0-x1-y1-x2-y2)
  + [fillTriangleShape](#filltriangleshape)

    - [<instance> fillTriangleShape(triangle)](#instance-filltriangleshapetriangle)
  + [generateTexture](#generatetexture)

    - [<instance> generateTexture(key, [width], [height])](#instance-generatetexturekey-width-height)
  + [getData](#getdata)

    - [<instance> getData(key)](#instance-getdatakey)
  + [getDisplayList](#getdisplaylist)

    - [<instance> getDisplayList()](#instance-getdisplaylist)
  + [getIndexList](#getindexlist)

    - [<instance> getIndexList()](#instance-getindexlist)
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
  + [getWorldTransformMatrix](#getworldtransformmatrix)

    - [<instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])](#instance-getworldtransformmatrixtempmatrix-parentmatrix)
  + [incData](#incdata)

    - [<instance> incData(key, [amount])](#instance-incdatakey-amount)
  + [initPipeline](#initpipeline)

    - [<instance> initPipeline([pipeline])](#instance-initpipelinepipeline)
  + [initPostPipeline](#initpostpipeline)

    - [<instance> initPostPipeline([preFX])](#instance-initpostpipelineprefx)
  + [lineBetween](#linebetween)

    - [<instance> lineBetween(x1, y1, x2, y2)](#instance-linebetweenx1-y1-x2-y2)
  + [lineGradientStyle](#linegradientstyle)

    - [<instance> lineGradientStyle(lineWidth, topLeft, topRight, bottomLeft, bottomRight, [alpha])](#instance-linegradientstylelinewidth-topleft-topright-bottomleft-bottomright-alpha)
  + [lineStyle](#linestyle)

    - [<instance> lineStyle(lineWidth, color, [alpha])](#instance-linestylelinewidth-color-alpha)
  + [lineTo](#lineto)

    - [<instance> lineTo(x, y)](#instance-linetox-y)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [moveTo](#moveto)

    - [<instance> moveTo(x, y)](#instance-movetox-y)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
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
  + [restore](#restore)

    - [<instance> restore()](#instance-restore)
  + [rotateCanvas](#rotatecanvas)

    - [<instance> rotateCanvas(radians)](#instance-rotatecanvasradians)
  + [save](#save)

    - [<instance> save()](#instance-save)
  + [scaleCanvas](#scalecanvas)

    - [<instance> scaleCanvas(x, y)](#instance-scalecanvasx-y)
  + [setAbove](#setabove)

    - [<instance> setAbove(gameObject)](#instance-setabovegameobject)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha([value])](#instance-setalphavalue)
  + [setAngle](#setangle)

    - [<instance> setAngle([degrees])](#instance-setangledegrees)
  + [setBelow](#setbelow)

    - [<instance> setBelow(gameObject)](#instance-setbelowgameobject)
  + [setBlendMode](#setblendmode)

    - [<instance> setBlendMode(value)](#instance-setblendmodevalue)
  + [setData](#setdata)

    - [<instance> setData(key, [data])](#instance-setdatakey-data)
  + [setDataEnabled](#setdataenabled)

    - [<instance> setDataEnabled()](#instance-setdataenabled)
  + [setDefaultStyles](#setdefaultstyles)

    - [<instance> setDefaultStyles(options)](#instance-setdefaultstylesoptions)
  + [setDepth](#setdepth)

    - [<instance> setDepth(value)](#instance-setdepthvalue)
  + [setInteractive](#setinteractive)

    - [<instance> setInteractive([hitArea], [callback], [dropZone])](#instance-setinteractivehitarea-callback-dropzone)
  + [setMask](#setmask)

    - [<instance> setMask(mask)](#instance-setmaskmask)
  + [setName](#setname)

    - [<instance> setName(value)](#instance-setnamevalue)
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
  + [setRotation](#setrotation)

    - [<instance> setRotation([radians])](#instance-setrotationradians)
  + [setScale](#setscale)

    - [<instance> setScale([x], [y])](#instance-setscalex-y)
  + [setScrollFactor](#setscrollfactor)

    - [<instance> setScrollFactor(x, [y])](#instance-setscrollfactorx-y)
  + [setState](#setstate)

    - [<instance> setState(value)](#instance-setstatevalue)
  + [setToBack](#settoback)

    - [<instance> setToBack()](#instance-settoback)
  + [setToTop](#settotop)

    - [<instance> setToTop()](#instance-settotop)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value)](#instance-setvisiblevalue)
  + [setW](#setw)

    - [<instance> setW([value])](#instance-setwvalue)
  + [setX](#setx)

    - [<instance> setX([value])](#instance-setxvalue)
  + [setY](#sety)

    - [<instance> setY([value])](#instance-setyvalue)
  + [setZ](#setz)

    - [<instance> setZ([value])](#instance-setzvalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [slice](#slice)

    - [<instance> slice(x, y, radius, startAngle, endAngle, [anticlockwise], [overshoot])](#instance-slicex-y-radius-startangle-endangle-anticlockwise-overshoot)
  + [stroke](#stroke)

    - [<instance> stroke()](#instance-stroke)
  + [strokeCircle](#strokecircle)

    - [<instance> strokeCircle(x, y, radius)](#instance-strokecirclex-y-radius)
  + [strokeCircleShape](#strokecircleshape)

    - [<instance> strokeCircleShape(circle)](#instance-strokecircleshapecircle)
  + [strokeEllipse](#strokeellipse)

    - [<instance> strokeEllipse(x, y, width, height, [smoothness])](#instance-strokeellipsex-y-width-height-smoothness)
  + [strokeEllipseShape](#strokeellipseshape)

    - [<instance> strokeEllipseShape(ellipse, [smoothness])](#instance-strokeellipseshapeellipse-smoothness)
  + [strokeLineShape](#strokelineshape)

    - [<instance> strokeLineShape(line)](#instance-strokelineshapeline)
  + [strokePath](#strokepath)

    - [<instance> strokePath()](#instance-strokepath)
  + [strokePoints](#strokepoints)

    - [<instance> strokePoints(points, [closeShape], [closePath], [endIndex])](#instance-strokepointspoints-closeshape-closepath-endindex)
  + [strokeRect](#strokerect)

    - [<instance> strokeRect(x, y, width, height)](#instance-strokerectx-y-width-height)
  + [strokeRectShape](#strokerectshape)

    - [<instance> strokeRectShape(rect)](#instance-strokerectshaperect)
  + [strokeRoundedRect](#strokeroundedrect)

    - [<instance> strokeRoundedRect(x, y, width, height, [radius])](#instance-strokeroundedrectx-y-width-height-radius)
  + [strokeTriangle](#stroketriangle)

    - [<instance> strokeTriangle(x0, y0, x1, y1, x2, y2)](#instance-stroketrianglex0-y0-x1-y1-x2-y2)
  + [strokeTriangleShape](#stroketriangleshape)

    - [<instance> strokeTriangleShape(triangle)](#instance-stroketriangleshapetriangle)
  + [toggleData](#toggledata)

    - [<instance> toggleData(key)](#instance-toggledatakey)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [translateCanvas](#translatecanvas)

    - [<instance> translateCanvas(x, y)](#instance-translatecanvasx-y)
  + [update](#update)

    - [<instance> update([args])](#instance-updateargs)
  + [willRender](#willrender)

    - [<instance> willRender(camera)](#instance-willrendercamera)
* [Private Methods](#private-methods)

  + [renderCanvas](#rendercanvas)

    - [<instance> renderCanvas(renderer, src, camera, parentMatrix, [renderTargetCtx], allowClip)](#instance-rendercanvasrenderer-src-camera-parentmatrix-rendertargetctx-allowclip)
  + [renderWebGL](#renderwebgl)

    - [<instance> renderWebGL(renderer, src, camera, parentMatrix)](#instance-renderwebglrenderer-src-camera-parentmatrix)

Back to top

©2025[Phaser](https://docs.phaser.io)



Graphics