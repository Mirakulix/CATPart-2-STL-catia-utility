# CATPart-2-STL-catia-utility

Die direkte Umwandlung von .CATPart zu .STL Dateien mit Python ist nicht möglich, da Python nicht nativ mit Catia interagieren kann. Allerdings kann Python mit Catia über die COM-Schnittstelle interagieren, um Catia zu steuern und die Umwandlung durchzuführen.


Dafür können .CATPart Dateien mit CATScript angesprochen werden. Ein zweites eigenständiges Skript ist zum Einfügen in die Catia Makros ebenfalls im Repository

Um CATScript in CATIA zu verwenden:

Öffnen Sie CATIA.
Wählen Sie im Menü "Tools" die Option "Macros".
Klicken Sie auf "Macros...".
Im Dialogfeld "Macros" klicken Sie auf "Erstellen...".
Geben Sie einen Namen für das Makro ein und wählen Sie "CATScript" als Typ.
Klicken Sie auf "Aufzeichnen".
Führen Sie die gewünschten Aktionen in CATIA aus. Das Makro zeichnet diese auf.
Klicken Sie auf "Stop" in der Makro-Aufzeichnungsleiste, um die Aufzeichnung zu beenden.
Sie können das Makro nun ausführen, indem Sie es im Dialogfeld "Macros" auswählen und auf "Ausführen" klicken.
Um ein vorhandenes CATScript zu verwenden, klicken Sie auf "Öffnen..." im Dialogfeld "Macros" und navigieren Sie zu der Datei. Sie können das Skript dann ausführen, indem Sie es auswählen und auf "Ausführen" klicken.
