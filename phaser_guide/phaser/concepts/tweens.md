# Tweens

Tweens

Tweens are an important part of most games, although it's entirely possible you have never come across the term before. Phaser has a built-in Tween Manager that allows you to create smooth, time-based changes to object properties. For example, you can tween the position of a Sprite from one coordinate to another, over a given duration of time. Or you can tween the alpha value of a Game Object from 1 to 0, making it appear to fade out. The Tween Manager is a Scene-based system, and each Scene has its own instance of it.

Although most often used on Game Objects, tweens can actually adjust any object at all. For example, you can tween the volume of a sound, or the position of a Camera. You can even tween the properties of a JavaScript object, such as an object containing a players score, or health points.

Tweens have a whole raft of features built into them. They can be set to repeat, yoyo, tween multiple objects at once, set multiple properties at once, each with their own custom values, have delays, interpolation, a variety of different smoothing effects and much, much more. They can even be chained together, so that one starts as soon as another finishes. As a result, they are a very powerful system and one that you'll find yourself using a lot in your games.

We will cover tweens in much more depth in a later chapter, but the take-away here is that a 'tween' is when the value of an object is changed over a period of time.

## Basic usage

### Creating a tween

```
Copyvar tween = scene.tweens.add({
    targets: gameObject,
    x: 1,
    // x: '+=1',
    // x: '-=1',
    // x: '*=1',
    // x: '/=1',
    // x: 'random(0.25, 0.75)',
    // x: 'int(10, 100)',
    // x: [100, 300, 200, 600],
    // x: { from: 0, to: 1 },
    // x: { start: 0, to: 1 },  
    // x: { start: value0, from: value1, to: value2 },  
    // x: {
    //      getActive: function (target, key, value, targetIndex, totalTargets, tween) { return newValue; },
    //      getStart: function (target, key, value, targetIndex, totalTargets, tween) { return newValue; },
    //      getEnd: function (target, key, value, targetIndex, totalTargets, tween) { return newValue; }
    // },
    ease: 'Linear',       // 'Cubic', 'Elastic', 'Bounce', 'Back'
    duration: 1000,
    repeat: 0,            // -1: infinity
    yoyo: false,

    // interpolation: null,
});

```

* `key: value2` : Tween to `value2`.
* `key: '+=deltaValue'` : Tween to current value + deltaValue
  + Support these expressions : `key: '+=deltaValue'`, `key: '-=deltaValue'`, `key: '*=deltaValue'`, `key: '/=deltaValue'`
* `key: 'random(10, 100)'` : Tween to a random float value.
* `key: 'int(10, 100)'` : Tween to a random int value.
* `key: [100, 300, 200, 600]` : Use `interpolation` to determine the value.
* `key: { from: value1, to: value2 }` : Set the property to `value11` when tween started after delay, then tween to `value2`.
  + `value1`, `value2` : A number, string, or callback(`function(target, key, value, targetIndex, totalTargets, tween) { return newValue; }`)
* `key: { start: value0, to: value2 }` : Set the property to `value0` immediately, then tween to `value2`.
  + `value1`, `value2` : A number, string, or callback(`function(target, key, value, targetIndex, totalTargets, tween) { return newValue; }`)
* `key: { start: value0, from: value1, to: value2 }` : Set the property to `value0` immediately, then set to `value1` when tween started after delay, then tween to `value2`.
  + `value0`, `value1`, `value2` : A number, string, or callback(`function(target, key, value, targetIndex, totalTargets, tween) { return newValue; }`)
* `key: function(target, key, value, targetIndex, totalTargets, tween) { return newValue; }`
  + `target` :　The tween target.
  + `key` : The target property.
  + `value` : The current value of the target property.
  + `targetIndex` : The index of the target within the Tween.
  + `totalTargets` : The total number of targets in this Tween.
  + `tween` : The Tween that invoked this callback.
* `key: { getActive:callback, getStart:callback, getEnd:callback}`
  + `callback` : `function(target, key, value, targetIndex, totalTargets, tween) { return newValue; }`

or

