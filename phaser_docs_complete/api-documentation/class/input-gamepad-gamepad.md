# Gamepad

Phaser.Input.Gamepad.Gamepad

A single Gamepad.

These are created, updated and managed by the Gamepad Plugin.

**Constructor**

`new Gamepad(manager, pad)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| manager | [Phaser.Input.Gamepad.GamepadPlugin](input-gamepad-gamepadplugin.md) | No | A reference to the Gamepad Plugin. |
| --- | --- | --- | --- |
| pad | [Phaser.Types.Input.Gamepad.Pad](../typedef/types-input-gamepad.md) | No | The Gamepad object, as extracted from GamepadEvent. |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/input/gamepad/Gamepad.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L13)  
> Since: 3.0.0

# Public Members

## A

### A: boolean

**Description:**

Is the Gamepad's bottom button in the right button cluster being pressed?

If the Gamepad doesn't have this button it will always return false.

On a Dual Shock controller it's the X button.

On an XBox controller it's the A button.

> Source: [src/input/gamepad/Gamepad.js#L609](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L609)  
> Since: 3.10.0

---

## axes

### axes: Array.<[Phaser.Input.Gamepad.Axis](input-gamepad-axis.md)>

**Description:**

An array of Gamepad Axis objects, corresponding to the different axes available on the Gamepad, if any.

> Source: [src/input/gamepad/Gamepad.js#L105](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L105)  
> Since: 3.0.0

---

## B

### B: boolean

**Description:**

Is the Gamepad's right button in the right button cluster being pressed?

If the Gamepad doesn't have this button it will always return false.

On a Dual Shock controller it's the Circle button.

On an XBox controller it's the B button.

> Source: [src/input/gamepad/Gamepad.js#L666](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L666)  
> Since: 3.10.0

---

## buttons

### buttons: Array.<[Phaser.Input.Gamepad.Button](input-gamepad-button.md)>

**Description:**

An array of Gamepad Button objects, corresponding to the different buttons available on the Gamepad.

> Source: [src/input/gamepad/Gamepad.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L89)  
> Since: 3.0.0

---

## connected

### connected: boolean

**Description:**

Is this Gamepad currently connected or not?

> Source: [src/input/gamepad/Gamepad.js#L504](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L504)  
> Since: 3.0.0

---

## down

### down: boolean

**Description:**

Is the Gamepad's Down button being pressed?

If the Gamepad doesn't have this button it will always return false.

This is the d-pad down button under standard Gamepad mapping.

> Source: [src/input/gamepad/Gamepad.js#L591](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L591)  
> Since: 3.10.0

---

## id

### id: string

**Description:**

A string containing some information about the controller.

This is not strictly specified, but in Firefox it will contain three pieces of information

separated by dashes (-): two 4-digit hexadecimal strings containing the USB vendor and

product id of the controller, and the name of the controller as provided by the driver.

In Chrome it will contain the name of the controller as provided by the driver,

followed by vendor and product 4-digit hexadecimal strings.

> Source: [src/input/gamepad/Gamepad.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L56)  
> Since: 3.0.0

---

## index

### index: number

**Description:**

An integer that is unique for each Gamepad currently connected to the system.

This can be used to distinguish multiple controllers.

Note that disconnecting a device and then connecting a new device may reuse the previous index.

> Source: [src/input/gamepad/Gamepad.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L71)  
> Since: 3.0.0

---

## L1

### L1: number

**Description:**

Returns the value of the Gamepad's top left shoulder button.

If the Gamepad doesn't have this button it will always return zero.

The value is a float between 0 and 1, corresponding to how depressed the button is.

On a Dual Shock controller it's the L1 button.

On an XBox controller it's the LB button.

> Source: [src/input/gamepad/Gamepad.js#L685](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L685)  
> Since: 3.10.0

---

## L2

### L2: number

**Description:**

Returns the value of the Gamepad's bottom left shoulder button.

If the Gamepad doesn't have this button it will always return zero.

The value is a float between 0 and 1, corresponding to how depressed the button is.

On a Dual Shock controller it's the L2 button.

On an XBox controller it's the LT button.

> Source: [src/input/gamepad/Gamepad.js#L705](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L705)  
> Since: 3.10.0

---

## left

### left: boolean

**Description:**

Is the Gamepad's Left button being pressed?

If the Gamepad doesn't have this button it will always return false.

This is the d-pad left button under standard Gamepad mapping.

> Source: [src/input/gamepad/Gamepad.js#L537](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L537)  
> Since: 3.10.0

---

## leftStick

### leftStick: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A Vector2 containing the most recent values from the Gamepad's left axis stick.

This is updated automatically as part of the Gamepad.update cycle.

The H Axis is mapped to the `Vector2.x` property, and the V Axis to the `Vector2.y` property.

The values are based on the Axis thresholds.

If the Gamepad does not have a left axis stick, the values will always be zero.

> Source: [src/input/gamepad/Gamepad.js#L291](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L291)  
> Since: 3.10.0

---

## manager

### manager: [Phaser.Input.Gamepad.GamepadPlugin](input-gamepad-gamepadplugin.md)

**Description:**

A reference to the Gamepad Plugin.

> Source: [src/input/gamepad/Gamepad.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L38)  
> Since: 3.0.0

---

## pad

### pad: any

**Description:**

A reference to the native Gamepad object that is connected to the browser.

> Source: [src/input/gamepad/Gamepad.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L47)  
> Since: 3.10.0

---

## R1

### R1: number

**Description:**

Returns the value of the Gamepad's top right shoulder button.

If the Gamepad doesn't have this button it will always return zero.

The value is a float between 0 and 1, corresponding to how depressed the button is.

On a Dual Shock controller it's the R1 button.

On an XBox controller it's the RB button.

> Source: [src/input/gamepad/Gamepad.js#L725](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L725)  
> Since: 3.10.0

---

## R2

### R2: number

**Description:**

Returns the value of the Gamepad's bottom right shoulder button.

If the Gamepad doesn't have this button it will always return zero.

The value is a float between 0 and 1, corresponding to how depressed the button is.

On a Dual Shock controller it's the R2 button.

On an XBox controller it's the RT button.

> Source: [src/input/gamepad/Gamepad.js#L745](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L745)  
> Since: 3.10.0

---

## right

### right: boolean

**Description:**

Is the Gamepad's Right button being pressed?

If the Gamepad doesn't have this button it will always return false.

This is the d-pad right button under standard Gamepad mapping.

> Source: [src/input/gamepad/Gamepad.js#L555](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L555)  
> Since: 3.10.0

---

## rightStick

### rightStick: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

A Vector2 containing the most recent values from the Gamepad's right axis stick.

This is updated automatically as part of the Gamepad.update cycle.

The H Axis is mapped to the `Vector2.x` property, and the V Axis to the `Vector2.y` property.

The values are based on the Axis thresholds.

If the Gamepad does not have a right axis stick, the values will always be zero.

> Source: [src/input/gamepad/Gamepad.js#L304](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L304)  
> Since: 3.10.0

---

## timestamp

### timestamp: number

**Description:**

A timestamp containing the most recent time this Gamepad was updated.

> Source: [src/input/gamepad/Gamepad.js#L521](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L521)  
> Since: 3.0.0

---

## up

### up: boolean

**Description:**

Is the Gamepad's Up button being pressed?

If the Gamepad doesn't have this button it will always return false.

This is the d-pad up button under standard Gamepad mapping.

> Source: [src/input/gamepad/Gamepad.js#L573](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L573)  
> Since: 3.10.0

---

## vibration

### vibration: GamepadHapticActuator

**Description:**

The Gamepad's Haptic Actuator (Vibration / Rumble support).

This is highly experimental and only set if both present on the device,

and exposed by both the hardware and browser.

> Source: [src/input/gamepad/Gamepad.js#L114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L114)  
> Since: 3.10.0

---

## X

### X: boolean

**Description:**

Is the Gamepad's left button in the right button cluster being pressed?

If the Gamepad doesn't have this button it will always return false.

On a Dual Shock controller it's the Square button.

On an XBox controller it's the X button.

> Source: [src/input/gamepad/Gamepad.js#L647](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L647)  
> Since: 3.10.0

---

## Y

### Y: boolean

**Description:**

Is the Gamepad's top button in the right button cluster being pressed?

If the Gamepad doesn't have this button it will always return false.

On a Dual Shock controller it's the Triangle button.

On an XBox controller it's the Y button.

> Source: [src/input/gamepad/Gamepad.js#L628](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L628)  
> Since: 3.10.0

---

# Private Members

## \_created

### \_created: number

**Description:**

When was this Gamepad created? Used to avoid duplicate event spamming in the update loop.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L317](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L317)  
> Since: 3.50.0

---

## \_FBLeftBottom

### \_FBLeftBottom: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Bottom Left Front Button (L2 Shoulder Button)

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L219](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L219)  
> Since: 3.10.0

---

## \_FBLeftTop

### \_FBLeftTop: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Top Left Front Button (L1 Shoulder Button)

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L209)  
> Since: 3.10.0

---

## \_FBRightBottom

### \_FBRightBottom: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Bottom Right Front Button (R2 Shoulder Button)

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L239](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L239)  
> Since: 3.10.0

---

## \_FBRightTop

### \_FBRightTop: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Top Right Front Button (R1 Shoulder Button)

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L229](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L229)  
> Since: 3.10.0

---

## \_HAxisLeft

### \_HAxisLeft: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Horizontal Axis for the Left Stick.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L251)  
> Since: 3.10.0

---

## \_HAxisRight

### \_HAxisRight: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Horizontal Axis for the Right Stick.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L271](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L271)  
> Since: 3.10.0

---

## \_LCBottom

### \_LCBottom: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Bottom Button in the Left Cluster.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L159)  
> Since: 3.10.0

---

## \_LCLeft

### \_LCLeft: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Left Button in the Left Cluster.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L129)  
> Since: 3.10.0

---

## \_LCRight

### \_LCRight: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Right Button in the Left Cluster.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L139)  
> Since: 3.10.0

---

## \_LCTop

### \_LCTop: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Top Button in the Left Cluster.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L149)  
> Since: 3.10.0

---

## \_RCBottom

### \_RCBottom: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Bottom Button in the Right Cluster.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L199)  
> Since: 3.10.0

---

## \_RCLeft

### \_RCLeft: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Left Button in the Right Cluster.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L169)  
> Since: 3.10.0

---

## \_RCRight

### \_RCRight: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Right Button in the Right Cluster.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L179](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L179)  
> Since: 3.10.0

---

## \_RCTop

### \_RCTop: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Top Button in the Right Cluster.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L189)  
> Since: 3.10.0

---

## \_VAxisLeft

### \_VAxisLeft: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Vertical Axis for the Left Stick.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L261](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L261)  
> Since: 3.10.0

---

## \_VAxisRight

### \_VAxisRight: [Phaser.Input.Gamepad.Button](input-gamepad-button.md)

**Description:**

A reference to the Vertical Axis for the Right Stick.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L281](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L281)  
> Since: 3.10.0

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

**Returns:** [Phaser.Input.Gamepad.Gamepad](input-gamepad-gamepad.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this Gamepad instance, its buttons and axes, and releases external references it holds.

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/input/gamepad/Gamepad.js#L475](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L475)  
> Since: 3.10.0

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

## getAxisTotal

### <instance> getAxisTotal()

**Description:**

Gets the total number of axis this Gamepad claims to support.

**Returns:** number - The total number of axes this Gamepad claims to support.

> Source: [src/input/gamepad/Gamepad.js#L328](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L328)  
> Since: 3.10.0

---

## getAxisValue

### <instance> getAxisValue(index)

**Description:**

Gets the value of an axis based on the given index.

The index must be valid within the range of axes supported by this Gamepad.

The return value will be a float between 0 and 1.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the axes to get the value for. |
| --- | --- | --- | --- |

**Returns:** number - The value of the axis, between 0 and 1.

> Source: [src/input/gamepad/Gamepad.js#L341](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L341)  
> Since: 3.10.0

---

## getButtonTotal

### <instance> getButtonTotal()

**Description:**

Gets the total number of buttons this Gamepad claims to have.

**Returns:** number - The total number of buttons this Gamepad claims to have.

> Source: [src/input/gamepad/Gamepad.js#L375](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L375)  
> Since: 3.10.0

---

## getButtonValue

### <instance> getButtonValue(index)

**Description:**

Gets the value of a button based on the given index.

The index must be valid within the range of buttons supported by this Gamepad.

The return value will be either 0 or 1 for an analogue button, or a float between 0 and 1

for a pressure-sensitive digital button, such as the shoulder buttons on a Dual Shock.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the button to get the value for. |
| --- | --- | --- | --- |

**Returns:** number - The value of the button, between 0 and 1.

> Source: [src/input/gamepad/Gamepad.js#L388](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L388)  
> Since: 3.10.0

---

## isButtonDown

### <instance> isButtonDown(index)

**Description:**

Returns if the button is pressed down or not.

The index must be valid within the range of buttons supported by this Gamepad.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the button to get the value for. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the button is considered as being pressed down, otherwise `false`.

> Source: [src/input/gamepad/Gamepad.js#L407](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L407)  
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

**Returns:** [Phaser.Input.Gamepad.Gamepad](input-gamepad-gamepad.md) - `this`.

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

**Returns:** [Phaser.Input.Gamepad.Gamepad](input-gamepad-gamepad.md) - `this`.

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

**Returns:** [Phaser.Input.Gamepad.Gamepad](input-gamepad-gamepad.md) - `this`.

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

**Returns:** [Phaser.Input.Gamepad.Gamepad](input-gamepad-gamepad.md) - `this`.

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

**Returns:** [Phaser.Input.Gamepad.Gamepad](input-gamepad-gamepad.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## setAxisThreshold

### <instance> setAxisThreshold(value)

**Description:**

Sets the threshold value of all axis on this Gamepad.

The value is a float between 0 and 1 and is the amount below which the axis is considered as not having been moved.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | A value between 0 and 1. |
| --- | --- | --- | --- |

> Source: [src/input/gamepad/Gamepad.js#L358](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L358)  
> Since: 3.10.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

# Private Methods

## update

### <instance> update()

**Description:**

Internal update handler for this Gamepad.

Called automatically by the Gamepad Manager as part of its update.

**Access:** private

> Source: [src/input/gamepad/Gamepad.js#L423](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Gamepad.js#L423)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [A](#a)

    - [A: boolean](#a-boolean)
  + [axes](#axes)

    - [axes: Array.<Phaser.Input.Gamepad.Axis>](#axes-arrayphaserinputgamepadaxis)
  + [B](#b)

    - [B: boolean](#b-boolean)
  + [buttons](#buttons)

    - [buttons: Array.<Phaser.Input.Gamepad.Button>](#buttons-arrayphaserinputgamepadbutton)
  + [connected](#connected)

    - [connected: boolean](#connected-boolean)
  + [down](#down)

    - [down: boolean](#down-boolean)
  + [id](#id)

    - [id: string](#id-string)
  + [index](#index)

    - [index: number](#index-number)
  + [L1](#l1)

    - [L1: number](#l1-number)
  + [L2](#l2)

    - [L2: number](#l2-number)
  + [left](#left)

    - [left: boolean](#left-boolean)
  + [leftStick](#leftstick)

    - [leftStick: Phaser.Math.Vector2](#leftstick-phasermathvector2)
  + [manager](#manager)

    - [manager: Phaser.Input.Gamepad.GamepadPlugin](#manager-phaserinputgamepadgamepadplugin)
  + [pad](#pad)

    - [pad: any](#pad-any)
  + [R1](#r1)

    - [R1: number](#r1-number)
  + [R2](#r2)

    - [R2: number](#r2-number)
  + [right](#right)

    - [right: boolean](#right-boolean)
  + [rightStick](#rightstick)

    - [rightStick: Phaser.Math.Vector2](#rightstick-phasermathvector2)
  + [timestamp](#timestamp)

    - [timestamp: number](#timestamp-number)
  + [up](#up)

    - [up: boolean](#up-boolean)
  + [vibration](#vibration)

    - [vibration: GamepadHapticActuator](#vibration-gamepadhapticactuator)
  + [X](#x)

    - [X: boolean](#x-boolean)
  + [Y](#y)

    - [Y: boolean](#y-boolean)
* [Private Members](#private-members)

  + [\_created](#_created)

    - [\_created: number](#_created-number)
  + [\_FBLeftBottom](#_fbleftbottom)

    - [\_FBLeftBottom: Phaser.Input.Gamepad.Button](#_fbleftbottom-phaserinputgamepadbutton)
  + [\_FBLeftTop](#_fblefttop)

    - [\_FBLeftTop: Phaser.Input.Gamepad.Button](#_fblefttop-phaserinputgamepadbutton)
  + [\_FBRightBottom](#_fbrightbottom)

    - [\_FBRightBottom: Phaser.Input.Gamepad.Button](#_fbrightbottom-phaserinputgamepadbutton)
  + [\_FBRightTop](#_fbrighttop)

    - [\_FBRightTop: Phaser.Input.Gamepad.Button](#_fbrighttop-phaserinputgamepadbutton)
  + [\_HAxisLeft](#_haxisleft)

    - [\_HAxisLeft: Phaser.Input.Gamepad.Button](#_haxisleft-phaserinputgamepadbutton)
  + [\_HAxisRight](#_haxisright)

    - [\_HAxisRight: Phaser.Input.Gamepad.Button](#_haxisright-phaserinputgamepadbutton)
  + [\_LCBottom](#_lcbottom)

    - [\_LCBottom: Phaser.Input.Gamepad.Button](#_lcbottom-phaserinputgamepadbutton)
  + [\_LCLeft](#_lcleft)

    - [\_LCLeft: Phaser.Input.Gamepad.Button](#_lcleft-phaserinputgamepadbutton)
  + [\_LCRight](#_lcright)

    - [\_LCRight: Phaser.Input.Gamepad.Button](#_lcright-phaserinputgamepadbutton)
  + [\_LCTop](#_lctop)

    - [\_LCTop: Phaser.Input.Gamepad.Button](#_lctop-phaserinputgamepadbutton)
  + [\_RCBottom](#_rcbottom)

    - [\_RCBottom: Phaser.Input.Gamepad.Button](#_rcbottom-phaserinputgamepadbutton)
  + [\_RCLeft](#_rcleft)

    - [\_RCLeft: Phaser.Input.Gamepad.Button](#_rcleft-phaserinputgamepadbutton)
  + [\_RCRight](#_rcright)

    - [\_RCRight: Phaser.Input.Gamepad.Button](#_rcright-phaserinputgamepadbutton)
  + [\_RCTop](#_rctop)

    - [\_RCTop: Phaser.Input.Gamepad.Button](#_rctop-phaserinputgamepadbutton)
  + [\_VAxisLeft](#_vaxisleft)

    - [\_VAxisLeft: Phaser.Input.Gamepad.Button](#_vaxisleft-phaserinputgamepadbutton)
  + [\_VAxisRight](#_vaxisright)

    - [\_VAxisRight: Phaser.Input.Gamepad.Button](#_vaxisright-phaserinputgamepadbutton)
* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [getAxisTotal](#getaxistotal)

    - [<instance> getAxisTotal()](#instance-getaxistotal)
  + [getAxisValue](#getaxisvalue)

    - [<instance> getAxisValue(index)](#instance-getaxisvalueindex)
  + [getButtonTotal](#getbuttontotal)

    - [<instance> getButtonTotal()](#instance-getbuttontotal)
  + [getButtonValue](#getbuttonvalue)

    - [<instance> getButtonValue(index)](#instance-getbuttonvalueindex)
  + [isButtonDown](#isbuttondown)

    - [<instance> isButtonDown(index)](#instance-isbuttondownindex)
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
  + [setAxisThreshold](#setaxisthreshold)

    - [<instance> setAxisThreshold(value)](#instance-setaxisthresholdvalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
* [Private Methods](#private-methods)

  + [update](#update)

    - [<instance> update()](#instance-update)

Back to top

©2025[Phaser](https://docs.phaser.io)