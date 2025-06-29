# Phaser.Tweens

# Phaser.Tweens.Builders

## GetBoolean

### <static> GetBoolean(source, key, defaultValue)

**Description:**

Retrieves the value of the given key from an object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | object | No | The object to retrieve the value from. |
| --- | --- | --- | --- |
| key | string | No | The key to look for in the `source` object. |
| defaultValue | boolean | No | The default value to return if the `key` doesn't exist or if no `source` object is provided. |

**Returns:** boolean - The retrieved value.

> Source: [src/tweens/builders/GetBoolean.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/GetBoolean.js#L7)  
> Since: 3.0.0

## GetEaseFunction

### <static> GetEaseFunction(ease, [easeParams])

**Description:**

This internal function is used to return the correct ease function for a Tween.

It can take a variety of input, including an EaseMap based string, or a custom function.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ease | string | function | No | The ease to find. This can be either a string from the EaseMap, or a custom function. |
| --- | --- | --- | --- |
| easeParams | Array.<number> | Yes | An optional array of ease parameters to go with the ease. |

**Returns:** function - The ease function.

> Source: [src/tweens/builders/GetEaseFunction.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/GetEaseFunction.js#L10)  
> Since: 3.0.0

## GetInterpolationFunction

### <static> GetInterpolationFunction(interpolation)

**Description:**

This internal function is used to return the correct interpolation function for a Tween.

It can take a variety of input, including a string, or a custom function.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| interpolation | string | function | null | No |
| --- | --- | --- | --- |

**Returns:** function - The interpolation function to use, or `null`.

> Source: [src/tweens/builders/GetInterpolationFunction.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/GetInterpolationFunction.js#L18)  
> Since: 3.60.0

## GetNewValue

### <static> GetNewValue(source, key, defaultValue)

**Description:**

Internal function used by the Tween Builder to create a function that will return

the given value from the source.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | any | No | The source object to get the value from. |
| --- | --- | --- | --- |
| key | string | No | The property to get from the source. |
| defaultValue | any | No | A default value to return should the source not have the property set. |

**Returns:** function - A function which, when called, will return the property value from the source.

> Source: [src/tweens/builders/GetNewValue.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/GetNewValue.js#L7)  
> Since: 3.0.0

## GetProps

### <static> GetProps(config)

**Description:**

Internal function used by the Tween Builder to return an array of properties

that the Tween will be operating on. It takes a tween configuration object

and then checks that none of the `props` entries start with an underscore, or that

none of the direct properties are on the Reserved list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](../typedef/types-tweens.md) | No | The configuration object of the Tween to get the properties from. |
| --- | --- | --- | --- |

**Returns:** Array.<string> - An array of all the properties the tween will operate on.

> Source: [src/tweens/builders/GetProps.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/GetProps.js#L9)  
> Since: 3.0.0

## GetTargets

### <static> GetTargets(config)

**Description:**

Extracts an array of targets from a Tween configuration object.

The targets will be looked for in a `targets` property. If it's a function, its return value will be used as the result.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | object | No | The configuration object to use. |
| --- | --- | --- | --- |

**Returns:** array - An array of targets (may contain only one element), or `null` if no targets were specified.

> Source: [src/tweens/builders/GetTargets.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/GetTargets.js#L9)  
> Since: 3.0.0

## GetValueOp

### <static> GetValueOp(key, propertyValue)

**Description:**

Returns `getActive`, `getStart` and `getEnd` functions for a TweenData based on a target property and end value.

`getActive` if not null, is invoked *immediately* as soon as the TweenData is running, and is set on the target property.

`getEnd` is invoked once any start delays have expired and returns what the value should tween to.

`getStart` is invoked when the tween reaches the end and needs to either repeat or yoyo, it returns the value to go back to.

If the end value is a number, it will be treated as an absolute value and the property will be tweened to it.

A string can be provided to specify a relative end value which consists of an operation

(`+=` to add to the current value, `-=` to subtract from the current value, `*=` to multiply the current

value, or `/=` to divide the current value) followed by its operand.

A function can be provided to allow greater control over the end value; it will receive the target

object being tweened, the name of the property being tweened, and the current value of the property

as its arguments and must return a value.

If both the starting and the ending values need to be controlled, an object with `getStart` and `getEnd`

callbacks, which will receive the same arguments, can be provided instead. If an object with a `value`

property is provided, the property will be used as the effective value under the same rules described here.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The name of the property to modify. |
| --- | --- | --- | --- |
| propertyValue | \* | No | The ending value of the property, as described above. |

**Returns:** function - An array of functions, `getActive`, `getStart` and `getEnd`, which return the starting and the ending value of the property based on the provided value.

> Source: [src/tweens/builders/GetValueOp.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/GetValueOp.js#L42)  
> Since: 3.0.0

## NumberTweenBuilder

### <static> NumberTweenBuilder(parent, config, defaults)

**Description:**

Creates a new Number Tween.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | [Phaser.Tweens.TweenManager](../class/tweens-tweenmanager.md) | No | The owner of the new Tween. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.NumberTweenBuilderConfig](../typedef/types-tweens.md) | No | Configuration for the new Tween. |
| defaults | [Phaser.Types.Tweens.TweenConfigDefaults](../typedef/types-tweens.md) | No | Tween configuration defaults. |

**Returns:** [Phaser.Tweens.Tween](../class/tweens-tween.md) - The new tween.

> Source: [src/tweens/builders/NumberTweenBuilder.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/NumberTweenBuilder.js#L18)  
> Since: 3.0.0

## StaggerBuilder

### <static> StaggerBuilder(value, [config])

**Description:**

Creates a Stagger function to be used by a Tween property.

The stagger function will allow you to stagger changes to the value of the property across all targets of the tween.

This is only worth using if the tween has multiple targets.

The following will stagger the delay by 100ms across all targets of the tween, causing them to scale down to 0.2

over the duration specified:

```
Copy
this.tweens.add({

    targets: [ ... ],

    scale: 0.2,

    ease: 'linear',

    duration: 1000,

    delay: this.tweens.stagger(100)

});


```

The following will stagger the delay by 500ms across all targets of the tween using a 10 x 6 grid, staggering

from the center out, using a cubic ease.

```
Copy
this.tweens.add({

    targets: [ ... ],

    scale: 0.2,

    ease: 'linear',

    duration: 1000,

    delay: this.tweens.stagger(500, { grid: [ 10, 6 ], from: 'center', ease: 'cubic.out' })

});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | Array.<number> | No | The amount to stagger by, or an array containing two elements representing the min and max values to stagger between. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.StaggerConfig](../typedef/types-tweens.md) | Yes | A Stagger Configuration object. |

**Returns:** function - The stagger function.

> Source: [src/tweens/builders/StaggerBuilder.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/StaggerBuilder.js#L11)  
> Since: 3.19.0

## TweenBuilder

### <static> TweenBuilder(parent, config, defaults)

**Description:**

Creates a new Tween.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | [Phaser.Tweens.TweenManager](../class/tweens-tweenmanager.md) | No | The owner of the new Tween. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](../typedef/types-tweens.md) | object | No | Configuration for the new Tween. |
| defaults | [Phaser.Types.Tweens.TweenConfigDefaults](../typedef/types-tweens.md) | No | Tween configuration defaults. |

**Returns:** [Phaser.Tweens.Tween](../class/tweens-tween.md) - The new tween.

> Source: [src/tweens/builders/TweenBuilder.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/TweenBuilder.js#L21)  
> Since: 3.0.0

## TweenChainBuilder

### <static> TweenChainBuilder(parent, config)

**Description:**

Creates a new Tween Chain instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | [Phaser.Tweens.TweenManager](../class/tweens-tweenmanager.md) | No | The owner of the new Tween. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tweens.TweenChainBuilderConfig](../typedef/types-tweens.md) | object | No | Configuration for the new Tween. |

**Returns:** [Phaser.Tweens.TweenChain](../class/tweens-tweenchain.md) - The new Tween Chain.

> Source: [src/tweens/builders/TweenChainBuilder.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/builders/TweenChainBuilder.js#L15)  
> Since: 3.60.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Tweens.Builders](#phasertweensbuilders)

  + [GetBoolean](#getboolean)

    - [<static> GetBoolean(source, key, defaultValue)](#static-getbooleansource-key-defaultvalue)
  + [GetEaseFunction](#geteasefunction)

    - [<static> GetEaseFunction(ease, [easeParams])](#static-geteasefunctionease-easeparams)
  + [GetInterpolationFunction](#getinterpolationfunction)

    - [<static> GetInterpolationFunction(interpolation)](#static-getinterpolationfunctioninterpolation)
  + [GetNewValue](#getnewvalue)

    - [<static> GetNewValue(source, key, defaultValue)](#static-getnewvaluesource-key-defaultvalue)
  + [GetProps](#getprops)

    - [<static> GetProps(config)](#static-getpropsconfig)
  + [GetTargets](#gettargets)

    - [<static> GetTargets(config)](#static-gettargetsconfig)
  + [GetValueOp](#getvalueop)

    - [<static> GetValueOp(key, propertyValue)](#static-getvalueopkey-propertyvalue)
  + [NumberTweenBuilder](#numbertweenbuilder)

    - [<static> NumberTweenBuilder(parent, config, defaults)](#static-numbertweenbuilderparent-config-defaults)
  + [StaggerBuilder](#staggerbuilder)

    - [<static> StaggerBuilder(value, [config])](#static-staggerbuildervalue-config)
  + [TweenBuilder](#tweenbuilder)

    - [<static> TweenBuilder(parent, config, defaults)](#static-tweenbuilderparent-config-defaults)
  + [TweenChainBuilder](#tweenchainbuilder)

    - [<static> TweenChainBuilder(parent, config)](#static-tweenchainbuilderparent-config)

Back to top

©2025[Phaser](https://docs.phaser.io)