```
Copyvar tween = scene.tweens.add({
    targets: gameObject,
    paused: false,
    callbackScope: tween,

    // timming/callback of each state
    onStart: function () {},
    onStartParams: [],

    // initial delay
    delay: 0,  // function(target, targetKey, value, targetIndex, totalTargets, tween) { },

    // tween duration
    duration: 1000,
    ease: 'Linear',
    easeParams: null,

    onActive: function () {},
    onUpdate: function (tween, target, key, current, previous, param) {},
    onUpdateParams: [],

    // delay between tween and yoyo
    hold: 0,
    yoyo: false,  // true to tween backward
    flipX: false,
    flipY: false,
    onYoyo: function (tween, target, key, current, previous, param) {},
    onYoyoParams: [],

    // repeat count (-1: infinite)
    repeat: 0,
    onRepeat: function (tween, target, key, current, previous, param) {},
    onRepeatParams: [],
    // delay to next pass
    repeatDelay: 0,

    // loop count (-1: infinite)
    loop: 0,
    onLoop: function () {},
    onLoopParams: [],
    // delay to next loop
    loopDelay: 0,

    // delay to onComplete callback
    completeDelay: 0,
    onComplete: function () {},
    onCompleteParams: [],
    // timming/callback of each state

    onStop: function () {}, 
    onPause: function () {}, 
    onResume: function () {}, 

    // properties:
    x: '+=600',        // start from current value
    y: 500,
    rotation: ...
    angle: ...
    alpha: ...
    // ...

    // or
    props: {
        x: { value: '+=600', duration: 3000, ease: 'Power2' },
        y: { value: '500', duration: 1500, ease: 'Bounce.easeOut' }
    },

    // or
    props: {
        x: {
            duration: 400,
            yoyo: true,
            repeat: 8,
            ease: 'Sine.easeInOut',
            value: {
                getActive: function (target, key, value, targetIndex, totalTargets, tween)
                {
                    return value;
                },
                getStart: function (target, key, value, targetIndex, totalTargets, tween)
                {
                    return value + 30;
                },
                getEnd: function (target, key, value, targetIndex, totalTargets, tween)
                {
                    destX -= 30;
                    return destX;
                }
            }
        },
        ....
    },

    persist: false,

    interpolation: null,
    interpolationData: null,

});

```

* `targets` : The targets the tween is updating.
* `delay` : The time the tween will wait before it first starts
  + A number, for all targets
  + A callback function, built via stagger builder :
    - From `0` to `endValue` :
      * `scene.tweens.stagger(endValue)`
    - From `startValue` to `endValue` :
      * `scene.tweens.stagger([startValue, endValue])`
    - From `0` to `endValue`, with specific ease function :
      * `scene.tweens.stagger(endValue, {ease: 'cubic.inout'})`
    - From `startValue` to `endValue`, with specific ease function :
      * `scene.tweens.stagger([startValue, endValue], {ease: 'cubic.inout'})`
    - From `0` to `endValue`, with specific start index :
      * `scene.tweens.stagger(endValue, {from: 'last'})`
      * `scene.tweens.stagger(endValue, {from: 'center'})`
      * `scene.tweens.stagger(endValue, {from: index})`
    - From `startValue` to `endValue`, , with specific start index :
      * `scene.tweens.stagger([startValue, endValue], {from: 'last'})`
      * `scene.tweens.stagger([startValue, endValue], {from: 'center'})`
      * `scene.tweens.stagger([startValue, endValue], {from: index})`
    - From `0` to `endValue`, with specific ease function, with specific start index :
      * `scene.tweens.stagger(endValue, {from: 'last', ease: 'cubic.inout'})`
    - From `startValue` to `endValue`, with specific ease function , with specific start index :
      * `scene.tweens.stagger([startValue, endValue], {from: 'last', ease: 'cubic.inout'})`
    - Grid mode. From `0` to `endValue`.
      * `scene.tweens.stagger(endValue, {grid: [gridWidth, gridHeight], })`
      * `scene.tweens.stagger(endValue, {grid: [gridWidth, gridHeight], from: 'center'})`
      * `scene.tweens.stagger(endValue, {grid: [gridWidth, gridHeight], from: 'center', ease: 'cubic.inout'})`
    - Grid mode. From `startValue` to `endValue`.
      * `scene.tweens.stagger([startValue, endValue], {grid: [gridWidth, gridHeight], })`
      * `scene.tweens.stagger([startValue, endValue], {grid: [gridWidth, gridHeight], from: 'center'})`
      * `scene.tweens.stagger([startValue, endValue], {grid: [gridWidth, gridHeight], from: 'center', ease: 'cubic.inout'})`
