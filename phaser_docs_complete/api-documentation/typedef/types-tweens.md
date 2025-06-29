# Types.Tweens

Phaser.Types.Tweens

## TweenConfigDefaults

### <static> TweenConfigDefaults

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| targets | object | Array.<object> | No |  | The object, or an array of objects, to run the tween on. |
| --- | --- | --- | --- | --- |
| delay | number | Yes | 0 | The number of milliseconds to delay before the tween will start. |
| duration | number | Yes | 1000 | The duration of the tween in milliseconds. |
| ease | string | Yes | "'Power0'" | The easing equation to use for the tween. |
| easeParams | array | Yes |  | Optional easing parameters. |
| hold | number | Yes | 0 | The number of milliseconds to hold the tween for before yoyo'ing. |
| repeat | number | Yes | 0 | The number of times to repeat the tween. |
| repeatDelay | number | Yes | 0 | The number of milliseconds to pause before a tween will repeat. |
| yoyo | boolean | Yes | false | Should the tween complete, then reverse the values incrementally to get back to the starting tween values? The reverse tweening will also take `duration` milliseconds to complete. |
| flipX | boolean | Yes | false | Horizontally flip the target of the Tween when it completes (before it yoyos, if set to do so). Only works for targets that support the `flipX` property. |
| flipY | boolean | Yes | false | Vertically flip the target of the Tween when it completes (before it yoyos, if set to do so). Only works for targets that support the `flipY` property. |
| persist | boolean | Yes | false | Retain the tween within the Tween Manager, even after playback completes? |
| interpolation | function | Yes | null | The interpolation function to use for array-based tween values. |

**Type**: object

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/tween/Defaults.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/tween/Defaults.js#L7)  
> Since: 3.0.0

---

## Event

### <static> Event

A Tween Event.

**Type**: string

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/Event.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/Event.js#L1)  
> Since: 3.19.0

---

## GetActiveCallback

### <static> GetActiveCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/GetActiveCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/GetActiveCallback.js#L1)  
> Since: 3.19.0

---

## GetEndCallback

### <static> GetEndCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/GetEndCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/GetEndCallback.js#L1)  
> Since: 3.18.0

---

## GetStartCallback

### <static> GetStartCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/GetStartCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/GetStartCallback.js#L1)  
> Since: 3.18.0

---

## NumberTweenBuilderConfig

