# KeyboardPlugin

Phaser.Input.Keyboard.KeyboardPlugin

The Keyboard Plugin is an input plugin that belongs to the Scene-owned Input system.

Its role is to listen for native DOM Keyboard Events and then process them.

You do not need to create this class directly, the Input system will create an instance of it automatically.

You can access it from within a Scene using `this.input.keyboard`. For example, you can do:

```
Copy
this.input.keyboard.on('keydown', callback, context);


```

Or, to listen for a specific key:

```
Copy
this.input.keyboard.on('keydown-A', callback, context);


```

You can also create Key objects, which you can then poll in your game loop:

```
Copy
var spaceBar = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);


```

If you have multiple parallel Scenes, each trying to get keyboard input, be sure to disable capture on them to stop them from

stealing input from another Scene in the list. You can do this with `this.input.keyboard.enabled = false` within the

Scene to stop all input, or `this.input.keyboard.preventDefault = false` to stop a Scene halting input on another Scene.

*Note*: Many keyboards are unable to process certain combinations of keys due to hardware limitations known as ghosting.

See <http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/> for more details

and use the site <https://w3c.github.io/uievents/tools/key-event-viewer.html> to test your n-key support in browser.

Also please be aware that certain browser extensions can disable or override Phaser keyboard handling.

For example the Chrome extension vimium is known to disable Phaser from using the D key, while EverNote disables the backtick key.

And there are others. So, please check your extensions before opening Phaser issues about keys that don't work.

**Constructor**

`new KeyboardPlugin(sceneInputPlugin)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| sceneInputPlugin | [Phaser.Input.InputPlugin](input-inputplugin.md) | No | A reference to the Scene Input Plugin that the KeyboardPlugin belongs to. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/input/keyboard/KeyboardPlugin.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L21)  
> Since: 3.10.0

# Public Members

## combos

### combos: Array.<[Phaser.Input.Keyboard.KeyCombo](input-keyboard-keycombo.md)>

**Description:**

An array of KeyCombo objects to process.

> Source: [src/input/keyboard/KeyboardPlugin.js#L142](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L142)  
> Since: 3.10.0

---

## enabled

### enabled: boolean

**Description:**

A boolean that controls if this Keyboard Plugin is enabled or not.

Can be toggled on the fly.

> Source: [src/input/keyboard/KeyboardPlugin.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L122)  
> Since: 3.10.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

A reference to the core game, so we can listen for visibility events.

> Source: [src/input/keyboard/KeyboardPlugin.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L77)  
> Since: 3.16.0

---

## keys

### keys: Array.<[Phaser.Input.Keyboard.Key](input-keyboard-key.md)>

**Description:**

An array of Key objects to process.

> Source: [src/input/keyboard/KeyboardPlugin.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L133)  
> Since: 3.10.0

---

## manager

### manager: [Phaser.Input.Keyboard.KeyboardManager](input-keyboard-keyboardmanager.md)

**Description:**

A reference to the global Keyboard Manager.

> Source: [src/input/keyboard/KeyboardPlugin.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L113)  
> Since: 3.16.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene that this Input Plugin is responsible for.

> Source: [src/input/keyboard/KeyboardPlugin.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L86)  
> Since: 3.10.0

---

## sceneInputPlugin

### sceneInputPlugin: [Phaser.Input.InputPlugin](input-inputplugin.md)

**Description:**

A reference to the Scene Input Plugin that created this Keyboard Plugin.

> Source: [src/input/keyboard/KeyboardPlugin.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L104)  
> Since: 3.10.0

---

## settings

### settings: [Phaser.Types.Scenes.SettingsObject](../typedef/types-scenes.md)

**Description:**

A reference to the Scene Systems Settings.

> Source: [src/input/keyboard/KeyboardPlugin.js#L95](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L95)  
> Since: 3.10.0

---

# Private Members

## prevCode

### prevCode: string

**Description:**

Internal repeat key flag.

**Access:** private

> Source: [src/input/keyboard/KeyboardPlugin.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L151)  
> Since: 3.50.0

---

## prevTime

### prevTime: number

**Description:**

Internal repeat key flag.

**Access:** private

> Source: [src/input/keyboard/KeyboardPlugin.js#L161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L161)  
> Since: 3.50.0

---

## prevType

### prevType: string

**Description:**

Internal repeat key flag.

**Access:** private

> Source: [src/input/keyboard/KeyboardPlugin.js#L171](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L171)  
> Since: 3.50.1

---

## time

### time: number

**Description:**

Internal time value.

**Access:** private

> Source: [src/input/keyboard/KeyboardPlugin.js#L927](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L927)  
> Since: 3.11.0

---

# Public Methods

## addCapture

### <instance> addCapture(keycode)

**Description:**

By default when a key is pressed Phaser will not stop the event from propagating up to the browser.

There are some keys this can be annoying for, like the arrow keys or space bar, which make the browser window scroll.

This `addCapture` method enables consuming keyboard events for specific keys, so they don't bubble up the browser

and cause the default behaviors.

Please note that keyboard captures are global. This means that if you call this method from within a Scene, to say prevent

the SPACE BAR from triggering a page scroll, then it will prevent it for any Scene in your game, not just the calling one.

You can pass a single key code value:

```
Copy
this.input.keyboard.addCapture(62);