* `duration` : The duration of the tween
* `ease` : The ease function used by the tween
* `easeParams` : The parameters to go with the ease function (if any)
* `hold` : The time the tween will pause before running a yoyo
* `repeat` : The number of times the tween will repeat itself (a value of 1 means the tween will play twice, as it repeated once)
* `repeatDelay` : The time the tween will pause for before starting a repeat. The tween holds in the start state.
* `yoyo` : boolean - Does the tween reverse itself (yoyo) when it reaches the end?
* `flipX` : flip X the GameObject on tween end
* `flipY` : flip Y the GameObject on tween end
* `completeDelay` : The time the tween will wait before the onComplete event is dispatched once it has completed
* `loop` : `-1` for an infinite loop
* `loopDelay`
* `paused` : Does the tween start in a paused state, or playing?
* `props` : The properties being tweened by the tween
* `onActive` : Tween becomes active within the Tween Manager.

  ```
  Copyfunction(tween, target) { }

  ```
* `onStart` : A tween starts.

  ```
  Copyfunction(tween, targets) { }

  ```
* `onUpdate` : Callback which fired when tween task updated

  ```
  Copyfunction(tween, target, key, current, previous, param) { }

  ```
* `onComplete` : Tween completes or is stopped.

  ```
  Copyfunction(tween, targets) { }

  ```
* `onYoyo` : A function to call each time the tween yoyos. Called once per property per target.

  ```
  Copyfunction(tween, target, key, current, previous, param) { }

  ```
* `onLoop` : A function to call each time the tween loops.

  ```
  Copyfunction(tween, targets) { }

  ```
* `onRepeat` : A function to call each time the tween repeats. Called once per property per target.

  ```
  Copyfunction(tween, target, key, current, previous, param) { }

  ```
* `onStop` : A function to call when the tween is stopped.

  ```
  Copyfunction(tween, targets) { }

  ```
* `onPause` : A function to call when the tween is paused.

  ```
  Copyfunction(tween, targets) { }

  ```
* `onResume` : A function to call when the tween is resumed after being paused.

  ```
  Copyfunction(tween, targets) { }

  ```
* `persist` : Will the Tween be automatically destroyed on completion, or retained for future playback?
* `interpolation` : The interpolation function to use if the `value` given is an array of numbers.
  + `'linear'`, `'bezier'`, `'catmull'` (or `'catmullrom'`)

!!! note
Tween task will not manipulate any property that begins with an **underscore**.

## Easing equations

* `Power0` : Linear
* `Power1` : Quadratic.Out
* `Power2` : Cubic.Out
* `Power3` : Quartic.Out
* `Power4` : Quintic.Out
* `Linear`
* `Quad` : Quadratic.Out
* `Cubic` : Cubic.Out
* `Quart` : Quartic.Out
* `Quint` : Quintic.Out
* `Sine` : Sine.Out
* `Expo` : Expo.Out
* `Circ` : Circular.Out
* `Elastic` : Elastic.Out
* `Back` : Back.Out
* `Bounce` : Bounce.Out
* `Stepped`
* `Quad.easeIn`
* `Cubic.easeIn`
* `Quart.easeIn`
* `Quint.easeIn`
* `Sine.easeIn`
* `Expo.easeIn`
* `Circ.easeIn`
* `Back.easeIn`
* `Bounce.easeIn`
* `Quad.easeOut`
* `Cubic.easeOut`
* `Quart.easeOut`
* `Quint.easeOut`
* `Sine.easeOut`
* `Expo.easeOut`
* `Circ.easeOut`
* `Back.easeOut`
* `Bounce.easeOut`
* `Quad.easeInOut`
* `Cubic.easeInOut`
* `Quart.easeInOut`
* `Quint.easeInOut`
* `Sine.easeInOut`
* `Expo.easeInOut`
* `Circ.easeInOut`
* `Back.easeInOut`
* `Bounce.easeInOut`

