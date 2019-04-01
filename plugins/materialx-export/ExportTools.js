function exportMaps(target_file) {
    var filename = target_file.replace(/^.*[\\\/]/, '')
    var base_path = target_file.substr(0, target_file.length - filename.length)
    alg.log.info(filename)
    alg.log.info(base_path)
    if(!alg.fileIO.exists(base_path)) {
        throw "Target directory " + base_path + " doesn't exist";
    }
    var res = alg.mapexport.exportDocumentMaps("Arnold 5 (AiStandard)", base_path, "png")
    alg.log.info(res)
    return res
}

function writeMtlx(target_file, map_data, onDone) {
    alg.log.info('Starting conversion')
    // Subprocess seem to run from the directory of the plugin
    alg.subprocess.start(['python', 'python/materialx_export.py', target_file, escape(JSON.stringify(map_data))], onDone)
}