### <static> NumberTweenBuilderConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| from | number | Yes | 0 | The start number. |
| --- | --- | --- | --- | --- |
| to | number | Yes | 1 | The end number. |
| delay | number | Yes | 0 | The number of milliseconds to delay before the counter will start. |
| duration | number | Yes | 1000 | The duration of the counter in milliseconds. |
| ease | string | function | Yes | "'Power0'" | The easing equation to use for the counter. |
| easeParams | array | Yes |  | Optional easing parameters. |
| hold | number | Yes | 0 | The number of milliseconds to hold the counter for before yoyo'ing. |
| repeat | number | Yes | 0 | The number of times to repeat the counter. |
| repeatDelay | number | Yes | 0 | The number of milliseconds to pause before the counter will repeat. |
| yoyo | boolean | Yes | false | Should the counter play forward to the end value and then backwards to the start? The reverse playback will also take `duration` milliseconds to complete. |
| completeDelay | string | number | function | object | array |
| loop | string | number | function | object | array |
| loopDelay | string | number | function | object | array |
| paused | boolean | Yes | false | Does the counter start in a paused state (true) or playing (false)? |
| callbackScope | any | Yes |  | Scope (this) for the callbacks. The default scope is the counter. |
| onComplete | [Phaser.Types.Tweens.TweenOnCompleteCallback](types-tweens.md) | Yes |  | A function to call when the counter completes. |
| onCompleteParams | array | Yes |  | Additional parameters to pass to `onComplete`. |
| onLoop | [Phaser.Types.Tweens.TweenOnLoopCallback](types-tweens.md) | Yes |  | A function to call each time the counter loops. |
| onLoopParams | array | Yes |  | Additional parameters to pass to `onLoop`. |
| onRepeat | [Phaser.Types.Tweens.TweenOnRepeatCallback](types-tweens.md) | Yes |  | A function to call each time the counter repeats. |
| onRepeatParams | array | Yes |  | Additional parameters to pass to `onRepeat`. |
| onStart | [Phaser.Types.Tweens.TweenOnStartCallback](types-tweens.md) | Yes |  | A function to call when the counter starts. |
| onStartParams | array | Yes |  | Additional parameters to pass to `onStart`. |
| onStop | [Phaser.Types.Tweens.TweenOnStopCallback](types-tweens.md) | Yes |  | A function to call when the counter is stopped. |
| onStopParams | array | Yes |  | Additional parameters to pass to `onStop`. |
| onUpdate | [Phaser.Types.Tweens.TweenOnUpdateCallback](types-tweens.md) | Yes |  | A function to call each time the counter steps. |
| onUpdateParams | array | Yes |  | Additional parameters to pass to `onUpdate`. |
| onYoyo | [Phaser.Types.Tweens.TweenOnYoyoCallback](types-tweens.md) | Yes |  | A function to call each time the counter yoyos. |
| onYoyoParams | array | Yes |  | Additional parameters to pass to `onYoyo`. |
| onPause | [Phaser.Types.Tweens.TweenOnPauseCallback](types-tweens.md) | Yes |  | A function to call when the counter is paused. |
| onPauseParams | array | Yes |  | Additional parameters to pass to `onPause`. |
| onResume | [Phaser.Types.Tweens.TweenOnResumeCallback](types-tweens.md) | Yes |  | A function to call when the counter is resumed after being paused. |
| onResumeParams | array | Yes |  | Additional parameters to pass to `onResume`. |
| persist | boolean | Yes |  | Will the counter be automatically destroyed on completion, or retained for future playback? |
| interpolation | string | function | Yes |  | The interpolation function to use if the `value` given is an array of numbers. |

**Type**: object

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/NumberTweenBuilderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/NumberTweenBuilderConfig.js#L1)  
> Since: 3.18.0

---

## StaggerConfig

### <static> StaggerConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| start | number | Yes | 0 | The value to start the stagger from. Can be used as a way to offset the stagger while still using a range for the value. |
| --- | --- | --- | --- | --- |
| ease | string | function | Yes | "'Linear'" | An ease to apply across the staggered values. Can either be a string, such as 'sine.inout', or a function. |
| from | string | number | Yes | 0 | The index to start the stagger from. Can be the strings `first`, `last` or `center`, or an integer representing the stagger position. |
| grid | Array.<number> | Yes |  | Set the stagger to run across a grid by providing an array where element 0 is the width of the grid and element 1 is the height. Combine with the 'from' property to control direction. |

**Type**: object

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/StaggerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/StaggerConfig.js#L1)  
> Since: 3.19.0

---

## TweenBuilderConfig