```

An array of key codes:

```
Copy
this.input.keyboard.addCapture([ 62, 63, 64 ]);


```

Or, a comma-delimited string:

```
Copy
this.input.keyboard.addCapture('W,S,A,D');


```

To use non-alpha numeric keys, use a string, such as 'UP', 'SPACE' or 'LEFT'.

You can also provide an array mixing both strings and key code integers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keycode | string | number | Array.<number> | Array.<any> |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - This KeyboardPlugin object.

> Source: [src/input/keyboard/KeyboardPlugin.js#L243](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L243)  
> Since: 3.16.0

---

## addKey

### <instance> addKey(key, [enableCapture], [emitOnRepeat])

**Description:**

Adds a Key object to this Keyboard Plugin.

The given argument can be either an existing Key object, a string, such as `A` or `SPACE`, or a key code value.

If a Key object is given, and one already exists matching the same key code, the existing one is replaced with the new one.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](input-keyboard-key.md) | string | number | No |  |
| --- | --- | --- | --- | --- |
| enableCapture | boolean | Yes | true | Automatically call `preventDefault` on the native DOM browser event for the key codes being added. |
| emitOnRepeat | boolean | Yes | false | Controls if the Key will continuously emit a 'down' event while being held down (true), or emit the event just once (false, the default). |

**Returns:** [Phaser.Input.Keyboard.Key](input-keyboard-key.md) - The newly created Key object, or a reference to it if it already existed in the keys array.

> Source: [src/input/keyboard/KeyboardPlugin.js#L475](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L475)  
> Since: 3.10.0

---

## addKeys

### <instance> addKeys(keys, [enableCapture], [emitOnRepeat])

**Description:**

A practical way to create an object containing user selected hotkeys.

For example:

```
Copy
this.input.keyboard.addKeys({ 'up': Phaser.Input.Keyboard.KeyCodes.W, 'down': Phaser.Input.Keyboard.KeyCodes.S });


```

would return an object containing the properties (`up` and `down`) mapped to W and S [Phaser.Input.Keyboard.Key](Phaser.Input.Keyboard.Key.md) objects.

You can also pass in a comma-separated string:

```
Copy
this.input.keyboard.addKeys('W,S,A,D');


