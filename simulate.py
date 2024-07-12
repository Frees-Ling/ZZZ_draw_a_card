#抽卡模拟器
import random

S_CHARACTER = ['猫又（Nekomata）','11（Soldier 11）','科莱达（Koleda）','莱卡恩（Lycaon）','格蕾丝（Grace）','莉娜（Rina）']
S_EQUIP = ['钢垫（Steel Cushion）', '地狱火齿轮（Hellfire Gears）', '束缚（The Restrained）', '硫磺（The Brimstone）', '融合编译器（Fusion Compiler）', '哭泣摇篮（Weeping Cradle）']
A_CHARACTER = ['安比（Anby）', '比利（Billy）', '苍鹭（Soukaku）', '妮可（Nicole）','安东（Anton）','露西（Lucy）', '柯林（Korin）', '本（Ben）', '派珀（Piper）']
A_EQUIP = [ '街头超级巨星（Street Superstar）', '星光引擎（Starlight Engine）', '原始变形者（Original Transmorpher）', '德玛拉电池II型（Demara Battery Mark II）', '星光引擎复制品（Starlight Engine Replica）', '害羞恶魔（Bashful Demon）', '时间切片（Slice of Time）', '蒸汽烤箱（Steam Oven）','哭泣双子（Weeping Gemini）', '保险库（The Vault）', '红轴钻机（Drill Rig – Red Axis）', '砰砰大炮（Kaboom the Cannon）', '雨林美食家（Rainforest Gourmet）', '珍贵的化石核心（Precious Fossilized Core）', '兔耳带（Bunny Band）', '管家（Housekeeper）', '大圆筒（Big Cylinder）', '咆哮之旅（Roaring Ride）']

class GachaSimulator:
    def __init__(self):
        #卡池
        self.pool = {
            'S': {'rate': 0.16, 'cards': S_CHARACTER + S_EQUIP},
            'A': {'rate': 0.84, 'cards': A_CHARACTER + A_EQUIP},
        }
        self.cumulative_rates = self._calculate_cumulative_rates()

    def _calculate_cumulative_rates(self):
        cumulative_rates = []
        cumulative = 0
        for rarity, data in self.pool.items():
            cumulative += data['rate']
            cumulative_rates.append((rarity, cumulative))
        return cumulative_rates

    def draw_card(self):
        rand_num = random.random()
        for rarity, cumulative_rate in self.cumulative_rates:
            if rand_num <= cumulative_rate:
                return random.choice(self.pool[rarity]['cards'])
        return None
    def draw_multiple(self, n):
        return [self.draw_card() for i in range(n)]

def baodi_S(x):
    if x == 80:
        x = 0
    return random.choice(S_CHARACTER + S_EQUIP)

if __name__ == '__main__':
    n = 0
    a = 0
    simulator = GachaSimulator()
    c = input("是否要显示卡池信息？(y or n)：")
    if c == 'y':
        print("S级卡池：")
        for i in S_CHARACTER + S_EQUIP:
            print(i)
        print("A级卡池：")
        for i in A_CHARACTER + A_EQUIP:
            print(i)
    while True:
        user_input = int(input("请输入要抽卡次数(1 or 10), 输入0退出："))
        if n == 80 :
            if n == 80:
                baodi_S(n)
                n = 0

        if user_input == 1:
            d = simulator.draw_card()
            print("抽卡结果为：", d)
            n += 1
            a += 1
            for i in S_CHARACTER + S_EQUIP:
                if i == d:
                    print("恭喜您抽到了S级人物/装备！——————", i)
        elif user_input == 10:
            d = simulator.draw_multiple(10)
            print("抽卡结果：")
            t = list(d)
            for i in t:
                print(i)
            for i in S_CHARACTER + S_EQUIP:
                if i in t:
                    print("恭喜您抽到了S级人物/装备！——————", i)
            n += 10
            a += 10
        else:
            print("输入有误，请重新输入！\n 只能抽一次或者十次哦！")
        if user_input == 0:
            break
        print("已抽卡{}次".format(a))

    # print("抽一次卡：", simulator.draw_card())
    # print("抽十次卡：", simulator.draw_multiple(10))