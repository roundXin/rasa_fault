from neo4j import GraphDatabase
from config import NEO4J_CONFIG
import numpy as np
import csv
import pandas as pd

DEIVER = GraphDatabase.driver(**NEO4J_CONFIG)


class VehicleLabel(object):
    def __init__(self):
        # self.session = DEIVER.session()
        self.a = ''

    def getAllData(self):
        """
        获取图谱数据
        :return:
        """
        # with DEIVER.session() as session:
        #     cypher = ''

    def vehicleFault(self, unit):
        """
        车辆状态、故障部件、故障现象、原因部件、原因分析、方案部件、方案分析 标注
        :return:
        """
        with DEIVER.session() as session:
            cypher = 'match (n:`{unit}`) return n.name as name'.format(unit=unit)
            data = session.run(cypher).data()
            return data
        return null

    def vehicleFaultDetail(self, unit1, ralation1, unit2, ralation2, unit3, savepath):
        """
        车辆状态及故障部件及故障现象标注
        :return:
        """
        with DEIVER.session() as session:
            cypher = 'match (l:`{unit1}`)-[r:`{ralation1}`]->(m:`{unit2}`)-[r2:`{ralation2}`]->(n:`{unit3}`) return l.name as name1,m.name as name2,n.name as name3'.format(
                unit1=unit1, ralation1=ralation1, unit2=unit2, ralation2=ralation2, unit3=unit3)
            data = session.run(cypher).data()
            data = pd.DataFrame(data).apply(lambda x: self.setDetailDataLabel(x), axis=1)
            # data = pd.DataFrame(data).apply(lambda x: '['+x[0]+x[1]+x[2]+']{}', axis=1)
            data.to_csv(savepath, sep='|', header=None, index=None, quoting=csv.QUOTE_NONE, encoding='utf-8')
            return data
        return null

    def vehicleFaultReason(self, unit1, ralation1, unit2, savepath):
        """
        原因部件及原因分析标注
        :return:
        """
        with DEIVER.session() as session:
            cypher = 'match (n:`{unit1}`)-[r:`{ralation1}`]->(m:`{unit2}`) return n.name as name1,m.name as name2'.format(
                unit1=unit1, ralation1=ralation1, unit2=unit2)
            data = session.run(cypher).data()
            data = pd.DataFrame(data).apply(lambda x: self.setReasonDataLabel(x), axis=1)
            data.to_csv(savepath, sep='|', header=None, index=None, quoting=csv.QUOTE_NONE, encoding='utf-8')
            return data
        return null

    def vehicleFaultSolution(self, unit1, ralation1, unit2, savepath):
        """
        方案部件及方案分析标注
        :return:
        """
        with DEIVER.session() as session:
            cypher = 'match (n:`{unit1}`)-[r:`{ralation1}`]->(m:`{unit2}`) return n.name as name1,m.name as name2'.format(
                unit1=unit1, ralation1=ralation1, unit2=unit2)
            data = session.run(cypher).data()
            data = pd.DataFrame(data).apply(lambda x: self.setSolutionDataLabel(x), axis=1)
            data.to_csv(savepath, sep='|', header=None, index=None, quoting=csv.QUOTE_NONE, encoding='utf-8')
            return data
        return null

    def setDetailDataLabel(self, x):
        """
        设置故障描述标签
        :return:
        """
        x0s = self.setStrLabel(x[0], 'detailStatus')
        x1s = self.setStrLabel(x[1], 'unit')
        x2s = self.setStrLabel(x[2], 'detailPhenomenon')
        return '- ' + x0s + x1s + x2s

    def setReasonDataLabel(self, x):
        """
        设置故障原因标签
        :return:
        """
        x0s = self.setStrLabel(x[0], 'reasonAnalyse')
        x1s = self.setStrLabel(x[1], 'unit')
        return '- ' + x0s + x1s

    def setSolutionDataLabel(self, x):
        """
        设置解决方案标签
        :return:
        """
        x0s = self.setStrLabel(x[0], 'unit')
        x1s = self.setStrLabel(x[1], 'schemeOperation')
        return '- ' + x0s + x1s

    def setStrLabel(self, strText, label):
        """
        词槽标注
        :param strText:
        :param label:
        :return:
        """
        # strText = strText.split('。|，|.|,')
        # ['['+i+']({0})'.format(label) for i in strText]
        # start = ''
        # end = ''
        result = ''
        isFirst = True
        for i in strText:
            if i in ['。', ',', '，', ' '] and not isFirst:
                result += ']({0}){1}'.format(label, i)
                isFirst = True
                continue
            elif isFirst:
                result += '['
                isFirst = False
            result += i
        else:
            if not isFirst:
                result += ']({0})'.format(label)
        return result


if __name__ == '__main__':
    v = VehicleLabel()
    r = v.vehicleFaultDetail('车辆状态', '状态部件', '故障部件', '部件现象', '故障现象', './data/故障描述.txt')
    r = v.vehicleFaultSolution('原因部件', '分析', '原因分析', './data/解决方案.txt')
    r = v.vehicleFaultReason('方案操作', '维修', '方案部件', './data/故障原因.txt')
    # x0s = str('你好。哈哈哈，haha').split('。|，|.|,')
    # print(x0s)

    # r = v.setStrLabel('你好，哈哈哈。哦', 'lsq')
    # print(r)
