# ScaleManager

Phaser.Scale.ScaleManager

The Scale Manager handles the scaling, resizing and alignment of the game canvas.

The way scaling is handled is by setting the game canvas to a fixed size, which is defined in the

game configuration. You also define the parent container in the game config. If no parent is given,

it will default to using the document body. The Scale Manager will then look at the available space

within the *parent* and scale the canvas accordingly. Scaling is handled by setting the canvas CSS

width and height properties, leaving the width and height of the canvas element itself untouched.

Scaling is therefore achieved by keeping the core canvas the same size and 'stretching'

it via its CSS properties. This gives the same result and speed as using the `transform-scale` CSS

property, without the need for browser prefix handling.

The calculations for the scale are heavily influenced by the bounding parent size, which is the computed

dimensions of the canvas's parent. The CSS rules of the parent element play an important role in the

operation of the Scale Manager. For example, if the parent has no defined width or height, then actions

like auto-centering will fail to achieve the required result. The Scale Manager works in tandem with the

CSS you set-up on the page hosting your game, rather than taking control of it.

#### Parent and Display canvas containment guidelines:

* Style the Parent element (of the game canvas) to control the Parent size and thus the games size and layout.
* The Parent element's CSS styles should *effectively* apply maximum (and minimum) bounding behavior.
* The Parent element should *not* apply a padding as this is not accounted for.

  If a padding is required apply it to the Parent's parent or apply a margin to the Parent.

  If you need to add a border, margin or any other CSS around your game container, then use a parent element and

  apply the CSS to this instead, otherwise you'll be constantly resizing the shape of the game container.
* The Display canvas layout CSS styles (i.e. margins, size) should not be altered / specified as

  they may be updated by the Scale Manager.

#### Scale Modes

The way the scaling is handled is determined by the `scaleMode` property. The default is `NONE`,

which prevents Phaser from scaling or touching the canvas, or its parent, at all. In this mode, you are

responsible for all scaling. The other scaling modes afford you automatic scaling.

If you wish to scale your game so that it always fits into the available space within the parent, you

should use the scale mode `FIT`. Look at the documentation for other scale modes to see what options are

available. Here is a basic config showing how to set this scale mode:

```
Copy
scale: {

    parent: 'yourgamediv',

    mode: Phaser.Scale.FIT,

    width: 800,

    height: 600

}


```

Place the `scale` config object within your game config.

If you wish for the canvas to be resized directly, so that the canvas itself fills the available space

(i.e. it isn't scaled, it's resized) then use the `RESIZE` scale mode. This will give you a 1:1 mapping

of canvas pixels to game size. In this mode CSS isn't used to scale the canvas, it's literally adjusted

to fill all available space within the parent. You should be extremely careful about the size of the

canvas you're creating when doing this, as the larger the area, the more work the GPU has to do and it's

very easy to hit fill-rate limits quickly.

For complex, custom-scaling requirements, you should probably consider using the `RESIZE` scale mode,

with your own limitations in place re: canvas dimensions and managing the scaling with the game scenes

yourself. For the vast majority of games, however, the `FIT` mode is likely to be the most used.

Please appreciate that the Scale Manager cannot perform miracles. All it does is scale your game canvas

as best it can, based on what it can infer from its surrounding area. There are all kinds of environments

where it's up to you to guide and help the canvas position itself, especially when built into rendering

frameworks like React and Vue. If your page requires meta tags to prevent user scaling gestures, or such

like, then it's up to you to ensure they are present in the html.

#### Centering

You can also have the game canvas automatically centered. Again, this relies heavily on the parent being

properly configured and styled, as the centering offsets are based entirely on the available space

within the parent element. Centering is disabled by default, or can be applied horizontally, vertically,

or both. Here's an example:

```
Copy
scale: {

    parent: 'yourgamediv',

    autoCenter: Phaser.Scale.CENTER_BOTH,

    width: 800,

    height: 600

}


```

#### Fullscreen API

If the browser supports it, you can send your game into fullscreen mode. In this mode, the game will fill

the entire display, removing all browser UI and anything else present on the screen. It will remain in this

mode until your game either disables it, or until the user tabs out or presses ESCape if on desktop. It's a

great way to achieve a desktop-game like experience from the browser, but it does require a modern browser

to handle it. Some mobile browsers also support this.

**Constructor**

