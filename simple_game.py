# 导入必要的模块
import random

# 定义中国省份的列表
provinces = ['河北省', '山西省', '辽宁省', '吉林省', '黑龙江省',
            '江苏省', '浙江省', '安徽省', '福建省', '江西省',
            '山东省', '河南省', '广东省', '湖南省', '湖北省',
            '海南省', '四川省', '贵州省', '云南省', '陕西省',
            '甘肃省', '青海省', '台湾省', '内蒙古自治区',
            '广西壮族自治区', '西藏自治区', '宁夏回族自治区',
            '新疆维吾尔自治区']

# 随机选择一个省份
province = random.choice(provinces)

# 显示选中的省份名称
print("你选中的省份是：", province)

print('end')