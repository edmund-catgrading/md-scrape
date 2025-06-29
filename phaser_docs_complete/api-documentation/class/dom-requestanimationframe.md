# RequestAnimationFrame

Phaser.DOM.RequestAnimationFrame

Abstracts away the use of RAF or setTimeOut for the core game update loop.

This is invoked automatically by the Phaser.Game instance.

**Scope**: static

> Source: [src/dom/RequestAnimationFrame.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L10)  
> Since: 3.0.0

# Public Members

## callback

### callback: FrameRequestCallback

**Description:**

The callback to be invoked each step.

> Source: [src/dom/RequestAnimationFrame.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L37)  
> Since: 3.0.0

---

## delay

### delay: number

**Description:**

The delay rate in ms for setTimeOut.

> Source: [src/dom/RequestAnimationFrame.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L66)  
> Since: 3.60.0

---

## isRunning

### isRunning: boolean

**Description:**

True if RequestAnimationFrame is running, otherwise false.

> Source: [src/dom/RequestAnimationFrame.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L27)  
> Since: 3.0.0

---

## isSetTimeOut

### isSetTimeOut: boolean

**Description:**

True if the step is using setTimeout instead of RAF.

> Source: [src/dom/RequestAnimationFrame.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L46)  
> Since: 3.0.0

---

## step

### step: FrameRequestCallback

**Description:**

The RAF step function.

Invokes the callback and schedules another call to requestAnimationFrame.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The timestamp passed in from RequestAnimationFrame. |
| --- | --- | --- | --- |

> Source: [src/dom/RequestAnimationFrame.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L78)  
> Since: 3.0.0

---

## stepTimeout

### stepTimeout: function

**Description:**

The SetTimeout step function.

Invokes the callback and schedules another call to setTimeout.

> Source: [src/dom/RequestAnimationFrame.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L99)  
> Since: 3.0.0

---

## timeOutID

### timeOutID: number

**Description:**

The setTimeout or RAF callback ID used when canceling them.

> Source: [src/dom/RequestAnimationFrame.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L56)  
> Since: 3.0.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Stops the step from running and clears the callback reference.

> Source: [src/dom/RequestAnimationFrame.js#L168](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L168)  
> Since: 3.0.0

---

## start

### <instance> start(callback, forceSetTimeOut, delay)

**Description:**

Starts the requestAnimationFrame or setTimeout process running.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | FrameRequestCallback | No | The callback to invoke each step. |
| --- | --- | --- | --- |
| forceSetTimeOut | boolean | No | Should it use SetTimeout, even if RAF is available? |
| delay | number | No | The setTimeout delay rate in ms. |

> Source: [src/dom/RequestAnimationFrame.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L120)  
> Since: 3.0.0

---

## stop

### <instance> stop()

**Description:**

Stops the requestAnimationFrame or setTimeout from running.

> Source: [src/dom/RequestAnimationFrame.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RequestAnimationFrame.js#L148)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [callback](#callback)

    - [callback: FrameRequestCallback](#callback-framerequestcallback)
  + [delay](#delay)

    - [delay: number](#delay-number)
  + [isRunning](#isrunning)

    - [isRunning: boolean](#isrunning-boolean)
  + [isSetTimeOut](#issettimeout)

    - [isSetTimeOut: boolean](#issettimeout-boolean)
  + [step](#step)

    - [step: FrameRequestCallback](#step-framerequestcallback)
  + [stepTimeout](#steptimeout)

    - [stepTimeout: function](#steptimeout-function)
  + [timeOutID](#timeoutid)

    - [timeOutID: number](#timeoutid-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [start](#start)

    - [<instance> start(callback, forceSetTimeOut, delay)](#instance-startcallback-forcesettimeout-delay)
  + [stop](#stop)

    - [<instance> stop()](#instance-stop)

Back to top

©2025[Phaser](https://docs.phaser.io)