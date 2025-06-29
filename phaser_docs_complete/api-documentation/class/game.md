# Game

Phaser.Game

The Phaser.Game instance is the main controller for the entire Phaser game. It is responsible

for handling the boot process, parsing the configuration values, creating the renderer,

and setting-up all of the global Phaser systems, such as sound and input.

Once that is complete it will start the Scene Manager and then begin the main game loop.

You should generally avoid accessing any of the systems created by Game, and instead use those

made available to you via the Phaser.Scene Systems class instead.

**Constructor**

`new Game([GameConfig])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| GameConfig | [Phaser.Types.Core.GameConfig](../typedef/types-core.md) | Yes | The configuration object for your Phaser Game instance. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/core/Game.js#L41](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L41)  
> Since: 3.0.0

# Public Members

## anims

### anims: [Phaser.Animations.AnimationManager](animations-animationmanager.md)

**Description:**

An instance of the Animation Manager.

The Animation Manager is a global system responsible for managing all animations used within your game.

> Source: [src/core/Game.js#L156](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L156)  
> Since: 3.0.0

---

## cache

### cache: [Phaser.Cache.CacheManager](cache-cachemanager.md)

**Description:**

An instance of the Cache Manager.

The Cache Manager is a global system responsible for caching, accessing and releasing external game assets.

> Source: [src/core/Game.js#L178](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L178)  
> Since: 3.0.0

---

## canvas

### canvas: HTMLCanvasElement

**Description:**

A reference to the HTML Canvas Element that Phaser uses to render the game.

This is created automatically by Phaser unless you provide a `canvas` property

in your Game Config.

> Source: [src/core/Game.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L103)  
> Since: 3.0.0

---

## config

### config: [Phaser.Core.Config](core-config.md)

**Description:**

The parsed Game Configuration object.

The values stored within this object are read-only and should not be changed at run-time.

> Source: [src/core/Game.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L68)  
> Since: 3.0.0

---

## context

### context: CanvasRenderingContext2D, WebGLRenderingContext

**Description:**

A reference to the Rendering Context belonging to the Canvas Element this game is rendering to.

If the game is running under Canvas it will be a 2d Canvas Rendering Context.

If the game is running under WebGL it will be a WebGL Rendering Context.

This context is created automatically by Phaser unless you provide a `context` property

in your Game Config.

> Source: [src/core/Game.js#L114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L114)  
> Since: 3.0.0

---

## device

### device: [Phaser.DeviceConf](../typedef/phaser.md)

**Description:**

A reference to the Device inspector.

Contains information about the device running this game, such as OS, browser vendor and feature support.

Used by various systems to determine capabilities and code paths.

> Source: [src/core/Game.js#L222](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L222)  
> Since: 3.0.0

---

## domContainer

### domContainer: HTMLDivElement

**Description:**

A reference to an HTML Div Element used as the DOM Element Container.

Only set if `createDOMContainer` is `true` in the game config (by default it is `false`) and

if you provide a parent element to insert the Phaser Game inside.

See the DOM Element Game Object for more details.

> Source: [src/core/Game.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L89)  
> Since: 3.17.0

---

## events

### events: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

An Event Emitter which is used to broadcast game-level events from the global systems.

> Source: [src/core/Game.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L147)  
> Since: 3.0.0

---

## facebook

### facebook: [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md)

**Description:**

An instance of the Facebook Instant Games Plugin.

This will only be available if the plugin has been built into Phaser,

or you're using the special Facebook Instant Games custom build.

> Source: [src/core/Game.js#L289](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L289)  
> Since: 3.13.0

---

## hasFocus

### hasFocus: boolean

**Description:**

Does the window the game is running in currently have focus or not?

This is modified by the VisibilityHandler.

> Source: [src/core/Game.js#L333](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L333)  
> Since: 3.9.0

---

## input

### input: [Phaser.Input.InputManager](input-inputmanager.md)

**Description:**

An instance of the Input Manager.

The Input Manager is a global system responsible for the capture of browser-level input events.

> Source: [src/core/Game.js#L200](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L200)  
> Since: 3.0.0

---

## isBooted

### isBooted: boolean

**Description:**

A flag indicating when this Game instance has finished its boot process.

> Source: [src/core/Game.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L127)  
> Since: 3.0.0

---

## isPaused

### isPaused: boolean

**Description:**

Is the Game currently paused? This will stop everything from updating,

except the `TimeStep` and related RequestAnimationFrame or setTimeout.

Those will continue stepping, but the core Game step will be skipped.

> Source: [src/core/Game.js#L344](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L344)  
> Since: 3.60.0

---

## isRunning

### isRunning: boolean

**Description:**

A flag indicating if this Game is currently running its game step or not.

> Source: [src/core/Game.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L137)  
> Since: 3.0.0

---

## loop

### loop: [Phaser.Core.TimeStep](core-timestep.md)

**Description:**

An instance of the Time Step.

The Time Step is a global system responsible for setting-up and responding to the browser frame events, processing

them and calculating delta values. It then automatically calls the game step.

> Source: [src/core/Game.js#L263](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L263)  
> Since: 3.0.0

---

## plugins

### plugins: [Phaser.Plugins.PluginManager](plugins-pluginmanager.md)

**Description:**

An instance of the Plugin Manager.

The Plugin Manager is a global system that allows plugins to register themselves with it, and can then install

those plugins into Scenes as required.

> Source: [src/core/Game.js#L275](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L275)  
> Since: 3.0.0

---

## registry

### registry: [Phaser.Data.DataManager](data-datamanager.md)

**Description:**

An instance of the Data Manager. This is a global manager, available from any Scene

and allows you to share and exchange your own game-level data or events without having

to use an internal event system.

> Source: [src/core/Game.js#L189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L189)  
> Since: 3.0.0

---

## renderer

### renderer: [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md), [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md)

**Description:**

A reference to either the Canvas or WebGL Renderer that this Game is using.

> Source: [src/core/Game.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L80)  
> Since: 3.0.0

---

## scale

### scale: [Phaser.Scale.ScaleManager](scale-scalemanager.md)

**Description:**

An instance of the Scale Manager.

The Scale Manager is a global system responsible for handling scaling of the game canvas.

> Source: [src/core/Game.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L234)  
> Since: 3.16.0

---

## scene

### scene: [Phaser.Scenes.SceneManager](scenes-scenemanager.md)

**Description:**

An instance of the Scene Manager.

The Scene Manager is a global system responsible for creating, modifying and updating the Scenes in your game.

> Source: [src/core/Game.js#L211](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L211)  
> Since: 3.0.0

---

## sound

### sound: [Phaser.Sound.NoAudioSoundManager](sound-noaudiosoundmanager.md), [Phaser.Sound.HTML5AudioSoundManager](sound-html5audiosoundmanager.md), [Phaser.Sound.WebAudioSoundManager](sound-webaudiosoundmanager.md)

**Description:**

An instance of the base Sound Manager.

The Sound Manager is a global system responsible for the playback and updating of all audio in your game.

You can disable the inclusion of the Sound Manager in your build by toggling the webpack `FEATURE_SOUND` flag.

> Source: [src/core/Game.js#L245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L245)  
> Since: 3.0.0

---

## textures

### textures: [Phaser.Textures.TextureManager](textures-texturemanager.md)

**Description:**

An instance of the Texture Manager.

The Texture Manager is a global system responsible for managing all textures being used by your game.

> Source: [src/core/Game.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L167)  
> Since: 3.0.0

---

# Private Members

## noReturn

### noReturn: boolean

**Description:**

Remove everything when the game is destroyed.

You cannot create a new Phaser instance on the same web page after doing this.

**Access:** private

> Source: [src/core/Game.js#L322](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L322)  
> Since: 3.12.0

---

## pendingDestroy

### pendingDestroy: boolean

**Description:**

Is this Game pending destruction at the start of the next frame?

**Access:** private

> Source: [src/core/Game.js#L302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L302)  
> Since: 3.5.0

---

## removeCanvas

### removeCanvas: boolean

**Description:**

Remove the Canvas once the destroy is over?

**Access:** private

> Source: [src/core/Game.js#L312](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L312)  
> Since: 3.5.0

---

# Public Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically when the DOM is ready. It is responsible for creating the renderer,

displaying the Debug Header, adding the game canvas to the DOM and emitting the 'boot' event.

It listens for a 'ready' event from the base systems and once received it will call `Game.start`.

**Access:** protected

**Fires:** [Phaser.Core.Events#event:BOOT](../event/core-events.md)

> Source: [src/core/Game.js#L359](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L359)  
> Since: 3.0.0

---

## destroy

### <instance> destroy(removeCanvas, [noReturn])

**Description:**

Flags this Game instance as needing to be destroyed on the *next frame*, making this an asynchronous operation.

It will wait until the current frame has completed and then call `runDestroy` internally.

If you need to react to the games eventual destruction, listen for the `DESTROY` event.

If you **do not** need to run Phaser again on the same web page you can set the `noReturn` argument to `true` and it will free-up

memory being held by the core Phaser plugins. If you do need to create another game instance on the same page, leave this as `false`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| removeCanvas | boolean | No |  | Set to `true` if you would like the parent canvas element removed from the DOM, or `false` to leave it in place. |
| --- | --- | --- | --- | --- |
| noReturn | boolean | Yes | false | If `true` all the core Phaser plugins are destroyed. You cannot create another instance of Phaser on the same web page if you do this. |

**Fires:** [Phaser.Core.Events#event:DESTROY](../event/core-events.md)

> Source: [src/core/Game.js#L715](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L715)  
> Since: 3.0.0

---

## getFrame

### <instance> getFrame()

**Description:**

Returns the current game frame.

When the game starts running, the frame is incremented every time Request Animation Frame, or Set Timeout, fires.

**Returns:** number - The current game frame.

> Source: [src/core/Game.js#L687](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L687)  
> Since: 3.16.0

---

## getTime

### <instance> getTime()

**Description:**

Returns the time that the current game step started at, as based on `performance.now`.

**Returns:** number - The current game timestamp.

> Source: [src/core/Game.js#L702](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L702)  
> Since: 3.16.0

---

## headlessStep

### <instance> headlessStep(time, delta)

**Description:**

A special version of the Game Step for the HEADLESS renderer only.

The main Game Step. Called automatically by the Time Step, once per browser frame (typically as a result of

Request Animation Frame, or Set Timeout on very old browsers.)

The step will update the global managers first, then proceed to update each Scene in turn, via the Scene Manager.

This process emits `prerender` and `postrender` events, even though nothing actually displays.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

**Fires:** Phaser.Game#event:PRE\_RENDER, Phaser.Game#event:POST\_RENDER

> Source: [src/core/Game.js#L525](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L525)  
> Since: 3.2.0

---

## onBlur

### <instance> onBlur()

**Description:**

Called automatically by the Visibility Handler.

This will set the main loop into a 'blurred' state, which pauses it.

**Access:** protected

> Source: [src/core/Game.js#L657](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L657)  
> Since: 3.0.0

---

## onFocus

### <instance> onFocus()

**Description:**

Called automatically by the Visibility Handler.

This will set the main loop into a 'focused' state, which resumes it.

**Access:** protected

> Source: [src/core/Game.js#L672](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L672)  
> Since: 3.0.0

---

## onHidden

### <instance> onHidden()

**Description:**

Called automatically by the Visibility Handler.

This will pause the main loop and then emit a pause event.

**Access:** protected

**Fires:** [Phaser.Core.Events#event:PAUSE](../event/core-events.md)

> Source: [src/core/Game.js#L581](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L581)  
> Since: 3.0.0

---

## onVisible

### <instance> onVisible()

**Description:**

Called automatically by the Visibility Handler.

This will resume the main loop and then emit a resume event.

**Access:** protected

**Fires:** [Phaser.Core.Events#event:RESUME](../event/core-events.md)

> Source: [src/core/Game.js#L620](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L620)  
> Since: 3.0.0

---

## pause

### <instance> pause()

**Description:**

This will pause the entire game and emit a `PAUSE` event.

All of Phaser's internal systems will be paused and the game will not re-render.

Note that it does not pause any Loader requests that are currently in-flight.

**Fires:** [Phaser.Core.Events#event:PAUSE](../event/core-events.md)

> Source: [src/core/Game.js#L597](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L597)  
> Since: 3.60.0

---

## resume

### <instance> resume()

**Description:**

This will resume the entire game and emit a `RESUME` event.

All of Phaser's internal systems will be resumed and the game will start rendering again.

**Fires:** [Phaser.Core.Events#event:RESUME](../event/core-events.md)

> Source: [src/core/Game.js#L636](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L636)  
> Since: 3.60.0

---

## start

### <instance> start()

**Description:**

Called automatically by Game.boot once all of the global systems have finished setting themselves up.

By this point the Game is now ready to start the main loop running.

It will also enable the Visibility Handler.

**Access:** protected

> Source: [src/core/Game.js#L421](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L421)  
> Since: 3.0.0

---

## step

### <instance> step(time, delta)

**Description:**

The main Game Step. Called automatically by the Time Step, once per browser frame (typically as a result of

Request Animation Frame, or Set Timeout on very old browsers.)

The step will update the global managers first, then proceed to update each Scene in turn, via the Scene Manager.

It will then render each Scene in turn, via the Renderer. This process emits `prerender` and `postrender` events.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

**Fires:** [Phaser.Core.Events#event:PRE\_STEP](../event/core-events.md), [Phaser.Core.Events#event:STEP](../event/core-events.md), [Phaser.Core.Events#event:POST\_STEP](../event/core-events.md), [Phaser.Core.Events#event:PRE\_RENDER](../event/core-events.md), [Phaser.Core.Events#event:POST\_RENDER](../event/core-events.md)

> Source: [src/core/Game.js#L455](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L455)  
> Since: 3.0.0

---

# Private Methods

## runDestroy

### <instance> runDestroy()

**Description:**

Destroys this Phaser.Game instance, all global systems, all sub-systems and all Scenes.

**Access:** private

> Source: [src/core/Game.js#L742](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L742)  
> Since: 3.5.0

---

## texturesReady

### <instance> texturesReady()

**Description:**

Called automatically when the Texture Manager has finished setting up and preparing the

default textures.

**Access:** private

**Fires:** Phaser.Game#event:READY

> Source: [src/core/Game.js#L404](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/Game.js#L404)  
> Since: 3.12.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [anims](#anims)

    - [anims: Phaser.Animations.AnimationManager](#anims-phaseranimationsanimationmanager)
  + [cache](#cache)

    - [cache: Phaser.Cache.CacheManager](#cache-phasercachecachemanager)
  + [canvas](#canvas)

    - [canvas: HTMLCanvasElement](#canvas-htmlcanvaselement)
  + [config](#config)

    - [config: Phaser.Core.Config](#config-phasercoreconfig)
  + [context](#context)

    - [context: CanvasRenderingContext2D, WebGLRenderingContext](#context-canvasrenderingcontext2d-webglrenderingcontext)
  + [device](#device)

    - [device: Phaser.DeviceConf](#device-phaserdeviceconf)
  + [domContainer](#domcontainer)

    - [domContainer: HTMLDivElement](#domcontainer-htmldivelement)
  + [events](#events)

    - [events: Phaser.Events.EventEmitter](#events-phasereventseventemitter)
  + [facebook](#facebook)

    - [facebook: Phaser.FacebookInstantGamesPlugin](#facebook-phaserfacebookinstantgamesplugin)
  + [hasFocus](#hasfocus)

    - [hasFocus: boolean](#hasfocus-boolean)
  + [input](#input)

    - [input: Phaser.Input.InputManager](#input-phaserinputinputmanager)
  + [isBooted](#isbooted)

    - [isBooted: boolean](#isbooted-boolean)
  + [isPaused](#ispaused)

    - [isPaused: boolean](#ispaused-boolean)
  + [isRunning](#isrunning)

    - [isRunning: boolean](#isrunning-boolean)
  + [loop](#loop)

    - [loop: Phaser.Core.TimeStep](#loop-phasercoretimestep)
  + [plugins](#plugins)

    - [plugins: Phaser.Plugins.PluginManager](#plugins-phaserpluginspluginmanager)
  + [registry](#registry)

    - [registry: Phaser.Data.DataManager](#registry-phaserdatadatamanager)
  + [renderer](#renderer)

    - [renderer: Phaser.Renderer.Canvas.CanvasRenderer, Phaser.Renderer.WebGL.WebGLRenderer](#renderer-phaserrenderercanvascanvasrenderer-phaserrendererwebglwebglrenderer)
  + [scale](#scale)

    - [scale: Phaser.Scale.ScaleManager](#scale-phaserscalescalemanager)
  + [scene](#scene)

    - [scene: Phaser.Scenes.SceneManager](#scene-phaserscenesscenemanager)
  + [sound](#sound)

    - [sound: Phaser.Sound.NoAudioSoundManager, Phaser.Sound.HTML5AudioSoundManager, Phaser.Sound.WebAudioSoundManager](#sound-phasersoundnoaudiosoundmanager-phasersoundhtml5audiosoundmanager-phasersoundwebaudiosoundmanager)
  + [textures](#textures)

    - [textures: Phaser.Textures.TextureManager](#textures-phasertexturestexturemanager)
* [Private Members](#private-members)

  + [noReturn](#noreturn)

    - [noReturn: boolean](#noreturn-boolean)
  + [pendingDestroy](#pendingdestroy)

    - [pendingDestroy: boolean](#pendingdestroy-boolean)
  + [removeCanvas](#removecanvas)

    - [removeCanvas: boolean](#removecanvas-boolean)
* [Public Methods](#public-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy(removeCanvas, [noReturn])](#instance-destroyremovecanvas-noreturn)
  + [getFrame](#getframe)

    - [<instance> getFrame()](#instance-getframe)
  + [getTime](#gettime)

    - [<instance> getTime()](#instance-gettime)
  + [headlessStep](#headlessstep)

    - [<instance> headlessStep(time, delta)](#instance-headlesssteptime-delta)
  + [onBlur](#onblur)

    - [<instance> onBlur()](#instance-onblur)
  + [onFocus](#onfocus)

    - [<instance> onFocus()](#instance-onfocus)
  + [onHidden](#onhidden)

    - [<instance> onHidden()](#instance-onhidden)
  + [onVisible](#onvisible)

    - [<instance> onVisible()](#instance-onvisible)
  + [pause](#pause)

    - [<instance> pause()](#instance-pause)
  + [resume](#resume)

    - [<instance> resume()](#instance-resume)
  + [start](#start)

    - [<instance> start()](#instance-start)
  + [step](#step)

    - [<instance> step(time, delta)](#instance-steptime-delta)
* [Private Methods](#private-methods)

  + [runDestroy](#rundestroy)

    - [<instance> runDestroy()](#instance-rundestroy)
  + [texturesReady](#texturesready)

    - [<instance> texturesReady()](#instance-texturesready)

Back to top

©2025[Phaser](https://docs.phaser.io)