```

Which will return an object with the properties W, S, A and D mapped to the relevant Key objects.

To use non-alpha numeric keys, use a string, such as 'UP', 'SPACE' or 'LEFT'.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| keys | object | string | No |  | An object containing Key Codes, or a comma-separated string. |
| --- | --- | --- | --- | --- |
| enableCapture | boolean | Yes | true | Automatically call `preventDefault` on the native DOM browser event for the key codes being added. |
| emitOnRepeat | boolean | Yes | false | Controls if the Key will continuously emit a 'down' event while being held down (true), or emit the event just once (false, the default). |

**Returns:** object - An object containing Key objects mapped to the input properties.

> Source: [src/input/keyboard/KeyboardPlugin.js#L413](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L413)  
> Since: 3.10.0

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

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## checkDown

### <instance> checkDown(key, [duration])

**Description:**

Checks if the given Key object is currently being held down.

The difference between this method and checking the `Key.isDown` property directly is that you can provide

a duration to this method. For example, if you wanted a key press to fire a bullet, but you only wanted

it to be able to fire every 100ms, then you can call this method with a `duration` of 100 and it

will only return `true` every 100ms.

If the Keyboard Plugin has been disabled, this method will always return `false`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](input-keyboard-key.md) | No |  | A Key object. |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 0 | The duration which must have elapsed before this Key is considered as being down. |

**Returns:** boolean - `true` if the Key is down within the duration specified, otherwise `false`.

> Source: [src/input/keyboard/KeyboardPlugin.js#L687](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L687)  
> Since: 3.11.0

---

## clearCaptures

### <instance> clearCaptures()

**Description:**

Removes all keyboard captures.

Note that this is a global change. It will clear all event captures across your game, not just for this specific Scene.

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - This KeyboardPlugin object.

> Source: [src/input/keyboard/KeyboardPlugin.js#L376](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L376)  
> Since: 3.16.0

---

## createCombo

### <instance> createCombo(keys, [config])

**Description:**

Creates a new KeyCombo.

A KeyCombo will listen for a specific string of keys from the Keyboard, and when it receives them

it will emit a `keycombomatch` event from this Keyboard Plugin.

The keys to be listened for can be defined as:

A string (i.e. 'ATARI')

An array of either integers (key codes) or strings, or a mixture of both

An array of objects (such as Key objects) with a public 'keyCode' property

For example, to listen for the Konami code (up, up, down, down, left, right, left, right, b, a, enter)

you could pass the following array of key codes:

```
Copy
this.input.keyboard.createCombo([ 38, 38, 40, 40, 37, 39, 37, 39, 66, 65, 13 ], { resetOnMatch: true });



this.input.keyboard.on('keycombomatch', function (event) {

    console.log('Konami Code entered!');

});


```

Or, to listen for the user entering the word PHASER:

```
Copy
this.input.keyboard.createCombo('PHASER');


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keys | string | Array.<number> | Array.<object> | No |
| --- | --- | --- | --- |
| config | [Phaser.Types.Input.Keyboard.KeyComboConfig](../typedef/types-input-keyboard.md) | Yes | A Key Combo configuration object. |

**Returns:** [Phaser.Input.Keyboard.KeyCombo](input-keyboard-keycombo.md) - The new KeyCombo object.