`new ScaleManager(game)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | A reference to the Phaser.Game instance. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/scale/ScaleManager.js#L22](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L22)  
> Since: 3.16.0

# Public Members

## \_resetZoom

### \_resetZoom: boolean

**Description:**

Internal flag set when the game zoom factor is modified.

> Source: [src/scale/ScaleManager.js#L253](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L253)  
> Since: 3.19.0

---

## autoCenter

### autoCenter: [Phaser.Scale.CenterType](../typedef/scale.md)

**Description:**

Automatically center the canvas within the parent? The different centering modes are:

1. No centering.
2. Center both horizontally and vertically.
3. Center horizontally.
4. Center vertically.

Please be aware that in order to center the game canvas, you must have specified a parent

that has a size set, or the canvas parent is the document.body.

> Source: [src/scale/ScaleManager.js#L283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L283)  
> Since: 3.16.0

---

## autoRound

### autoRound: boolean

**Description:**

If set, the canvas sizes will be automatically passed through Math.floor.

This results in rounded pixel display values, which is important for performance on legacy

and low powered devices, but at the cost of not achieving a 'perfect' fit in some browser windows.

> Source: [src/scale/ScaleManager.js#L272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L272)  
> Since: 3.16.0

---

## baseSize

### baseSize: [Phaser.Structs.Size](structs-size.md)

**Description:**

The Base Size component.

The modified game size, which is the auto-rounded gameSize, used to set the canvas width and height

(but not the CSS style)

> Source: [src/scale/ScaleManager.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L205)  
> Since: 3.16.0

---

## canvas

### canvas: HTMLCanvasElement

**Description:**

A reference to the HTML Canvas Element that Phaser uses to render the game.

> Source: [src/scale/ScaleManager.js#L145](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L145)  
> Since: 3.16.0

---

## canvasBounds

### canvasBounds: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

The DOM bounds of the canvas element.

> Source: [src/scale/ScaleManager.js#L154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L154)  
> Since: 3.16.0

---

## dirty

### dirty: boolean

**Description:**

The dirty state of the Scale Manager.

Set if there is a change between the parent size and the current size.

> Source: [src/scale/ScaleManager.js#L339](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L339)  
> Since: 3.16.0

---

## displayScale

### displayScale: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The scale factor between the baseSize and the canvasBounds.

> Source: [src/scale/ScaleManager.js#L263](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L263)  
> Since: 3.16.0

---

## displaySize

### displaySize: [Phaser.Structs.Size](structs-size.md)

**Description:**

The Display Size component.

The size used for the canvas style, factoring in the scale mode, parent and other values.

> Source: [src/scale/ScaleManager.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L217)  
> Since: 3.16.0

---

## fullscreen

### fullscreen: [Phaser.Device.Fullscreen](../typedef/device.md)

**Description:**

A reference to the Device.Fullscreen object.

> Source: [src/scale/ScaleManager.js#L311](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L311)  
> Since: 3.16.0

---

## fullscreenTarget

### fullscreenTarget: any

**Description:**

The DOM Element which is sent into fullscreen mode.

> Source: [src/scale/ScaleManager.js#L320](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L320)  
> Since: 3.16.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

A reference to the Phaser.Game instance.

> Source: [src/scale/ScaleManager.js#L135](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L135)  
> Since: 3.15.0

---

## gameSize

### gameSize: [Phaser.Structs.Size](structs-size.md)

**Description:**

The Game Size component.

The un-modified game size, as requested in the game config (the raw width / height),

as used for world bounds, cameras, etc

> Source: [src/scale/ScaleManager.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L193)  
> Since: 3.16.0

---

## height

### height: number

**Description:**

The game height.

This is typically the size given in the game configuration.

> Source: [src/scale/ScaleManager.js#L1802](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1802)  
> Since: 3.16.0

---

## isFullscreen

### isFullscreen: boolean

**Description:**

Is the browser currently in fullscreen mode or not?

> Source: [src/scale/ScaleManager.js#L1766](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1766)  
> Since: 3.16.0

---

## isGameLandscape

### isGameLandscape: boolean

**Description:**

Are the game dimensions landscape? (i.e. wider than they are tall)

This is different to the device itself being in a landscape orientation.

> Source: [src/scale/ScaleManager.js#L1876](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1876)  
> Since: 3.16.0

---

## isGamePortrait

### isGamePortrait: boolean

**Description:**

Are the game dimensions portrait? (i.e. taller than they are wide)

This is different to the device itself being in a portrait orientation.

> Source: [src/scale/ScaleManager.js#L1857](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1857)  
> Since: 3.16.0

---

## isLandscape

### isLandscape: boolean

**Description:**

Is the device in a landscape orientation as reported by the Orientation API?

This value is usually only available on mobile devices.

> Source: [src/scale/ScaleManager.js#L1839](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1839)  
> Since: 3.16.0

---

## isPortrait

### isPortrait: boolean

**Description:**

Is the device in a portrait orientation as reported by the Orientation API?

This value is usually only available on mobile devices.

> Source: [src/scale/ScaleManager.js#L1821](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1821)  
> Since: 3.16.0

---

## orientation

### orientation: [Phaser.Scale.OrientationType](../typedef/scale.md)

**Description:**

The current device orientation.

Orientation events are dispatched via the Device Orientation API, typically only on mobile browsers.

> Source: [src/scale/ScaleManager.js#L300](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L300)  
> Since: 3.16.0

---

## parent

### parent: any

**Description:**

The parent object of the Canvas. Often a div, or the browser window, or nothing in non-browser environments.

This is set in the Game Config as the `parent` property. If undefined (or just not present), it will default

to use the document body. If specifically set to `null` Phaser will ignore all parent operations.

> Source: [src/scale/ScaleManager.js#L163](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L163)  
> Since: 3.16.0

---

## parentIsWindow

### parentIsWindow: boolean

**Description:**

Is the parent element the browser window?

> Source: [src/scale/ScaleManager.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L175)  
> Since: 3.16.0

---

## parentSize

### parentSize: [Phaser.Structs.Size](structs-size.md)

**Description:**

The Parent Size component.

> Source: [src/scale/ScaleManager.js#L184](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L184)  
> Since: 3.16.0

---

## resizeInterval

### resizeInterval: number

**Description:**

How many milliseconds should elapse before checking if the browser size has changed?

Most modern browsers dispatch a 'resize' event, which the Scale Manager will listen for.

However, older browsers fail to do this, or do it consistently, so we fall back to a

more traditional 'size check' based on a time interval. You can control how often it is

checked here.

> Source: [src/scale/ScaleManager.js#L349](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L349)  
> Since: 3.16.0

---

## scaleMode

### scaleMode: [Phaser.Scale.ScaleModeType](../typedef/scale.md)

**Description:**

The game scale mode.

> Source: [src/scale/ScaleManager.js#L228](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L228)  
> Since: 3.16.0

---

## width

### width: number

**Description:**

The game width.

This is typically the size given in the game configuration.

> Source: [src/scale/ScaleManager.js#L1783](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1783)  
> Since: 3.16.0

---

## zoom

### zoom: number

**Description:**

The game zoom factor.

This value allows you to multiply your games base size by the given zoom factor.

This is then used when calculating the display size, even in `NONE` situations.

If you don't want Phaser to touch the canvas style at all, this value should be 1.

Can also be set to `MAX_ZOOM` in which case the zoom value will be derived based

on the game size and available space within the parent.

> Source: [src/scale/ScaleManager.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L237)  
> Since: 3.16.0

---

# Private Members

## \_checkOrientation

### \_checkOrientation: boolean

**Description:**

Internal flag to check orientation state.

**Access:** private

> Source: [src/scale/ScaleManager.js#L373](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L373)  
> Since: 3.16.0

---

## \_createdFullscreenTarget

### \_createdFullscreenTarget: boolean

**Description:**

Did Phaser create the fullscreen target div, or was it provided in the game config?

**Access:** private

> Source: [src/scale/ScaleManager.js#L329](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L329)  
> Since: 3.16.0

---

## \_lastCheck

### \_lastCheck: number

**Description:**

Internal size interval tracker.

**Access:** private

> Source: [src/scale/ScaleManager.js#L363](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L363)  
> Since: 3.16.0

---

## domlisteners

### domlisteners: object

**Description:**

Internal object containing our defined event listeners.

**Access:** private

> Source: [src/scale/ScaleManager.js#L383](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L383)  
> Since: 3.16.0

---

# Public Methods

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

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## boot

### <instance> boot()

**Description:**

The Boot handler is called by Phaser.Game when it first starts up.

The renderer is available by now and the canvas has been added to the DOM.

**Access:** protected

**Fires:** [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L417](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L417)  
> Since: 3.16.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this Scale Manager, releasing all references to external resources.

Once destroyed, the Scale Manager cannot be used again.

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/scale/ScaleManager.js#L1741](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1741)  
> Since: 3.16.0

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

## getFullscreenTarget

### <instance> getFullscreenTarget()

**Description:**

An internal method that gets the target element that is used when entering fullscreen mode.

**Returns:** object - The fullscreen target element.

> Source: [src/scale/ScaleManager.js#L1378](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1378)  
> Since: 3.16.0

---

## getMaxZoom

### <instance> getMaxZoom()

**Description:**

Calculates and returns the largest possible zoom factor, based on the current

parent and game sizes. If the parent has no dimensions (i.e. an unstyled div),

or is smaller than the un-zoomed game, then this will return a value of 1 (no zoom)

**Returns:** number - The maximum possible zoom factor. At a minimum this value is always at least 1.

> Source: [src/scale/ScaleManager.js#L1162](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1162)  
> Since: 3.16.0

---

## getParent

### <instance> getParent(config)

**Description:**

Determines the parent element of the game canvas, if any, based on the game configuration.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Core.GameConfig](../typedef/types-core.md) | No | The Game configuration object. |
| --- | --- | --- | --- |

> Source: [src/scale/ScaleManager.js#L598](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L598)  
> Since: 3.16.0

---

## getParentBounds

### <instance> getParentBounds()

**Description:**

Calculates the size of the parent bounds and updates the `parentSize`

properties, only if the canvas has a dom parent.

**Returns:** boolean - `true` if the parent bounds have changed size or position, otherwise `false`.

> Source: [src/scale/ScaleManager.js#L648](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L648)  
> Since: 3.16.0

---

## getViewPort

### <instance> getViewPort([camera], [out])

**Description:**

Get Rectange of visible area.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The camera this viewport is respond upon. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | The Rectangle of visible area. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - The Rectangle of visible area.

> Source: [src/scale/ScaleManager.js#L1609](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1609)  
> Since: 3.60.0

---

## leaveFullScreenSuccessHandler

### <instance> leaveFullScreenSuccessHandler()

**Description:**

The browser has successfully left fullscreen mode.

**Fires:** [Phaser.Scale.Events#event:LEAVE\_FULLSCREEN](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L1463](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1463)  
> Since: 3.85.0

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

## lockOrientation

### <instance> lockOrientation(orientation)

**Description:**

Attempts to lock the orientation of the web browser using the Screen Orientation API.

This API is only available on modern mobile browsers.

See <https://developer.mozilla.org/en-US/docs/Web/API/Screen/lockOrientation> for details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | string | No | The orientation you'd like to lock the browser in. Should be an API string such as 'landscape', 'landscape-primary', 'portrait', etc. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the orientation was successfully locked, otherwise `false`.

> Source: [src/scale/ScaleManager.js#L703](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L703)  
> Since: 3.16.0

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

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - `this`.

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

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - `this`.

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

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## onFullScreenChange

### <instance> onFullScreenChange()

**Description:**

Triggered when a fullscreenchange event is dispatched by the DOM.

**Access:** protected

> Source: [src/scale/ScaleManager.js#L1577](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1577)  
> Since: 3.16.0

---

## onFullScreenError

### <instance> onFullScreenError()

**Description:**

Triggered when a fullscreenerror event is dispatched by the DOM.

> Source: [src/scale/ScaleManager.js#L1598](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1598)  
> Since: 3.16.0

---

## parseConfig

### <instance> parseConfig(config)

**Description:**

Parses the game configuration to set-up the scale defaults.

**Access:** protected

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Core.GameConfig](../typedef/types-core.md) | No | The Game configuration object. |
| --- | --- | --- | --- |

> Source: [src/scale/ScaleManager.js#L465](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L465)  
> Since: 3.16.0

---

## preBoot

### <instance> preBoot()

**Description:**

Called *before* the canvas object is created and added to the DOM.

**Access:** protected

> Source: [src/scale/ScaleManager.js#L401](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L401)  
> Since: 3.16.0

---

## refresh

### <instance> refresh([previousWidth], [previousHeight])

**Description:**

Refreshes the internal scale values, bounds sizes and orientation checks.

Once finished, dispatches the resize event.

This is called automatically by the Scale Manager when the browser window size changes,

as long as it is using a Scale Mode other than 'NONE'.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| previousWidth | number | Yes | The previous width of the game. Only set if the gameSize has changed. |
| --- | --- | --- | --- |
| previousHeight | number | Yes | The previous height of the game. Only set if the gameSize has changed. |

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - The Scale Manager instance.

**Fires:** [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L949](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L949)  
> Since: 3.16.0

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

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeFullscreenTarget

### <instance> removeFullscreenTarget()

**Description:**

Removes the fullscreen target that was added to the DOM.

> Source: [src/scale/ScaleManager.js#L1414](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1414)  
> Since: 3.17.0

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

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## resize

### <instance> resize(width, height)

**Description:**

Call this to modify the size of the Phaser canvas element directly.

You should only use this if you are using the `NONE` scale mode,

it will update all internal components completely.

If all you want to do is change the size of the parent, see the `setParentSize` method.

If all you want is to change the base size of the game, but still have the Scale Manager

manage all the scaling (i.e. you're **not** using `NONE`), then see the `setGameSize` method.

This method will set the `gameSize`, `baseSize` and `displaySize` components to the given

dimensions. It will then resize the canvas width and height to the values given, by

directly setting the properties. Finally, if you have set the Scale Manager zoom value

to anything other than 1 (the default), it will set the canvas CSS width and height to

be the given size multiplied by the zoom factor (the canvas pixel size remains untouched).

If you have enabled `autoCenter`, it is then passed to the `updateCenter` method and

the margins are set, allowing the canvas to be centered based on its parent element

alone. Finally, the `displayScale` is adjusted and the RESIZE event dispatched.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of the game. |
| --- | --- | --- | --- |
| height | number | No | The new height of the game. |

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - The Scale Manager instance.

**Fires:** [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L801](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L801)  
> Since: 3.16.0

---

## setGameSize

### <instance> setGameSize(width, height)

**Description:**

This method will set a new size for your game.

It should only be used if you're looking to change the base size of your game and are using

one of the Scale Manager scaling modes, i.e. `FIT`. If you're using `NONE` and wish to

change the game and canvas size directly, then please use the `resize` method instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of the game. |
| --- | --- | --- | --- |
| height | number | No | The new height of the game. |

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - The Scale Manager instance.

**Fires:** [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L750](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L750)  
> Since: 3.16.0

---

## setMaxZoom

### <instance> setMaxZoom()

**Description:**

Sets the zoom to be the maximum possible based on the *current* parent size.

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - The Scale Manager instance.

**Fires:** [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L902](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L902)  
> Since: 3.16.0

---

## setParentSize

### <instance> setParentSize(width, height)

**Description:**

This method will set the size of the Parent Size component, which is used in scaling

and centering calculations. You only need to call this method if you have explicitly

disabled the use of a parent in your game config, but still wish to take advantage of

other Scale Manager features.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of the parent. |
| --- | --- | --- | --- |
| height | number | No | The new height of the parent. |

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - The Scale Manager instance.

**Fires:** [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L728](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L728)  
> Since: 3.16.0

---

## setSnap

### <instance> setSnap([snapWidth], [snapHeight])

**Description:**

By setting a Snap value, when the browser size is modified, its dimensions will automatically

be snapped to the nearest grid slice, using floor. For example, if you have snap value of 16,

and the width changes to 68, then it will snap down to 64 (the closest multiple of 16 when floored)

This mode is best used with the `FIT` scale mode.

Call this method with no arguments to reset the snap values.

Calling this method automatically invokes `ScaleManager.refresh` which emits a `RESIZE` event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| snapWidth | number | Yes | 0 | The amount to snap the width to. If you don't want to snap the width, pass a value of zero. |
| --- | --- | --- | --- | --- |
| snapHeight | number | Yes | "snapWidth" | The amount to snap the height to. If not provided it will use the `snapWidth` value. If you don't want to snap the height, pass a value of zero. |

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - The Scale Manager instance.

**Fires:** [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L919](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L919)  
> Since: 3.80.0

---

## setZoom

### <instance> setZoom(value)

**Description:**

Sets the zoom value of the Scale Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new zoom value of the game. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scale.ScaleManager](scale-scalemanager.md) - The Scale Manager instance.

**Fires:** [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L883](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L883)  
> Since: 3.16.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## startFullscreen

### <instance> startFullscreen([fullscreenOptions])

**Description:**

Sends a request to the browser to ask it to go in to full screen mode, using the {@link <https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API> Fullscreen API}.

If the browser does not support this, a `FULLSCREEN_UNSUPPORTED` event will be emitted.

This method *must* be called from a `pointerup` user-input gesture (**not** `pointerdown`). You cannot launch

games fullscreen without this, as most browsers block it. Games within an iframe will also be blocked

from fullscreen unless the iframe has the `allowfullscreen` attribute.

On touch devices, such as Android and iOS Safari, you should always use `pointerup` and NOT `pointerdown`,

otherwise the request will fail unless the document in which your game is embedded has already received

some form of touch input, which you cannot guarantee. Activating fullscreen via `pointerup` circumvents

this issue.

Performing an action that navigates to another page, or opens another tab, will automatically cancel

fullscreen mode, as will the user pressing the ESC key. To cancel fullscreen mode directly from your game,

i.e. by clicking an icon, call the `stopFullscreen` method.

A browser can only send one DOM element into fullscreen. You can control which element this is by

setting the `fullscreenTarget` property in your game config, or changing the property in the Scale Manager.

Note that the game canvas *must* be a child of the target. If you do not give a target, Phaser will

automatically create a blank `<div>` element and move the canvas into it, before going fullscreen.

When it leaves fullscreen, the div will be removed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fullscreenOptions | object | Yes | The FullscreenOptions dictionary is used to provide configuration options when entering full screen. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scale.Events#event:ENTER\_FULLSCREEN](../event/scale-events.md), [Phaser.Scale.Events#event:FULLSCREEN\_FAILED](../event/scale-events.md), [Phaser.Scale.Events#event:FULLSCREEN\_UNSUPPORTED](../event/scale-events.md), [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L1281](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1281)  
> Since: 3.16.0

---

## startListeners

### <instance> startListeners()

**Description:**

An internal method that starts the different DOM event listeners running.

> Source: [src/scale/ScaleManager.js#L1511](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1511)  
> Since: 3.16.0

---

## step

### <instance> step(time, delta)

**Description:**

Internal method, called automatically by the game step.

Monitors the elapsed time and resize interval to see if a parent bounds check needs to take place.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The time value from the most recent Game step. Typically a high-resolution timer value, or Date.now(). |
| --- | --- | --- | --- |
| delta | number | No | The delta value since the last frame. This is smoothed to avoid delta spikes by the TimeStep class. |

> Source: [src/scale/ScaleManager.js#L1675](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1675)  
> Since: 3.16.0

---

## stopFullscreen

### <instance> stopFullscreen()

**Description:**

Calling this method will cancel fullscreen mode, if the browser has entered it.

**Fires:** [Phaser.Scale.Events#event:FULLSCREEN\_UNSUPPORTED](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L1437](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1437)  
> Since: 3.16.0

---

## stopListeners

### <instance> stopListeners()

**Description:**

Stops all DOM event listeners.

> Source: [src/scale/ScaleManager.js#L1707](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1707)  
> Since: 3.16.0

---

## toggleFullscreen

### <instance> toggleFullscreen([fullscreenOptions])

**Description:**

Toggles the fullscreen mode. If already in fullscreen, calling this will cancel it.

If not in fullscreen, this will request the browser to enter fullscreen mode.

If the browser does not support this, a `FULLSCREEN_UNSUPPORTED` event will be emitted.

This method *must* be called from a user-input gesture, such as `pointerdown`. You cannot launch

games fullscreen without this, as most browsers block it. Games within an iframe will also be blocked

from fullscreen unless the iframe has the `allowfullscreen` attribute.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fullscreenOptions | object | Yes | The FullscreenOptions dictionary is used to provide configuration options when entering full screen. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scale.Events#event:ENTER\_FULLSCREEN](../event/scale-events.md), [Phaser.Scale.Events#event:LEAVE\_FULLSCREEN](../event/scale-events.md), [Phaser.Scale.Events#event:FULLSCREEN\_UNSUPPORTED](../event/scale-events.md), [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L1480](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1480)  
> Since: 3.16.0

---

## transformX

### <instance> transformX(pageX)

**Description:**

Transforms the pageX value into the scaled coordinate space of the Scale Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pageX | number | No | The DOM pageX value. |
| --- | --- | --- | --- |

**Returns:** number - The translated value.

> Source: [src/scale/ScaleManager.js#L1251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1251)  
> Since: 3.16.0

---

## transformY

### <instance> transformY(pageY)

**Description:**

Transforms the pageY value into the scaled coordinate space of the Scale Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pageY | number | No | The DOM pageY value. |
| --- | --- | --- | --- |

**Returns:** number - The translated value.

> Source: [src/scale/ScaleManager.js#L1266](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1266)  
> Since: 3.16.0

---

## updateBounds

### <instance> updateBounds()

**Description:**

Updates the `canvasBounds` rectangle to match the bounding client rectangle of the

canvas element being used to track input events.

> Source: [src/scale/ScaleManager.js#L1233](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1233)  
> Since: 3.16.0

---

## updateCenter

### <instance> updateCenter()

**Description:**

Calculates and updates the canvas CSS style in order to center it within the

bounds of its parent. If you have explicitly set parent to be `null` in your

game config then this method will likely give incorrect results unless you have called the

`setParentSize` method first.

It works by modifying the canvas CSS `marginLeft` and `marginTop` properties.

If they have already been set by your own style sheet, or code, this will overwrite them.

To prevent the Scale Manager from centering the canvas, either do not set the

`autoCenter` property in your game config, or make sure it is set to `NO_CENTER`.

> Source: [src/scale/ScaleManager.js#L1180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1180)  
> Since: 3.16.0

---

## updateOrientation

### <instance> updateOrientation()

**Description:**

Internal method that checks the current screen orientation, only if the internal check flag is set.

If the orientation has changed it updates the orientation property and then dispatches the orientation change event.

**Fires:** [Phaser.Scale.Events#event:ORIENTATION\_CHANGE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L997](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L997)  
> Since: 3.16.0

---

## updateScale

### <instance> updateScale()

**Description:**

Internal method that manages updating the size components based on the scale mode.

> Source: [src/scale/ScaleManager.js#L1023](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1023)  
> Since: 3.16.0

---

# Private Methods

## fullscreenErrorHandler

### <instance> fullscreenErrorHandler(error)

**Description:**

The browser failed to enter fullscreen mode.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| error | any | No | The DOM error event. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scale.Events#event:FULLSCREEN\_FAILED](../event/scale-events.md), [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L1360](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1360)  
> Since: 3.17.0

---

## fullscreenSuccessHandler

### <instance> fullscreenSuccessHandler()

**Description:**

The browser has successfully entered fullscreen mode.

**Access:** private

**Fires:** [Phaser.Scale.Events#event:ENTER\_FULLSCREEN](../event/scale-events.md), [Phaser.Scale.Events#event:RESIZE](../event/scale-events.md)

> Source: [src/scale/ScaleManager.js#L1342](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/ScaleManager.js#L1342)  
> Since: 3.17.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [\_resetZoom](#_resetzoom)

    - [\_resetZoom: boolean](#_resetzoom-boolean)
  + [autoCenter](#autocenter)

    - [autoCenter: Phaser.Scale.CenterType](#autocenter-phaserscalecentertype)
  + [autoRound](#autoround)

    - [autoRound: boolean](#autoround-boolean)
  + [baseSize](#basesize)

    - [baseSize: Phaser.Structs.Size](#basesize-phaserstructssize)
  + [canvas](#canvas)

    - [canvas: HTMLCanvasElement](#canvas-htmlcanvaselement)
  + [canvasBounds](#canvasbounds)

    - [canvasBounds: Phaser.Geom.Rectangle](#canvasbounds-phasergeomrectangle)
  + [dirty](#dirty)

    - [dirty: boolean](#dirty-boolean)
  + [displayScale](#displayscale)

    - [displayScale: Phaser.Math.Vector2](#displayscale-phasermathvector2)
  + [displaySize](#displaysize)

    - [displaySize: Phaser.Structs.Size](#displaysize-phaserstructssize)
  + [fullscreen](#fullscreen)

    - [fullscreen: Phaser.Device.Fullscreen](#fullscreen-phaserdevicefullscreen)
  + [fullscreenTarget](#fullscreentarget)

    - [fullscreenTarget: any](#fullscreentarget-any)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [gameSize](#gamesize)

    - [gameSize: Phaser.Structs.Size](#gamesize-phaserstructssize)
  + [height](#height)

    - [height: number](#height-number)
  + [isFullscreen](#isfullscreen)

    - [isFullscreen: boolean](#isfullscreen-boolean)
  + [isGameLandscape](#isgamelandscape)

    - [isGameLandscape: boolean](#isgamelandscape-boolean)
  + [isGamePortrait](#isgameportrait)

    - [isGamePortrait: boolean](#isgameportrait-boolean)
  + [isLandscape](#islandscape)

    - [isLandscape: boolean](#islandscape-boolean)
  + [isPortrait](#isportrait)

    - [isPortrait: boolean](#isportrait-boolean)
  + [orientation](#orientation)

    - [orientation: Phaser.Scale.OrientationType](#orientation-phaserscaleorientationtype)
  + [parent](#parent)

    - [parent: any](#parent-any)
  + [parentIsWindow](#parentiswindow)

    - [parentIsWindow: boolean](#parentiswindow-boolean)
  + [parentSize](#parentsize)

    - [parentSize: Phaser.Structs.Size](#parentsize-phaserstructssize)
  + [resizeInterval](#resizeinterval)

    - [resizeInterval: number](#resizeinterval-number)
  + [scaleMode](#scalemode)

    - [scaleMode: Phaser.Scale.ScaleModeType](#scalemode-phaserscalescalemodetype)
  + [width](#width)

    - [width: number](#width-number)
  + [zoom](#zoom)

    - [zoom: number](#zoom-number)
* [Private Members](#private-members)

  + [\_checkOrientation](#_checkorientation)

    - [\_checkOrientation: boolean](#_checkorientation-boolean)
  + [\_createdFullscreenTarget](#_createdfullscreentarget)

    - [\_createdFullscreenTarget: boolean](#_createdfullscreentarget-boolean)
  + [\_lastCheck](#_lastcheck)

    - [\_lastCheck: number](#_lastcheck-number)
  + [domlisteners](#domlisteners)

    - [domlisteners: object](#domlisteners-object)
* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [getFullscreenTarget](#getfullscreentarget)

    - [<instance> getFullscreenTarget()](#instance-getfullscreentarget)
  + [getMaxZoom](#getmaxzoom)

    - [<instance> getMaxZoom()](#instance-getmaxzoom)
  + [getParent](#getparent)

    - [<instance> getParent(config)](#instance-getparentconfig)
  + [getParentBounds](#getparentbounds)

    - [<instance> getParentBounds()](#instance-getparentbounds)
  + [getViewPort](#getviewport)

    - [<instance> getViewPort([camera], [out])](#instance-getviewportcamera-out)
  + [leaveFullScreenSuccessHandler](#leavefullscreensuccesshandler)

    - [<instance> leaveFullScreenSuccessHandler()](#instance-leavefullscreensuccesshandler)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [lockOrientation](#lockorientation)

    - [<instance> lockOrientation(orientation)](#instance-lockorientationorientation)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [onFullScreenChange](#onfullscreenchange)

    - [<instance> onFullScreenChange()](#instance-onfullscreenchange)
  + [onFullScreenError](#onfullscreenerror)

    - [<instance> onFullScreenError()](#instance-onfullscreenerror)
  + [parseConfig](#parseconfig)

    - [<instance> parseConfig(config)](#instance-parseconfigconfig)
  + [preBoot](#preboot)

    - [<instance> preBoot()](#instance-preboot)
  + [refresh](#refresh)

    - [<instance> refresh([previousWidth], [previousHeight])](#instance-refreshpreviouswidth-previousheight)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeFullscreenTarget](#removefullscreentarget)

    - [<instance> removeFullscreenTarget()](#instance-removefullscreentarget)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [resize](#resize)

    - [<instance> resize(width, height)](#instance-resizewidth-height)
  + [setGameSize](#setgamesize)

    - [<instance> setGameSize(width, height)](#instance-setgamesizewidth-height)
  + [setMaxZoom](#setmaxzoom)

    - [<instance> setMaxZoom()](#instance-setmaxzoom)
  + [setParentSize](#setparentsize)

    - [<instance> setParentSize(width, height)](#instance-setparentsizewidth-height)
  + [setSnap](#setsnap)

    - [<instance> setSnap([snapWidth], [snapHeight])](#instance-setsnapsnapwidth-snapheight)
  + [setZoom](#setzoom)

    - [<instance> setZoom(value)](#instance-setzoomvalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [startFullscreen](#startfullscreen)

    - [<instance> startFullscreen([fullscreenOptions])](#instance-startfullscreenfullscreenoptions)
  + [startListeners](#startlisteners)

    - [<instance> startListeners()](#instance-startlisteners)
  + [step](#step)

    - [<instance> step(time, delta)](#instance-steptime-delta)
  + [stopFullscreen](#stopfullscreen)

    - [<instance> stopFullscreen()](#instance-stopfullscreen)
  + [stopListeners](#stoplisteners)

    - [<instance> stopListeners()](#instance-stoplisteners)
  + [toggleFullscreen](#togglefullscreen)

    - [<instance> toggleFullscreen([fullscreenOptions])](#instance-togglefullscreenfullscreenoptions)
  + [transformX](#transformx)

    - [<instance> transformX(pageX)](#instance-transformxpagex)
  + [transformY](#transformy)

    - [<instance> transformY(pageY)](#instance-transformypagey)
  + [updateBounds](#updatebounds)

    - [<instance> updateBounds()](#instance-updatebounds)
  + [updateCenter](#updatecenter)

    - [<instance> updateCenter()](#instance-updatecenter)
  + [updateOrientation](#updateorientation)

    - [<instance> updateOrientation()](#instance-updateorientation)
  + [updateScale](#updatescale)

    - [<instance> updateScale()](#instance-updatescale)
* [Private Methods](#private-methods)

  + [fullscreenErrorHandler](#fullscreenerrorhandler)

    - [<instance> fullscreenErrorHandler(error)](#instance-fullscreenerrorhandlererror)
  + [fullscreenSuccessHandler](#fullscreensuccesshandler)

    - [<instance> fullscreenSuccessHandler()](#instance-fullscreensuccesshandler)

Back to top

©2025[Phaser](https://docs.phaser.io)