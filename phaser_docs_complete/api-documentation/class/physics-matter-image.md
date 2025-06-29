# Image

Phaser.Physics.Matter.Image

A Matter Physics Image Game Object.

An Image is a light-weight Game Object useful for the display of static images in your game,

such as logos, backgrounds, scenery or other non-animated elements. Images can have input

events and physics bodies, or be tweened, tinted or scrolled. The main difference between an

Image and a Sprite is that you cannot animate an Image as they do not have the Animation component.

**Constructor**

`new Image(world, x, y, texture, [frame], [options])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| world | [Phaser.Physics.Matter.World](physics-matter-world.md) | No | A reference to the Matter.World instance that this body belongs to. |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| y | number | No | The vertical position of this Game Object in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | No | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes | An optional frame from the Texture this Game Object is rendering with. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.Image](gameobjects-image.md)  
> [Phaser.Physics.Matter.Components.Bounce](../namespace/physics-matter-components-bounce.md)  
> [Phaser.Physics.Matter.Components.Collision](../namespace/physics-matter-components-collision.md)  
> [Phaser.Physics.Matter.Components.Force](../namespace/physics-matter-components-force.md)  
> [Phaser.Physics.Matter.Components.Friction](../namespace/physics-matter-components-friction.md)  
> [Phaser.Physics.Matter.Components.Gravity](../namespace/physics-matter-components-gravity.md)  
> [Phaser.Physics.Matter.Components.Mass](../namespace/physics-matter-components-mass.md)  
> [Phaser.Physics.Matter.Components.Sensor](../namespace/physics-matter-components-sensor.md)  
> [Phaser.Physics.Matter.Components.SetBody](../namespace/physics-matter-components-setbody.md)  
> [Phaser.Physics.Matter.Components.Sleep](../namespace/physics-matter-components-sleep.md)  
> [Phaser.Physics.Matter.Components.Static](../namespace/physics-matter-components-static.md)  
> [Phaser.Physics.Matter.Components.Transform](../namespace/physics-matter-components-transform.md)  
> [Phaser.Physics.Matter.Components.Velocity](../namespace/physics-matter-components-velocity.md)  
> [Phaser.GameObjects.Components.Alpha](../namespace/gameobjects-components-alpha.md)  
> [Phaser.GameObjects.Components.BlendMode](../namespace/gameobjects-components-blendmode.md)  
> [Phaser.GameObjects.Components.Depth](../namespace/gameobjects-components-depth.md)  
> [Phaser.GameObjects.Components.Flip](../namespace/gameobjects-components-flip.md)  
> [Phaser.GameObjects.Components.GetBounds](../namespace/gameobjects-components-getbounds.md)  
> [Phaser.GameObjects.Components.Mask](../namespace/gameobjects-components-mask.md)  
> [Phaser.GameObjects.Components.Origin](../namespace/gameobjects-components-origin.md)  
> [Phaser.GameObjects.Components.Pipeline](../namespace/gameobjects-components-pipeline.md)  
> [Phaser.GameObjects.Components.PostPipeline](../namespace/gameobjects-components-postpipeline.md)  
> [Phaser.GameObjects.Components.ScrollFactor](../namespace/gameobjects-components-scrollfactor.md)  
> [Phaser.GameObjects.Components.Size](../namespace/gameobjects-components-size.md)  
> [Phaser.GameObjects.Components.Texture](../namespace/gameobjects-components-texture.md)  
> [Phaser.GameObjects.Components.Tint](../namespace/gameobjects-components-tint.md)  
> [Phaser.GameObjects.Components.Transform](../namespace/gameobjects-components-transform.md)  
> [Phaser.GameObjects.Components.Visible](../namespace/gameobjects-components-visible.md)

> Source: [src/physics/matter-js/MatterImage.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterImage.js#L15)  
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

**Overrides:** Phaser.GameObjects.Components.Alpha#alpha

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

**Overrides:** Phaser.GameObjects.Components.Alpha#alphaBottomLeft

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

**Overrides:** Phaser.GameObjects.Components.Alpha#alphaBottomRight

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

**Overrides:** Phaser.GameObjects.Components.Alpha#alphaTopLeft

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

**Overrides:** Phaser.GameObjects.Components.Alpha#alphaTopRight

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

**Overrides:** Phaser.GameObjects.Components.Transform#angle

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

**Overrides:** Phaser.GameObjects.Components.BlendMode#blendMode

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

## centerOfMass

### centerOfMass: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The body's center of mass.

Calling this creates a new `Vector2 each time to avoid mutation.

If you only need to read the value and won't change it, you can get it from `GameObject.body.centerOfMass`.

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The center of mass.

