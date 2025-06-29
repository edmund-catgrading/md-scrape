# Video

Phaser.GameObjects.Video

A Video Game Object.

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

Playback is handled entirely via the Request Video Frame API, which is supported by most modern browsers.

A polyfill is provided for older browsers.

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

**Constructor**

`new Video(scene, x, y, [key])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time. |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| y | number | No | The vertical position of this Game Object in the world. |
| key | string | Yes | Optional key of the Video this Game Object will play, as stored in the Video Cache. |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)  
> [Phaser.GameObjects.Components.Alpha](../namespace/gameobjects-components-alpha.md)  
> [Phaser.GameObjects.Components.BlendMode](../namespace/gameobjects-components-blendmode.md)  
> [Phaser.GameObjects.Components.ComputedSize](../namespace/gameobjects-components-computedsize.md)  
> [Phaser.GameObjects.Components.Depth](../namespace/gameobjects-components-depth.md)  
> [Phaser.GameObjects.Components.Flip](../namespace/gameobjects-components-flip.md)  
> [Phaser.GameObjects.Components.GetBounds](../namespace/gameobjects-components-getbounds.md)  
> [Phaser.GameObjects.Components.Mask](../namespace/gameobjects-components-mask.md)  
> [Phaser.GameObjects.Components.Origin](../namespace/gameobjects-components-origin.md)  
> [Phaser.GameObjects.Components.Pipeline](../namespace/gameobjects-components-pipeline.md)  
> [Phaser.GameObjects.Components.PostPipeline](../namespace/gameobjects-components-postpipeline.md)  
> [Phaser.GameObjects.Components.ScrollFactor](../namespace/gameobjects-components-scrollfactor.md)  
> [Phaser.GameObjects.Components.TextureCrop](../namespace/gameobjects-components-texturecrop.md)  
> [Phaser.GameObjects.Components.Tint](../namespace/gameobjects-components-tint.md)  
> [Phaser.GameObjects.Components.Transform](../namespace/gameobjects-components-transform.md)  
> [Phaser.GameObjects.Components.Visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/video/Video.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L18)  
> Since: 3.20.0

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

## cacheKey

### cacheKey: string

**Description:**

The key of the current video as stored in the Video cache.

If the video did not come from the cache this will be an empty string.

> Source: [src/gameobjects/video/Video.js#L461](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L461)  
> Since: 3.60.0

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

The displayed height of this Game Object.

This value takes into account the scale factor.

Setting this value will adjust the Game Object's scale property.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#displayHeight](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L68)  
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

The displayed width of this Game Object.

This value takes into account the scale factor.

Setting this value will adjust the Game Object's scale property.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#displayWidth](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L43)  
> Since: 3.0.0

---

## failedPlayAttempts

### failedPlayAttempts: number

**Description:**

Records the number of times the video has failed to play,

typically because the user hasn't interacted with the page yet.

> Source: [src/gameobjects/video/Video.js#L272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L272)  
> Since: 3.60.0

---

## flipX

### flipX: boolean

**Description:**

The horizontally flipped state of the Game Object.

A Game Object that is flipped horizontally will render inversed on the horizontal axis.

Flipping always takes place from the middle of the texture and does not impact the scale value.

If this Game Object has a physics body, it will not change the body. This is a rendering toggle only.

**Inherits:** [Phaser.GameObjects.Components.Flip#flipX](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L17)  
> Since: 3.0.0

---

## flipY

### flipY: boolean

**Description:**

If you have saved this video to a texture via the `saveTexture` method, this controls if the video

is rendered with `flipY` in WebGL or not. You often need to set this if you wish to use the video texture

as the input source for a shader. If you find your video is appearing upside down within a shader or

custom pipeline, flip this property.

**Overrides:** Phaser.GameObjects.Components.Flip#flipY

> Source: [src/gameobjects/video/Video.js#L194](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L194)  
> Since: 3.20.0

---

## frame

### frame: [Phaser.Textures.Frame](textures-frame.md)

**Description:**

The Texture Frame this Game Object is using to render with.

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#frame](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L30)  
> Since: 3.0.0

---

## frameReady

### frameReady: boolean

**Description:**

Has the video created its texture and populated it with the first frame of video?

> Source: [src/gameobjects/video/Video.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L236)  
> Since: 3.60.0

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

The native (un-scaled) height of this Game Object.

Changing this value will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or use

the `displayHeight` property.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#height](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L30)  
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

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#isCropped](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L39)  
> Since: 3.11.0

---

## isSeeking

### isSeeking: boolean

**Description:**

Is the video currently seeking?

This is set to `true` when the `seeking` event is fired,

and set to `false` when the `seeked` event is fired.

> Source: [src/gameobjects/video/Video.js#L473](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L473)  
> Since: 3.60.0

---

## isStalled

### isStalled: boolean

**Description:**

This read-only property returns `true` if the video is currently stalled, i.e. it has stopped

playing due to a lack of data, or too much data, but hasn't yet reached the end of the video.

This is set if the Video DOM element emits any of the following events:

`stalled`

`suspend`

`waiting`

And is cleared if the Video DOM element emits the `playing` event, or handles

a requestVideoFrame call.

Listen for the Phaser Event `VIDEO_STALLED` to be notified and inspect the event

to see which DOM event caused it.

Note that being stalled isn't always a negative thing. A video can be stalled if it

has downloaded enough data in to its buffer to not need to download any more until

the current batch of frames have rendered.

> Source: [src/gameobjects/video/Video.js#L245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L245)  
> Since: 3.60.0

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

## markers

### markers: any

**Description:**

An object containing in and out markers for sequence playback.

> Source: [src/gameobjects/video/Video.js#L412](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L412)  
> Since: 3.20.0

---

## mask

### mask: [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md), [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)

**Description:**

The Mask this Game Object is using during render.

**Inherits:** [Phaser.GameObjects.Components.Mask#mask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L19)  
> Since: 3.0.0

---

## metadata

### metadata: VideoFrameCallbackMetadata

**Description:**

If the browser supports the Request Video Frame API then this

property will hold the metadata that is returned from

the callback each time it is invoked.

See <https://wicg.github.io/video-rvfc/#video-frame-metadata-callback>

for a complete list of all properties that will be in this object.

Likely of most interest is the `mediaTime` property:

The media presentation timestamp (PTS) in seconds of the frame presented

(e.g. its timestamp on the video.currentTime timeline). MAY have a zero

value for live-streams or WebRTC applications.

If the browser doesn't support the API then this property will be undefined.

> Source: [src/gameobjects/video/Video.js#L282](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L282)  
> Since: 3.60.0

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

## playWhenUnlocked

### playWhenUnlocked: boolean

**Description:**

Should the video auto play when document interaction is required and happens?

> Source: [src/gameobjects/video/Video.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L227)  
> Since: 3.20.0

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

## retry

### retry: number

**Description:**

The current retry elapsed time.

> Source: [src/gameobjects/video/Video.js#L303](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L303)  
> Since: 3.20.0

---

## retryInterval

### retryInterval: number

**Description:**

If a video fails to play due to a lack of user interaction, this is the

amount of time, in ms, that the video will wait before trying again to

play. The default is 500ms.

> Source: [src/gameobjects/video/Video.js#L312](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L312)  
> Since: 3.20.0

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

## snapshotTexture

### snapshotTexture: [Phaser.Textures.CanvasTexture](textures-canvastexture.md)

**Description:**

A Phaser `CanvasTexture` instance that holds the most recent snapshot taken from the video.

This will only be set if the `snapshot` or `snapshotArea` methods have been called.

Until those methods are called, this property will be `undefined`.

> Source: [src/gameobjects/video/Video.js#L181](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L181)  
> Since: 3.20.0

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

## touchLocked

### touchLocked: boolean

**Description:**

An internal flag holding the current state of the video lock, should document interaction be required

before playback can begin.

> Source: [src/gameobjects/video/Video.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L216)  
> Since: 3.20.0

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

## video

### video: HTMLVideoElement

**Description:**

A reference to the HTML Video Element this Video Game Object is playing.

Will be `undefined` until a video is loaded for playback.

> Source: [src/gameobjects/video/Video.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L148)  
> Since: 3.20.0

---

## videoTexture

### videoTexture: [Phaser.Textures.Texture](textures-texture.md)

**Description:**

The Phaser Texture this Game Object is using to render the video to.

Will be `undefined` until a video is loaded for playback.

> Source: [src/gameobjects/video/Video.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L159)  
> Since: 3.20.0

---

## videoTextureSource

### videoTextureSource: [Phaser.Textures.TextureSource](textures-texturesource.md)

**Description:**

A reference to the TextureSource backing the `videoTexture` Texture object.

Will be `undefined` until a video is loaded for playback.

> Source: [src/gameobjects/video/Video.js#L170](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L170)  
> Since: 3.20.0

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

The native (un-scaled) width of this Game Object.

Changing this value will not change the size that the Game Object is rendered in-game.

For that you need to either set the scale of the Game Object (`setScale`) or use

the `displayWidth` property.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#width](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L17)  
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

## \_callbacks

### \_callbacks: any

**Description:**

The locally bound event callback handlers.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L363](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L363)  
> Since: 3.20.0

---

## \_codeMuted

### \_codeMuted: boolean

**Description:**

The video was muted due to game code, not a system event.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L333](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L333)  
> Since: 3.20.0

---

## \_codePaused

### \_codePaused: boolean

**Description:**

The video was paused due to game code, not a system event.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L353](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L353)  
> Since: 3.20.0

---

## \_crop

### \_crop: object

**Description:**

The internal crop data object, as used by `setCrop` and passed to the `Frame.setCropUVs` method.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L402](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L402)  
> Since: 3.20.0

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

## \_device

### \_device: Array.<string>

**Description:**

A reference to Device.Video.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L518](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L518)  
> Since: 3.60.0

---

## \_getFrame

### \_getFrame: boolean

**Description:**

Has Video.getFirstFrame been called? This is reset if a new Video is loaded or played.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L496](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L496)  
> Since: 3.85.0

---

## \_key

### \_key: string

**Description:**

The key used by the texture as stored in the Texture Manager.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L206](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L206)  
> Since: 3.20.0

---

## \_lastUpdate

### \_lastUpdate: number

**Description:**

The previous frames mediaTime.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L451](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L451)  
> Since: 3.60.0

---

## \_loadCallbackHandler

### \_loadCallbackHandler: function

**Description:**

The locally bound callback handler specifically for load and load error events.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L382](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L382)  
> Since: 3.60.0

---

## \_markerIn

### \_markerIn: number

**Description:**

The in marker.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L421](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L421)  
> Since: 3.20.0

---

## \_markerOut

### \_markerOut: number

**Description:**

The out marker.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L431](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L431)  
> Since: 3.20.0

---

## \_metadataCallbackHandler

### \_metadataCallbackHandler: function

**Description:**

The locally bound callback handler specifically for the loadedmetadata event.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L392](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L392)  
> Since: 3.80.0

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

## \_playCalled

### \_playCalled: boolean

**Description:**

Has Video.play been called? This is reset if a new Video is loaded.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L486](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L486)  
> Since: 3.60.0

---

## \_playingMarker

### \_playingMarker: boolean

**Description:**

Are we playing a marked segment of the video?

**Access:** private

> Source: [src/gameobjects/video/Video.js#L441](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L441)  
> Since: 3.60.0

---

## \_rfvCallbackId

### \_rfvCallbackId: number

**Description:**

The Callback ID returned by Request Video Frame.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L506](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L506)  
> Since: 3.60.0

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

## \_systemMuted

### \_systemMuted: boolean

**Description:**

The video was muted due to a system event, such as the game losing focus.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L323](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L323)  
> Since: 3.20.0

---

## \_systemPaused

### \_systemPaused: boolean

**Description:**

The video was paused due to a system event, such as the game losing focus.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L343](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L343)  
> Since: 3.20.0

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

## addEventHandlers

### <instance> addEventHandlers()

**Description:**

Adds the playback specific event handlers to the video element.

> Source: [src/gameobjects/video/Video.js#L1103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1103)  
> Since: 3.60.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addLoadEventHandlers

### <instance> addLoadEventHandlers()

**Description:**

Adds the loading specific event handlers to the video element.

> Source: [src/gameobjects/video/Video.js#L1068](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1068)  
> Since: 3.60.0

---

## addMarker

### <instance> addMarker(key, markerIn, markerOut)

**Description:**

Adds a sequence marker to this video.

Markers allow you to split a video up into sequences, delineated by a start and end time, given in seconds.

You can then play back specific markers via the `playMarker` method.

Note that marker timing is *not* frame-perfect. You should construct your videos in such a way that you allow for

plenty of extra padding before and after each sequence to allow for discrepancies in browser seek and currentTime accuracy.

See <https://github.com/w3c/media-and-entertainment/issues/4> for more details about this issue.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | A unique name to give this marker. |
| --- | --- | --- | --- |
| markerIn | number | No | The time, in seconds, representing the start of this marker. |
| markerOut | number | No | The time, in seconds, representing the end of this marker. |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L1198](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1198)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addToUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L735](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L735)  
> Since: 3.53.0

---

## changeSource

### <instance> changeSource(key, [autoplay], [loop], [markerIn], [markerOut])

**Description:**

This method allows you to change the source of the current video element. It works by first stopping the

current video, if playing. Then deleting the video texture, if one has been created. Finally, it makes a

new video texture and starts playback of the new source through the existing video element.

The reason you may wish to do this is because videos that require interaction to unlock, remain in an unlocked

state, even if you change the source of the video. By changing the source to a new video you avoid having to

go through the unlock process again.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the Video this Game Object will swap to playing, as stored in the Video Cache. |
| --- | --- | --- | --- | --- |
| autoplay | boolean | Yes | true | Should the video start playing immediately, once the swap is complete? |
| loop | boolean | Yes | false | Should the video loop automatically when it reaches the end? Please note that not all browsers support *seamless* video looping for all encoding formats. |
| markerIn | number | Yes |  | Optional in marker time, in seconds, for playback of a sequence of the video. |
| markerOut | number | Yes |  | Optional out marker time, in seconds, for playback of a sequence of the video. |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L596](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L596)  
> Since: 3.20.0

---

## clearAlpha

### <instance> clearAlpha()

**Description:**

Clears all alpha values associated with this Game Object.

Immediately sets the alpha levels back to 1 (fully opaque).

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Tint#clearTint](../namespace/gameobjects-components-tint.md)

> Source: [src/gameobjects/components/Tint.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Tint.js#L79)  
> Since: 3.0.0

---

## completeHandler

### <instance> completeHandler()

**Description:**

Called when the video completes playback, i.e. reaches an `ended` state.

This will never happen if the video is coming from a live stream, where the duration is `Infinity`.

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_COMPLETE](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L1609](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1609)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

## createPlayPromise

### <instance> createPlayPromise([catchError])

**Description:**

Creates the video.play promise and adds the success and error handlers to it.

Not all browsers support the video.play promise, so this method will fall back to

the old-school way of handling the video.play call.

See <https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/play#browser_compatibility> for details.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| catchError | boolean | Yes | true | Should the error be caught and the video marked as failed to play? |
| --- | --- | --- | --- | --- |

> Source: [src/gameobjects/video/Video.js#L1148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1148)  
> Since: 3.60.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This GameObject.

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

## getCurrentTime

### <instance> getCurrentTime()

**Description:**

A double-precision floating-point value indicating the current playback time in seconds.

If the media has not started to play and has not been seeked, this value is the media's initial playback time.

For a more accurate value, use the `Video.metadata.mediaTime` property instead.

**Returns:** number - A double-precision floating-point value indicating the current playback time in seconds.

> Source: [src/gameobjects/video/Video.js#L1697](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1697)  
> Since: 3.20.0

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

## getDuration

### <instance> getDuration()

**Description:**

A double-precision floating-point value which indicates the duration (total length) of the media in seconds,

on the media's timeline. If no media is present on the element, or the media is not valid, the returned value is NaN.

If the media has no known end (such as for live streams of unknown duration, web radio, media incoming from WebRTC,

and so forth), this value is +Infinity.

If no video has been loaded, this method will return 0.

**Returns:** number - A double-precision floating-point value indicating the duration of the media in seconds.

> Source: [src/gameobjects/video/Video.js#L1822](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1822)  
> Since: 3.20.0

---

## getFirstFrame

### <instance> getFirstFrame()

**Description:**

Attempts to get the first frame of the video by running the `requestVideoFrame` callback once,

then stopping. This is useful if you need to grab the first frame of the video to display behind

a 'play' button, without actually calling the 'play' method.

If the video is already playing, or has been queued to play with `changeSource` then this method just returns.

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L1030](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1030)  
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

## getLoop

### <instance> getLoop()

**Description:**

Returns a boolean which indicates whether the media element should start over when it reaches the end.

**Returns:** boolean - A boolean which indicates whether the media element will start over when it reaches the end.

> Source: [src/gameobjects/video/Video.js#L2098](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2098)  
> Since: 3.20.0

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

## getPlaybackRate

### <instance> getPlaybackRate()

**Description:**

Returns a double that indicates the rate at which the media is being played back.

**Returns:** number - A double that indicates the rate at which the media is being played back.

> Source: [src/gameobjects/video/Video.js#L2063](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2063)  
> Since: 3.20.0

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

## getProgress

### <instance> getProgress()

**Description:**

Returns the current progress of the video as a float.

Progress is defined as a value between 0 (the start) and 1 (the end).

Progress can only be returned if the video has a duration. Some videos,

such as those coming from a live stream, do not have a duration. In this

case the method will return -1.

**Returns:** number - The current progress of playback. If the video has no duration, will always return -1.

> Source: [src/gameobjects/video/Video.js#L1791](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1791)  
> Since: 3.20.0

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

## getVideoKey

### <instance> getVideoKey()

**Description:**

Returns the key of the currently played video, as stored in the Video Cache.

If the video did not come from the cache this will return an empty string.

**Returns:** string - The key of the video being played from the Video Cache, if any.

> Source: [src/gameobjects/video/Video.js#L632](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L632)  
> Since: 3.20.0

---

## getVolume

### <instance> getVolume()

**Description:**

Returns a double indicating the audio volume, from 0.0 (silent) to 1.0 (loudest).

**Returns:** number - A double indicating the audio volume, from 0.0 (silent) to 1.0 (loudest).

> Source: [src/gameobjects/video/Video.js#L2026](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2026)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This GameObject.

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

## isMuted

### <instance> isMuted()

**Description:**

Returns a boolean indicating if this Video is currently muted.

**Returns:** boolean - A boolean indicating if this Video is currently muted, or not.

> Source: [src/gameobjects/video/Video.js#L1867](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1867)  
> Since: 3.20.0

---

## isPaused

### <instance> isPaused()

**Description:**

Returns a boolean which indicates whether the video is currently paused.

**Returns:** boolean - A boolean which indicates whether the video is paused, or not.

> Source: [src/gameobjects/video/Video.js#L2152](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2152)  
> Since: 3.20.0

---

## isPlaying

### <instance> isPlaying()

**Description:**

Returns a boolean which indicates whether the video is currently playing.

**Returns:** boolean - A boolean which indicates whether the video is playing, or not.

> Source: [src/gameobjects/video/Video.js#L2139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2139)  
> Since: 3.20.0

---

## legacyPlayHandler

### <instance> legacyPlayHandler()

**Description:**

Called when the video emits a `playing` event.

This is the legacy handler for browsers that don't support Promise based playback.

> Source: [src/gameobjects/video/Video.js#L1483](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1483)  
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

## load

### <instance> load(key)

**Description:**

Loads a Video from the Video Cache, ready for playback with the `Video.play` method.

If a video is already playing, this method allows you to change the source of the current video element.

It works by first stopping the current video and then starts playback of the new source through the existing video element.

The reason you may wish to do this is because videos that require interaction to unlock, remain in an unlocked

state, even if you change the source of the video. By changing the source to a new video you avoid having to

go through the unlock process again.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Video this Game Object will play, as stored in the Video Cache. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L561](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L561)  
> Since: 3.60.0

---

## loadErrorHandler

### <instance> loadErrorHandler(event)

**Description:**

This internal method is called automatically if the video fails to load.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | Event | No | The error Event. |
| --- | --- | --- | --- |

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_ERROR](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L1517](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1517)  
> Since: 3.20.0

---

## loadHandler

### <instance> loadHandler([url], [noAudio], [crossOrigin], [stream])

**Description:**

Internal method that loads a Video from the given URL, ready for playback with the

`Video.play` method.

Normally you don't call this method directly, but instead use the `Video.loadURL` method,

or the `Video.load` method if you have preloaded the video.

Calling this method will skip checking if the browser supports the given format in

the URL, where-as the other two methods enforce these checks.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| url | string | Yes | The absolute or relative URL to load the video file from. Set to `null` if passing in a MediaStream object. |
| --- | --- | --- | --- |
| noAudio | boolean | Yes | Does the video have an audio track? If not you can enable auto-playing on it. |
| crossOrigin | string | Yes | The value to use for the `crossOrigin` property in the video load request. Either undefined, `anonymous` or `use-credentials`. If no value is given, `crossorigin` will not be set in the request. |
| stream | string | Yes | A MediaStream object if this is playing a stream instead of a file. |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L703](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L703)  
> Since: 3.60.0

---

## loadMediaStream

### <instance> loadMediaStream(stream, [noAudio], [crossOrigin])

**Description:**

Loads a Video from the given MediaStream object, ready for playback with the `Video.play` method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| stream | MediaStream | No |  | The MediaStream object. |
| --- | --- | --- | --- | --- |
| noAudio | boolean | Yes | false | Does the video have an audio track? If not you can enable auto-playing on it. |
| crossOrigin | string | Yes |  | The value to use for the `crossOrigin` property in the video load request. Either undefined, `anonymous` or `use-credentials`. If no value is given, `crossorigin` will not be set in the request. |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L686](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L686)  
> Since: 3.50.0

---

## loadURL

### <instance> loadURL([urls], [noAudio], [crossOrigin])

**Description:**

Loads a Video from the given URL, ready for playback with the `Video.play` method.

If a video is already playing, this method allows you to change the source of the current video element.

It works by first stopping the current video and then starts playback of the new source through the existing video element.

The reason you may wish to do this is because videos that require interaction to unlock, remain in an unlocked

state, even if you change the source of the video. By changing the source to a new video you avoid having to

go through the unlock process again.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| urls | string | Array.<string> | [Phaser.Types.Loader.FileTypes.VideoFileURLConfig](../typedef/types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.VideoFileURLConfig](../typedef/types-loader-filetypes.md)> | Yes |
| --- | --- | --- | --- | --- |
| noAudio | boolean | Yes | false | Does the video have an audio track? If not you can enable auto-playing on it. |
| crossOrigin | string | Yes |  | The value to use for the `crossOrigin` property in the video load request. Either undefined, `anonymous` or `use-credentials`. If no value is given, `crossorigin` will not be set in the request. |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L647](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L647)  
> Since: 3.60.0

---

## metadataHandler

### <instance> metadataHandler(event)

**Description:**

This internal method is called automatically when the video metadata is available.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | Event | No | The loadedmetadata Event. |
| --- | --- | --- | --- |

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_METADATA](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L1533](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1533)  
> Since: 3.80.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - `this`.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - `this`.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## pause

### <instance> pause()

**Description:**

Pauses the current Video, if one is playing.

If no video is loaded, this method does nothing.

Call `Video.resume` to resume playback.

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L1992](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1992)  
> Since: 3.60.0

---

## play

### <instance> play([loop], [markerIn], [markerOut])

**Description:**

Starts this video playing.

If the video is already playing, or has been queued to play with `changeSource` then this method just returns.

Videos can only autoplay if the browser has been unlocked. This happens if you have interacted with the browser, i.e.

by clicking on it or pressing a key, or due to server settings. The policies that control autoplaying are vast and

vary between browser. You can read more here: <https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide>

If your video doesn't contain any audio, then set the `noAudio` parameter to `true` when the video is loaded,

and it will often allow the video to play immediately:

```
Copy
preload () {

  this.load.video('pixar', 'nemo.mp4', true);

}


