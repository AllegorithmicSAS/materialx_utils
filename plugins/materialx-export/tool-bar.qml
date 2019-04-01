import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Window 2.2
import QtQuick.Layouts 1.2
import AlgWidgets 1.0
import AlgWidgets.Style 1.0

Rectangle
{
    id: materialXExportButton
    width: 50
    height: 30
    border.color: "white"
    property var windowReference : null
    color: buttonMouseArea.containsMouse ? "grey" : "black"
    
    Text {
        id: buttonLabel
        anchors.centerIn: parent
        text: "MaterialX\nExport"
        color: "white"
    }
    signal buttonClick()
        
    onButtonClick:
    {
        try
        {
            windowReference.visible = true
            //windowReference.refreshInterface()
            windowReference.raise()
            windowReference.requestActivate()
        }
        catch(err)
        {
            alg.log.exception(err)
        }
    }
    MouseArea {
        id: buttonMouseArea
        //anchor all sides of the mouse area to the rectangle's anchors
        anchors.fill: parent 
         
        //onClicked handles valid mouse button clicks
        onClicked: buttonClick()
    }
}
