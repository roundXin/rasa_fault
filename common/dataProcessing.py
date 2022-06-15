from neo4j import GraphDatabase
from config import NEO4J_CONFIG
import numpy as np
import pandas as pd

DEIVER = GraphDatabase.driver(NEO4J_CONFIG)


class VehicleLabel(object):
    def __init__(self):
        # self.session = DEIVER.session()
        pass
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
            cypher = 'match (n:`$unit`) return n.name as name'
            data = session.run(cypher, unit).data()
            return data
        return null

    def vehicleFault2(self, unit1, ralation1, unit2):
        """
        车辆状态及故障部件及故障现象、原因部件及原因分析、方案部件及方案分析标注
        :return:
        """
        with DEIVER.session() as session:
            cypher = 'match (n:`$unit1`)-[r:`$ralation1`]->(m:`$unit2`) return n.name as name1,m.name as name2'
            data = session.run(cypher, unit1, ralation1, unit2).data()
            return data
        return null

    def vehicleFault3(self, unit1, ralation1, unit2, ralation2, unit3):
        """
        车辆状态及故障部件及故障现象、原因部件及原因分析、方案部件及方案分析标注
        :return:
        """
        with DEIVER.session() as session:
            cypher = 'match (l:`$unit1`)-[r:`$ralation1`]->(m:`$unit2`)-[r2:`$ralation2`]->(n:`$unit3`) return l.name as name1,m.name as name2,n.name as name3'
            data = session.run(cypher, unit1, ralation1, unit2, ralation2, unit3).data()
            return data
        return null

if __name__ == '__main__':
    v = VehicleLabel()
    vehicleFault