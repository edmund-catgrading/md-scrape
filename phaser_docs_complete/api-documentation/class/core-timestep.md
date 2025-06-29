# TimeStep

Phaser.Core.TimeStep

The core runner class that Phaser uses to handle the game loop. It can use either Request Animation Frame,

or SetTimeout, based on browser support and config settings, to create a continuous loop within the browser.

Each time the loop fires, `TimeStep.step` is called and this is then passed onto the core Game update loop,

it is the core heartbeat of your game. It will fire as often as Request Animation Frame is capable of handling

on the target device.

Note that there are lots of situations where a browser will stop updating your game. Such as if the player

switches tabs, or covers up the browser window with another application. In these cases, the 'heartbeat'

of your game will pause, and only resume when focus is returned to it by the player. There is no way to avoid

this situation, all you can do is use the visibility events the browser, and Phaser, provide to detect when

it has happened and then gracefully recover.

**Constructor**

`new TimeStep(game, config)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | A reference to the Phaser.Game instance that owns this Time Step. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Core.FPSConfig](../typedef/types-core.md) | No | No description provided |

---

**Scope**: static

> Source: [src/core/TimeStep.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L14)  
> Since: 3.0.0

# Public Members

## actualFps

### actualFps: number

**Description:**

An exponential moving average of the frames per second.

> Source: [src/core/TimeStep.js#L188](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L188)  
> Since: 3.0.0

---

## callback

### callback: [Phaser.Types.Core.TimeStepCallback](../typedef/types-core.md)

**Description:**

A callback to be invoked each time the TimeStep steps.

> Source: [src/core/TimeStep.js#L223](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L223)  
> Since: 3.0.0

---

## delta

### delta: number

**Description:**

The delta time, in ms, since the last game step. This is a clamped and smoothed average value.

> Source: [src/core/TimeStep.js#L340](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L340)  
> Since: 3.0.0

---

## deltaHistory

### deltaHistory: Array.<number>

**Description:**

Internal array holding the previous delta values, used for delta smoothing.

> Source: [src/core/TimeStep.js#L360](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L360)  
> Since: 3.0.0

---

## deltaIndex

### deltaIndex: number

**Description:**

Internal index of the delta history position.

> Source: [src/core/TimeStep.js#L350](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L350)  
> Since: 3.0.0

---

## deltaSmoothingMax

### deltaSmoothingMax: number

**Description:**

The maximum number of delta values that are retained in order to calculate a smoothed moving average.

This can be changed in the Game Config via the `fps.deltaHistory` property. The default is 10.

> Source: [src/core/TimeStep.js#L369](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L369)  
> Since: 3.0.0

---

## forceSetTimeOut

### forceSetTimeOut: boolean

**Description:**

You can force the TimeStep to use SetTimeOut instead of Request Animation Frame by setting

the `forceSetTimeOut` property to `true` in the Game Configuration object. It cannot be changed at run-time.

> Source: [src/core/TimeStep.js#L233](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L233)  
> Since: 3.0.0

---

## fpsLimit

### fpsLimit: number

**Description:**

Enforce a frame rate limit. This forces how often the Game step will run. By default it is zero,

which means it will run at whatever limit the browser (via RequestAnimationFrame) can handle, which

is the optimum rate for fast-action or responsive games.

However, if you are building a non-game app, like a graphics generator, or low-intensity game that doesn't

require 60fps, then you can lower the step rate via this Game Config value:

```
Copy
fps: {

  limit: 30

}


