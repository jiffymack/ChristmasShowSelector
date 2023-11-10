import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 806
    height: 600
    title: "MainWindow"

    ListView {
        width: parent.width
        height: parent.height

        model: ListModel {
            ListElement { text: "Selection 1" }
            ListElement { text: "Selection 2" }
            // Add more items as needed
        }

        delegate: Item {
            width: parent.width
            height: 50

            Rectangle {
                width: parent.width
                height: 50
                color: "lightblue"

                Text {
                    text: model.text
                    anchors.centerIn: parent
                    font.pixelSize: 22
                    horizontalAlignment: Text.AlignHCenter
                }
            }
        }
    }

    MenuBar {
        Menu {
            title: "File"
            MenuItem { text: "Open" }
            MenuItem { text: "Save" }
            // Add more menu items as needed
        }
    }

    StatusBar {
        // Define your status bar content here
    }
}
