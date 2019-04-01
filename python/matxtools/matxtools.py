import sys
import MaterialX as mx


def _add_value_input(bi, data):
    if data['type'] == 'color3':
        bi.setValue(mx.Color3(data['value']))
    if data['type'] == 'vector3':
        bi.setValue(mx.Vector3(data['value']))
    elif data['type'] == 'float':
        bi.setValue(float(data['value']))

def _add_file_input(bi, input_name, data, node_graph, material_name):
    decorated_input = input_name + '_' + material_name
    sys.stderr.write(decorated_input + '\n')
    image_node = node_graph.addNode('image', decorated_input, data['type'])
    image_node.setColorSpace(data['colorspace'])
    file_param = image_node.addParameter('file', 'filename')
    file_param.setValue(data['filename'], 'filename')
    if input_name == 'normal':
        # Normal map need to go through the normal map node
        normal_node = node_graph.addNode('normalmap', decorated_input + '_normal', data['type'])
        normal_node.setConnectedNode('in', image_node)
        next_node = normal_node
    else:
        next_node = image_node
    print(data['type'])
    output = node_graph.addOutput(decorated_input + '_output', data['type'])
    output.setConnectedNode(next_node)
    bi.setConnectedOutput(output)
    bi.setType(data['type'])

class MatXExporter:
    def __init__(self, filename):
        self.mDoc = mx.createDocument()
        self.mFilename = filename

    def materialx_write_material(self, material_name, shader_ref, bindings):
        material = self.mDoc.addMaterial(material_name)
        sr = material.addShaderRef(material_name, shader_ref)
        ng_name = material_name + '_node_graph' 
        for binding_name, binding_data in bindings.items():        
            bi = sr.addBindInput(binding_name)
            if 'value' in binding_data:
                _add_value_input(bi, binding_data)
            elif 'filename' in binding_data:
                node_graph = self.mDoc.addNodeGraph(ng_name) if self.mDoc.getNodeGraph(ng_name) is None else self.mDoc.getNodeGraph(ng_name)
                _add_file_input(bi, binding_name, binding_data, node_graph, material_name)

    def write(self):
        mx.writeToXmlFile(self.mDoc, self.mFilename)
