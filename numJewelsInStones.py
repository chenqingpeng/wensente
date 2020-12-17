
＃给定字符串J代表石头中宝石的类型，和字符串S代表你拥有的石头。S中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
＃
＃J中的字母不重复，J和S中的所有字符都是字母。字母区分大小写，因此“ a”和“ A”是不同类型的石头。
＃
＃示例1：
＃
＃输入：J =“ aA”，S =“ aAAbbbb”
＃输出：3
＃示例2：
＃
＃输入：J =“ z”，S =“ ZZ”
＃输出：0

类 解决方案：
    def  numJewelsInStones（self，J：str，S：str）->  int：
        jewelsSet  = 套装（J）
        返回 总和（小号 在 jewelsSet 为 小号 的 小号）

    打印（numJewelsInStones（“”，“ aA”，“ aAAbbbb”））

