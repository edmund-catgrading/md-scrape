# Key

Phaser.Input.Keyboard.Key

A generic Key object which can be passed to the Process functions (and so on)

keycode must be an integer

**Constructor**

`new Key(plugin, keyCode)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| plugin | [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) | No | The Keyboard Plugin instance that owns this Key object. |
| --- | --- | --- | --- |
| keyCode | number | No | The keycode of this key. |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/input/keyboard/keys/Key.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L11)  
> Since: 3.0.0

# Public Members

## altKey

### altKey: boolean

**Description:**

The down state of the ALT key, if pressed at the same time as this key.

> Source: [src/input/keyboard/keys/Key.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L92)  
> Since: 3.0.0

---

## ctrlKey

### ctrlKey: boolean

**Description:**

The down state of the CTRL key, if pressed at the same time as this key.

> Source: [src/input/keyboard/keys/Key.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L102)  
> Since: 3.0.0

---

## duration

### duration: number

**Description:**

The number of milliseconds this key was held down for in the previous down - up sequence.

This value isn't updated every game step, only when the Key changes state.

To get the current duration use the `getDuration` method.

> Source: [src/input/keyboard/keys/Key.js#L153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L153)  
> Since: 3.0.0

---

## emitOnRepeat

### emitOnRepeat: boolean

**Description:**

When a key is held down should it continuously fire the `down` event each time it repeats?

By default it will emit the `down` event just once, but if you wish to receive the event

for each repeat as well, enable this property.

> Source: [src/input/keyboard/keys/Key.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L175)  
> Since: 3.16.0

---

## enabled

### enabled: boolean

**Description:**

Can this Key be processed?

> Source: [src/input/keyboard/keys/Key.js#L62](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L62)  
> Since: 3.0.0

---

## isDown

### isDown: boolean

**Description:**

The "down" state of the key. This will remain `true` for as long as the keyboard thinks this key is held down.

> Source: [src/input/keyboard/keys/Key.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L72)  
> Since: 3.0.0

---

## isUp

### isUp: boolean

**Description:**

The "up" state of the key. This will remain `true` for as long as the keyboard thinks this key is up.

> Source: [src/input/keyboard/keys/Key.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L82)  
> Since: 3.0.0

---

## keyCode

### keyCode: number

**Description:**

The keycode of this key.

> Source: [src/input/keyboard/keys/Key.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L44)  
> Since: 3.0.0

---

## location

### location: number

**Description:**

The location of the modifier key. 0 for standard (or unknown), 1 for left, 2 for right, 3 for numpad.

> Source: [src/input/keyboard/keys/Key.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L133)  
> Since: 3.0.0

---

## metaKey

### metaKey: boolean

**Description:**

The down state of the Meta key, if pressed at the same time as this key.

On a Mac the Meta Key is the Command key. On Windows keyboards, it's the Windows key.

> Source: [src/input/keyboard/keys/Key.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L122)  
> Since: 3.16.0

---

## originalEvent

### originalEvent: KeyboardEvent

**Description:**

The original DOM event.

> Source: [src/input/keyboard/keys/Key.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L53)  
> Since: 3.0.0

---

## plugin

### plugin: [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md)

**Description:**

The Keyboard Plugin instance that owns this Key object.

> Source: [src/input/keyboard/keys/Key.js#L35](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L35)  
> Since: 3.17.0

---

## repeats

### repeats: number

**Description:**

If a key is held down this holds down the number of times the key has 'repeated'.

> Source: [src/input/keyboard/keys/Key.js#L188](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L188)  
> Since: 3.0.0

---

## shiftKey

### shiftKey: boolean

**Description:**

The down state of the SHIFT key, if pressed at the same time as this key.

> Source: [src/input/keyboard/keys/Key.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L112)  
> Since: 3.0.0

---

## timeDown

### timeDown: number

**Description:**

The timestamp when the key was last pressed down.

> Source: [src/input/keyboard/keys/Key.js#L143](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L143)  
> Since: 3.0.0

---

## timeUp

### timeUp: number

**Description:**

The timestamp when the key was last released.

> Source: [src/input/keyboard/keys/Key.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L165)  
> Since: 3.0.0

---

# Private Members

## \_justDown

### \_justDown: boolean

**Description:**

True if the key has just been pressed (NOTE: requires to be reset, see justDown getter)

**Access:** private

> Source: [src/input/keyboard/keys/Key.js#L198](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L198)  
> Since: 3.0.0

---

## \_justUp

### \_justUp: boolean

**Description:**

True if the key has just been pressed (NOTE: requires to be reset, see justDown getter)

**Access:** private

> Source: [src/input/keyboard/keys/Key.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L209)  
> Since: 3.0.0

---

## \_tick

### \_tick: number

**Description:**

Internal tick counter.

**Access:** private

> Source: [src/input/keyboard/keys/Key.js#L220](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L220)  
> Since: 3.11.0

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

**Returns:** [Phaser.Input.Keyboard.Key](input-keyboard-key.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Removes any bound event handlers and removes local references.

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/input/keyboard/keys/Key.js#L379](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L379)  
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

## getDuration

### <instance> getDuration()

**Description:**

Returns the duration, in ms, that the Key has been held down for.

If the key is not currently down it will return zero.

To get the duration the Key was held down for in the previous up-down cycle,

use the `Key.duration` property value instead.

**Returns:** number - The duration, in ms, that the Key has been held down for if currently down.

> Source: [src/input/keyboard/keys/Key.js#L354](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L354)  
> Since: 3.17.0

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

**Returns:** [Phaser.Input.Keyboard.Key](input-keyboard-key.md) - `this`.

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

**Returns:** [Phaser.Input.Keyboard.Key](input-keyboard-key.md) - `this`.

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

**Returns:** [Phaser.Input.Keyboard.Key](input-keyboard-key.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## onDown

### <instance> onDown(event)

**Description:**

Processes the Key Down action for this Key.

Called automatically by the Keyboard Plugin.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native DOM Keyboard event. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Input.Keyboard.Events#event:DOWN](../event/input-keyboard-events.md)

> Source: [src/input/keyboard/keys/Key.js#L249](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L249)  
> Since: 3.16.0

---

## onUp

### <instance> onUp(event)

**Description:**

Processes the Key Up action for this Key.

Called automatically by the Keyboard Plugin.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native DOM Keyboard event. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Input.Keyboard.Events#event:UP](../event/input-keyboard-events.md)

> Source: [src/input/keyboard/keys/Key.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L293)  
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

**Returns:** [Phaser.Input.Keyboard.Key](input-keyboard-key.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

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

**Returns:** [Phaser.Input.Keyboard.Key](input-keyboard-key.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## reset

### <instance> reset()

**Description:**

Resets this Key object back to its default un-pressed state.

As of version 3.60.0 it no longer resets the `enabled` or `preventDefault` flags.

**Returns:** [Phaser.Input.Keyboard.Key](input-keyboard-key.md) - This Key instance.

> Source: [src/input/keyboard/keys/Key.js#L325](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L325)  
> Since: 3.6.0

---

## setEmitOnRepeat

### <instance> setEmitOnRepeat(value)

**Description:**

Controls if this Key will continuously emit a `down` event while being held down (true),

or emit the event just once, on first press, and then skip future events (false).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | Emit `down` events on repeated key down actions, or just once? |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.Keyboard.Key](input-keyboard-key.md) - This Key instance.

> Source: [src/input/keyboard/keys/Key.js#L231](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/Key.js#L231)  
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

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [altKey](#altkey)

    - [altKey: boolean](#altkey-boolean)
  + [ctrlKey](#ctrlkey)

    - [ctrlKey: boolean](#ctrlkey-boolean)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [emitOnRepeat](#emitonrepeat)

    - [emitOnRepeat: boolean](#emitonrepeat-boolean)
  + [enabled](#enabled)

    - [enabled: boolean](#enabled-boolean)
  + [isDown](#isdown)

    - [isDown: boolean](#isdown-boolean)
  + [isUp](#isup)

    - [isUp: boolean](#isup-boolean)
  + [keyCode](#keycode)

    - [keyCode: number](#keycode-number)
  + [location](#location)

    - [location: number](#location-number)
  + [metaKey](#metakey)

    - [metaKey: boolean](#metakey-boolean)
  + [originalEvent](#originalevent)

    - [originalEvent: KeyboardEvent](#originalevent-keyboardevent)
  + [plugin](#plugin)

    - [plugin: Phaser.Input.Keyboard.KeyboardPlugin](#plugin-phaserinputkeyboardkeyboardplugin)
  + [repeats](#repeats)

    - [repeats: number](#repeats-number)
  + [shiftKey](#shiftkey)

    - [shiftKey: boolean](#shiftkey-boolean)
  + [timeDown](#timedown)

    - [timeDown: number](#timedown-number)
  + [timeUp](#timeup)

    - [timeUp: number](#timeup-number)
* [Private Members](#private-members)

  + [\_justDown](#_justdown)

    - [\_justDown: boolean](#_justdown-boolean)
  + [\_justUp](#_justup)

    - [\_justUp: boolean](#_justup-boolean)
  + [\_tick](#_tick)

    - [\_tick: number](#_tick-number)
* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [getDuration](#getduration)

    - [<instance> getDuration()](#instance-getduration)
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
  + [onDown](#ondown)

    - [<instance> onDown(event)](#instance-ondownevent)
  + [onUp](#onup)

    - [<instance> onUp(event)](#instance-onupevent)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [reset](#reset)

    - [<instance> reset()](#instance-reset)
  + [setEmitOnRepeat](#setemitonrepeat)

    - [<instance> setEmitOnRepeat(value)](#instance-setemitonrepeatvalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)

Back to top

©2025[Phaser](https://docs.phaser.io)