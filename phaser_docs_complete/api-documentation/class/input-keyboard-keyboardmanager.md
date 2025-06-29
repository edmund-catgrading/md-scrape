# KeyboardManager

Phaser.Input.Keyboard.KeyboardManager

The Keyboard Manager is a helper class that belongs to the global Input Manager.

Its role is to listen for native DOM Keyboard Events and then store them for further processing by the Keyboard Plugin.

You do not need to create this class directly, the Input Manager will create an instance of it automatically if keyboard

input has been enabled in the Game Config.

**Constructor**

`new KeyboardManager(inputManager)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| inputManager | [Phaser.Input.InputManager](input-inputmanager.md) | No | A reference to the Input Manager. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/input/keyboard/KeyboardManager.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L14)  
> Since: 3.16.0

# Public Members

## captures

### captures: Array.<number>

**Description:**

An array of Key Code values that will automatically have `preventDefault` called on them,

as long as the `KeyboardManager.preventDefault` boolean is set to `true`.

By default the array is empty.

The key must be non-modified when pressed in order to be captured.

A non-modified key is one that doesn't have a modifier key held down with it. The modifier keys are

shift, control, alt and the meta key (Command on a Mac, the Windows Key on Windows).

Therefore, if the user presses shift + r, it won't prevent this combination, because of the modifier.

However, if the user presses just the r key on its own, it will have its event prevented.

If you wish to stop capturing the keys, for example switching out to a DOM based element, then

you can toggle the `KeyboardManager.preventDefault` boolean at run-time.

If you need more specific control, you can create Key objects and set the flag on each of those instead.

This array can be populated via the Game Config by setting the `input.keyboard.capture` array, or you

can call the `addCapture` method. See also `removeCapture` and `clearCaptures`.

> Source: [src/input/keyboard/KeyboardManager.js#L73](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L73)  
> Since: 3.16.0

---

## enabled

### enabled: boolean

**Description:**

A boolean that controls if the Keyboard Manager is enabled or not.

Can be toggled on the fly.

> Source: [src/input/keyboard/KeyboardManager.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L100)  
> Since: 3.16.0

---

## manager

### manager: [Phaser.Input.InputManager](input-inputmanager.md)

**Description:**

A reference to the Input Manager.

> Source: [src/input/keyboard/KeyboardManager.js#L36](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L36)  
> Since: 3.16.0

---

## onKeyDown

### onKeyDown: function

**Description:**

The Key Down Event handler.

This function is sent the native DOM KeyEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/keyboard/KeyboardManager.js#L121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L121)  
> Since: 3.16.00

---

## onKeyUp

### onKeyUp: function

**Description:**

The Key Up Event handler.

This function is sent the native DOM KeyEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/keyboard/KeyboardManager.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L132)  
> Since: 3.16.00

---

## preventDefault

### preventDefault: boolean

**Description:**

A flag that controls if the non-modified keys, matching those stored in the `captures` array,

have `preventDefault` called on them or not.

A non-modified key is one that doesn't have a modifier key held down with it. The modifier keys are

shift, control, alt and the meta key (Command on a Mac, the Windows Key on Windows).

Therefore, if the user presses shift + r, it won't prevent this combination, because of the modifier.

However, if the user presses just the r key on its own, it will have its event prevented.

If you wish to stop capturing the keys, for example switching out to a DOM based element, then

you can toggle this property at run-time.

> Source: [src/input/keyboard/KeyboardManager.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L55)  
> Since: 3.16.0

---

## target

### target: any

**Description:**

The Keyboard Event target, as defined in the Game Config.

Typically the window in which the game is rendering, but can be any interactive DOM element.

> Source: [src/input/keyboard/KeyboardManager.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L111)  
> Since: 3.16.0

---

# Private Members

## queue

### queue: Array.<KeyboardEvent>

**Description:**

An internal event queue.

**Access:** private

> Source: [src/input/keyboard/KeyboardManager.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L45)  
> Since: 3.16.0

---

# Public Methods

## addCapture

### <instance> addCapture(keycode)

**Description:**

By default when a key is pressed Phaser will not stop the event from propagating up to the browser.

There are some keys this can be annoying for, like the arrow keys or space bar, which make the browser window scroll.

This `addCapture` method enables consuming keyboard event for specific keys so it doesn't bubble up to the the browser

and cause the default browser behavior.

Please note that keyboard captures are global. This means that if you call this method from within a Scene, to say prevent

the SPACE BAR from triggering a page scroll, then it will prevent it for any Scene in your game, not just the calling one.

You can pass in a single key code value, or an array of key codes, or a string:

```
Copy
this.input.keyboard.addCapture(62);


