# Events

Events

Events are a way for one system to send a signal, that other systems may listen for and then act upon. For example, if the player clicks their mouse on your game, that will internally emit a sequence of events within Phaser. Or if the Loader finishes downloading a file, that will emit a related event.

Events are a core part of Phaser and you'll find them used throughout the framework. They are used both internally, for one system to talk to another, and externally, for your game code to listen for and respond to. There are hundreds of such events that Phaser will emit during the course of a game.

Events are always emitted by what is known as an Event Emitter. Most systems and Game Objects within Phaser are Event Emitters, meaning they can emit events directly and you can hook event handlers to them.

We adopted this practise because events are extremely common in the web browser. Most browser APIs are event-driven, so it made sense to follow this pattern. It also means that you can easily extend Phaser by adding your own events, or listening for existing ones and responding to them.

## The Event Emitter

Phaser 3 uses a slightly modified [eventemitter3](https://github.com/primus/eventemitter3), as [Phaser.Events.EventEmitter](../../docs/latest/Phaser.Events.EventEmitter.md).

* Event names are strings
* The emitter chooses a default context (`this` value), but listeners can override this
* The emitter chooses the callback arguments
* `on()` is the same as `addListener()`
* `off()` is the same as `removeListener()`
* `off()` with no arguments is the same as `removeAllListeners()`
* `off()` can match event name; event name and listener; or event name, listener, and context; but no other combination
* A listener added with `once()` is removed after its first call

All of [Phaser's events](../../docs/latest/events.md) (names, default context, arguments) are defined in the API.

Some Phaser classes (e.g., GameObject) extend Phaser.Events.EventEmitter directly, and some (e.g., Game, Scene) hold an emitter on their `events` property.

You can emit and listen to your own events on these objects, but don't use any of Phaser's event names (e.g., "update"), and never remove listeners that aren't yours. Be careful of removing more than you meant to with `off()`.

```
Copy// NO (removes all listeners on all events)
this.game.events.off();

// NO (removes all listeners to `step`)
this.game.events.off('step');

// YES (same arguments used on `on()`)
this.game.events.off('step', this.onStep, this);

```

Remember that event emitters just hook up functions to other functions. The emitter doesn't know or care about any state associated with the listener. It's up to you to remove listeners when appropriate.

### Get event emitter

* Scene:

  ```
  Copyvar ee = scene.events;

  ```
* Game object:

  ```
  Copyvar ee = gameObject;

  ```

### Attach listener

```
Copyee.on(eventName, callback, scope);
ee.once(eventName, callback, scope);  // only fire listeners one time

```

Alias

```
Copyee.addListener(eventName, callback, scope);
ee.addListener(eventName, callback, scope, true);  // only fire listeners one time

```

### Fire event

```
Copyee.emit(eventName, parameter0, ...);

```

### Remove listeners

* Remove a listener

  ```
  Copyee.off(eventName, callback, scope);
  ee.off(eventName, callback, scope, true);   // only remove one-time listeners

  ```

  or

  ```
  Copyee.removeListener(eventName, callback, scope); 
  ee.removeListener(eventName, callback, scope, true);  // only remove one-time listeners

  ```
* Remove listeners of an event

  ```
  Copyee.off(eventName);

  ```

  or

  ```
  Copyee.removeListener(eventName); 

  ```
* Remove listeners of all events

  ```
  Copyee.removeAllListeners();

  ```

### Get listeners count

```
Copyvar count = ee.listenerCount(eventName);
//var noListener = (ee.listenerCount(eventName) === 0);

```

### Get listeners

```
Copyvar listeners = ee.listeners(eventName);

```

### Get event names

```
Copyvar names = ee.eventNames();

```

### Listener

```
Copy{
    fn: callback,
    context: scope,
    once: once
}

```

## Custom event emitter class

```
Copyclass MyEventEmitter extends Phaser.Events.EventEmitter {
    // construct() {
    //     super();
    // }

    // destroy() {
    //     super.destroy();
    // }
}

```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)
* [samme](https://github.com/samme)

Updated on June 4, 2025, 1:16 PM UTC

---

[Display](display.md)

[FX](fx.md)

On this page

* [Events](#events)

  + [The Event Emitter](#the-event-emitter)

    - [Get event emitter](#get-event-emitter)
    - [Attach listener](#attach-listener)
    - [Fire event](#fire-event)
    - [Remove listeners](#remove-listeners)
    - [Get listeners count](#get-listeners-count)
    - [Get listeners](#get-listeners)
    - [Get event names](#get-event-names)
    - [Listener](#listener)
  + [Custom event emitter class](#custom-event-emitter-class)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../index.md)



Events