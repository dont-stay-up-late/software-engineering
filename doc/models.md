# 模型类

所有模型类继承自`pygame.sprite.Sprite`，`Sprite`类提供了`update`函数，用以显示、刷新屏幕上的对象。

在模型类中，主要的模型是人物，此外还有子弹，但现在看来子弹可有可无，或许没有的话实现起来更方便，毕竟只需要两帧的动画。子弹类`Bullet`也在此文件中实现（未完成），但是否需要最终实现可以再议。以下仅讨论人物类。

人物类`CharacterModel`是所有人物类的基类，守方人物类`Defender`和攻方人物类`Attacker`均继承自此类，而各种具体的攻守方人物类分别继承自`Defender`和`Attacker`。

以下按自顶向下的顺序，介绍各类及它们的重要成员，以梳理各类之间的关系。窘于时间，只能挑选重点，无法尽数每一个成员。希望之后有时间。

## `CharacterModel`

`CharacterModel`类是所有人物模型类的抽象基类。规定了所有人物模型类都要有的成员变量、方法，以及一些静态成员。

每一个`CharacterModel`子类的实例对象，都有其在`__init__(self, position, direction)`函数中规定的一系列属性。这里解释其中的2个。

1. `self.position`：一个`tuple`，保存了对象的坐标（像素）；
2. `self.direction`：取值为0、1、2、3，分别表示当前对象的朝向为上、左、下、右（与静态常量`MOVEMENT`中规定一致）；

当一个人物对象被创建时，首先会执行其`__init__(self, position, direction)`方法，其中，会调用其`init_image(self)`方法，这一方法的作用是初始化对象的UI，可能会需要加载图片？

由于在我们的游戏中，人物均按范围攻击，因而不存在特定的攻击对象一说。`attack(self)`方法会根据自己是攻方还是守方，遍历所有对方对象，判断其是否在自己的攻击范围内。如果在，那么就调用对方的`attacked(self, loss, attacker)`方法，对其进行攻击。

`attacked(self, loss, attacker)`方法通常会直接在自己的`self.hp`上扣掉`loss`的血量。如果受到伤害后自己的`self.hp <= 0`，那么就调用`die(self)`。之所以需要将`attacker`加入参数，是因为攻方的药剂师可以在收到伤害时，直接杀死攻击者。

当对象死亡时，`die(self)`方法会被调用，以将本对象从画面中抹去。

`get_coordinate(self)`将自身的像素坐标化为地图坐标。

`reachable(reaching_char, reached_char, reach_model)`是一个静态方法，用来判断角色是否在另一角色的覆盖范围内。这取决于后者的位置（`reaching_char.position`）、朝向（`reaching_char.direction`）、攻击范围（`reach_model`），以及前者的位置（`reached_char.position`）。之所以将`reach_model`单独放入参数表，而非调用`reaching_char.reach_model`，是因为攻方的恐怖分子既有`reach_model`，又有`special_reach_model`。

## `Defender(CharacterModel)`

`speed`为`0`的`CharacterModel`，也是抽象类。

## `Attacker(CharacterModel)`

`speed`不为`0`的`CharacterModel`，又是抽象类。

## `CivilianDefender(Defender)`、`FattyDefender(Defender)`、`KamikazeDefender(Defender)`

调整了各种参数的守方平民、胖墩、敢死队。

## `CivilianAttacker(Attacker)`、`FattyAttacker(Attacker)`、`KamikazeAttacker(Attacker)`

调整了各种参数的攻方平民、胖墩、敢死队。

## `PharmacistDefender(Defender)`、`AuraDefender(Defender)`、`BombDefender(Defender)`

调整了各种参数、实现了各种特殊技能的守方药剂师、工头、恐怖分子。重载了一些函数（`update(self)`、`die(self)`）来触发技能，所有一次性技能都通过`special(self, character)`来触发，所有状态性技能都通过静态的`activate_special(character)`和`deactivate_special(character)`来管理。

## `PharmacistAttacker(Attacker)`、`AuraAttacker(Attacker)`、`BombAttacker(Attacker)`

调整了各种参数、实现了各种特殊技能的攻方药剂师、工头、恐怖分子。重载了一些函数（`update(self)`、`die(self)`）来触发技能，所有一次性技能都通过`special(self, character)`来触发，所有状态性技能都通过静态的`activate_special(character)`和`deactivate_special(character)`来管理。