```

An array of key codes:

```
Copy
this.input.keyboard.addCapture([ 62, 63, 64 ]);


```

Or a string:

```
Copy
this.input.keyboard.addCapture('W,S,A,D');


```

To use non-alpha numeric keys, use a string, such as 'UP', 'SPACE' or 'LEFT'.

You can also provide an array mixing both strings and key code integers.

If there are active captures after calling this method, the `preventDefault` property is set to `true`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keycode | string | number | Array.<number> | Array.<any> |
| --- | --- | --- | --- |

> Source: [src/input/keyboard/KeyboardManager.js#L267](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L267)  
> Since: 3.16.0

---

## clearCaptures

### <instance> clearCaptures()

**Description:**

Removes all keyboard captures and sets the `preventDefault` property to `false`.

> Source: [src/input/keyboard/KeyboardManager.js#L402](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L402)  
> Since: 3.16.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this Keyboard Manager instance.

> Source: [src/input/keyboard/KeyboardManager.js#L415](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L415)  
> Since: 3.16.0

---

## removeCapture

### <instance> removeCapture(keycode)

**Description:**

Removes an existing key capture.

Please note that keyboard captures are global. This means that if you call this method from within a Scene, to remove

the capture of a key, then it will remove it for any Scene in your game, not just the calling one.

You can pass in a single key code value, or an array of key codes, or a string:

```
Copy
this.input.keyboard.removeCapture(62);


```

An array of key codes:

```
Copy
this.input.keyboard.removeCapture([ 62, 63, 64 ]);


```

Or a string:

```
Copy
this.input.keyboard.removeCapture('W,S,A,D');


```

To use non-alpha numeric keys, use a string, such as 'UP', 'SPACE' or 'LEFT'.

You can also provide an array mixing both strings and key code integers.

If there are no captures left after calling this method, the `preventDefault` property is set to `false`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keycode | string | number | Array.<number> | Array.<any> |
| --- | --- | --- | --- |

> Source: [src/input/keyboard/KeyboardManager.js#L338](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L338)  
> Since: 3.16.0

---

## startListeners

### <instance> startListeners()

**Description:**

Starts the Keyboard Event listeners running.

This is called automatically and does not need to be manually invoked.

> Source: [src/input/keyboard/KeyboardManager.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L175)  
> Since: 3.16.0

---

## stopListeners

### <instance> stopListeners()

**Description:**

Stops the Key Event listeners.

This is called automatically and does not need to be manually invoked.

> Source: [src/input/keyboard/KeyboardManager.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L237)  
> Since: 3.16.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

The Keyboard Manager boot process.

**Access:** private

> Source: [src/input/keyboard/KeyboardManager.js#L146](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L146)  
> Since: 3.16.0

---

## postUpdate

### <instance> postUpdate()

**Description:**

Clears the event queue.

Called automatically by the Input Manager.

**Access:** private

> Source: [src/input/keyboard/KeyboardManager.js#L254](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardManager.js#L254)  
> Since: 3.16.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [captures](#captures)

    - [captures: Array.<number>](#captures-arraynumber)
  + [enabled](#enabled)

    - [enabled: boolean](#enabled-boolean)
  + [manager](#manager)

    - [manager: Phaser.Input.InputManager](#manager-phaserinputinputmanager)
  + [onKeyDown](#onkeydown)

    - [onKeyDown: function](#onkeydown-function)
  + [onKeyUp](#onkeyup)

    - [onKeyUp: function](#onkeyup-function)
  + [preventDefault](#preventdefault)

    - [preventDefault: boolean](#preventdefault-boolean)
  + [target](#target)

    - [target: any](#target-any)
* [Private Members](#private-members)

  + [queue](#queue)

    - [queue: Array.<KeyboardEvent>](#queue-arraykeyboardevent)
* [Public Methods](#public-methods)

  + [addCapture](#addcapture)

    - [<instance> addCapture(keycode)](#instance-addcapturekeycode)
  + [clearCaptures](#clearcaptures)

    - [<instance> clearCaptures()](#instance-clearcaptures)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [removeCapture](#removecapture)

    - [<instance> removeCapture(keycode)](#instance-removecapturekeycode)
  + [startListeners](#startlisteners)

    - [<instance> startListeners()](#instance-startlisteners)
  + [stopListeners](#stoplisteners)

    - [<instance> stopListeners()](#instance-stoplisteners)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [postUpdate](#postupdate)

    - [<instance> postUpdate()](#instance-postupdate)

Back to top

©2025[Phaser](https://docs.phaser.io)