> Source: [src/input/keyboard/KeyboardPlugin.js#L645](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L645)  
> Since: 3.10.0

---

## createCursorKeys

### <instance> createCursorKeys()

**Description:**

Creates and returns an object containing 4 hotkeys for Up, Down, Left and Right, and also Space Bar and shift.

**Returns:** [Phaser.Types.Input.Keyboard.CursorKeys](../typedef/types-input-keyboard.md) - An object containing the properties: `up`, `down`, `left`, `right`, `space` and `shift`.

> Source: [src/input/keyboard/KeyboardPlugin.js#L393](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L393)  
> Since: 3.10.0

---

## disableGlobalCapture

### <instance> disableGlobalCapture()

**Description:**

Disables Phaser from preventing any key captures you may have defined, without actually removing them.

You can use this to temporarily disable event capturing if, for example, you swap to a DOM element.

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - This KeyboardPlugin object.

> Source: [src/input/keyboard/KeyboardPlugin.js#L360](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L360)  
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

## enableGlobalCapture

### <instance> enableGlobalCapture()

**Description:**

Allows Phaser to prevent any key captures you may have defined from bubbling up the browser.

You can use this to re-enable event capturing if you had paused it via `disableGlobalCapture`.

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - This KeyboardPlugin object.

> Source: [src/input/keyboard/KeyboardPlugin.js#L344](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L344)  
> Since: 3.16.0

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

## getCaptures

### <instance> getCaptures()

**Description:**

Returns an array that contains all of the keyboard captures currently enabled.

**Returns:** Array.<number> - An array of all the currently capturing key codes.

> Source: [src/input/keyboard/KeyboardPlugin.js#L331](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L331)  
> Since: 3.16.0

---

## isActive

### <instance> isActive()

**Description:**

Checks to see if both this plugin and the Scene to which it belongs is active.

**Returns:** boolean - `true` if the plugin and the Scene it belongs to is active.

> Source: [src/input/keyboard/KeyboardPlugin.js#L230](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L230)  
> Since: 3.10.0

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

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - `this`.

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

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - `this`.

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

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## removeAllKeys

### <instance> removeAllKeys([destroy], [removeCapture])

**Description:**

Removes all Key objects created by *this* Keyboard Plugin.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| destroy | boolean | Yes | false | Call `Key.destroy` on each removed Key object? |
| --- | --- | --- | --- | --- |
| removeCapture | boolean | Yes | false | Remove all key captures for Key objects owened by this plugin? |

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - This KeyboardPlugin object.

> Source: [src/input/keyboard/KeyboardPlugin.js#L604](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L604)  
> Since: 3.24.0

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

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeCapture

### <instance> removeCapture(keycode)

**Description:**

Removes an existing key capture.

Please note that keyboard captures are global. This means that if you call this method from within a Scene, to remove

the capture of a key, then it will remove it for any Scene in your game, not just the calling one.

You can pass a single key code value:

```
Copy
this.input.keyboard.removeCapture(62);


```

An array of key codes:

```
Copy
this.input.keyboard.removeCapture([ 62, 63, 64 ]);


```

Or, a comma-delimited string:

```
Copy
this.input.keyboard.removeCapture('W,S,A,D');


```

To use non-alpha numeric keys, use a string, such as 'UP', 'SPACE' or 'LEFT'.

You can also provide an array mixing both strings and key code integers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keycode | string | number | Array.<number> | Array.<any> |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - This KeyboardPlugin object.

> Source: [src/input/keyboard/KeyboardPlugin.js#L289](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L289)  
> Since: 3.16.0

---

## removeKey

### <instance> removeKey(key, [destroy], [removeCapture])

**Description:**

Removes a Key object from this Keyboard Plugin.

The given argument can be either a Key object, a string, such as `A` or `SPACE`, or a key code value.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](input-keyboard-key.md) | string | number | No |  |
| --- | --- | --- | --- | --- |
| destroy | boolean | Yes | false | Call `Key.destroy` on the removed Key object? |
| removeCapture | boolean | Yes | false | Remove this Key from being captured? Only applies if set to capture when created. |

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - This KeyboardPlugin object.

> Source: [src/input/keyboard/KeyboardPlugin.js#L541](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L541)  
> Since: 3.10.0

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

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## resetKeys

### <instance> resetKeys()

**Description:**

Resets all Key objects created by *this* Keyboard Plugin back to their default un-pressed states.

This can only reset keys created via the `addKey`, `addKeys` or `createCursorKeys` methods.

If you have created a Key object directly you'll need to reset it yourself.

This method is called automatically when the Keyboard Plugin shuts down, but can be

invoked directly at any time you require.

**Returns:** [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md) - This KeyboardPlugin object.

> Source: [src/input/keyboard/KeyboardPlugin.js#L840](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L840)  
> Since: 3.15.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

> Source: [src/input/keyboard/KeyboardPlugin.js#L185](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L185)  
> Since: 3.10.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this Keyboard Plugin instance and all references it holds, plus clears out local arrays.

**Access:** private

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/input/keyboard/KeyboardPlugin.js#L895](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L895)  
> Since: 3.10.0

---

## shutdown

### <instance> shutdown()

**Description:**

Shuts this Keyboard Plugin down. This performs the following tasks:

1 - Removes all keys created by this Keyboard plugin.

2 - Stops and removes the keyboard event listeners.

3 - Clears out any pending requests in the queue, without processing them.

**Access:** private

**Overrides:** Phaser.Events.EventEmitter#shutdown

> Source: [src/input/keyboard/KeyboardPlugin.js#L869](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L869)  
> Since: 3.10.0

---

## start

### <instance> start()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

> Source: [src/input/keyboard/KeyboardPlugin.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L209)  
> Since: 3.10.0

---

## update

### <instance> update()

**Description:**

Internal update handler called by the Input Plugin, which is in turn invoked by the Game step.

**Access:** private

> Source: [src/input/keyboard/KeyboardPlugin.js#L724](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L724)  
> Since: 3.10.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [combos](#combos)

    - [combos: Array.<Phaser.Input.Keyboard.KeyCombo>](#combos-arrayphaserinputkeyboardkeycombo)
  + [enabled](#enabled)

    - [enabled: boolean](#enabled-boolean)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [keys](#keys)

    - [keys: Array.<Phaser.Input.Keyboard.Key>](#keys-arrayphaserinputkeyboardkey)
  + [manager](#manager)

    - [manager: Phaser.Input.Keyboard.KeyboardManager](#manager-phaserinputkeyboardkeyboardmanager)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [sceneInputPlugin](#sceneinputplugin)

    - [sceneInputPlugin: Phaser.Input.InputPlugin](#sceneinputplugin-phaserinputinputplugin)
  + [settings](#settings)

    - [settings: Phaser.Types.Scenes.SettingsObject](#settings-phasertypesscenessettingsobject)
* [Private Members](#private-members)

  + [prevCode](#prevcode)

    - [prevCode: string](#prevcode-string)
  + [prevTime](#prevtime)

    - [prevTime: number](#prevtime-number)
  + [prevType](#prevtype)

    - [prevType: string](#prevtype-string)
  + [time](#time)

    - [time: number](#time-number)
* [Public Methods](#public-methods)

  + [addCapture](#addcapture)

    - [<instance> addCapture(keycode)](#instance-addcapturekeycode)
  + [addKey](#addkey)

    - [<instance> addKey(key, [enableCapture], [emitOnRepeat])](#instance-addkeykey-enablecapture-emitonrepeat)
  + [addKeys](#addkeys)

    - [<instance> addKeys(keys, [enableCapture], [emitOnRepeat])](#instance-addkeyskeys-enablecapture-emitonrepeat)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [checkDown](#checkdown)

    - [<instance> checkDown(key, [duration])](#instance-checkdownkey-duration)
  + [clearCaptures](#clearcaptures)

    - [<instance> clearCaptures()](#instance-clearcaptures)
  + [createCombo](#createcombo)

    - [<instance> createCombo(keys, [config])](#instance-createcombokeys-config)
  + [createCursorKeys](#createcursorkeys)

    - [<instance> createCursorKeys()](#instance-createcursorkeys)
  + [disableGlobalCapture](#disableglobalcapture)

    - [<instance> disableGlobalCapture()](#instance-disableglobalcapture)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [enableGlobalCapture](#enableglobalcapture)

    - [<instance> enableGlobalCapture()](#instance-enableglobalcapture)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [getCaptures](#getcaptures)

    - [<instance> getCaptures()](#instance-getcaptures)
  + [isActive](#isactive)

    - [<instance> isActive()](#instance-isactive)
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
  + [removeAllKeys](#removeallkeys)

    - [<instance> removeAllKeys([destroy], [removeCapture])](#instance-removeallkeysdestroy-removecapture)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeCapture](#removecapture)

    - [<instance> removeCapture(keycode)](#instance-removecapturekeycode)
  + [removeKey](#removekey)

    - [<instance> removeKey(key, [destroy], [removeCapture])](#instance-removekeykey-destroy-removecapture)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [resetKeys](#resetkeys)

    - [<instance> resetKeys()](#instance-resetkeys)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [start](#start)

    - [<instance> start()](#instance-start)
  + [update](#update)

    - [<instance> update()](#instance-update)

Back to top

©2025[Phaser](https://docs.phaser.io)