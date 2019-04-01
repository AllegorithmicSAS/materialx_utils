import sys
import os
from urllib import unquote
from matxtools import MatXExporter
import json

def _guess_mesh_name(material_data):
	def _extract_mesh_name(ts, pattern, path):
		base_name = os.path.splitext(os.path.basename(path))[0]
		expanded_pattern = pattern.replace('$textureSet', ts)
		suffix_start = 1
		while suffix_start < min(len(base_name), len(expanded_pattern)):
			if base_name[-suffix_start] != expanded_pattern[-suffix_start]:
				break
			suffix_start = suffix_start + 1
		return base_name[0:len(base_name) - suffix_start + 1]
	for ts_name, ts_data in material_data.items():
		for pattern, path in ts_data.items():
			if ts_name != '' and pattern != '' and path != '':
				return _extract_mesh_name(ts_name, pattern, path)

channel_mapping = {
	'BaseColor'  : {'name':'base_color', 'type': 'color3', 'value':[0.0, 0.0, 0.0], 'colorspace':'sRGB'},
	'Emissive'   : {'name':'emissive', 'type': 'color3', 'value':[0.0, 0.0, 0.0], 'colorspace':'sRGB'},
	'Height'     : {'name':'height', 'type': 'float', 'value':.5, 'colorspace':'Raw'},
	'Metalness'  : {'name':'metalness', 'type': 'float', 'value':0.0, 'colorspace':'Raw'},
	'Normal'     : {'name':'normal', 'type': 'vector3', 'value':[0.0, 1.0, 0.0], 'colorspace':'Raw'},
	'Roughness'  : {'name':'specular_roughness', 'type': 'float', 'value':0.0, 'colorspace':'Raw'},
	'Tangent'    : {'name':'tangent', 'type': 'vector3', 'value': [0, 0, 0]},
	'Coat_normal': {'name':'coat_normal', 'type': 'vector3', 'value': [0, 0, 0]},

}

def _export_texture_set(exporter, ts_name, ts_data):
	print('Starting export: ' + ts_name)
	matx_channel_data = {}
	for channel_name, channel_data in channel_mapping.items():
		sp_key = '$mesh_$textureSet_' + channel_name
		print(sp_key)
		sp_data = ts_data.get(sp_key, None)
		if sp_data and sp_data != "":
			# We have data from sp
			matx_channel_data[channel_data['name']] = {
				'type': channel_data['type'],
				'filename': os.path.basename(sp_data),
				'colorspace': channel_data['colorspace']
			}
		else:
			# Use defaults if no data exists
			matx_channel_data[channel_data['name']] = {
				'type': channel_data['type'],
				'value': channel_data['value'],
			}
	print('Writing material: ' + ts_name)
	exporter.materialx_write_material(ts_name,
			'standard_surface',
			matx_channel_data)

def main():
	target_file_name = sys.argv[1]
	material_data = json.loads(unquote(sys.argv[2]))
	mesh_name = _guess_mesh_name(material_data)	
	exporter = MatXExporter(target_file_name)
	for ts_name, ts_data in material_data.items():
		_export_texture_set(exporter, ts_name, ts_data)
	exporter.write()
	return 0

if __name__ == '__main__':
	main()