[Demo](https://labs.phaser.io/view.html?src=src/tweens/eases/ease%20mixer.js)

### Pause / Resume task

```
Copytween.pause();

```

```
Copytween.resume();

```

#### Stop task

```
Copytween.complete();

```

```
Copytween.stop();

```

Won't invoke `onComplete` callback (`'complete'` event)

#### Play task

```
Copytween.play();

```

#### Restart task

```
Copytween.restart();

```

#### Seek

```
Copytween.seek(amount);
// tween.seek(amount, delta, emit);

```

* `amount` : The number of milliseconds to seek into the Tween from the beginning.
* `delta` : The size of each step when seeking through the Tween. Default value is `16.6` (1000/60)
* `emit` : While seeking, should the Tween emit any of its events or callbacks? The default is `false`.

#### Remove task

Removes this Tween from the TweenManager

```
Copytween.remove();

```

#### Destroy task

Free tween task from memory

```
Copytween.destroy();

```

!!! note
A Tween that has been destroyed cannot ever be played or used again.

#### Get tweens

* Tweens of a target

  ```
  Copyvar tweens = scene.tweens.getTweensOf(target);
  // var tweens = scene.tweens.getTweensOf(target, includePending);

  ```

  + `tweens` : Array of tweens, or timelines.
  + `includePending` : Set `true` to search pending tweens.
* All tweens

  ```
  Copyvar tweens = scene.tweens.getTweens();

  ```

#### Destroy task of a target

```
Copyscene.tweens.killTweensOf(target);

```

* `target` : The target to kill the tweens of. Provide an array to use multiple targets.

#### Time-scale

```
Copytween.setTimeScale(v);
// tween.timeScale = timescale;

```

```
Copyvar timeScale = tween.getTimeScale();
// var timeScale = tween.timeScale;

```

##### Global time-scale

```
Copyvar timeScale = scene.tweens.timeScale;

```

```
Copyscene.tweens.timeScale = timescale;

```

#### Events

* Tween becomes active within the Tween Manager.

  ```
  Copytween.on('active', function(tween, targets){

  }, scope);

  ```
* Tween completes or is stopped.

  ```
  Copytween.on('complete', function(tween, targets){

  }, scope);

  ```
* A tween loops, after any loop delay expires.

  ```
  Copytween.on('loop', function(tween, targets){

  }, scope);

  ```
* A tween property repeats, after any repeat delay expires.

  ```
  Copytween.on('repeat', function(tween, key, target){

  }, scope);

  ```
* A tween starts.

  ```
  Copytween.on('start', function(tween, targets){

  }, scope);

  ```
* A tween property updates.

  ```
  Copytween.on('update', function(tween, key, target, current, previous){

  }, scope);

  ```

  + `tween` : A reference to the Tween instance that emitted the event.
  + `key` : The property that was updated, i.e. `x` or `scale`.
  + `target` : The target object that was updated. Usually a Game Object, but can be of any type.
  + `current` : The current value of the property that was tweened.
  + `previous` : The previous value of the property that was tweened, prior to this update.
* A tween property pause.

  ```
  Copytween.on('pause', function(tween, key, target){

  }, scope);

  ```
* A tween property resume.

  ```
  Copytween.on('resume', function(tween, key, target){

  }, scope);

  ```
* A tween property yoyos.

  ```
  Copytween.on('yoyo', function(tween, key, target){

  }, scope);

  ```
* A tween stopped.

  ```
  Copytween.on('stop', function(tween, targets){

  }, scope);

  ```

#### Set callbacks

```
Copytween.setCallback(type, callback, param);

```

* `type` :
  + `'onActive'` : When the Tween is first created it moves to an 'active' state when added to the Tween Manager. 'Active' does not mean 'playing'.
  + `'onStart'` : When the Tween starts playing after a delayed or paused state. This will happen at the same time as `onActive` if the tween has no delay and isn't paused.
  + `'onLoop'` : When a Tween loops, if it has been set to do so. This happens *after* the `loopDelay` expires, if set.
  + `'onComplete'` : When the Tween finishes playback fully. Never invoked if the Tween is set to repeat infinitely.
  + `'onStop'` : Invoked only if the `Tween.stop` method is called.
  + `'onPause'` : Invoked only if the `Tween.pause` method is called. Not invoked if the Tween Manager is paused.
  + `'onResume'` : Invoked only if the `Tween.resume` method is called. Not invoked if the Tween Manager is resumed.
  + `'onYoyo'` : When a TweenData starts a yoyo. This happens *after* the `hold` delay expires, if set.
  + `'onRepeat'` : When a TweenData repeats playback. This happens *after* the `repeatDelay` expires, if set.
  + `'onUpdate'` : When a TweenData updates a property on a source target during playback.
* `callback` :
  + `'onRepeat'`, `'onUpdate'`, `'onYoyo'`

    ```
    Copyfunction(tween, targets, key, current, previous, param) {
        
    }

    ```
  + `'onActive'`, `'onLoop'`, `'onPause'`, `'onResume'`, `'onComplete'`, `'onStart'`, `'onStop'`,

    ```
    Copyfunction(tween, targets, param) {
        
    }

    ```

#### State

* Is playing

  ```
  Copyvar isPlaying = tween.isPlaying();

  ```
* Is paused

  ```
  Copyvar isPaused = tween.isPaused();

  ```
* Is actively and not just in a delayed state

  ```
  Copyvar hasStarted = tween.hasStarted;

  ```

#### Custom ease function

```
Copyvar tween = scene.tweens.add({
    targets: gameObject,
    // ...
    ease: function (t) {  // t: 0~1
        return value;     // value: 0~1
    },
    // ...
});

```

#### Has target

```
Copyvar hasTarget = tween.hasTarget(gameObject);

```

#### Tween value

* Create tween task

  ```
  Copyvar tween = scene.tweens.addCounter({
      from: 0,
      to: 1,
      ease: 'Linear',       // 'Cubic', 'Elastic', 'Bounce', 'Back'
      duration: 1000,
      repeat: 0,            // -1: infinity
      yoyo: false,
      onUpdate(tween, targets, key, current, previous, param) {
          // var value = current;
          // var value = tween.getValue();
      }
  });

  ```

  + [More config parameters...](#creating-a-tween)
* Get value

  ```
  Copyvar value = tween.getValue();

  ```

## Chain

### Create chain

```
Copyvar chain = scene.tweens.chain({
    targets: null,
    tweens: [
        {
            // targets: gameObject,
            alpha: 1,            
            ease: 'Linear',       // 'Cubic', 'Elastic', 'Bounce', 'Back'
            duration: 1000,
            repeat: 0,            // -1: infinity
            yoyo: false
        },        
        // ...
    ],
    
    delay: 0,
    completeDelay: 0,
    loop: 0,  // repeat: 0,
    repeatDelay: 0,
    paused: false,
    persist: true,
    // callbackScope: this,
})

```

* `targets`, or `tweenConfig.targets`
* `tweens` : Array of [tween config](#creating-a-tween)

### Pause / Resume chain

```
Copychain.pause();

```

```
Copychain.resume();

```

### Restart chain

```
Copychain.restart();

```

### Add tween task

```
Copychain.add({
    targets: gameObject,
    alpha: 1,
    ease: 'Linear',       // 'Cubic', 'Elastic', 'Bounce', 'Back'
    duration: 1000,
    repeat: 0,            // -1: infinity
    yoyo: false
})

```

or

```
Copychain.add([tweenConfig0, tweenConfig1, ...]);

```

### Remove tween task

```
Copychain.remove(tweenTask);

```

### Has target

```
Copyvar hasTarget = chain.hasTarget(gameObject);

```

## Flow chart

Yes

No

Yes

No

Yes

No

Start

Callback: onStart

delay

Tween forward  
Callback: onUpdate  
(duration)

hold

Is yoyo

Callback: onYoyo

Tween backword  
Callback: onUpdate  
(duration)

Repeat count > 0

Callback: onRepeat

repeatDelay

Loop count > 0

Callback: onLoop

loopDelay

completeDelay

Callback: onComplete

End

## Tween data

* `tween.data` : An array of TweenData objects, each containing a unique property and target being tweened.
  + `tween.data[i].key` : The property of the target to tween.
  + `tween.data[i].start`, `tween.data[i].end`, `tween.data[i].current` : Ease Value Data.

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Time](time.md)

[Utils](utils.md)

On this page

* [Tweens](#tweens)

  + [Basic usage](#basic-usage)

    - [Creating a tween](#creating-a-tween)
  + [Easing equations](#easing-equations)

    - [Pause / Resume task](#pause--resume-task)
  + [Chain](#chain)

    - [Create chain](#create-chain)
    - [Pause / Resume chain](#pause--resume-chain)
    - [Restart chain](#restart-chain)
    - [Add tween task](#add-tween-task)
    - [Remove tween task](#remove-tween-task)
    - [Has target](#has-target-1)
  + [Flow chart](#flow-chart)
  + [Tween data](#tween-data)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../index.md)



Tweens