**Inherits:** [Phaser.Physics.Matter.Components.Mass#centerOfMass](../namespace/physics-matter-components-mass.md)

> Source: [src/physics/matter-js/components/Mass.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Mass.js#L52)  
> Since: 3.10.0

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

**Overrides:** Phaser.GameObjects.Components.Pipeline#defaultPipeline

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

**Overrides:** Phaser.GameObjects.Components.Depth#depth

**Inherits:** [Phaser.GameObjects.Components.Depth#depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L30)  
> Since: 3.0.0

---

## displayHeight

### displayHeight: number

**Description:**

The displayed height of this Game Object.

This value takes into account the scale factor.

Setting this value will adjust the Game Object's scale property.

**Overrides:** Phaser.GameObjects.Components.Size#displayHeight

**Inherits:** [Phaser.GameObjects.Components.Size#displayHeight](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L78)  
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

The horizontal display origin of this Game Object.

The origin is a normalized value between 0 and 1.

The displayOrigin is a pixel value, based on the size of the Game Object combined with the origin.

**Overrides:** Phaser.GameObjects.Components.Origin#displayOriginX

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

**Overrides:** Phaser.GameObjects.Components.Origin#displayOriginY

**Inherits:** [Phaser.GameObjects.Components.Origin#displayOriginY](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L88)  
> Since: 3.0.0

---

## displayWidth

### displayWidth: number

**Description:**

The displayed width of this Game Object.

This value takes into account the scale factor.

Setting this value will adjust the Game Object's scale property.

**Overrides:** Phaser.GameObjects.Components.Size#displayWidth

**Inherits:** [Phaser.GameObjects.Components.Size#displayWidth](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L53)  
> Since: 3.0.0

---

## flipX

### flipX: boolean

**Description:**

The horizontally flipped state of the Game Object.

A Game Object that is flipped horizontally will render inversed on the horizontal axis.

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Overrides:** Phaser.GameObjects.Components.Flip#flipX

**Inherits:** [Phaser.GameObjects.Components.Flip#flipX](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L17)  
> Since: 3.0.0

---

## flipY

### flipY: boolean

**Description:**

The vertically flipped state of the Game Object.

A Game Object that is flipped vertically will render inversed on the vertical axis (i.e. upside down)

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Overrides:** Phaser.GameObjects.Components.Flip#flipY

**Inherits:** [Phaser.GameObjects.Components.Flip#flipY](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L31)  
> Since: 3.0.0

---

## frame

### frame: [Phaser.Textures.Frame](textures-frame.md)

**Description:**

The Texture Frame this Game Object is using to render with.

**Overrides:** Phaser.GameObjects.Components.Texture#frame

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#frame](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L30)  
> Since: 3.0.0

---

## hasPostPipeline

### hasPostPipeline: boolean

**Description:**

Does this Game Object have any Post Pipelines set?

**Tags:**

* webglOnly

**Overrides:** Phaser.GameObjects.Components.PostPipeline#hasPostPipeline

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#hasPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L21)  
> Since: 3.60.0

---

## hasTransformComponent

### hasTransformComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Overrides:** Phaser.GameObjects.Components.Transform#hasTransformComponent

**Inherits:** [Phaser.GameObjects.Components.Transform#hasTransformComponent](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L26](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L26)  
> Since: 3.60.0

---

## height

### height: number

**Description:**

The native (un-scaled) height of this Game Object.

Changing this value will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or use

the `displayHeight` property.

**Overrides:** Phaser.GameObjects.Components.Size#height

**Inherits:** [Phaser.GameObjects.Components.Size#height](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L40)  
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

## isCropped

### isCropped: boolean

**Description:**

A boolean flag indicating if this Game Object is being cropped or not.

You can toggle this at any time after `setCrop` has been called, to turn cropping on or off.

Equally, calling `setCrop` with no arguments will reset the crop and disable it.

**Overrides:** Phaser.GameObjects.Components.Texture#isCropped

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#isCropped](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L39)  
> Since: 3.11.0

---

## isTinted

### isTinted: boolean

**Description:**

Does this Game Object have a tint applied?

It checks to see if the 4 tint properties are set to the value 0xffffff

and that the `tintFill` property is `false`. This indicates that a Game Object isn't tinted.

**Tags:**

* webglOnly

**Overrides:** Phaser.GameObjects.Components.Tint#isTinted

**Inherits:** [Phaser.GameObjects.Components.Tint#isTinted](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L205)  
> Since: 3.11.0

---

## mask

### mask: [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md), [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)

**Description:**

The Mask this Game Object is using during render.

**Overrides:** Phaser.GameObjects.Components.Mask#mask

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

## originX

### originX: number

**Description:**

The horizontal origin of this Game Object.

The origin maps the relationship between the size and position of the Game Object.

The default value is 0.5, meaning all Game Objects are positioned based on their center.

Setting the value to 0 means the position now relates to the left of the Game Object.

Set this value with `setOrigin()`.

**Overrides:** Phaser.GameObjects.Components.Origin#originX

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

**Overrides:** Phaser.GameObjects.Components.Origin#originY

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

**Overrides:** Phaser.GameObjects.Components.Pipeline#pipeline

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

**Overrides:** Phaser.GameObjects.Components.Pipeline#pipelineData

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#postFX

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#postPipelineData

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#postPipelines

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#preFX

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

**Overrides:** Phaser.GameObjects.Components.Transform#rotation

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

**Overrides:** Phaser.GameObjects.Components.Transform#scale

**Inherits:** [Phaser.GameObjects.Components.Transform#scale](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L113)  
> Since: 3.18.0

---

## scaleX

### scaleX: number

**Description:**

The horizontal scale of this Game Object.

**Overrides:** Phaser.GameObjects.Components.Transform#scaleX

**Inherits:** [Phaser.GameObjects.Components.Transform#scaleX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L149)  
> Since: 3.0.0

---

## scaleY

### scaleY: number

**Description:**

The vertical scale of this Game Object.

**Overrides:** Phaser.GameObjects.Components.Transform#scaleY

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

**Overrides:** Phaser.GameObjects.Components.ScrollFactor#scrollFactorX

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

**Overrides:** Phaser.GameObjects.Components.ScrollFactor#scrollFactorY

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

## texture

### texture: [Phaser.Textures.Texture](textures-texture.md), [Phaser.Textures.CanvasTexture](textures-canvastexture.md)

**Description:**

The Texture this Game Object is using to render with.

**Overrides:** Phaser.GameObjects.Components.Texture#texture

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#texture](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L21)  
> Since: 3.0.0

---

## tint

### tint: number

**Description:**

The tint value being applied to the whole of the Game Object.

Return `tintTopLeft` when read this tint property.

**Tags:**

* webglOnly

**Overrides:** Phaser.GameObjects.Components.Tint#tint

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

**Overrides:** Phaser.GameObjects.Components.Tint#tintBottomLeft

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

**Overrides:** Phaser.GameObjects.Components.Tint#tintBottomRight

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

**Overrides:** Phaser.GameObjects.Components.Tint#tintFill

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

**Overrides:** Phaser.GameObjects.Components.Tint#tintTopLeft

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

**Overrides:** Phaser.GameObjects.Components.Tint#tintTopRight

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

**Overrides:** Phaser.GameObjects.Components.Visible#visible

**Inherits:** [Phaser.GameObjects.Components.Visible#visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L31)  
> Since: 3.0.0

---

## w

### w: number

**Description:**

The w position of this Game Object.

**Overrides:** Phaser.GameObjects.Components.Transform#w

**Inherits:** [Phaser.GameObjects.Components.Transform#w](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L103)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The native (un-scaled) width of this Game Object.

Changing this value will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or use

the `displayWidth` property.

**Overrides:** Phaser.GameObjects.Components.Size#width

**Inherits:** [Phaser.GameObjects.Components.Size#width](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L27)  
> Since: 3.0.0

---

## world

### world: [Phaser.Physics.Matter.World](physics-matter-world.md)

**Description:**

A reference to the Matter.World instance that this body belongs to.

> Source: [src/physics/matter-js/MatterImage.js#L105](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterImage.js#L105)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x position of this Game Object.

**Overrides:** Phaser.GameObjects.Components.Transform#x

**Inherits:** [Phaser.GameObjects.Components.Transform#x](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L70)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of this Game Object.

**Overrides:** Phaser.GameObjects.Components.Transform#y

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

**Overrides:** Phaser.GameObjects.Components.Transform#z

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

**Overrides:** Phaser.GameObjects.Components.Alpha#\_alpha

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alpha](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L22](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L22)  
> Since: 3.0.0

---

## \_alphaBL

### \_alphaBL: number

**Description:**

Private internal value. Holds the bottom-left alpha value.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Alpha#\_alphaBL

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaBL](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L55)  
> Since: 3.0.0

---

## \_alphaBR

### \_alphaBR: number

**Description:**

Private internal value. Holds the bottom-right alpha value.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Alpha#\_alphaBR

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaBR](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L66)  
> Since: 3.0.0

---

## \_alphaTL

### \_alphaTL: number

**Description:**

Private internal value. Holds the top-left alpha value.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Alpha#\_alphaTL

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaTL](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L33)  
> Since: 3.0.0

---

## \_alphaTR

### \_alphaTR: number

**Description:**

Private internal value. Holds the top-right alpha value.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Alpha#\_alphaTR

**Inherits:** [Phaser.GameObjects.Components.Alpha#\_alphaTR](../namespace/gameobjects-components-alpha.md)

> Source: [src/gameobjects/components/Alpha.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Alpha.js#L44)  
> Since: 3.0.0

---

## \_blendMode

### \_blendMode: number

**Description:**

Private internal value. Holds the current blend mode.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.BlendMode#\_blendMode

**Inherits:** [Phaser.GameObjects.Components.BlendMode#\_blendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L19)  
> Since: 3.0.0

---

## \_crop

### \_crop: object

**Description:**

The internal crop data object, as used by `setCrop` and passed to the `Frame.setCropUVs` method.

**Access:** private

**Overrides:** Phaser.GameObjects.Image#\_crop

> Source: [src/physics/matter-js/MatterImage.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterImage.js#L91)  
> Since: 3.24.0

---

## \_depth

### \_depth: number

**Description:**

Private internal value. Holds the depth of the Game Object.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Depth#\_depth

**Inherits:** [Phaser.GameObjects.Components.Depth#\_depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L19)  
> Since: 3.0.0

---

## \_originComponent

### \_originComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Origin#\_originComponent

**Inherits:** [Phaser.GameObjects.Components.Origin#\_originComponent](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L19)  
> Since: 3.2.0

---

## \_rotation

### \_rotation: number

**Description:**

Private internal value. Holds the rotation value in radians.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Transform#\_rotation

**Inherits:** [Phaser.GameObjects.Components.Transform#\_rotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L59)  
> Since: 3.0.0

---

## \_scaleX

### \_scaleX: number

**Description:**

Private internal value. Holds the horizontal scale value.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Transform#\_scaleX

**Inherits:** [Phaser.GameObjects.Components.Transform#\_scaleX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L37)  
> Since: 3.0.0

---

## \_scaleY

### \_scaleY: number

**Description:**

Private internal value. Holds the vertical scale value.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Transform#\_scaleY

**Inherits:** [Phaser.GameObjects.Components.Transform#\_scaleY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L48)  
> Since: 3.0.0

---

## \_sizeComponent

### \_sizeComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Size#\_sizeComponent

**Inherits:** [Phaser.GameObjects.Components.Size#\_sizeComponent](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L16)  
> Since: 3.2.0

---

## \_tempVec2

### \_tempVec2: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

An internal temp vector used for velocity and force calculations.

**Access:** private

> Source: [src/physics/matter-js/MatterImage.js#L114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterImage.js#L114)  
> Since: 3.0.0

---

## \_visible

### \_visible: boolean

**Description:**

Private internal value. Holds the visible value.

**Access:** private

**Overrides:** Phaser.GameObjects.Components.Visible#\_visible

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - `this`.

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object.

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addToUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L735](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L735)  
> Since: 3.53.0

---

## applyForce

### <instance> applyForce(force)

**Description:**

Applies a force to a body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| force | [Phaser.Math.Vector2](math-vector2.md) | No | A Vector that specifies the force to apply. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Force#applyForce](../namespace/physics-matter-components-force.md)

> Source: [src/physics/matter-js/components/Force.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Force.js#L19)  
> Since: 3.0.0

---

## applyForceFrom

### <instance> applyForceFrom(position, force)

**Description:**

Applies a force to a body from a given position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| position | [Phaser.Math.Vector2](math-vector2.md) | No | The position in which the force comes from. |
| --- | --- | --- | --- |
| force | [Phaser.Math.Vector2](math-vector2.md) | No | A Vector that specifies the force to apply. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Force#applyForceFrom](../namespace/physics-matter-components-force.md)

> Source: [src/physics/matter-js/components/Force.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Force.js#L38)  
> Since: 3.0.0

---

## clearAlpha

### <instance> clearAlpha()

**Description:**

Clears all alpha values associated with this Game Object.

Immediately sets the alpha levels back to 1 (fully opaque).

**Overrides:** Phaser.GameObjects.Components.Alpha#clearAlpha

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#clearFX

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object.

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

**Overrides:** Phaser.GameObjects.Components.Mask#clearMask

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Tint#clearTint

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Transform#copyPosition

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Mask#createBitmapMask

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

**Overrides:** Phaser.GameObjects.Components.Mask#createGeometryMask

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This GameObject.

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

## getAngularSpeed

### <instance> getAngularSpeed()

**Description:**

Gets the current rotational speed of the body.

Equivalent to the magnitude of its angular velocity.

**Returns:** number - The current angular velocity of the body.

**Inherits:** [Phaser.Physics.Matter.Components.Velocity#getAngularSpeed](../namespace/physics-matter-components-velocity.md)

> Source: [src/physics/matter-js/components/Velocity.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Velocity.js#L137)  
> Since: 3.60.0

---

## getAngularVelocity

### <instance> getAngularVelocity()

**Description:**

Gets the current rotational velocity of the body.

**Returns:** number - The current angular velocity of the body.

**Inherits:** [Phaser.Physics.Matter.Components.Velocity#getAngularVelocity](../namespace/physics-matter-components-velocity.md)

> Source: [src/physics/matter-js/components/Velocity.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Velocity.js#L106)  
> Since: 3.60.0

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

**Overrides:** Phaser.GameObjects.Components.GetBounds#getBottomCenter

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

**Overrides:** Phaser.GameObjects.Components.GetBounds#getBottomLeft

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

**Overrides:** Phaser.GameObjects.Components.GetBounds#getBottomRight

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

**Overrides:** Phaser.GameObjects.Components.GetBounds#getBounds

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

**Overrides:** Phaser.GameObjects.Components.GetBounds#getCenter

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L54)  
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

**Overrides:** Phaser.GameObjects.Components.GetBounds#getLeftCenter

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

**Overrides:** Phaser.GameObjects.Components.Transform#getLocalPoint

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

**Overrides:** Phaser.GameObjects.Components.Transform#getLocalTransformMatrix

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

**Overrides:** Phaser.GameObjects.Components.Transform#getParentRotation

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

**Overrides:** Phaser.GameObjects.Components.Pipeline#getPipelineName

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#getPostPipeline

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

**Overrides:** Phaser.GameObjects.Components.GetBounds#getRightCenter

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getRightCenter](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L184](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L184)  
> Since: 3.18.0

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

**Overrides:** Phaser.GameObjects.Components.GetBounds#getTopCenter

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

**Overrides:** Phaser.GameObjects.Components.GetBounds#getTopLeft

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

**Overrides:** Phaser.GameObjects.Components.GetBounds#getTopRight

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The values stored in the output object.

**Inherits:** [Phaser.GameObjects.Components.GetBounds#getTopRight](../namespace/gameobjects-components-getbounds.md)

> Source: [src/gameobjects/components/GetBounds.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/GetBounds.js#L132)  
> Since: 3.0.0

---

## getVelocity

### <instance> getVelocity()

**Description:**

Gets the current linear velocity of the physics body.

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The current linear velocity of the body.

**Inherits:** [Phaser.Physics.Matter.Components.Velocity#getVelocity](../namespace/physics-matter-components-velocity.md)

> Source: [src/physics/matter-js/components/Velocity.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Velocity.js#L75)  
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

**Overrides:** Phaser.GameObjects.Components.Transform#getWorldTransformMatrix

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This GameObject.

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

**Overrides:** Phaser.GameObjects.Components.Pipeline#initPipeline

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#initPostPipeline

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#initPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L113)  
> Since: 3.60.0

---

## isSensor

### <instance> isSensor()

**Description:**

Is the body belonging to this Game Object a sensor or not?

**Returns:** boolean - `true` if the body is a sensor, otherwise `false`.

**Inherits:** [Phaser.Physics.Matter.Components.Sensor#isSensor](../namespace/physics-matter-components-sensor.md)

> Source: [src/physics/matter-js/components/Sensor.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Sensor.js#L33)  
> Since: 3.0.0

---

## isStatic

### <instance> isStatic()

**Description:**

Returns `true` if the body is static, otherwise `false` for a dynamic body.

**Returns:** boolean - `true` if the body is static, otherwise `false`.

**Inherits:** [Phaser.Physics.Matter.Components.Static#isStatic](../namespace/physics-matter-components-static.md)

> Source: [src/physics/matter-js/components/Static.js#L34](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Static.js#L34)  
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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - `this`.

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - `this`.

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - `this`.

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object.

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object.

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This GameObject.

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - `this`.

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#removePostPipeline

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#removePostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L299)  
> Since: 3.60.0

---

## resetFlip

### <instance> resetFlip()

**Description:**

Resets the horizontal and vertical flipped state of this Game Object back to their default un-flipped state.

**Overrides:** Phaser.GameObjects.Components.Flip#resetFlip

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#resetFlip](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L140)  
> Since: 3.0.0

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

**Overrides:** Phaser.GameObjects.Components.Pipeline#resetPipeline

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#resetPostPipeline

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

**Overrides:** Phaser.GameObjects.Components.Depth#setAbove

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This GameObject.

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

**Overrides:** Phaser.GameObjects.Components.Alpha#setAlpha

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Transform#setAngle

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setAngle](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L364](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L364)  
> Since: 3.0.0

---

## setAngularSpeed

### <instance> setAngularSpeed(speed)

**Description:**

Sets the current rotational speed of the body.

Direction is maintained. Affects body angular velocity.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| speed | number | No | The angular speed. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Velocity#setAngularSpeed](../namespace/physics-matter-components-velocity.md)

> Source: [src/physics/matter-js/components/Velocity.js#L119](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Velocity.js#L119)  
> Since: 3.60.0

---

## setAngularVelocity

### <instance> setAngularVelocity(velocity)

**Description:**

Sets the angular velocity of the body instantly.

Position, angle, force etc. are unchanged.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| velocity | number | No | The angular velocity. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Velocity#setAngularVelocity](../namespace/physics-matter-components-velocity.md)

> Source: [src/physics/matter-js/components/Velocity.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Velocity.js#L88)  
> Since: 3.0.0

---

## setAwake

### <instance> setAwake()

**Description:**

Wakes this Body if asleep.

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Sleep#setAwake](../namespace/physics-matter-components-sleep.md)

> Source: [src/physics/matter-js/components/Sleep.js#L34](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Sleep.js#L34)  
> Since: 3.22.0

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

**Overrides:** Phaser.GameObjects.Components.Depth#setBelow

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.BlendMode#setBlendMode

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#setBlendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L80)  
> Since: 3.0.0

---

## setBody

### <instance> setBody(config, [options])

**Description:**

Set this Game Object to create and use a new Body based on the configuration object given.

Calling this methods resets all previous properties you may have set on the body, including

plugins, mass, friction, collision categories, etc. So be sure to re-apply these as needed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | string | [Phaser.Types.Physics.Matter.MatterSetBodyConfig](../typedef/types-physics-matter.md) | No | Either a string, such as `circle`, or a Matter Set Body Configuration object. |
| --- | --- | --- | --- |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.SetBody#setBody](../namespace/physics-matter-components-setbody.md)

> Source: [src/physics/matter-js/components/SetBody.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/SetBody.js#L175)  
> Since: 3.0.0

---

## setBounce

### <instance> setBounce(value)

**Description:**

Sets the restitution on the physics object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | A Number that defines the restitution (elasticity) of the body. The value is always positive and is in the range (0, 1). A value of 0 means collisions may be perfectly inelastic and no bouncing may occur. A value of 0.8 means the body may bounce back with approximately 80% of its kinetic energy. Note that collision response is based on pairs of bodies, and that restitution values are combined with the following formula: `Math.max(bodyA.restitution, bodyB.restitution)` |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Bounce#setBounce](../namespace/physics-matter-components-bounce.md)

> Source: [src/physics/matter-js/components/Bounce.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Bounce.js#L15)  
> Since: 3.0.0

---

## setCircle

### <instance> setCircle(radius, [options])

**Description:**

Set this Game Objects Matter physics body to be a circle shape.

Calling this methods resets all previous properties you may have set on the body, including

plugins, mass, friction, collision categories, etc. So be sure to re-apply these as needed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| radius | number | No | The radius of the circle. |
| --- | --- | --- | --- |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.SetBody#setCircle](../namespace/physics-matter-components-setbody.md)

> Source: [src/physics/matter-js/components/SetBody.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/SetBody.js#L43)  
> Since: 3.0.0

---

## setCollidesWith

### <instance> setCollidesWith(categories)

**Description:**

Sets the collision mask for this Game Object's Matter Body. Two Matter Bodies with different collision groups will only

collide if each one includes the other's category in its mask based on a bitwise AND, i.e. `(categoryA & maskB) !== 0`

and `(categoryB & maskA) !== 0` are both true.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| categories | number | Array.<number> | No | A unique category bitfield, or an array of them. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Collision#setCollidesWith](../namespace/physics-matter-components-collision.md)

> Source: [src/physics/matter-js/components/Collision.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L54)  
> Since: 3.0.0

---

## setCollisionCategory

### <instance> setCollisionCategory(value)

**Description:**

Sets the collision category of this Game Object's Matter Body. This number must be a power of two between 2^0 (= 1) and 2^31.

Two bodies with different collision groups (see <#setCollisionGroup>) will only collide if their collision

categories are included in their collision masks (see <#setCollidesWith>).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | Unique category bitfield. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Collision#setCollisionCategory](../namespace/physics-matter-components-collision.md)

> Source: [src/physics/matter-js/components/Collision.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L15)  
> Since: 3.0.0

---

## setCollisionGroup

### <instance> setCollisionGroup(value)

**Description:**

Sets the collision group of this Game Object's Matter Body. If this is zero or two Matter Bodies have different values,

they will collide according to the usual rules (see <#setCollisionCategory> and <#setCollisionGroup>).

If two Matter Bodies have the same positive value, they will always collide; if they have the same negative value,

they will never collide.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | Unique group index. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Collision#setCollisionGroup](../namespace/physics-matter-components-collision.md)

> Source: [src/physics/matter-js/components/Collision.js#L34](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L34)  
> Since: 3.0.0

---

## setCrop

### <instance> setCrop([x], [y], [width], [height])

**Description:**

Applies a crop to a texture based Game Object, such as a Sprite or Image.

The crop is a rectangle that limits the area of the texture frame that is visible during rendering.

Cropping a Game Object does not change its size, dimensions, physics body or hit area, it just

changes what is shown when rendered.

The crop size as well as coordinates can not exceed the the size of the texture frame.

The crop coordinates are relative to the texture frame, not the Game Object, meaning 0 x 0 is the top-left.

Therefore, if you had a Game Object that had an 800x600 sized texture, and you wanted to show only the left

half of it, you could call `setCrop(0, 0, 400, 600)`.

It is also scaled to match the Game Object scale automatically. Therefore a crop rectangle of 100x50 would crop

an area of 200x100 when applied to a Game Object that had a scale factor of 2.

You can either pass in numeric values directly, or you can provide a single Rectangle object as the first argument.

Call this method with no arguments at all to reset the crop, or toggle the property `isCropped` to `false`.

You should do this if the crop rectangle becomes the same size as the frame itself, as it will allow

the renderer to skip several internal calculations.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | The x coordinate to start the crop from. Cannot be negative or exceed the Frame width. Or a Phaser.Geom.Rectangle object, in which case the rest of the arguments are ignored. |
| --- | --- | --- | --- |
| y | number | Yes | The y coordinate to start the crop from. Cannot be negative or exceed the Frame height. |
| width | number | Yes | The width of the crop rectangle in pixels. Cannot exceed the Frame width. |
| height | number | Yes | The height of the crop rectangle in pixels. Cannot exceed the Frame height. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#setCrop](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L50)  
> Since: 3.11.0

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L295)  
> Since: 3.0.0

---

## setDataEnabled

### <instance> setDataEnabled()

**Description:**

Adds a Data Manager component to this Game Object.

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setDataEnabled](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L276)  
> Since: 3.0.0

---

## setDensity

### <instance> setDensity(value)

**Description:**

Sets density of the body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new density of the body. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Mass#setDensity](../namespace/physics-matter-components-mass.md)

> Source: [src/physics/matter-js/components/Mass.js#L35](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Mass.js#L35)  
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

**Overrides:** Phaser.GameObjects.Components.Depth#setDepth

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Origin#setDisplayOrigin

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setDisplayOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L159)  
> Since: 3.0.0

---

## setDisplaySize

### <instance> setDisplaySize(width, height)

**Description:**

Sets the display size of this Game Object.

Calling this will adjust the scale.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of this Game Object. |
| --- | --- | --- | --- |
| height | number | No | The height of this Game Object. |

**Overrides:** Phaser.GameObjects.Components.Size#setDisplaySize

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Size#setDisplaySize](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L166)  
> Since: 3.0.0

---

## setExistingBody

### <instance> setExistingBody(body, [addToWorld])

**Description:**

Set this Game Object to use the given existing Matter Body.

The body is first removed from the world before being added to this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| body | MatterJS.BodyType | No |  | The Body this Game Object should use. |
| --- | --- | --- | --- | --- |
| addToWorld | boolean | Yes | true | Should the body be immediately added to the World? |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.SetBody#setExistingBody](../namespace/physics-matter-components-setbody.md)

> Source: [src/physics/matter-js/components/SetBody.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/SetBody.js#L103)  
> Since: 3.0.0

---

## setFixedRotation

### <instance> setFixedRotation()

**Description:**

Setting fixed rotation sets the Body inertia to Infinity, which stops it

from being able to rotate when forces are applied to it.

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Transform#setFixedRotation](../namespace/physics-matter-components-transform.md)

> Source: [src/physics/matter-js/components/Transform.js#L239](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L239)  
> Since: 3.0.0

---

## setFlip

### <instance> setFlip(x, y)

**Description:**

Sets the horizontal and vertical flipped state of this Game Object.

A Game Object that is flipped will render inversed on the flipped axis.

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | boolean | No | The horizontal flipped state. `false` for no flip, or `true` to be flipped. |
| --- | --- | --- | --- |
| y | boolean | No | The horizontal flipped state. `false` for no flip, or `true` to be flipped. |

**Overrides:** Phaser.GameObjects.Components.Flip#setFlip

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#setFlip](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L117)  
> Since: 3.0.0

---

## setFlipX

### <instance> setFlipX(value)

**Description:**

Sets the horizontal flipped state of this Game Object.

A Game Object that is flipped horizontally will render inversed on the horizontal axis.

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The flipped state. `false` for no flip, or `true` to be flipped. |
| --- | --- | --- | --- |

**Overrides:** Phaser.GameObjects.Components.Flip#setFlipX

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#setFlipX](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L79)  
> Since: 3.0.0

---

## setFlipY

### <instance> setFlipY(value)

**Description:**

Sets the vertical flipped state of this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The flipped state. `false` for no flip, or `true` to be flipped. |
| --- | --- | --- | --- |

**Overrides:** Phaser.GameObjects.Components.Flip#setFlipY

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#setFlipY](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L100)  
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

**Overrides:** Phaser.GameObjects.Components.Texture#setFrame

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#setFrame](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L130)  
> Since: 3.0.0

---

## setFriction

### <instance> setFriction(value, [air], [fstatic])

**Description:**

Sets new friction values for this Game Object's Matter Body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new friction of the body, between 0 and 1, where 0 allows the Body to slide indefinitely, while 1 allows it to stop almost immediately after a force is applied. |
| --- | --- | --- | --- |
| air | number | Yes | If provided, the new air resistance of the Body. The higher the value, the faster the Body will slow as it moves through space. 0 means the body has no air resistance. |
| fstatic | number | Yes | If provided, the new static friction of the Body. The higher the value (e.g. 10), the more force it will take to initially get the Body moving when it is nearly stationary. 0 means the body will never "stick" when it is nearly stationary. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Friction#setFriction](../namespace/physics-matter-components-friction.md)

> Source: [src/physics/matter-js/components/Friction.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Friction.js#L15)  
> Since: 3.0.0

---

## setFrictionAir

### <instance> setFrictionAir(value)

**Description:**

Sets a new air resistance for this Game Object's Matter Body.

A value of 0 means the Body will never slow as it moves through space.

The higher the value, the faster a Body slows when moving through space.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new air resistance for the Body. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Friction#setFrictionAir](../namespace/physics-matter-components-friction.md)

> Source: [src/physics/matter-js/components/Friction.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Friction.js#L44)  
> Since: 3.0.0

---

## setFrictionStatic

### <instance> setFrictionStatic(value)

**Description:**

Sets a new static friction for this Game Object's Matter Body.

A value of 0 means the Body will never "stick" when it is nearly stationary.

The higher the value (e.g. 10), the more force it will take to initially get the Body moving when it is nearly stationary.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new static friction for the Body. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Friction#setFrictionStatic](../namespace/physics-matter-components-friction.md)

> Source: [src/physics/matter-js/components/Friction.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Friction.js#L63)  
> Since: 3.0.0

---

## setIgnoreGravity

### <instance> setIgnoreGravity(value)

**Description:**

A togglable function for ignoring world gravity in real-time on the current body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | Set to true to ignore the effect of world gravity, or false to not ignore it. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Gravity#setIgnoreGravity](../namespace/physics-matter-components-gravity.md)

> Source: [src/physics/matter-js/components/Gravity.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Gravity.js#L15)  
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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This GameObject.

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

**Overrides:** Phaser.GameObjects.Components.Mask#setMask

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#setMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L28](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L28)  
> Since: 3.6.2

---

## setMass

### <instance> setMass(value)

**Description:**

Sets the mass of the Game Object's Matter Body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new mass of the body. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Mass#setMass](../namespace/physics-matter-components-mass.md)

> Source: [src/physics/matter-js/components/Mass.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Mass.js#L18)  
> Since: 3.0.0

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setName](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L234)  
> Since: 3.0.0

---

## setOnCollide

### <instance> setOnCollide(callback)

**Description:**

The callback is sent a `Phaser.Types.Physics.Matter.MatterCollisionData` object.

This does not change the bodies collision category, group or filter. Those must be set in addition

to the callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The callback to invoke when this body starts colliding with another. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Collision#setOnCollide](../namespace/physics-matter-components-collision.md)

> Source: [src/physics/matter-js/components/Collision.js#L87](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L87)  
> Since: 3.22.0

---

## setOnCollideActive

### <instance> setOnCollideActive(callback)

**Description:**

The callback is sent a `Phaser.Types.Physics.Matter.MatterCollisionData` object.

This does not change the bodies collision category, group or filter. Those must be set in addition

to the callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The callback to invoke for the duration of this body colliding with another. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Collision#setOnCollideActive](../namespace/physics-matter-components-collision.md)

> Source: [src/physics/matter-js/components/Collision.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L127)  
> Since: 3.22.0

---

## setOnCollideEnd

### <instance> setOnCollideEnd(callback)

**Description:**

The callback is sent a `Phaser.Types.Physics.Matter.MatterCollisionData` object.

This does not change the bodies collision category, group or filter. Those must be set in addition

to the callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The callback to invoke when this body stops colliding with another. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Collision#setOnCollideEnd](../namespace/physics-matter-components-collision.md)

> Source: [src/physics/matter-js/components/Collision.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L107)  
> Since: 3.22.0

---

## setOnCollideWith

### <instance> setOnCollideWith(body, callback)

**Description:**

The callback is sent a reference to the other body, along with a `Phaser.Types.Physics.Matter.MatterCollisionData` object.

This does not change the bodies collision category, group or filter. Those must be set in addition

to the callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | MatterJS.Body | Array.<MatterJS.Body> | No | The body, or an array of bodies, to test for collisions with. |
| --- | --- | --- | --- |
| callback | function | No | The callback to invoke when this body collides with the given body or bodies. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Collision#setOnCollideWith](../namespace/physics-matter-components-collision.md)

> Source: [src/physics/matter-js/components/Collision.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L147)  
> Since: 3.22.0

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

**Overrides:** Phaser.GameObjects.Components.Origin#setOrigin

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L112)  
> Since: 3.0.0

---

## setOriginFromFrame

### <instance> setOriginFromFrame()

**Description:**

Sets the origin of this Game Object based on the Pivot values in its Frame.

**Overrides:** Phaser.GameObjects.Components.Origin#setOriginFromFrame

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Pipeline#setPipeline

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Pipeline#setPipelineData

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#setPipelineData](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L144)  
> Since: 3.50.0

---

## setPolygon

### <instance> setPolygon(radius, sides, [options])

**Description:**

Set this Game Objects Matter physics body to be a polygon shape.

Calling this methods resets all previous properties you may have set on the body, including

plugins, mass, friction, collision categories, etc. So be sure to re-apply these as needed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| radius | number | No | The "radius" of the polygon, i.e. the distance from its center to any vertex. This is also the radius of its circumcircle. |
| --- | --- | --- | --- |
| sides | number | No | The number of sides the polygon will have. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.SetBody#setPolygon](../namespace/physics-matter-components-setbody.md)

> Source: [src/physics/matter-js/components/SetBody.js#L62](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/SetBody.js#L62)  
> Since: 3.0.0

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

**Overrides:** Phaser.GameObjects.Components.Transform#setPosition

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#setPostPipeline

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.PostPipeline#setPostPipelineData

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Transform#setRandomPosition

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRandomPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L313](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L313)  
> Since: 3.8.0

---

## setRectangle

### <instance> setRectangle(width, height, [options])

**Description:**

Set this Game Objects Matter physics body to be a rectangle shape.

Calling this methods resets all previous properties you may have set on the body, including

plugins, mass, friction, collision categories, etc. So be sure to re-apply these as needed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | Width of the rectangle. |
| --- | --- | --- | --- |
| height | number | No | Height of the rectangle. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.SetBody#setRectangle](../namespace/physics-matter-components-setbody.md)

> Source: [src/physics/matter-js/components/SetBody.js#L23](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/SetBody.js#L23)  
> Since: 3.0.0

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

**Overrides:** Phaser.GameObjects.Components.Transform#setRotation

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Transform#setScale

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.ScrollFactor#setScrollFactor

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#setScrollFactor](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L64)  
> Since: 3.0.0

---

## setSensor

### <instance> setSensor(value)

**Description:**

Set the body belonging to this Game Object to be a sensor.

Sensors trigger collision events, but don't react with colliding body physically.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to set the body as a sensor, or `false` to disable it. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Sensor#setSensor](../namespace/physics-matter-components-sensor.md)

> Source: [src/physics/matter-js/components/Sensor.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Sensor.js#L15)  
> Since: 3.0.0

---

## setSize

### <instance> setSize(width, height)

**Description:**

Sets the internal size of this Game Object, as used for frame or physics body creation.

This will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or call the

`setDisplaySize` method, which is the same thing as changing the scale but allows you

to do so by giving pixel values.

If you have enabled this Game Object for input, changing the size will *not* change the

size of the hit area. To do this you should adjust the `input.hitArea` object directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of this Game Object. |
| --- | --- | --- | --- |
| height | number | No | The height of this Game Object. |

**Overrides:** Phaser.GameObjects.Components.Size#setSize

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Size#setSize](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L139)  
> Since: 3.0.0

---

## setSizeToFrame

### <instance> setSizeToFrame([frame])

**Description:**

Sets the size of this Game Object to be that of the given Frame.

This will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or call the

`setDisplaySize` method, which is the same thing as changing the scale but allows you

to do so by giving pixel values.

If you have enabled this Game Object for input, changing the size will *not* change the

size of the hit area. To do this you should adjust the `input.hitArea` object directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| frame | [Phaser.Textures.Frame](textures-frame.md) | boolean | Yes | The frame to base the size of this Game Object on. |
| --- | --- | --- | --- |

**Overrides:** Phaser.GameObjects.Components.Size#setSizeToFrame

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Size#setSizeToFrame](../namespace/gameobjects-components-size.md)

> Source: [src/gameobjects/components/Size.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Size.js#L103)  
> Since: 3.0.0

---

## setSleepEndEvent

### <instance> setSleepEndEvent(value)

**Description:**

Enables or disables the Sleep End event for this body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to enable the sleep event, or `false` to disable it. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Sleep#setSleepEndEvent](../namespace/physics-matter-components-sleep.md)

> Source: [src/physics/matter-js/components/Sleep.js#L121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Sleep.js#L121)  
> Since: 3.0.0

---

## setSleepEvents

### <instance> setSleepEvents(start, end)

**Description:**

Enable sleep and wake events for this body.

By default when a body goes to sleep, or wakes up, it will not emit any events.

The events are emitted by the Matter World instance and can be listened to via

the `SLEEP_START` and `SLEEP_END` events.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| start | boolean | No | `true` if you want the sleep start event to be emitted for this body. |
| --- | --- | --- | --- |
| end | boolean | No | `true` if you want the sleep end event to be emitted for this body. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Sleep#setSleepEvents](../namespace/physics-matter-components-sleep.md)

> Source: [src/physics/matter-js/components/Sleep.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Sleep.js#L68)  
> Since: 3.0.0

---

## setSleepStartEvent

### <instance> setSleepStartEvent(value)

**Description:**

Enables or disables the Sleep Start event for this body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to enable the sleep event, or `false` to disable it. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Sleep#setSleepStartEvent](../namespace/physics-matter-components-sleep.md)

> Source: [src/physics/matter-js/components/Sleep.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Sleep.js#L92)  
> Since: 3.0.0

---

## setSleepThreshold

### <instance> setSleepThreshold([value])

**Description:**

Sets the number of updates in which this body must have near-zero velocity before it is set as sleeping (if sleeping is enabled by the engine).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 60 | A `Number` that defines the number of updates in which this body must have near-zero velocity before it is set as sleeping. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Sleep#setSleepThreshold](../namespace/physics-matter-components-sleep.md)

> Source: [src/physics/matter-js/components/Sleep.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Sleep.js#L49)  
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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setState](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L252)  
> Since: 3.16.0

---

## setStatic

### <instance> setStatic(value)

**Description:**

Changes the physics body to be either static `true` or dynamic `false`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to set the body as being static, or `false` to make it dynamic. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Static#setStatic](../namespace/physics-matter-components-static.md)

> Source: [src/physics/matter-js/components/Static.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Static.js#L17)  
> Since: 3.0.0

---

## setTexture

### <instance> setTexture(key, [frame])

**Description:**

Sets the texture and frame this Game Object will use to render with.

Textures are referenced by their string-based keys, as stored in the Texture Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the texture to be used, as stored in the Texture Manager. |
| --- | --- | --- | --- |
| frame | string | number | Yes | The name or index of the frame within the Texture. |

**Overrides:** Phaser.GameObjects.Components.Texture#setTexture

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#setTexture](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L110)  
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

**Overrides:** Phaser.GameObjects.Components.Tint#setTint

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Tint#setTintFill

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Depth#setToBack

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToBack](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L115)  
> Since: 3.85.0

---

## setToSleep

### <instance> setToSleep()

**Description:**

Sets this Body to sleep.

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Sleep#setToSleep](../namespace/physics-matter-components-sleep.md)

> Source: [src/physics/matter-js/components/Sleep.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Sleep.js#L19)  
> Since: 3.22.0

---

## setToTop

### <instance> setToTop()

**Description:**

Sets this Game Object to be at the top of the display list, or the top of its parent container.

Being at the top means it will render on-top of everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Overrides:** Phaser.GameObjects.Components.Depth#setToTop

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToTop](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L91)  
> Since: 3.85.0

---

## setTrapezoid

### <instance> setTrapezoid(width, height, slope, [options])

**Description:**

Set this Game Objects Matter physics body to be a trapezoid shape.

Calling this methods resets all previous properties you may have set on the body, including

plugins, mass, friction, collision categories, etc. So be sure to re-apply these as needed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of the trapezoid Body. |
| --- | --- | --- | --- |
| height | number | No | The height of the trapezoid Body. |
| slope | number | No | The slope of the trapezoid. 0 creates a rectangle, while 1 creates a triangle. Positive values make the top side shorter, while negative values make the bottom side shorter. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.SetBody#setTrapezoid](../namespace/physics-matter-components-setbody.md)

> Source: [src/physics/matter-js/components/SetBody.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/SetBody.js#L82)  
> Since: 3.0.0

---

## setVelocity

### <instance> setVelocity(x, [y])

**Description:**

Sets both the horizontal and vertical velocity of the physics body.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal velocity value. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical velocity value, it can be either positive or negative. If not given, it will be the same as the `x` value. |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Velocity#setVelocity](../namespace/physics-matter-components-velocity.md)

> Source: [src/physics/matter-js/components/Velocity.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Velocity.js#L55)  
> Since: 3.0.0

---

## setVelocityX

### <instance> setVelocityX(x)

**Description:**

Sets the horizontal velocity of the physics body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal velocity value. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Velocity#setVelocityX](../namespace/physics-matter-components-velocity.md)

> Source: [src/physics/matter-js/components/Velocity.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Velocity.js#L17)  
> Since: 3.0.0

---

## setVelocityY

### <instance> setVelocityY(y)

**Description:**

Sets vertical velocity of the physics body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| y | number | No | The vertical velocity value. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Velocity#setVelocityY](../namespace/physics-matter-components-velocity.md)

> Source: [src/physics/matter-js/components/Velocity.js#L36](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Velocity.js#L36)  
> Since: 3.0.0

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

**Overrides:** Phaser.GameObjects.Components.Visible#setVisible

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Transform#setW

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Transform#setX

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Transform#setY

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

**Overrides:** Phaser.GameObjects.Components.Transform#setZ

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

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

## thrust

### <instance> thrust(speed)

**Description:**

Apply thrust to the forward position of the body.

Use very small values, such as 0.1, depending on the mass and required speed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| speed | number | No | A speed value to be applied to a directional force. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Force#thrust](../namespace/physics-matter-components-force.md)

> Source: [src/physics/matter-js/components/Force.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Force.js#L56)  
> Since: 3.0.0

---

## thrustBack

### <instance> thrustBack(speed)

**Description:**

Apply thrust to the back position of the body.

Use very small values, such as 0.1, depending on the mass and required speed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| speed | number | No | A speed value to be applied to a directional force. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Force#thrustBack](../namespace/physics-matter-components-force.md)

> Source: [src/physics/matter-js/components/Force.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Force.js#L125)  
> Since: 3.0.0

---

## thrustLeft

### <instance> thrustLeft(speed)

**Description:**

Apply thrust to the left position of the body.

Use very small values, such as 0.1, depending on the mass and required speed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| speed | number | No | A speed value to be applied to a directional force. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Force#thrustLeft](../namespace/physics-matter-components-force.md)

> Source: [src/physics/matter-js/components/Force.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Force.js#L79)  
> Since: 3.0.0

---

## thrustRight

### <instance> thrustRight(speed)

**Description:**

Apply thrust to the right position of the body.

Use very small values, such as 0.1, depending on the mass and required speed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| speed | number | No | A speed value to be applied to a directional force. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.Physics.Matter.Components.Force#thrustRight](../namespace/physics-matter-components-force.md)

> Source: [src/physics/matter-js/components/Force.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Force.js#L102)  
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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#toggleData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L387)  
> Since: 3.23.0

---

## toggleFlipX

### <instance> toggleFlipX()

**Description:**

Toggles the horizontal flipped state of this Game Object.

A Game Object that is flipped horizontally will render inversed on the horizontal axis.

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Overrides:** Phaser.GameObjects.Components.Flip#toggleFlipX

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#toggleFlipX](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L45)  
> Since: 3.0.0

---

## toggleFlipY

### <instance> toggleFlipY()

**Description:**

Toggles the vertical flipped state of this Game Object.

**Overrides:** Phaser.GameObjects.Components.Flip#toggleFlipY

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#toggleFlipY](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L64)  
> Since: 3.0.0

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

**Returns:** [Phaser.Physics.Matter.Image](physics-matter-image.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#updateDisplayOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L182)  
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

**Overrides:** Phaser.GameObjects.Components.GetBounds#prepareBoundsOutput

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
| src | [Phaser.GameObjects.Image](gameobjects-image.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

**Inherits:** [Phaser.GameObjects.Image#renderCanvas](gameobjects-image.md)

> Source: [src/gameobjects/image/ImageCanvasRenderer.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/image/ImageCanvasRenderer.js#L7)  
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
| src | [Phaser.GameObjects.Image](gameobjects-image.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

**Inherits:** [Phaser.GameObjects.Image#renderWebGL](gameobjects-image.md)

> Source: [src/gameobjects/image/ImageWebGLRenderer.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/image/ImageWebGLRenderer.js#L7)  
> Since: 3.0.0

---

## resetCropObject

### <instance> resetCropObject()

**Description:**

Internal method that returns a blank, well-formed crop object for use by a Game Object.

**Access:** private

**Returns:** object - The crop object.

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#resetCropObject](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L201](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L201)  
> Since: 3.12.0

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
  + [centerOfMass](#centerofmass)

    - [centerOfMass: Phaser.Math.Vector2](#centerofmass-phasermathvector2)
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
  + [flipX](#flipx)

    - [flipX: boolean](#flipx-boolean)
  + [flipY](#flipy)

    - [flipY: boolean](#flipy-boolean)
  + [frame](#frame)

    - [frame: Phaser.Textures.Frame](#frame-phasertexturesframe)
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
  + [isCropped](#iscropped)

    - [isCropped: boolean](#iscropped-boolean)
  + [isTinted](#istinted)

    - [isTinted: boolean](#istinted-boolean)
  + [mask](#mask)

    - [mask: Phaser.Display.Masks.BitmapMask, Phaser.Display.Masks.GeometryMask](#mask-phaserdisplaymasksbitmapmask-phaserdisplaymasksgeometrymask)
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
  + [world](#world)

    - [world: Phaser.Physics.Matter.World](#world-phaserphysicsmatterworld)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
  + [z](#z)

    - [z: number](#z-number)
* [Private Members](#private-members)

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
  + [\_crop](#_crop)

    - [\_crop: object](#_crop-object)
  + [\_depth](#_depth)

    - [\_depth: number](#_depth-number)
  + [\_originComponent](#_origincomponent)

    - [\_originComponent: boolean](#_origincomponent-boolean)
  + [\_rotation](#_rotation)

    - [\_rotation: number](#_rotation-number)
  + [\_scaleX](#_scalex)

    - [\_scaleX: number](#_scalex-number)
  + [\_scaleY](#_scaley)

    - [\_scaleY: number](#_scaley-number)
  + [\_sizeComponent](#_sizecomponent)

    - [\_sizeComponent: boolean](#_sizecomponent-boolean)
  + [\_tempVec2](#_tempvec2)

    - [\_tempVec2: Phaser.Math.Vector2](#_tempvec2-phasermathvector2)
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
  + [applyForce](#applyforce)

    - [<instance> applyForce(force)](#instance-applyforceforce)
  + [applyForceFrom](#applyforcefrom)

    - [<instance> applyForceFrom(position, force)](#instance-applyforcefromposition-force)
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
  + [getAngularSpeed](#getangularspeed)

    - [<instance> getAngularSpeed()](#instance-getangularspeed)
  + [getAngularVelocity](#getangularvelocity)

    - [<instance> getAngularVelocity()](#instance-getangularvelocity)
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
  + [getTopCenter](#gettopcenter)

    - [<instance> getTopCenter([output], [includeParent])](#instance-gettopcenteroutput-includeparent)
  + [getTopLeft](#gettopleft)

    - [<instance> getTopLeft([output], [includeParent])](#instance-gettopleftoutput-includeparent)
  + [getTopRight](#gettopright)

    - [<instance> getTopRight([output], [includeParent])](#instance-gettoprightoutput-includeparent)
  + [getVelocity](#getvelocity)

    - [<instance> getVelocity()](#instance-getvelocity)
  + [getWorldTransformMatrix](#getworldtransformmatrix)

    - [<instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])](#instance-getworldtransformmatrixtempmatrix-parentmatrix)
  + [incData](#incdata)

    - [<instance> incData(key, [amount])](#instance-incdatakey-amount)
  + [initPipeline](#initpipeline)

    - [<instance> initPipeline([pipeline])](#instance-initpipelinepipeline)
  + [initPostPipeline](#initpostpipeline)

    - [<instance> initPostPipeline([preFX])](#instance-initpostpipelineprefx)
  + [isSensor](#issensor)

    - [<instance> isSensor()](#instance-issensor)
  + [isStatic](#isstatic)

    - [<instance> isStatic()](#instance-isstatic)
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
  + [resetFlip](#resetflip)

    - [<instance> resetFlip()](#instance-resetflip)
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
  + [setAngularSpeed](#setangularspeed)

    - [<instance> setAngularSpeed(speed)](#instance-setangularspeedspeed)
  + [setAngularVelocity](#setangularvelocity)

    - [<instance> setAngularVelocity(velocity)](#instance-setangularvelocityvelocity)
  + [setAwake](#setawake)

    - [<instance> setAwake()](#instance-setawake)
  + [setBelow](#setbelow)

    - [<instance> setBelow(gameObject)](#instance-setbelowgameobject)
  + [setBlendMode](#setblendmode)

    - [<instance> setBlendMode(value)](#instance-setblendmodevalue)
  + [setBody](#setbody)

    - [<instance> setBody(config, [options])](#instance-setbodyconfig-options)
  + [setBounce](#setbounce)

    - [<instance> setBounce(value)](#instance-setbouncevalue)
  + [setCircle](#setcircle)

    - [<instance> setCircle(radius, [options])](#instance-setcircleradius-options)
  + [setCollidesWith](#setcollideswith)

    - [<instance> setCollidesWith(categories)](#instance-setcollideswithcategories)
  + [setCollisionCategory](#setcollisioncategory)

    - [<instance> setCollisionCategory(value)](#instance-setcollisioncategoryvalue)
  + [setCollisionGroup](#setcollisiongroup)

    - [<instance> setCollisionGroup(value)](#instance-setcollisiongroupvalue)
  + [setCrop](#setcrop)

    - [<instance> setCrop([x], [y], [width], [height])](#instance-setcropx-y-width-height)
  + [setData](#setdata)

    - [<instance> setData(key, [data])](#instance-setdatakey-data)
  + [setDataEnabled](#setdataenabled)

    - [<instance> setDataEnabled()](#instance-setdataenabled)
  + [setDensity](#setdensity)

    - [<instance> setDensity(value)](#instance-setdensityvalue)
  + [setDepth](#setdepth)

    - [<instance> setDepth(value)](#instance-setdepthvalue)
  + [setDisplayOrigin](#setdisplayorigin)

    - [<instance> setDisplayOrigin([x], [y])](#instance-setdisplayoriginx-y)
  + [setDisplaySize](#setdisplaysize)

    - [<instance> setDisplaySize(width, height)](#instance-setdisplaysizewidth-height)
  + [setExistingBody](#setexistingbody)

    - [<instance> setExistingBody(body, [addToWorld])](#instance-setexistingbodybody-addtoworld)
  + [setFixedRotation](#setfixedrotation)

    - [<instance> setFixedRotation()](#instance-setfixedrotation)
  + [setFlip](#setflip)

    - [<instance> setFlip(x, y)](#instance-setflipx-y)
  + [setFlipX](#setflipx)

    - [<instance> setFlipX(value)](#instance-setflipxvalue)
  + [setFlipY](#setflipy)

    - [<instance> setFlipY(value)](#instance-setflipyvalue)
  + [setFrame](#setframe)

    - [<instance> setFrame(frame, [updateSize], [updateOrigin])](#instance-setframeframe-updatesize-updateorigin)
  + [setFriction](#setfriction)

    - [<instance> setFriction(value, [air], [fstatic])](#instance-setfrictionvalue-air-fstatic)
  + [setFrictionAir](#setfrictionair)

    - [<instance> setFrictionAir(value)](#instance-setfrictionairvalue)
  + [setFrictionStatic](#setfrictionstatic)

    - [<instance> setFrictionStatic(value)](#instance-setfrictionstaticvalue)
  + [setIgnoreGravity](#setignoregravity)

    - [<instance> setIgnoreGravity(value)](#instance-setignoregravityvalue)
  + [setInteractive](#setinteractive)

    - [<instance> setInteractive([hitArea], [callback], [dropZone])](#instance-setinteractivehitarea-callback-dropzone)
  + [setMask](#setmask)

    - [<instance> setMask(mask)](#instance-setmaskmask)
  + [setMass](#setmass)

    - [<instance> setMass(value)](#instance-setmassvalue)
  + [setName](#setname)

    - [<instance> setName(value)](#instance-setnamevalue)
  + [setOnCollide](#setoncollide)

    - [<instance> setOnCollide(callback)](#instance-setoncollidecallback)
  + [setOnCollideActive](#setoncollideactive)

    - [<instance> setOnCollideActive(callback)](#instance-setoncollideactivecallback)
  + [setOnCollideEnd](#setoncollideend)

    - [<instance> setOnCollideEnd(callback)](#instance-setoncollideendcallback)
  + [setOnCollideWith](#setoncollidewith)

    - [<instance> setOnCollideWith(body, callback)](#instance-setoncollidewithbody-callback)
  + [setOrigin](#setorigin)

    - [<instance> setOrigin([x], [y])](#instance-setoriginx-y)
  + [setOriginFromFrame](#setoriginfromframe)

    - [<instance> setOriginFromFrame()](#instance-setoriginfromframe)
  + [setPipeline](#setpipeline)

    - [<instance> setPipeline(pipeline, [pipelineData], [copyData])](#instance-setpipelinepipeline-pipelinedata-copydata)
  + [setPipelineData](#setpipelinedata)

    - [<instance> setPipelineData(key, [value])](#instance-setpipelinedatakey-value)
  + [setPolygon](#setpolygon)

    - [<instance> setPolygon(radius, sides, [options])](#instance-setpolygonradius-sides-options)
  + [setPosition](#setposition)

    - [<instance> setPosition([x], [y], [z], [w])](#instance-setpositionx-y-z-w)
  + [setPostPipeline](#setpostpipeline)

    - [<instance> setPostPipeline(pipelines, [pipelineData], [copyData])](#instance-setpostpipelinepipelines-pipelinedata-copydata)
  + [setPostPipelineData](#setpostpipelinedata)

    - [<instance> setPostPipelineData(key, [value])](#instance-setpostpipelinedatakey-value)
  + [setRandomPosition](#setrandomposition)

    - [<instance> setRandomPosition([x], [y], [width], [height])](#instance-setrandompositionx-y-width-height)
  + [setRectangle](#setrectangle)

    - [<instance> setRectangle(width, height, [options])](#instance-setrectanglewidth-height-options)
  + [setRotation](#setrotation)

    - [<instance> setRotation([radians])](#instance-setrotationradians)
  + [setScale](#setscale)

    - [<instance> setScale([x], [y])](#instance-setscalex-y)
  + [setScrollFactor](#setscrollfactor)

    - [<instance> setScrollFactor(x, [y])](#instance-setscrollfactorx-y)
  + [setSensor](#setsensor)

    - [<instance> setSensor(value)](#instance-setsensorvalue)
  + [setSize](#setsize)

    - [<instance> setSize(width, height)](#instance-setsizewidth-height)
  + [setSizeToFrame](#setsizetoframe)

    - [<instance> setSizeToFrame([frame])](#instance-setsizetoframeframe)
  + [setSleepEndEvent](#setsleependevent)

    - [<instance> setSleepEndEvent(value)](#instance-setsleependeventvalue)
  + [setSleepEvents](#setsleepevents)

    - [<instance> setSleepEvents(start, end)](#instance-setsleepeventsstart-end)
  + [setSleepStartEvent](#setsleepstartevent)

    - [<instance> setSleepStartEvent(value)](#instance-setsleepstarteventvalue)
  + [setSleepThreshold](#setsleepthreshold)

    - [<instance> setSleepThreshold([value])](#instance-setsleepthresholdvalue)
  + [setState](#setstate)

    - [<instance> setState(value)](#instance-setstatevalue)
  + [setStatic](#setstatic)

    - [<instance> setStatic(value)](#instance-setstaticvalue)
  + [setTexture](#settexture)

    - [<instance> setTexture(key, [frame])](#instance-settexturekey-frame)
  + [setTint](#settint)

    - [<instance> setTint([topLeft], [topRight], [bottomLeft], [bottomRight])](#instance-settinttopleft-topright-bottomleft-bottomright)
  + [setTintFill](#settintfill)

    - [<instance> setTintFill([topLeft], [topRight], [bottomLeft], [bottomRight])](#instance-settintfilltopleft-topright-bottomleft-bottomright)
  + [setToBack](#settoback)

    - [<instance> setToBack()](#instance-settoback)
  + [setToSleep](#settosleep)

    - [<instance> setToSleep()](#instance-settosleep)
  + [setToTop](#settotop)

    - [<instance> setToTop()](#instance-settotop)
  + [setTrapezoid](#settrapezoid)

    - [<instance> setTrapezoid(width, height, slope, [options])](#instance-settrapezoidwidth-height-slope-options)
  + [setVelocity](#setvelocity)

    - [<instance> setVelocity(x, [y])](#instance-setvelocityx-y)
  + [setVelocityX](#setvelocityx)

    - [<instance> setVelocityX(x)](#instance-setvelocityxx)
  + [setVelocityY](#setvelocityy)

    - [<instance> setVelocityY(y)](#instance-setvelocityyy)
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
  + [thrust](#thrust)

    - [<instance> thrust(speed)](#instance-thrustspeed)
  + [thrustBack](#thrustback)

    - [<instance> thrustBack(speed)](#instance-thrustbackspeed)
  + [thrustLeft](#thrustleft)

    - [<instance> thrustLeft(speed)](#instance-thrustleftspeed)
  + [thrustRight](#thrustright)

    - [<instance> thrustRight(speed)](#instance-thrustrightspeed)
  + [toggleData](#toggledata)

    - [<instance> toggleData(key)](#instance-toggledatakey)
  + [toggleFlipX](#toggleflipx)

    - [<instance> toggleFlipX()](#instance-toggleflipx)
  + [toggleFlipY](#toggleflipy)

    - [<instance> toggleFlipY()](#instance-toggleflipy)
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
  + [resetCropObject](#resetcropobject)

    - [<instance> resetCropObject()](#instance-resetcropobject)

Back to top

©2025[Phaser](https://docs.phaser.io)