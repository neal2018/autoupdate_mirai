import json
import os
import sys
import re
import collections


json_path = "test.json"


dic = {}


# Need to change to words:
# - [ ] Categories
# - [ ] HideTags
# - [ ] Faction
# - [ ] Group
# - [ ] CardUseInfo
# - [ ] CardType


categorie_str = """DoubleAgent,    //双面间谍
WildHunt,       //狂猎
Tactic,         //谋略
Beast,          //野兽
Leader,         //领袖牌
Mage,           //法师
Boss,           //首领
Vampire,        //吸血鬼
Cintra,         //辛特拉
Insectoid,      //类虫生物
Stray,          //流亡军
Construct,      //构造体
Spell,          //法术
Redania,        //瑞达尼亚
SiegeSupport,   //攻城支援
ClanDrummond,   //德拉蒙家族
Specter,        //鬼灵
Cursed,         //诅咒生物
Soldier,        //士兵
Kaedwen,        //科德温
Vodyanoi,       //水生
ClanTuirseach,  //图尔赛克家族
ClanTordarroch, //托达洛克家族
ClanDimun,      //迪门家族
Witcher,        //猎魔人
Cultist,        //呓语
Alchemy,        //炼金
Reckless,       //鲁莽
ClanHeymaey,    //海玫家族
Blitz,          //闪击
Dryad,          //树精
Special,        //特殊
Elf,            //精灵
Lyria,          //莱里亚
Necrophage,     //食腐生物
Machine,        //机械
Aedirn,         //亚甸
Support,        //辅助
ClanAnCraite,   //奎特家族
Dwarf,          //矮人
Draconid,       //龙兽
SiegeEngine,    //攻城器械
Temeria,        //泰莫利亚
Officer,        //军官
Weather,        //天气
Organic,        //有机
Item,           //道具
Hazard,         //灾厄
Boon,           //恩泽
Ambush,         //伏击
Doomed,         //佚亡
Bear,           //巨熊
Ogroid,         //食人魔
BlueStripes,    //蓝衣铁卫
Breedable,      //繁育
Devourer,       //吞食者
Dragon,         //巨龙
Harpy,          //鹰身女妖
Medic,          //医生
Stubborn,       //坚守
Permadeath,     //永逝
Peasant,        //农民
Potion,         //药水
Relict,         //残物
Regressing,     //回溯
Shapeshifter,   //变身
Token,          //退场
Agent,          //密探
ClanBrokvar,    //布洛克瓦尔家族
Test,           //测试"""


categorie_list = re.sub(r" *//.*(\n)?", "", categorie_str).split(",")


hideTag_str = """Deathwish,  //遗愿
Geralt,     //杰洛特
Yennefer,   //叶奈法
Triss,      //特莉丝
Zoltan,     //卓尔坦"""
hideTag_list = re.sub(r" *//.*(\n)?", "", hideTag_str).split(",")


faction_str = """All = 0,//全部
Neutral = 1,//中立
Monsters = 2,//怪物
Nilfgaard = 3,//帝国
NorthernRealms = 4,//北方
ScoiaTael = 5,//松鼠党
Skellige = 6,//群岛"""
faction_list = re.sub(r" = [0-9],( )*//.*(\n)?", ",", faction_str).split(",")


group_str = """Copper,//铜
Silver,//银
Gold,//金
Leader//领袖"""
group_list = re.sub(r" *//.*(\n)?", "", group_str).split(",")


cardUseInfo_str = """ReSet,
MyPlace,
EnemyPlace,
AnyPlace,
MyRow,
EnemyRow,
AnyRow"""
cardUseInfo_list = re.sub(r"\n", "", cardUseInfo_str).split(",")


cardType_str = """Unit,
Special,
Any"""
cardType_list = re.sub(r"\n", "", cardType_str).split(",")



with open(json_path, 'rb') as f:
    dic = json.load(f)


def get_order(string):
    order = {'CardArtsId': 16,
             'CardId': 0,
             'CardType': 6,
             'CardUseInfo': 8,
             'Categories': 7,
             'Countdown': 12,
             'CrewCount': 14,
             'Faction': 5,
             'Flavor': 7.5,
             'Group': 4,
             'HideTags': 8,
             'Info': 3,
             'IsConcealCard': 13,
             'IsCountdown': 11,
             'IsDerive': 9,
             'IsDoomed': 10,
             'Name': 1,
             'Strength': 2}
    return order[string]


for i, v in dic.items():
    for key in v.keys():
        if key == "Categories":
            v[key] = [categorie_list[num] for num in v[key]]
        if key == "HideTags":
            if v[key] is None:
                v[key] = []
            else:
                v[key] = [hideTag_list[num] for num in v[key]]
        if key == "Faction":
            v[key] = faction_list[v[key]]
        if key == "Group":
            v[key] = group_list[v[key]]
        if key == "CardUseInfo":
            v[key] = cardUseInfo_list[v[key]]
        if key == "CardType":
            v[key] = cardType_list[v[key]]
    dic[i] = collections.OrderedDict(
        sorted(dic[i].items(), key=lambda x: get_order(x[0])))


with open("cardInfo.json", 'w', encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False)
