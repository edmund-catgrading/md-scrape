# FX

Phaser.GameObjects.Components.FX

The FX Component features a set of methods used for applying a range of special built-in effects to a Game Object.

The effects include the following:

* Barrel Distortion
* Bloom
* Blur
* Bokeh / Tilt Shift
* Circle Outline
* Color Matrix
* Glow
* Displacement
* Gradient
* Pixelate
* Shine
* Shadow
* Vignette
* Wipe / Reveal

All Game Objects support Post FX. These are effects applied after the Game Object has been rendered.

Texture-based Game Objects also support Pre FX, including:

* Image
* Sprite
* TileSprite
* Text
* RenderTexture
* Video

And any Game Object that extends the above.

The difference between Pre FX and Post FX are that all Post FX take place in a canvas (renderer) sized frame buffer,

after the Game Object has been rendered. Pre FX, however, take place in a texture sized frame buffer, which is sized

based on the Game Object itself. The end result is then composited back to the main game canvas. For intensive effects,

such as blur, bloom or glow, which can require many iterations, this is a much more efficient way to apply the effect,

as only it only has to work on a Game Object sized texture and not all pixels in the canvas.

In short, you should always try and use a Pre FX if you can.

Due to the way that FX work they can be stacked-up. For example, you can apply a blur to a Game Object, then apply

a bloom effect to the same Game Object. The bloom effect will be applied to the blurred texture, not the original.

Keep the order in mind when stacking effects.

All effects are WebGL only and do not have canvas counterparts.

As you can appreciate, some effects are more expensive than others. For example, a bloom effect is going to be more

expensive than a simple color matrix effect, so please consider using them wisely and performance test your target

platforms early on in production.

This component is created automatically by the `PostPipeline` class and does not need to be instantiated directly.

**Constructor**

