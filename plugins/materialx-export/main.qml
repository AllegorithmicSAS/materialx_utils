import QtQuick 2.2
import Painter 1.0

PainterPlugin {
    
    MaterialXExport
    {
        id: window
    }

    /* called after the object has been instantiated. Used to execute script code at startup,
    once the full QML environment has been established. */
    Component.onCompleted:{
        //create a toolbar button
        var toolbar = alg.ui.addToolBarWidget( "tool-bar.qml" )
        toolbar.windowReference = window
    }
}