### <static> TweenBuilderConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| targets | any | No |  | The object, or an array of objects, to run the tween on. |
| --- | --- | --- | --- | --- |
| delay | number | function | Yes | 0 | The number of milliseconds to delay before the tween will start. |
| duration | number | Yes | 1000 | The duration of the tween in milliseconds. |
| ease | string | function | Yes | "'Power0'" | The easing equation to use for the tween. |
| easeParams | array | Yes |  | Optional easing parameters. |
| hold | number | Yes | 0 | The number of milliseconds to hold the tween for before yoyo'ing. |
| repeat | number | Yes | 0 | The number of times each property tween repeats. |
| repeatDelay | number | Yes | 0 | The number of milliseconds to pause before a repeat. |
| yoyo | boolean | Yes | false | Should the tween complete, then reverse the values incrementally to get back to the starting tween values? The reverse tweening will also take `duration` milliseconds to complete. |
| flipX | boolean | Yes | false | Horizontally flip the target of the Tween when it completes (before it yoyos, if set to do so). Only works for targets that support the `flipX` property. |
| flipY | boolean | Yes | false | Vertically flip the target of the Tween when it completes (before it yoyos, if set to do so). Only works for targets that support the `flipY` property. |
| completeDelay | string | number | function | object | array |
| loop | string | number | function | object | array |
| loopDelay | string | number | function | object | array |
| paused | boolean | Yes | false | Does the tween start in a paused state (true) or playing (false)? |
| props | Object.<string, (number, string, [Phaser.Types.Tweens.GetEndCallback](types-tweens.md), [Phaser.Types.Tweens.TweenPropConfig](types-tweens.md))> | Yes |  | The properties to tween. |
| callbackScope | any | Yes |  | The scope (or context) for all of the callbacks. The default scope is the tween. |
| onComplete | [Phaser.Types.Tweens.TweenOnCompleteCallback](types-tweens.md) | Yes |  | A function to call when the tween completes. |
| onCompleteParams | array | Yes |  | Additional parameters to pass to `onComplete`. |
| onLoop | [Phaser.Types.Tweens.TweenOnLoopCallback](types-tweens.md) | Yes |  | A function to call each time the tween loops. |
| onLoopParams | array | Yes |  | Additional parameters to pass to `onLoop`. |
| onRepeat | [Phaser.Types.Tweens.TweenOnRepeatCallback](types-tweens.md) | Yes |  | A function to call each time a property tween repeats. Called once per property per target. |
| onRepeatParams | array | Yes |  | Additional parameters to pass to `onRepeat`. |
| onStart | [Phaser.Types.Tweens.TweenOnStartCallback](types-tweens.md) | Yes |  | A function to call when the tween starts playback, after any delays have expired. |
| onStartParams | array | Yes |  | Additional parameters to pass to `onStart`. |
| onStop | [Phaser.Types.Tweens.TweenOnStopCallback](types-tweens.md) | Yes |  | A function to call when the tween is stopped. |
| onStopParams | array | Yes |  | Additional parameters to pass to `onStop`. |
| onUpdate | [Phaser.Types.Tweens.TweenOnUpdateCallback](types-tweens.md) | Yes |  | A function to call each time the tween steps. Called once per property per target. |
| onUpdateParams | array | Yes |  | Additional parameters to pass to `onUpdate`. |
| onYoyo | [Phaser.Types.Tweens.TweenOnYoyoCallback](types-tweens.md) | Yes |  | A function to call each time a property tween yoyos. Called once per property per target. |
| onYoyoParams | array | Yes |  | Additional parameters to pass to `onYoyo`. |
| onActive | [Phaser.Types.Tweens.TweenOnActiveCallback](types-tweens.md) | Yes |  | A function to call when the tween becomes active within the Tween Manager. |
| onActiveParams | array | Yes |  | Additional parameters to pass to `onActive`. |
| onPause | [Phaser.Types.Tweens.TweenOnPauseCallback](types-tweens.md) | Yes |  | A function to call when the tween is paused. |
| onPauseParams | array | Yes |  | Additional parameters to pass to `onPause`. |
| onResume | [Phaser.Types.Tweens.TweenOnResumeCallback](types-tweens.md) | Yes |  | A function to call when the tween is resumed after being paused. |
| onResumeParams | array | Yes |  | Additional parameters to pass to `onResume`. |
| persist | boolean | Yes |  | Will the Tween be automatically destroyed on completion, or retained for future playback? |
| interpolation | string | function | Yes |  | The interpolation function to use if the `value` given is an array of numbers. |

**Type**: object

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenBuilderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenBuilderConfig.js#L1)  
> Since: 3.18.0

---

## TweenCallbacks

### <static> TweenCallbacks

