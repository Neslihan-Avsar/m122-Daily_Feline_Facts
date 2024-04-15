# M122 - Daily Feline Facts

Dieses Python und Bash Projekt holt ein zufälliges Katzenfakt und publiziert es mit einem Discord WebHook auf deinen Discord Server nach Wahl!  
Während der Server an ist, schickt es einen Katzenfakt regelmässig. Katzenbild kann im Endprodukt inkludiert sein.

Embed WebHook Mockup Beispiel:  
![cat fact example](images/embed_webhook_mockup.png)

### Verwendungs Guide

###### 1. Erstelle einen Discord Webhook:  
  1.1. Gehe zu deinem Discord Server und stelle sicher, dass du die Berechtigungen hast, Integrationen zu verwalten.  
  1.2. Öffne die Servereinstellungen, unter Apps findest du "Integrationen", klicke auf "WebHooks".  
  1.3. Erstelle einen neuen WebHook und kopiere den Token, wenn du es benötigst (teile diesen Token mit niemanden, ausser es ist dir egal, wer eine Nachricht mit dem WebHook schreibt.)

###### 2. Richte dein Python Skript ein:
  2.1. Installiere Python mittels diesen Befehlen auf deiner Linux Maschine  
   ```bash
     $ sudo apt-get update
     $ sudo apt-get install python3.6
   ```
  2.2. Stelle sicher, dass du Python 3 hast mit `$ python3 --version`.  
  2.3. Unter [diesem Path](src/) solltest du zwei Skripte finden können. Lade sie herunter und tu es am besten in einer Directory namens "DailyFelineFacts" hinein.  
  2.4. Lade das Setup Skript `dff_setup.py` einmal und lasse es eine .cfg und eine .log Datei erstellen. Wenn du schon welche hast, wird es diese nicht überschreiben!  
  2.5. Nun kannst du in einem Texteditor die Variabeln (wie deine API nach Wahl oder dein Discord Token) verändern (solltest du auch, da es sonst nicht gehen wird...)

Manuell solltest du den Skript mit diesem Befehl laufen lassen können:
```bash
  $ python3 /home/DEIN_USERNAME/DailyFelineFacts/dff_api.py
```
Wenn du schon in dem Folder bist, wo der Skript vorhanden ist, kannst du auch nur `$ python3 dff_api.py` verwenden.  

> [!NOTE]  
> Obwohl die Setup Datei nicht mehr gebraucht wird nach dem ersten Mal, müssen alle anderen drei Dateien in einem gemeinsamen Ordner bleiben! Der Ordner kann auch einen anderen Namen haben, wenn du etwas ausser Katzen Fakten nehmen möchtest.

### To-Do

###### obligatorische Kriterien
- [x] Verwende [catfact.ninja API](https://catfact.ninja/) um Katzenfakten zu erhalten.
- [x] Erstelle einen Discord Server mit einem Kanal für Katzen Fakten und einen WebHook. [Link to Discord Server](https://discord.gg/GHsjrUvY2n)
- [x] Verarbeite die Rohdaten der Katzen Fakten
- [x] Verschicke es mittels dem Discord WebHook
- [x] Logge alle Resultate in einer LOG-Datei
- [ ] Finde einen Weg, wie man das Skript automatisch laufen lassen kann.

###### optionale Kriterien
- [x] Intergriere die Optionen in der CFG-Datei für Token, Aesthetik, etc.
- [x] Zufälliges Katzen Bild inkludiert von der Seite [Cat As A Service](https://cataas.com/)
- [x] Embed Nachricht Farbe und Text kann konfiguriert werden
