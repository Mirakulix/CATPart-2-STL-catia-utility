# CATPart-2-STL-catia-utility

Die direkte Umwandlung von .CATPart zu .STL Dateien mit Python ist nicht möglich, da Python nicht nativ mit Catia interagieren kann. Allerdings kann Python mit Catia über die COM-Schnittstelle interagieren, um Catia zu steuern und die Umwandlung durchzuführen.


Dafür können .CATPart Dateien mit CATScript angesprochen werden. Ein zweites eigenständiges Skript ist zum Einfügen in die Catia Makros ebenfalls im Repository

# Verwendung von CATScript in CATIA

Folgen Sie diesen Schritten, um CATScript in CATIA zu verwenden:

1. Öffnen Sie **CATIA**.
2. Wählen Sie im Menü **Tools** die Option **Macros**.
3. Klicken Sie auf **Macros...**.
4. Im Dialogfeld **Macros** klicken Sie auf **Erstellen...**.
5. Geben Sie einen Namen für das Makro ein und wählen Sie **CATScript** als Typ.
6. Klicken Sie auf **Aufzeichnen**.
7. Führen Sie die gewünschten Aktionen in CATIA aus. Das Makro zeichnet diese auf.
8. Klicken Sie auf **Stop** in der Makro-Aufzeichnungsleiste, um die Aufzeichnung zu beenden.
9. Sie können das Makro nun ausführen, indem Sie es im Dialogfeld **Macros** auswählen und auf **Ausführen** klicken.

Um ein vorhandenes CATScript zu verwenden:

1. Klicken Sie auf **Öffnen...** im Dialogfeld **Macros** und navigieren Sie zu der Datei.
2. Sie können das Skript dann ausführen, indem Sie es auswählen und auf **Ausführen** klicken.