| name | type | optional | description |
| --- | --- | --- | --- |
| onActive | [Phaser.Types.Tweens.TweenOnActiveCallback](types-tweens.md) | Yes | A function to call when the tween becomes active within the Tween Manager. |
| --- | --- | --- | --- |
| onStart | [Phaser.Types.Tweens.TweenOnStartCallback](types-tweens.md) | Yes | A function to call when the tween starts playback, after any delays have expired. |
| onComplete | [Phaser.Types.Tweens.TweenOnCompleteCallback](types-tweens.md) | Yes | A function to call when the tween completes. |
| onLoop | [Phaser.Types.Tweens.TweenOnLoopCallback](types-tweens.md) | Yes | A function to call each time the tween loops. |
| onPause | [Phaser.Types.Tweens.TweenOnPauseCallback](types-tweens.md) | Yes | A function to call each time the tween is paused. |
| onResume | [Phaser.Types.Tweens.TweenOnResumeCallback](types-tweens.md) | Yes | A function to call each time the tween is resumed. |
| onRepeat | [Phaser.Types.Tweens.TweenOnRepeatCallback](types-tweens.md) | Yes | A function to call each time the tween repeats. Called once per property per target. |
| onStop | [Phaser.Types.Tweens.TweenOnStopCallback](types-tweens.md) | Yes | A function to call when the tween is stopped. |
| onUpdate | [Phaser.Types.Tweens.TweenOnUpdateCallback](types-tweens.md) | Yes | A function to call each time the tween steps. Called once per property per target. |
| onYoyo | [Phaser.Types.Tweens.TweenOnYoyoCallback](types-tweens.md) | Yes | A function to call each time the tween yoyos. Called once per property per target. |

**Type**: object

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenCallbacks.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenCallbacks.js#L1)  
> Since: 3.60.0

---

## TweenCallbackTypes

### <static> TweenCallbackTypes

**Type**: 'onActive' | 'onComplete' | 'onLoop' | 'onPause' | 'onRepeat' | 'onResume' | 'onStart' | 'onStop' | 'onUpdate' | 'onYoyo'

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenCallbackTypes.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenCallbackTypes.js#L1)  
> Since: 3.60.0

---

## TweenChainBuilderConfig

### <static> TweenChainBuilderConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| targets | any | No |  | The object, or an array of objects, to run each tween on. |
| --- | --- | --- | --- | --- |
| delay | number | function | Yes | 0 | The number of milliseconds to delay before the chain will start. |
| completeDelay | string | number | function | object | array |
| loop | string | number | function | object | array |
| loopDelay | string | number | function | object | array |
| paused | boolean | Yes | false | Does the chain start in a paused state (true) or playing (false)? |
| tweens | Array.<[Phaser.Types.Tweens.TweenBuilderConfig](types-tweens.md)> | Yes |  | The tweens to chain together. |
| callbackScope | any | Yes |  | The scope (or context) for all of the callbacks. The default scope is the chain. |
| onComplete | [Phaser.Types.Tweens.TweenOnCompleteCallback](types-tweens.md) | Yes |  | A function to call when the chain completes. |
| onCompleteParams | array | Yes |  | Additional parameters to pass to `onComplete`. |
| onLoop | [Phaser.Types.Tweens.TweenOnLoopCallback](types-tweens.md) | Yes |  | A function to call each time the chain loops. |
| onLoopParams | array | Yes |  | Additional parameters to pass to `onLoop`. |
| onStart | [Phaser.Types.Tweens.TweenOnStartCallback](types-tweens.md) | Yes |  | A function to call when the chain starts playback, after any delays have expired. |
| onStartParams | array | Yes |  | Additional parameters to pass to `onStart`. |
| onStop | [Phaser.Types.Tweens.TweenOnStopCallback](types-tweens.md) | Yes |  | A function to call when the chain is stopped. |
| onStopParams | array | Yes |  | Additional parameters to pass to `onStop`. |
| onActive | [Phaser.Types.Tweens.TweenOnActiveCallback](types-tweens.md) | Yes |  | A function to call when the chain becomes active within the Tween Manager. |
| onActiveParams | array | Yes |  | Additional parameters to pass to `onActive`. |
| onPause | [Phaser.Types.Tweens.TweenOnPauseCallback](types-tweens.md) | Yes |  | A function to call when the chain is paused. |
| onPauseParams | array | Yes |  | Additional parameters to pass to `onPause`. |
| onResume | [Phaser.Types.Tweens.TweenOnResumeCallback](types-tweens.md) | Yes |  | A function to call when the chain is resumed after being paused. |
| onResumeParams | array | Yes |  | Additional parameters to pass to `onResume`. |
| persist | boolean | Yes |  | Will the Tween be automatically destroyed on completion, or retained for future playback? |