```

Setting this *beyond* the rate of RequestAnimationFrame will make no difference at all.

Use it purely to *restrict* updates in low-intensity situations only.

> Source: [src/core/TimeStep.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L115)  
> Since: 3.60.0

---

## frame

### frame: number

**Description:**

The current frame the game is on. This counter is incremented once every game step, regardless of how much

time has passed and is unaffected by delta smoothing.

> Source: [src/core/TimeStep.js#L282](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L282)  
> Since: 3.0.0

---

## framesThisSecond

### framesThisSecond: number

**Description:**

The number of frames processed this second.

> Source: [src/core/TimeStep.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L212)  
> Since: 3.0.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

A reference to the Phaser.Game instance.

> Source: [src/core/TimeStep.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L43)  
> Since: 3.0.0

---

## hasFpsLimit

### hasFpsLimit: boolean

**Description:**

Is the FPS rate limited?

This is set by setting the Game Config `limit` value to a value above zero.

Consider this property as read-only.

> Source: [src/core/TimeStep.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L140)  
> Since: 3.60.0

---

## inFocus

### inFocus: boolean

**Description:**

Is the browser currently considered in focus by the Page Visibility API?

This value is set in the `blur` method, which is called automatically by the Game instance.

> Source: [src/core/TimeStep.js#L294](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L294)  
> Since: 3.0.0

---

## lastTime

### lastTime: number

**Description:**

The time of the previous step.

This is typically a high resolution timer value, as provided by Request Animation Frame.

> Source: [src/core/TimeStep.js#L270](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L270)  
> Since: 3.0.0

---

## minFps

### minFps: number

**Description:**

The minimum fps rate you want the Time Step to run at.

Setting this cannot guarantee the browser runs at this rate, it merely influences

the internal timing values to help the Timestep know when it has gone out of sync.

> Source: [src/core/TimeStep.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L88)  
> Since: 3.0.0

---

## nextFpsUpdate

### nextFpsUpdate: number

**Description:**

The time at which the next fps rate update will take place.

When an fps update happens, the `framesThisSecond` value is reset.

> Source: [src/core/TimeStep.js#L199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L199)  
> Since: 3.0.0

---

## now

### now: number

**Description:**

The time, set at the start of the current step.

This is typically a high resolution timer value, as provided by Request Animation Frame.

This can differ from the `time` value in that it isn't calculated based on the delta value.

> Source: [src/core/TimeStep.js#L407](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L407)  
> Since: 3.18.0

---

## panicMax

### panicMax: number

**Description:**

The number of frames that the cooldown is set to after the browser panics over the FPS rate, usually

as a result of switching tabs and regaining focus.

This can be changed in the Game Config via the `fps.panicMax` property. The default is 120.

> Source: [src/core/TimeStep.js#L381](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L381)  
> Since: 3.0.0

---

## pauseDuration

### pauseDuration: number

**Description:**

The duration of the most recent game pause, if any, in ms.

> Source: [src/core/TimeStep.js#L307](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L307)  
> Since: 3.85.0

---

## raf

### raf: [Phaser.DOM.RequestAnimationFrame](dom-requestanimationframe.md)

**Description:**

The Request Animation Frame DOM Event handler.

> Source: [src/core/TimeStep.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L53)  
> Since: 3.0.0

---

## rawDelta

### rawDelta: number

**Description:**

The actual elapsed time in ms between one update and the next.

Unlike with `delta`, no smoothing, capping, or averaging is applied to this value.

So please be careful when using this value in math calculations.

> Source: [src/core/TimeStep.js#L394](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L394)  
> Since: 3.0.0

---

## running

### running: boolean

**Description:**

A flag that is set once the TimeStep has started running and toggled when it stops.

The difference between this value and `started` is that `running` is toggled when

the TimeStep is sent to sleep, where-as `started` remains `true`, only changing if

the TimeStep is actually stopped, not just paused.

> Source: [src/core/TimeStep.js#L74](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L74)  
> Since: 3.0.0

---

## smoothStep

### smoothStep: boolean

**Description:**

Apply smoothing to the delta value used within Phasers internal calculations?

This can be changed in the Game Config via the `fps.smoothStep` property. The default is `true`.

Smoothing helps settle down the delta values after browser tab switches, or other situations

which could cause significant delta spikes or dips. By default it has been enabled in Phaser 3

since the first version, but is now exposed under this property (and the corresponding game config

`smoothStep` value), to allow you to easily disable it, should you require.

> Source: [src/core/TimeStep.js#L421](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L421)  
> Since: 3.22.0

---

## started

### started: boolean

**Description:**

A flag that is set once the TimeStep has started running and toggled when it stops.

> Source: [src/core/TimeStep.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L63)  
> Since: 3.0.0

---

## startTime

### startTime: number

**Description:**

The time at which the game started running.

This value is adjusted if the game is then paused and resumes.

> Source: [src/core/TimeStep.js#L258](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L258)  
> Since: 3.0.0

---

## targetFps

### targetFps: number

**Description:**

The target fps rate for the Time Step to run at.

Setting this value will not actually change the speed at which the browser runs, that is beyond

the control of Phaser. Instead, it allows you to determine performance issues and if the Time Step

is spiraling out of control.

> Source: [src/core/TimeStep.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L101)  
> Since: 3.0.0

---

## time

### time: number

**Description:**

The time, updated each step by adding the elapsed delta time to the previous value.

This differs from the `TimeStep.now` value, which is the high resolution time value

as provided by Request Animation Frame.

> Source: [src/core/TimeStep.js#L245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L245)  
> Since: 3.0.0

---

# Private Members

## \_coolDown

### \_coolDown: number

**Description:**

An internal counter to allow for the browser 'cooling down' after coming back into focus.

**Access:** private

> Source: [src/core/TimeStep.js#L329](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L329)  
> Since: 3.0.0

---

## \_limitRate

### \_limitRate: number

**Description:**

Internal value holding the fps rate limit in ms.

**Access:** private

> Source: [src/core/TimeStep.js#L154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L154)  
> Since: 3.60.0

---

## \_min

### \_min: number

**Description:**

The minimum fps value in ms.

Defaults to 200ms between frames (i.e. super slow!)

**Access:** private

> Source: [src/core/TimeStep.js#L164](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L164)  
> Since: 3.0.0

---

## \_pauseTime

### \_pauseTime: number

**Description:**

The timestamp at which the game became paused, as determined by the Page Visibility API.

**Access:** private

> Source: [src/core/TimeStep.js#L318](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L318)  
> Since: 3.0.0

---

## \_target

### \_target: number

**Description:**

The target fps value in ms.

Defaults to 16.66ms between frames (i.e. normal)

**Access:** private

> Source: [src/core/TimeStep.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L176)  
> Since: 3.0.0

---

# Public Methods

## blur

### <instance> blur()

**Description:**

Called by the Game instance when the DOM window.onBlur event triggers.

> Source: [src/core/TimeStep.js#L438](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L438)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys the TimeStep. This will stop Request Animation Frame, stop the step, clear the callbacks and null

any objects.

> Source: [src/core/TimeStep.js#L864](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L864)  
> Since: 3.0.0

---

## focus

### <instance> focus()

**Description:**

Called by the Game instance when the DOM window.onFocus event triggers.

> Source: [src/core/TimeStep.js#L449](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L449)  
> Since: 3.0.0

---

## getDuration

### <instance> getDuration()

**Description:**

Gets the duration which the game has been running, in seconds.

**Returns:** number - The duration in seconds.

> Source: [src/core/TimeStep.js#L820](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L820)  
> Since: 3.17.0

---

## getDurationMS

### <instance> getDurationMS()

**Description:**

Gets the duration which the game has been running, in ms.

**Returns:** number - The duration in ms.

> Source: [src/core/TimeStep.js#L833](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L833)  
> Since: 3.17.0

---

## pause

### <instance> pause()

**Description:**

Called when the visibility API says the game is 'hidden' (tab switch out of view, etc)

> Source: [src/core/TimeStep.js#L462](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L462)  
> Since: 3.0.0

---

## resetDelta

### <instance> resetDelta()

**Description:**

Resets the time, lastTime, fps averages and delta history.

Called automatically when a browser sleeps them resumes.

> Source: [src/core/TimeStep.js#L487](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L487)  
> Since: 3.0.0

---

## resume

### <instance> resume()

**Description:**

Called when the visibility API says the game is 'visible' again (tab switch back into view, etc)

> Source: [src/core/TimeStep.js#L473](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L473)  
> Since: 3.0.0

---

## sleep

### <instance> sleep()

**Description:**

Sends the TimeStep to sleep, stopping Request Animation Frame (or SetTimeout) and toggling the `running` flag to false.

> Source: [src/core/TimeStep.js#L767](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L767)  
> Since: 3.0.0

---

## smoothDelta

### <instance> smoothDelta(delta)

**Description:**

Takes the delta value and smooths it based on the previous frames.

Called automatically as part of the step.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The delta value for this step. |
| --- | --- | --- | --- |

**Returns:** number - The smoothed delta value.

> Source: [src/core/TimeStep.js#L551](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L551)  
> Since: 3.60.0

---

## start

### <instance> start(callback)

**Description:**

Starts the Time Step running, if it is not already doing so.

Called automatically by the Game Boot process.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | [Phaser.Types.Core.TimeStepCallback](../typedef/types-core.md) | No | The callback to be invoked each time the Time Step steps. |
| --- | --- | --- | --- |

> Source: [src/core/TimeStep.js#L516](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L516)  
> Since: 3.0.0

---

## step

### <instance> step(time)

**Description:**

The main step method. This is called each time the browser updates, either by Request Animation Frame,

or by Set Timeout. It is responsible for calculating the delta values, frame totals, cool down history and more.

You generally should never call this method directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The timestamp passed in from RequestAnimationFrame or setTimeout. |
| --- | --- | --- | --- |

> Source: [src/core/TimeStep.js#L701](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L701)  
> Since: 3.0.0

---

## stepLimitFPS

### <instance> stepLimitFPS(time)

**Description:**

The main step method with an fps limiter. This is called each time the browser updates, either by Request Animation Frame,

or by Set Timeout. It is responsible for calculating the delta values, frame totals, cool down history and more.

You generally should never call this method directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The timestamp passed in from RequestAnimationFrame or setTimeout. |
| --- | --- | --- | --- |

> Source: [src/core/TimeStep.js#L650](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L650)  
> Since: 3.60.0

---

## stop

### <instance> stop()

**Description:**

Stops the TimeStep running.

**Returns:** [Phaser.Core.TimeStep](core-timestep.md) - The TimeStep object.

> Source: [src/core/TimeStep.js#L846](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L846)  
> Since: 3.0.0

---

## tick

### <instance> tick()

**Description:**

Manually calls `TimeStep.step`.

> Source: [src/core/TimeStep.js#L747](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L747)  
> Since: 3.0.0

---

## updateFPS

### <instance> updateFPS(time)

**Description:**

Update the estimate of the frame rate, `fps`. Every second, the number

of frames that occurred in that second are included in an exponential

moving average of all frames per second, with an alpha of 0.25. This

means that more recent seconds affect the estimated frame rate more than

older seconds.

When a browser window is NOT minimized, but is covered up (i.e. you're using

another app which has spawned a window over the top of the browser), then it

will start to throttle the raf callback time. It waits for a while, and then

starts to drop the frame rate at 1 frame per second until it's down to just over 1fps.

So if the game was running at 60fps, and the player opens a new window, then

after 60 seconds (+ the 'buffer time') it'll be down to 1fps, so rafin'g at 1Hz.

When they make the game visible again, the frame rate is increased at a rate of

approx. 8fps, back up to 60fps (or the max it can obtain)

There is no easy way to determine if this drop in frame rate is because the

browser is throttling raf, or because the game is struggling with performance

because you're asking it to do too much on the device.

Compute the new exponential moving average with an alpha of 0.25.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The timestamp passed in from RequestAnimationFrame or setTimeout. |
| --- | --- | --- | --- |

> Source: [src/core/TimeStep.js#L615](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L615)  
> Since: 3.60.0

---

## wake

### <instance> wake([seamless])

**Description:**

Wakes-up the TimeStep, restarting Request Animation Frame (or SetTimeout) and toggling the `running` flag to true.

The `seamless` argument controls if the wake-up should adjust the start time or not.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| seamless | boolean | Yes | false | Adjust the startTime based on the lastTime values. |
| --- | --- | --- | --- | --- |

> Source: [src/core/TimeStep.js#L783](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/TimeStep.js#L783)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [actualFps](#actualfps)

    - [actualFps: number](#actualfps-number)
  + [callback](#callback)

    - [callback: Phaser.Types.Core.TimeStepCallback](#callback-phasertypescoretimestepcallback)
  + [delta](#delta)

    - [delta: number](#delta-number)
  + [deltaHistory](#deltahistory)

    - [deltaHistory: Array.<number>](#deltahistory-arraynumber)
  + [deltaIndex](#deltaindex)

    - [deltaIndex: number](#deltaindex-number)
  + [deltaSmoothingMax](#deltasmoothingmax)

    - [deltaSmoothingMax: number](#deltasmoothingmax-number)
  + [forceSetTimeOut](#forcesettimeout)

    - [forceSetTimeOut: boolean](#forcesettimeout-boolean)
  + [fpsLimit](#fpslimit)

    - [fpsLimit: number](#fpslimit-number)
  + [frame](#frame)

    - [frame: number](#frame-number)
  + [framesThisSecond](#framesthissecond)

    - [framesThisSecond: number](#framesthissecond-number)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [hasFpsLimit](#hasfpslimit)

    - [hasFpsLimit: boolean](#hasfpslimit-boolean)
  + [inFocus](#infocus)

    - [inFocus: boolean](#infocus-boolean)
  + [lastTime](#lasttime)

    - [lastTime: number](#lasttime-number)
  + [minFps](#minfps)

    - [minFps: number](#minfps-number)
  + [nextFpsUpdate](#nextfpsupdate)

    - [nextFpsUpdate: number](#nextfpsupdate-number)
  + [now](#now)

    - [now: number](#now-number)
  + [panicMax](#panicmax)

    - [panicMax: number](#panicmax-number)
  + [pauseDuration](#pauseduration)

    - [pauseDuration: number](#pauseduration-number)
  + [raf](#raf)

    - [raf: Phaser.DOM.RequestAnimationFrame](#raf-phaserdomrequestanimationframe)
  + [rawDelta](#rawdelta)

    - [rawDelta: number](#rawdelta-number)
  + [running](#running)

    - [running: boolean](#running-boolean)
  + [smoothStep](#smoothstep)

    - [smoothStep: boolean](#smoothstep-boolean)
  + [started](#started)

    - [started: boolean](#started-boolean)
  + [startTime](#starttime)

    - [startTime: number](#starttime-number)
  + [targetFps](#targetfps)

    - [targetFps: number](#targetfps-number)
  + [time](#time)

    - [time: number](#time-number)
* [Private Members](#private-members)

  + [\_coolDown](#_cooldown)

    - [\_coolDown: number](#_cooldown-number)
  + [\_limitRate](#_limitrate)

    - [\_limitRate: number](#_limitrate-number)
  + [\_min](#_min)

    - [\_min: number](#_min-number)
  + [\_pauseTime](#_pausetime)

    - [\_pauseTime: number](#_pausetime-number)
  + [\_target](#_target)

    - [\_target: number](#_target-number)
* [Public Methods](#public-methods)

  + [blur](#blur)

    - [<instance> blur()](#instance-blur)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [focus](#focus)

    - [<instance> focus()](#instance-focus)
  + [getDuration](#getduration)

    - [<instance> getDuration()](#instance-getduration)
  + [getDurationMS](#getdurationms)

    - [<instance> getDurationMS()](#instance-getdurationms)
  + [pause](#pause)

    - [<instance> pause()](#instance-pause)
  + [resetDelta](#resetdelta)

    - [<instance> resetDelta()](#instance-resetdelta)
  + [resume](#resume)

    - [<instance> resume()](#instance-resume)
  + [sleep](#sleep)

    - [<instance> sleep()](#instance-sleep)
  + [smoothDelta](#smoothdelta)

    - [<instance> smoothDelta(delta)](#instance-smoothdeltadelta)
  + [start](#start)

    - [<instance> start(callback)](#instance-startcallback)
  + [step](#step)

    - [<instance> step(time)](#instance-steptime)
  + [stepLimitFPS](#steplimitfps)

    - [<instance> stepLimitFPS(time)](#instance-steplimitfpstime)
  + [stop](#stop)

    - [<instance> stop()](#instance-stop)
  + [tick](#tick)

    - [<instance> tick()](#instance-tick)
  + [updateFPS](#updatefps)

    - [<instance> updateFPS(time)](#instance-updatefpstime)
  + [wake](#wake)

    - [<instance> wake([seamless])](#instance-wakeseamless)

Back to top

©2025[Phaser](https://docs.phaser.io)