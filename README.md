# M122 - Daily Feline Facts

Dieses Python und Bash Projekt holt ein zufälliges Katzenfakt und publiziert es mit einem Discord WebHook auf deinen Discord Server nach Wahl!  
Während der Server an ist, schickt es einen Katzenfakt regelmässig. Katzenbild kann im Endprodukt inkludiert sein.

Embed WebHook Mockup Beispiel:  
![cat fact example](images/embed_webhook_mockup.png)

### To-Do

###### obligatorische Kriterien
- [ ] Verwende [catfact.ninja API](https://catfact.ninja/) um Katzenfakten zu erhalten.
- [x] Erstelle einen Discord Server mit einem Kanal für Katzen Fakten und einen WebHook. [Link to Discord Server](https://discord.gg/GHsjrUvY2n)
- [ ] Verarbeite die Rohdaten der Katzen Fakten
- [ ] Verschicke es mittels dem Discord WebHook
- [ ] Logge alle Resultate in einer LOG-Datei

###### optionale Kriterien
- [ ] Intergriere die Optionen in der CFG-Datei für Intervalle
- [ ] Zufälliges Katzen Bild inkludiert von der Seite [Cat As A Service](https://cataas.com/)
- [ ] Embed Nachricht Farbe und Text kann konfiguriert werden