```

The 3rd parameter in the load call tells Phaser that the video doesn't contain any audio tracks. Video without

audio can autoplay without requiring a user interaction. Video with audio cannot do this unless it satisfies

the browsers MEI settings. See the MDN Autoplay Guide for details.

If you need audio in your videos, then you'll have to consider the fact that the video cannot start playing until the

user has interacted with the browser, into your game flow.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| loop | boolean | Yes | false | Should the video loop automatically when it reaches the end? Please note that not all browsers support *seamless* video looping for all encoding formats. |
| --- | --- | --- | --- | --- |
| markerIn | number | Yes |  | Optional in marker time, in seconds, for playback of a sequence of the video. |
| markerOut | number | Yes |  | Optional out marker time, in seconds, for playback of a sequence of the video. |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L953](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L953)  
> Since: 3.20.0

---

## playError

### <instance> playError(error)

**Description:**

This internal method is called automatically if the playback Promise fails to resolve.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| error | DOMException | No | The Promise DOM Exception error. |
| --- | --- | --- | --- |

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_ERROR](../event/gameobjects-events.md), [Phaser.GameObjects.Events#event:VIDEO\_UNSUPPORTED](../event/gameobjects-events.md), [Phaser.GameObjects.Events#event:VIDEO\_LOCKED](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L1446](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1446)  
> Since: 3.60.0

---

## playingHandler

### <instance> playingHandler()

**Description:**

Called when the video emits a `playing` event.

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_PLAYING](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L1503](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1503)  
> Since: 3.60.0

---

## playMarker

### <instance> playMarker(key, [loop])

**Description:**

Plays a pre-defined sequence in this video.

Markers allow you to split a video up into sequences, delineated by a start and end time, given in seconds and

specified via the `addMarker` method.

Note that marker timing is *not* frame-perfect. You should construct your videos in such a way that you allow for

plenty of extra padding before and after each sequence to allow for discrepancies in browser seek and currentTime accuracy.

See <https://github.com/w3c/media-and-entertainment/issues/4> for more details about this issue.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The name of the marker sequence to play. |
| --- | --- | --- | --- | --- |
| loop | boolean | Yes | false | Should the video loop automatically when it reaches the end? Please note that not all browsers support *seamless* video looping for all encoding formats. |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L1229](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1229)  
> Since: 3.20.0

---

## playSuccess

### <instance> playSuccess()

**Description:**

This internal method is called automatically if the playback Promise resolves successfully.

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_UNLOCKED](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L1405](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1405)  
> Since: 3.60.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - `this`.

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

## removeEventHandlers

### <instance> removeEventHandlers()

**Description:**

Removes the playback specific event handlers from the video element.

> Source: [src/gameobjects/video/Video.js#L1127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1127)  
> Since: 3.60.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This GameObject.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## removeLoadEventHandlers

### <instance> removeLoadEventHandlers()

**Description:**

Removes the loading specific event handlers from the video element.

> Source: [src/gameobjects/video/Video.js#L1086](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1086)  
> Since: 3.60.0

---

## removeMarker

### <instance> removeMarker(key)

**Description:**

Removes a previously set marker from this video.

If the marker is currently playing it will *not* stop playback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The name of the marker to remove. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L1260](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1260)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#removePostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L299)  
> Since: 3.60.0

---

## removeVideoElement

### <instance> removeVideoElement()

**Description:**

Removes the Video element from the DOM by calling parentNode.removeChild on itself.

Also removes the autoplay and src attributes and nulls the `Video.video` reference.

If you loaded an external video via `Video.loadURL` then you should call this function

to clear up once you are done with the instance, but don't want to destroy this

Video Game Object.

This method is called automatically by `Video.destroy`.

> Source: [src/gameobjects/video/Video.js#L2274](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2274)  
> Since: 3.20.0

---

## requestVideoFrame

### <instance> requestVideoFrame(now, metadata)

**Description:**

This method handles the Request Video Frame callback.

It is called by the browser when a new video frame is ready to be displayed.

It's also responsible for the creation of the video texture, if it doesn't

already exist. If it does, it updates the texture as required.

For more details about the Request Video Frame callback, see:

<https://web.dev/requestvideoframecallback-rvfc>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| now | DOMHighResTimeStamp | No | The current time in milliseconds. |
| --- | --- | --- | --- |
| metadata | VideoFrameCallbackMetadata | No | Useful metadata about the video frame that was most recently presented for composition. See <https://wicg.github.io/video-rvfc/#video-frame-metadata-callback> |

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_CREATED](../event/gameobjects-events.md), [Phaser.GameObjects.Events#event:VIDEO\_LOOP](../event/gameobjects-events.md), [Phaser.GameObjects.Events#event:VIDEO\_COMPLETE](../event/gameobjects-events.md), [Phaser.GameObjects.Events#event:VIDEO\_PLAY](../event/gameobjects-events.md), [Phaser.GameObjects.Events#event:VIDEO\_TEXTURE](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L816](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L816)  
> Since: 3.60.0

---

## resetFlip

### <instance> resetFlip()

**Description:**

Resets the horizontal and vertical flipped state of this Game Object back to their default un-flipped state.

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

## resume

### <instance> resume()

**Description:**

Resumes the current Video, if one was previously playing and has been paused.

If no video is loaded, this method does nothing.

Call `Video.pause` to pause playback.

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L2009](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2009)  
> Since: 3.60.0

---

## saveSnapshotTexture

### <instance> saveSnapshotTexture(key)

**Description:**

Stores a copy of this Videos `snapshotTexture` in the Texture Manager using the given key.

This texture is created when the `snapshot` or `snapshotArea` methods are called.

After doing this, any texture based Game Object, such as a Sprite, can use the contents of the

snapshot by using the texture key:

```
Copy
var vid = this.add.video(0, 0, 'intro');



