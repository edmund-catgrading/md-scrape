# Input.Keyboard.Events

Phaser.Input.Keyboard.Events

## ANY\_KEY\_DOWN

**Description:** The Global Key Down Event.

This event is dispatched by the Keyboard Plugin when any key on the keyboard is pressed down.

Listen to this event from within a Scene using: `this.input.keyboard.on('keydown', listener)`.

You can also listen for a specific key being pressed. See [Keyboard.Events.KEY\_DOWN]{@linkcode Phaser.Input.Keyboard.Events#event:KEY\_DOWN} for details.

Finally, you can create Key objects, which you can also listen for events from. See [Keyboard.Events.DOWN]{@linkcode Phaser.Input.Keyboard.Events#event:DOWN} for details.

*Note*: Many keyboards are unable to process certain combinations of keys due to hardware limitations known as ghosting.

Read [this article on ghosting]{@link [http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/}](http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/%7D) for details.

Also, please be aware that some browser extensions can disable or override Phaser keyboard handling.

For example, the Chrome extension vimium is known to disable Phaser from using the D key, while EverNote disables the backtick key.

There are others. So, please check your extensions if you find you have specific keys that don't work.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native DOM Keyboard Event. You can inspect this to learn more about the key that was pressed, any modifiers, etc. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Input.Keyboard.Events](../namespace/input-keyboard-events.md)

> Source: [src/input/keyboard/events/ANY\_KEY\_DOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/events/ANY_KEY_DOWN_EVENT.js#L7)  
> Since: 3.0.0

## ANY\_KEY\_UP

**Description:** The Global Key Up Event.

This event is dispatched by the Keyboard Plugin when any key on the keyboard is released.

Listen to this event from within a Scene using: `this.input.keyboard.on('keyup', listener)`.

You can also listen for a specific key being released. See [Keyboard.Events.KEY\_UP]{@linkcode Phaser.Input.Keyboard.Events#event:KEY\_UP} for details.

Finally, you can create Key objects, which you can also listen for events from. See [Keyboard.Events.UP]{@linkcode Phaser.Input.Keyboard.Events#event:UP} for details.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native DOM Keyboard Event. You can inspect this to learn more about the key that was released, any modifiers, etc. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Input.Keyboard.Events](../namespace/input-keyboard-events.md)

> Source: [src/input/keyboard/events/ANY\_KEY\_UP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/events/ANY_KEY_UP_EVENT.js#L7)  
> Since: 3.0.0

## COMBO\_MATCH

**Description:** The Key Combo Match Event.

This event is dispatched by the Keyboard Plugin when a [Key Combo]{@link Phaser.Input.Keyboard.KeyCombo} is matched.

Listen for this event from the Key Plugin after a combo has been created:

```
Copy
this.input.keyboard.createCombo([ 38, 38, 40, 40, 37, 39, 37, 39, 66, 65, 13 ], { resetOnMatch: true });



this.input.keyboard.on('keycombomatch', function (event) {

    console.log('Konami Code entered!');

});


```

| name | type | optional | description |
| --- | --- | --- | --- |
| keycombo | [Phaser.Input.Keyboard.KeyCombo](../class/input-keyboard-keycombo.md) | No | The Key Combo object that was matched. |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native DOM Keyboard Event of the final key in the combo. You can inspect this to learn more about any modifiers, etc. |

**Member of:** [Phaser.Input.Keyboard.Events](../namespace/input-keyboard-events.md)

> Source: [src/input/keyboard/events/COMBO\_MATCH\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/events/COMBO_MATCH_EVENT.js#L7)  
> Since: 3.0.0

## DOWN

**Description:** The Key Down Event.

This event is dispatched by a [Key]{@link Phaser.Input.Keyboard.Key} object when it is pressed.

Listen for this event from the Key object instance directly:

```
Copy
var spaceBar = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);



spaceBar.on('down', listener)


```

You can also create a generic 'global' listener. See [Keyboard.Events.ANY\_KEY\_DOWN]{@linkcode Phaser.Input.Keyboard.Events#event:ANY\_KEY\_DOWN} for details.

| name | type | optional | description |
| --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | No | The Key object that was pressed. |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native DOM Keyboard Event. You can inspect this to learn more about any modifiers, etc. |

**Member of:** [Phaser.Input.Keyboard.Events](../namespace/input-keyboard-events.md)

> Source: [src/input/keyboard/events/DOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/events/DOWN_EVENT.js#L7)  
> Since: 3.0.0

## KEY\_DOWN

**Description:** The Key Down Event.

This event is dispatched by the Keyboard Plugin when any key on the keyboard is pressed down.

Unlike the `ANY_KEY_DOWN` event, this one has a special dynamic event name. For example, to listen for the `A` key being pressed

use the following from within a Scene: `this.input.keyboard.on('keydown-A', listener)`. You can replace the `-A` part of the event

name with any valid [Key Code string]{@link Phaser.Input.Keyboard.KeyCodes}. For example, this will listen for the space bar:

`this.input.keyboard.on('keydown-SPACE', listener)`.

You can also create a generic 'global' listener. See [Keyboard.Events.ANY\_KEY\_DOWN]{@linkcode Phaser.Input.Keyboard.Events#event:ANY\_KEY\_DOWN} for details.

Finally, you can create Key objects, which you can also listen for events from. See [Keyboard.Events.DOWN]{@linkcode Phaser.Input.Keyboard.Events#event:DOWN} for details.

*Note*: Many keyboards are unable to process certain combinations of keys due to hardware limitations known as ghosting.

Read [this article on ghosting]{@link [http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/}](http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/%7D) for details.

Also, please be aware that some browser extensions can disable or override Phaser keyboard handling.

For example, the Chrome extension vimium is known to disable Phaser from using the D key, while EverNote disables the backtick key.

There are others. So, please check your extensions if you find you have specific keys that don't work.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native DOM Keyboard Event. You can inspect this to learn more about the key that was pressed, any modifiers, etc. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Input.Keyboard.Events](../namespace/input-keyboard-events.md)

> Source: [src/input/keyboard/events/KEY\_DOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/events/KEY_DOWN_EVENT.js#L7)  
> Since: 3.0.0

## KEY\_UP

**Description:** The Key Up Event.

This event is dispatched by the Keyboard Plugin when any key on the keyboard is released.

Unlike the `ANY_KEY_UP` event, this one has a special dynamic event name. For example, to listen for the `A` key being released

use the following from within a Scene: `this.input.keyboard.on('keyup-A', listener)`. You can replace the `-A` part of the event

name with any valid [Key Code string]{@link Phaser.Input.Keyboard.KeyCodes}. For example, this will listen for the space bar:

`this.input.keyboard.on('keyup-SPACE', listener)`.

You can also create a generic 'global' listener. See [Keyboard.Events.ANY\_KEY\_UP]{@linkcode Phaser.Input.Keyboard.Events#event:ANY\_KEY\_UP} for details.

Finally, you can create Key objects, which you can also listen for events from. See [Keyboard.Events.UP]{@linkcode Phaser.Input.Keyboard.Events#event:UP} for details.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native DOM Keyboard Event. You can inspect this to learn more about the key that was released, any modifiers, etc. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Input.Keyboard.Events](../namespace/input-keyboard-events.md)

> Source: [src/input/keyboard/events/KEY\_UP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/events/KEY_UP_EVENT.js#L7)  
> Since: 3.0.0

## UP

**Description:** The Key Up Event.

This event is dispatched by a [Key]{@link Phaser.Input.Keyboard.Key} object when it is released.

Listen for this event from the Key object instance directly:

```
Copy
var spaceBar = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);



spaceBar.on('up', listener)


```

You can also create a generic 'global' listener. See [Keyboard.Events.ANY\_KEY\_UP]{@linkcode Phaser.Input.Keyboard.Events#event:ANY\_KEY\_UP} for details.

| name | type | optional | description |
| --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | No | The Key object that was released. |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native DOM Keyboard Event. You can inspect this to learn more about any modifiers, etc. |

**Member of:** [Phaser.Input.Keyboard.Events](../namespace/input-keyboard-events.md)

> Source: [src/input/keyboard/events/UP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/events/UP_EVENT.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Input.Keyboard.Events](#inputkeyboardevents)

  + [ANY\_KEY\_DOWN](#any_key_down)
  + [ANY\_KEY\_UP](#any_key_up)
  + [COMBO\_MATCH](#combo_match)
  + [DOWN](#down)
  + [KEY\_DOWN](#key_down)
  + [KEY\_UP](#key_up)
  + [UP](#up)

Back to top

©2025[Phaser](https://docs.phaser.io)



Input.Keyboard.Events