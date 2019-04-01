from matxtools import materialx_write_material

def main():
	materialx_write_material('test.mtlx', 
		'test_material',
		'test_shader', 
		{
			'base': {'type': 'float', 'value': 1},
			'base_color': {'type': 'color3', 'value':[1, 0, 1]},
			'specular_roughness': {'type': 'float', 'filename':'c:\\temp\\apa.png', 'colorspace':'Raw'},
			'metalness': {'type': 'float', 'value':.5},
			'normal': {'type': 'vector3', 'filename':'c:\\temp\\apa2.png', 'colorspace':'Raw'},
			'tangent': {'type': 'vector3', 'value': [0, 0, 0]},
			'coat_normal': {'type': 'vector3', 'value': [0, 0, 0]},
		})

if __name__ == '__main__':
	main()