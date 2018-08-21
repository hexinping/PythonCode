# -*- coding: UTF-8 -*-


#https://www.jb51.net/article/74942.htm
from xml.etree.ElementTree import ElementTree,Element


class ElementTree_Class():

    def __init__(self, in_path):
        self.in_path = in_path


    def read_xml(self):
        tree = ElementTree()
        tree.parse(self.in_path)
        self.tree = tree
        # return tree

    def write_xml(self, out_path):
        '''将xml文件写出
          tree: xml树
          out_path: 写出路径'''
        self.tree.write(out_path, encoding="utf-8", xml_declaration=True)

    def if_match(self, node, kv_map):
        '''判断某个节点是否包含所有传入参数属性
          node: 节点
          kv_map: 属性及属性值组成的map'''
        for key in kv_map:
            if node.get(key) != kv_map.get(key):
                return False
        return True

    def if_matchTagValue(self, node, kv_map):
        '''判断某个节点是否包含所有传入参数属性
          node: 节点
          kv_map: tag和标签值组成的map'''
        for key in kv_map:
            value1 = node.text
            value2 = kv_map.get(key)
            if value1 != value2:
                return False
        return True

    def find_nodes(self, path):
        '''查找某个路径匹配的所有节点
          tree: xml树
          path: 节点路径'''
        return self.tree.findall(path)

    def get_node_by_keyvalue(self, nodelist, kv_map, isTag=False):
        '''根据属性及属性值定位符合的节点，返回节点
          nodelist: 节点列表
          kv_map: 匹配属性及属性值map'''
        result_nodes = []
        for node in nodelist:
            if not isTag:
                if self.if_match(node, kv_map):
                    result_nodes.append(node)
            else:
                if self.if_matchTagValue(node, kv_map):
                    result_nodes.append(node)
        return result_nodes

    def change_node_properties(self, nodelist, kv_map, is_delete=False):
        '''修改/增加 /删除 节点的属性及属性值
          nodelist: 节点列表
          kv_map:属性及属性值map'''
        for node in nodelist:
            for key in kv_map:
                if is_delete:
                    if key in node.attrib:
                        del node.attrib[key]
                else:
                    node.set(key, kv_map.get(key))

    def change_node_text(self, nodelist, text, is_add=False, is_delete=False):
        '''改变/增加/删除一个节点的文本
          nodelist:节点列表
          text : 更新后的文本'''
        for node in nodelist:
            if is_add:
                node.text += text
            elif is_delete:
                node.text = ""
            else:
                node.text = text

    def create_node(self, tag, property_map, content):
        '''新造一个节点
          tag:节点标签
          property_map:属性及属性值map
          content: 节点闭合标签里的文本内容
          return 新节点'''
        element = Element(tag, property_map)
        element.text = content
        return element

    def add_child_node(nodelist, element):
        '''给一个节点添加子节点
          nodelist: 节点列表
          element: 子节点'''
        for node in nodelist:
            node.append(element)

    def del_node_by_tagkeyvalue(self, nodelist, tag, kv_map):
        '''同过属性及属性值定位一个节点，并删除之
          nodelist: 父节点列表
          tag:子节点标签
          kv_map: 属性及属性值列表'''
        for parent_node in nodelist:
            children = parent_node.getchildren()
            for child in children:
                if child.tag == tag and self.if_match(child, kv_map):
                    parent_node.remove(child)

    def check_node_isExist(self, nodelist, tag):

        for node in nodelist:
            if node.tag == tag:
                return True
        return False