**Type**: object

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenChainBuilderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenChainBuilderConfig.js#L1)  
> Since: 3.60.0

---

## TweenDataConfig

### <static> TweenDataConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | any | No |  | The target to tween. |
| --- | --- | --- | --- | --- |
| index | number | No |  | The target index within the Tween targets array. |
| key | string | No |  | The property of the target being tweened. |
| getActiveValue | [Phaser.Types.Tweens.GetActiveCallback](types-tweens.md) | No |  | If not null, is invoked *immediately* as soon as the TweenData is running, and is set on the target property. |
| getEndValue | [Phaser.Types.Tweens.GetEndCallback](types-tweens.md) | No |  | The returned value sets what the property will be at the END of the Tween. |
| getStartValue | [Phaser.Types.Tweens.GetStartCallback](types-tweens.md) | No |  | The returned value sets what the property will be at the START of the Tween. |
| ease | function | No |  | The ease function this tween uses. |
| duration | number | Yes | 0 | Duration of the tween in milliseconds, excludes time for yoyo or repeats. |
| totalDuration | number | Yes | 0 | The total calculated duration of this TweenData (based on duration, repeat, delay and yoyo) |
| delay | number | Yes | 0 | Time in milliseconds before tween will start. |
| yoyo | boolean | Yes | false | Cause the tween to return back to its start value after hold has expired. |
| hold | number | Yes | 0 | Time in milliseconds the tween will pause before running the yoyo or starting a repeat. |
| repeat | number | Yes | 0 | Number of times to repeat the tween. The tween will always run once regardless, so a repeat value of '1' will play the tween twice. |
| repeatDelay | number | Yes | 0 | Time in milliseconds before the repeat will start. |
| flipX | boolean | Yes | false | Automatically call toggleFlipX when the TweenData yoyos or repeats |
| flipY | boolean | Yes | false | Automatically call toggleFlipY when the TweenData yoyos or repeats |
| progress | number | Yes | 0 | Between 0 and 1 showing completion of this TweenData. |
| elapsed | number | Yes | 0 | Delta counter |
| repeatCounter | number | Yes | 0 | How many repeats are left to run? |
| start | number | Yes | 0 | The property value at the start of the ease. |
| current | number | Yes | 0 | The current propety value. |
| previous | number | Yes | 0 | The previous property value. |
| end | number | Yes | 0 | The property value at the end of the ease. |
| gen | [Phaser.Types.Tweens.TweenDataGenConfig](types-tweens.md) | Yes |  | LoadValue generation functions. |
| state | [Phaser.Tweens.StateType](tweens.md) | Yes | 0 | TWEEN\_CONST.CREATED |

**Type**: object

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenDataConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenDataConfig.js#L1)  
> Since: 3.0.0

---

## TweenDataGenConfig

### <static> TweenDataGenConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| delay | function | No | Time in milliseconds before tween will start. |
| --- | --- | --- | --- |
| duration | function | No | Duration of the tween in milliseconds, excludes time for yoyo or repeats. |
| hold | function | No | Time in milliseconds the tween will pause before running the yoyo or starting a repeat. |
| repeat | function | No | Number of times to repeat the tween. The tween will always run once regardless, so a repeat value of '1' will play the tween twice. |
| repeatDelay | function | No | Time in milliseconds before the repeat will start. |

**Type**: object

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenDataGenConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenDataGenConfig.js#L1)  
> Since: 3.0.0

---

## TweenFrameDataConfig

