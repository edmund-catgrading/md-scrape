# FacebookInstantGamesLeaderboard

Phaser.FacebookInstantGamesLeaderboard

This class represents one single Leaderboard that belongs to a Facebook Instant Game.

You do not need to instantiate this class directly, it will be created when you use the

`getLeaderboard()` method of the main plugin.

**Constructor**

`new FacebookInstantGamesLeaderboard(plugin, data)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| plugin | [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md) | No | A reference to the Facebook Instant Games Plugin. |
| --- | --- | --- | --- |
| data | any | No | An Instant Game leaderboard instance. |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/Leaderboard.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L11)  
> Since: 3.13.0

# Public Members

## contextID

### contextID: string

**Description:**

The ID of the context that the leaderboard is associated with, or null if the leaderboard is not tied to a particular context.

> Source: [src/Leaderboard.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L64)  
> Since: 3.13.0

---

## entryCount

### entryCount: integer

**Description:**

The total number of player entries in the leaderboard.

This value defaults to zero. Populate it via the `getEntryCount()` method.

> Source: [src/Leaderboard.js#L73](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L73)  
> Since: 3.13.0

---

## name

### name: string

**Description:**

The name of the leaderboard.

> Source: [src/Leaderboard.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L55)  
> Since: 3.13.0

---

## playerScore

### playerScore: LeaderboardScore

**Description:**

The players score object.

This value defaults to `null`. Populate it via the `getPlayerScore()` method.

> Source: [src/Leaderboard.js#L83](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L83)  
> Since: 3.13.0

---

## plugin

### plugin: [Phaser.FacebookInstantGamesPlugin](facebookinstantgamesplugin.md)

**Description:**

A reference to the Facebook Instant Games Plugin.

> Source: [src/Leaderboard.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L37)  
> Since: 3.13.0

---

## ref

### ref: any

**Description:**

An Instant Game leaderboard instance.

> Source: [src/Leaderboard.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L46)  
> Since: 3.13.0

---

## scores

### scores: Array.<LeaderboardScore>

**Description:**

The scores in the Leaderboard from the currently requested range.

This value defaults to an empty array. Populate it via the `getScores()` method.

The contents of this array are reset each time `getScores()` is called.

> Source: [src/Leaderboard.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L93)  
> Since: 3.13.0

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

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#destroy](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L42)  
> Since: 3.0.0

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

## getConnectedScores

### <instance> getConnectedScores()

**Description:**

Retrieves a set of leaderboard entries, based on the current player's connected players (including the current player), ordered by local rank within the set of connected players.

The data is requested in an async call, so the result isn't available immediately.

When the call completes this Leaderboard will emit the `getconnectedscores` event along with an array of LeaderboardScore entries and the name of the Leaderboard.

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - This Leaderboard instance.

> Source: [src/Leaderboard.js#L271](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L271)  
> Since: 3.16.0

---

## getEntryCount

### <instance> getEntryCount()

**Description:**

Fetches the total number of player entries in the leaderboard.

The data is requested in an async call, so the result isn't available immediately.

When the call completes this Leaderboard will emit the `getentrycount` event along with the count and name of the Leaderboard.

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - This Leaderboard instance.

> Source: [src/Leaderboard.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L107)  
> Since: 3.13.0

---

## getPlayerScore

### <instance> getPlayerScore()

**Description:**

Gets the players leaderboard entry and stores it in the `playerScore` property.

The data is requested in an async call, so the result isn't available immediately.

When the call completes this Leaderboard will emit the `getplayerscore` event along with the score and the name of the Leaderboard.

If the player has not yet saved a score, the event will send `null` as the score value, and `playerScore` will be set to `null` as well.

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - This Leaderboard instance.

> Source: [src/Leaderboard.js#L189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L189)  
> Since: 3.13.0

---

## getScores

### <instance> getScores([count], [offset])

**Description:**

Retrieves a set of leaderboard entries, ordered by score ranking in the leaderboard.

The data is requested in an async call, so the result isn't available immediately.

When the call completes this Leaderboard will emit the `getscores` event along with an array of LeaderboardScore entries and the name of the Leaderboard.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| count | integer | Yes | 10 | The number of entries to attempt to fetch from the leaderboard. Currently, up to a maximum of 100 entries may be fetched per query. |
| --- | --- | --- | --- | --- |
| offset | integer | Yes | 0 | The offset from the top of the leaderboard that entries will be fetched from. |

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - This Leaderboard instance.

> Source: [src/Leaderboard.js#L230](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L230)  
> Since: 3.13.0

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

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - `this`.

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

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - `this`.

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

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - `this`.

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

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - `this`.

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

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## setScore

### <instance> setScore(score, [data])

**Description:**

Updates the player's score. If the player has an existing score, the old score will only be replaced if the new score is better than it.

NOTE: If the leaderboard is associated with a specific context, the game must be in that context to set a score for the player.

The data is requested in an async call, so the result isn't available immediately.

When the call completes this Leaderboard will emit the `setscore` event along with the LeaderboardScore object and the name of the Leaderboard.

If the save fails the event will send `null` as the score value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| score | integer | No | The new score for the player. Must be a 64-bit integer number. |
| --- | --- | --- | --- |
| data | string | any | Yes | Metadata to associate with the stored score. Must be less than 2KB in size. If an object is given it will be passed to `JSON.stringify`. |

**Returns:** [Phaser.FacebookInstantGamesLeaderboard](facebookinstantgamesleaderboard.md) - This Leaderboard instance.

> Source: [src/Leaderboard.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/Leaderboard.js#L137)  
> Since: 3.13.0

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

  + [contextID](#contextid)

    - [contextID: string](#contextid-string)
  + [entryCount](#entrycount)

    - [entryCount: integer](#entrycount-integer)
  + [name](#name)

    - [name: string](#name-string)
  + [playerScore](#playerscore)

    - [playerScore: LeaderboardScore](#playerscore-leaderboardscore)
  + [plugin](#plugin)

    - [plugin: Phaser.FacebookInstantGamesPlugin](#plugin-phaserfacebookinstantgamesplugin)
  + [ref](#ref)

    - [ref: any](#ref-any)
  + [scores](#scores)

    - [scores: Array.<LeaderboardScore>](#scores-arrayleaderboardscore)
* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [getConnectedScores](#getconnectedscores)

    - [<instance> getConnectedScores()](#instance-getconnectedscores)
  + [getEntryCount](#getentrycount)

    - [<instance> getEntryCount()](#instance-getentrycount)
  + [getPlayerScore](#getplayerscore)

    - [<instance> getPlayerScore()](#instance-getplayerscore)
  + [getScores](#getscores)

    - [<instance> getScores([count], [offset])](#instance-getscorescount-offset)
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
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [setScore](#setscore)

    - [<instance> setScore(score, [data])](#instance-setscorescore-data)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)

Back to top

©2025[Phaser](https://docs.phaser.io)