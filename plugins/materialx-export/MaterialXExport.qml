// Copyright (C) 2017 Allegorithmic
//
// This software may be modified and distributed under the terms
// of the MIT license.  See the LICENSE file for details.

import QtQuick 2.3
import QtQuick.Layouts 1.2
import QtQuick.Dialogs 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import AlgWidgets 1.0
import AlgWidgets.Style 1.0
import "."
import "./ExportTools.js" as ExportTools

AlgWindow
{
    id: window
    title: "Substance Painter - MaterialX Export"
    visible: false
    width: 300
    height: mainLayout.height

    //Flags to keep the window on top
    flags: Qt.Window
    | Qt.WindowTitleHint // title
    | Qt.WindowSystemMenuHint // Recquired to add buttons
    | Qt.WindowMinMaxButtonsHint // minimize and maximize button
    | Qt.WindowCloseButtonHint // close button


    ColumnLayout {
        id: mainLayout
        anchors {
            left: parent.left;
            right: parent.right;
        }
        RowLayout {
            anchors {
                left: parent.left;
                right: parent.right;
            }
            AlgLabel {
                anchors {
                    left: parent.left;
                }
                text: "Conflict Policy"
            }
            AlgComboBox
            {
                anchors {
                    right: parent.right;
                }
                id: updatePolicy
                model: ListModel {
                    id: updatePolicyModel
                    ListElement { text: "Update" }
                    ListElement { text: "Import" }
                    ListElement { text: "Fail" }
                }
            }
        }
        RowLayout {
            AlgTextInput {
                id: filenameField
                width: 150
                Layout.preferredWidth: 150
                anchors {
                    left: parent.left;
                }
            }
            AlgButton {
                FileDialog
                {
                    id: fileDialog
                    title: "Select Target File"
                    nameFilters: ["MaterialX files (*.mtlx)", "All files (*)"]
                    selectedNameFilter: "MaterialX files (*.mtlx)"
                    selectExisting: false
                    folder: "c:\\temp\\matxexport"
                    onAccepted: {
                        var filename = alg.fileIO.urlToLocalFile(fileUrl.toString());
                        filenameField.text = filename
                    }
                }
                onClicked: {
                    fileDialog.open();
                }
                text: "Select File"
                anchors {
                    right: parent.right;
                }

            }
        }
        AlgButton
        {
            anchors {
                left: parent.left;
                right: parent.right;
            }
            AlgWindow
            {
                id: progressWindow
                title: "Exporting"
                modality: WindowModal
                width: 600
                height: progressLayout.height
                ColumnLayout {
                    id: progressLayout
                    anchors {
                        left: parent.left;
                        right: parent.right;
                    }
                    AlgLabel
                    {
                        id: statusLabel
                        text: "Idle"
                        anchors {
                            left: parent.left;
                            right: parent.right;
                        }
                    }
                    ProgressBar
                    {
                       indeterminate: true
                        anchors {
                            left: parent.left;
                            right: parent.right;
                        }
                    }
                }
            }
            id: exportButton
            text: "Export"
            onClicked: {
                statusLabel.text = "Exporting MaterialX file: " + filenameField.text;
                progressWindow.open()
                var map_data = ExportTools.exportMaps(filenameField.text)
                ExportTools.writeMtlx(filenameField.text, map_data, window.emitPythonDone)
            }

        }
    }
    
    signal pythonDone(var data)


    onPythonDone: {
        alg.log.info("Python done");
        alg.log.info(data.cerr);
        progressWindow.close();
    }
    // Trampoline functions to emit events
    function emitPythonDone(data) {
        pythonDone(data)
    }

}