`new FX(gameObject, isPost)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | A reference to the Game Object that owns this FX Component. |
| --- | --- | --- | --- |
| isPost | boolean | No | Is this a Pre or Post FX Component? |

---

**Scope**: static

> Source: [src/gameobjects/components/FX.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L11)  
> Since: 3.60.0

# Public Members

## enabled

### enabled: boolean

**Description:**

Has this FX Component been enabled?

You should treat this property as read-only, although it is toggled

automaticaly during internal use.

> Source: [src/gameobjects/components/FX.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L100)  
> Since: 3.60.0

---

## gameObject

### gameObject: [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)

**Description:**

A reference to the Game Object that owns this FX Component.

> Source: [src/gameobjects/components/FX.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L80)  
> Since: 3.60.0

---

## isPost

### isPost: boolean

**Description:**

Is this a Post FX Controller? or a Pre FX Controller?

> Source: [src/gameobjects/components/FX.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L90)  
> Since: 3.60.0

---

## list

### list: Array.<[Phaser.FX.Controller](fx-controller.md)>

**Description:**

An array containing all of the Pre FX Controllers that

have been added to this FX Component. They are processed in

the order they are added.

This array is empty if this is a Post FX Component.

> Source: [src/gameobjects/components/FX.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L112)  
> Since: 3.60.0

---

## padding

### padding: number

**Description:**

The amount of extra padding to be applied to this Game Object

when it is being rendered by a PreFX Pipeline.

Lots of FX require additional spacing added to the texture the

Game Object uses, for example a glow or shadow effect, and this

method allows you to control how much extra padding is included

in addition to the texture size.

You do not need to set this if you're only using Post FX.

> Source: [src/gameobjects/components/FX.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L125)  
> Since: 3.60.0

---

# Public Methods

## add

### <instance> add(fx, [config])

**Description:**

Adds the given FX Controler to this FX Component.

Note that adding an FX Controller does not remove any existing FX. They all stack-up

on-top of each other. If you don't want this, make sure to call either `remove` or

`clear` first.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fx | [Phaser.FX.Controller](fx-controller.md) | No | The FX Controller to add to this FX Component. |
| --- | --- | --- | --- |
| config | object | Yes | Optional configuration object that is passed to the pipeline during instantiation. |

**Returns:** [Phaser.FX.Controller](fx-controller.md) - The FX Controller.

> Source: [src/gameobjects/components/FX.js#L377](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L377)  
> Since: 3.60.0

---

## addBarrel

### <instance> addBarrel([amount])

**Description:**

Adds a Barrel effect.

A barrel effect allows you to apply either a 'pinch' or 'expand' distortion to

a Game Object. The amount of the effect can be modified in real-time.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The amount of distortion applied to the barrel effect. A value of 1 is no distortion. Typically keep this within +- 1. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.Barrel](fx-barrel.md) - The Barrel FX Controller.

> Source: [src/gameobjects/components/FX.js#L671](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L671)  
> Since: 3.60.0

---

## addBloom

### <instance> addBloom([color], [offsetX], [offsetY], [blurStrength], [strength], [steps])

**Description:**

Adds a Bloom effect.

Bloom is an effect used to reproduce an imaging artifact of real-world cameras.

The effect produces fringes of light extending from the borders of bright areas in an image,

contributing to the illusion of an extremely bright light overwhelming the

camera or eye capturing the scene.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color | number | Yes |  | The color of the Bloom, as a hex value. |
| --- | --- | --- | --- | --- |
| offsetX | number | Yes | 1 | The horizontal offset of the bloom effect. |
| offsetY | number | Yes | 1 | The vertical offset of the bloom effect. |
| blurStrength | number | Yes | 1 | The strength of the blur process of the bloom effect. |
| strength | number | Yes | 1 | The strength of the blend process of the bloom effect. |
| steps | number | Yes | 4 | The number of steps to run the Bloom effect for. This value should always be an integer. |

**Returns:** [Phaser.FX.Bloom](fx-bloom.md) - The Bloom FX Controller.

> Source: [src/gameobjects/components/FX.js#L600](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L600)  
> Since: 3.60.0

---

## addBlur

### <instance> addBlur([quality], [x], [y], [strength], [color], [steps])

**Description:**

Adds a Blur effect.

A Gaussian blur is the result of blurring an image by a Gaussian function. It is a widely used effect,

typically to reduce image noise and reduce detail. The visual effect of this blurring technique is a

smooth blur resembling that of viewing the image through a translucent screen, distinctly different

from the bokeh effect produced by an out-of-focus lens or the shadow of an object under usual illumination.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| quality | number | Yes | 0 | The quality of the blur effect. Can be either 0 for Low Quality, 1 for Medium Quality or 2 for High Quality. |
| --- | --- | --- | --- | --- |
| x | number | Yes | 2 | The horizontal offset of the blur effect. |
| y | number | Yes | 2 | The vertical offset of the blur effect. |
| strength | number | Yes | 1 | The strength of the blur effect. |
| color | number | Yes | "0xffffff" | The color of the blur, as a hex value. |
| steps | number | Yes | 4 | The number of steps to run the blur effect for. This value should always be an integer. |

**Returns:** [Phaser.FX.Blur](fx-blur.md) - The Blur FX Controller.

> Source: [src/gameobjects/components/FX.js#L548](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L548)  
> Since: 3.60.0

---

## addBokeh

### <instance> addBokeh([radius], [amount], [contrast])

**Description:**

Adds a Bokeh effect.

Bokeh refers to a visual effect that mimics the photographic technique of creating a shallow depth of field.

This effect is used to emphasize the game's main subject or action, by blurring the background or foreground

elements, resulting in a more immersive and visually appealing experience. It is achieved through rendering

techniques that simulate the out-of-focus areas, giving a sense of depth and realism to the game's graphics.

See also Tilt Shift.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radius | number | Yes | 0.5 | The radius of the bokeh effect. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The amount of the bokeh effect. |
| contrast | number | Yes | 0.2 | The color contrast of the bokeh effect. |

**Returns:** [Phaser.FX.Bokeh](fx-bokeh.md) - The Bokeh FX Controller.

> Source: [src/gameobjects/components/FX.js#L774](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L774)  
> Since: 3.60.0

---

## addCircle

### <instance> addCircle([thickness], [color], [backgroundColor], [scale], [feather])

**Description:**

Adds a Circle effect.

This effect will draw a circle around the texture of the Game Object, effectively masking off

any area outside of the circle without the need for an actual mask. You can control the thickness

of the circle, the color of the circle and the color of the background, should the texture be

transparent. You can also control the feathering applied to the circle, allowing for a harsh or soft edge.

Please note that adding this effect to a Game Object will not change the input area or physics body of

the Game Object, should it have one.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| thickness | number | Yes | 8 | The width of the circle around the texture, in pixels. |
| --- | --- | --- | --- | --- |
| color | number | Yes | "0xfeedb6" | The color of the circular ring, given as a number value. |
| backgroundColor | number | Yes | "0xff0000" | The color of the background, behind the texture, given as a number value. |
| scale | number | Yes | 1 | The scale of the circle. The default scale is 1, which is a circle the full size of the underlying texture. |
| feather | number | Yes | 0.005 | The amount of feathering to apply to the circle from the ring. |

**Returns:** [Phaser.FX.Circle](fx-circle.md) - The Circle FX Controller.

> Source: [src/gameobjects/components/FX.js#L644](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L644)  
> Since: 3.60.0

---

## addColorMatrix

### <instance> addColorMatrix()

**Description:**

Adds a ColorMatrix effect.

The color matrix effect is a visual technique that involves manipulating the colors of an image

or scene using a mathematical matrix. This process can adjust hue, saturation, brightness, and contrast,

allowing developers to create various stylistic appearances or mood settings within the game.

Common applications include simulating different lighting conditions, applying color filters,

or achieving a specific visual style.

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - The ColorMatrix FX Controller.

> Source: [src/gameobjects/components/FX.js#L625](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L625)  
> Since: 3.60.0

---

## addDisplacement

### <instance> addDisplacement([texture], [x], [y])

**Description:**

Adds a Displacement effect.

The displacement effect is a visual technique that alters the position of pixels in an image

or texture based on the values of a displacement map. This effect is used to create the illusion

of depth, surface irregularities, or distortion in otherwise flat elements. It can be applied to

characters, objects, or backgrounds to enhance realism, convey movement, or achieve various

stylistic appearances.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| texture | string | Yes | "'\_\_WHITE'" | The unique string-based key of the texture to use for displacement, which must exist in the Texture Manager. |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0.005 | The amount of horizontal displacement to apply. A very small float number, such as 0.005. |
| y | number | Yes | 0.005 | The amount of vertical displacement to apply. A very small float number, such as 0.005. |

**Returns:** [Phaser.FX.Displacement](fx-displacement.md) - The Displacement FX Controller.

> Source: [src/gameobjects/components/FX.js#L689](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L689)  
> Since: 3.60.0

---

## addGlow

### <instance> addGlow([color], [outerStrength], [innerStrength], [knockout], [quality], [distance])

**Description:**

Adds a Glow effect.

The glow effect is a visual technique that creates a soft, luminous halo around game objects,

characters, or UI elements. This effect is used to emphasize importance, enhance visual appeal,

or convey a sense of energy, magic, or otherworldly presence. The effect can also be set on

the inside of the Game Object. The color and strength of the glow can be modified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color | number | Yes | "0xffffff" | The color of the glow effect as a number value. |
| --- | --- | --- | --- | --- |
| outerStrength | number | Yes | 4 | The strength of the glow outward from the edge of the Sprite. |
| innerStrength | number | Yes | 0 | The strength of the glow inward from the edge of the Sprite. |
| knockout | boolean | Yes | false | If `true` only the glow is drawn, not the texture itself. |
| quality | number | Yes | 0.1 | Only available for PostFX. Sets the quality of this Glow effect. Default is 0.1. Cannot be changed post-creation. |
| distance | number | Yes | 10 | Only available for PostFX. Sets the distance of this Glow effect. Default is 10. Cannot be changed post-creation. |

**Returns:** [Phaser.FX.Glow](fx-glow.md) - The Glow FX Controller.

> Source: [src/gameobjects/components/FX.js#L433](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L433)  
> Since: 3.60.0

---

## addGradient

### <instance> addGradient([color1], [color2], [alpha], [fromX], [fromY], [toX], [toY], [size])

**Description:**

Adds a Gradient effect.

The gradient overlay effect is a visual technique where a smooth color transition is applied over Game Objects,

such as sprites or UI components. This effect is used to enhance visual appeal, emphasize depth, or create

stylistic and atmospheric variations. It can also be utilized to convey information, such as representing

progress or health status through color changes.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color1 | number | Yes | "0xff0000" | The first gradient color, given as a number value. |
| --- | --- | --- | --- | --- |
| color2 | number | Yes | "0x00ff00" | The second gradient color, given as a number value. |
| alpha | number | Yes | 0.2 | The alpha value of the gradient effect. |
| fromX | number | Yes | 0 | The horizontal position the gradient will start from. This value is normalized, between 0 and 1, and is not in pixels. |
| fromY | number | Yes | 0 | The vertical position the gradient will start from. This value is normalized, between 0 and 1, and is not in pixels. |
| toX | number | Yes | 0 | The horizontal position the gradient will end at. This value is normalized, between 0 and 1, and is not in pixels. |
| toY | number | Yes | 1 | The vertical position the gradient will end at. This value is normalized, between 0 and 1, and is not in pixels. |
| size | number | Yes | 0 | How many 'chunks' the gradient is divided in to, as spread over the entire height of the texture. Leave this at zero for a smooth gradient, or set higher for a more retro chunky effect. |

**Returns:** [Phaser.FX.Gradient](fx-gradient.md) - The Gradient FX Controller.

> Source: [src/gameobjects/components/FX.js#L573](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L573)  
> Since: 3.60.0

---

## addPixelate

### <instance> addPixelate([amount])

**Description:**

Adds a Pixelate effect.

The pixelate effect is a visual technique that deliberately reduces the resolution or detail of an image,

creating a blocky or mosaic appearance composed of large, visible pixels. This effect can be used for stylistic

purposes, as a homage to retro gaming, or as a means to obscure certain elements within the game, such as

during a transition or to censor specific content.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The amount of pixelation to apply. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.Pixelate](fx-pixelate.md) - The Pixelate FX Controller.

> Source: [src/gameobjects/components/FX.js#L483](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L483)  
> Since: 3.60.0

---

## addReveal

### <instance> addReveal([wipeWidth], [direction], [axis])

**Description:**

Adds a Reveal Wipe effect.

The wipe or reveal effect is a visual technique that gradually uncovers or conceals elements

in the game, such as images, text, or scene transitions. This effect is often used to create

a sense of progression, reveal hidden content, or provide a smooth and visually appealing transition

between game states.

You can set both the direction and the axis of the wipe effect. The following combinations are possible:

* left to right: direction 0, axis 0
* right to left: direction 1, axis 0
* top to bottom: direction 1, axis 1
* bottom to top: direction 1, axis 0

It is up to you to set the `progress` value yourself, i.e. via a Tween, in order to transition the effect.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| wipeWidth | number | Yes | 0.1 | The width of the wipe effect. This value is normalized in the range 0 to 1. |
| --- | --- | --- | --- | --- |
| direction | number | Yes | 0 | The direction of the wipe effect. Either 0 or 1. Set in conjunction with the axis property. |
| axis | number | Yes | 0 | The axis of the wipe effect. Either 0 or 1. Set in conjunction with the direction property. |

**Returns:** [Phaser.FX.Wipe](fx-wipe.md) - The Wipe FX Controller.

> Source: [src/gameobjects/components/FX.js#L743](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L743)  
> Since: 3.60.0

---

## addShadow

### <instance> addShadow([x], [y], [decay], [power], [color], [samples], [intensity])

**Description:**

Adds a Shadow effect.

The shadow effect is a visual technique used to create the illusion of depth and realism by adding darker,

offset silhouettes or shapes beneath game objects, characters, or environments. These simulated shadows

help to enhance the visual appeal and immersion, making the 2D game world appear more dynamic and three-dimensional.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal offset of the shadow effect. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical offset of the shadow effect. |
| decay | number | Yes | 0.1 | The amount of decay for shadow effect. |
| power | number | Yes | 1 | The power of the shadow effect. |
| color | number | Yes | "0x000000" | The color of the shadow. |
| samples | number | Yes | 6 | The number of samples that the shadow effect will run for. An integer between 1 and 12. |
| intensity | number | Yes | 1 | The intensity of the shadow effect. |

**Returns:** [Phaser.FX.Shadow](fx-shadow.md) - The Shadow FX Controller.

> Source: [src/gameobjects/components/FX.js#L458](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L458)  
> Since: 3.60.0

---

## addShine

### <instance> addShine([speed], [lineWidth], [gradient], [reveal])

**Description:**

Adds a Shine effect.

The shine effect is a visual technique that simulates the appearance of reflective

or glossy surfaces by passing a light beam across a Game Object. This effect is used to

enhance visual appeal, emphasize certain features, and create a sense of depth or

material properties.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| speed | number | Yes | 0.5 | The speed of the Shine effect. |
| --- | --- | --- | --- | --- |
| lineWidth | number | Yes | 0.5 | The line width of the Shine effect. |
| gradient | number | Yes | 3 | The gradient of the Shine effect. |
| reveal | boolean | Yes | false | Does this Shine effect reveal or get added to its target? |

**Returns:** [Phaser.FX.Shine](fx-shine.md) - The Shine FX Controller.

> Source: [src/gameobjects/components/FX.js#L525](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L525)  
> Since: 3.60.0

---

## addTiltShift

### <instance> addTiltShift([radius], [amount], [contrast], [blurX], [blurY], [strength])

**Description:**

Adds a Tilt Shift effect.

This Bokeh effect can also be used to generate a Tilt Shift effect, which is a technique used to create a miniature

effect by blurring everything except a small area of the image. This effect is achieved by blurring the

top and bottom elements, while keeping the center area in focus.

See also Bokeh.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radius | number | Yes | 0.5 | The radius of the bokeh effect. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The amount of the bokeh effect. |
| contrast | number | Yes | 0.2 | The color contrast of the bokeh effect. |
| blurX | number | Yes | 1 | The amount of horizontal blur. |
| blurY | number | Yes | 1 | The amount of vertical blur. |
| strength | number | Yes | 1 | The strength of the blur. |

**Returns:** [Phaser.FX.Bokeh](fx-bokeh.md) - The Bokeh TiltShift FX Controller.

> Source: [src/gameobjects/components/FX.js#L798](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L798)  
> Since: 3.60.0

---

## addVignette

### <instance> addVignette([x], [y], [radius], [strength])

**Description:**

Adds a Vignette effect.

The vignette effect is a visual technique where the edges of the screen, or a Game Object, gradually darken or blur,

creating a frame-like appearance. This effect is used to draw the player's focus towards the central action or subject,

enhance immersion, and provide a cinematic or artistic quality to the game's visuals.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0.5 | The horizontal offset of the vignette effect. This value is normalized to the range 0 to 1. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0.5 | The vertical offset of the vignette effect. This value is normalized to the range 0 to 1. |
| radius | number | Yes | 0.5 | The radius of the vignette effect. This value is normalized to the range 0 to 1. |
| strength | number | Yes | 0.5 | The strength of the vignette effect. |

**Returns:** [Phaser.FX.Vignette](fx-vignette.md) - The Vignette FX Controller.

> Source: [src/gameobjects/components/FX.js#L503](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L503)  
> Since: 3.60.0

---

## addWipe

### <instance> addWipe([wipeWidth], [direction], [axis])

**Description:**

Adds a Wipe effect.

The wipe or reveal effect is a visual technique that gradually uncovers or conceals elements

in the game, such as images, text, or scene transitions. This effect is often used to create

a sense of progression, reveal hidden content, or provide a smooth and visually appealing transition

between game states.

You can set both the direction and the axis of the wipe effect. The following combinations are possible:

* left to right: direction 0, axis 0
* right to left: direction 1, axis 0
* top to bottom: direction 1, axis 1
* bottom to top: direction 1, axis 0

It is up to you to set the `progress` value yourself, i.e. via a Tween, in order to transition the effect.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| wipeWidth | number | Yes | 0.1 | The width of the wipe effect. This value is normalized in the range 0 to 1. |
| --- | --- | --- | --- | --- |
| direction | number | Yes | 0 | The direction of the wipe effect. Either 0 or 1. Set in conjunction with the axis property. |
| axis | number | Yes | 0 | The axis of the wipe effect. Either 0 or 1. Set in conjunction with the direction property. |

**Returns:** [Phaser.FX.Wipe](fx-wipe.md) - The Wipe FX Controller.

> Source: [src/gameobjects/components/FX.js#L712](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L712)  
> Since: 3.60.0

---

## clear

### <instance> clear()

**Description:**

Destroys and removes all FX Controllers that are part of this FX Component,

then disables it.

If this is a Pre FX Component it will only remove Pre FX.

If this is a Post FX Component it will only remove Post FX.

To remove both at once use the `GameObject.clearFX` method instead.

**Returns:** [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md) - This Game Object instance.

> Source: [src/gameobjects/components/FX.js#L244](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L244)  
> Since: 3.60.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this FX Component.

Called automatically when Game Objects are destroyed.

> Source: [src/gameobjects/components/FX.js#L824](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L824)  
> Since: 3.60.0

---

## disable

### <instance> disable([clear])

**Description:**

Disables this FX Component.

This will reset the pipeline on the Game Object that owns this component back to its

default and flag this component as disabled.

You can re-enable it again by calling `enable` for Pre FX or by adding an FX for Post FX.

Optionally, set `clear` to destroy all current FX Controllers.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| clear | boolean | Yes | false | Destroy and remove all FX Controllers that are part of this component. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md) - This Game Object instance.

> Source: [src/gameobjects/components/FX.js#L341](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L341)  
> Since: 3.60.0

---

## enable

### <instance> enable([padding])

**Description:**

Enables this FX Component and applies the FXPipeline to the parent Game Object.

This is called automatically whenever you call a method such as `addBloom`, etc.

You can check the `enabled` property to see if the Game Object is already enabled, or not.

This only applies to Pre FX. Post FX are always enabled.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| padding | number | Yes | 0 | The amount of padding to add to this Game Object. |
| --- | --- | --- | --- | --- |

> Source: [src/gameobjects/components/FX.js#L204](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L204)  
> Since: 3.60.0

---

## onFX

### <instance> onFX(pipeline)

**Description:**

This callback is invoked when this Game Object is rendered by a PreFX Pipeline.

This happens when the pipeline uses its `drawSprite` method.

It's invoked prior to the draw, allowing you to set shader uniforms, etc on the pipeline.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.Pipelines.PreFXPipeline](renderer-webgl-pipelines-prefxpipeline.md) | No | The PreFX Pipeline that invoked this callback. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/components/FX.js#L188](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L188)  
> Since: 3.60.0

---

## onFXCopy

### <instance> onFXCopy(pipeline)

**Description:**

This callback is invoked when this Game Object is copied by a PreFX Pipeline.

This happens when the pipeline uses its `copySprite` method.

It's invoked prior to the copy, allowing you to set shader uniforms, etc on the pipeline.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.Pipelines.PreFXPipeline](renderer-webgl-pipelines-prefxpipeline.md) | No | The PreFX Pipeline that invoked this callback. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/components/FX.js#L172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L172)  
> Since: 3.60.0

---

## remove

### <instance> remove(fx)

**Description:**

Searches for the given FX Controller within this FX Component.

If found, the controller is removed from this component and then destroyed.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fx | [Phaser.FX.Controller](fx-controller.md) | No | The FX Controller to remove from this FX Component. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md) - This Game Object instance.

> Source: [src/gameobjects/components/FX.js#L281](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L281)  
> Since: 3.60.0

---

## setPadding

### <instance> setPadding([padding])

**Description:**

Sets the amount of extra padding to be applied to this Game Object

when it is being rendered by a PreFX Pipeline.

Lots of FX require additional spacing added to the texture the

Game Object uses, for example a glow or shadow effect, and this

method allows you to control how much extra padding is included

in addition to the texture size.

You do not need to set this if you're only using Post FX.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| padding | number | Yes | 0 | The amount of padding to add to this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md) - This Game Object instance.

> Source: [src/gameobjects/components/FX.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/FX.js#L144)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [enabled](#enabled)

    - [enabled: boolean](#enabled-boolean)
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [isPost](#ispost)

    - [isPost: boolean](#ispost-boolean)
  + [list](#list)

    - [list: Array.<Phaser.FX.Controller>](#list-arrayphaserfxcontroller)
  + [padding](#padding)

    - [padding: number](#padding-number)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(fx, [config])](#instance-addfx-config)
  + [addBarrel](#addbarrel)

    - [<instance> addBarrel([amount])](#instance-addbarrelamount)
  + [addBloom](#addbloom)

    - [<instance> addBloom([color], [offsetX], [offsetY], [blurStrength], [strength], [steps])](#instance-addbloomcolor-offsetx-offsety-blurstrength-strength-steps)
  + [addBlur](#addblur)

    - [<instance> addBlur([quality], [x], [y], [strength], [color], [steps])](#instance-addblurquality-x-y-strength-color-steps)
  + [addBokeh](#addbokeh)

    - [<instance> addBokeh([radius], [amount], [contrast])](#instance-addbokehradius-amount-contrast)
  + [addCircle](#addcircle)

    - [<instance> addCircle([thickness], [color], [backgroundColor], [scale], [feather])](#instance-addcirclethickness-color-backgroundcolor-scale-feather)
  + [addColorMatrix](#addcolormatrix)

    - [<instance> addColorMatrix()](#instance-addcolormatrix)
  + [addDisplacement](#adddisplacement)

    - [<instance> addDisplacement([texture], [x], [y])](#instance-adddisplacementtexture-x-y)
  + [addGlow](#addglow)

    - [<instance> addGlow([color], [outerStrength], [innerStrength], [knockout], [quality], [distance])](#instance-addglowcolor-outerstrength-innerstrength-knockout-quality-distance)
  + [addGradient](#addgradient)

    - [<instance> addGradient([color1], [color2], [alpha], [fromX], [fromY], [toX], [toY], [size])](#instance-addgradientcolor1-color2-alpha-fromx-fromy-tox-toy-size)
  + [addPixelate](#addpixelate)

    - [<instance> addPixelate([amount])](#instance-addpixelateamount)
  + [addReveal](#addreveal)

    - [<instance> addReveal([wipeWidth], [direction], [axis])](#instance-addrevealwipewidth-direction-axis)
  + [addShadow](#addshadow)

    - [<instance> addShadow([x], [y], [decay], [power], [color], [samples], [intensity])](#instance-addshadowx-y-decay-power-color-samples-intensity)
  + [addShine](#addshine)

    - [<instance> addShine([speed], [lineWidth], [gradient], [reveal])](#instance-addshinespeed-linewidth-gradient-reveal)
  + [addTiltShift](#addtiltshift)

    - [<instance> addTiltShift([radius], [amount], [contrast], [blurX], [blurY], [strength])](#instance-addtiltshiftradius-amount-contrast-blurx-blury-strength)
  + [addVignette](#addvignette)

    - [<instance> addVignette([x], [y], [radius], [strength])](#instance-addvignettex-y-radius-strength)
  + [addWipe](#addwipe)

    - [<instance> addWipe([wipeWidth], [direction], [axis])](#instance-addwipewipewidth-direction-axis)
  + [clear](#clear)

    - [<instance> clear()](#instance-clear)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [disable](#disable)

    - [<instance> disable([clear])](#instance-disableclear)
  + [enable](#enable)

    - [<instance> enable([padding])](#instance-enablepadding)
  + [onFX](#onfx)

    - [<instance> onFX(pipeline)](#instance-onfxpipeline)
  + [onFXCopy](#onfxcopy)

    - [<instance> onFXCopy(pipeline)](#instance-onfxcopypipeline)
  + [remove](#remove)

    - [<instance> remove(fx)](#instance-removefx)
  + [setPadding](#setpadding)

    - [<instance> setPadding([padding])](#instance-setpaddingpadding)

Back to top

©2025[Phaser](https://docs.phaser.io)