vid.snapshot();



vid.saveSnapshotTexture('doodle');



this.add.image(400, 300, 'doodle');


```

Updating the contents of the `snapshotTexture`, for example by calling `snapshot` again,

will automatically update *any* Game Object that is using it as a texture.

Calling `saveSnapshotTexture` again will not save another copy of the same texture,

it will just rename the existing one.

By default it will create a single base texture. You can add frames to the texture

by using the `Texture.add` method. After doing this, you can then allow Game Objects

to use a specific frame.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique key to store the texture as within the global Texture Manager. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - The Texture that was saved.

> Source: [src/gameobjects/video/Video.js#L1357](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1357)  
> Since: 3.20.0

---

## saveTexture

### <instance> saveTexture(key, [flipY])

**Description:**

Stores this Video in the Texture Manager using the given key as a dynamic texture,

which any texture-based Game Object, such as a Sprite, can use as its source:

```
Copy
const vid = this.add.video(0, 0, 'intro');



vid.play();



vid.saveTexture('doodle');



this.add.image(400, 300, 'doodle');


```

If the video is not yet playing then you need to listen for the `TEXTURE_READY` event before

you can use this texture on a Game Object:

```
Copy
const vid = this.add.video(0, 0, 'intro');



vid.play();



vid.once('textureready', (video, texture, key) => {



    this.add.image(400, 300, key);



});



