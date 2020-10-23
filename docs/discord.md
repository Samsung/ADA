Automatic Delivery Aid: Discord
================================

Wykonaj poniższe polecenia, aby utworzyć nową aplikację dla bota i dodać ją
do swojego serwera:
1. Zaloguj się do platformy Discord:  
   https://discordapp.com/
2. Przejdź do podstrony dla developerów aplikacji:  
   https://discordapp.com/developers/applications/
3. Kliknij na przycisk `New Application` i utwórz nową aplikację o nazwie `Ada`.
4. Powinieneś zostać przekierowany do konfiguracji aplikacji, jeżeli nie stało
   się to automatycznie, to kliknij na jej ikonę na liście aplikacji.
5. Przejdź do zakładki `Bot` i kliknij przyciski `Add Bot`.
6. **Wyłącz** w zakładce `Bot` poniższy przywilej:  
   Public bots can be added by anyone. When unchecked, only you can join this
   bot to servers.
7. Przejdź do zakładki OAuth2 i wygeneruj link do zaproszenia z następującymi
   uprawnieniami:
   * Scopes:
     * bot
   * Bot permissions:
     * Send Messages
     * Manage Messages
     * Embed Links
     * Read Message History
     * Mention Everyone
8. Kliknij przycisk `Copy` i wklej skopiowany link do przeglądarki.
9. Zaproś wygenerowanego bota na swój serwer.
10. Znów przejdź do zakładki `Bot` i skopiuj token bota, wklej go następnie do
    konfiguracji Ady.

W celu zapobiegnięcia pokazywania się niechcianej roli podczas wołania bota:
1. Przejdź do ustawień swojego serwera na podstronie `Server Settings`.
2. Przejdź do zakładki `Roles` w której znajduje się lista ról na serwerze.
3. Odszukaj rolę przypisaną do bota, standardowo będzie to rola `Ada`.
4. Zmień nazwę tej roli, na przykład na `bot`.

