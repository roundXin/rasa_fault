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

    def vehicleFaultReason(self, unit1, ralation1, unit2, savepath):
        """
        原因部件及原因分析标注
        :return:
        """
        with DEIVER.session() as session:
            cypher = 'match (n:`{unit1}`)-[r:`{ralation1}`]->(m:`{unit2}`) return n.name as name1,m.name as name2'.format(
                unit1=unit1, ralation1=ralation1, unit2=unit2)
            data = session.run(cypher).data()
            data = pd.DataFrame(data).apply(lambda x: '- [' + x[0] + '](reasonUnit)[' + x[1] + '](reasonAnalyse)', axis=1)
            data.to_csv(savepath,sep='|', header=None, index=None, quoting=csv.QUOTE_NONE,encoding='utf-8')
            return data
        return null

    def vehicleFaultScheme(self, unit1, ralation1, unit2, savepath):
        """
        方案部件及方案分析标注
        :return:
        """
        with DEIVER.session() as session:
            cypher = 'match (n:`{unit1}`)-[r:`{ralation1}`]->(m:`{unit2}`) return n.name as name1,m.name as name2'.format(
                unit1=unit1, ralation1=ralation1, unit2=unit2)
            data = session.run(cypher).data()
            data = pd.DataFrame(data).apply(lambda x: '- [' + x[0] + '](schemeUnit)[' + x[1] + '](schemeAnalyse)', axis=1)
            data.to_csv(savepath,sep='|', header=None, index=None, quoting=csv.QUOTE_NONE,encoding='utf-8')
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
            data = pd.DataFrame(data).apply(
                lambda x: '- [' + x[0] + '](detailStatus)[' + x[1] + '](detailUnit)[' + x[2] + '](detailPhenomenon)',
                axis=1)
            data.to_csv(savepath,sep='|', header=None, index=None, quoting=csv.QUOTE_NONE,encoding='utf-8')
            return data
        return null


if __name__ == '__main__':
    v = VehicleLabel()
    r = v.vehicleFaultDetail('车辆状态', '状态部件', '故障部件', '部件现象', '故障现象', './data/故障描述.txt')
    r = v.vehicleFaultScheme('原因部件', '分析', '原因分析', './data/故障原因.txt')
    r = v.vehicleFaultReason('方案操作', '维修', '方案部件', './data/解决方案.txt')
    # print(r)