### <static> TweenFrameDataConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | any | No |  | The target to tween. |
| --- | --- | --- | --- | --- |
| index | number | No |  | The target index within the Tween targets array. |
| key | string | No |  | The property of the target being tweened. |
| duration | number | Yes | 0 | Duration of the tween in milliseconds, excludes time for yoyo or repeats. |
| totalDuration | number | Yes | 0 | The total calculated duration of this TweenData (based on duration, repeat, delay and yoyo) |
| delay | number | Yes | 0 | Time in milliseconds before tween will start. |
| hold | number | Yes | 0 | Time in milliseconds the tween will pause before running the yoyo or starting a repeat. |
| repeat | number | Yes | 0 | Number of times to repeat the tween. The tween will always run once regardless, so a repeat value of '1' will play the tween twice. |
| repeatDelay | number | Yes | 0 | Time in milliseconds before the repeat will start. |
| flipX | boolean | Yes | false | Automatically call toggleFlipX when the TweenData yoyos or repeats |
| flipY | boolean | Yes | false | Automatically call toggleFlipY when the TweenData yoyos or repeats |
| progress | number | Yes | 0 | Between 0 and 1 showing completion of this TweenData. |
| elapsed | number | Yes | 0 | Delta counter |
| repeatCounter | number | Yes | 0 | How many repeats are left to run? |
| gen | [Phaser.Types.Tweens.TweenDataGenConfig](types-tweens.md) | Yes |  | LoadValue generation functions. |
| state | [Phaser.Tweens.StateType](tweens.md) | Yes | 0 | TWEEN\_CONST.CREATED |

**Type**: object

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenFrameDataConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenFrameDataConfig.js#L1)  
> Since: 3.60.0

---

## TweenOnActiveCallback

### <static> TweenOnActiveCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenOnActiveCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenOnActiveCallback.js#L1)  
> Since: 3.19.0

---

## TweenOnCompleteCallback

### <static> TweenOnCompleteCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenOnCompleteCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenOnCompleteCallback.js#L1)  
> Since: 3.18.0

---

## TweenOnLoopCallback

### <static> TweenOnLoopCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenOnLoopCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenOnLoopCallback.js#L1)  
> Since: 3.18.0

---

## TweenOnPauseCallback

### <static> TweenOnPauseCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenOnPauseCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenOnPauseCallback.js#L1)  
> Since: 3.60.0

---

## TweenOnRepeatCallback

### <static> TweenOnRepeatCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenOnRepeatCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenOnRepeatCallback.js#L1)  
> Since: 3.18.0

---

## TweenOnResumeCallback

### <static> TweenOnResumeCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenOnResumeCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenOnResumeCallback.js#L1)  
> Since: 3.60.0

---

## TweenOnStartCallback

### <static> TweenOnStartCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenOnStartCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenOnStartCallback.js#L1)  
> Since: 3.18.0

---

## TweenOnStopCallback

### <static> TweenOnStopCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenOnStopCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenOnStopCallback.js#L1)  
> Since: 3.24.0

---

## TweenOnUpdateCallback

### <static> TweenOnUpdateCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenOnUpdateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenOnUpdateCallback.js#L1)  
> Since: 3.18.0

---

## TweenOnYoyoCallback

### <static> TweenOnYoyoCallback

**Type**: function

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenOnYoyoCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenOnYoyoCallback.js#L1)  
> Since: 3.18.0

---

## TweenPropConfig

### <static> TweenPropConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | Array.<number> | string | [Phaser.Types.Tweens.GetEndCallback](types-tweens.md) |
| --- | --- | --- | --- |
| getActive | [Phaser.Types.Tweens.GetActiveCallback](types-tweens.md) | Yes | What the property will be set to immediately when this tween becomes active. |
| getEnd | [Phaser.Types.Tweens.GetEndCallback](types-tweens.md) | Yes | What the property will be at the END of the Tween. |
| getStart | [Phaser.Types.Tweens.GetStartCallback](types-tweens.md) | Yes | What the property will be at the START of the Tween. |
| ease | string | function | Yes | The ease function this tween uses. |
| delay | number | Yes | Time in milliseconds before tween will start. |
| duration | number | Yes | Duration of the tween in milliseconds. |
| yoyo | boolean | Yes | Determines whether the tween should return back to its start value after hold has expired. |
| hold | number | Yes | Time in milliseconds the tween will pause before repeating or returning to its starting value if yoyo is set to true. |
| repeat | number | Yes | Number of times to repeat the tween. The tween will always run once regardless, so a repeat value of '1' will play the tween twice. |
| repeatDelay | number | Yes | Time in milliseconds before the repeat will start. |
| flipX | boolean | Yes | Should toggleFlipX be called when yoyo or repeat happens? |
| flipY | boolean | Yes | Should toggleFlipY be called when yoyo or repeat happens? |
| interpolation | string | function | Yes | The interpolation function to use if the `value` given is an array of numbers. |