vid.saveTexture('doodle');


```

The saved texture is automatically updated as the video plays. If you pause this video,

or change its source, then the saved texture updates instantly.

Calling `saveTexture` again will not save another copy of the same texture, it will just rename the existing one.

By default it will create a single base texture. You can add frames to the texture

by using the `Texture.add` method. After doing this, you can then allow Game Objects

to use a specific frame.

If you intend to save the texture so you can use it as the input for a Shader, you may need to set the

`flipY` parameter to `true` if you find the video renders upside down in your shader.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The unique key to store the texture as within the global Texture Manager. |
| --- | --- | --- | --- | --- |
| flipY | boolean | Yes | false | Should the WebGL Texture set `UNPACK_MULTIPLY_FLIP_Y` during upload? |

**Returns:** boolean - Returns `true` if the texture is available immediately, otherwise returns `false` and you should listen for the `TEXTURE_READY` event.

> Source: [src/gameobjects/video/Video.js#L2165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2165)  
> Since: 3.20.0

---

## seekTo

### <instance> seekTo(value)

**Description:**

Seeks to a given point in the video. The value is given as a float between 0 and 1,

where 0 represents the start of the video and 1 represents the end.

Seeking only works if the video has a duration, so will not work for live streams.

When seeking begins, this video will emit a `seeking` event. When the video completes

seeking (i.e. reaches its designated timestamp) it will emit a `seeked` event.

If you wish to seek based on time instead, use the `Video.setCurrentTime` method.

Unfortunately, the DOM video element does not guarantee frame-accurate seeking.

This has been an ongoing subject of discussion: <https://github.com/w3c/media-and-entertainment/issues/4>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The point in the video to seek to. A value between 0 and 1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L1657](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1657)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This GameObject.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#setBlendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L80)  
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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#setCrop](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L50)  
> Since: 3.11.0

---

## setCurrentTime

### <instance> setCurrentTime(value)

**Description:**

Seeks to a given playback time in the video. The value is given in *seconds* or as a string.

Seeking only works if the video has a duration, so will not work for live streams.

When seeking begins, this video will emit a `seeking` event. When the video completes

seeking (i.e. reaches its designated timestamp) it will emit a `seeked` event.

You can provide a string prefixed with either a `+` or a `-`, such as `+2.5` or `-2.5`.

In this case it will seek to +/- the value given, relative to the *current time*.

If you wish to seek based on a duration percentage instead, use the `Video.seekTo` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | number | No | The playback time to seek to in seconds. Can be expressed as a string, such as `+2` to seek 2 seconds ahead from the current time. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L1714](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1714)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L295)  
> Since: 3.0.0

---

## setDataEnabled

### <instance> setDataEnabled()

**Description:**

Adds a Data Manager component to this Game Object.

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This GameObject.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#setDisplaySize](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L120)  
> Since: 3.4.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.TextureCrop#setFrame](../namespace/gameobjects-components-texturecrop.md)

> Source: [src/gameobjects/components/TextureCrop.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L130)  
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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L456](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L456)  
> Since: 3.0.0

---

## setLoop

### <instance> setLoop([value])

**Description:**

Sets the loop state of the current video.

The value given is a boolean which indicates whether the media element will start over when it reaches the end.

Not all videos can loop, for example live streams.

Please note that not all browsers support *seamless* video looping for all encoding formats.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | A boolean which indicates whether the media element will start over when it reaches the end. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L2111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2111)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#setMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L28](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L28)  
> Since: 3.6.2

---

## setMute

### <instance> setMute([value])

**Description:**

Sets the muted state of the currently playing video, if one is loaded.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | The mute value. `true` if the video should be muted, otherwise `false`. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L1841](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1841)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This GameObject.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L112)  
> Since: 3.0.0

---

## setOriginFromFrame

### <instance> setOriginFromFrame()

**Description:**

Sets the origin of this Game Object based on the Pivot values in its Frame.

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setOriginFromFrame](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L136)  
> Since: 3.0.0

---

## setPaused

### <instance> setPaused([value])

**Description:**

Sets the paused state of the currently loaded video.

If the video is playing, calling this method with `true` will pause playback.

If the video is paused, calling this method with `false` will resume playback.

If no video is loaded, this method does nothing.

If the video has not yet been played, `Video.play` will be called with no parameters.

If the video has ended, this method will do nothing.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | The paused value. `true` if the video should be paused, `false` to resume it. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L1938](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1938)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#setPipelineData](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L144)  
> Since: 3.50.0

---

## setPlaybackRate

### <instance> setPlaybackRate([rate])

**Description:**

Sets the playback rate of the current video.

The value given is a double that indicates the rate at which the media is being played back.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rate | number | Yes | A double that indicates the rate at which the media is being played back. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L2076](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2076)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#setScrollFactor](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L64)  
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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ComputedSize#setSize](../namespace/gameobjects-components-computedsize.md)

> Source: [src/gameobjects/components/ComputedSize.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ComputedSize.js#L93)  
> Since: 3.4.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

> Source: [src/gameobjects/video/Video.js#L1547](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1547)  
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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setState](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L252)  
> Since: 3.16.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Visible#setVisible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L63)  
> Since: 3.0.0

---

## setVolume

### <instance> setVolume([value])

**Description:**

Sets the volume of the currently playing video.

The value given is a double indicating the audio volume, from 0.0 (silent) to 1.0 (loudest).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 1 | A double indicating the audio volume, from 0.0 (silent) to 1.0 (loudest). |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

> Source: [src/gameobjects/video/Video.js#L2039](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2039)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

## snapshot

### <instance> snapshot([width], [height])

**Description:**

Takes a snapshot of the current frame of the video and renders it to a CanvasTexture object,

which is then returned. You can optionally resize the grab by passing a width and height.

This method returns a reference to the `Video.snapshotTexture` object. Calling this method

multiple times will overwrite the previous snapshot with the most recent one.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | Yes | The width of the resulting CanvasTexture. |
| --- | --- | --- | --- |
| height | number | Yes | The height of the resulting CanvasTexture. |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - undefined

> Source: [src/gameobjects/video/Video.js#L1279](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1279)  
> Since: 3.20.0

---

## snapshotArea

### <instance> snapshotArea([x], [y], [srcWidth], [srcHeight], [destWidth], [destHeight])

**Description:**

Takes a snapshot of the specified area of the current frame of the video and renders it to a CanvasTexture object,

which is then returned. You can optionally resize the grab by passing a different `destWidth` and `destHeight`.

This method returns a reference to the `Video.snapshotTexture` object. Calling this method

multiple times will overwrite the previous snapshot with the most recent one.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal location of the top-left of the area to grab from. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical location of the top-left of the area to grab from. |
| srcWidth | number | Yes |  | The width of area to grab from the video. If not given it will grab the full video dimensions. |
| srcHeight | number | Yes |  | The height of area to grab from the video. If not given it will grab the full video dimensions. |
| destWidth | number | Yes |  | The destination width of the grab, allowing you to resize it. |
| destHeight | number | Yes |  | The destination height of the grab, allowing you to resize it. |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - undefined

> Source: [src/gameobjects/video/Video.js#L1302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1302)  
> Since: 3.20.0

---

## stalledHandler

### <instance> stalledHandler(event)

**Description:**

This internal method is called automatically if the video stalls, for whatever reason.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | Event | No | The error Event. |
| --- | --- | --- | --- |

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_STALLED](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L1593](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1593)  
> Since: 3.60.0

---

## stop

### <instance> stop([emitStopEvent])

**Description:**

Stops the video playing and clears all internal event listeners.

If you only wish to pause playback of the video, and resume it a later time, use the `Video.pause` method instead.

If the video hasn't finished downloading, calling this method will not abort the download. To do that you need to

call `destroy` instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| emitStopEvent | boolean | Yes | true | Should the `VIDEO_STOP` event be emitted? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Video Game Object for method chaining.

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_STOP](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L2232](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2232)  
> Since: 3.20.0

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This GameObject.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Flip#toggleFlipX](../namespace/gameobjects-components-flip.md)

> Source: [src/gameobjects/components/Flip.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Flip.js#L45)  
> Since: 3.0.0

---

## toggleFlipY

### <instance> toggleFlipY()

**Description:**

Toggles the vertical flipped state of this Game Object.

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

**Returns:** [Phaser.GameObjects.Video](gameobjects-video.md) - This Game Object instance.

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

## globalMute

### <instance> globalMute(soundManager, mute)

**Description:**

Internal global mute handler. Will mute the video, if playing, if the global sound system mutes.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| soundManager | [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md) | [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md) | No | A reference to the Sound Manager that emitted the event. |
| --- | --- | --- | --- |
| mute | boolean | No | The mute value. `true` if the Sound Manager is now muted, otherwise `false`. |

> Source: [src/gameobjects/video/Video.js#L1880](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1880)  
> Since: 3.20.0

---

## globalPause

### <instance> globalPause()

**Description:**

Internal global pause handler. Will pause the video if the Game itself pauses.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L1902](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1902)  
> Since: 3.20.0

---

## globalResume

### <instance> globalResume()

**Description:**

Internal global resume handler. Will resume a paused video if the Game itself resumes.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L1921](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1921)  
> Since: 3.20.0

---

## preDestroy

### <instance> preDestroy()

**Description:**

Handles the pre-destroy step for the Video object.

This calls `Video.stop` and optionally `Video.removeVideoElement`.

If any Sprites are using this Video as their texture it is up to you to manage those.

**Access:** private

> Source: [src/gameobjects/video/Video.js#L2313](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L2313)  
> Since: 3.21.0

---

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

## preUpdate

### <instance> preUpdate(time, delta)

**Description:**

The internal update step.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. |

> Source: [src/gameobjects/video/Video.js#L1625](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1625)  
> Since: 3.20.0

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
| src | [Phaser.GameObjects.Video](gameobjects-video.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

> Source: [src/gameobjects/video/VideoCanvasRenderer.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/VideoCanvasRenderer.js#L7)  
> Since: 3.20.0

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
| src | [Phaser.GameObjects.Video](gameobjects-video.md) | No | The Game Object being rendered in this call. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera that is rendering the Game Object. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | This transform matrix is defined if the game object is nested |

> Source: [src/gameobjects/video/VideoWebGLRenderer.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/VideoWebGLRenderer.js#L7)  
> Since: 3.20.0

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

## seekedHandler

### <instance> seekedHandler()

**Description:**

Internal seeked handler.

**Access:** private

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_SEEKED](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L1776](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1776)  
> Since: 3.20.0

---

## seekingHandler

### <instance> seekingHandler()

**Description:**

Internal seeking handler.

**Access:** private

**Fires:** [Phaser.GameObjects.Events#event:VIDEO\_SEEKING](../event/gameobjects-events.md)

> Source: [src/gameobjects/video/Video.js#L1761](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/video/Video.js#L1761)  
> Since: 3.20.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Autoplaying Videos](#autoplaying-videos)
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
  + [cacheKey](#cachekey)

    - [cacheKey: string](#cachekey-string)
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
  + [failedPlayAttempts](#failedplayattempts)

    - [failedPlayAttempts: number](#failedplayattempts-number)
  + [flipX](#flipx)

    - [flipX: boolean](#flipx-boolean)
  + [flipY](#flipy)

    - [flipY: boolean](#flipy-boolean)
  + [frame](#frame)

    - [frame: Phaser.Textures.Frame](#frame-phasertexturesframe)
  + [frameReady](#frameready)

    - [frameReady: boolean](#frameready-boolean)
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
  + [isSeeking](#isseeking)

    - [isSeeking: boolean](#isseeking-boolean)
  + [isStalled](#isstalled)

    - [isStalled: boolean](#isstalled-boolean)
  + [isTinted](#istinted)

    - [isTinted: boolean](#istinted-boolean)
  + [markers](#markers)

    - [markers: any](#markers-any)
  + [mask](#mask)

    - [mask: Phaser.Display.Masks.BitmapMask, Phaser.Display.Masks.GeometryMask](#mask-phaserdisplaymasksbitmapmask-phaserdisplaymasksgeometrymask)
  + [metadata](#metadata)

    - [metadata: VideoFrameCallbackMetadata](#metadata-videoframecallbackmetadata)
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
  + [playWhenUnlocked](#playwhenunlocked)

    - [playWhenUnlocked: boolean](#playwhenunlocked-boolean)
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
  + [retry](#retry)

    - [retry: number](#retry-number)
  + [retryInterval](#retryinterval)

    - [retryInterval: number](#retryinterval-number)
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
  + [snapshotTexture](#snapshottexture)

    - [snapshotTexture: Phaser.Textures.CanvasTexture](#snapshottexture-phasertexturescanvastexture)
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
  + [touchLocked](#touchlocked)

    - [touchLocked: boolean](#touchlocked-boolean)
  + [type](#type)

    - [type: string](#type-string)
  + [video](#video)

    - [video: HTMLVideoElement](#video-htmlvideoelement)
  + [videoTexture](#videotexture)

    - [videoTexture: Phaser.Textures.Texture](#videotexture-phasertexturestexture)
  + [videoTextureSource](#videotexturesource)

    - [videoTextureSource: Phaser.Textures.TextureSource](#videotexturesource-phasertexturestexturesource)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
  + [w](#w)

    - [w: number](#w-number)
  + [width](#width)

    - [width: number](#width-number)
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
  + [\_callbacks](#_callbacks)

    - [\_callbacks: any](#_callbacks-any)
  + [\_codeMuted](#_codemuted)

    - [\_codeMuted: boolean](#_codemuted-boolean)
  + [\_codePaused](#_codepaused)

    - [\_codePaused: boolean](#_codepaused-boolean)
  + [\_crop](#_crop)

    - [\_crop: object](#_crop-object)
  + [\_depth](#_depth)

    - [\_depth: number](#_depth-number)
  + [\_device](#_device)

    - [\_device: Array.<string>](#_device-arraystring)
  + [\_getFrame](#_getframe)

    - [\_getFrame: boolean](#_getframe-boolean)
  + [\_key](#_key)

    - [\_key: string](#_key-string)
  + [\_lastUpdate](#_lastupdate)

    - [\_lastUpdate: number](#_lastupdate-number)
  + [\_loadCallbackHandler](#_loadcallbackhandler)

    - [\_loadCallbackHandler: function](#_loadcallbackhandler-function)
  + [\_markerIn](#_markerin)

    - [\_markerIn: number](#_markerin-number)
  + [\_markerOut](#_markerout)

    - [\_markerOut: number](#_markerout-number)
  + [\_metadataCallbackHandler](#_metadatacallbackhandler)

    - [\_metadataCallbackHandler: function](#_metadatacallbackhandler-function)
  + [\_originComponent](#_origincomponent)

    - [\_originComponent: boolean](#_origincomponent-boolean)
  + [\_playCalled](#_playcalled)

    - [\_playCalled: boolean](#_playcalled-boolean)
  + [\_playingMarker](#_playingmarker)

    - [\_playingMarker: boolean](#_playingmarker-boolean)
  + [\_rfvCallbackId](#_rfvcallbackid)

    - [\_rfvCallbackId: number](#_rfvcallbackid-number)
  + [\_rotation](#_rotation)

    - [\_rotation: number](#_rotation-number)
  + [\_scaleX](#_scalex)

    - [\_scaleX: number](#_scalex-number)
  + [\_scaleY](#_scaley)

    - [\_scaleY: number](#_scaley-number)
  + [\_systemMuted](#_systemmuted)

    - [\_systemMuted: boolean](#_systemmuted-boolean)
  + [\_systemPaused](#_systempaused)

    - [\_systemPaused: boolean](#_systempaused-boolean)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
* [Public Methods](#public-methods)

  + [addedToScene](#addedtoscene)

    - [<instance> addedToScene()](#instance-addedtoscene)
  + [addEventHandlers](#addeventhandlers)

    - [<instance> addEventHandlers()](#instance-addeventhandlers)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addLoadEventHandlers](#addloadeventhandlers)

    - [<instance> addLoadEventHandlers()](#instance-addloadeventhandlers)
  + [addMarker](#addmarker)

    - [<instance> addMarker(key, markerIn, markerOut)](#instance-addmarkerkey-markerin-markerout)
  + [addToDisplayList](#addtodisplaylist)

    - [<instance> addToDisplayList([displayList])](#instance-addtodisplaylistdisplaylist)
  + [addToUpdateList](#addtoupdatelist)

    - [<instance> addToUpdateList()](#instance-addtoupdatelist)
  + [changeSource](#changesource)

    - [<instance> changeSource(key, [autoplay], [loop], [markerIn], [markerOut])](#instance-changesourcekey-autoplay-loop-markerin-markerout)
  + [clearAlpha](#clearalpha)

    - [<instance> clearAlpha()](#instance-clearalpha)
  + [clearFX](#clearfx)

    - [<instance> clearFX()](#instance-clearfx)
  + [clearMask](#clearmask)

    - [<instance> clearMask([destroyMask])](#instance-clearmaskdestroymask)
  + [clearTint](#cleartint)

    - [<instance> clearTint()](#instance-cleartint)
  + [completeHandler](#completehandler)

    - [<instance> completeHandler()](#instance-completehandler)
  + [copyPosition](#copyposition)

    - [<instance> copyPosition(source)](#instance-copypositionsource)
  + [createBitmapMask](#createbitmapmask)

    - [<instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])](#instance-createbitmapmaskmaskobject-x-y-texture-frame)
  + [createGeometryMask](#creategeometrymask)

    - [<instance> createGeometryMask([graphics])](#instance-creategeometrymaskgraphics)
  + [createPlayPromise](#createplaypromise)

    - [<instance> createPlayPromise([catchError])](#instance-createplaypromisecatcherror)
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
  + [getCurrentTime](#getcurrenttime)

    - [<instance> getCurrentTime()](#instance-getcurrenttime)
  + [getData](#getdata)

    - [<instance> getData(key)](#instance-getdatakey)
  + [getDisplayList](#getdisplaylist)

    - [<instance> getDisplayList()](#instance-getdisplaylist)
  + [getDuration](#getduration)

    - [<instance> getDuration()](#instance-getduration)
  + [getFirstFrame](#getfirstframe)

    - [<instance> getFirstFrame()](#instance-getfirstframe)
  + [getIndexList](#getindexlist)

    - [<instance> getIndexList()](#instance-getindexlist)
  + [getLeftCenter](#getleftcenter)

    - [<instance> getLeftCenter([output], [includeParent])](#instance-getleftcenteroutput-includeparent)
  + [getLocalPoint](#getlocalpoint)

    - [<instance> getLocalPoint(x, y, [point], [camera])](#instance-getlocalpointx-y-point-camera)
  + [getLocalTransformMatrix](#getlocaltransformmatrix)

    - [<instance> getLocalTransformMatrix([tempMatrix])](#instance-getlocaltransformmatrixtempmatrix)
  + [getLoop](#getloop)

    - [<instance> getLoop()](#instance-getloop)
  + [getParentRotation](#getparentrotation)

    - [<instance> getParentRotation()](#instance-getparentrotation)
  + [getPipelineName](#getpipelinename)

    - [<instance> getPipelineName()](#instance-getpipelinename)
  + [getPlaybackRate](#getplaybackrate)

    - [<instance> getPlaybackRate()](#instance-getplaybackrate)
  + [getPostPipeline](#getpostpipeline)

    - [<instance> getPostPipeline(pipeline)](#instance-getpostpipelinepipeline)
  + [getProgress](#getprogress)

    - [<instance> getProgress()](#instance-getprogress)
  + [getRightCenter](#getrightcenter)

    - [<instance> getRightCenter([output], [includeParent])](#instance-getrightcenteroutput-includeparent)
  + [getTopCenter](#gettopcenter)

    - [<instance> getTopCenter([output], [includeParent])](#instance-gettopcenteroutput-includeparent)
  + [getTopLeft](#gettopleft)

    - [<instance> getTopLeft([output], [includeParent])](#instance-gettopleftoutput-includeparent)
  + [getTopRight](#gettopright)

    - [<instance> getTopRight([output], [includeParent])](#instance-gettoprightoutput-includeparent)
  + [getVideoKey](#getvideokey)

    - [<instance> getVideoKey()](#instance-getvideokey)
  + [getVolume](#getvolume)

    - [<instance> getVolume()](#instance-getvolume)
  + [getWorldTransformMatrix](#getworldtransformmatrix)

    - [<instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])](#instance-getworldtransformmatrixtempmatrix-parentmatrix)
  + [incData](#incdata)

    - [<instance> incData(key, [amount])](#instance-incdatakey-amount)
  + [initPipeline](#initpipeline)

    - [<instance> initPipeline([pipeline])](#instance-initpipelinepipeline)
  + [initPostPipeline](#initpostpipeline)

    - [<instance> initPostPipeline([preFX])](#instance-initpostpipelineprefx)
  + [isMuted](#ismuted)

    - [<instance> isMuted()](#instance-ismuted)
  + [isPaused](#ispaused)

    - [<instance> isPaused()](#instance-ispaused)
  + [isPlaying](#isplaying)

    - [<instance> isPlaying()](#instance-isplaying)
  + [legacyPlayHandler](#legacyplayhandler)

    - [<instance> legacyPlayHandler()](#instance-legacyplayhandler)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [load](#load)

    - [<instance> load(key)](#instance-loadkey)
  + [loadErrorHandler](#loaderrorhandler)

    - [<instance> loadErrorHandler(event)](#instance-loaderrorhandlerevent)
  + [loadHandler](#loadhandler)

    - [<instance> loadHandler([url], [noAudio], [crossOrigin], [stream])](#instance-loadhandlerurl-noaudio-crossorigin-stream)
  + [loadMediaStream](#loadmediastream)

    - [<instance> loadMediaStream(stream, [noAudio], [crossOrigin])](#instance-loadmediastreamstream-noaudio-crossorigin)
  + [loadURL](#loadurl)

    - [<instance> loadURL([urls], [noAudio], [crossOrigin])](#instance-loadurlurls-noaudio-crossorigin)
  + [metadataHandler](#metadatahandler)

    - [<instance> metadataHandler(event)](#instance-metadatahandlerevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [pause](#pause)

    - [<instance> pause()](#instance-pause)
  + [play](#play)

    - [<instance> play([loop], [markerIn], [markerOut])](#instance-playloop-markerin-markerout)
  + [playError](#playerror)

    - [<instance> playError(error)](#instance-playerrorerror)
  + [playingHandler](#playinghandler)

    - [<instance> playingHandler()](#instance-playinghandler)
  + [playMarker](#playmarker)

    - [<instance> playMarker(key, [loop])](#instance-playmarkerkey-loop)
  + [playSuccess](#playsuccess)

    - [<instance> playSuccess()](#instance-playsuccess)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removedFromScene](#removedfromscene)

    - [<instance> removedFromScene()](#instance-removedfromscene)
  + [removeEventHandlers](#removeeventhandlers)

    - [<instance> removeEventHandlers()](#instance-removeeventhandlers)
  + [removeFromDisplayList](#removefromdisplaylist)

    - [<instance> removeFromDisplayList()](#instance-removefromdisplaylist)
  + [removeFromUpdateList](#removefromupdatelist)

    - [<instance> removeFromUpdateList()](#instance-removefromupdatelist)
  + [removeInteractive](#removeinteractive)

    - [<instance> removeInteractive([resetCursor])](#instance-removeinteractiveresetcursor)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [removeLoadEventHandlers](#removeloadeventhandlers)

    - [<instance> removeLoadEventHandlers()](#instance-removeloadeventhandlers)
  + [removeMarker](#removemarker)

    - [<instance> removeMarker(key)](#instance-removemarkerkey)
  + [removePostPipeline](#removepostpipeline)

    - [<instance> removePostPipeline(pipeline)](#instance-removepostpipelinepipeline)
  + [removeVideoElement](#removevideoelement)

    - [<instance> removeVideoElement()](#instance-removevideoelement)
  + [requestVideoFrame](#requestvideoframe)

    - [<instance> requestVideoFrame(now, metadata)](#instance-requestvideoframenow-metadata)
  + [resetFlip](#resetflip)

    - [<instance> resetFlip()](#instance-resetflip)
  + [resetPipeline](#resetpipeline)

    - [<instance> resetPipeline([resetData])](#instance-resetpipelineresetdata)
  + [resetPostPipeline](#resetpostpipeline)

    - [<instance> resetPostPipeline([resetData])](#instance-resetpostpipelineresetdata)
  + [resume](#resume)

    - [<instance> resume()](#instance-resume)
  + [saveSnapshotTexture](#savesnapshottexture)

    - [<instance> saveSnapshotTexture(key)](#instance-savesnapshottexturekey)
  + [saveTexture](#savetexture)

    - [<instance> saveTexture(key, [flipY])](#instance-savetexturekey-flipy)
  + [seekTo](#seekto)

    - [<instance> seekTo(value)](#instance-seektovalue)
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
  + [setCrop](#setcrop)

    - [<instance> setCrop([x], [y], [width], [height])](#instance-setcropx-y-width-height)
  + [setCurrentTime](#setcurrenttime)

    - [<instance> setCurrentTime(value)](#instance-setcurrenttimevalue)
  + [setData](#setdata)

    - [<instance> setData(key, [data])](#instance-setdatakey-data)
  + [setDataEnabled](#setdataenabled)

    - [<instance> setDataEnabled()](#instance-setdataenabled)
  + [setDepth](#setdepth)

    - [<instance> setDepth(value)](#instance-setdepthvalue)
  + [setDisplayOrigin](#setdisplayorigin)

    - [<instance> setDisplayOrigin([x], [y])](#instance-setdisplayoriginx-y)
  + [setDisplaySize](#setdisplaysize)

    - [<instance> setDisplaySize(width, height)](#instance-setdisplaysizewidth-height)
  + [setFlip](#setflip)

    - [<instance> setFlip(x, y)](#instance-setflipx-y)
  + [setFlipX](#setflipx)

    - [<instance> setFlipX(value)](#instance-setflipxvalue)
  + [setFlipY](#setflipy)

    - [<instance> setFlipY(value)](#instance-setflipyvalue)
  + [setFrame](#setframe)

    - [<instance> setFrame(frame, [updateSize], [updateOrigin])](#instance-setframeframe-updatesize-updateorigin)
  + [setInteractive](#setinteractive)

    - [<instance> setInteractive([hitArea], [callback], [dropZone])](#instance-setinteractivehitarea-callback-dropzone)
  + [setLoop](#setloop)

    - [<instance> setLoop([value])](#instance-setloopvalue)
  + [setMask](#setmask)

    - [<instance> setMask(mask)](#instance-setmaskmask)
  + [setMute](#setmute)

    - [<instance> setMute([value])](#instance-setmutevalue)
  + [setName](#setname)

    - [<instance> setName(value)](#instance-setnamevalue)
  + [setOrigin](#setorigin)

    - [<instance> setOrigin([x], [y])](#instance-setoriginx-y)
  + [setOriginFromFrame](#setoriginfromframe)

    - [<instance> setOriginFromFrame()](#instance-setoriginfromframe)
  + [setPaused](#setpaused)

    - [<instance> setPaused([value])](#instance-setpausedvalue)
  + [setPipeline](#setpipeline)

    - [<instance> setPipeline(pipeline, [pipelineData], [copyData])](#instance-setpipelinepipeline-pipelinedata-copydata)
  + [setPipelineData](#setpipelinedata)

    - [<instance> setPipelineData(key, [value])](#instance-setpipelinedatakey-value)
  + [setPlaybackRate](#setplaybackrate)

    - [<instance> setPlaybackRate([rate])](#instance-setplaybackraterate)
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
  + [setSize](#setsize)

    - [<instance> setSize(width, height)](#instance-setsizewidth-height)
  + [setSizeToFrame](#setsizetoframe)

    - [<instance> setSizeToFrame([frame])](#instance-setsizetoframeframe)
  + [setState](#setstate)

    - [<instance> setState(value)](#instance-setstatevalue)
  + [setTexture](#settexture)

    - [<instance> setTexture(key, [frame])](#instance-settexturekey-frame)
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
  + [setVolume](#setvolume)

    - [<instance> setVolume([value])](#instance-setvolumevalue)
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
  + [snapshot](#snapshot)

    - [<instance> snapshot([width], [height])](#instance-snapshotwidth-height)
  + [snapshotArea](#snapshotarea)

    - [<instance> snapshotArea([x], [y], [srcWidth], [srcHeight], [destWidth], [destHeight])](#instance-snapshotareax-y-srcwidth-srcheight-destwidth-destheight)
  + [stalledHandler](#stalledhandler)

    - [<instance> stalledHandler(event)](#instance-stalledhandlerevent)
  + [stop](#stop)

    - [<instance> stop([emitStopEvent])](#instance-stopemitstopevent)
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

  + [globalMute](#globalmute)

    - [<instance> globalMute(soundManager, mute)](#instance-globalmutesoundmanager-mute)
  + [globalPause](#globalpause)

    - [<instance> globalPause()](#instance-globalpause)
  + [globalResume](#globalresume)

    - [<instance> globalResume()](#instance-globalresume)
  + [preDestroy](#predestroy)

    - [<instance> preDestroy()](#instance-predestroy)
  + [prepareBoundsOutput](#prepareboundsoutput)

    - [<instance> prepareBoundsOutput(output, [includeParent])](#instance-prepareboundsoutputoutput-includeparent)
  + [preUpdate](#preupdate)

    - [<instance> preUpdate(time, delta)](#instance-preupdatetime-delta)
  + [renderCanvas](#rendercanvas)

    - [<instance> renderCanvas(renderer, src, camera, parentMatrix)](#instance-rendercanvasrenderer-src-camera-parentmatrix)
  + [renderWebGL](#renderwebgl)

    - [<instance> renderWebGL(renderer, src, camera, parentMatrix)](#instance-renderwebglrenderer-src-camera-parentmatrix)
  + [resetCropObject](#resetcropobject)

    - [<instance> resetCropObject()](#instance-resetcropobject)
  + [seekedHandler](#seekedhandler)

    - [<instance> seekedHandler()](#instance-seekedhandler)
  + [seekingHandler](#seekinghandler)

    - [<instance> seekingHandler()](#instance-seekinghandler)

Back to top

©2025[Phaser](https://docs.phaser.io)