**Type**: object

**Member of**: Phaser.Types.Tweens

> Source: [src/tweens/typedefs/TweenPropConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tweens/typedefs/TweenPropConfig.js#L1)  
> Since: 3.18.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Tweens](#typestweens)

  + [TweenConfigDefaults](#tweenconfigdefaults)

    - [<static> TweenConfigDefaults](#static-tweenconfigdefaults)
  + [Event](#event)

    - [<static> Event](#static-event)
  + [GetActiveCallback](#getactivecallback)

    - [<static> GetActiveCallback](#static-getactivecallback)
  + [GetEndCallback](#getendcallback)

    - [<static> GetEndCallback](#static-getendcallback)
  + [GetStartCallback](#getstartcallback)

    - [<static> GetStartCallback](#static-getstartcallback)
  + [NumberTweenBuilderConfig](#numbertweenbuilderconfig)

    - [<static> NumberTweenBuilderConfig](#static-numbertweenbuilderconfig)
  + [StaggerConfig](#staggerconfig)

    - [<static> StaggerConfig](#static-staggerconfig)
  + [TweenBuilderConfig](#tweenbuilderconfig)

    - [<static> TweenBuilderConfig](#static-tweenbuilderconfig)
  + [TweenCallbacks](#tweencallbacks)

    - [<static> TweenCallbacks](#static-tweencallbacks)
  + [TweenCallbackTypes](#tweencallbacktypes)

    - [<static> TweenCallbackTypes](#static-tweencallbacktypes)
  + [TweenChainBuilderConfig](#tweenchainbuilderconfig)

    - [<static> TweenChainBuilderConfig](#static-tweenchainbuilderconfig)
  + [TweenDataConfig](#tweendataconfig)

    - [<static> TweenDataConfig](#static-tweendataconfig)
  + [TweenDataGenConfig](#tweendatagenconfig)

    - [<static> TweenDataGenConfig](#static-tweendatagenconfig)
  + [TweenFrameDataConfig](#tweenframedataconfig)

    - [<static> TweenFrameDataConfig](#static-tweenframedataconfig)
  + [TweenOnActiveCallback](#tweenonactivecallback)

    - [<static> TweenOnActiveCallback](#static-tweenonactivecallback)
  + [TweenOnCompleteCallback](#tweenoncompletecallback)

    - [<static> TweenOnCompleteCallback](#static-tweenoncompletecallback)
  + [TweenOnLoopCallback](#tweenonloopcallback)

    - [<static> TweenOnLoopCallback](#static-tweenonloopcallback)
  + [TweenOnPauseCallback](#tweenonpausecallback)

    - [<static> TweenOnPauseCallback](#static-tweenonpausecallback)
  + [TweenOnRepeatCallback](#tweenonrepeatcallback)

    - [<static> TweenOnRepeatCallback](#static-tweenonrepeatcallback)
  + [TweenOnResumeCallback](#tweenonresumecallback)

    - [<static> TweenOnResumeCallback](#static-tweenonresumecallback)
  + [TweenOnStartCallback](#tweenonstartcallback)

    - [<static> TweenOnStartCallback](#static-tweenonstartcallback)
  + [TweenOnStopCallback](#tweenonstopcallback)

    - [<static> TweenOnStopCallback](#static-tweenonstopcallback)
  + [TweenOnUpdateCallback](#tweenonupdatecallback)

    - [<static> TweenOnUpdateCallback](#static-tweenonupdatecallback)
  + [TweenOnYoyoCallback](#tweenonyoyocallback)

    - [<static> TweenOnYoyoCallback](#static-tweenonyoyocallback)
  + [TweenPropConfig](#tweenpropconfig)

    - [<static> TweenPropConfig](#static-tweenpropconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Tweens